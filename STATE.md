# STATE: Codex — Site Handoff Kit

Last updated: 2026-11-07, approximately 14:02 UTC (day 2 of 45). Handover saved early, before the 14:43 documentation cutoff and 14:53 hard stop. Race ends Sunday 20 December 2026. Next session is Sunday: update METRICS.md then.

## Business and live offer

- **Idea:** A £5 GBP one-time offline website handover kit for freelance designers delivering small brochure/marketing sites. Includes an offline HTML builder, 40-point CSV checklist, five client email templates and instructions. Builder exports a seven-section client guide with studio name/colour, a delivery email and saved project files. HTML exports can be printed to PDF. No subscription or remote AI generation.
- **Status:** Free tools LIVE; paid sales CLOSED. Live activation is APPROVED, but Stripe credential remains TEST-only, merchant verification is incomplete and SUPPORT_EMAIL is empty. OPERATOR.md expressly says sales stay closed without that address. Do not enable sales or claim customers.
- **Target:** Freelance website designers needing a repeatable client handover. WordPress, Webflow, static/custom and generic starting points; complex apps/shops need extra documentation. Willingness to pay is unvalidated.
- **Main offer/preview:** https://race-codex.pages.dev — live guide preview and branded HTML sample, no signup. Paid kit removes Site Handoff Kit branding from client exports and adds offline reuse/project save-load and supporting files.
- **Free acquisition pages:** /website-handover-checklist and **/website-handover-email-template** (new day 2). The latter personalises one final-delivery email in the browser, with copy and text download, and leads to the guide preview/£5 kit. Both are linked in the footer and sitemap. Organic visibility is not proven.
- **Policies:** /privacy, /terms, /support. Supplied trader identity/address now published on these pages only. No support address yet; build reads SUPPORT_EMAIL when provided. Current policies accurately say sales closed; update payment handling before opening checkout.
- **Public repository:** https://github.com/hoggylewis-debug/race-codex . Source/product artifacts are public as part of the experiment. Paid value is convenient packaging and a commercial client-use licence; never promise secret/exclusive code.

## Numbers at day-2 close

| Measure | Value |
| --- | --- |
| Genuine visitors | Unknown; historical traffic unmeasured and no genuine visitor evidence yet |
| Analytics query | No records through 2026-11-07 14:01:24 UTC; beacon only deployed during day 2, ingestion may lag |
| Sign-ups | 0 — no signup form |
| Paying customers | 0 — sales have never opened |
| Revenue | £0 |
| Spent | £0 |
| Budget left | £50 |
| Outreach sent | 0 |

`python scripts/metrics.py` confirms provided Stripe key is TEST mode: 0 sessions, 0 payments. Test numbers do not establish live account metrics. Read-only Stripe account check: charges_enabled=false, details_submitted=false. No test or real purchase was made.

**Analytics now works:** R-005 fulfilled. Project build_config already contained analytics setup; day-2 deployment injects the Cloudflare beacon. Privacy and CSP updated. Actual browser confirmed public-page analytics requests with HTTP 204 acceptance and strict CSP blocking on /success. `python scripts/analytics.py` fetches only race-codex then queries aggregate pageviews/visits filtered by its siteTag. No account-wide sites/metrics are read. Visits are estimates, not unique people/customers; operator checks count and must not be reported as demand. Empty results do not establish zero visitors. No copy/download event tracking exists.

## One next task: complete the approved first-customer launch

1. Check REPLIES and environment for R-006 provisioning. Existing approvals persist; do not ask for live activation or the exact Reddit post again. No human responds during sessions.
2. If live Stripe and working private inbox become available, follow docs/OPERATIONS.md to create the approved £5 LIVE Payment Link, update payment/privacy/refund copy, configure merchant/support details, set secrets only on race-codex, enable SALES_ENABLED and deploy. Do not buy our product. Honour every refund. Merchant verification requiring a human cannot be performed by the agent.
3. If dedicated Reddit account access becomes available, recheck current official community/platform rules and send the exact approved R-004 post once. No other communities, repeat posts, DMs, cold emails or contact scraping are authorized. No account/post has yet been created. Do not bypass account verification.
4. Measure genuine exposure and purchases. Prefer reaching a buyer over adding more features. Rethink course seriously if nobody pays by end of week 3 (26 November); idea changes after week 2 need approval.

## Approvals and access blockers

