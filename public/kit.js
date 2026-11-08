// Shared by the free preview and the purchased offline builder. No network calls.
export const defaults = {
  client: 'Juniper Studio', studio: 'Your design studio', url: 'https://example.com',
  platform: 'WordPress', launchDate: '', supportEnd: '', supportChannel: '[your agreed support channel]',
  supportScope: 'Fixes for issues with the delivered website. New pages, new features and content changes are quoted separately.',
  domain: '[registrar, account owner and next renewal date]', hosting: '[provider, account owner and next renewal date]',
  access: '[account owner and invitation status for CMS, analytics and other services — never passwords]',
  backups: '[who runs backups, frequency, storage location and date of last restore test]',
  editing: '[link or location of your project-specific editing walkthrough]',
  services: '[service, purpose, account owner and renewal date for each paid dependency]',
  assets: '[location of source files, logo files and image/font licence records]',
  openItems: 'Review the placeholders in this guide and record any outstanding work before sharing.',
  accent: '#173a36'
};
// Fictional completed project used by the public template resource.
export const exampleProject = {
  client: 'Juniper Ceramics (fictional example)', studio: 'Northline Design (fictional example)',
  url: 'https://example.com', platform: 'WordPress', accent: '#173a36',
  launchDate: '2026-11-06', supportEnd: '2026-12-06',
  supportChannel: 'The shared project support board, linked in the client project folder',
  domain: 'Client business account at the registrar. Client director owns renewal. Example renewal: 6 November 2027. Confirm the reminder reaches the client.',
  hosting: 'Client-owned managed hosting account. Client director owns billing. Example renewal: 6 November 2027. Designer access is a separate invited account.',
  access: 'Client director: administrator invitation accepted. Content lead: editor invitation accepted and a test edit completed. Designer: separate maintenance account. Review access when the support arrangement changes.',
  services: 'Contact form: hosted with the site; content lead checks delivery. No paid third-party integrations in this fictional project. Add real services and renewals for your site.',
  editing: 'Project folder: Training / Editing-walkthrough.pdf. To change the About page: sign in with your own account, open Pages, choose About, edit the text and preview it. Check the phone layout, then Update. The content lead practised this during handover. Follow the recorded walkthrough for this fictional site; your editor may differ.',
  backups: 'Example arrangement: hosting provider runs daily backups with 14-day retention. Designer checks backup status during the agreed support window; the client appoints a maintenance owner afterward. Restore rehearsal completed on a staging copy on 5 November 2026. Steps: Project folder / Maintenance / Restore-runbook.pdf. Confirm your real provider, retention and restore process.',
  supportScope: 'Example of an already-agreed arrangement: fixes to delivered pages through 6 December 2026. New pages, additional features and ongoing content updates are separately scoped. Copy your actual agreed scope and dates here.',
  assets: 'Client-owned project folder: Source / for design files; Assets / for approved logos, photos and font records; Training / for the walkthrough; Maintenance / for the restore runbook. Client director confirmed folder access.',
  openItems: 'Client content lead to supply the final studio photograph by 10 November 2026. Designer to replace the approved placeholder by 12 November 2026. Record completion in the project board.'
};
export const platforms = {
  WordPress: [
    ['Edit a page', 'Sign in using your own editor account. Open Pages, select the page and choose Edit. Preview your change before publishing or updating. Your theme or page builder may use a different editor; follow the project walkthrough below.'],
    ['Add an image', 'Upload a web-sized image in Media. Add descriptive alternative text where the image carries meaning. Check the page at phone and desktop widths after replacing an image.'],
    ['Updates and recovery', 'Confirm who maintains WordPress, the theme and plugins. Take a backup and test changes on a staging copy before applying updates to the live site. Use the agreed recovery procedure if a change breaks the site.']
  ],
  Webflow: [
    ['Edit content', 'Use the editing role and interface assigned to you. Open the relevant page or CMS item, make the change and preview it. Confirm you are publishing to the intended domain before publishing. Workspace permissions determine which controls you see.'],
    ['Add a CMS item', 'Open the collection used by the site, add an item and complete its required fields. Check its URL, images and page preview before publishing. Follow the project walkthrough for the site’s collection structure.'],
    ['Keep ownership clear', 'Confirm the client controls the intended workspace, site plan and billing. Record who manages forms, backups and any connected apps. Check permissions before removing the designer’s access.']
  ],
  'Static / custom': [
    ['Request a content change', 'Use the project walkthrough to identify the source file or content system. If updates require a developer, send the page URL, the current text and the replacement text through the agreed support channel.'],
    ['Publish a change', 'Follow the project-specific build and deployment instructions. Preview a deployment before promoting it to the production domain. Record the repository, hosting project and the person who owns deployment access.'],
    ['Recover a previous version', 'Locate the last known working deployment or source revision and the agreed rollback steps. Confirm who can restore it and test the recovery process before handover.']
  ],
  Other: [
    ['Edit content', 'Use your own account and the project-specific walkthrough. Preview changes before publishing and check both phone and desktop layouts afterward.'],
    ['Publish safely', 'Confirm who can publish, which site is production and how changes are previewed. Record any approval step used by your team.'],
    ['Recover a change', 'Record the backup or version-history feature used by this platform, who can restore it and the last time the process was tested.']
  ]
};
export function escapeHTML(value) { return String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
export function cleanData(raw = {}) {
  const result = {};
  for (const [key, fallback] of Object.entries(defaults)) {
    const value = typeof raw[key] === 'string' ? raw[key].trim().slice(0, 6000) : '';
    result[key] = value || fallback;
  }
  if (!platforms[result.platform]) result.platform = 'Other';
  if (!/^#[\da-f]{6}$/i.test(result.accent)) result.accent = defaults.accent;
  return result;
}
export function handoverHTML(raw, { sample = true } = {}) {
  const d = cleanData(raw), e = escapeHTML;
  const dateText = value => /^\d{4}-\d{2}-\d{2}$/.test(value) ? new Date(value + 'T12:00:00Z').toLocaleDateString('en-GB', {day:'numeric',month:'long',year:'numeric',timeZone:'UTC'}) : '[confirm date]';
  const row = (label, value) => `<tr><th>${e(label)}</th><td>${e(value)}</td></tr>`;
  const paragraph = value => `<p class="entered">${e(value)}</p>`;
  const tasks = platforms[d.platform].map(([title, text]) => `<h3>${e(title)}</h3><p>${e(text)}</p>`).join('');
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${e(d.client)} — website handover</title><style>
  :root{--accent:${d.accent}}*{box-sizing:border-box}body{font:14px/1.65 system-ui,-apple-system,sans-serif;color:#263a34;max-width:850px;padding:42px;margin:auto;background:#fff}h1,h2,h3{color:var(--accent);line-height:1.25}h1{font:42px/1.15 Georgia,serif;margin:15px 0}h2{font:26px/1.2 Georgia,serif;border-top:1px solid #d9dfd8;padding-top:23px;margin-top:32px;break-after:avoid}h3{font-size:15px;margin:20px 0 6px;break-after:avoid}p{margin:0 0 12px}.kicker{font-size:10px;letter-spacing:2px;text-transform:uppercase;border-bottom:3px solid var(--accent);padding-bottom:15px}.sub{color:#61716a}.notice{background:#edf1e9;border-left:3px solid var(--accent);padding:14px;margin:22px 0}.sample{background:#fff2df;color:#70431d;padding:12px;font-size:12px;margin-bottom:20px}table{border-collapse:collapse;width:100%;margin:15px 0}th,td{text-align:left;vertical-align:top;border-bottom:1px solid #d9dfd8;padding:10px 8px;overflow-wrap:anywhere}th{width:32%;font-weight:600}ul{padding-left:22px}.entered{white-space:pre-wrap;overflow-wrap:anywhere}footer{margin-top:35px;border-top:1px solid #d9dfd8;padding-top:14px;font-size:11px;color:#61716a}@media(max-width:500px){body{padding:23px}h1{font-size:32px}th{width:38%}}@media print{body{padding:0;max-width:none;font-size:10.5pt}h1{font-size:30pt}h2{font-size:20pt}table{break-inside:auto}tr,.notice{break-inside:avoid}a{color:inherit}footer{position:static}.sample{border:1px solid #bbb} @page{size:A4;margin:18mm}}
  </style></head><body>${sample ? '<div class="sample">FREE SAMPLE · Check every detail and complete the bracketed prompts before sharing. Export from Site Handoff Kit.</div>' : ''}
  <div class="kicker">${e(d.studio)} / Website handover</div><h1>Your website,<br>in your hands.</h1><p class="sub">Prepared for ${e(d.client)} · ${e(dateText(d.launchDate))}</p>
  <div class="notice"><strong>Start here</strong><br>This guide records where your website lives, how to change it and who to contact. Keep a copy somewhere your team can find. Do not add passwords, recovery codes or private access links.</div>
  <h2>01 / Your website at a glance</h2><table>${row('Website',d.url)}${row('Platform',d.platform)}${row('Prepared by',d.studio)}${row('Launch date',dateText(d.launchDate))}${row('Support contact',d.supportChannel)}${row('Support window ends',dateText(d.supportEnd))}</table>
  <h2>02 / Accounts & renewals</h2><p>These records identify the accounts your site relies on. Confirm each owner has accepted their invitation and can sign in with their own account.</p><table>${row('Domain',d.domain)}${row('Hosting',d.hosting)}${row('Access checklist',d.access)}${row('Connected services',d.services)}</table><p>Transfer credentials separately using the method agreed with your designer. Keep recovery details in your team’s password manager.</p>
  <h2>03 / Everyday content changes</h2><p>These are general starting points for ${e(d.platform)}. The walkthrough for your particular website takes priority.</p>${tasks}<h3>Your project walkthrough</h3>${paragraph(d.editing)}<p>After any change, check the page in a private browser window and on a phone. Try the affected links and forms. If anything is unclear, ask before changing site settings.</p>
  <h2>04 / Backups & maintenance</h2>${paragraph(d.backups)}<ul><li>Confirm a named person owns website updates and backup checks.</li><li>Record the latest successful restore test and where the steps are documented.</li><li>Review domain, hosting and service renewals before they fall due.</li><li>Recheck forms and key journeys after significant changes.</li></ul>
  <h2>05 / Getting help</h2><table>${row('Contact channel',d.supportChannel)}${row('Agreed support through',dateText(d.supportEnd))}${row('Included support / new work',d.supportScope)}</table><p>For a problem report, include the page URL, the action you took, what happened and what you expected. Add a screenshot without sensitive details. For a site outage, say when you first noticed it and whether it affects all pages. Use the response arrangements you agreed with your designer.</p>
  <h2>06 / Files & open items</h2><h3>Your project files</h3>${paragraph(d.assets)}<h3>Still to complete</h3>${paragraph(d.openItems)}
  <h2>07 / Handover meeting</h2><ul><li>Open the live website together and check the main customer journey.</li><li>Have the client sign in, make a small content edit and preview it.</li><li>Confirm account ownership, renewals, support dates and the backup owner.</li><li>Record any unfinished items with an owner and a target date.</li><li>Save this guide with the project files and note where the latest version lives.</li></ul>
  <footer>${sample ? 'Site Handoff Kit · Free sample · Built and run by an AI agent as part of a public experiment.' : `${e(d.studio)} · Prepared for ${e(d.client)} · Update this guide when ownership, services or support arrangements change.`}</footer></body></html>`;
}
export function handoverEmail(raw) {
  const d = cleanData(raw);
  return `Subject: ${d.client} — your website handover and next steps\n\nHi ${d.client} team,\n\nYour website is live at ${d.url}. Attached is your handover guide, with account ownership, editing instructions, maintenance responsibilities and support details.\n\nBefore we close the handover, please:\n1. Confirm you can sign in using your own account.\n2. Try one small content edit using the walkthrough.\n3. Review the account owners and renewal details in the guide.\n4. Let me know if any open item needs a different owner or date.\n\nPlease use ${d.supportChannel} for questions. The support dates and included work are recorded in the guide.\n\nThanks,\n${d.studio}`;
}
