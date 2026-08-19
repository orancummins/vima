"""Throwaway discovery for the 'Add key' (Developers API Keys) modal/form.

Uses the cached session_state.json. Navigates to the account page, clicks
'Add key', waits, then dumps a screenshot + an inventory of all inputs,
buttons, labels, and dialog text so we can craft correct selectors.

Run:
    $env:PLAYWRIGHT_BROWSER_CHANNEL='chrome'
    .venv\\Scripts\\python.exe discover_admin_key.py
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


async def inventory(page) -> dict:
    return await page.evaluate(
        """() => {
            const vis = el => el.offsetParent !== null;
            const q = sel => Array.from(document.querySelectorAll(sel)).filter(vis);
            return {
                url: location.href,
                inputs: q('input, textarea, select').map(i => ({
                    tag: i.tagName, type: i.type||null, name: i.name||null, id: i.id||null,
                    placeholder: i.placeholder||null, testid: i.getAttribute('data-testid'),
                    aria: i.getAttribute('aria-label'),
                })),
                buttons: q("button, [role=button], a").map(b => ({
                    text: (b.innerText||b.value||'').trim().slice(0,60),
                    testid: b.getAttribute('data-testid'),
                    aria: b.getAttribute('aria-label'), href: b.getAttribute('href'),
                })).filter(b => b.text || b.testid),
                labels: q('label').map(l => ({
                    text: (l.innerText||'').trim().slice(0,60), for: l.getAttribute('for'),
                })),
                dialogs: q("[role=dialog], .modal, [class*=modal], [class*=Modal]").map(d => ({
                    testid: d.getAttribute('data-testid'),
                    text: (d.innerText||'').trim().slice(0,400),
                })),
                headings: q('h1,h2,h3,h4').map(h => (h.innerText||'').trim().slice(0,80)),
            };
        }"""
    )


async def main() -> None:
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True, channel="chrome")
        ctx = await browser.new_context(
            storage_state=str(STATE) if STATE.exists() else None,
            accept_downloads=True,
        )
        page = await ctx.new_page()
        await page.goto("https://developer.mastercard.com/account/profile", wait_until="domcontentloaded")
        await asyncio.sleep(3)

        before = await inventory(page)
        (OUT / "01_account.json").write_text(json.dumps(before, indent=2))
        await page.screenshot(path=str(OUT / "01_account.png"), full_page=True)

        # Click 'Add key'
        add = page.locator("text='Add key'").first
        if await add.count() == 0:
            add = page.locator("a:has-text('Add key'), button:has-text('Add key')").first
        print("Add key count:", await add.count())
        await add.scroll_into_view_if_needed()
        await add.click(force=True)
        await asyncio.sleep(3)

        after = await inventory(page)
        (OUT / "02_after_add_key.json").write_text(json.dumps(after, indent=2))
        await page.screenshot(path=str(OUT / "02_after_add_key.png"), full_page=True)
        print("URL after click:", after["url"])
        print("Headings:", after["headings"])
        print("Inputs:", json.dumps(after["inputs"], indent=2))
        print("Dialog count:", len(after["dialogs"]))
        for d in after["dialogs"]:
            print("DIALOG:", d["text"][:300])

        await ctx.close()
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
