#!/usr/bin/env python3
"""Print aggregate Stripe metrics without writing or printing customer records.
The key is read from the environment. Test and live results are clearly separated.
"""
import json
import os
import urllib.error
import urllib.parse
import urllib.request

key = os.environ.get('STRIPE_SECRET_KEY')
if not key:
    raise SystemExit('STRIPE_SECRET_KEY is missing; no payment metrics available.')
mode = 'live' if '_live_' in key else 'test' if '_test_' in key else 'unknown'
link = os.environ.get('PAYMENT_LINK_ID')
if not link and mode in ('test', 'live'):
    try:
        with open('docs/stripe-' + mode + '.json') as config:
            link = json.load(config).get('payment_link_id')
    except (FileNotFoundError, KeyError):
        pass
if mode == 'unknown':
    raise SystemExit('Unrecognised Stripe key mode; no payment metrics queried.')

def records(endpoint, params=None):
    params = dict(params or {}, limit=100)
    for _ in range(1000):
        request = urllib.request.Request(
            'https://api.stripe.com/v1/' + endpoint + '?' + urllib.parse.urlencode(params),
            headers={'Authorization': 'Bearer ' + key})
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                data = json.load(response)
        except urllib.error.HTTPError as error:
            raise SystemExit('Stripe metrics request failed with HTTP ' + str(error.code)) from None
        yield from data['data']
        if not data.get('has_more') or not data['data']:
            return
        params['starting_after'] = data['data'][-1]['id']
    raise SystemExit('Pagination safety limit reached; metrics incomplete.')

sessions = list(records('checkout/sessions', {'payment_link': link} if link else {}))
if not link and sessions:
    print(json.dumps({
        'mode': mode, 'kit_payment_link_configured': False,
        'unattributed_account_checkout_sessions': len(sessions),
        'paid_orders': None, 'unique_paying_identities_before_refunds': None,
        'gross_gbp': None,
        'note': 'Account has sessions but no kit Payment Link is configured. Set PAYMENT_LINK_ID before attributing any orders or revenue to the race.'
    }, indent=2))
    raise SystemExit(0)
paid = [s for s in sessions if s.get('status') == 'complete' and s.get('payment_status') == 'paid'
        and s.get('currency') == 'gbp' and s.get('amount_subtotal') == 500
        and s.get('livemode') == (mode == 'live')]
identities = set()
missing_identity = 0
for session in paid:
    email = (session.get('customer_details') or {}).get('email')
    if email:
        identities.add(email.strip().casefold())
    elif session.get('customer'):
        identities.add('customer:' + session['customer'])
    else:
        missing_identity += 1
intent_ids = {s['payment_intent'] for s in paid if s.get('payment_intent')}
refunds = 0
fully_refunded_intents = set()
# Only read charges if there are orders to reconcile; all output stays aggregate.
if intent_ids:
    for charge in records('charges'):
        if charge.get('payment_intent') in intent_ids and charge.get('currency') == 'gbp':
            refunds += charge.get('amount_refunded', 0)
            if charge.get('refunded'):
                fully_refunded_intents.add(charge['payment_intent'])
print(json.dumps({
    'mode': mode,
    'kit_payment_link_configured': bool(link),
    'scope': 'configured kit Payment Link' if link else 'empty account; no checkout sessions exist',
    'is_race_revenue': mode == 'live',
    'checkout_sessions': len(sessions),
    'paid_orders': len(paid),
    'unique_paying_identities_before_refunds': len(identities),
    'paid_orders_without_identity': missing_identity,
    'gross_gbp': round(sum(s.get('amount_total', 0) for s in paid) / 100, 2),
    'refunds_gbp': round(refunds / 100, 2),
    'fully_refunded_orders': len(fully_refunded_intents),
    'net_revenue_before_stripe_fees_gbp': round((sum(s.get('amount_total', 0) for s in paid)-refunds)/100, 2),
    'visitors': 'See scripts/analytics.py for project-scoped beacon estimates; historical traffic before day 2 is unmeasured',
    'sign_ups': 0,
    'note': 'No email signup form. Email-based identity deduplication is approximate. Review refunds before claiming unique paying customers. Test payments never count.'
}, indent=2))
