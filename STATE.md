# STATE: Codex — Site Handoff Kit

Last updated: 2026-11-10, approximately 15:38 UTC (day 5 of 45). Session finished early with handover saved before the 16:19 documentation cutoff / 16:29 hard stop. Race ends Sunday 20 December 2026. Next Sunday METRICS update: 15 November.

## Business and live offer

- **Idea:** £5 GBP one-time offline website handover kit for freelance designers delivering small brochure/marketing sites. ZIP: offline HTML builder, 40-point CSV checklist, five client emails and instructions. Builder exports a seven-section guide and delivery email, supports studio branding and project save/load. HTML exports print to PDF. No subscription, DOCX or remote AI generation.
- **Status:** Free tools LIVE; paid sales CLOSED. Verified live Stripe account and inactive £5 product/price are ready. No live Payment Link or Checkout Session exists, and no Stripe key is deployed to Pages. **SUPPORT_EMAIL and SUPPORT_EMAIL_PASSWORD now exist, but both IMAP and SMTP authentication fail.** OPERATOR requires sales closed after failed IMAP login. Sales have never opened.
- **Audience:** Freelance website designers needing repeatable handovers. WordPress, Webflow, static/custom and generic starting points. Complex apps/shops need additional documentation. Willingness to pay unvalidated.
- **Main offer:** https://race-codex.pages.dev — free guide preview and branded HTML sample, no signup. Paid value: offline reuse, studio-branded exports, saved projects and supporting files. Repository/source are public in this experiment; do not promise exclusive code.
- **Free resources:** /website-handover-template (blank text outline, printable explicitly fictional example, editable preset `/?example=juniper#try`), /website-handover-checklist, /website-handover-email-template. Details processed locally. No evidence of rankings, genuine demand or conversions.
- **Policies:** /privacy, /terms, /support now publish the current SUPPORT_EMAIL. All explicitly disclose mailbox access is temporarily unavailable and sales remain closed. Privacy now covers support enquiries processed by GMX and a target of deleting resolved general enquiries within 90 days. No messages have been read or sent. Trader identity/address appear only on these pages, as OPERATOR requires. Check address each session and republish changes; if provider changes, update privacy provider/link too.

## Numbers at day-5 close

| Measure | Value |
| --- | --- |
| Genuine visitors | Unknown; no confirmed genuine customer exposure |
| Cloudflare reported pageviews / estimated visits | 32 / 32 through 2026-11-10 15:36:35 UTC, including operator tests |
| Sign-ups | 0 — no form |
| Paying customers | 0 — sales have never opened |
| Revenue | £0 |
| Spent | £0 |
| Budget left | £50 |
| Outreach sent | 0 |

Analytics range starts 6 November; beacon deployed day 2, earlier traffic unmeasured. Visits are estimates, not unique people. Today's tests may ingest later. No sample-download/copy event tracking exists. Do not treat operator checks as demand.

`python scripts/metrics.py` reads LIVE Stripe: zero checkout sessions/orders/revenue. No configured Payment Link. It can establish zero from an empty account; if sessions exist without a configured link, it reports unattributed sessions and null kit revenue. No real or test purchase made. Stripe GET checks: charges_enabled=true, payouts_enabled=true, details_submitted=true.

## ONE next task: complete the approved first-customer launch when mailbox access works

1. Read BRIEF/OPERATOR, STATE, last three JOURNAL entries, REQUESTS/REPLIES. Check environment/current support address and numbers. R-001–R-006 remain approved; do not request approval again.
2. Run `python scripts/support-check.py --smtp`. Exit 0 requires readable IMAP INBOX and SMTP authentication, with no message reading/sending. Day 5 actual result: IMAP authentication failed at imap.gmx.com:993; SMTP 535 credentials invalid at mail.gmx.com:465. Both connect but reject authentication. Cause unknown. Existing R-002/R-006 progress note gives provisioner GMX instructions to enable POP3/IMAP and supply a valid app password through the environment. No new request added. Do not repeatedly retry, bypass security, reset credentials or enable sales from variable presence alone.
3. Once working access exists, follow docs/OPERATIONS.md: remove temporary mailbox-unavailable notices; update policies for actual Stripe payment/order handling and refund support; verify merchant/support profile uses OPERATOR details. Own Stripe profile updates may require Dashboard: official API account-update documentation describes connected accounts, not arbitrary own-account editing. No authenticated Dashboard provided. Inspect safely before deciding next step; never print private account data.
4. Reuse product/price IDs in docs/stripe-live.json; both currently inactive. Activate only when private support/policies are ready. Create approved £5 GBP one-time LIVE Payment Link with card-only immediate confirmation, tagged race_project=race-codex, redirect `https://race-codex.pages.dev/success?session_id={CHECKOUT_SESSION_ID}`. Save only public IDs/Payment Link URL, never real session references. Do not buy our product.
5. Configure secrets on ONLY race-codex: STRIPE_SECRET_KEY, PAYMENT_LINK_ID, PAYMENT_LINK_URL, PRIVATE_SUPPORT_EMAIL, MERCHANT_NAME. Set SALES_ENABLED=true only after prerequisites, deploy and verify checkout/status/download safeguards. Restricted live key works for account/catalogue/session-list operations and inactive catalogue writes; actual paid-session retrieval and refund permissions remain untested. No key is deployed yet.
6. With dedicated Reddit access, recheck official community/platform rules and send exact approved R-004 post once. No other community, repeated post, DM, cold email or scraped contacts authorized. Reddit credentials still missing; no posting connector/account/post exists.
7. Measure genuine exposure, purchases/refunds. Prioritise buyer exposure over new product features/resources. No ad-spending evidence. Seriously consider changing course if nobody pays by end of week 3 (26 November); idea changes after week 2 require approval.

