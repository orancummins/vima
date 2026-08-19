"""Playwright session manager.

Headful chromium with persistent storage state. Provides a context manager that yields
a (browser, context, page) tuple ready for orchestration to drive.
"""
from __future__ import annotations

import asyncio
import contextlib
import os
import shutil
import sys
from pathlib import Path
from typing import AsyncIterator

from loguru import logger
from playwright.async_api import (
    Browser,
    BrowserContext,
    Page,
    async_playwright,
)


STATE_FILE = Path(__file__).parent.parent / "session_state.json"


def _detect_system_channel() -> str | None:
    """Return an installed system browser channel, preferring Chrome over Edge.

    Chrome is preferred because Edge — often the user's default browser and
    already running — can consolidate/close the automation window when Playwright
    drives it via ``channel='msedge'``.
    """
    if sys.platform == "win32":
        pf = os.environ.get("ProgramFiles", r"C:\Program Files")
        pf86 = os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")
        local = os.environ.get("LOCALAPPDATA", str(Path.home() / "AppData" / "Local"))
        chrome_paths = [
            Path(pf) / "Google/Chrome/Application/chrome.exe",
            Path(pf86) / "Google/Chrome/Application/chrome.exe",
            Path(local) / "Google/Chrome/Application/chrome.exe",
        ]
        edge_paths = [
            Path(pf86) / "Microsoft/Edge/Application/msedge.exe",
            Path(pf) / "Microsoft/Edge/Application/msedge.exe",
        ]
        if any(p.exists() for p in chrome_paths):
            return "chrome"
        if any(p.exists() for p in edge_paths):
            return "msedge"
        return None
    if sys.platform == "darwin":
        if Path("/Applications/Google Chrome.app").exists():
            return "chrome"
        if Path("/Applications/Microsoft Edge.app").exists():
            return "msedge"
        return None
    # Linux / other: rely on PATH.
    for exe, channel in (
        ("google-chrome", "chrome"),
        ("google-chrome-stable", "chrome"),
        ("microsoft-edge", "msedge"),
        ("microsoft-edge-stable", "msedge"),
    ):
        if shutil.which(exe):
            return channel
    return None


def _launch_plan() -> list[str | None]:
    """Ordered list of browser channels to try, most-preferred first.

    ``None`` means Playwright's bundled Chromium. We can't reliably tell in
    advance whether the bundled build matching *this* Playwright version is
    present (a stale ``chromium-*`` dir for another version may exist without a
    usable executable), so we simply try each option in turn and fall back to a
    system-installed Chrome/Edge. This makes the tool work on first download
    with zero config even when the Chromium download was blocked.
    """
    explicit = os.environ.get("PLAYWRIGHT_BROWSER_CHANNEL", "").strip() or None
    system = _detect_system_channel()
    if explicit:
        plan: list[str | None] = [explicit, None, system]
    else:
        # Prefer bundled Chromium (isolated, matches Playwright), then system
        # Chrome/Edge as a fallback when bundled isn't installed.
        plan = [None, system]
    # De-duplicate while preserving order.
    seen: set = set()
    ordered: list[str | None] = []
    for item in plan:
        key = item or "__bundled__"
        if key not in seen:
            seen.add(key)
            ordered.append(item)
    return ordered



async def _install_cookie_banner_dismisser(page) -> None:
    """Auto-dismiss the 'Cookies on this site' consent modal whenever it appears.

    The consent dialog overlays the create-project wizard and intercepts clicks
    (Proceed/Create stay unreachable behind it). Playwright's locator handler
    runs automatically during actionability checks, so this clears the banner no
    matter which step triggers it. We prefer 'Reject all' (dismisses with the
    fewest cookies); fall back to other accept/save buttons across UI variants.
    """
    async def _handler(*_args) -> None:
        for label in ("Reject all", "Accept cookies", "Accept all", "Save settings", "Close"):
            try:
                btn = page.get_by_role("button", name=label, exact=False)
                if await btn.count() > 0:
                    await btn.first.click(timeout=3000, force=True)
                    logger.info("Dismissed cookie consent banner via {!r}", label)
                    return
            except Exception:
                continue

    try:
        # Trigger on the consent dialog's heading text; the handler then clicks
        # the appropriate dismiss button. no_wait_after so Playwright resumes
        # the original action once the banner is gone.
        trigger = page.get_by_text("Cookies on this site", exact=False)
        await page.add_locator_handler(trigger, _handler, no_wait_after=True)
    except Exception as exc:  # pragma: no cover - defensive
        logger.warning("Could not install cookie-banner handler: {}", exc)


