import { defaults, handoverHTML, handoverEmail } from './kit.js';
const form = document.querySelector('#builder');
const preview = document.querySelector('#preview');
const offline = document.body.dataset.mode === 'offline';
const fields = Object.keys(defaults);
function getData() { return Object.fromEntries(fields.map(key => [key, form.elements.namedItem(key)?.value || ''])); }
function render() { preview.srcdoc = handoverHTML(getData(), {sample: !offline}); }
function download(name, content, type) {
  const url = URL.createObjectURL(new Blob([content], {type}));
  const a = document.createElement('a'); a.href = url; a.download = name; a.click();
  setTimeout(() => URL.revokeObjectURL(url), 2000);
}
function slug() { return (getData().client || 'client').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'').slice(0,60) || 'client'; }
for (const key of fields) { const input = form.elements.namedItem(key); if (input && defaults[key] && key !== 'launchDate' && key !== 'supportEnd') input.value = defaults[key]; }
form.addEventListener('input', render);
form.addEventListener('submit', e => { e.preventDefault(); render(); });
document.querySelector('#download-guide').addEventListener('click', () => download(`${slug()}-handover${offline ? '' : '-sample'}.html`, handoverHTML(getData(), {sample: !offline}), 'text/html;charset=utf-8'));
document.querySelector('#reset').addEventListener('click', () => { form.reset(); for (const key of fields) {const input = form.elements.namedItem(key); if(input) input.value=defaults[key];} render(); });
if (offline) {
  document.querySelector('#download-email').addEventListener('click', () => download(`${slug()}-handover-email.txt`, handoverEmail(getData()), 'text/plain;charset=utf-8'));
  document.querySelector('#save-project').addEventListener('click', () => download(`${slug()}-project.json`, JSON.stringify({version:1,details:getData()},null,2), 'application/json'));
  document.querySelector('#load-project').addEventListener('change', async e => {
    const file = e.target.files[0]; if (!file) return;
    const status = document.querySelector('#project-status');
    try {
      if (file.size > 150000) throw new Error('That file is too large.');
      const data = JSON.parse(await file.text());
      if(data.version !== 1 || !data.details || typeof data.details !== 'object') throw new Error('Choose a project JSON file saved by this tool.');
      for(const key of fields) {const input=form.elements.namedItem(key); if(input) input.value=typeof data.details[key]==='string' ? data.details[key].slice(0,6000) : defaults[key];}
      render(); status.textContent='Project loaded. Your file stayed on this device.';
    } catch(error) { status.textContent=error instanceof SyntaxError ? 'That file is not valid JSON. Choose a saved project file.' : error.message; }
    e.target.value='';
  });
} else {
  fetch('/api/status').then(r => r.ok ? r.json() : Promise.reject()).then(data => {
    if(data.salesEnabled && /^https:\/\/buy\.stripe\.com\/[a-zA-Z0-9_]+$/.test(data.paymentLink)) {
      const buy=document.querySelector('#buy'); buy.href=data.paymentLink; buy.textContent='Get the complete kit — £5'; buy.classList.remove('hidden');
      document.querySelector('#sales-status').textContent='One payment. Instant ZIP download after checkout. No account needed.';
    }
  }).catch(() => {});
}
render();
