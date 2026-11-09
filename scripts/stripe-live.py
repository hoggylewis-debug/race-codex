#!/usr/bin/env python3
"""Check live launch access; optionally prepare the approved, INACTIVE £5 catalogue.

Never creates a Payment Link, Checkout Session, customer or payment. Prints only
aggregate/status data. The saved config contains public catalogue IDs, not keys.
R-001 approved this offer. Sales still require a working dedicated support inbox.
"""
import argparse
import json
import os
from pathlib import Path
import urllib.error
import urllib.parse
import urllib.request

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--prepare-catalogue', action='store_true')
args = parser.parse_args()
key = os.environ.get('STRIPE_SECRET_KEY', '')
if not key.startswith(('sk_live_', 'rk_live_')):
    raise SystemExit('A live secret or restricted Stripe key is required; no changes made.')


def api(endpoint, fields=None, idempotency=None):
    headers = {'Authorization': 'Bearer ' + key}
    if idempotency:
        headers['Idempotency-Key'] = idempotency
    request = urllib.request.Request('https://api.stripe.com/v1/' + endpoint,
        headers=headers, data=urllib.parse.urlencode(fields).encode() if fields is not None else None)
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        # Never print raw API responses, headers, credentials or customer data.
        raise SystemExit('Stripe request failed with HTTP ' + str(error.code) + '; no sales enabled.') from None
    except (urllib.error.URLError, TimeoutError):
        raise SystemExit('Stripe unavailable; no sales enabled. Re-run to reconcile catalogue state.') from None


def all_records(endpoint):
    after = None
    for _ in range(100):
        query = {'limit': 100}
        if after:
            query['starting_after'] = after
        data = api(endpoint + ('&' if '?' in endpoint else '?') + urllib.parse.urlencode(query))
        yield from data['data']
        if not data.get('has_more'):
            return
        after = data['data'][-1]['id']
    raise SystemExit('Catalogue pagination limit reached; no further changes made.')


account = api('account')
products = [p for p in all_records('products')
    if p.get('metadata', {}).get('race_project') == 'race-codex'
    and p.get('metadata', {}).get('offer') == 'handoff-kit-v1']
if len(products) > 1:
    raise SystemExit('Multiple matching products; review before making changes.')
product = products[0] if products else None
if args.prepare_catalogue and not product:
    product = api('products', {
        'name': 'Site Handoff Kit — complete website handover kit',
        'description': 'Offline HTML handover builder, 40-point CSV checklist, five client email templates and instructions. One-time download for freelance website designers.',
        'active': 'false',
        'url': 'https://race-codex.pages.dev/#pricing',
        'metadata[race_project]': 'race-codex',
        'metadata[offer]': 'handoff-kit-v1',
    }, 'race-codex-live-product-v1')

price = None
if product:
    prices = [p for p in all_records('prices?product=' + urllib.parse.quote(product['id']))
        if p.get('lookup_key') == 'race_codex_handoff_kit_gbp_500_v1']
    if len(prices) > 1:
        raise SystemExit('Multiple matching prices; review before making changes.')
    price = prices[0] if prices else None
    if args.prepare_catalogue and not price:
        price = api('prices', {
            'product': product['id'], 'currency': 'gbp', 'unit_amount': 500,
            'active': 'false', 'lookup_key': 'race_codex_handoff_kit_gbp_500_v1',
            'metadata[race_project]': 'race-codex',
        }, 'race-codex-live-price-v1')
    if price and (price.get('currency') != 'gbp' or price.get('unit_amount') != 500
                  or price.get('type') != 'one_time' or not price.get('livemode')):
        raise SystemExit('Catalogue price does not match the approved live £5 offer.')

links = [p for p in all_records('payment_links')
    if p.get('metadata', {}).get('race_project') == 'race-codex']
if args.prepare_catalogue and product and price:
    # Whitelist public catalogue fields. No URLs granting downloads or account data.
    Path('docs/stripe-live.json').write_text(json.dumps({
        'livemode': True, 'product_id': product['id'], 'price_id': price['id'],
        'currency': 'gbp', 'unit_amount': 500,
        'note': 'Catalogue only. No Payment Link created. Initially inactive; do not enable purchases before private support and policies are ready.',
    }, indent=2) + '\n')

print(json.dumps({
    'mode': 'live', 'restricted_key': key.startswith('rk_live_'),
    'charges_enabled': bool(account.get('charges_enabled')),
    'payouts_enabled': bool(account.get('payouts_enabled')),
    'details_submitted': bool(account.get('details_submitted')),
    'catalogue_prepared': bool(product and price),
    'product_active': product.get('active') if product else None,
    'price_active': price.get('active') if price else None,
    'tagged_payment_links': len(links),
    'active_tagged_payment_links': sum(bool(p.get('active')) for p in links),
    'support_address_present': bool(os.environ.get('SUPPORT_EMAIL', '').strip()),
    'support_password_present': bool(os.environ.get('SUPPORT_EMAIL_PASSWORD')),
    'reddit_credentials_present': bool(os.environ.get('REDDIT_USERNAME') and os.environ.get('REDDIT_PASSWORD')),
    'note': 'Presence does not verify inbox access or key permissions for every operation. This script never enables sales.',
}, indent=2))
