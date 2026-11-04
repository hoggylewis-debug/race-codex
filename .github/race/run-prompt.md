This is your scheduled daily session in the £50 AI Startup Race.

- Today: __DATE__ (day __DAY__ of 42). The race ends on Sunday 20 December 2026.
- Session started: __START_TIME__ UTC. Hard stop: __DEADLINE__ UTC. Run `date -u` to check the time.
  At 10 minutes before the hard stop, stop other work and update JOURNAL.md and STATE.md.
  If you are cut off before then, today's work may be lost.

Read BRIEF.md now and follow "Every session, in this order". Check REQUESTS.md for the
referee's answers before you plan anything.

Practical notes:
- You are running unattended. No human will reply during this session.
- Commit locally as often as you like, but don't push: you have no push access. Everything is
  saved and pushed for you at the end of the session as one commit.
- Don't edit anything in .github/. Changes there are thrown away at the end of the session.
- This repository is PUBLIC. Never write an API key, token, password or card number into
  any file, commit message or log. Read credentials only from environment variables.
  A commit that contains a secret is blocked and the whole session's work is discarded.
- Credentials that may be set as environment variables (check which ones exist; never print them):
  CLOUDFLARE_API_TOKEN and CLOUDFLARE_ACCOUNT_ID for deploying to Cloudflare Pages
  (e.g. `npx wrangler pages deploy`), and STRIPE_SECRET_KEY for your Stripe account.
- If something you need doesn't exist yet (a credential, an account), add a request to
  REQUESTS.md and work on something else.
