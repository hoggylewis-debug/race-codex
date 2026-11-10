#!/usr/bin/env python3
"""Verify support access without reading messages, sending email or logging secrets.

Run at the start of every session. Exit 0 means IMAP authentication and a read-only
INBOX selection succeeded. --smtp also verifies outgoing authentication.
Unknown providers require explicit SUPPORT_IMAP_HOST / SUPPORT_SMTP_HOST settings.
"""
import argparse
import imaplib
import json
import os
import smtplib
import ssl

PROVIDERS = {
    'gmx.com': ('imap.gmx.com', 'mail.gmx.com', 465),
    'gmx.co.uk': ('imap.gmx.com', 'mail.gmx.com', 465),
    'gmail.com': ('imap.gmail.com', 'smtp.gmail.com', 465),
    'googlemail.com': ('imap.gmail.com', 'smtp.gmail.com', 465),
    'yahoo.com': ('imap.mail.yahoo.com', 'smtp.mail.yahoo.com', 465),
    'yahoo.co.uk': ('imap.mail.yahoo.com', 'smtp.mail.yahoo.com', 465),
    'outlook.com': ('outlook.office365.com', 'smtp.office365.com', 587),
    'hotmail.com': ('outlook.office365.com', 'smtp.office365.com', 587),
}


def check(smtp=False):
    address = os.environ.get('SUPPORT_EMAIL', '').strip()
    password = os.environ.get('SUPPORT_EMAIL_PASSWORD', '')
    result = {'imap': 'not_checked', 'smtp': 'not_checked', 'sales_support_ready': False}
    if not address or not password:
        return {**result, 'error': 'missing_support_credentials'}
    provider = PROVIDERS.get(address.rsplit('@', 1)[-1].lower(), ('', '', 465))
    imap_host = os.environ.get('SUPPORT_IMAP_HOST') or provider[0]
    smtp_host = os.environ.get('SUPPORT_SMTP_HOST') or provider[1]
    if not imap_host or (smtp and not smtp_host):
        return {**result, 'error': 'unknown_provider_set_explicit_hosts'}
    try:
        with imaplib.IMAP4_SSL(imap_host, 993, timeout=20) as inbox:
            inbox.login(address, password)
            status, _ = inbox.select('INBOX', readonly=True)
            result['imap'] = 'ok' if status == 'OK' else 'inbox_unavailable'
    except imaplib.IMAP4.error:
        result['imap'] = 'authentication_or_protocol_failed'
    except (OSError, TimeoutError):
        result['imap'] = 'connection_failed'
    if smtp:
        try:
            port = int(os.environ.get('SUPPORT_SMTP_PORT') or provider[2])
            if port not in (465, 587):
                return {**result, 'error': 'smtp_port_must_be_465_or_587'}
            client = smtplib.SMTP_SSL if port == 465 else smtplib.SMTP
            with client(smtp_host, port, timeout=20) as outgoing:
                if port == 587:
                    outgoing.starttls(context=ssl.create_default_context())
                outgoing.login(address, password)
                result['smtp'] = 'ok'
        except smtplib.SMTPAuthenticationError:
            result['smtp'] = 'authentication_failed'
        except (OSError, smtplib.SMTPException, ValueError):
            result['smtp'] = 'connection_or_protocol_failed'
    result['sales_support_ready'] = result['imap'] == 'ok' and (not smtp or result['smtp'] == 'ok')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--smtp', action='store_true')
    outcome = check(parser.parse_args().smtp)
    print(json.dumps(outcome, indent=2))
    raise SystemExit(0 if outcome['sales_support_ready'] else 1)
