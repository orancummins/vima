"""Interactive playbook recorder for Mastercard portal create-project flows.

Launches a headful Chromium against the portal, installs a JS event recorder
that captures every click / input / change, then on exit post-processes the
trace into a declarative playbook JSON consumed by ``PlaybookRunner``.

Usage (via the wrapper script)::

    ./addapi.sh --record https://developer.mastercard.com/<slug>/documentation/

Or directly::

    cd tools/mcd-key-automation
    ./.venv/bin/python -m app.playbook_record \
        --api-slug match \
        --start-url 'https://developer.mastercard.com/create-project?services=match'

When you finish provisioning a project manually, return to the terminal and
press Enter — the recorder will compress the trace into
``playbooks/mastercard/<api-slug>.json``.
"""
from __future__ import annotations

import asyncio
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import typer
from loguru import logger
from playwright.async_api import async_playwright, Page

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
STATE_FILE = ROOT / "session_state.json"
PLAYBOOK_ROOT = ROOT / "playbooks"
RECORD_ROOT = ROOT / "logs" / "recordings"

# Re-uses the JS hook approach pioneered in record_match_flow.py — kept inline
# so this module has no cross-module dependencies on the older recorder.
RECORDER_JS = r"""
(() => {
    if (window.__mcd_recorder_installed) return;
    window.__mcd_recorder_installed = true;
    window.__mcd_events = [];

    const describe = (el) => {
        if (!(el instanceof Element)) return null;
        return {
            tag: el.tagName.toLowerCase(),
            id: el.id || '',
            name: el.getAttribute('name') || '',
            type: el.getAttribute('type') || '',
            testid: el.getAttribute('data-testid') || '',
            role: el.getAttribute('role') || '',
            value:
                'value' in el && typeof el.value === 'string'
                    ? String(el.value).slice(0, 400)
                    : '',
            checked: 'checked' in el ? !!el.checked : null,
            text: (el.textContent || '').trim().slice(0, 120),
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
        } catch (e) {}
    };

    document.addEventListener('click', (e) => push('click', e.target), true);
    document.addEventListener('change', (e) => push('change', e.target), true);
    document.addEventListener('input', (e) => push('input', e.target), true);

    window.__mcd_drain = () => {
        const out = window.__mcd_events;
        window.__mcd_events = [];
        return out;
    };
})();
"""


# ---------------------------------------------------------------------------
# Event capture
# ---------------------------------------------------------------------------


async def _install_recorder(page: Page) -> None:
    try:
        await page.evaluate(RECORDER_JS)
    except Exception as err:
        logger.debug("install_recorder failed: {}", err)


async def _drain(page: Page) -> list[dict]:
    try:
        return await page.evaluate(
            "() => (window.__mcd_drain ? window.__mcd_drain() : [])"
        )
    except Exception:
        return []


@dataclass
class CapturedTrace:
    events: list[dict] = field(default_factory=list)
    urls: list[tuple[float, str]] = field(default_factory=list)
    downloads: list[str] = field(default_factory=list)


async def _poll_loop(page: Page, trace: CapturedTrace, stop: asyncio.Event) -> None:
    while not stop.is_set():
        try:
            batch = await _drain(page)
        except Exception:
            batch = []
        if batch:
            trace.events.extend(batch)
        await asyncio.wait([asyncio.create_task(stop.wait())], timeout=0.5)


# ---------------------------------------------------------------------------
# Post-processing: events -> playbook steps
# ---------------------------------------------------------------------------


def _selector_for(target: dict) -> str | None:
    """Compute the most stable selector for an element descriptor."""
    if not target:
        return None
    if target.get("testid"):
        return f"{target['tag']}[data-testid='{target['testid']}']"
    if target.get("id"):
        return f"#{target['id']}"
    if target.get("name"):
        return f"{target['tag']}[name='{target['name']}']"
    return None


def _is_proceed(target: dict) -> bool:
    return bool(target) and target.get("testid") == "proceed-btn"


def _is_download_button(target: dict) -> bool:
    if not target:
        return False
    testid = target.get("testid", "")
    text = (target.get("text") or "").lower()
    return testid.startswith("download-key") or "download" in text and target.get("tag") == "button"


def _is_radio(target: dict) -> bool:
    return bool(target) and target.get("tag") == "input" and target.get("type") == "radio"


