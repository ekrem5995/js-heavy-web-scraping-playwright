# STEP 1 — save your logged-in + captcha-passed state
import asyncio
from playwright.async_api import async_playwright

async def save_state():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.sahibinden.com/")
        input("Solve CAPTCHA manually, then press ENTER here...")
        await context.storage_state(path="storage_state.json")
        await browser.close()

asyncio.run(save_state())
