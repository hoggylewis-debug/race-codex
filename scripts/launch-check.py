#!/usr/bin/env python3
"""Read-only launch checks; exit 1 when prerequisites are incomplete.

By default checks Stripe and the published policies, without another mailbox
login. Use --check-support once per session to also prove IMAP/SMTP access.
No raw account fields, customer records, addresses or credentials are output.
This report does not enable sales or prove real payment/refund permissions.
"""
import argparse
import json
import os
from pathlib import Path
import runpy
import urllib.error
import urllib.request

ROOT = 'https://race-codex.pages.dev'


def stripe_account(key):
    request = urllib.request.Request('https://api.stripe.com/v1/account',
        headers={'Authorization': 'Bearer ' + key})
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def policy_page(name):
    request = urllib.request.Request(ROOT + '/' + name,
        headers={'User-Agent': 'SiteHandoffKit-LaunchCheck/1.0'})
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read(500_000).decode('utf-8')


def profile_checks(account, support):
    profile = account.get('business_profile') or {}
    return {
        'stripe_charges_enabled': account.get('charges_enabled') is True,
        'stripe_payouts_enabled': account.get('payouts_enabled') is True,
        'stripe_details_submitted': account.get('details_submitted') is True,
        'stripe_trading_name_matches': profile.get('name') == 'Site Handoff Kit',
        'stripe_support_email_matches': bool(support) and profile.get('support_email') == support,
        'stripe_support_url_matches': profile.get('support_url') == ROOT + '/support',
        'stripe_website_matches': (profile.get('url') or '').rstrip('/') == ROOT,
        # OPERATOR prohibits publishing a phone number. Never print its value.
        'stripe_public_support_phone_absent': not profile.get('support_phone'),
    }


def check(check_support=False):
    checks = {}
    support = os.environ.get('SUPPORT_EMAIL', '').strip()
    key = os.environ.get('STRIPE_SECRET_KEY', '')
    checks['support_address_configured'] = bool(support)
    checks['live_stripe_key_configured'] = key.startswith(('sk_live_', 'rk_live_'))
    if checks['live_stripe_key_configured']:
        try:
            checks.update(profile_checks(stripe_account(key), support))
            checks['stripe_account_readable'] = True
        except (urllib.error.URLError, OSError, ValueError):
            checks['stripe_account_readable'] = False
    for name in ('terms', 'privacy', 'support'):
        try:
            html = policy_page(name)
            checks[name + '_reachable'] = True
            checks[name + '_support_address_current'] = bool(support) and support in html
            # Explicit marker must be added only after reviewing paid-sales copy.
            # A missing outage notice alone cannot establish launch readiness.
            checks[name + '_paid_policy_reviewed'] = 'data-sales-policy="ready"' in html
            checks[name + '_no_mailbox_outage_notice'] = 'Mailbox access is temporarily unavailable' not in html
        except (urllib.error.URLError, OSError, ValueError):
            checks[name + '_reachable'] = False
    if check_support:
        support_check = runpy.run_path(str(Path(__file__).with_name('support-check.py')))['check']
        checks['support_imap_and_smtp_verified'] = support_check(smtp=True)['sales_support_ready']
    else:
        checks['support_imap_and_smtp_verified'] = None
    return {
        'checks': checks,
        'prerequisites_ready': all(value is True for value in checks.values()),
        'blockers': [name for name, ready in checks.items() if ready is not True],
        'note': 'Read-only preflight, not proof of checkout, delivery or refunds. A skipped mailbox check is not a pass. No sales settings changed.',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-support', action='store_true')
    result = check(parser.parse_args().check_support)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['prerequisites_ready'] else 1)
