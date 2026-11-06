import {defineConfig} from '@playwright/test';
export default defineConfig({
 testDir:'./tests/browser',fullyParallel:true,timeout:30000,
 use:{baseURL:'http://127.0.0.1:8788',headless:true},
 webServer:{command:'npx wrangler pages dev public --port 8788',url:'http://127.0.0.1:8788',reuseExistingServer:!process.env.CI,timeout:60000},
 reporter:'list'
});
