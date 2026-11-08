# STATE: Codex — Site Handoff Kit

Last updated: 2026-11-08, approximately 14:20 UTC (day 3 of 45). Today's work is complete and handover saved early, before the 15:01 documentation cutoff / 15:11 hard stop. Race ends Sunday 20 December 2026. Sunday METRICS.md is updated; next weekly update 15 November.

## Business and live offer

- **Idea:** £5 GBP one-time offline website handover kit for freelance designers delivering small brochure/marketing sites. ZIP includes offline HTML builder, 40-point CSV checklist, five client email templates and instructions. Builder exports a seven-section guide with studio name/colour, delivery email and saved project files. HTML exports print to PDF. No subscription, DOCX export or remote AI generation.
- **Status:** Free tools LIVE; paid sales CLOSED. Live activation approved, but Stripe credential remains TEST-only, merchant verification incomplete, and SUPPORT_EMAIL absent. OPERATOR.md expressly says sales stay closed without it. No sales have ever opened.
- **Audience:** Freelance website designers needing repeatable handovers. WordPress, Webflow, static/custom and generic starting points. Complex apps/shops need additional documentation. Willingness to pay unvalidated.
- **Main offer/preview:** https://race-codex.pages.dev — live guide preview and branded HTML sample, no signup. Paid kit adds offline reuse, project save/load, exports without Site Handoff Kit branding and supporting files.
- **New day-3 resource:** https://race-codex.pages.dev/website-handover-template — blank downloadable text outline, completed printable fictional HTML example and fixed preset `/?example=juniper#try` to edit that example in the free builder. Names, dates and completed checks explicitly fictional; not a client story. Resource targets document-template searches; no indexing/ranking/search volume or buyer response established. Linked from homepage/footer/sitemap/README.
- **Other free acquisition resources:** /website-handover-checklist and /website-handover-email-template. Email tool personalises one final-delivery email locally with copy/text download. None has demonstrated genuine demand yet.
- **Policies:** /privacy, /terms, /support. Trader identity/address supplied in OPERATOR appear only on these pages. Build reads SUPPORT_EMAIL as publishable contact if supplied. Policies correctly say sales closed; update payment data handling/refund support before enabling checkout.
- **Public repo:** https://github.com/hoggylewis-debug/race-codex . Sources are public as part of experiment. Paid value is packaging/workflow and commercial client-use licence; never promise exclusive/secret code.

## Numbers at day-3 close

| Measure | Value |
| --- | --- |
| Genuine visitors | Unknown; no confirmed genuine customer exposure |
| Cloudflare reported pageviews / estimated visits | 16 / 16 through 2026-11-08 14:18:55 UTC; includes operator checks |
| Sign-ups | 0 — no signup form |
| Paying customers | 0 — sales have never opened |
| Revenue | £0 |
| Spent | £0 |
| Budget left | £50 |
| Outreach sent | 0 |

Analytics range starts 6 November. Beacon deployed during day 2; earlier traffic unmeasured. Estimates are not unique people. Today's tests may ingest later. Do not call operator tests demand or claim downloads/copies (no event tracking). Sunday METRICS.md records these limits.

`python scripts/metrics.py`: provided Stripe key TEST mode, 0 sessions/payments. Cannot independently query live account transactions with that key. Read-only account check day 3: charges_enabled=false, payouts_enabled=false, details_submitted=false. No test or real purchase made.

## ONE next task: execute the approved first-customer launch when access exists

1. Read current replies/check environment once for provisioned access. R-006 now APPROVED. Do not re-request existing approval or repeat the provisioning request. No human replies during sessions.
2. With live Stripe and working dedicated private inbox, follow docs/OPERATIONS.md: create the approved £5 LIVE Payment Link, update payment/privacy/refund wording, configure merchant/support details, set secrets only on race-codex, enable SALES_ENABLED and deploy. Never buy our own product. Human merchant verification cannot be done by the agent. Refunds always honoured.
3. With dedicated Reddit access, recheck current official platform/community rules and send exact approved R-004 post once. No other communities, repeat posts, DMs, cold emails or scraped contacts authorized. Do not bypass verification. No account/post yet created.
4. Measure genuine exposure and purchases. Prefer reaching a buyer over more template pages or builder features. No evidence yet supports spending on ads. Seriously reconsider course if nobody pays by end of week 3 (26 November); idea changes after week 2 need approval.

## Approvals and outstanding access

REPLIES: R-001–R-005 APPROVED 6 November 16:18 UTC; **R-006 APPROVED 7 November 18:07 UTC**. Permission persists but is not provisioned access. OPEN requests reflect incomplete execution, not missing approval. R-005 is CLOSED/fulfilled.

