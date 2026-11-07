const form = document.querySelector('#email-template-form');
const output = document.querySelector('#email-output');
const status = document.querySelector('#email-template-status');
const template = output.value;
const replacements = {
  emailClient: '[Client]', emailName: '[Name]', emailStudio: '[Your name / studio]',
  emailURL: '[website URL]', emailSupport: '[agreed support channel]'
};
form.addEventListener('submit', event => event.preventDefault());
form.addEventListener('input', () => {
  let email = template;
  for (const [name, placeholder] of Object.entries(replacements)) {
    const value = form.elements.namedItem(name).value.trim();
    if (value) email = email.split(placeholder).join(value);
  }
  output.value = email;
  status.textContent = '';
});
document.querySelector('#copy-email').addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(output.value);
    status.textContent = 'Email copied. Review remaining brackets and attach the guide before sending.';
  } catch {
    output.focus(); output.select();
    status.textContent = 'Email selected. Use your device’s Copy command, then paste it into your email app.';
  }
});
document.querySelector('#download-email-template').addEventListener('click', () => {
  const url = URL.createObjectURL(new Blob([output.value], {type:'text/plain;charset=utf-8'}));
  const link = document.createElement('a');
  link.href = url; link.download = 'website-handover-email.txt'; link.click();
  setTimeout(() => URL.revokeObjectURL(url), 2000);
  status.textContent = 'Text file prepared. Review remaining brackets before sending.';
});
