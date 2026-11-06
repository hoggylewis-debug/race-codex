# STATE: Codex — Site Handoff Kit

Last updated: 2026-11-06, approximately 15:54 UTC (day 1 of 45). Today's work is saved ahead of the 16:27 documentation cutoff and 16:37 hard stop. Race ends 20 December 2026.

## Business

- **Idea:** A reusable offline website handover kit for freelance designers delivering small marketing/brochure sites.
- **Target customer:** Freelance website designers who want a client guide with their studio branding and a repeatable project finish. WordPress, Webflow, static/custom and generic starting points; complex apps/shops need extra documentation.
- **Offer:** £5 GBP once for a ZIP containing an offline HTML builder, 40-point launch checklist CSV, five client emails and instructions. The builder creates a seven-section handover guide, an email, and per-client saved project files. Client HTML exports carry the buyer's studio name/colour; browser Print → Save as PDF provides PDFs.
- **Free entry:** Live browser preview and branded sample HTML download, plus an interactive free checklist. No signup, subscription or remote AI generation. Project input remains in browser memory; there is no database or customer data collection by the builder.
- **Status:** Free preview LIVE. Paid sales CLOSED pending Stripe live approval, merchant identity and a working private refund/support channel. Do not claim the business has customers or validated demand.
- **Primary URL:** https://race-codex.pages.dev
- **Free checklist:** https://race-codex.pages.dev/website-handover-checklist
- **Policy/support URLs:** /privacy, /terms, /support. Current copy explicitly says sales are closed; rewrite it before enabling payments.
- **Repository:** https://github.com/hoggylewis-debug/race-codex (PUBLIC). Product source is visible as part of the experiment; the paid offer is a convenient packaged tool with a commercial-use licence. Do not promise secret/exclusive source code.

## Numbers

| Measure | Value |
| --- | --- |
| Visitors (total) | 0 at start; **unmeasured after launch**, analytics missing |
| Sign-ups | 0 — no signup form |
| Paying customers | 0 |
| Revenue (£) | 0 |
| Spent (£) | 0 |
| Budget left (£) | 50 |
| Outreach sent | 0 |

Stripe was checked read-only at session start: provided key is TEST mode, charges_enabled=false, no charges. A test product, £5 price and Payment Link were then created. Their non-secret IDs/URL are in docs/stripe-test.json. No real or test purchase was made. Test payments never count. Run `python scripts/metrics.py` for aggregate Stripe checks; it prints no customer details and clearly labels test/live. A test key cannot read live account metrics.

No Cloudflare Web Analytics tag/token is configured for our project. Do not report operator tests as visits or invent traffic numbers. R-005 asks for project-only analytics setup.

## Top 3 priorities

1. **Open genuine sales if approved:** read R-001/R-002 replies, obtain live Stripe access and working dedicated private support, publish merchant identity and correct payment/privacy/refund policies, create live £5 Payment Link, set only our Pages project's secrets, and enable checkout. Follow docs/OPERATIONS.md. Do not buy our own product.
2. **Reach the first buyer:** if R-003/R-004 are approved and usable account access exists, recheck r/SideProject rules and send the exact approved post once. No account/post/contact has yet been created. Do not cold-email/text individuals or sole traders, scrape contacts, or DM anyone.
3. **Measure response:** enable project-scoped analytics if R-005 is fulfilled; update CSP/privacy before collecting analytics, excluding checkout-success/download URLs. Record genuine visitors, purchases and refunds. Prioritise customer exposure over more generator features. Consider course seriously if nobody pays by the end of week 3 (26 November).

## Waiting on the referee

All requests were created 2026-11-06 and remain OPEN with no reply. Under BRIEF, no answer within 24 hours means declined; check REPLIES before acting. No human replies during a session.

- **R-001:** Approve live Stripe activation for £5 one-time kit and provision live credential/merchant verification. Available Stripe credential is test-only.
- **R-002:** Supply the race's dedicated inbox access via environment/tool and publishable merchant identity/contact. No email tool or email-related environment variables are available. Never use Lewis's personal/business contacts. Do not put credentials in replies or this repo.
- **R-003:** Create/access one dedicated Reddit account with the supplied transparent AI-experiment bio.
- **R-004:** Exact first-contact r/SideProject launch/feedback post. Full text is in REQUESTS.md. Does not authorize other communities, repeat posts, DMs or email.
- **R-005:** Free Cloudflare Web Analytics setup/access for race-codex only. No other project or account-wide setting has been touched.

## Technical handover

- Runtime: Node 22. `npm ci`, `npm run build`, `npm run dev` (local Pages server).
- Deploy: `npm run deploy` → **only** Cloudflare Pages project `race-codex`. CLOUDFLARE_API_TOKEN and CLOUDFLARE_ACCOUNT_ID are environment variables. Do not print them. No push access; end-of-session automation commits/pushes. No changes to .github/, BRIEF.md or REPLIES.md.
- Main copy and policies: `scripts/build.mjs` generates static HTML in `public/` and the offline product. Generator: `public/kit.js`. UI: `public/app.js`; CSS: `public/base.css`. Source content: `product/checklist.json`, `product/client-emails.txt`, `product/START-HERE.txt`.
- Paid artifact: `product/site-handoff-kit.zip` and offline-builder.html. Build embeds the ZIP in `functions/_bundle.js`; **do not place it in public/**. Cloudflare packages `functions/` during deployment.
- Download gate: `functions/api/download.js` and `functions/_sales.js`. Requires SALES_ENABLED=true, live key, configured live link, merchant/support details, and a live complete paid Stripe session for that link with £5 GBP subtotal. No production secrets have been set. `wrangler.toml` keeps SALES_ENABLED=false.
- Tests: `npm run test:unit` (8 passed); install browser with `npx playwright install chromium` if missing, then `npm run test:browser` (5 passed). Paid verification is mocked, not a real charge. Mobile, sample export, offline file mode, zero-network operation and project save/load passed.
- Live verification: homepage, policies, free checklist and status returned 200 in an actual browser; preview updates; status says false; product download is blocked (503), and static ZIP path is 404. No browser errors. Python default UA sometimes received 403; curl/browser succeeded, so use them for availability checks.
- Read **docs/OPERATIONS.md** for live activation, secret handling, refunds, delivery limitations and metrics. No independent delivery email/webhook exists yet: the checkout redirect is the planned delivery path, with private support required for recovery.
- Rationale/source research: docs/RESEARCH.md. Free competing checklists exist; paid differentiation is reusable offline personalisation and packaging. Willingness to pay is unvalidated.

## Session rules to preserve

Read BRIEF and its ordered session routine; read the last three JOURNAL entries and all requests/replies before choosing one task. Check numbers, then ship one thing most likely to win the next real paying customer. Save JOURNAL and rewrite STATE by ten minutes before the hard stop. Update METRICS on Sunday (next: 8 November).

All purchases/paid ads, first new contacts, social/marketplace accounts and Stripe live activation need the referee's explicit approval. After week 2, idea changes are gated too. Always honour refunds. Every site must disclose the AI-run public experiment in its footer. Public repo: never save credentials or private customer/order records. Credentials only from environment variables. Shared Cloudflare account: never list/change other projects, tokens or settings.
