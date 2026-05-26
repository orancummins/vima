"""Discovery script: USOpenFinance sandbox page (OAuth 2.0 credentials + Signature Verification Key).

Run: python discover_ofin_sandbox.py
Requires: saved session_state.json (run mcd-key-automation login first if needed)
"""
from __future__ import annotations

import asyncio
import json
import textwrap
from pathlib import Path

from playwright.async_api import async_playwright

OFIN_UUID = "64a9380f-7109-4cab-8fd7-32dbe22ca067"
SANDBOX_URL = f"https://developer.mastercard.com/project-details/{OFIN_UUID}/sandbox"
SESSION_FILE = Path(__file__).parent / "session_state.json"
OUT_DIR = Path(__file__).parent / "logs"
OUT_DIR.mkdir(exist_ok=True)


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        ctx = await browser.new_context(storage_state=str(SESSION_FILE))
        page = await ctx.new_page()

        print(f"Navigating to {SANDBOX_URL} ...")
        await page.goto(SANDBOX_URL, wait_until="domcontentloaded")
        try:
            await page.wait_for_load_state("networkidle", timeout=6000)
        except Exception:
            pass
        await asyncio.sleep(3)

        # --- 1. Dump full page text for overview ---
        text = await page.inner_text("body")
        print("\n=== PAGE TEXT (first 3000 chars) ===")
        print(text[:3000])

        # --- 2. Look for credential fields ---
        print("\n=== CREDENTIAL SELECTORS ===")
        candidates = [
            "[data-testid*='partner']",
            "[data-testid*='app-key']",
            "[data-testid*='secret']",
            "[data-testid*='credential']",
            "input[type='password']",
            "input[type='text']",
            "[data-testid*='copy']",
            "button:has-text('Copy')",
            "[class*='credential']",
            "[class*='key-value']",
            "[class*='partner']",
        ]
        for sel in candidates:
            count = await page.locator(sel).count()
            if count:
                print(f"  {sel!r} → {count} element(s)")
                for i in range(min(count, 3)):
                    el = page.locator(sel).nth(i)
                    try:
                        tt = (await el.text_content() or "").strip()[:80]
                        ta = await el.get_attribute("data-testid") or ""
                        print(f"    [{i}] testid={ta!r} text={tt!r}")
                    except Exception:
                        pass

        # --- 3. Look for 'Add key' button (Signature Verification Key) ---
        print("\n=== ADD KEY BUTTONS ===")
        add_btns = [
            "button:has-text('Add key')",
            "a:has-text('Add key')",
            "[data-testid*='add-key']",
            "button:has-text('Download')",
        ]
        for sel in add_btns:
            count = await page.locator(sel).count()
            if count:
                print(f"  {sel!r} → {count}")
                for i in range(min(count, 5)):
                    el = page.locator(sel).nth(i)
                    try:
                        tt = (await el.text_content() or "").strip()[:80]
                        href = await el.get_attribute("href") or ""
                        ta = await el.get_attribute("data-testid") or ""
                        print(f"    [{i}] testid={ta!r} text={tt!r} href={href!r}")
                    except Exception:
                        pass

        # --- 4. Dump data-testid inventory ---
        print("\n=== ALL data-testid VALUES ===")
        elements = await page.query_selector_all("[data-testid]")
        seen: set[str] = set()
        for el in elements:
            tid = await el.get_attribute("data-testid") or ""
            if tid not in seen:
                seen.add(tid)
                txt = (await el.text_content() or "").strip()[:60]
                print(f"  {tid!r}: {txt!r}")

        # --- 5. Screenshot ---
        ss = OUT_DIR / "ofin_sandbox.png"
        await page.screenshot(path=str(ss), full_page=True)
        print(f"\nScreenshot saved: {ss}")

        # --- 6. Check if clicking 'Add key' opens something useful ---
        add_key_locator = page.locator("button:has-text('Add key')").first
        if await add_key_locator.count() > 0:
            print("\n=== Clicking first 'Add key' button ===")
            await add_key_locator.click()
            await asyncio.sleep(3)
            url_after = page.url
            print(f"URL after click: {url_after}")
            text2 = await page.inner_text("body")
            print(text2[:2000])
            ss2 = OUT_DIR / "ofin_add_key.png"
            await page.screenshot(path=str(ss2), full_page=True)
            print(f"Screenshot saved: {ss2}")

            # testids on the new page
            print("\n=== data-testids after click ===")
            elements2 = await page.query_selector_all("[data-testid]")
            seen2: set[str] = set()
            for el in elements2:
                tid = await el.get_attribute("data-testid") or ""
                if tid not in seen2:
                    seen2.add(tid)
                    txt = (await el.text_content() or "").strip()[:60]
                    print(f"  {tid!r}: {txt!r}")

        input("\nInspect the browser, then press Enter to close...")
        await browser.close()


asyncio.run(main())