## Approvals and access

REPLIES: R-001–R-005 approved 6 November 16:18 UTC; R-006 approved 7 November 18:07 UTC. Permission persists; access must still work. R-005 CLOSED/fulfilled; other items OPEN because execution incomplete.

- R-001 live Stripe activation: merchant verification/live key supplied, inactive catalogue prepared day 4; operational checkout incomplete.
- R-002 private inbox/trader identity: trader details published; support variables supplied day 5 but IMAP/SMTP fail. Current address published with truthful outage notices.
- R-003 dedicated Reddit account / R-004 exact r/SideProject post: approved, authentication unavailable, no account/post created.
- R-005 analytics: fulfilled, working scoped read and public-page beacons.
- R-006 provisioning: Stripe supplied; mailbox supplied but unusable; Reddit missing. Repair status/instructions appended without duplicate approval request.

## Technical handover

- Node 22 / Python stdlib. `npm ci`; `npm run build`; `npm run dev`. Dependencies/Chromium installed. `npm test` combines unit, Python operations and browser suites.
- Deploy: `npm run deploy` targets ONLY Pages race-codex. Production https://race-codex.pages.dev . Latest https://77c85fbe.race-codex.pages.dev . No push access; end-session automation saves/pushes.
- Source: scripts/build.mjs generates site/policies; scripts/template-resource.mjs supplies document resource; public/kit.js guide engine and fictional preset; public/app.js builder; public/email-template.js email tool. product/ contains sources and generated offline builder/ZIP; functions/_bundle.js embeds ZIP. No static ZIP in public/.
- New day-5 `scripts/support-check.py`: IMAP SSL + read-only INBOX, optional --smtp authentication, no mail read/sent or raw error/credential output. Known GMX/Gmail/Yahoo/Outlook hosts; unknown providers require SUPPORT_IMAP_HOST/SUPPORT_SMTP_HOST. SMTP port override SUPPORT_SMTP_PORT supports 465 SSL or 587 STARTTLS. Exit nonzero on failure; inspect result, never presence alone. Four mocked tests cover unreadable inbox, auth redaction, missing credentials and no message read/send. Official provider docs linked in operations/request status.
- scripts/stripe-live.py defaults GET-only. --prepare-catalogue reconciles inactive product/price with metadata, lookup key and idempotency. Never activates sales/creates links or charges. docs/stripe-live.json contains only public catalogue IDs. Do not rerun preparation after adding live Payment Link config without reviewing its whitelist writer: it writes catalogue-only config.
- functions/_sales.js accepts sk_live_ and rk_live_; requires SALES_ENABLED=true plus live Payment Link, private support and merchant. Download independently requires LIVE complete/paid session for configured link, GBP and £5 subtotal. Re-verifies on every download; no-store. wrangler.toml remains SALES_ENABLED=false.
- Stripe redirect provides access; no independent delivery email/webhook. Keep private support working for access recovery before collecting payment. Real checkout session references are private bearer-like credentials: never log/commit them. Honour every refund request.
- Analytics: scripts/analytics.py fetches ONLY race-codex project and aggregate GraphQL with its siteTag. Never list account sites/query unfiltered traffic. Public pages allow injected Cloudflare beacon; success/API routes use strict CSP so private session URLs cannot reach analytics. Browser may report one script attempt on /success, but it fails with csp; check actual beacon transmissions rather than attempted requests. Offline kit has no analytics.
- **Day-5 validation:** 8 unit + 9 Python operations + 7 browser tests pass. Production: all three policy pages 200/current support address/outage notice/experiment footer; working preview; salesEnabled=false/buy hidden; gated download 503; static ZIP 404; no page exceptions. Success-page analytics script blocked with csp; no beacon sent. No real payment/session retrieval/refund tested or claimed.

## Session rules

Follow BRIEF session order; save JOURNAL and rewrite STATE no later than 10 minutes before hard stop. Update METRICS on Sundays. Purchases/ads, first contacts, accounts and live Stripe activation gated; approvals persist. No cold email/text, scraping contacts, false claims or refused refunds. Sites disclose AI-run public experiment. No secrets/customer records/private checkout references in public repo. Only race-codex Cloudflare project; never list/change others. Never edit .github/, BRIEF.md, OPERATOR.md or REPLIES.md.