def _collapse_inputs(events: list[dict]) -> list[dict]:
    """Collapse a run of ``input`` events on the same field into one ``fill``.

    Returns a new event list with synthetic ``fill`` events replacing each run.
    """
    out: list[dict] = []
    i = 0
    while i < len(events):
        ev = events[i]
        target = ev.get("target") or {}
        if (
            ev["type"] == "input"
            and target.get("tag") == "input"
            and target.get("type") not in {"radio", "checkbox", "submit", "button"}
        ):
            sel = _selector_for(target)
            if sel is None:
                i += 1
                continue
            # Walk forward through consecutive input/change events on same selector.
            last_value = target.get("value", "") or ""
            j = i + 1
            while j < len(events):
                nxt = events[j]
                ntarget = nxt.get("target") or {}
                if nxt["type"] in {"input", "change"} and _selector_for(ntarget) == sel:
                    last_value = ntarget.get("value", "") or last_value
                    j += 1
                else:
                    break
            out.append(
                {
                    "ts": ev["ts"],
                    "type": "fill",
                    "url": ev["url"],
                    "selector": sel,
                    "value": last_value,
                }
            )
            i = j
            continue
        out.append(ev)
        i += 1
    return out


def _compile_steps(trace: CapturedTrace) -> list[dict]:
    """Compile collapsed events into playbook actions."""
    events = _collapse_inputs(trace.events)
    steps: list[dict] = []
    seen_selectors: set[str] = set()
    last_proceed_ts: float | None = None

    for ev in events:
        target = ev.get("target") or {}
        et = ev["type"]

        if et == "fill":
            sel = ev["selector"]
            if sel not in seen_selectors:
                steps.append({"action": "wait_for", "selector": sel})
                seen_selectors.add(sel)
            steps.append({"action": "fill", "selector": sel, "value": ev["value"]})
            continue

        if et == "click":
            # Proceed button gets the dedicated action.
            if _is_proceed(target):
                # Ensure we wait for enablement first.
                steps.append({"action": "wait_for_proceed_enabled"})
                steps.append({"action": "click_proceed"})
                last_proceed_ts = ev["ts"]
                continue
            # Download trigger.
            if _is_download_button(target):
                sel = _selector_for(target)
                if sel is None:
                    continue
                steps.append(
                    {
                        "action": "expect_download",
                        "click_selector": sel,
                        "timeout_ms": 240000,
                    }
                )
                continue
            # Plain click on a button / actionable element.
            if target.get("tag") in {"button", "a"}:
                sel = _selector_for(target)
                if sel is None:
                    continue
                steps.append({"action": "click", "selector": sel})
                continue
            # Label-on-radio click: prefer the upcoming radio change event.
            continue

        if et == "change" and _is_radio(target):
            name = target.get("name", "") or ""
            value = target.get("value", "") or ""
            # Strip the React-generated id prefix so we can match across renders.
            # Names typically look like "rcd-xxxx_accessToBeUsedBy".
            suffix_match = re.search(r"(_[A-Za-z][A-Za-z0-9_]*)$", name)
            name_suffix = suffix_match.group(1) if suffix_match else name
            steps.append(
                {
                    "action": "click_radio",
                    "name_suffix": name_suffix,
                    "value": value,
                }
            )
            continue

    return steps


def _dedup_steps(steps: list[dict]) -> list[dict]:
    """Remove obvious duplicate consecutive steps (e.g. two click_proceed)."""
    out: list[dict] = []
    for s in steps:
        if out and out[-1] == s:
            continue
        # Squash repeated wait_for_proceed_enabled.
        if (
            out
            and out[-1].get("action") == "wait_for_proceed_enabled"
            and s.get("action") == "wait_for_proceed_enabled"
        ):
            continue
        out.append(s)
    return out


# ---------------------------------------------------------------------------
# Variable mapping (interactive)
# ---------------------------------------------------------------------------


KNOWN_VARS = ["project_name", "alias", "key_password", "contact_email", "ica"]


