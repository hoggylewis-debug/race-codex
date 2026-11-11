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
            'SUPPORT_EMAIL': 'support@example.invalid',
        }, clear=True)
        self.env.start()
        self.addCleanup(self.env.stop)

    def handler(self, request, **_):
        self.assertEqual(request.get_method(), 'GET')
        if request.full_url == 'https://api.stripe.com/v1/account':
            return io.StringIO(json.dumps({
                'charges_enabled': True, 'payouts_enabled': True, 'details_submitted': True,
                'business_profile': {'name': 'Site Handoff Kit',
                    'support_email': 'support@example.invalid', 'support_url': ROOT + '/support',
                    'url': ROOT + '/'},
            }))
        self.assertIn(request.full_url, [ROOT + '/' + name for name in ('terms', 'privacy', 'support')])
        return io.BytesIO(b'<article data-sales-policy="ready">support@example.invalid</article>')

    def test_read_only_and_skipped_mailbox_is_not_a_pass(self):
        with patch('urllib.request.urlopen', side_effect=self.handler), patch('imaplib.IMAP4_SSL') as imap:
            result = check()
        self.assertFalse(result['prerequisites_ready'])
        self.assertEqual(result['blockers'], ['support_imap_and_smtp_verified'])
        imap.assert_not_called()
        self.assertNotIn('private_placeholder', json.dumps(result))
        self.assertNotIn('support@example.invalid', json.dumps(result))

    def test_profile_mismatches_are_flags_only(self):
        flags = launch['profile_checks']({'business_profile': {
            'name': 'private unrelated name', 'support_phone': 'private phone',
            'support_email': 'private address',
        }}, 'support@example.invalid')
        self.assertFalse(flags['stripe_trading_name_matches'])
        self.assertFalse(flags['stripe_support_email_matches'])
        self.assertFalse(flags['stripe_public_support_phone_absent'])
        self.assertNotIn('private', json.dumps(flags))

    def test_support_is_checked_and_failure_blocks_readiness(self):
        with patch('urllib.request.urlopen', side_effect=self.handler), patch('imaplib.IMAP4_SSL') as imap, \
             patch('smtplib.SMTP_SSL'):
            # No password provided: actual support checker must fail before login.
            result = check(check_support=True)
        self.assertFalse(result['prerequisites_ready'])
        self.assertIs(result['checks']['support_imap_and_smtp_verified'], False)
        imap.assert_not_called()

    def test_ready_requires_actual_support_check_and_every_profile_and_policy_flag(self):
        with patch.dict(os.environ, {'SUPPORT_EMAIL_PASSWORD': 'private_placeholder',
                 'SUPPORT_IMAP_HOST': 'imap.example.invalid',
                 'SUPPORT_SMTP_HOST': 'smtp.example.invalid'}), \
             patch('urllib.request.urlopen', side_effect=self.handler), \
             patch('imaplib.IMAP4_SSL') as imap, patch('smtplib.SMTP_SSL') as smtp:
            inbox = imap.return_value.__enter__.return_value
            inbox.select.return_value = ('OK', [b'0'])
            result = check(check_support=True)
        self.assertTrue(result['prerequisites_ready'])
        self.assertEqual(result['blockers'], [])
        inbox.select.assert_called_once_with('INBOX', readonly=True)
        inbox.fetch.assert_not_called()
        smtp.return_value.__enter__.return_value.sendmail.assert_not_called()

    def test_outage_notice_blocks_even_a_reviewed_policy(self):
        def handler(request, **kwargs):
            if 'api.stripe.com' in request.full_url:
                return self.handler(request, **kwargs)
            return io.BytesIO(b'<article data-sales-policy="ready">support@example.invalid '
                b'Mailbox access is temporarily unavailable</article>')
        with patch('urllib.request.urlopen', side_effect=handler):
            result = check()
        for page in ('terms', 'privacy', 'support'):
            self.assertIn(page + '_no_mailbox_outage_notice', result['blockers'])

    def test_unreviewed_policies_cannot_pass_when_outage_text_is_removed(self):
        def handler(request, **kwargs):
            if 'api.stripe.com' in request.full_url:
                return self.handler(request, **kwargs)
            return io.BytesIO(b'<article>support@example.invalid</article>')
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
