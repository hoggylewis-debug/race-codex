#!/usr/bin/env python3
"""Read aggregate Web Analytics for race-codex ONLY. No account-wide site listing.
The UTC range defaults to the race start through now; accepts --start and --end.
Empty data is not evidence of zero visitors: beacon blockers and setup gaps apply.
"""
import argparse
import datetime as dt
import json
import os
import urllib.error
import urllib.request

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--start', default='2026-11-06T00:00:00Z')
parser.add_argument('--end', default=dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))
args = parser.parse_args()
for value in (args.start, args.end):
    try:
        dt.datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
    except ValueError:
        raise SystemExit('Dates must use UTC YYYY-MM-DDTHH:MM:SSZ.') from None
if args.start >= args.end:
    raise SystemExit('Start must precede end.')
account = os.environ.get('CLOUDFLARE_ACCOUNT_ID')
token = os.environ.get('CLOUDFLARE_API_TOKEN')
if not account or not token:
    raise SystemExit('Cloudflare credentials missing; analytics unavailable.')
headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}

def read(url, payload=None):
    request = urllib.request.Request(url, headers=headers,
        data=json.dumps(payload).encode() if payload is not None else None)
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        raise SystemExit('Cloudflare request failed with HTTP ' + str(error.code)) from None
    except (urllib.error.URLError, TimeoutError):
        raise SystemExit('Cloudflare unavailable; analytics not measured.') from None

project = read('https://api.cloudflare.com/client/v4/accounts/' + account + '/pages/projects/race-codex')
if not project.get('success'):
    raise SystemExit('Could not read race-codex project configuration.')
config = (project.get('result') or {}).get('build_config') or {}
site = config.get('web_analytics_tag')
if not site:
    raise SystemExit('race-codex has no configured analytics tag; visitors unmeasured.')
query = '''query($account: string, $site: string, $start: Time, $end: Time) {
 viewer { accounts(filter: {accountTag: $account}) {
  rumPageloadEventsAdaptiveGroups(limit: 1, filter: {
   siteTag: $site, datetime_geq: $start, datetime_lt: $end
  }) { count sum { visits } }
 } }
}'''
data = read('https://api.cloudflare.com/client/v4/graphql', {
    'query': query, 'variables': {'account': account, 'site': site, 'start': args.start, 'end': args.end}})
if data.get('errors'):
    # Avoid printing account identifiers or any raw service response.
    raise SystemExit('Project-scoped analytics query failed; check Analytics read permission/schema.')
accounts = ((data.get('data') or {}).get('viewer') or {}).get('accounts')
if not accounts:
    raise SystemExit('No analytics account access; visitors unmeasured.')
rows = accounts[0].get('rumPageloadEventsAdaptiveGroups') or []
print(json.dumps({
    'project': 'race-codex', 'start_utc_inclusive': args.start, 'end_utc_exclusive': args.end,
    'reported_pageviews': sum(row.get('count', 0) for row in rows),
    'reported_visits': sum((row.get('sum') or {}).get('visits', 0) for row in rows),
    'data_present': bool(rows),
    'note': 'Aggregate beacon estimates, not unique people or customers. Includes operator tests. Empty data does not establish zero traffic; earlier pages had no working beacon.'
}, indent=2))
