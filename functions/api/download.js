import {kitBase64} from '../_bundle.js';
import {salesReady,json,verifySession} from '../_sales.js';
export async function onRequest({request,env}) {
  if(!['GET','HEAD'].includes(request.method)) return json({error:'Method not allowed'},405);
  if(!salesReady(env)) return json({error:'Sales and downloads are not open.'},503);
  const sessionId=new URL(request.url).searchParams.get('session_id');
  if(!sessionId || !/^cs_live_[A-Za-z0-9]{10,240}$/.test(sessionId)) return json({error:'Invalid purchase reference.'},400);
  let session;
  try {
    const response=await fetch('https://api.stripe.com/v1/checkout/sessions/'+encodeURIComponent(sessionId),{
      headers:{Authorization:'Bearer '+env.STRIPE_SECRET_KEY},signal:AbortSignal.timeout(10000)
    });
    if(response.status===404) return json({error:'Purchase not found.'},404);
    if(!response.ok) return json({error:'Payment verification temporarily unavailable.'},503);
    session=await response.json();
  } catch { return json({error:'Payment verification temporarily unavailable.'},503); }
  if(!verifySession(session,env)) return json({error:'A completed payment for this kit is required.'},402);
  const headers={'Content-Type':'application/zip','Content-Disposition':'attachment; filename="site-handoff-kit.zip"','Cache-Control':'private, no-store','Referrer-Policy':'no-referrer','X-Content-Type-Options':'nosniff','X-Robots-Tag':'noindex, nofollow'};
  return new Response(request.method==='HEAD' ? null : Uint8Array.from(atob(kitBase64),c=>c.charCodeAt(0)),{headers});
}
