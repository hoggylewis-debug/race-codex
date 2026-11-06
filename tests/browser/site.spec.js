import {test,expect} from '@playwright/test';
import path from 'node:path';
test('free preview personalises safely and exports a sample',async({page})=>{
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto('/');
 await expect(page.getByRole('heading',{name:'Finish the site.'})).toBeVisible();
 await page.locator('[name=client]').fill('Acme <script>alert(1)</script>');
 await expect(page.frameLocator('#preview').locator('h1')).toContainText('Your website');
 await expect(page.frameLocator('#preview').locator('body')).toContainText('Acme <script>alert(1)</script>');
 const downloadPromise=page.waitForEvent('download');await page.locator('#download-guide').click();
 const download=await downloadPromise;expect(download.suggestedFilename()).toContain('-sample.html');
 await expect(page.locator('#buy')).toBeHidden();
 await expect(page.locator('#sales-status')).toContainText('Sales aren’t open yet');
 expect(errors).toEqual([]);
});
test('mobile layout fits and the form remains usable',async({page})=>{
 await page.setViewportSize({width:375,height:812});await page.goto('/');
 expect(await page.evaluate(()=>document.documentElement.scrollWidth)).toBeLessThanOrEqual(375);
 await page.locator('[name=client]').fill('Small Screen Studio');
 await expect(page.frameLocator('#preview').locator('body')).toContainText('Small Screen Studio');
 await page.screenshot({path:'test-results/mobile.png',fullPage:true});
});
test('privacy, terms, support and checklist exist and display the experiment footer',async({page})=>{
 for(const route of ['/privacy','/terms','/support','/website-handover-checklist']){
  await page.goto(route);await expect(page.locator('footer')).toContainText('Built and run by an AI agent');
 }
 await expect(page.locator('.checklist input')).toHaveCount(40);
 await page.locator('.checklist input').first().check();await expect(page.locator('.checklist input').first()).toBeChecked();
});
test('offline product runs from a local file, exports, saves and reloads without network',async({page})=>{
 const requests=[];page.on('request',r=>{if(r.url().startsWith('http'))requests.push(r.url())});
 await page.goto('file://'+path.resolve('product/offline-builder.html'));
 await page.locator('[name=client]').fill('Offline Client');
 await page.locator('[name=platform]').selectOption('Webflow');
 await expect(page.frameLocator('#preview').locator('body')).toContainText('Offline Client');
 await expect(page.frameLocator('#preview').locator('body')).toContainText('Add a CMS item');
 const savePromise=page.waitForEvent('download');await page.locator('#save-project').click();const saved=await savePromise;const filePath=await saved.path();
 await page.locator('[name=client]').fill('Changed');await page.locator('#load-project').setInputFiles(filePath);
 await expect(page.locator('[name=client]')).toHaveValue('Offline Client');
 const guidePromise=page.waitForEvent('download');await page.locator('#download-guide').click();const guide=await guidePromise;expect(guide.suggestedFilename()).toBe('offline-client-handover.html');
 expect(requests).toEqual([]);
});
test('missing checkout reference shows a useful recovery message',async({page})=>{
 await page.goto('/success');await expect(page.locator('#download-status')).toContainText('No valid checkout reference');await expect(page.locator('#download-kit')).toBeHidden();
});
