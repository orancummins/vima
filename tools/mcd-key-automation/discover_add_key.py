"""Discover the add-project-key page form structure."""
import asyncio, re
from pathlib import Path
from playwright.async_api import async_playwright

LOGIN_URL = "https://developer.mastercard.com/account/log-in"
ADD_KEY_URL = "https://developer.mastercard.com/project-details/09472f05-c0de-47d8-bdb5-72fff12c1543/sandbox/add-project-key"
SS_DIR = Path("logs/screenshots")
DOM_DIR = Path("logs/dom")

async def safe_settle(page, timeout=3000):
    for state in ("domcontentloaded", "networkidle"):
        try:
            await page.wait_for_load_state(state, timeout=timeout)
        except Exception:
            pass
    await asyncio.sleep(2)

async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False, slow_mo=200, args=["--foreground"])
        ctx = await browser.new_context()
        page = await ctx.new_page()
        await page.bring_to_front()

        print("🔐 Log in...")
        await page.goto(LOGIN_URL)
        while "/account/log-in" in page.url:
            await asyncio.sleep(1)
        print(f"✅ Authenticated")

        print(f"\n[1] Navigating to add-project-key page...")
        await page.goto(ADD_KEY_URL)
        await safe_settle(page)

        await page.screenshot(path=str(SS_DIR / "add_project_key.png"), full_page=True)
        (DOM_DIR / "add_project_key.html").write_text(await page.content())

        print(f"  URL: {page.url}")
        headings = await page.eval_on_selector_all("h1,h2,h3,h4", "els => els.map(e => e.innerText.trim())")
        print(f"  Headings: {headings}")
        buttons = await page.eval_on_selector_all("button", "els => els.map(e => e.innerText.trim())")
        print(f"  Buttons: {[b for b in buttons if b]}")

        # Look for form inputs
        inputs = await page.eval_on_selector_all("input,select,textarea", """els => els.map(e => ({
            tag: e.tagName, type: e.type, name: e.name, id: e.id,
            placeholder: e.placeholder, 'data-testid': e.getAttribute('data-testid'),
            label: e.getAttribute('aria-label') || e.getAttribute('aria-labelledby')
        }))""")
        print(f"  Inputs: {inputs}")

        # Look for labels
        labels = await page.eval_on_selector_all("label", "els => els.map(e => ({text: e.innerText.trim(), for: e.htmlFor}))")
        print(f"  Labels: {labels}")

        body_text = await page.eval_on_selector("body", "el => el.innerText")
        for line in body_text.split('\n'):
            line = line.strip()
            if line and any(k in line.lower() for k in ['key', 'name', 'download', 'generate', 'certif', 'password']):
                print(f"  TEXT: {line}")

        print("\n📸 add_project_key.png saved")
        print("⏳ Keeping browser open 60s...")
        await asyncio.sleep(60)
        await browser.close()

asyncio.run(main())
