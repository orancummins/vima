"""Targeted discovery: explore an existing project detail page.

Loads the BINLookup project-details page to find key management options.
"""
from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).parent
SHOTS = ROOT / "logs" / "screenshots"
DOM = ROOT / "logs" / "dom"

LOGIN_URL = "https://developer.mastercard.com/account/log-in"
LOGIN_PATH = "/account/log-in"

for d in (SHOTS, DOM):
    d.mkdir(parents=True, exist_ok=True)


async def safe_settle(page, ms=5000):
    try:
        await page.wait_for_load_state("domcontentloaded", timeout=ms)
    except Exception:
        pass
    await asyncio.sleep(2)


async def snap(page, label):
    out = SHOTS / f"{label}.png"
    try:
        await page.screenshot(path=str(out), full_page=True)
        print(f"  📸 {out.name}")
    except Exception as e:
        print(f"  ⚠ screenshot: {e}")


async def dump(page, label):
    out = DOM / f"{label}.html"
    try:
        out.write_text(await page.content())
        print(f"  📄 {out.name}")
    except Exception as e:
        print(f"  ⚠ dump: {e}")


async def inventory(page):
    result = {}
    for key, js in {
        "buttons": """Array.from(document.querySelectorAll('button,[role=button]'))
            .filter(b=>b.offsetParent!==null)
            .map(b=>({text:(b.innerText||'').trim().slice(0,80),id:b.id||null,
                      testid:b.getAttribute('data-testid'),aria:b.getAttribute('aria-label'),
                      cls:(b.className||'').toString().slice(0,80)}))
            .filter(b=>b.text||b.aria||b.testid)""",
        "links": """Array.from(document.querySelectorAll('a[href]'))
            .filter(a=>a.offsetParent!==null)
            .map(a=>({text:(a.innerText||'').trim().slice(0,60),href:a.href}))
            .filter(a=>a.text)""",
        "headings": """Array.from(document.querySelectorAll('h1,h2,h3,h4'))
            .filter(h=>h.offsetParent!==null)
            .map(h=>h.innerText.trim().slice(0,100))""",
        "tabs": """Array.from(document.querySelectorAll('[role=tab],[role=tablist] a'))
            .map(t=>({text:(t.innerText||'').trim(),selected:t.getAttribute('aria-selected')}))""",
    }.items():
        try:
            result[key] = await page.evaluate(js)
        except Exception:
            result[key] = []
    return result


async def wait_for_login(page):
    print(f"\n🔐 Log in to Mastercard Developers...")
    while True:
        if LOGIN_PATH not in page.url and page.url.startswith("http"):
            print(f"✅ Authenticated — {page.url}")
            return
        await asyncio.sleep(1.5)


async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False, slow_mo=300)
        context = await browser.new_context(accept_downloads=True)
        page = await context.new_page()

        await page.goto(LOGIN_URL, wait_until="domcontentloaded")
        await wait_for_login(page)
        await safe_settle(page)

        # ── Dashboard: get all project links ─────────────────────────────────
        print("\n[1] Loading dashboard project list...")
        await page.goto("https://developer.mastercard.com/dashboard", wait_until="domcontentloaded")
        await safe_settle(page)

        project_links = await page.evaluate("""
            Array.from(document.querySelectorAll('a[href*="/project-details/"]'))
                .map(a=>({name:(a.innerText||'').trim(), href:a.href}))
                .filter(a=>a.name)
        """)
        print(f"  Projects: {json.dumps(project_links, indent=2)}")

        # ── Open each project and explore ────────────────────────────────────
        for proj in project_links:
            name = proj["name"]
            href = proj["href"]
            label = name.replace(" ", "_").lower()
            print(f"\n[2] Opening project: {name!r} → {href}")
            await page.goto(href, wait_until="domcontentloaded")
            await safe_settle(page)

            inv = await inventory(page)
            print(f"  URL: {page.url}")
            print(f"  Headings: {inv['headings']}")
            print(f"  Tabs: {inv['tabs']}")
            print(f"  Buttons: {[b['text'] for b in inv['buttons']]}")

            await snap(page, f"proj_{label}")
            await dump(page, f"proj_{label}")

            # Look for any key/certificate section tabs
            for tab_text in ["Keys", "API Keys", "Certificates", "Security", "Credentials"]:
                try:
                    loc = page.locator(f"[role=tab]:has-text('{tab_text}'), a:has-text('{tab_text}'), button:has-text('{tab_text}')").first
                    if await loc.is_visible(timeout=800):
                        print(f"  ✓ Found tab/link: {tab_text!r}")
                        await loc.click()
                        await safe_settle(page)
                        inv2 = await inventory(page)
                        print(f"    After clicking {tab_text!r}:")
                        print(f"    Headings: {inv2['headings']}")
                        print(f"    Buttons: {[b['text'] for b in inv2['buttons']]}")
                        await snap(page, f"proj_{label}_{tab_text.lower()}_tab")
                        await dump(page, f"proj_{label}_{tab_text.lower()}_tab")
                        break
                except Exception:
                    pass

        print("\n\n✅ Discovery complete.")
        print(f"📂 Screenshots → {SHOTS}")
        print(f"📂 DOM → {DOM}")
        print("\nBrowser stays open 60s for manual exploration...")
        try:
            await asyncio.sleep(60)
        except KeyboardInterrupt:
            pass
        await browser.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(130)
