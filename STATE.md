# STATE: Codex — Site Handoff Kit

Last updated: 2026-11-09, approximately 17:32 UTC (day 4 of 45). Session work complete and handover saved early, before the 18:12 documentation cutoff / 18:22 hard stop. Race ends Sunday 20 December 2026. METRICS.md was updated Sunday 8 November; next weekly update 15 November.

## Business and live offer

- **Idea:** £5 GBP one-time offline website handover kit for freelance designers delivering small brochure/marketing sites. ZIP includes offline HTML builder, 40-point CSV checklist, five client email templates and instructions. Builder exports a seven-section guide with studio name/colour, delivery email and saved project files. HTML exports print to PDF. No subscription, DOCX export or remote AI generation.
- **Status:** Free tools LIVE; paid sales CLOSED. Live Stripe access and merchant verification are now provisioned. The approved £5 live product and price exist, both INACTIVE. No live Payment Link or Checkout Session created. SUPPORT_EMAIL/private inbox access are still missing; OPERATOR.md expressly says sales stay closed without the address. No sales have ever opened.
- **Audience:** Freelance website designers needing repeatable handovers. WordPress, Webflow, static/custom and generic starting points. Complex apps/shops need additional documentation. Willingness to pay unvalidated.
- **Main offer/preview:** https://race-codex.pages.dev — live guide preview and branded HTML sample, no signup. Paid kit adds offline reuse, project save/load, exports without Site Handoff Kit branding and supporting files.
- **Free acquisition resources:** /website-handover-template (blank text outline, printable fictional example and editable preset `/?example=juniper#try`), /website-handover-checklist and /website-handover-email-template. Details processed locally; no signup. None has established genuine demand, search rankings or conversions. The example is explicitly fictional, never a customer story.
- **Policies:** /privacy, /terms, /support. Trader identity/address supplied in OPERATOR appear only on these pages. Build reads SUPPORT_EMAIL as publishable contact if supplied. Today it is absent and the published pages contain no mailto address; no stale address to replace. Policies correctly say sales closed. Update payment data handling/refund support before enabling checkout.
- **Public repo:** https://github.com/hoggylewis-debug/race-codex . Sources are public as part of experiment. Paid value is packaging/workflow and commercial client-use licence; never promise exclusive/secret code.

## Numbers at day-4 close

| Measure | Value |
| --- | --- |
| Genuine visitors | Unknown; no confirmed genuine customer exposure |
| Cloudflare reported pageviews / estimated visits | 26 / 26 through 2026-11-09 17:30:47 UTC; includes operator checks |
| Sign-ups | 0 — no signup form |
| Paying customers | 0 — sales have never opened |
| Revenue | £0 |
| Spent | £0 |
| Budget left | £50 |
| Outreach sent | 0 |

Analytics range starts 6 November. Beacon deployed during day 2; earlier traffic unmeasured. Estimates are not unique people. Today's tests may ingest later. Do not call operator tests demand or claim downloads/copies (no event tracking).

`python scripts/metrics.py` now successfully queries the LIVE account: zero checkout sessions, paid orders and revenue. No kit Payment Link is configured yet. With no link the script can establish zero from an empty account; if any sessions exist without a configured link, it reports unattributed sessions and null kit revenue instead of claiming sales. Read-only live account check: charges_enabled=true, payouts_enabled=true, details_submitted=true. No test or real purchase made.

## ONE next task: finish the approved first-customer launch when support/access exists

1. Read current replies/check environment once for provisioned access. R-001–R-006 remain APPROVED. Run `python scripts/stripe-live.py` for GET-only access/catalogue status. No human replies during sessions. Do not re-request approved provisioning.
2. When SUPPORT_EMAIL/private inbox access exists, confirm the inbox works using its provider's IMAP/SMTP settings and SUPPORT_EMAIL_PASSWORD. Compare the address against all three published policy/support pages each session; republish the current one if different. Do not publish passwords or reuse Lewis's own contacts.
3. Follow docs/OPERATIONS.md: update policies for actual payments/support/refunds; configure the race Stripe merchant/support profile using OPERATOR details only where expected. Reuse the INACTIVE live product/price in docs/stripe-live.json. Activate them only when support/policies are ready, then create the approved £5 LIVE Payment Link with immediate card confirmation and redirect `/success?session_id={CHECKOUT_SESSION_ID}`. Save the public payment_link_id in docs/stripe-live.json or set PAYMENT_LINK_ID in the runner. No link exists yet. Never buy our own product.
4. Configure project secrets only on race-codex: live STRIPE_SECRET_KEY, PAYMENT_LINK_ID, PAYMENT_LINK_URL, PRIVATE_SUPPORT_EMAIL, MERCHANT_NAME. Change SALES_ENABLED only after every prerequisite; deploy and verify. The runner has a restricted live key (`rk_live_`), now supported by the server. Successful account/catalogue/session-list reads and product/price writes do not prove session retrieval or refund permissions; verify as applicable. No key has been deployed to Pages yet.
5. With dedicated Reddit access, recheck official platform/community rules and send exact approved R-004 post once. No new community, repeat post, DM, cold email or scraped contacts authorized. Do not bypass verification. No account/post created yet.
6. Measure genuine exposure, purchases and refunds. Prefer reaching a buyer over further template pages/features. No evidence supports ad spending yet. Seriously reconsider course if nobody pays by end of week 3 (26 November); idea changes after week 2 need approval.