REPLIES.md: **R-001 through R-005 all APPROVED 2026-11-06 16:18 UTC.** Approval is not the same as provisioned access. R-001 through R-004 remain OPEN because execution is incomplete; R-005 is CLOSED/fulfilled.

- **R-001:** Live Stripe sales approved. STRIPE_SECRET_KEY exists but is TEST mode; account charges disabled and details unsubmitted. Need human verification/live key.
- **R-002:** Private inbox and trader information approved. OPERATOR.md now provides identity and address (published); SUPPORT_EMAIL and SUPPORT_EMAIL_PASSWORD are empty. No inbox/email connector exists. Need a dedicated working support route, not Lewis's personal/business contacts.
- **R-003:** Dedicated Reddit account creation approved with exact bio in REQUESTS. REDDIT_USERNAME and REDDIT_PASSWORD are empty, and no authenticated posting tool/session exists. Need permitted account access. No account created.
- **R-004:** One exact public r/SideProject launch/feedback post approved, subject to current rules. Exact title/body/destination in REQUESTS. Not sent.
- **R-005:** Free analytics for race-codex approved and now operational. No other account project or setting touched.
- **R-006 (new, OPEN):** Requests execution of the already-approved access provisioning: live Stripe, dedicated support inbox, dedicated Reddit login through environment/tool. £0 upfront, no new outreach. Do not put secrets in replies or repo.

## Technical handover

- Node 22. `npm ci`; `npm run build`; `npm run dev`. Dependencies installed in day 2; browser Chromium installed.
- Deploy: `npm run deploy` → **only** Pages project race-codex. Production: https://race-codex.pages.dev . Day-2 deployment: https://f824ce04.race-codex.pages.dev . No push access; end-session automation saves/pushes. No purchases made.
- HTML source: scripts/build.mjs. Generated site: public/. Existing guide engine: public/kit.js and public/app.js. New email tool: public/email-template.js. Style: public/base.css. Build publishes trader details only on the three policy/support pages, and reads SUPPORT_EMAIL as a publishable address if supplied.
- Paid product sources: product/checklist.json, client-emails.txt, START-HERE.txt. Build makes product/offline-builder.html, product/site-handoff-kit.zip and functions/_bundle.js. Paid ZIP is bundled in a server function, never placed in public/ (although source is public in the experiment repo).
- Download gate: functions/_sales.js and functions/api/download.js. Requires SALES_ENABLED=true, a live key, configured live link, support/merchant values and a completed paid live Stripe session for that link, £5 GBP subtotal. Every download re-verifies. wrangler.toml remains SALES_ENABLED=false. Test Stripe setup is in docs/stripe-test.json; do not confuse it with live setup.
- Analytics: Cloudflare injects the project beacon on deploy. public/_headers permits it globally and adds strict CSP on confirmation/download paths. /success may contain an injected script in HTML, but actual browser verifies it is blocked with failure=csp and sends no analytics beacon. Keep these protections when editing headers. Never store its configured token in repo source.
- Payment delivery is planned via checkout redirect /success?session_id={CHECKOUT_SESSION_ID}. Session references are private download credentials; never log/commit them. No independent delivery email/webhook exists. Keep private support working for recovery before accepting money.
- Validation: day 2 passed **8 unit and 6 browser tests**, covering payment gates, ZIP, offline operation, personalisation, mobile, download/save/load, policy routes and email local processing/export/clipboard-denial fallback. Local tests do not prove real live payment. Live browser confirmed 200 on main/email/policy pages, email updates, no page exceptions, public beacons and success-page CSP blocking. Status salesEnabled=false; download 503; static ZIP 404.
- Operations/activation/refunds/metrics: docs/OPERATIONS.md. Initial hypothesis/sources: docs/RESEARCH.md. Day-2 acquisition hypothesis is unvalidated; no demand claims or testimonials.

## Session rules

Read BRIEF/OPERATOR and follow the ordered routine: STATE, last three JOURNAL entries, REQUESTS/REPLIES; check numbers; choose one task; ship; journal and rewrite state. Save by ten minutes before the hard stop. Update METRICS on Sundays (next 8 November).

All purchases/paid ads, first new contacts, social/marketplace accounts and Stripe live activation need approval. Existing approvals persist. No response after 24 hours is declined. Refunds always honoured. Every site must disclose the AI-run public experiment. Public repo: no credentials, customer/order records or private checkout links. Credentials only from environment. Cloudflare shared account: touch ONLY race-codex, never list or alter other projects/settings. Do not edit .github/, BRIEF.md, OPERATOR.md or REPLIES.md.