def _install_failed_response_logger(page) -> None:
    """Log the portal's backend API calls relevant to project/credential/cert creation.

    Portal error dialogs like "There was an issue trying to create the
    certificate" are generic; the real cause is in the backend response — which
    is frequently an HTTP 200 carrying an error payload (not a 4xx/5xx). So we
    log any mastercard backend call whose URL mentions certificate/credential/
    project/service/sandbox regardless of status, including the request body and
    the (truncated) response body, so failures can be diagnosed from evidence.
    """
    keywords = ("certificate", "credential", "project", "service", "sandbox",
                "graphql", "/api/")
    noisy = (".js", ".css", ".png", ".jpg", ".jpeg", ".svg", ".woff", ".woff2",
             ".ico", ".gif", "/fonts/", "analytics", "telemetry", "smetrics.",
             "/b/ss/")

    def _is_asset(low: str) -> bool:
        return any(n in low for n in noisy)

    async def _log(resp) -> None:
        try:
            url = resp.url
            low = url.lower()
            if "mastercard.com" not in low:
                return
            if _is_asset(low):
                return
            status = resp.status
            req = resp.request
            method = req.method
            relevant = any(k in low for k in keywords)
            # Log ALL non-GET (POST/PUT/PATCH/DELETE) calls, all HTTP errors, and
            # keyword-relevant GETs. Non-GET calls are the ones that create the
            # project/certificate, so we must never filter them out.
            if method == "GET" and status < 400 and not relevant:
                return
            post = ""
            try:
                post = (req.post_data or "")[:600]
            except Exception:
                pass
            body = ""
            try:
                body = (await resp.text())[:1500]
            except Exception:
                pass
            logger.warning(
                "NET {} {} {} | req={} | resp={}",
                status, method, url,
                post.replace("\n", " "), body.replace("\n", " "),
            )
        except Exception:
            pass

    def _on_response(resp) -> None:
        try:
            asyncio.ensure_future(_log(resp))
        except Exception:
            pass

    def _on_requestfailed(request) -> None:
        """Capture requests that never got a response (blocked/cancelled/net error).

        A certificate endpoint blocked by a corporate MITM proxy fails here with
        no HTTP status, and the SPA surfaces it as the generic cert error dialog.
        """
        try:
            url = request.url
            low = url.lower()
            if "mastercard.com" not in low or _is_asset(low):
                return
            failure = ""
            try:
                failure = request.failure or ""
            except Exception:
                pass
            logger.warning(
                "NETFAIL {} {} | error={}", request.method, url, failure,
            )
        except Exception:
            pass

    page.on("response", _on_response)
    page.on("requestfailed", _on_requestfailed)
    try:
        # Also listen at the context level so responses from popups/other frames
        # are captured even if they aren't on the primary page.
        page.context.on("response", _on_response)
        page.context.on("requestfailed", _on_requestfailed)
    except Exception:
        pass


def _install_console_logger(page) -> None:
    """Log browser console errors and uncaught page exceptions.

    Some portal failures (e.g. "There was an issue trying to create the
    certificate") are client-side: the SPA generates the keypair/certificate in
    the browser via WebCrypto and never sends a request, so there is no HTTP
    response to inspect. The underlying JS exception surfaces here instead.
    """
    def _on_console(msg) -> None:
        try:
            if msg.type in ("error", "warning"):
                logger.warning("CONSOLE[{}] {}", msg.type, (msg.text or "")[:800])
        except Exception:
            pass

    def _on_pageerror(exc) -> None:
        try:
            logger.warning("PAGEERROR {}", str(exc)[:1000])
        except Exception:
            pass

    page.on("console", _on_console)
    page.on("pageerror", _on_pageerror)


