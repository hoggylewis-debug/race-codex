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

## R-005 | 2026-11-06 | OPEN
- Action: Enable free Cloudflare Web Analytics for the Pages project race-codex only, or supply an already-approved project-specific analytics integration. No other contestant project or account-wide setting should be changed. If the API credential lacks access to read this project's analytics, provide an appropriately scoped way to read its aggregate metrics through the environment.
- Why: Neither a Web Analytics tag nor token is configured on our Pages project. Without it we cannot measure visits or acquisition. The session limits us to our own Pages project, so I have not created an account-level analytics site or touched other account settings.
- Cost: £0; free service only.
- Exact text / link: Follow https://developers.cloudflare.com/pages/how-to/web-analytics/ : select Pages project race-codex → Metrics → Enable under Web Analytics. I will update the privacy policy and CSP, redeploy and verify the beacon before reporting measured visitor numbers. No project form data should be sent to analytics.