## Approvals and outstanding access

REPLIES: R-001–R-005 APPROVED 6 November 16:18 UTC; R-006 APPROVED 7 November 18:07 UTC. Permission persists but does not supply missing credentials. OPEN reflects incomplete execution. R-005 is CLOSED/fulfilled.

- **R-001:** Live Stripe activation approved. LIVE restricted key and merchant verification now supplied. Inactive live catalogue prepared day 4. Remains OPEN until operational checkout; do not duplicate catalogue or request new activation approval.
- **R-002:** Private inbox/trader information approved. OPERATOR supplies identity/address, already published. SUPPORT_EMAIL and SUPPORT_EMAIL_PASSWORD missing; no email connector. Working private support/refunds route still required before sales.
- **R-003:** Dedicated Reddit account approved with exact bio in REQUESTS. REDDIT_USERNAME/REDDIT_PASSWORD absent; no posting connector/authenticated session. No account created.
- **R-004:** Exact one r/SideProject post approved subject to current rules. Text/destination in REQUESTS; not sent.
- **R-005:** Analytics fulfilled and operational. No other Cloudflare project/settings touched.
- **R-006:** Provisioning approved; Stripe portion completed day 4, support/Reddit outstanding. Progress noted in REQUESTS without a duplicate request.

## Technical handover

- Node 22, Python standard library. `npm ci`; `npm run build`; `npm run dev`. Dependencies and Chromium installed this session. Validation: `npm run test:unit`, `npm run test:ops`, `npm run test:browser`. `npm test` combines all three.
- Deploy: `npm run deploy` targets ONLY Pages project race-codex. Production https://race-codex.pages.dev . Latest deployment https://41c07e61.race-codex.pages.dev . No push access; end-session automation saves/pushes. No purchase made.
- Page source: scripts/build.mjs. Document resource: scripts/template-resource.mjs. Generated site: public/. Guide engine/shared fictional example: public/kit.js. Browser: public/app.js. Email tool: public/email-template.js. Styles: public/base.css.
- Product sources: product/checklist.json, client-emails.txt, START-HERE.txt. Build creates product/offline-builder.html, product/site-handoff-kit.zip and functions/_bundle.js. ZIP is embedded in a function, never in public/ (sources remain public in experiment repo).
- **New live operations:** scripts/stripe-live.py defaults to GET-only checks. `--prepare-catalogue` explicitly reconciles/creates only inactive product/price, with metadata, lookup key and idempotency; saves whitelisted public catalogue IDs to docs/stripe-live.json. Never creates a Payment Link/session/customer/charge, never activates purchases. Repeated real execution reuses catalogue. No secrets/customer data in config or output.
- **Restricted-key fix deployed:** functions/_sales.js accepts both sk_live_ and rk_live_ keys, while rejecting test/public keys. All other gates persist. functions/api/download.js requires SALES_ENABLED=true, live key/link, support/merchant settings and a complete paid LIVE Stripe session for configured link, £5 GBP subtotal. Re-verifies each download. wrangler.toml stays SALES_ENABLED=false. docs/stripe-test.json has historical test IDs only.
- Planned delivery: Stripe redirect to success with session reference. Real session references are private download credentials; never log/commit them. No independent delivery email/webhook yet. Keep private support working for access recovery before accepting money. Honour every refund request.
- Analytics: Cloudflare injects project beacon. scripts/analytics.py fetches ONLY race-codex and queries aggregate GraphQL with its siteTag. Never list account sites/query unfiltered account traffic. Never copy analytics token into source. public/_headers permits public beacons and sets strict CSP on success/API routes to prevent confirmation URLs reaching analytics. Offline kit has no analytics.
- **Day-4 validation:** 8 unit + 5 Python operations + 7 browser tests passed. Unit mocks cover restricted-key paid download and missing support/test/public-key rejection. Operations tests cover read-only mode, inactive catalogue creation/reuse, test-key refusal and honest no-link metrics. Browser tests cover existing guide/export/offline/save-load/mobile/policies/email/resource flows. Mocks do not prove a real payment.
- **Production browser:** Free preview works; all three policies HTTP 200 with experiment footer and no stale mailto; salesEnabled=false with no link, buy hidden, download 503, static ZIP 404; no page errors; no /success analytics beacon. No real payment, session retrieval or refund tested or claimed.

## Session rules

Read BRIEF/OPERATOR; then STATE, last three JOURNAL entries, REQUESTS/REPLIES; check numbers; pick ONE task; ship; append journal and rewrite state. Save no later than 10 minutes before hard stop; update METRICS Sundays.

Purchases/paid ads, first new contacts, social/marketplace accounts and live Stripe activation require approval. No answer in 24 hours means declined; existing approvals persist. Never cold email/text individuals or sole traders, scrape contacts, fake claims or refuse refunds. Every site discloses AI-run public experiment. Public repo: no secrets/customer records/private checkout references. Credentials only from environment. Shared Cloudflare: touch ONLY race-codex, never list/change other projects/settings. Do not edit .github/, BRIEF.md, OPERATOR.md or REPLIES.md.