_CRYPTO_PROBE_JS = r"""
(() => {
  try {
    const log = (m) => { try { console.error('WCPROBE: ' + m); } catch (e) {} };
    window.addEventListener('unhandledrejection', (e) => {
      const r = e && e.reason;
      log('unhandledrejection: ' + (r && (r.stack || r.message) || r));
    });
    window.addEventListener('error', (e) => {
      log('error: ' + (e && e.error && (e.error.stack || e.error.message) || (e && e.message)));
    });
    const s = window.crypto && window.crypto.subtle;
    if (!s) { log('NO crypto.subtle! isSecureContext=' + window.isSecureContext); return; }
    const methods = ['generateKey','exportKey','importKey','sign','verify',
                     'digest','deriveKey','deriveBits','encrypt','decrypt',
                     'wrapKey','unwrapKey'];
    for (const name of methods) {
      const orig = s[name];
      if (typeof orig !== 'function') continue;
      s[name] = function (...args) {
        let alg = '';
        try { alg = JSON.stringify(args[0]); } catch (e) {}
        let p;
        try { p = orig.apply(this, args); }
        catch (err) { log('subtle.' + name + ' THREW: ' + (err && err.message || err) + ' | alg=' + alg); throw err; }
        return Promise.resolve(p).catch((err) => {
          log('subtle.' + name + ' REJECTED: ' + (err && (err.message || err.name) || err) + ' | alg=' + alg);
          throw err;
        });
      };
    }
    log('installed isSecureContext=' + window.isSecureContext);
  } catch (e) { try { console.error('WCPROBE: install-failed ' + e); } catch (x) {} }
})();
"""


async def _install_crypto_probe(page) -> None:
    """Instrument in-browser WebCrypto so swallowed certificate-generation errors surface.

    The portal generates the mTLS/signing certificate client-side via
    ``crypto.subtle`` and catches any rejection internally (showing only a
    generic dialog). This init script wraps those methods so the underlying
    error is logged as ``WCPROBE: ...`` before the SPA swallows it.
    """
    try:
        await page.add_init_script(_CRYPTO_PROBE_JS)
    except Exception:
        pass




@contextlib.asynccontextmanager
async def browser_session(
    *,
    headless: bool = False,
    storage_state: Path | None = STATE_FILE,
    downloads_dir: Path | None = None,
) -> AsyncIterator[tuple[Browser, BrowserContext, Page]]:
    async with async_playwright() as pw:
        base_kwargs: dict = {
            "headless": headless,
            "args": ["--foreground"] if not headless else [],
        }
        # Try each option in order (bundled Chromium → system Chrome → Edge, or an
        # explicit override first) so the tool works on first download with no
        # config even when the Chromium download was blocked by a corp proxy.
        browser = None
        last_exc: Exception | None = None
        for channel in _launch_plan():
            kwargs = dict(base_kwargs)
            if channel:
                kwargs["channel"] = channel
            label = channel or "bundled Chromium"
            try:
                browser = await pw.chromium.launch(**kwargs)
                logger.info("Launched browser: {}", label)
                break
            except Exception as exc:  # noqa: BLE001 - want to try the next option
                last_exc = exc
                logger.warning(
                    "Browser launch via {} failed ({}) — trying next option…",
                    label, type(exc).__name__,
                )
        if browser is None:
            raise RuntimeError(
                "Could not launch any browser (bundled Chromium or system "
                "Chrome/Edge). Install Google Chrome, or run "
                "'python -m playwright install chromium'."
            ) from last_exc
        ctx_kwargs: dict = {"accept_downloads": True}
        if storage_state and storage_state.exists():
            logger.info("Reusing saved session from {}", storage_state)
            ctx_kwargs["storage_state"] = str(storage_state)
        if downloads_dir:
            downloads_dir.mkdir(parents=True, exist_ok=True)
        context = await browser.new_context(**ctx_kwargs)
        page = await context.new_page()
        await page.bring_to_front()
        await _install_cookie_banner_dismisser(page)
        _install_failed_response_logger(page)
        _install_console_logger(page)
        await _install_crypto_probe(page)
        try:
            yield browser, context, page
        finally:
            try:
                if storage_state:
                    await context.storage_state(path=str(storage_state))
                    logger.info("Saved session state to {}", storage_state)
            except Exception as e:
                logger.warning("Failed to save session state: {}", e)
            await context.close()
            await browser.close()
