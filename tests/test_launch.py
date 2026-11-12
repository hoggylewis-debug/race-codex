"""Launch preflight must fail closed and never expose merchant credentials."""
import io
import json
import os
from pathlib import Path
import runpy
import unittest
from unittest.mock import patch
from urllib.error import URLError

launch = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'scripts/launch-check.py'))
check = launch['check']
ROOT = launch['ROOT']


class LaunchTests(unittest.TestCase):
    def setUp(self):
        self.env = patch.dict(os.environ, {
            'STRIPE_SECRET_KEY': 'rk_' + 'live_private_placeholder',
            'SUPPORT_EMAIL': 'sitehandoff.support@gmx.co.uk',
        }, clear=True)
        self.env.start()
        self.addCleanup(self.env.stop)

    def handler(self, request, **_):
        self.assertEqual(request.get_method(), 'GET')
        if request.full_url == 'https://api.stripe.com/v1/account':
            return io.StringIO(json.dumps({
                'charges_enabled': True, 'payouts_enabled': True, 'details_submitted': True,
                'business_profile': {'name': 'Site Handoff Kit',
                    'support_email': 'sitehandoff.support@gmx.co.uk', 'support_url': ROOT + '/support',
                    'url': ROOT + '/'},
            }))
        self.assertIn(request.full_url, [ROOT + '/' + name for name in ('terms', 'privacy', 'support')])
        return io.BytesIO(b'<article data-sales-policy="ready">sitehandoff.support@gmx.co.uk</article>')

    def test_read_only_ready_with_alias_without_mailbox_credentials(self):
        with patch('urllib.request.urlopen', side_effect=self.handler), patch('socket.create_connection') as connection:
            result = check()
        self.assertTrue(result['prerequisites_ready'])
        self.assertEqual(result['blockers'], [])
        connection.assert_not_called()
        self.assertNotIn('private_placeholder', json.dumps(result))
        self.assertNotIn('sitehandoff.support@gmx.co.uk', json.dumps(result))

    def test_profile_mismatches_are_flags_only(self):
        flags = launch['profile_checks']({'business_profile': {
            'name': 'private unrelated name', 'support_phone': 'private phone',
            'support_email': 'private address',
        }}, 'sitehandoff.support@gmx.co.uk')
        self.assertFalse(flags['stripe_trading_name_matches'])
        self.assertFalse(flags['stripe_support_email_matches'])
        self.assertFalse(flags['stripe_public_support_phone_absent'])
        self.assertNotIn('private', json.dumps(flags))

    def test_wrong_support_alias_blocks_without_any_login(self):
        with patch.dict(os.environ, {'SUPPORT_EMAIL': 'old@example.invalid'}), \
             patch('urllib.request.urlopen', side_effect=self.handler), patch('socket.create_connection') as connection:
            result = check(check_support=True)
        self.assertFalse(result['prerequisites_ready'])
        self.assertEqual(result['blockers'], ['support_alias_matches'])
        connection.assert_not_called()

    def test_legacy_option_cannot_trigger_a_mailbox_login(self):
        with patch('urllib.request.urlopen', side_effect=self.handler), patch('socket.create_connection') as connection:
            result = check(check_support=True)
        self.assertTrue(result['prerequisites_ready'])
        connection.assert_not_called()

    def test_outage_notice_blocks_even_a_reviewed_policy(self):
        def handler(request, **kwargs):
            if 'api.stripe.com' in request.full_url:
                return self.handler(request, **kwargs)
            return io.BytesIO(b'<article data-sales-policy="ready">sitehandoff.support@gmx.co.uk '
                b'Mailbox access is temporarily unavailable</article>')
        with patch('urllib.request.urlopen', side_effect=handler):
            result = check()
        for page in ('terms', 'privacy', 'support'):
            self.assertIn(page + '_no_mailbox_outage_notice', result['blockers'])

    def test_unreviewed_policies_cannot_pass_when_outage_text_is_removed(self):
        def handler(request, **kwargs):
            if 'api.stripe.com' in request.full_url:
                return self.handler(request, **kwargs)
            return io.BytesIO(b'<article>sitehandoff.support@gmx.co.uk</article>')
        with patch('urllib.request.urlopen', side_effect=handler):
            result = check()
        for page in ('terms', 'privacy', 'support'):
            self.assertIn(page + '_paid_policy_reviewed', result['blockers'])

    def test_network_failure_redacts_raw_provider_error(self):
        error = URLError('private_placeholder')
        with patch('urllib.request.urlopen', side_effect=error):
            result = check()
        self.assertFalse(result['prerequisites_ready'])
        self.assertFalse(result['checks']['stripe_account_readable'])
        self.assertNotIn('private_placeholder', json.dumps(result))
