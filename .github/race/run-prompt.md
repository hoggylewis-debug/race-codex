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
- Your website: put everything it serves in the `site/` folder. Cloudflare Pages publishes that folder
  automatically when your session's work is pushed at the end of the session, so changes go live after
  each session, not during it. Your address is https://race-codex.pages.dev. You have no Cloudflare access and
  can't run deploys. Server-side code goes in a `functions/` folder at the repo root.
- STRIPE_SECRET_KEY may be set for your Stripe account. Check it exists; never print it. It isn't
  available to your live site, so prefer Stripe Payment Links, which need no secret key. If your site
  needs a secret or environment variable, add a request to REQUESTS.md and Lewis will set it.
- If something you need doesn't exist yet (a credential, an account), add a request to
  REQUESTS.md and work on something else.
