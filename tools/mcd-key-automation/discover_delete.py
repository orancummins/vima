"""One-shot discovery: find the delete trigger on a project settings page."""
import asyncio
from pathlib import Path
from browser.session import browser_session
from providers.mastercard.pages.login_page import LoginPage
from providers.mastercard.pages.dashboard_page import DashboardPage

LOGIN_URL = "https://developer.mastercard.com/account/log-in"
SHOTS = Path("logs/screenshots")
DOM   = Path("logs/dom")
SHOTS.mkdir(parents=True, exist_ok=True)
DOM.mkdir(parents=True, exist_ok=True)


async def main():
    async with browser_session() as (_b, _c, page):
        lp = LoginPage(page, LOGIN_URL)
        await lp.goto()
        await lp.wait_for_manual_auth()

        db = DashboardPage(page)
        await db.goto()
        links = await page.locator("a[href*='/project-details/']").all()
        projects = [(await l.inner_text(), await l.get_attribute("href")) for l in links]
        sst = [(n.strip(), h) for n, h in projects if n.strip().startswith("SST-")]
        print(f"SST projects: {[n for n,_ in sst]}")
        if not sst:
            print("No SST projects found — create one first then re-run.")
            return

        name, href = sst[0]
        url = href if href.startswith("http") else "https://developer.mastercard.com" + href
        print(f"\nOpening project page: {url}")
        await page.goto(url, wait_until="domcontentloaded")
        await asyncio.sleep(2)

        await page.screenshot(path=str(SHOTS / "del_01_project.png"), full_page=True)
        DOM.joinpath("del_01_project.html").write_text(await page.content(), encoding="utf-8")
        print("Saved del_01_project.*")

        # Try every candidate settings tab selector
        settings_sels = [
            "[data-testid='option-settings']",
            "[data-testid='tab-settings']",
            "[role='tab']:has-text('Settings')",
            "a:has-text('Settings')",
            "button:has-text('Settings')",
        ]
        for sel in settings_sels:
            loc = page.locator(sel)
            if await loc.count() > 0:
                print(f"Clicking settings tab via: {sel!r}")
                await loc.first.click()
                await asyncio.sleep(1.5)
                break

        await page.screenshot(path=str(SHOTS / "del_02_settings.png"), full_page=True)
        DOM.joinpath("del_02_settings.html").write_text(await page.content(), encoding="utf-8")
        print("Saved del_02_settings.*")

        # Scroll to bottom
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(1)
        await page.screenshot(path=str(SHOTS / "del_03_settings_bottom.png"), full_page=False)
        print("Saved del_03_settings_bottom.png")

        # Dump ALL elements with their text/testid/visibility
        all_els = await page.evaluate("""
            Array.from(document.querySelectorAll("a,button,[role='button'],[role='menuitem'],input[type='submit']"))
                .map(e => ({
                    tag: e.tagName,
                    text: (e.innerText || e.textContent || '').trim().replace(/\\s+/g,' ').slice(0, 100),
                    vis:  e.offsetParent !== null,
                    testid: e.getAttribute('data-testid') || '',
                    id:    e.id || '',
                    cls:   (e.className || '').toString().slice(0, 60),
                }))
                .filter(e => e.text || e.testid)
        """)
        print(f"\nAll {len(all_els)} elements (vis=visible):")
        for e in all_els:
            flag = "VIS" if e["vis"] else "hid"
            print(f"  [{flag}] <{e['tag']}> testid={e['testid']!r:35} id={e['id']!r:20} text={e['text']!r}")


if __name__ == "__main__":
    asyncio.run(main())
