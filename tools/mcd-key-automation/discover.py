"""DOM discovery script.

Loads the saved session state and navigates the Mastercard Developers portal,
capturing screenshots and HTML snippets at each step so we can build real selectors.

Usage (from tools/mcd-key-automation directory, venv active):
    python discover.py
"""
from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

from playwright.async_api import async_playwright

ROOT = Path(__file__).parent
SESSION_STATE = ROOT / "session_state.json"
SCREENSHOTS_DIR = ROOT / "logs" / "screenshots"
DOM_DIR = ROOT / "logs" / "dom"

SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
DOM_DIR.mkdir(parents=True, exist_ok=True)


async def snap(page, label: str) -> None:
    safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in label)
    out = SCREENSHOTS_DIR / f"{safe}.png"
    await page.screenshot(path=str(out), full_page=True)
    print(f"  📸 {out}")


async def dump_html(page, label: str, selector: str = "body") -> None:
    safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in label)
    try:
        html = await page.inner_html(selector)
    except Exception:
        html = await page.content()
    out = DOM_DIR / f"{safe}.html"
    out.write_text(html)
    print(f"  📄 {out}")


async def query_all_text(page, selector: str) -> list[str]:
    """Return inner_text of all matching elements."""
    try:
        els = await page.query_selector_all(selector)
        return [await e.inner_text() for e in els]
    except Exception:
        return []


async def find_links(page, pattern: str) -> list[dict]:
    """Return href+text for anchors containing pattern in href."""
    js = f"""
        Array.from(document.querySelectorAll('a[href]'))
            .filter(a => a.href.includes({json.dumps(pattern)}))
            .map(a => ({{href: a.href, text: a.innerText.trim(), id: a.id, cls: a.className}}))
    """
    try:
        return await page.evaluate(js)
    except Exception:
        return []


async def find_buttons(page) -> list[dict]:
    js = """
        Array.from(document.querySelectorAll('button, [role="button"], input[type="button"], input[type="submit"]'))
            .map(b => ({text: b.innerText.trim(), id: b.id, cls: b.className, disabled: b.disabled}))
            .filter(b => b.text.length > 0)
    """
    try:
        return await page.evaluate(js)
    except Exception:
        return []


async def main() -> None:
    if not SESSION_STATE.exists():
        print("❌ No session_state.json found. Run `mcd-key-automation login` first.")
        sys.exit(1)

    print("🔍 Starting DOM discovery (headful) — watch the browser window.")
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False, slow_mo=500)
        context = await browser.new_context(storage_state=str(SESSION_STATE), accept_downloads=True)
        page = await context.new_page()

        # ── STEP 1: Dashboard ────────────────────────────────────────────────
        print("\n[1] Navigating to dashboard...")
        await page.goto("https://developer.mastercard.com/dashboard", wait_until="networkidle")
        print(f"    URL: {page.url}")
        await snap(page, "01-dashboard")
        await dump_html(page, "01-dashboard")

        buttons = await find_buttons(page)
        print(f"    Buttons: {json.dumps(buttons, indent=2)}")

        nav_links = await find_links(page, "dashboard")
        print(f"    Dashboard links: {json.dumps(nav_links, indent=2)}")

        project_links = await find_links(page, "project")
        print(f"    Project links: {json.dumps(project_links[:20], indent=2)}")

        # ── STEP 2: Look for "My Projects" / project list area ───────────────
        print("\n[2] Looking for projects section...")
        # Common candidates
        candidates = [
            "[data-testid*='project']",
            "a[href*='/project']",
            "a[href*='/projects']",
            ".project-card",
            ".project-list",
            "h2, h3",
        ]
        for sel in candidates:
            texts = await query_all_text(page, sel)
            if texts:
                print(f"    {sel}: {texts[:10]}")

        # ── STEP 3: Try to navigate to a "create project" flow ───────────────
        print("\n[3] Looking for Create Project button...")
        create_sel_candidates = [
            "button:has-text('Create')",
            "button:has-text('New project')",
            "button:has-text('Add project')",
            "a:has-text('Create')",
            "a:has-text('New project')",
            "[data-testid*='create']",
        ]
        found_create = None
        for sel in create_sel_candidates:
            try:
                loc = page.locator(sel).first
                if await loc.is_visible(timeout=1000):
                    found_create = sel
                    text = await loc.inner_text()
                    print(f"    Found: {sel!r} → {text!r}")
                    break
            except Exception:
                pass

        if found_create:
            print(f"\n[4] Clicking {found_create!r}...")
            await page.locator(found_create).first.click()
            await page.wait_for_load_state("networkidle")
            print(f"    URL after click: {page.url}")
            await snap(page, "04-create-project-modal-or-page")
            await dump_html(page, "04-create-project-modal-or-page")
            buttons_after = await find_buttons(page)
            print(f"    Buttons: {json.dumps(buttons_after, indent=2)}")
        else:
            print("    ⚠ No Create Project button found on dashboard.")

        # ── STEP 4: Look for existing projects ───────────────────────────────
        print("\n[5] Checking for existing project cards/links...")
        all_proj = await find_links(page, "project")
        print(f"    Project-related links: {json.dumps(all_proj[:30], indent=2)}")

        print("\n✅ Discovery complete. Check logs/screenshots/ and logs/dom/")
        input("\nPress ENTER to close the browser...")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
