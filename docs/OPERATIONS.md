# Site Handoff Kit operations

Read STATE.md and the race session order first. This is a public repository: no secrets, customer records, actual checkout-session references or card details belong here.

## Run and deploy

- `npm ci`
- `npm run build`
- `npm run test:unit` and `npm run test:ops`
- `npx playwright install chromium` if browser binaries are missing
- `npm run test:browser`
- `npm run deploy` (only Pages project `race-codex`)

`public/` is the static site. Cloudflare includes `functions/` during deployment. The source of page copy, privacy and terms is `scripts/build.mjs`; edit that source rather than just generated HTML. The guide generator is `public/kit.js`, with browser behaviour in `public/app.js`. Product source is in `product/`. The build creates the offline builder, ZIP and `functions/_bundle.js`. The ZIP is embedded in a server function and is not a static site download. The repository and source artifacts remain public as part of the experiment; the paid offer is a convenient packaged tool with a commercial-use licence, not exclusive or secret code.

No server database, cookies or marketing pixels are configured. Cloudflare Web Analytics is enabled on public pages (R-005 fulfilled day 2). No customer input is sent from the builder or email template tool. No production Stripe secret is deployed; checkout remains closed. No email signup form exists. Read-only analytics must always be filtered to this project; never list other sites or query unfiltered account traffic.

## Before live sales

All of these are required before opening checkout:

1. R-001 was APPROVED on 6 November 2026. This approval persists: do not request it again. Read current replies for provisioning updates. R-006 was APPROVED on 7 November and identifies missing access; approvals for R-001 through R-004 exist but execution is incomplete.
2. Live Stripe access is now provisioned (9 November): restricted live key, charges_enabled=true, payouts_enabled=true, details_submitted=true. `python scripts/stripe-live.py` performs a read-only access/catalogue check. The server accepts live standard and restricted keys; test/public keys remain blocked. Verify restricted-key permissions when using each API; never print a key. Human verification is complete; do not redo it.
3. Obtain the dedicated inbox and private support access (R-002/R-006). SUPPORT_EMAIL and SUPPORT_EMAIL_PASSWORD are present on day 5, but both IMAP and SMTP authentication fail. OPERATOR.md requires sales to remain closed after a failed IMAP login. Run `python scripts/support-check.py --smtp`; do not infer working access from environment presence. OPERATOR.md supplies the trader identity and address; they are now published only on /terms, /privacy and /support. Build reads the publishable SUPPORT_EMAIL if provided. Never use Lewis's personal/business contacts or credentials.
4. Update the support page, terms and privacy source. Include the actual merchant identity, private refund address and payment data handling before collecting payment. Stripe will process checkout email/order data; document actual retention and deletion/access contact. Publish the unconditional refund policy. The current text explicitly says sales are closed and mailbox access is temporarily unavailable; remove these notices only after verified access and update the actual payment processing text before opening checkout.
5. Configure the actual business support and policy URLs in the race Stripe account as appropriate. The LIVE £5 GBP one-time product and price already exist: their public catalogue IDs are in docs/stripe-live.json. Both are inactive. Reuse them rather than creating duplicates. `python scripts/stripe-live.py --prepare-catalogue` reconciles this catalogue without enabling it or creating a link. Only after private support and updated policies are ready, activate this product/price and create the LIVE Payment Link, tagged with metadata race_project=race-codex. Save only the public payment_link_id in docs/stripe-live.json (or configure PAYMENT_LINK_ID in the runner environment). Do not reuse test IDs. Restrict initial payment methods to promptly confirmed methods, e.g. cards. Do not enable tax features, subscriptions, new paid tools or additional purchases without relevant approval.
6. Set the Payment Link to redirect to `https://race-codex.pages.dev/success?session_id={CHECKOUT_SESSION_ID}` after payment. The braces placeholder is literal in the Stripe setting. Session references are private download credentials; never put real ones in repo files or logs.
7. Set production Pages secrets only for project `race-codex`: `STRIPE_SECRET_KEY`, `PAYMENT_LINK_ID`, `PAYMENT_LINK_URL`, `PRIVATE_SUPPORT_EMAIL`, `MERCHANT_NAME`. Feed values to Wrangler from environment/stdin; never echo them into logs or write temporary secret files. Example for the key, after approval: `printenv STRIPE_SECRET_KEY | npx wrangler pages secret put STRIPE_SECRET_KEY --project-name race-codex`. No actual key value should appear in the command.
8. Change `SALES_ENABLED` in wrangler.toml to `true` only after the above. Deploy, verify status, policy pages and the real hosted checkout configuration. Update the sales-closed fallback text in `scripts/build.mjs`; the browser enables the buy link only when `/api/status` reports ready. Include a useful service-outage fallback.
9. The download function independently checks a live, complete, paid Stripe session for the configured link, GBP, £5 subtotal and at least £5 total. It re-verifies on every download, sets no-store headers and checks IDs before making a Stripe request. It refuses unpaid, test and unrelated payments. Unit tests mock Stripe; this is not proof of a real production charge. Do not buy our own product to test it.
10. Keep customer support operational. A payment redirect provides download access; there is currently no independent delivery email/webhook. If someone closes checkout before saving their confirmation link, use private support to verify their order and recover access. Add durable private delivery if evidence warrants it, while keeping customer/order records out of this public repo.

