"""Dump the 'Developers API Keys' table rows on the Account page.

Uses the cached session. Prints every element in the section with a
data-testid plus the section's full text so we can build a reliable
per-row extractor (key name, consumer key, status).
"""
from __future__ import annotations

import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).parent
STATE = ROOT / "session_state.json"
OUT = ROOT / "logs" / "admin_key_discovery"
OUT.mkdir(parents=True, exist_ok=True)


async def main() -> None:
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True, channel="chrome")
        ctx = await browser.new_context(
            storage_state=str(STATE) if STATE.exists() else None,
            accept_downloads=True,
        )
        page = await ctx.new_page()
        await page.goto("https://developer.mastercard.com/account/profile", wait_until="domcontentloaded")
        # Wait for the SPA to render the section (poll for the heading text).
        for _ in range(30):
            try:
                if await page.locator("text=/Developers API Keys/i").first.count() > 0 \
                        and await page.locator("text=/Developers API Keys/i").first.is_visible():
                    break
            except Exception:
                pass
            await asyncio.sleep(1)
        await asyncio.sleep(2)

        data = await page.evaluate(
            """() => {
                const vis = el => el.offsetParent !== null;
                // Find the 'Developers API Keys' section container.
                const all = Array.from(document.querySelectorAll('*'));
                const hdr = all.find(e => /Developers API Keys/i.test(e.textContent||'')
                    && e.children.length < 3 && (e.tagName||'').match(/H[1-4]|SPAN|DIV|P/));
                let section = hdr;
                for (let i=0;i<6 && section;i++){ section = section.parentElement; }
                const scope = section || document.body;
                const testids = Array.from(scope.querySelectorAll('[data-testid]'))
                    .filter(vis)
                    .map(e => ({testid: e.getAttribute('data-testid'),
                                tag: e.tagName,
                                text: (e.innerText||'').trim().slice(0,80)}));
                return {
                    sectionText: (scope.innerText||'').trim().slice(0,1500),
                    testids,
                };
            }"""
        )
        (OUT / "03_keys_table.json").write_text(json.dumps(data, indent=2))
        await page.screenshot(path=str(OUT / "03_keys_table.png"), full_page=True)
        print("SECTION TEXT:\n", data["sectionText"])
        print("\nTEST IDS:")
        for t in data["testids"]:
            print(f"  {t['testid']}  <{t['tag']}>  {t['text']!r}")

        await ctx.close()
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
