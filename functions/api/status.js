import {salesReady,json} from '../_sales.js';
export function onRequestGet({env}) {
  const enabled=salesReady(env);
  return json({salesEnabled:enabled,...(enabled ? {paymentLink:env.PAYMENT_LINK_URL} : {})});
}
