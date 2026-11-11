# STATE: Codex — Site Handoff Kit

Last updated: 2026-11-11, approximately 15:13 UTC (day 6 of 45). Handover saved early, before today's 15:54 documentation cutoff / 16:04 hard stop. Race ends Sunday 20 December 2026. Next Sunday METRICS update: 15 November.

## Business and live offer

- **Idea:** £5 GBP one-time offline website handover kit for freelance designers delivering small brochure/marketing sites. ZIP: offline HTML builder, 40-point CSV checklist, five client emails and instructions. Builder exports a seven-section guide and delivery email, supports studio branding and project save/load. HTML exports print to PDF. No subscription, DOCX or remote AI generation. Willingness to pay unvalidated.
- **Status:** Free tools LIVE; paid sales CLOSED and have never opened. Verified LIVE Stripe account, inactive £5 product/price prepared. No live Payment Link or Checkout Session exists. No Stripe secret is deployed to Pages. SUPPORT_EMAIL/password exist, but IMAP and SMTP authentication fail. Reddit credentials are missing.
- **New verified blocker:** Stripe's customer-facing trading name, support email, support URL and website do not match this project; a support phone is present. OPERATOR prohibits publishing a phone number. No raw account values were printed/saved. R-007 requests exact correction through this account's Dashboard; Stripe's API documentation directs own-account profile changes there. No Dashboard access is available here. Merchant verification is complete, but public profile configuration is not.
- **Main offer:** https://race-codex.pages.dev — free guide preview/branded HTML sample without signup. Paid value: convenient offline reuse, studio-branded exports, saved projects and supporting files. Repository/source are public; do not promise exclusive code.
- **Resources:** /website-handover-template (blank text outline, explicitly fictional printable example, editable preset /?example=juniper#try), /website-handover-checklist, /website-handover-email-template. Project details processed locally. No evidence of rankings, genuine demand or conversions.
- **Policies:** /privacy, /terms, /support publish current SUPPORT_EMAIL; day-6 live checks match it. All say mailbox access temporarily unavailable and sales closed. Privacy covers GMX support enquiries and aims to delete resolved general enquiries within 90 days. No messages read/sent. OPERATOR trader identity/address appear only on these pages. Check address each session; if provider changes, update privacy provider/link too.

## Numbers at day-6 close

| Measure | Value |
| --- | --- |
| Genuine visitors | Unknown; no confirmed genuine customer exposure |
| Cloudflare pageviews / estimated visits | 38 / 38 through 2026-11-11 15:09:46 UTC, including operator checks |
| Sign-ups | 0 — no form |
| Paying customers | 0 — sales have never opened |
| Revenue / refunds | £0 / £0 |
| Spent / budget left | £0 / £50 |
| Outreach sent | 0 |

Analytics range starts 6 November; beacon deployed day 2, earlier traffic unmeasured. Visits are estimates, not unique people. No sample-download/copy tracking. Do not treat operator checks as demand. `python scripts/metrics.py` reads LIVE Stripe: zero account checkout sessions/orders/revenue, no Payment Link configured. If account sessions later exist without a configured kit link, metrics leaves them unattributed. No real/test purchase made. Stripe charges_enabled, payouts_enabled and details_submitted are all true.

## ONE next task: complete the approved first-customer launch once support/profile work

1. Read BRIEF/OPERATOR, STATE, last three JOURNAL entries, REQUESTS/REPLIES. Check environment/current support address and numbers. R-001–R-006 approved; R-007 pending. Do not re-request approved items.
2. Run `python scripts/launch-check.py --check-support` ONCE per session (instead of separately running support-check). It checks support, Stripe public profile and live policies, prints only status flags, exits 1 when false/unverified. Day-6 IMAP and SMTP authentication failed; cause unknown. No email was read/sent. Keep sales closed and do not repeatedly retry, bypass verification or reset credentials. Existing R-002/R-006 contain GMX repair instructions: provisioner checks POP3/IMAP enabled and supplies a valid app password through environment only.
3. R-007 supplies the exact own-account Dashboard profile correction: Site Handoff Kit trading name, project website/support URL, current SUPPORT_EMAIL, OPERATOR identity/address where required, public phone blank, policy URLs where offered. No raw profile values belong in logs/repo. Standard-account own-profile updates require Dashboard per official Stripe docs; do not misuse connected-account endpoints. Follow reply/access; do not open hosted checkout with the mismatched current profile.
4. Once private support works, update policies for actual Stripe payment/order handling, retention, access recovery and unconditional refunds. Remove mailbox-outage/closed-sale notices only when truthful. After reviewing each paid policy, add `data-sales-policy="ready"` to its article in build source, deploy and rerun the read-only report without another support login. The report cannot prove address correctness, payment/refund permission or delivery; check those separately.
5. Reuse catalogue in docs/stripe-live.json. Both product and price currently inactive. Activate only after support/profile/policies ready, then create approved £5 GBP one-time LIVE Payment Link, card-only immediate confirmation, metadata race_project=race-codex, redirect https://race-codex.pages.dev/success?session_id={CHECKOUT_SESSION_ID}. Save only public IDs/link URL. Never buy our product. Do not rerun catalogue preparation after configuring Payment Link without reviewing its catalogue-only writer, which overwrites the saved config.
6. Configure secrets ONLY on Pages race-codex: STRIPE_SECRET_KEY, PAYMENT_LINK_ID, PAYMENT_LINK_URL, PRIVATE_SUPPORT_EMAIL, MERCHANT_NAME. Set SALES_ENABLED=true only after prerequisites, deploy and verify status/checkout/download gates. Restricted-key paid-session retrieval/refund permissions remain untested. No key is deployed yet.
7. With dedicated Reddit access, recheck official platform/community rules and send exact approved R-004 once. No other community, repeated post, DM, cold email or scraped contacts authorized. No Reddit account/post currently exists.
8. Prioritise genuine buyer exposure over more features/resources. No ads/spending evidence. Seriously consider changing course if nobody pays by end of week 3 (26 November); idea changes after week 2 require approval.

## Approvals/access

REPLIES: R-001–R-005 approved 6 November 16:18 UTC; R-006 approved 7 November 18:07 UTC. Approval persists, working access is separate. R-005 CLOSED/fulfilled; R-001–R-004/R-006 OPEN because execution incomplete. R-007 submitted 11 November for newly verified public Stripe profile correction, £0, awaiting reply (normal 24-hour rule applies).

- R-001: live merchant verification/key supplied, inactive catalogue prepared day 4; checkout incomplete.
- R-002: trader details published; mailbox supplied day 5 but authentication fails on days 5 and 6.
- R-003/R-004: dedicated Reddit account/exact r/SideProject post approved; no credentials/posting connector.
- R-005: fulfilled, scoped analytics read/public beacons working.
- R-006: Stripe supplied, mailbox unusable, Reddit missing. Do not submit another duplicate provisioning request.
- R-007: Dashboard correction now concretely specified; no profile change attempted from runner.

## Technical handover

- Node 22/Python stdlib. `npm ci`; `npm run build`; `npm run dev`. `npm test` combines unit, Python operations and browser suites. Today's only code changes are the new Python preflight/tests; no app or product changes/deployment needed.
- Production https://race-codex.pages.dev ; latest deployment https://77c85fbe.race-codex.pages.dev . Deploy `npm run deploy` targets ONLY race-codex. No push access; end-session automation saves/pushes.
- scripts/build.mjs generates pages/policies; scripts/template-resource.mjs supplies document resource; public/kit.js guide engine/fixed fictional preset; public/app.js builder; public/email-template.js email tool. product/ contains sources/generated offline builder/ZIP; functions/_bundle.js embeds ZIP. No public static ZIP.
- NEW scripts/launch-check.py: GET-only Stripe account/public policy checks. Default skips another mailbox login; null mailbox status blocks readiness. --check-support imports support checker for real IMAP/SMTP proof without reading/sending mail. Prints only booleans/blocker names, never raw account values/errors/secrets. Checks profile matches and absent public phone, current page support addresses, explicit paid-policy marker and absent outage notice. Does not activate anything or prove hosted checkout/delivery/refund permissions. README/operations describe limits and marker review.
- scripts/support-check.py: IMAP SSL/read-only INBOX and optional --smtp auth; known GMX/Gmail/Yahoo/Outlook hosts. Unknown providers require SUPPORT_IMAP_HOST/SUPPORT_SMTP_HOST; SMTP supports 465 SSL or 587 STARTTLS via SUPPORT_SMTP_PORT. No messages read/sent or raw provider errors logged. Day-6 result: authentication_or_protocol_failed IMAP; authentication_failed SMTP; sales_support_ready=false.
- scripts/stripe-live.py: default GET-only; --prepare-catalogue reconciles inactive catalogue with metadata/lookup key/idempotency; never creates links/charges. Public catalogue IDs in docs/stripe-live.json. Catalogue-only writer does NOT preserve future link fields: review before reuse after launch.
- functions/_sales.js permits sk_live_ and rk_live_, requires SALES_ENABLED=true, live link, private support/merchant. Download independently requires LIVE complete/paid session for configured link, GBP/£5 subtotal; re-verifies each download, no-store. wrangler.toml remains SALES_ENABLED=false.
- Payment redirect is delivery; no independent delivery email/webhook. Keep private support working for recovery. Real checkout-session references grant download access: never log/commit them. Honour every refund request.
- scripts/analytics.py fetches ONLY race-codex project and aggregate GraphQL with its siteTag; never list sites/query unfiltered traffic. Public beacon allowed; success/API routes strict CSP to prevent private session URLs reaching analytics. On success page an attempted script may appear but fails with csp; check actual transmissions. Offline kit has no analytics.
- Day-6 validation: all 16 Python operations tests pass (9 existing + 7 new). Actual preflight reads live Stripe/all policies and fails on documented blockers; /api/status salesEnabled=false. App/browser suites unchanged, not rerun today. Last day-5 full suite: 8 unit + 9 operations + 7 browser pass, live preview works, policies 200/footer, download 503, static ZIP 404, no success analytics beacon. No real payment/refund tested or claimed.

## Session rules

Follow BRIEF session order. Save JOURNAL and rewrite STATE at least 10 minutes before hard stop. Update METRICS Sundays. Purchases/ads, first contacts, accounts/live activation gated; existing approvals persist. No cold email/text, scraping, false claims/refused refunds. Site discloses AI-run public experiment. No secrets, private account/customer data or checkout references in this public repo. Only race-codex Cloudflare project; never list/change others. Never edit .github/, BRIEF.md, OPERATOR.md or REPLIES.md.
