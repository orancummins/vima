"""Login + DOM discovery in one run.

Launches headful Chromium, waits for you to log in, then methodically
explores the portal capturing screenshots, HTML dumps, and a JSON report
of buttons/links/inputs at each step so we can build real selectors.

Outputs:
    logs/screenshots/*.png
    logs/dom/*.html
    logs/discovery.json
"""
from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path
from typing import Any

from playwright.async_api import Page, TimeoutError as PWTimeoutError, async_playwright

ROOT = Path(__file__).parent
SHOTS = ROOT / "logs" / "screenshots"
DOM = ROOT / "logs" / "dom"
REPORT = ROOT / "logs" / "discovery.json"

LOGIN_URL = "https://developer.mastercard.com/account/log-in"
LOGIN_PATH = "/account/log-in"

for d in (SHOTS, DOM):
    d.mkdir(parents=True, exist_ok=True)

report: dict[str, Any] = {"steps": []}


def step(label: str) -> dict:
    s = {"label": label, "url": None, "buttons": [], "links": [], "inputs": [], "headings": []}
    report["steps"].append(s)
    return s


async def snap(page: Page, label: str) -> None:
    safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in label)
    out = SHOTS / f"{safe}.png"
    try:
        await page.screenshot(path=str(out), full_page=True)
        print(f"  📸 {out.name}")
    except Exception as e:
        print(f"  ⚠ screenshot failed: {e}")


async def dump(page: Page, label: str) -> None:
    safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in label)
    try:
        html = await page.content()
        (DOM / f"{safe}.html").write_text(html)
        print(f"  📄 {safe}.html")
    except Exception as e:
        print(f"  ⚠ dump failed: {e}")


async def inventory(page: Page, s: dict) -> None:
    """Capture all interactive elements visible on the page."""
    s["url"] = page.url
    try:
        s["buttons"] = await page.evaluate(
            """Array.from(document.querySelectorAll('button, [role=button], input[type=button], input[type=submit]'))
                .filter(b => b.offsetParent !== null)
                .map(b => ({text: (b.innerText||b.value||'').trim().slice(0,80), id: b.id||null,
                            testid: b.getAttribute('data-testid'),
                            aria: b.getAttribute('aria-label'),
                            classes: (b.className||'').toString().slice(0,120)}))
                .filter(b => b.text || b.aria || b.testid)"""
        )
    except Exception:
        pass
    try:
        s["links"] = await page.evaluate(
            """Array.from(document.querySelectorAll('a[href]'))
                .filter(a => a.offsetParent !== null)
                .map(a => ({text: (a.innerText||'').trim().slice(0,80), href: a.href,
                            testid: a.getAttribute('data-testid')}))
                .filter(a => a.text || a.testid)"""
        )
    except Exception:
        pass
    try:
        s["inputs"] = await page.evaluate(
            """Array.from(document.querySelectorAll('input, textarea, select'))
                .filter(i => i.offsetParent !== null)
                .map(i => ({type: i.type||i.tagName, name: i.name, id: i.id,
                            placeholder: i.placeholder, label: i.getAttribute('aria-label'),
                            testid: i.getAttribute('data-testid')}))"""
        )
    except Exception:
        pass
    try:
        s["headings"] = await page.evaluate(
            """Array.from(document.querySelectorAll('h1, h2, h3'))
                .filter(h => h.offsetParent !== null)
                .map(h => ({level: h.tagName, text: h.innerText.trim().slice(0,120)}))"""
        )
    except Exception:
        pass


async def safe_settle(page: Page, timeout_ms: int = 8000) -> None:
    """Best-effort wait. Dashboards with persistent connections never hit networkidle."""
    try:
        await page.wait_for_load_state("domcontentloaded", timeout=timeout_ms)
    except Exception:
        pass
    try:
        await page.wait_for_load_state("networkidle", timeout=timeout_ms)
    except Exception:
        pass
    await asyncio.sleep(1.5)


async def wait_for_login(page: Page, timeout_s: float = 600) -> None:
    print(f"\n🔐 Waiting up to {int(timeout_s)}s for manual login. Complete sign-in + MFA in the browser...")
    start = asyncio.get_event_loop().time()
    while True:
        if LOGIN_PATH not in page.url and page.url.startswith("http"):
            print(f"✅ Authenticated — at {page.url}")
            return
        if asyncio.get_event_loop().time() - start > timeout_s:
            raise PWTimeoutError("Login timeout")
        await asyncio.sleep(1.5)


async def try_click(page: Page, *candidates: str, label: str = "") -> str | None:
    """Try each selector; click the first visible one. Returns the matching selector."""
    for sel in candidates:
        try:
            loc = page.locator(sel).first
            if await loc.is_visible(timeout=1500):
                print(f"  → clicking {sel!r}  ({label})")
                await loc.click()
                await safe_settle(page)
                return sel
        except Exception:
            continue
    return None


