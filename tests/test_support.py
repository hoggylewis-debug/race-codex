"""Support readiness follows OPERATOR's alias signal and never logs in."""
import json
import os
from pathlib import Path
import runpy
import unittest
from unittest.mock import patch

module = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'scripts/support-check.py'))
check = module['check']
ALIAS = module['SUPPORT_ALIAS']


class SupportTests(unittest.TestCase):
    def test_alias_is_sufficient_without_password_or_network(self):
        with patch.dict(os.environ, {'SUPPORT_EMAIL': ALIAS}, clear=True), \
             patch('socket.create_connection') as connection:
            self.assertTrue(check()['sales_support_ready'])
            self.assertTrue(check(smtp=True)['sales_support_ready'])
            connection.assert_not_called()

    def test_wrong_or_missing_alias_blocks_even_with_old_credentials(self):
        for address in ('', 'support@example.invalid', ALIAS + ' '):
            with self.subTest(address=address), patch.dict(os.environ, {
                    'SUPPORT_EMAIL': address, 'SUPPORT_EMAIL_PASSWORD': 'private_placeholder'}, clear=True), \
                 patch('socket.create_connection') as connection:
                result = check(smtp=True)
                self.assertFalse(result['sales_support_ready'])
                self.assertFalse(result['mailbox_login_attempted'])
                self.assertNotIn('private_placeholder', json.dumps(result))
                self.assertNotIn(address or 'not_an_actual_key', json.dumps(result))
                connection.assert_not_called()
