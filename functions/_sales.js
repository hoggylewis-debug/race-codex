export function salesReady(env) {
  return env.SALES_ENABLED === 'true'
    && /^sk_live_/.test(env.STRIPE_SECRET_KEY || '')
    && /^plink_[A-Za-z0-9]+$/.test(env.PAYMENT_LINK_ID || '')
    && /^https:\/\/buy\.stripe\.com\/(?!test_)[A-Za-z0-9]+$/.test(env.PAYMENT_LINK_URL || '')
    && Boolean(env.PRIVATE_SUPPORT_EMAIL && env.MERCHANT_NAME);
}
export function json(data, status=200) {
  return new Response(JSON.stringify(data), {status,headers:{'Content-Type':'application/json;charset=utf-8','Cache-Control':'no-store','X-Content-Type-Options':'nosniff','Referrer-Policy':'no-referrer'}});
}
export function verifySession(session, env) {
  return session.livemode === true && session.status === 'complete' && session.payment_status === 'paid'
    && session.payment_link === env.PAYMENT_LINK_ID && session.currency === 'gbp'
    && session.amount_subtotal === 500 && session.amount_total >= 500;
}