## Metrics

Run `python scripts/metrics.py`. It reads Stripe via environment credentials, uses `PAYMENT_LINK_ID` (or the saved docs/stripe-live.json or docs/stripe-test.json link for the key mode), and prints only aggregate counts and money. It never prints or saves customer emails or IDs. It explicitly labels live/test results. A test key cannot verify live account numbers. With no configured link, it checks account sessions: an empty account establishes zero; any nonempty account is reported as unattributed with null kit orders/revenue, never claimed as race sales. Day 4 live read confirms zero sessions/payments. No customer records are logged or saved.

The baseline is zero paid customers, revenue and spend. Traffic before the day-2 deployment is **unmeasured**, not zero. Sign-ups are zero because there is no signup form. Operator browser checks are not customer visits. No event tracking for sample downloads or email copies exists; do not claim those counts.

R-005 is fulfilled. Run `python scripts/analytics.py` (optionally `--start 2026-11-07T00:00:00Z --end 2026-11-08T00:00:00Z`). It fetches only the race-codex project and queries aggregate Web Analytics with that project’s siteTag. It never lists account sites or prints tokens. `reported_visits` is the provider’s visits estimate, not unique people. Empty results do not establish zero visitors. Current data includes operator smoke tests and cannot yet demonstrate genuine demand.

Cloudflare automatically injects its configured beacon on redeployment. `public/_headers` permits its script and connection on public pages, with a second strict CSP for `/success`, `/success.html`, `/success/`, `/success/*` and `/api/*`. An actual browser confirmed HTTP 204 acceptance for public-page beacons and verified the injected success-page script fails with CSP and sends no analytics beacon. Expected CSP console messages on this route are deliberate. API JSON and download responses have no HTML beacon. Preserve this when changing headers; never let a checkout-session URL reach analytics. Do not copy the project analytics token into repo source. The offline product contains no analytics.

## Distribution

First contact with any new person/business requires an approved exact message. Social/marketplace account creation is gated too. R-003 asks for a dedicated Reddit account and R-004 covers exactly one r/SideProject post. Do not post before approval, or bypass platform protections to create/access the account. Recheck the current community rules first. Do not crosspost the same message into other communities without their own approval.

No email/DM campaign, scraped contacts or paid ads have been authorized. The public launch, sitemap, free checklist, social card and README are available without further contact. The next useful task is to enable genuine sales and send an approved distribution message, not to add more generator features.


## Day-2 free resource

`/website-handover-email-template` is a free, indexed landing page aimed at designers ready to deliver a client site. It personalises one final-delivery email, supports copy (with selection fallback) and plain-text download, and points to the guide builder and £5 offer. Fields stay in tab memory. No email is sent or address collected. Source is generated by scripts/build.mjs; interaction lives in public/email-template.js. The complete kit still includes five templates and the reusable offline builder.

## Current access blockers (10 November)

