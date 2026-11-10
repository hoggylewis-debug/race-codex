# REQUESTS: Codex

_Anything gated in BRIEF.md goes here. Add the request, then keep working on something else._
_Lewis answers from his phone. His answers appear in REPLIES.md, not in this file. No answer within 24 hours means declined._
_Once an answer is in and you have acted on it, change OPEN to CLOSED in the request's heading._

```
## R-001 | YYYY-MM-DD | OPEN
- Action:
- Why:
- Cost: £
- Exact text / link:
```

## R-001 | 2026-11-06 | OPEN
- Action: Approve activating this race's Stripe account for live sales of Site Handoff Kit at £5 per one-time download. Provide a live-mode key through the environment (never this public repo) and complete any Stripe merchant verification that requires a human.
- Why: The available Stripe key is test-mode only; the account reports charges_enabled=false. A live checkout is required for the next paying customer. The offer will be reviewable at https://race-codex.pages.dev before this session ends.
- Cost: £0 upfront. Standard Stripe transaction fees deducted from genuine sales; no subscription or paid tool purchase requested.
- Exact text / link: Product: “Site Handoff Kit — complete website handover kit”. Price: £5 GBP once. Deliverables: offline HTML handover builder, 40-point CSV checklist, five email templates and instructions. Full offer: https://race-codex.pages.dev/#pricing . Refunds honoured on request. Live checkout will stay disabled until approval, working private support and merchant details are in place.

- Progress 2026-11-09: live restricted key is now supplied; Stripe confirms charges_enabled=true, payouts_enabled=true and details_submitted=true. Prepared the approved live product and one-time £5 GBP price with both inactive. No live Payment Link or checkout created because SUPPORT_EMAIL/private inbox access are still missing. R-001 remains OPEN until live checkout is actually operational; no further activation approval requested.

## R-002 | 2026-11-06 | OPEN
- Action: Supply access to the race's dedicated business inbox through environment variables or an email tool, plus the merchant identity/business contact details to display for paid sales. Do not paste credentials into REPLIES.md or any repository file. A non-secret inbox address and merchant display name can be supplied there.
- Why: BRIEF.md says we have our own inbox, but no email tool or email-related environment variable is available. A private route for refunds and order support is needed before collecting payment. Public GitHub issues are unsuitable for customer/order information. Do not supply Lewis's personal contacts or own business inbox.
- Cost: £0. Use the existing dedicated race inbox; no new purchase requested.
- Exact text / link: Before opening checkout, publish “Customer support and refunds: [dedicated race inbox]” on https://race-codex.pages.dev/support and publish the supplied merchant identity in the site terms. I will not send email to anyone without the necessary first-contact approval.

## R-003 | 2026-11-06 | OPEN
- Action: Approve creation of one dedicated Reddit account for this business, proposed username SiteHandoffCodex (or SiteHandoffCodexRace if unavailable). Provide a permitted authenticated way to access it if account creation/login requires human interaction. No personal/Lewis account will be used.
- Why: We need a distribution channel for the free handover preview. This request covers account creation only. The first post has its own exact-text approval request R-004. No post or message will be sent before approval.
- Cost: £0.
- Exact text / link: Account bio: “AI agent building Site Handoff Kit: a website handover tool for freelance designers. Part of a public £50 startup experiment. https://race-codex.pages.dev” . Account creation: https://www.reddit.com/register/ . Will follow platform rules and not bypass access controls.

## R-004 | 2026-11-06 | OPEN
- Action: Approve one public launch/feedback post in r/SideProject from the dedicated account in R-003, only if the current community and platform rules permit it. No DMs, cold email, contact scraping or repeat posts. This is the first contact with that community.
- Why: Reach builders who deliver client websites and test whether the sample solves a real handover problem. r/SideProject's official description invites projects and feedback; recheck rules immediately before posting. The product must be live and tested before the post.
- Cost: £0.
- Exact text / link:
  - Destination: https://www.reddit.com/r/SideProject/submit
  - Title: Site Handoff Kit - an offline website handover builder for freelance designers
  - Body:

I’m an AI agent running a small business as part of a public £50 startup experiment. Today I built a website handover tool for freelance designers finishing small client sites.

Enter the client, studio, platform, account owners and support details. It creates a seven-section guide the client can keep. There are starting points for WordPress, Webflow and custom sites; you still need to add the site's own walkthrough and review the result.

The free preview and branded HTML sample need no sign-up. Project details stay in your browser and aren’t sent to an AI model.

Try it: https://race-codex.pages.dev/?source=reddit-sideproject

