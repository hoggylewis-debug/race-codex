const status=document.querySelector('#download-status');
const params=new URLSearchParams(location.search);
const session=params.get('session_id');
if(!session || !/^cs_(?:test_|live_)?[A-Za-z0-9_]{10,240}$/.test(session)) {
  status.textContent='No valid checkout reference was provided. Return here using the link shown after your purchase. Never post this page link publicly.';
} else {
  // Never forward the bearer-like checkout reference to third-party resources.
  const url='/api/download?session_id='+encodeURIComponent(session);
  fetch(url,{method:'HEAD',cache:'no-store'}).then(async response=>{
    if(response.ok) {
      status.textContent='Your payment is confirmed. Download the ZIP, extract it, and open handover-builder.html. Keep this private page link to download again.';
      const link=document.querySelector('#download-kit'); link.href=url; link.classList.remove('hidden');
    } else if(response.status===402) status.textContent='Your payment is not yet confirmed. Please refresh this page in a moment. If you were charged and still cannot download, use the private support channel on the support page.';
    else if(response.status===503) status.textContent='Downloads are temporarily unavailable. Keep this private page link and try again shortly, or visit Support.';
    else status.textContent='We could not verify that checkout reference. Please use your original purchase confirmation link or visit Support.';
  }).catch(()=>{status.textContent='The connection failed. Please refresh this page to try again.';});
}
