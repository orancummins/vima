"""Generic playbook replay engine for Mastercard portal flows.

Reads a recorded JSON playbook (see ``playbooks/README.md``) and executes
its steps against a Playwright ``Page``. Designed to be portal-API-agnostic
so a new API can be onboarded by recording its create-project flow once
and replaying it forever after.
"""
from __future__ import annotations

import asyncio
import json
import re
import time
from pathlib import Path
from typing import Any

from loguru import logger
from playwright.async_api import Page

from browser.downloads import save_download
from browser.screenshots import capture as screenshot


HERE = Path(__file__).resolve().parent
PLAYBOOK_ROOT = HERE.parent.parent / "playbooks"


# ---------------------------------------------------------------------------
# Variable regex (used by both loading and substitution)
# ---------------------------------------------------------------------------

_VAR_RE = re.compile(r"{{\s*([A-Za-z_][A-Za-z0-9_]*)\s*}}")

# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------


def playbook_path(organization: str, api_slug: str) -> Path:
    """Return the on-disk path to ``playbooks/<org>/<slug>.json``."""
    return PLAYBOOK_ROOT / organization / f"{api_slug}.json"


def find_playbook(organization: str, api_slug: str) -> Path | None:
    """Return the playbook path if present, else None."""
    candidate = playbook_path(organization, api_slug)
    return candidate if candidate.is_file() else None


def load_playbook(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text())
    if data.get("schema") != 1:
        raise ValueError(f"Unsupported playbook schema {data.get('schema')!r} in {path}")
    if "steps" not in data or not isinstance(data["steps"], list):
        raise ValueError(f"Playbook {path} missing 'steps' list")

    # Verify every {{variable}} referenced in step values is declared in the
    # playbook's top-level 'variables' list or 'defaults' dict.  This catches
    # missing declarations at load time rather than mid-provisioning-session.
    declared: set[str] = set(data.get("variables", []))
    declared |= set(data.get("defaults", {}).keys())
    missing: list[str] = []
    for step in data["steps"]:
        for v in step.values():
            if isinstance(v, str):
                for m in _VAR_RE.finditer(v):
                    name = m.group(1)
                    if name not in declared:
                        missing.append(f"{{{{{name}}}}} in step {step!r}")
    if missing:
        raise ValueError(
            f"Playbook {path} references undeclared variable(s): " + ", ".join(missing)
        )

    return data


# ---------------------------------------------------------------------------
# Variable substitution
# ---------------------------------------------------------------------------


def substitute(value: Any, variables: dict[str, str]) -> Any:
    """Replace ``{{name}}`` tokens in ``value`` from ``variables`` mapping."""
    if not isinstance(value, str):
        return value

    def repl(match: re.Match[str]) -> str:
        name = match.group(1)
        if name not in variables:
            raise KeyError(f"Playbook references undefined variable {name!r}")
        return str(variables[name])

    return _VAR_RE.sub(repl, value)


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------


