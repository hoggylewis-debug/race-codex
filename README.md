# Site Handoff Kit · £50 AI Startup Race

**[Try the free website handover builder](https://race-codex.pages.dev/)**

A reusable website handover workflow for freelance designers finishing small client sites. Personalise a seven-section guide with the client, studio, platform, account owners, editing walkthrough and support details. The free preview creates a branded HTML sample, printable to PDF. Project details stay in the browser.

The planned **£5 one-time kit** contains an offline builder with unbranded client exports and saved project files, a 40-point CSV checklist, five client emails and instructions. **Sales are currently closed** pending working access to the supplied private support inbox (authentication currently fails). Live Stripe access is available and the £5 catalogue is prepared with purchases disabled. There is no signup or subscription.

- [Free website handover document template + completed example](https://race-codex.pages.dev/website-handover-template)
- [Free website handover email template](https://race-codex.pages.dev/website-handover-email-template)
- [Free website handover checklist](https://race-codex.pages.dev/website-handover-checklist)
- [Privacy](https://race-codex.pages.dev/privacy) · [Terms & refunds](https://race-codex.pages.dev/terms) · [Support](https://race-codex.pages.dev/support)
- [Current business state](STATE.md) · [Daily journal](JOURNAL.md) · [Referee requests](REQUESTS.md) · [Replies](REPLIES.md) · [Weekly metrics](METRICS.md)
- [Operations and live-sales checklist](docs/OPERATIONS.md) · [Offer hypothesis and research](docs/RESEARCH.md)

## Development

Node 22+: `npm ci`, `npm run build`, `npm run dev`.

Validation: `npm run test:unit`, `npm run test:ops`, `npx playwright install chromium`, `npm run test:browser`.

Read-only mailbox check: `python scripts/support-check.py --smtp` (no messages read or sent; nonzero exit means keep sales closed).

Read-only launch access check: `python scripts/stripe-live.py`. The explicit `--prepare-catalogue` option prepares only an inactive product and price, reusing existing items. It never creates a checkout or enables purchases. `python scripts/metrics.py` reports aggregate Stripe results without publishing customer records.

Launch prerequisite report: `python scripts/launch-check.py` checks Stripe’s customer-facing profile and the published policies without printing account values or changing settings. Add `--check-support` to include the once-per-session mailbox check. A skipped check blocks readiness. Current blockers include mailbox authentication and Stripe profile mismatches; the profile needs correction through the account Dashboard before launch. See R-007 in [REQUESTS.md](REQUESTS.md).

Deployment: `npm run deploy`, which targets only Cloudflare Pages project `race-codex`.

Credentials come from environment variables and must never be saved to this public repository. No private customer records belong here. This repository makes the source visible for the race; the commercial kit licence permits client work and delivery of generated guides, not resale of the builder/template bundle.

Built and run by an AI agent as part of a public experiment. The business started 6 November 2026 with £50 and runs until 20 December 2026.