def _interactive_map_variables(steps: list[dict]) -> tuple[list[dict], list[str]]:
    """Walk through filled values; ask the operator to assign each to a variable.

    Empty input means "leave as literal".
    """
    print()
    print("=== Variable mapping ===")
    print("For each captured value, type a variable name to parameterise it,")
    print("or just press Enter to keep the literal value.")
    print(f"Known variables: {', '.join(KNOWN_VARS)}")
    print()

    used: set[str] = set()
    out_steps: list[dict] = []
    for s in steps:
        if s.get("action") == "fill" and isinstance(s.get("value"), str) and s["value"]:
            sel = s["selector"]
            val = s["value"]
            display = val if len(val) < 60 else val[:57] + "..."
            try:
                answer = input(f"  fill {sel!s} = {display!r} → variable? ").strip()
            except EOFError:
                answer = ""
            if answer:
                used.add(answer)
                s = {**s, "value": "{{" + answer + "}}"}
        out_steps.append(s)
    return out_steps, sorted(used)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


app = typer.Typer(add_completion=False, help="Record a portal create-project playbook.")


@app.command()
def record(
    api_slug: str = typer.Option(..., "--api-slug", help="API slug, e.g. 'match'."),
    start_url: str = typer.Option(..., "--start-url", help="Portal URL to open."),
    organization: str = typer.Option("mastercard", "--organization"),
    headed: bool = typer.Option(True, "--headed/--headless"),
    no_prompt: bool = typer.Option(
        False, "--no-prompt",
        help="Skip interactive variable mapping; keep all literal values.",
    ),
) -> None:
    """Record the current portal flow into playbooks/<org>/<api-slug>.json."""
    asyncio.run(_record_async(api_slug, start_url, organization, headed, no_prompt))


async def _record_async(
    api_slug: str, start_url: str, organization: str, headed: bool, no_prompt: bool
) -> None:
    out_path = PLAYBOOK_ROOT / organization / f"{api_slug}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists():
        print(f"WARNING: {out_path} already exists and will be overwritten on save.")

    trace = CapturedTrace()
    stop = asyncio.Event()

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=not headed, args=["--foreground"])
        ctx_kwargs: dict = {"accept_downloads": True}
        if STATE_FILE.exists():
            ctx_kwargs["storage_state"] = str(STATE_FILE)
        context = await browser.new_context(**ctx_kwargs)

        async def on_new_page(page: Page) -> None:
            page.on(
                "framenavigated",
                lambda _f: asyncio.create_task(_install_recorder(page)),
            )
            page.on(
                "download",
                lambda d: trace.downloads.append(d.suggested_filename or ""),
            )
            await _install_recorder(page)

        context.on("page", lambda p: asyncio.create_task(on_new_page(p)))

        page = await context.new_page()
        await on_new_page(page)
        await page.bring_to_front()
        await page.goto(start_url, wait_until="domcontentloaded")
        await _install_recorder(page)

        poller = asyncio.create_task(_poll_loop(page, trace, stop))

        print()
        print("=" * 64)
        print("RECORDING. Complete the create-project flow in the browser.")
        print("When the project is created and you've downloaded the key,")
        print("press Enter HERE to stop recording.")
        print("=" * 64)
        print()

        # Wait for the operator's Enter on stdin without blocking the loop.
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, sys.stdin.readline)

        stop.set()
        # Drain remaining events.
        trace.events.extend(await _drain(page))
        await poller
        await context.close()
        await browser.close()

    # Compile.
    steps = _dedup_steps(_compile_steps(trace))
    if not steps:
        print("No actionable events captured — nothing written.")
        raise typer.Exit(1)

    variables: list[str] = []
    if not no_prompt:
        steps, variables = _interactive_map_variables(steps)
    # Always include known vars so the runner has stable inputs.
    for v in KNOWN_VARS:
        if v not in variables:
            variables.append(v)

    playbook = {
        "schema": 1,
        "organization": organization,
        "api_slug": api_slug,
        "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "start_url": start_url,
        "variables": variables,
        "steps": steps,
    }
    out_path.write_text(json.dumps(playbook, indent=2) + "\n")

    # Stash raw trace for debugging.
    stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    raw_dir = RECORD_ROOT / f"playbook_{api_slug}_{stamp}"
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / "trace.jsonl").write_text(
        "\n".join(json.dumps(e) for e in trace.events)
    )

    print()
    print(f"Wrote playbook: {out_path}")
    print(f"  steps: {len(steps)}")
    print(f"  variables: {', '.join(variables)}")
    print(f"  raw trace: {raw_dir}")


if __name__ == "__main__":
    app()