class PlaybookRunner:
    """Execute a playbook against a Playwright page.

    Side effects: the runner records artifacts (downloads, screenshots) and
    populates ``self.result`` with structured data the caller can extract
    after ``run()`` returns:

      - ``self.downloads``: list of saved download Paths
      - ``self.final_url``: page URL after the last step
    """

    # Selectors / timeouts that the portal uses consistently across APIs.
    PROCEED_SELECTOR = "button[data-testid='proceed-btn']"

    def __init__(
        self,
        page: Page,
        playbook: dict[str, Any],
        variables: dict[str, str],
        *,
        dest_dir: Path,
        download_name_hint: str = "portal-keys",
    ) -> None:
        self.page = page
        self.playbook = playbook
        self.variables = variables
        self.dest_dir = dest_dir
        self.download_name_hint = download_name_hint
        self.downloads: list[Path] = []
        self.final_url: str | None = None

    # -- action dispatch ----------------------------------------------------

    async def run(self) -> None:
        steps = self.playbook["steps"]
        slug = self.playbook.get("api_slug", "?")
        logger.info("Playbook[{}]: replaying {} steps", slug, len(steps))

        # If the playbook specifies a start_url and the page isn't there yet,
        # navigate. (The caller is responsible for being authenticated.)
        start_url = self.playbook.get("start_url")
        if start_url and self.page.url != start_url:
            logger.info("Playbook[{}]: navigating to {}", slug, start_url)
            await self.page.goto(start_url, wait_until="domcontentloaded")
            await asyncio.sleep(1.0)

        for i, step in enumerate(steps, start=1):
            action = step.get("action")
            if not action:
                raise ValueError(f"Step {i} has no 'action': {step!r}")
            logger.info("Playbook[{}] step {}/{}: {}", slug, i, len(steps), action)
            handler = getattr(self, f"_do_{action}", None)
            if handler is None:
                raise ValueError(f"Unknown playbook action {action!r} at step {i}")
            await handler(step)
            # Small pause between steps so React handlers settle.
            await asyncio.sleep(step.get("post_sleep_ms", 300) / 1000.0)

        self.final_url = self.page.url
        logger.info("Playbook[{}]: complete; final_url={}", slug, self.final_url)

    # -- individual actions -------------------------------------------------

    def _val(self, step: dict[str, Any], key: str, default: Any = None) -> Any:
        if key not in step:
            if default is None:
                raise KeyError(f"Step missing required field {key!r}: {step!r}")
            return default
        return substitute(step[key], self.variables)

    async def _do_goto(self, step: dict[str, Any]) -> None:
        url = self._val(step, "url")
        await self.page.goto(url, wait_until="domcontentloaded")

    async def _do_sleep(self, step: dict[str, Any]) -> None:
        ms = int(step.get("ms", 500))
        await asyncio.sleep(ms / 1000.0)

    async def _do_screenshot(self, step: dict[str, Any]) -> None:
        name = step.get("name") or f"playbook_{int(time.time())}"
        await screenshot(self.page, name)

    async def _do_browser_notify(self, step: dict[str, Any]) -> None:
        """Inject a persistent banner into the visible browser window.

        Used to prompt the user for manual interaction (e.g. clicking a button
        that the portal's bot-detection blocks for automated input).  The banner
        is styled to stand out clearly above the page content and disappears
        automatically once the target selector appears (if ``dismiss_on`` is
        supplied).
        """
        message = self._val(step, "message", default="Action required — see terminal for instructions.")
        dismiss_on = step.get("dismiss_on", "")
        color = step.get("color", "#1a73e8")

        await self.page.evaluate(
            """
            ({ message, dismissOn, color }) => {
                // Remove any existing vima banner first.
                const old = document.getElementById('vima-notify-banner');
                if (old) old.remove();

                const banner = document.createElement('div');
                banner.id = 'vima-notify-banner';
                banner.innerHTML = `
                  <span style="font-size:22px;margin-right:10px;">👆</span>
                  <span>${message}</span>
                `;
                Object.assign(banner.style, {
                    position: 'fixed',
                    top: '0',
                    left: '0',
                    right: '0',
                    zIndex: '2147483647',
                    background: color,
                    color: '#fff',
                    fontFamily: 'system-ui, sans-serif',
                    fontSize: '16px',
                    fontWeight: '600',
                    padding: '14px 24px',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    boxShadow: '0 2px 8px rgba(0,0,0,0.3)',
                });
                document.body.prepend(banner);

                if (dismissOn) {
                    const observer = new MutationObserver(() => {
                        if (document.querySelector(dismissOn)) {
                            banner.style.background = '#188038';
                            banner.innerHTML = '<span style="font-size:22px;margin-right:10px;">✅</span><span>Key generated — downloading…</span>';
                            setTimeout(() => banner.remove(), 3000);
                            observer.disconnect();
                        }
                    });
                    observer.observe(document.body, { childList: true, subtree: true });
                }
            }
            """,
            {"message": message, "dismissOn": dismiss_on, "color": color},
        )
        logger.info("Playbook: browser notify shown — {}", message)

    async def _do_os_click(self, step: dict[str, Any]) -> None:
        """Click a button using OS-level Quartz mouse events.

        Unlike Playwright's CDP mouse API (page.mouse.click), OS-level events
        are injected at the macOS input stack before the browser sees them.
        This makes them indistinguishable from real physical hardware clicks,
        bypassing any browser-side or server-side bot-detection heuristics.

        The selector must resolve to a *visible* element; we compute the
        element's screen coordinates from its viewport rect combined with the
        browser window's screen position, then use pyautogui to move and click.
        """
        try:
            import pyautogui
        except ImportError:
            raise RuntimeError(
                "os_click requires pyautogui: "
                "pip install pyautogui in the mcd-key-automation venv"
            )

        selector = self._val(step, "selector")
        timeout = int(step.get("timeout_ms", 20000))

        # Wait for a visible copy of the button.
        loc = self.page.locator(selector + ":visible").first
        await loc.wait_for(state="visible", timeout=timeout)
        await loc.scroll_into_view_if_needed()
        await asyncio.sleep(0.4)

        # Compute screen-space coordinates.
        # window.screenX/Y  — outer-left / outer-top of the browser window
        # outerHeight - innerHeight — height of browser chrome (tabs + address bar)
        # getBoundingClientRect()  — element position within the viewport (CSS px)
        # devicePixelRatio — physical-px per CSS-px. Used on Retina Macs (=2)
        #     where Quartz still wants logical points but the comparison is for
        #     sanity logging. On Windows we deliberately keep the Python process
        #     DPI-virtualised so pyautogui clicks land in the same coordinate
        #     space the browser uses (also virtualised, per Edge's default).
        #     Multiplying by dpr on Windows would cause a mismatch on scaled
        #     displays where the browser reports dpr=1.0 anyway.
        # We iterate all matching elements and pick the first *visible* one
        # (non-zero bounding box) to avoid the hidden duplicate that the portal
        # injects alongside the real button.
        coords: dict = await self.page.evaluate(
            """
            (sel) => {
                let el = null;
                for (const e of document.querySelectorAll(sel)) {
                    const r = e.getBoundingClientRect();
                    if (r.width > 0 && r.height > 0) { el = e; break; }
                }
                if (!el) return null;
                const r = el.getBoundingClientRect();
                return {
                    ex: r.left + r.width  / 2,
                    ey: r.top  + r.height / 2,
                    wx: window.screenX,
                    wy: window.screenY,
                    ch: window.outerHeight - window.innerHeight,
                    dpr: window.devicePixelRatio || 1,
                };
            }
            """,
            selector,
        )
        if coords is None:
            raise RuntimeError(f"os_click: selector {selector!r} not found in DOM")

        sx = int(coords["wx"] + coords["ex"])
        sy = int(coords["wy"] + coords["ch"] + coords["ey"])
        logger.info(
            "Playbook: os_click selector={!r}  screen=({}, {})  win=({}, {})  ch={}  view=({}, {})  dpr={}",
            selector, sx, sy,
            coords["wx"], coords["wy"], coords["ch"], coords["ex"], coords["ey"],
            coords.get("dpr"),
        )

        # Move naturally to avoid instant-jump suspicion, then click.
        pyautogui.moveTo(sx - 50, sy + 6, duration=0.25)
        await asyncio.sleep(0.1)
        pyautogui.moveTo(sx, sy, duration=0.18)
        await asyncio.sleep(0.15)
        pyautogui.click(sx, sy)

        # Verify the click actually advanced past the target. The portal removes
        # the proceed button from the DOM (or hides it) once the click is
        # accepted. If it's still visible after a short grace period we likely
        # missed (DPI virtualisation drift, off-screen window, hidden chrome,
        # etc.) — fall back to Playwright's CDP click which is reliable even if
        # less stealthy. Better to provision noisily than to skip the API.
        try:
            await loc.wait_for(state="hidden", timeout=4000)
            logger.info("Playbook: os_click verified — target hidden after click")
        except Exception:
            logger.warning(
                "Playbook: os_click on {!r} did not advance the page — "
                "falling back to Playwright locator.click()",
                selector,
            )
            try:
                await loc.click(timeout=8000)
            except Exception as cdp_exc:
                raise RuntimeError(
                    f"os_click fallback also failed for {selector!r}: {cdp_exc}"
                )

    async def _do_wait_for(self, step: dict[str, Any]) -> None:
        selector = self._val(step, "selector")
        timeout = int(step.get("timeout_ms", 20000))
        await self.page.wait_for_selector(selector, timeout=timeout)

    async def _do_wait_for_url_contains(self, step: dict[str, Any]) -> None:
        needle = self._val(step, "value")
        timeout = int(step.get("timeout_ms", 60000))
        deadline = time.monotonic() + timeout / 1000.0
        while time.monotonic() < deadline:
            if needle in self.page.url:
                return
            await asyncio.sleep(0.5)
        raise TimeoutError(
            f"URL did not contain {needle!r} within {timeout}ms (last url={self.page.url})"
        )

    async def _do_wait_for_proceed_enabled(self, step: dict[str, Any]) -> None:
        timeout = int(step.get("timeout_ms", 20000))
        await self.page.wait_for_function(
            f"""
            () => {{
                const btns = document.querySelectorAll("{self.PROCEED_SELECTOR}");
                for (const btn of btns) {{
                    if (btn.disabled) continue;
                    if ((btn.getAttribute('aria-disabled') || '').toLowerCase() === 'true') continue;
                    // Must also be visually present (not CSS-hidden by the portal).
                    const rect = btn.getBoundingClientRect();
                    if (rect.width > 0 && rect.height > 0) return true;
                }}
                return false;
            }}
            """,
            timeout=timeout,
        )

    async def _do_fill(self, step: dict[str, Any]) -> None:
        selector = self._val(step, "selector")
        value = str(self._val(step, "value", default=""))
        delay = int(step.get("delay_ms", 70))
        loc = self.page.locator(selector).first
        await loc.wait_for(state="visible", timeout=int(step.get("timeout_ms", 20000)))
        await loc.scroll_into_view_if_needed()
        await loc.click()
        await asyncio.sleep(0.25)
        await loc.fill("")
        await loc.press_sequentially(value, delay=delay)
        await loc.press("Tab")
        await asyncio.sleep(0.4)
        got = await loc.input_value()
        if got != value:
            logger.warning(
                "Playbook fill mismatch: selector={!r} expected={!r} got={!r}",
                selector, value, got,
            )

    async def _do_click(self, step: dict[str, Any]) -> None:
        selector = self._val(step, "selector")
        timeout = int(step.get("timeout_ms", 20000))
        loc = self.page.locator(selector).first
        await loc.wait_for(state="visible", timeout=timeout)
        await loc.scroll_into_view_if_needed()
        await loc.click()

    async def _do_click_proceed(self, step: dict[str, Any]) -> None:
        """Click the proceed button.

        Uses Playwright's page.mouse API (generates isTrusted events via CDP)
        rather than the JS btn.click() path (isTrusted: false).

        NOTE: The Mastercard portal keeps a CSS-hidden proceed-btn in the DOM
        alongside the visible one.  We must target only the *visible* button;
        otherwise Playwright's .first picks the hidden one and wait_for("visible")
        times out after 20 s.
        """
        timeout = int(step.get("timeout_ms", 20000))
        # :visible filters to elements with a non-zero bounding box, skipping
        # the portal's permanently-hidden duplicate proceed button.
        btn = self.page.locator(self.PROCEED_SELECTOR + ":visible").first
        await btn.wait_for(state="visible", timeout=timeout)
        await btn.scroll_into_view_if_needed()
        await asyncio.sleep(0.35)
        box = await btn.bounding_box()
        if box is None:
            raise RuntimeError("click_proceed: proceed button has no bounding box")
        # Click at element centre using OS-level mouse events (isTrusted: true).
        x = box["x"] + box["width"] / 2
        y = box["y"] + box["height"] / 2
        await self.page.mouse.move(x - 55, y + 8, steps=4)
        await asyncio.sleep(0.12)
        await self.page.mouse.move(x, y, steps=6)
        await asyncio.sleep(0.18)
        await self.page.mouse.click(x, y)

    async def _do_click_radio(self, step: dict[str, Any]) -> None:
        name_suffix = self._val(step, "name_suffix")
        value = self._val(step, "value")
        timeout = int(step.get("timeout_ms", 10000))
        id_value = await self.page.evaluate(
            """
            ({ nameSuffix, value }) => {
                const radio = Array.from(document.querySelectorAll("input[type='radio']"))
                    .find((r) =>
                        (r.getAttribute('name') || '').endsWith(nameSuffix) &&
                        (r.getAttribute('value') || '') === value
                    );
                return radio ? radio.id : '';
            }
            """,
            {"nameSuffix": name_suffix, "value": value},
        )
        if not id_value:
            raise RuntimeError(
                f"click_radio: no radio with name endswith {name_suffix!r} value={value!r}"
            )

        async def is_checked() -> bool:
            return bool(await self.page.evaluate(
                "(id) => { const el = document.getElementById(id); return !!(el && el.checked); }",
                id_value,
            ))

        # 1. Click input directly.
        try:
            loc = self.page.locator(f"input[id='{id_value}']").first
            await loc.scroll_into_view_if_needed()
            await loc.click(force=True, timeout=timeout)
            await asyncio.sleep(0.25)
            if await is_checked():
                return
        except Exception as err:
            logger.debug("radio input click failed: {}", err)

        # 2. Click label[for=id].
        try:
            label = self.page.locator(f"label[for='{id_value}']").first
            await label.wait_for(state="visible", timeout=timeout)
            await label.scroll_into_view_if_needed()
            await label.click()
            await asyncio.sleep(0.25)
            if await is_checked():
                return
        except Exception as err:
            logger.debug("radio label click failed: {}", err)

        # 3. JS click + change.
        await self.page.evaluate(
            """
            (id) => {
                const el = document.getElementById(id);
                if (!el) return;
                try { el.click(); } catch (_e) {}
                if (!el.checked) {
                    el.checked = true;
                    el.dispatchEvent(new Event('input', { bubbles: true }));
                    el.dispatchEvent(new Event('change', { bubbles: true }));
                }
            }
            """,
            id_value,
        )
        await asyncio.sleep(0.3)
        if not await is_checked():
            raise RuntimeError(
                f"click_radio: failed to check radio name~={name_suffix!r} value={value!r}"
            )

    async def _do_expect_download(self, step: dict[str, Any]) -> None:
        click_selector = self._val(step, "click_selector")
        timeout = int(step.get("timeout_ms", 180000))
        # Wait for the trigger button first (may follow a long server-side wait).
        await self.page.wait_for_selector(click_selector, timeout=timeout)

        before_files = {p.name for p in self.dest_dir.glob("*") if p.is_file()}
        try:
            async with self.page.expect_download(timeout=timeout) as dl_info:
                await self.page.locator(click_selector).click()
            download = await dl_info.value
            original = download.suggested_filename or f"{self.download_name_hint}.zip"
            dest = self.dest_dir / original
            await save_download(download, dest)
            self.downloads.append(dest)
            logger.info("Playbook download saved: {}", dest)
        except Exception as err:
            logger.warning(
                "Playbook download event missed ({}) — polling filesystem fallback", err
            )
            for _ in range(30):
                await asyncio.sleep(1.0)
                new_files = [
                    p for p in self.dest_dir.glob("*")
                    if p.is_file()
                    and p.name not in before_files
                    and p.suffix.lower() in {".zip", ".p12", ".pem"}
                ]
                if new_files:
                    latest = max(new_files, key=lambda p: p.stat().st_mtime)
                    self.downloads.append(latest)
                    logger.info("Playbook download captured (fs fallback): {}", latest)
                    return
            raise
