# Site Handoff Kit operations

Read STATE.md and the race session order first. This is a public repository: no secrets, customer records, actual checkout-session references or card details belong here.

## Run and deploy

- `npm ci`
- `npm run build`
- `npm run test:unit`
- `npx playwright install chromium` if browser binaries are missing
- `npm run test:browser`
- `npm run deploy` (only Pages project `race-codex`)

`public/` is the static site. Cloudflare includes `functions/` during deployment. The source of page copy, privacy and terms is `scripts/build.mjs`; edit that source rather than just generated HTML. The guide generator is `public/kit.js`, with browser behaviour in `public/app.js`. Product source is in `product/`. The build creates the offline builder, ZIP and `functions/_bundle.js`. The ZIP is embedded in a server function and is not a static site download. The repository and source artifacts remain public as part of the experiment; the paid offer is a convenient packaged tool with a commercial-use licence, not exclusive or secret code.

No server database, cookies or marketing analytics are configured. No customer input is sent from the builder. No production Stripe secret is deployed. No email signup form exists. Request R-005 asks the referee to enable project-specific free visitor analytics; do not touch other account services to work around it.

## Before live sales

All of these are required before opening checkout:

1. Read R-001's reply. Approval to activate Stripe is required by BRIEF.md. No reply after 24 hours means declined.
2. Obtain live Stripe access through environment variables and verify charges are enabled. Do not log or save a key. Do not attempt identity verification on behalf of a human.
3. Obtain the dedicated inbox, private support route and merchant details (R-002). Confirm it works. Never use Lewis's personal/business contacts or credentials.
4. Update the support page, terms and privacy source. Include the actual merchant identity, private refund address and payment data handling before collecting payment. Stripe will process checkout email/order data; document actual retention and deletion/access contact. Publish the unconditional refund policy. The current text explicitly says sales are closed and must be rewritten before opening them.
5. Configure the actual business support and policy URLs in the race Stripe account as appropriate. Create a LIVE £5 GBP one-time product/price/Payment Link. Do not reuse test IDs. Restrict initial payment methods to promptly confirmed methods, e.g. cards. Do not enable tax features, subscriptions, new paid tools or additional purchases without relevant approval.
6. Set the Payment Link to redirect to `https://race-codex.pages.dev/success?session_id={CHECKOUT_SESSION_ID}` after payment. The braces placeholder is literal in the Stripe setting. Session references are private download credentials; never put real ones in repo files or logs.
7. Set production Pages secrets only for project `race-codex`: `STRIPE_SECRET_KEY`, `PAYMENT_LINK_ID`, `PAYMENT_LINK_URL`, `PRIVATE_SUPPORT_EMAIL`, `MERCHANT_NAME`. Feed values to Wrangler from environment/stdin; never echo them into logs or write temporary secret files. Example for the key, after approval: `printenv STRIPE_SECRET_KEY | npx wrangler pages secret put STRIPE_SECRET_KEY --project-name race-codex`. No actual key value should appear in the command.
8. Change `SALES_ENABLED` in wrangler.toml to `true` only after the above. Deploy, verify status, policy pages and the real hosted checkout configuration. Update the sales-closed fallback text in `scripts/build.mjs`; the browser enables the buy link only when `/api/status` reports ready. Include a useful service-outage fallback.
9. The download function independently checks a live, complete, paid Stripe session for the configured link, GBP, £5 subtotal and at least £5 total. It re-verifies on every download, sets no-store headers and checks IDs before making a Stripe request. It refuses unpaid, test and unrelated payments. Unit tests mock Stripe; this is not proof of a real production charge. Do not buy our own product to test it.
10. Keep customer support operational. A payment redirect provides download access; there is currently no independent delivery email/webhook. If someone closes checkout before saving their confirmation link, use private support to verify their order and recover access. Add durable private delivery if evidence warrants it, while keeping customer/order records out of this public repo.

## Metrics

Run `python scripts/metrics.py`. It reads Stripe via environment credentials, uses `PAYMENT_LINK_ID` (or the saved test ID in test mode), and prints only aggregate counts and money. It never prints or saves customer emails or IDs. It explicitly labels test-mode results. A test key cannot verify live account numbers.

The baseline at launch is zero paid customers, revenue and spend. Visitors after launch are **unmeasured**, not zero. Operator browser checks are not customer visits. Until analytics is available, do not invent visitors, conversions or sample-download counts. Sign-ups are zero because there is no signup form.

When R-005 is fulfilled, update privacy and CSP for the actual Cloudflare analytics endpoints, redeploy, verify the beacon and read only this site's aggregate metrics. Do not expose checkout-session URLs to third-party tracking: exclude `/success` and `/api/` from analytics. Do not report test traffic as demand.

## Distribution

First contact with any new person/business requires an approved exact message. Social/marketplace account creation is gated too. R-003 asks for a dedicated Reddit account and R-004 covers exactly one r/SideProject post. Do not post before approval, or bypass platform protections to create/access the account. Recheck the current community rules first. Do not crosspost the same message into other communities without their own approval.

No email/DM campaign, scraped contacts or paid ads have been authorized. The public launch, sitemap, free checklist, social card and README are available without further contact. The next useful task is to enable genuine sales and send an approved distribution message, not to add more generator features.
