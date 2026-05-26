"""Discover the /sandbox sub-page of a project (where keys live)."""
import asyncio, json, re, time
from pathlib import Path
from playwright.async_api import async_playwright

LOGIN_URL = "https://developer.mastercard.com/account/log-in"
# "Testing BIN Lookup" project - has /sandbox link
SANDBOX_URL = "https://developer.mastercard.com/project-details/09472f05-c0de-47d8-bdb5-72fff12c1543/sandbox"
SS_DIR = Path("logs/screenshots")
DOM_DIR = Path("logs/dom")
SS_DIR.mkdir(parents=True, exist_ok=True)
DOM_DIR.mkdir(parents=True, exist_ok=True)

async def safe_settle(page, timeout=3000):
    try:
        await page.wait_for_load_state("domcontentloaded", timeout=timeout)
    except Exception:
        pass
    try:
        await page.wait_for_load_state("networkidle", timeout=timeout)
    except Exception:
        pass
    await asyncio.sleep(2)

async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False, slow_mo=200)
        ctx = await browser.new_context()
        page = await ctx.new_page()

        print("🔐 Log in...")
        await page.goto(LOGIN_URL)
        # Wait for login
        while True:
            if "/account/log-in" not in page.url:
                break
            await asyncio.sleep(1)
        print(f"✅ Authenticated — {page.url}")

        print(f"\n[1] Navigating to sandbox page: {SANDBOX_URL}")
        await page.goto(SANDBOX_URL)
        await safe_settle(page)

        await page.screenshot(path=str(SS_DIR / "sandbox_page.png"), full_page=True)
        (DOM_DIR / "sandbox_page.html").write_text(await page.content())

        # Dump structure
        print(f"  URL: {page.url}")

        headings = await page.eval_on_selector_all("h1,h2,h3,h4", "els => els.map(e => e.innerText.trim())")
        print(f"  Headings: {headings}")

        buttons = await page.eval_on_selector_all("button", "els => els.map(e => e.innerText.trim())")
        print(f"  Buttons: {[b for b in buttons if b]}")

        links = await page.eval_on_selector_all("a", "els => els.map(e => ({text: e.innerText.trim(), href: e.href}))")
        relevant = [l for l in links if any(k in l['href'] for k in ['sandbox','key','download','certif','p12','pem'])]
        print(f"  Relevant links: {json.dumps(relevant, indent=2)}")

        # Look for tables, cards, sections with key info
        tables = await page.eval_on_selector_all("table", "els => els.map(e => e.innerText.trim())")
        if tables:
            print(f"  Tables:\n{tables}")

        # Look for any text content mentioning keys
        body_text = await page.eval_on_selector("body", "el => el.innerText")
        for line in body_text.split('\n'):
            line = line.strip()
            if line and any(k in line.lower() for k in ['key', 'certif', 'download', 'p12', '.pem', 'sandbox', 'regenerat', 'consumer']):
                print(f"  TEXT: {line}")

        # Check for specific elements
        for sel in [
            "button:has-text('Download')",
            "button:has-text('Regenerate')",
            "button:has-text('Generate')",
            "[data-testid*='key']",
            "[data-testid*='download']",
            "[data-testid*='certif']",
            "a[href*='.p12']",
            "a[href*='.pem']",
        ]:
            try:
                count = await page.locator(sel).count()
                if count > 0:
                    text = await page.locator(sel).first.inner_text()
                    print(f"  FOUND [{sel}]: {count} match(es) — '{text}'")
            except Exception as e:
                pass

        print("\n📸 sandbox_page.png saved")
        print("⏳ Keeping browser open 60s for manual exploration...")

        # Also try clicking on each "API" card/section to see if there's key info there
        await asyncio.sleep(60)
        await browser.close()

asyncio.run(main())