async def main() -> None:
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False, slow_mo=200, args=["--foreground"])
        context = await browser.new_context(accept_downloads=True)
        page = await context.new_page()
        await page.bring_to_front()

        # ── 1. LOGIN ────────────────────────────────────────────────────────
        print(f"🌐 Opening {LOGIN_URL}")
        await page.goto(LOGIN_URL, wait_until="domcontentloaded")
        await wait_for_login(page)

        # ── 2. POST-LOGIN LANDING ───────────────────────────────────────────
        await safe_settle(page)
        s = step("01-post-login-landing")
        await inventory(page, s)
        await snap(page, "01-post-login-landing")
        await dump(page, "01-post-login-landing")

        # ── 3. DASHBOARD ────────────────────────────────────────────────────
        print("\n📍 Navigating to /dashboard")
        try:
            await page.goto("https://developer.mastercard.com/dashboard", wait_until="domcontentloaded")
            await safe_settle(page)
        except Exception as e:
            print(f"  ⚠ dashboard nav failed: {e}")
        s = step("02-dashboard")
        await inventory(page, s)
        await snap(page, "02-dashboard")
        await dump(page, "02-dashboard")
        print(f"  Headings: {[h['text'] for h in s['headings']]}")
        print(f"  Buttons: {[b['text'] for b in s['buttons'][:15]]}")
        print(f"  Project links: {[l for l in s['links'] if '/project' in l.get('href','')][:10]}")

        # ── 4. PROJECTS PAGE ────────────────────────────────────────────────
        print("\n📍 Looking for projects area")
        clicked = await try_click(
            page,
            "a:has-text('My Projects')",
            "a:has-text('Projects')",
            "a[href*='/projects']",
            "[data-testid*='projects-nav']",
            label="projects nav",
        )
        s = step("03-projects-page")
        await inventory(page, s)
        await snap(page, "03-projects-page")
        await dump(page, "03-projects-page")
        if not clicked:
            print("  (no Projects nav link clicked — page may already show projects)")

        # ── 5. CREATE PROJECT ───────────────────────────────────────────────
        print("\n📍 Looking for Create Project button")
        clicked = await try_click(
            page,
            "button:has-text('Create a new project')",
            "a:has-text('Create a new project')",
            "button:has-text('Create new project')",
            "button:has-text('Create project')",
            "button:has-text('New project')",
            "button:has-text('Add project')",
            "a:has-text('Create')",
            "[data-testid*='create-project']",
            label="create project",
        )
        s = step("04-create-project")
        await inventory(page, s)
        await snap(page, "04-create-project")
        await dump(page, "04-create-project")
        if clicked:
            print(f"  ✅ Create-project trigger: {clicked!r}")
            print(f"  Inputs on form: {s['inputs']}")
            print(f"  Buttons on form: {[b['text'] for b in s['buttons']]}")
        else:
            print("  ❌ Could not find a Create Project button.")

        # ── 6. EXIT create-project modal and explore an existing project ────
        print("\n📍 Exiting create-project modal")
        await try_click(page, "button:has-text('Exit')", label="exit modal")
        await safe_settle(page)

        print("\n📍 Opening an existing project (first project link)")
        try:
            first_proj = page.locator("a[href*='/project-details/']").first
            href = await first_proj.get_attribute("href")
            name = (await first_proj.inner_text()).strip()
            print(f"  → {name}: {href}")
            await first_proj.click()
            await safe_settle(page)
        except Exception as e:
            print(f"  ⚠ could not open project: {e}")

        s = step("05-project-details")
        await inventory(page, s)
        await snap(page, "05-project-details")
        await dump(page, "05-project-details")
        print(f"  URL: {s['url']}")
        print(f"  Headings: {[h['text'] for h in s['headings']]}")
        print(f"  Buttons: {[b['text'] for b in s['buttons']]}")
        print(f"  Tabs/links: {[l['text'] for l in s['links'] if l['text']][:20]}")

        # ── 7. LOOK FOR "ADD API" / KEYS SECTION ────────────────────────────
        print("\n📍 Looking for Add API / Keys controls")
        for sel, lbl in [
            ("button:has-text('Add API')", "Add API button"),
            ("a:has-text('Add API')", "Add API link"),
            ("button:has-text('Add an API')", "Add an API"),
            ("a:has-text('Keys')", "Keys tab"),
            ("button:has-text('Keys')", "Keys tab btn"),
            ("a:has-text('API Keys')", "API Keys tab"),
            ("button:has-text('Add Key')", "Add Key btn"),
            ("button:has-text('Generate')", "Generate btn"),
            ("button:has-text('Download')", "Download btn"),
        ]:
            try:
                loc = page.locator(sel).first
                if await loc.is_visible(timeout=600):
                    print(f"  ✓ visible: {sel!r}  ({lbl})")
            except Exception:
                pass

        # Try clicking a Keys tab if present
        print("\n📍 Trying to open the Keys section")
        clicked = await try_click(
            page,
            "a:has-text('Keys')",
            "button:has-text('Keys')",
            "a:has-text('API Keys')",
            "[role=tab]:has-text('Keys')",
            label="Keys tab",
        )
        s = step("06-keys-section")
        await inventory(page, s)
        await snap(page, "06-keys-section")
        await dump(page, "06-keys-section")
        print(f"  Headings: {[h['text'] for h in s['headings']]}")
        print(f"  Buttons: {[b['text'] for b in s['buttons']]}")

        # ── 6. SAVE REPORT ──────────────────────────────────────────────────
        REPORT.write_text(json.dumps(report, indent=2))
        print(f"\n📊 Report → {REPORT}")
        print(f"📂 Screenshots → {SHOTS}")
        print(f"📂 DOM dumps → {DOM}")

        print("\n👀 Browser stays open for 60s so you can manually explore...")
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
