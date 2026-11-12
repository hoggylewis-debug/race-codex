#!/usr/bin/env python3
"""Check the operator-provisioned support alias without any network or login.

OPERATOR.md: Lewis alone reads the inbox and handles refunds. An exact
SUPPORT_EMAIL match confirms provisioning. Never use inbox credentials.
--smtp is retained as an inert compatibility option for old runbooks.
"""
import argparse
import json
import os

SUPPORT_ALIAS = 'sitehandoff.support@gmx.co.uk'


def check(smtp=False):
    ready = os.environ.get('SUPPORT_EMAIL') == SUPPORT_ALIAS
    return {
        'support_alias_matches': ready,
        'sales_support_ready': ready,
        'support_handled_by': 'human_trader',
        'mailbox_login_attempted': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--smtp', action='store_true', help='Deprecated; no login is performed.')
    outcome = check(parser.parse_args().smtp)
    print(json.dumps(outcome, indent=2))
    raise SystemExit(0 if outcome['sales_support_ready'] else 1)