- **R-001:** Live Stripe activation approved. Key exists but TEST mode; account incomplete/charges disabled. Need live key and human verification.
- **R-002:** Private inbox/trader information approved. OPERATOR supplies trader identity/address, already published. SUPPORT_EMAIL and SUPPORT_EMAIL_PASSWORD missing; no email connector. Need dedicated working private support/refunds route. Do not use Lewis's own contacts.
- **R-003:** Dedicated Reddit account approved with exact bio in REQUESTS. REDDIT_USERNAME/REDDIT_PASSWORD absent; no posting connector/authenticated session. No account created.
- **R-004:** Exact one r/SideProject post approved subject to current rules. Text/destination in REQUESTS; not sent.
- **R-005:** Analytics fulfilled, operational. No other Cloudflare project/settings touched.
- **R-006:** Approved provisioning of the above missing access. Status recorded in REQUESTS on day 3; do not re-request.

## Technical handover

- Node 22. `npm ci`; `npm run build`; `npm run dev`. Dependencies and Playwright Chromium installed this session. Operations/activation/refunds/measurement: docs/OPERATIONS.md; hypothesis/sources: docs/RESEARCH.md.
- Deploy: `npm run deploy` targets ONLY Pages project race-codex. Production https://race-codex.pages.dev . Latest deployment https://601d0c22.race-codex.pages.dev . No push access; end-session automation saves/pushes. No purchase made.
- Page source: scripts/build.mjs. New resource copy/text outline: scripts/template-resource.mjs. Generated site: public/. Guide engine + shared fictional `exampleProject`: public/kit.js. Browser behaviour: public/app.js. Email tool: public/email-template.js. Styles: public/base.css.
- Build generates /website-handover-template plus public/examples/website-handover.html (noindex, fictional, printable) and website-handover-template.txt. Fixed builder preset reads only `example=juniper`; never load arbitrary project details from URLs. Plain resource and downloads work without JS.
- Product sources: product/checklist.json, client-emails.txt, START-HERE.txt. Build makes product/offline-builder.html, product/site-handoff-kit.zip and functions/_bundle.js. ZIP is bundled in a function, never in public/ (sources remain public in the experiment repo).
- Download gates: functions/_sales.js and functions/api/download.js. Require SALES_ENABLED=true, live key/link, support/merchant values and a complete paid LIVE Stripe session for the configured link, £5 GBP subtotal. Re-verifies every download. wrangler.toml remains SALES_ENABLED=false. docs/stripe-test.json has test IDs only.
- Planned delivery: Stripe redirect /success?session_id={CHECKOUT_SESSION_ID}. Real session references are private download credentials; never log/commit them. No independent delivery email/webhook yet. Keep private support working for recovery before accepting money.
- Analytics: Cloudflare injects the configured project beacon. scripts/analytics.py fetches ONLY race-codex and queries aggregate GraphQL with its siteTag. No account-wide sites listing or unfiltered traffic. Never copy configured token into source. public/_headers permits public beacons and sets strict CSP on success/API routes to prevent confirmation URLs reaching analytics. Offline product has no analytics.
- **Day-3 validation:** 8 unit + 7 browser tests passed. Covers escaping/payment gates/ZIP, guide editing/export, offline operation/save-load with no network, mobile, policy pages, email local processing/export/clipboard-denial fallback and new template/download/example/preset flow. Unknown preset/query client data rejected. Local mocks do not prove real payment.
- **Live browser:** New resource/example/text/sitemap all HTTP 200; fixed preset and preview work; phone width fits; no page errors; salesEnabled=false; download 503; static ZIP 404; no /success analytics beacon. Reviewed mobile screenshot (temporary /tmp only). No live payment tested or claimed.

## Session rules

Read BRIEF/OPERATOR; then STATE, last three JOURNAL entries, REQUESTS/REPLIES; check numbers; pick ONE task; ship; append journal and rewrite state. Save no later than 10 minutes before hard stop; update METRICS Sundays.

Purchases/paid ads, first new contacts, social/marketplace accounts and live Stripe activation require approval. No answer in 24 hours means declined; existing approvals persist. Never cold email/text individuals or sole traders, scrape contacts, fake claims or refuse refunds. Every site discloses AI-run public experiment. Public repo: no secrets/customer records/private checkout references. Credentials only from environment. Shared Cloudflare: touch ONLY race-codex, never list/change other projects/settings. Do not edit .github/, BRIEF.md, OPERATOR.md or REPLIES.md.
