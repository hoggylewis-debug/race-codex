"""Support readiness must prove readable IMAP access and keep credentials private."""
import imaplib
import json
import os
from pathlib import Path
import runpy
import unittest
from unittest.mock import patch

check = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'scripts/support-check.py'))['check']


class SupportTests(unittest.TestCase):
    def setUp(self):
        self.environment = patch.dict(os.environ, {
            'SUPPORT_EMAIL': 'support@example.invalid',
            'SUPPORT_EMAIL_PASSWORD': 'private_placeholder',
            'SUPPORT_IMAP_HOST': 'imap.example.invalid',
            'SUPPORT_SMTP_HOST': 'smtp.example.invalid',
        }, clear=True)
        self.environment.start()
        self.addCleanup(self.environment.stop)

    def test_readonly_inbox_required_and_no_messages_read_or_sent(self):
        with patch('imaplib.IMAP4_SSL') as imap, patch('smtplib.SMTP_SSL') as smtp:
            inbox = imap.return_value.__enter__.return_value
            inbox.select.return_value = ('OK', [b'7'])
            result = check(smtp=True)
            self.assertTrue(result['sales_support_ready'])
            inbox.select.assert_called_once_with('INBOX', readonly=True)
            inbox.fetch.assert_not_called()
            inbox.search.assert_not_called()
            smtp.return_value.__enter__.return_value.sendmail.assert_not_called()
            smtp.return_value.__enter__.return_value.send_message.assert_not_called()

    def test_bad_auth_never_exposes_provider_response_or_credentials(self):
        with patch('imaplib.IMAP4_SSL') as imap:
            imap.return_value.__enter__.return_value.login.side_effect = imaplib.IMAP4.error('private_placeholder support@example.invalid')
            result = check()
            self.assertFalse(result['sales_support_ready'])
            self.assertNotIn('private_placeholder', json.dumps(result))
            self.assertNotIn('support@example.invalid', json.dumps(result))

    def test_login_without_readable_inbox_is_not_ready(self):
        with patch('imaplib.IMAP4_SSL') as imap:
            imap.return_value.__enter__.return_value.select.return_value = ('NO', [])
            self.assertFalse(check()['sales_support_ready'])

    def test_missing_credentials_fail_before_network(self):
        os.environ.pop('SUPPORT_EMAIL_PASSWORD')
        with patch('imaplib.IMAP4_SSL') as imap:
            self.assertEqual(check()['error'], 'missing_support_credentials')
            imap.assert_not_called()
