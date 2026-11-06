import test from 'node:test';
import assert from 'node:assert/strict';
import {cleanData, handoverHTML, handoverEmail} from '../public/kit.js';
import {salesReady,verifySession} from '../functions/_sales.js';
import {onRequest} from '../functions/api/download.js';
import JSZip from 'jszip';
import fs from 'node:fs/promises';
const mockEnv={SALES_ENABLED:'true',STRIPE_SECRET_KEY:'sk_live_mock_not_a_real_key',PAYMENT_LINK_ID:'plink_mock',PAYMENT_LINK_URL:'https://buy.stripe.com/mock',PRIVATE_SUPPORT_EMAIL:'support@example.invalid',MERCHANT_NAME:'Test operator'};
const paid={livemode:true,status:'complete',payment_status:'paid',payment_link:'plink_mock',currency:'gbp',amount_subtotal:500,amount_total:500};
test('client input is escaped in the document and CSS colours are constrained',()=>{
 const html=handoverHTML({client:'<img src=x onerror=alert(1)>',accent:'red;}body{display:none'});
 assert.ok(!html.includes('<img src=x')); assert.ok(html.includes('&lt;img src=x')); assert.ok(html.includes('--accent:#173a36'));
});
test('unknown platform gets safe generic instructions; empty values become prompts',()=>{
 const data=cleanData({platform:'<script>',client:' ',launchDate:'invalid'});
 assert.equal(data.platform,'Other'); assert.equal(data.client,'Juniper Studio');
 assert.ok(handoverHTML(data).includes('[confirm date]'));
});
test('export uses chosen platform, dates, client branding and entered line breaks',()=>{
 const html=handoverHTML({client:'Acme',studio:'My Studio',platform:'Static / custom',launchDate:'2026-11-06',domain:'One\nTwo'},{sample:false});
 assert.ok(html.includes('6 November 2026')); assert.ok(html.includes('My Studio')); assert.ok(html.includes('One\nTwo')); assert.ok(html.includes('Publish a change')); assert.ok(!html.includes('FREE SAMPLE')); assert.ok(!html.includes('Site Handoff Kit'));
 assert.ok(handoverEmail({client:'Acme'}).startsWith('Subject: Acme'));
});
test('live checkout cannot be enabled by just one variable or a test key',()=>{
 assert.equal(salesReady({}),false); assert.equal(salesReady({SALES_ENABLED:'true'}),false);
 assert.equal(salesReady({...mockEnv,STRIPE_SECRET_KEY:'sk_test_mock'}),false);
 assert.equal(salesReady({...mockEnv,PAYMENT_LINK_URL:'https://buy.stripe.com/test_mock'}),false);
 assert.equal(salesReady({...mockEnv,PRIVATE_SUPPORT_EMAIL:''}),false);
 assert.equal(salesReady(mockEnv),true);
});
test('only paid, complete, live sessions for this £5 kit unlock the product',()=>{
 assert.equal(verifySession(paid,mockEnv),true);
 for(const change of [{livemode:false},{status:'open'},{payment_status:'unpaid'},{payment_link:'plink_other'},{currency:'usd'},{amount_subtotal:100},{amount_total:0}]) assert.equal(verifySession({...paid,...change},mockEnv),false);
});
test('download route blocks disabled sales, malformed IDs and wrong methods',async()=>{
 assert.equal((await onRequest({request:new Request('https://example.com/api/download?session_id=bogus'),env:{}})).status,503);
 assert.equal((await onRequest({request:new Request('https://example.com/api/download?session_id=bogus'),env:mockEnv})).status,400);
 assert.equal((await onRequest({request:new Request('https://example.com/api/download',{method:'POST'}),env:mockEnv})).status,405);
});
test('download route verifies Stripe and returns a valid ZIP; unpaid sessions stay blocked',async()=>{
 const previous=globalThis.fetch;
 try{
  globalThis.fetch=async()=>Response.json(paid);
  const request=new Request('https://example.com/api/download?session_id=cs_live_mock1234567890');
  const response=await onRequest({request,env:mockEnv});
  assert.equal(response.status,200);assert.equal(response.headers.get('cache-control'),'private, no-store');
  const zip=await JSZip.loadAsync(await response.arrayBuffer());assert.equal(Object.keys(zip.files).filter(name=>!zip.files[name].dir).length,4);
  globalThis.fetch=async()=>Response.json({...paid,payment_status:'unpaid'});
  assert.equal((await onRequest({request,env:mockEnv})).status,402);
  globalThis.fetch=async()=>{throw new Error('Network down')};
  assert.equal((await onRequest({request,env:mockEnv})).status,503);
 }finally{globalThis.fetch=previous;}
});
test('offline kit has no external dependencies and all 40 checklist rows',async()=>{
 const zip=await JSZip.loadAsync(await fs.readFile('product/site-handoff-kit.zip'));
 const html=await zip.file('Site Handoff Kit/handover-builder.html').async('string');
 assert.ok(!html.includes('<script src='));assert.ok(!html.includes('<link rel="stylesheet"'));assert.ok(html.includes('data-mode="offline"'));
 const csv=await zip.file('Site Handoff Kit/launch-checklist.csv').async('string');assert.equal(csv.split('\r\n').length,41);
});
