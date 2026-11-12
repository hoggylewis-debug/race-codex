#!/usr/bin/env python3
"""Read-only launch checks; exit 1 when prerequisites are incomplete.

Checks Stripe and published policies. Support readiness is the exact alias
match required by OPERATOR.md; the human trader handles support and refunds.
No mailbox login, customer records or raw account values are used or output.
This report does not enable sales or prove real payment/delivery permissions.
"""
import argparse
import json
import os
import urllib.error
import urllib.request

ROOT = 'https://race-codex.pages.dev'
SUPPORT_ALIAS = 'sitehandoff.support@gmx.co.uk'


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
    support = SUPPORT_ALIAS
    key = os.environ.get('STRIPE_SECRET_KEY', '')
    checks['support_alias_matches'] = os.environ.get('SUPPORT_EMAIL') == SUPPORT_ALIAS
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
    return {
        'checks': checks,
        'prerequisites_ready': all(value is True for value in checks.values()),
        'blockers': [name for name, ready in checks.items() if ready is not True],
        'note': 'Read-only preflight, not proof of checkout or delivery. Support/refunds are handled by the human trader; no mailbox login attempted. No sales settings changed.',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-support', action='store_true', help='Deprecated; alias is always checked without a mailbox login.')
    result = check(parser.parse_args().check_support)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['prerequisites_ready'] else 1)
