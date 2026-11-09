"""Offline checks for launch mutations and honest live-metric attribution."""
import contextlib
import io
import json
import os
from pathlib import Path
import runpy
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
LIVE_KEY = 'rk_' + 'live_' + 'unit_test_placeholder'


def execute(script, handler, args=(), env=None):
    output = io.StringIO()
    with patch.dict(os.environ, {'STRIPE_SECRET_KEY': LIVE_KEY, **(env or {})}, clear=True), \
         patch('sys.argv', [script, *args]), \
         patch('urllib.request.urlopen', side_effect=handler), \
         contextlib.redirect_stdout(output):
        runpy.run_path(str(ROOT / 'scripts' / script), run_name='__main__')
    return json.loads(output.getvalue())


class OperationsTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.previous_cwd = os.getcwd()
        os.chdir(self.directory.name)
        Path('docs').mkdir()

    def tearDown(self):
        os.chdir(self.previous_cwd)
        self.directory.cleanup()

    def test_preflight_is_read_only_and_does_not_expose_key_or_account(self):
        def handler(request, **_):
            self.assertEqual(request.get_method(), 'GET')
            path = urlparse(request.full_url).path
            data = {'data': [], 'has_more': False}
            if path == '/v1/account':
                data = {'charges_enabled': True, 'id': 'private_account_identifier'}
            return io.StringIO(json.dumps(data))
        result = execute('stripe-live.py', handler)
        self.assertTrue(result['restricted_key'])
        self.assertFalse(result['catalogue_prepared'])
        self.assertFalse(result['support_address_present'])
        self.assertFalse(Path('docs/stripe-live.json').exists())
        self.assertNotIn(LIVE_KEY, json.dumps(result))
        self.assertNotIn('private_account_identifier', json.dumps(result))

    def test_prepare_only_creates_inactive_catalogue_and_rerun_reuses_it(self):
        product = None
        price = None
        mutations = []

        def handler(request, **_):
            nonlocal product, price
            path = urlparse(request.full_url).path
            if request.get_method() == 'POST':
                fields = parse_qs(request.data.decode())
                mutations.append(path)
                self.assertIn(path, ['/v1/products', '/v1/prices'])
                self.assertEqual(fields['active'], ['false'])
                self.assertTrue(request.get_header('Idempotency-key'))
                if path == '/v1/products':
                    product = {'id': 'prod_fixture', 'active': False, 'livemode': True,
                        'metadata': {'race_project': 'race-codex', 'offer': 'handoff-kit-v1'}}
                    return io.StringIO(json.dumps(product))
                self.assertEqual(fields['currency'], ['gbp'])
                self.assertEqual(fields['unit_amount'], ['500'])
                self.assertNotIn('recurring', fields)
                price = {'id': 'price_fixture', 'active': False, 'livemode': True,
                    'currency': 'gbp', 'unit_amount': 500, 'type': 'one_time',
                    'lookup_key': 'race_codex_handoff_kit_gbp_500_v1'}
                return io.StringIO(json.dumps(price))
            if path == '/v1/account':
                return io.StringIO('{}')
            items = [product] if path == '/v1/products' and product else \
                    [price] if path == '/v1/prices' and price else []
            return io.StringIO(json.dumps({'data': items, 'has_more': False}))

        for _ in range(2):
            result = execute('stripe-live.py', handler, ['--prepare-catalogue'])
            self.assertTrue(result['catalogue_prepared'])
            self.assertFalse(result['price_active'])
        self.assertEqual(mutations, ['/v1/products', '/v1/prices'])
        saved = json.loads(Path('docs/stripe-live.json').read_text())
        self.assertEqual(set(saved), {'livemode', 'product_id', 'price_id', 'currency', 'unit_amount', 'note'})
        self.assertNotIn(LIVE_KEY, json.dumps(saved))

    def test_test_key_cannot_prepare_live_catalogue(self):
        with self.assertRaisesRegex(SystemExit, 'live secret or restricted'):
            execute('stripe-live.py', lambda *_args, **_kwargs: self.fail('No API call permitted'),
                ['--prepare-catalogue'], {'STRIPE_SECRET_KEY': 'rk_' + 'test_placeholder'})

    def test_empty_live_account_reports_verified_zero_without_link(self):
        result = execute('metrics.py', lambda *_args, **_kwargs:
            io.StringIO('{"data": [], "has_more": false}'))
        self.assertEqual(result['mode'], 'live')
        self.assertFalse(result['kit_payment_link_configured'])
        self.assertEqual(result['paid_orders'], 0)
        self.assertEqual(result['gross_gbp'], 0)

    def test_sessions_without_configured_link_are_not_claimed_as_race_revenue(self):
        output = io.StringIO()
        session = {'id': 'cs_fixture', 'payment_status': 'paid', 'amount_total': 500}
        with patch.dict(os.environ, {'STRIPE_SECRET_KEY': LIVE_KEY}, clear=True), \
             patch('urllib.request.urlopen', return_value=io.StringIO(json.dumps({'data': [session]}))), \
             contextlib.redirect_stdout(output), self.assertRaises(SystemExit):
            runpy.run_path(str(ROOT / 'scripts/metrics.py'), run_name='__main__')
        result = json.loads(output.getvalue())
        self.assertIsNone(result['paid_orders'])
        self.assertIsNone(result['gross_gbp'])
        self.assertEqual(result['unattributed_account_checkout_sessions'], 1)
        self.assertNotIn('cs_fixture', output.getvalue())


if __name__ == '__main__':
    unittest.main()
