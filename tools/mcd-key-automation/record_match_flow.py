"""Interactive recorder for the MATCH create-project flow.

Launches a headful Chromium session against the Mastercard developer portal,
re-uses the saved storage state, and records every user interaction (click,
input, change, focus, navigation, key fields). For each event it captures:

  - timestamp
  - event type
  - target element descriptor (tag, id, name, data-testid, role, type, text)
  - target value (if any)
  - selector candidates (id, data-testid, name, role+name, css path)
  - page URL / title at the time of the event
  - a screenshot (before the next event arrives) saved to disk

The recorder also dumps the full HTML of the active page whenever the URL
changes, so we can analyze every step (create-project -> Step 2 -> MATCH
service details -> download key) end-to-end.

Output layout:

    logs/recordings/<timestamp>/
        trace.jsonl            # one event per line
        screenshots/*.png
        dom/<step>.html

Usage:

    cd tools/mcd-key-automation
    ./.venv/bin/python record_match_flow.py

Press Ctrl+C in the terminal (or close the browser) to stop recording.
"""
from __future__ import annotations

import asyncio
import json
import signal
from datetime import datetime
from pathlib import Path

from loguru import logger
from playwright.async_api import async_playwright, Page

ROOT = Path(__file__).parent
STATE_FILE = ROOT / "session_state.json"
RECORD_ROOT = ROOT / "logs" / "recordings"
START_URL = "https://developer.mastercard.com/create-project?services=match"


RECORDER_JS = r"""
(() => {
    if (window.__mcd_recorder_installed) return;
    window.__mcd_recorder_installed = true;
    window.__mcd_events = [];

    const cssPath = (el) => {
        if (!(el instanceof Element)) return '';
        const path = [];
        let node = el;
        while (node && node.nodeType === 1 && path.length < 8) {
            let selector = node.nodeName.toLowerCase();
            if (node.id) {
                selector += `#${node.id}`;
                path.unshift(selector);
                break;
            }
            const dt = node.getAttribute('data-testid');
            if (dt) {
                selector += `[data-testid="${dt}"]`;
                path.unshift(selector);
                break;
            }
            const parent = node.parentElement;
            if (parent) {
                const siblings = Array.from(parent.children).filter(
                    (c) => c.nodeName === node.nodeName
                );
                if (siblings.length > 1) {
                    const idx = siblings.indexOf(node) + 1;
                    selector += `:nth-of-type(${idx})`;
                }
            }
            path.unshift(selector);
            node = node.parentElement;
        }
        return path.join(' > ');
    };

    const describe = (el) => {
        if (!(el instanceof Element)) return null;
        const labelEl =
            el.id ? document.querySelector(`label[for="${CSS.escape(el.id)}"]`) : null;
        const labelText = labelEl ? (labelEl.textContent || '').trim() : '';
        return {
            tag: el.tagName.toLowerCase(),
            id: el.id || '',
            name: el.getAttribute('name') || '',
            type: el.getAttribute('type') || '',
            testid: el.getAttribute('data-testid') || '',
            role: el.getAttribute('role') || '',
            placeholder: el.getAttribute('placeholder') || '',
            ariaLabel: el.getAttribute('aria-label') || '',
            value:
                'value' in el && typeof el.value === 'string'
                    ? String(el.value).slice(0, 200)
                    : '',
            checked: 'checked' in el ? !!el.checked : null,
            text: (el.textContent || '').trim().slice(0, 120),
            labelText,
            cssPath: cssPath(el),
            outerHTMLHead: (el.outerHTML || '').slice(0, 240),
        };
    };

    const push = (type, target, extra) => {
        try {
            window.__mcd_events.push({
                ts: Date.now(),
                type,
                url: location.href,
                target: describe(target),
                extra: extra || null,
            });
        } catch (e) {
            // best-effort
        }
    };

    document.addEventListener('click', (e) => push('click', e.target), true);
    document.addEventListener('change', (e) => push('change', e.target), true);
    document.addEventListener('input', (e) => push('input', e.target), true);
    document.addEventListener('focusin', (e) => push('focus', e.target), true);
    document.addEventListener('submit', (e) => push('submit', e.target), true);

    window.addEventListener('beforeunload', () => push('beforeunload', document.body));

    window.__mcd_drain = () => {
        const out = window.__mcd_events;
        window.__mcd_events = [];
        return out;
    };
})();
"""