The planned paid version is £5 once for an offline builder with unbranded exports, saved project files, a 40-point checklist and five emails. The site shows whether sales are open; the sample is free either way.

If you hand websites over to clients, what information do you most often have to explain again after launch? I’d like to know whether the generated guide covers that.

Code and experiment log: https://github.com/hoggylewis-debug/race-codex

## R-005 | 2026-11-06 | CLOSED
- Action: Enable free Cloudflare Web Analytics for the Pages project race-codex only, or supply an already-approved project-specific analytics integration. No other contestant project or account-wide setting should be changed. If the API credential lacks access to read this project's analytics, provide an appropriately scoped way to read its aggregate metrics through the environment.
- Why: Neither a Web Analytics tag nor token is configured on our Pages project. Without it we cannot measure visits or acquisition. The session limits us to our own Pages project, so I have not created an account-level analytics site or touched other account settings.
- Cost: £0; free service only.
- Exact text / link: Follow https://developers.cloudflare.com/pages/how-to/web-analytics/ : select Pages project race-codex → Metrics → Enable under Web Analytics. I will update the privacy policy and CSP, redeploy and verify the beacon before reporting measured visitor numbers. No project form data should be sent to analytics.


- Completed 2026-11-07: project build_config contains the analytics tag and beacon configuration. Redeployed race-codex with updated privacy/CSP; an actual browser confirmed public-page beacons to Cloudflare and CSP blocking on /success. Project-scoped aggregate GraphQL read succeeds through scripts/analytics.py. No other project was listed or touched. Pre-session query returned no records; historic visitors remain unmeasured.

## R-006 | 2026-11-07 | OPEN
- Action: Complete the already-approved R-001/R-002/R-003 provisioning through the runner environment. Set a live `STRIPE_SECRET_KEY` for this race's account after human merchant verification, a working dedicated `SUPPORT_EMAIL` plus inbox access (`SUPPORT_EMAIL_PASSWORD` or an inbox tool), and the dedicated account's `REDDIT_USERNAME` / `REDDIT_PASSWORD` (or a permitted authenticated posting method).
- Why: All five day-1 requests are approved, and OPERATOR.md supplies merchant identity. However, at 13:58 UTC today the key was still TEST mode, Stripe charges_enabled=false and details_submitted=false, and SUPPORT_EMAIL, SUPPORT_EMAIL_PASSWORD, REDDIT_USERNAME and REDDIT_PASSWORD were all empty. Approval alone has not made live payment, private refunds or the approved Reddit post executable. OPERATOR.md explicitly requires sales to stay closed if SUPPORT_EMAIL is missing. No further purchase or new outreach is requested.
- Cost: £0 upfront; use the approved existing race services. Never supply credentials in REPLIES.md or any public file.
- Exact text / link: Live checkout for the approved “Site Handoff Kit — complete website handover kit”, £5 GBP once, https://race-codex.pages.dev/#pricing . Publish the dedicated support address on /support, /terms and /privacy. Then send only the exact already-approved R-004 post, subject to current Reddit rules. R-001 through R-004 remain approved and OPEN because execution is incomplete.

- Status checked 2026-11-08: R-006 APPROVED 2026-11-07 18:07 UTC. Provisioning remains incomplete: Stripe key is TEST mode, charges_enabled=false/details_submitted=false, and support/Reddit environment values are missing. No duplicate approval or provisioning request submitted. R-001/R-002/R-003/R-004/R-006 stay OPEN until executed.

- Progress checked 2026-11-09: live Stripe credential and merchant verification are now provisioned. SUPPORT_EMAIL, SUPPORT_EMAIL_PASSWORD, REDDIT_USERNAME and REDDIT_PASSWORD remain missing. Existing approval/provisioning request still covers these items; no duplicate request submitted. Sales remain closed as OPERATOR requires. R-006 stays OPEN until remaining access is supplied.

- Progress checked 2026-11-10: SUPPORT_EMAIL and SUPPORT_EMAIL_PASSWORD are now provisioned, but the dedicated GMX account rejects IMAP authentication (`imap.gmx.com:993`, authentication failed) and SMTP authentication (`mail.gmx.com:465`, 535 credentials invalid). No message sent or inbox contents read. Working access is still covered by existing R-002/R-006; this is a status/repair note, not a duplicate request. Please check GMX POP3/IMAP access is enabled and supply a valid application-specific password through SUPPORT_EMAIL_PASSWORD only. Official instructions: https://support.gmx.com/pop-imap/toggle.html and https://support.gmx.com/security/2fa/application-specific-passwords.html . The cause is not established. Current support address is published on all three policies/support pages with an access-unavailable notice; sales remain closed per OPERATOR. Reddit access remains missing.
