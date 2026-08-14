"""Watch a manual project deletion via timed screenshots.

Run:
    .venv/Scripts/python.exe record_delete.py

Opens the browser at the first SST-* project and takes a screenshot every
second until the project disappears from the dashboard.
"""
import asyncio
from pathlib import Path
from browser.session import browser_session
from providers.mastercard.pages.login_page import LoginPage
from providers.mastercard.pages.dashboard_page import DashboardPage

LOGIN_URL = "https://developer.mastercard.com/account/log-in"
SHOTS = Path("logs/screenshots/delete_recording")
DOM   = Path("logs/dom/delete_recording")
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
        sst = [(await l.inner_text(), await l.get_attribute("href")) for l in links]
        sst = [(n.strip(), h) for n, h in sst if n.strip().startswith("SST-")]

        if not sst:
            print("No SST-* projects found on dashboard.")
            return

        name, href = sst[0]
        url = href if href.startswith("http") else "https://developer.mastercard.com" + href
        print(f"\nProject: {name}")
        print(f"URL: {url}")
        print("\nNavigating to project page...")
        await page.goto(url, wait_until="domcontentloaded")
        try:
            await page.wait_for_load_state("networkidle", timeout=10000)
        except Exception:
            pass
        await asyncio.sleep(2)

        print("\n" + "="*60)
        print("READY. Please delete this project manually.")
        print("Taking a screenshot every second. Press Ctrl+C when done.")
        print("="*60 + "\n")

        frame = 0
        prev_url = ""
        while frame < 300:
            await asyncio.sleep(1)
            frame += 1
            cur_url = page.url

            # Always snapshot on URL change; otherwise every 3s
            if cur_url != prev_url or frame % 3 == 0:
                shot = SHOTS / f"frame_{frame:04d}.png"
                dom  = DOM   / f"frame_{frame:04d}.html"
                try:
                    await page.screenshot(path=str(shot), full_page=True)
                    dom.write_text(await page.content(), encoding="utf-8")
                    print(f"  [{frame:3d}s] {shot.name}  url={cur_url}")
                except Exception:
                    pass
                prev_url = cur_url

            # Stop once back on dashboard and project is gone
            if "/dashboard" in cur_url:
                count = await page.locator(f"a[href*='/project-details/']:has-text({name!r})").count()
                if count == 0:
                    print(f"\nProject '{name}' is gone!")
                    break
        else:
            print("Timeout.")

        print(f"\nScreenshots saved to: {SHOTS}")
        print(f"DOM dumps saved to:   {DOM}")


if __name__ == "__main__":
    asyncio.run(main())