async def install_recorder(page: Page) -> None:
    try:
        await page.evaluate(RECORDER_JS)
    except Exception as e:
        logger.warning("Failed to install recorder on {}: {}", page.url, e)


async def drain_events(page: Page) -> list[dict]:
    try:
        return await page.evaluate("() => (window.__mcd_drain ? window.__mcd_drain() : [])")
    except Exception:
        return []


def _safe_label(url: str) -> str:
    return (
        url.replace("https://", "")
        .replace("http://", "")
        .replace("/", "_")
        .replace("?", "_")
        .replace("&", "_")
        .replace("=", "-")
    )[:80]


async def record(stop_event: asyncio.Event) -> Path:
    stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    out_dir = RECORD_ROOT / stamp
    (out_dir / "screenshots").mkdir(parents=True, exist_ok=True)
    (out_dir / "dom").mkdir(parents=True, exist_ok=True)
    trace_path = out_dir / "trace.jsonl"
    logger.info("Recording to {}", out_dir)

    seen_urls: set[str] = set()
    last_screenshot_at = 0.0
    last_url = ""

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False, args=["--foreground"])
        ctx_kwargs: dict = {"accept_downloads": True}
        if STATE_FILE.exists():
            ctx_kwargs["storage_state"] = str(STATE_FILE)
        context = await browser.new_context(**ctx_kwargs)

        async def on_page(page: Page) -> None:
            page.on("framenavigated", lambda _f: asyncio.create_task(install_recorder(page)))
            await install_recorder(page)

        context.on("page", lambda p: asyncio.create_task(on_page(p)))

        page = await context.new_page()
        await on_page(page)
        await page.bring_to_front()
        await page.goto(START_URL, wait_until="domcontentloaded")
        await install_recorder(page)

        logger.info(
            "Browser is open. Drive the MATCH create-project flow end-to-end. "
            "Press Ctrl+C in this terminal when finished."
        )

        with trace_path.open("a", encoding="utf-8") as trace_f:
            while not stop_event.is_set():
                try:
                    current = context.pages[-1] if context.pages else None
                    if current is None:
                        await asyncio.sleep(0.5)
                        continue

                    await install_recorder(current)
                    events = await drain_events(current)
                    now = asyncio.get_event_loop().time()

                    if events:
                        for ev in events:
                            trace_f.write(json.dumps(ev, ensure_ascii=False) + "\n")
                        trace_f.flush()

                    url = current.url
                    if url and url != last_url:
                        last_url = url
                        if url not in seen_urls:
                            seen_urls.add(url)
                            try:
                                html = await current.content()
                                (out_dir / "dom" / f"{stamp}_{_safe_label(url)}.html").write_text(
                                    html, encoding="utf-8"
                                )
                            except Exception as e:
                                logger.warning("DOM dump failed for {}: {}", url, e)

                    if events or (now - last_screenshot_at) > 2.5:
                        try:
                            label = _safe_label(url or "page")
                            shot = out_dir / "screenshots" / (
                                f"{datetime.utcnow().strftime('%Y%m%dT%H%M%S_%f')}_{label}.png"
                            )
                            await current.screenshot(path=str(shot), full_page=True)
                            last_screenshot_at = now
                        except Exception:
                            pass

                    await asyncio.sleep(0.6)
                except Exception as loop_err:
                    logger.warning("Recorder loop error: {}", loop_err)
                    await asyncio.sleep(1.0)

        try:
            if STATE_FILE:
                await context.storage_state(path=str(STATE_FILE))
        except Exception:
            pass
        await context.close()
        await browser.close()

    logger.info("Recording complete: {}", out_dir)
    return out_dir


def main() -> None:
    stop_event = asyncio.Event()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    def _stop(*_args) -> None:
        logger.info("Stop signal received; finishing recording...")
        loop.call_soon_threadsafe(stop_event.set)

    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            signal.signal(sig, _stop)
        except Exception:
            pass

    try:
        loop.run_until_complete(record(stop_event))
    finally:
        loop.close()


if __name__ == "__main__":
    main()
