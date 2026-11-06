This is your scheduled daily session in the £50 AI Startup Race.

- Today: __DATE__ (day __DAY__ of 45). The race ends on Sunday 20 December 2026.
- Session started: __START_TIME__ UTC. Hard stop: __DEADLINE__ UTC. Run `date -u` to check the time.
  At 10 minutes before the hard stop, stop other work and update JOURNAL.md and STATE.md.
  If you are cut off before then, today's work may be lost.

Read BRIEF.md and OPERATOR.md (the public trader details Lewis supplied) now and follow "Every session, in this order". Check REPLIES.md for the
referee's answers before you plan anything.

Practical notes:
- You are running unattended. No human will reply during this session.
- Commit locally as often as you like, but don't push: you have no push access. Everything is
  saved and pushed for you at the end of the session as one commit.
- Don't edit .github/, BRIEF.md, OPERATOR.md or REPLIES.md. Changes to them are thrown away at the end of the session.
- This repository is PUBLIC. Never write an API key, token, password or card number into
  any file, commit message or log. Read credentials only from environment variables.
  A commit that contains a secret is blocked and the whole session's work is discarded.
- Deploying: you can deploy mid-session and test your live site. Run
  `npx wrangler pages deploy <folder> --project-name race-codex`; CLOUDFLARE_API_TOKEN and
  CLOUDFLARE_ACCOUNT_ID are set as environment variables (never print them). Your address is
  https://race-codex.pages.dev. Set your own project's secrets with
  `npx wrangler pages secret put NAME --project-name race-codex`.
  The Cloudflare account is shared with the other contestant. Touch ONLY the Pages project `race-codex`:
  never list, change or delete any other project, token or setting on the account.
- STRIPE_SECRET_KEY may be set for your Stripe account. Check it exists; never print it. Prefer
  Stripe Payment Links, which need no secret key.
- If something you need doesn't exist yet (a credential, an account), add a request to
  REQUESTS.md and work on something else.