- Live Stripe account/merchant verification and inactive £5 catalogue are ready. No Payment Link exists and no Stripe secret is deployed to Pages. No real payment, paid-session retrieval or refund has been exercised.
- SUPPORT_EMAIL and SUPPORT_EMAIL_PASSWORD now exist. IMAP at `imap.gmx.com:993` returns authentication failed; SMTP at `mail.gmx.com:465` returns 535 authentication credentials invalid. These are server authentication rejections, not missing variables or connection timeouts. No email was sent and no inbox contents were read. Do not retry repeatedly or try to bypass verification. The exact cause is unknown.
- Existing R-002/R-006 provisioning covers working access; no new approval is required. In the dedicated GMX account, the provisioner should check [POP3/IMAP access](https://support.gmx.com/pop-imap/toggle.html) is enabled and supply a valid [application-specific password](https://support.gmx.com/security/2fa/application-specific-passwords.html) through SUPPORT_EMAIL_PASSWORD. These are troubleshooting possibilities, not a diagnosis. Do not put passwords or recovery material in this repo.
- `python scripts/support-check.py` authenticates and selects INBOX read-only, reads no messages, and exits nonzero unless access works. `--smtp` additionally verifies outgoing authentication without sending any message. Only fixed status categories are printed, never raw provider errors/addresses/passwords. GMX settings follow [official server data](https://support.gmx.com/pop-imap/imap/server.html). Gmail, Yahoo and Outlook consumer hosts are mapped too; other providers require SUPPORT_IMAP_HOST and SUPPORT_SMTP_HOST. SMTP supports TLS on 465 or STARTTLS on 587 via SUPPORT_SMTP_PORT. Provider-specific restrictions may still require provisioning.
- The current support address is now published on /terms, /privacy and /support; all three explain access is temporarily unavailable and paid sales remain closed. Check against the current environment every session. If the provider changes, update the privacy provider name/link too. Do not place trader details elsewhere.
- Reddit credentials remain missing, with no authenticated posting connector. R-003/R-004 remain approved; no account or post exists. Do not bypass platform verification, post anonymously elsewhere or re-request the same provisioning. Recheck official rules when access exists.

## Day-3 document resource

`/website-handover-template` provides a blank `.txt` outline, a completed fictional HTML example and `/?example=juniper#try` to load that fixed example into the free builder. The page works without JavaScript for reading/downloading. No arbitrary project data is loaded from query parameters. Example source lives in `public/kit.js` (`exampleProject`); resource copy and text outline live in `scripts/template-resource.mjs`. Build writes `public/examples/website-handover.html` (noindex) and `public/examples/website-handover-template.txt`. The printable example is branded like the existing free sample, explicitly fictional, and not a customer testimonial. No DOCX export exists.

Day-3 validation passed 8 unit and 7 browser tests, plus production browser checks of new routes, fixed preset, mobile width, closed sales, download 503, public static ZIP 404 and no analytics beacon on /success. Deployment: https://601d0c22.race-codex.pages.dev .


## Day-4 launch preparation

The live catalogue was created through the approved race Stripe account with both product and price inactive. No Payment Link was created: Stripe’s documented creation API creates an active link by default, and we have no support inbox yet. The offer must not become purchasable before that inbox is operational. API references: [product creation](https://docs.stripe.com/api/products/create), [price creation](https://docs.stripe.com/api/prices/create), [Payment Link creation](https://docs.stripe.com/api/payment-link/create), [deactivation](https://docs.stripe.com/api/payment-link/update).

`scripts/stripe-live.py` defaults to GET-only checks. `--prepare-catalogue` explicitly creates only the inactive catalogue, uses idempotency keys and metadata/lookup-key reconciliation, and saves only whitelisted public catalogue fields. It never creates customers, links, sessions or charges. Repeated real execution reused the existing catalogue; five offline operations tests cover read-only mode, inactive creation/reuse, rejecting test credentials and honest metrics with/without configured links.

`functions/_sales.js` now accepts restricted live keys (`rk_live_`) as well as standard live keys (`sk_live_`). Every other live-sale gate still applies, including SALES_ENABLED=true, private support and merchant settings. Existing download tests exercise a mocked paid request using both key types, and verify missing support/test keys remain blocked. No Stripe key has been stored in source or deployed to Pages.
