"""Post-provisioning smoke tester for a Mastercard API.

Automatically called at the end of `provision-api`.
Can also be invoked standalone via the `test-api` CLI command.

Flow:
  1. Load credentials from config/.env + config/.env.generated.
  2. Call execute() on the first MANIFEST operation with its default params.
  3. If 401/403: wait for key activation (60 s × 3 retries).
  4. If 400 or empty response: fetch sandbox values from the docs URL.
  5. If good values found: retry, then patch MANIFEST defaults + how_to.
"""
from __future__ import annotations

import json
import os
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from loguru import logger


# ---------------------------------------------------------------------------
# Result type
# ---------------------------------------------------------------------------

@dataclass
class SmokeOutcome:
    api_id: str
    success: bool = False
    status_code: int | None = None
    error: str | None = None
    op_id: str | None = None
    params_used: dict[str, Any] = field(default_factory=dict)
    sandbox_values_found: bool = False
    manifest_updated: bool = False
    attempts: int = 0
    raw_response: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_ACTIVATION_WAIT_S = 60
_ACTIVATION_MAX_RETRIES = 3
_DOCS_VARIANTS = [
    "documentation/testing/",
    "documentation/sandbox/",
    "documentation/quick-start-guide/",
    "documentation/",
]


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def run_smoke(
    api_id: str,
    docs_url: str,
    vima_root: Path,
    *,
    env_file: Path | None = None,
) -> SmokeOutcome:
    """Smoke-test a recently provisioned Mastercard API.

    Calls execute() on the first MANIFEST operation. On failure, searches the
    docs URL for sandbox test values, retries with those values, and patches
    the MANIFEST if a successful response is obtained.
    """
    outcome = SmokeOutcome(api_id=api_id)

    _ensure_vima_root(vima_root)
    _load_env_files(vima_root, env_file)

    mod = _import_api(api_id)
    if mod is None:
        outcome.error = f"No module apis.{api_id}.api — API not yet wired"
        logger.warning("Smoke skipped: {}", outcome.error)
        return outcome

    manifest = getattr(mod, "MANIFEST", {})
    ops = manifest.get("operations") or []
    if not ops:
        outcome.error = "No operations in MANIFEST"
        logger.warning("Smoke skipped for {}: no operations", api_id)
        return outcome

    op = ops[0]
    op_id = op["id"]
    outcome.op_id = op_id
    params = {
        p["name"]: p.get("default")
        for p in op.get("params", [])
        if p.get("default") is not None
    }
    outcome.params_used = dict(params)

    # First call
    result = _call(mod, op_id, params)
    outcome.attempts = 1
    status_code = (result.get("response") or {}).get("status_code")
    outcome.status_code = status_code

    # 401/403 → key may still be activating
    if status_code in (401, 403):
        result, outcome.attempts = _wait_for_activation(mod, op_id, params, starting_attempts=1)
        status_code = (result.get("response") or {}).get("status_code")
        outcome.status_code = status_code

    if result.get("success") and _has_useful_data(result):
        outcome.success = True
        outcome.raw_response = result
        logger.info("Smoke PASS: {} op={} attempt={}", api_id, op_id, outcome.attempts)
        return outcome

    # 400 or empty response — look for better test values in docs
    logger.info(
        "Smoke call: status={} success={} — searching docs for test values…",
        status_code, result.get("success"),
    )
    slug = _slug_from_url(docs_url)
    sandbox_vals = _find_sandbox_values(slug, docs_url)

    if not sandbox_vals:
        outcome.error = (
            f"status={status_code}, no sandbox values found in docs. "
            f"Error: {result.get('error') or ''}"
        )
        outcome.raw_response = result
        logger.warning("Smoke FAIL: {} — {}", api_id, outcome.error)
        return outcome

    outcome.sandbox_values_found = True
    logger.info("Sandbox values: {}", list(sandbox_vals.keys()))

    updated = _apply_sandbox_values(op, sandbox_vals)
    outcome.params_used.update(updated)

    if updated:
        result = _call(mod, op_id, outcome.params_used)
        outcome.attempts += 1
        status_code = (result.get("response") or {}).get("status_code")
        outcome.status_code = status_code

    if result.get("success") and _has_useful_data(result):
        outcome.success = True
        outcome.raw_response = result
        logger.info(
            "Smoke PASS with sandbox values: {} op={} attempt={}",
            api_id, op_id, outcome.attempts,
        )
        try:
            _patch_manifest(api_id, vima_root, ops, sandbox_vals, docs_url)
            outcome.manifest_updated = True
            logger.info("MANIFEST patched with sandbox values for {}", api_id)
        except Exception as exc:
            logger.warning("MANIFEST patch failed (non-fatal): {}", exc)
    else:
        outcome.error = (
            f"status={status_code} even with sandbox values. "
            f"Error: {result.get('error') or ''}"
        )
        outcome.raw_response = result
        logger.warning("Smoke FAIL after sandbox retry: {} — {}", api_id, outcome.error)

    return outcome


# ---------------------------------------------------------------------------
# API invocation helpers
# ---------------------------------------------------------------------------

def _ensure_vima_root(vima_root: Path) -> None:
    if str(vima_root) not in sys.path:
        sys.path.insert(0, str(vima_root))


def _import_api(api_id: str):
    import importlib
    try:
        mod = importlib.import_module(f"apis.{api_id}.api")
        importlib.reload(mod)  # Pick up freshly loaded env vars
        return mod
    except ImportError:
        return None


def _call(mod, op_id: str, params: dict[str, Any]) -> dict[str, Any]:
    try:
        return mod.execute(op_id, params)
    except Exception as exc:
        return {"success": False, "error": f"{type(exc).__name__}: {exc}", "response": {}}


def _wait_for_activation(
    mod, op_id: str, params: dict[str, Any], *, starting_attempts: int
) -> tuple[dict[str, Any], int]:
    attempts = starting_attempts
    result: dict[str, Any] = {}
    for i in range(_ACTIVATION_MAX_RETRIES):
        logger.info(
            "Key not yet active (401/403) — waiting {}s (retry {}/{})…",
            _ACTIVATION_WAIT_S, i + 1, _ACTIVATION_MAX_RETRIES,
        )
        time.sleep(_ACTIVATION_WAIT_S)
        result = _call(mod, op_id, params)
        attempts += 1
        if (result.get("response") or {}).get("status_code") not in (401, 403):
            break
    return result, attempts


def _has_useful_data(result: dict[str, Any]) -> bool:
    if not result.get("success"):
        return False
    return _nonempty(result.get("data"))


def _nonempty(obj: Any, depth: int = 0) -> bool:
    if depth > 4 or obj is None:
        return False if obj is None else bool(obj)
    if isinstance(obj, list):
        return len(obj) > 0
    if isinstance(obj, dict):
        return any(_nonempty(v, depth + 1) for v in obj.values())
    if isinstance(obj, str):
        return bool(obj.strip())
    return bool(obj)


# ---------------------------------------------------------------------------
# Sandbox value discovery
# ---------------------------------------------------------------------------

def _slug_from_url(url: str) -> str:
    from urllib.parse import urlparse
    path = urlparse(url).path.strip("/")
    return path.split("/")[0] if path else ""


def _find_sandbox_values(slug: str, docs_url: str) -> dict[str, Any]:
    """Try docs URL variants and extract test values from the page."""
    import requests

    base = f"https://developer.mastercard.com/{slug}/" if slug else ""
    candidates: list[str] = [docs_url]
    for variant in _DOCS_VARIANTS:
        url = base + variant
        if url not in candidates:
            candidates.append(url)

    for url in candidates:
        try:
            resp = requests.get(url, timeout=15, headers={"User-Agent": "vima/1.0"})
            if resp.status_code != 200 or len(resp.text) < 300:
                continue
            vals = _extract_with_claude(resp.text, url) or _extract_heuristic(resp.text)
            if vals:
                logger.info("Sandbox values extracted from: {}", url)
                return vals
        except Exception as exc:
            logger.debug("Fetch failed for {}: {}", url, exc)

    return {}


def _extract_with_claude(html: str, url: str) -> dict[str, Any] | None:
    """Use Claude Haiku to extract sandbox test values from docs HTML."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not api_key:
        return None

    try:
        import anthropic

        client = anthropic.Anthropic(api_key=api_key)
        prompt = (
            "Extract sandbox/test values from this Mastercard Developers API docs page.\n\n"
            f"URL: {url}\n\nHTML (truncated):\n```html\n{html[:12000]}\n```\n\n"
            "Return ONLY a JSON object mapping parameter names (snake_case) to example test values. "
            'Example: {"account_range": "543210", "country_code": "USA"}. '
            "Only include values explicitly shown as sandbox/test data. "
            "If none found, return {}."
        )
        msg = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=400,
            messages=[{"role": "user", "content": prompt}],
        )
        text = (msg.content[0].text or "").strip()
        start, end = text.find("{"), text.rfind("}") + 1
        if start >= 0 and end > start:
            result = json.loads(text[start:end])
            return result if isinstance(result, dict) and result else None
    except Exception as exc:
        logger.debug("Claude extraction failed: {}", exc)

    return None


def _extract_heuristic(html: str) -> dict[str, Any]:
    """Fallback: pull plausible test values from <code> blocks in docs HTML."""
    import re

    vals: dict[str, Any] = {}
    code_texts = re.findall(r"<code[^>]*>(.*?)</code>", html, re.DOTALL)
    for block in code_texts:
        text = re.sub(r"<[^>]+>", "", block).strip()
        if not text or len(text) > 60 or "\n" in text:
            continue
        if re.match(r"^\d{6,8}$", text):
            vals.setdefault("account_range", text)
            vals.setdefault("bin", text)
        elif re.match(r"^\d{9,19}$", text):
            vals.setdefault("card_number", text)
            vals.setdefault("account_number", text)
        elif re.match(r"^[A-Z]{3}$", text):
            vals.setdefault("country_code", text)
        elif re.match(r"^[A-Z]{2}$", text):
            vals.setdefault("country_code", text)
    return vals


def _apply_sandbox_values(op: dict[str, Any], sandbox_vals: dict[str, Any]) -> dict[str, Any]:
    return {
        p["name"]: sandbox_vals[p["name"]]
        for p in op.get("params", [])
        if p["name"] in sandbox_vals
    }


# ---------------------------------------------------------------------------
# Env helpers
# ---------------------------------------------------------------------------

def _load_env_files(vima_root: Path, extra: Path | None = None) -> None:
    for path in [vima_root / "config" / ".env", vima_root / "config" / ".env.generated"]:
        _load_dotenv(path)
    if extra:
        _load_dotenv(extra)


def _load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


# ---------------------------------------------------------------------------
# MANIFEST patching
# ---------------------------------------------------------------------------

def _patch_manifest(
    api_id: str,
    vima_root: Path,
    ops: list[dict],
    sandbox_vals: dict[str, Any],
    docs_url: str,
) -> None:
    api_file = vima_root / "apis" / api_id / "api.py"
    if not api_file.exists():
        logger.warning("apis/{}/api.py not found — skipping MANIFEST patch", api_id)
        return

    source = api_file.read_text()
    original = source

    for op in ops:
        for param in op.get("params", []):
            name = param["name"]
            if name in sandbox_vals:
                source = _update_param_default(source, op["id"], name, sandbox_vals[name])

    sandbox_html = _build_sandbox_html(ops, sandbox_vals, docs_url)
    source = _upsert_how_to_sandbox(source, sandbox_html)

    if source != original:
        api_file.write_text(source)


def _update_param_default(source: str, op_id: str, param_name: str, new_value: Any) -> str:
    """Replace the "default" value for a param within a named operation block."""
    import re

    new_repr = json.dumps(str(new_value))

    op_match = re.search(r'"id"\s*:\s*"' + re.escape(op_id) + r'"', source)
    if not op_match:
        return source

    # Search for param within next 3000 chars of the operation
    window_start = op_match.start()
    window = source[window_start:window_start + 3000]
    param_match = re.search(r'"name"\s*:\s*"' + re.escape(param_name) + r'"', window)
    if not param_match:
        return source

    # Search for "default": <value> within next 500 chars of the param
    pw_start = window_start + param_match.start()
    pw = source[pw_start:pw_start + 500]
    dm = re.search(r'("default"\s*:\s*)("[^"]*"|\'[^\']*\'|\d+(?:\.\d+)?)', pw)
    if not dm:
        return source

    replaced = pw.replace(dm.group(0), dm.group(1) + new_repr, 1)
    return source[:pw_start] + replaced + source[pw_start + 500:]


def _build_sandbox_html(ops: list[dict], sandbox_vals: dict[str, Any], docs_url: str) -> str:
    slug = _slug_from_url(docs_url)
    testing_url = (
        f"https://developer.mastercard.com/{slug}/documentation/testing/" if slug else docs_url
    )
    parts = [
        "<h3>Sandbox test values</h3>",
        f"<p>Official sandbox data: "
        f"<a href='{testing_url}' target='_blank'>{slug or 'testing page'}</a>.</p>",
        "<ul>",
    ]
    for op in ops:
        items = [
            f"<code>{p['name']}={sandbox_vals[p['name']]}</code>"
            for p in op.get("params", [])
            if p["name"] in sandbox_vals
        ]
        if items:
            parts.append(f"<li><strong>{op['name']}</strong>: {', '.join(items)}.</li>")
    parts.append("</ul>")
    return "".join(parts)


def _upsert_how_to_sandbox(source: str, sandbox_html: str) -> str:
    """Insert or replace the sandbox section in the how_to Python expression."""
    import ast

    how_to_start = source.find('"how_to"')
    if how_to_start == -1:
        return source

    colon_pos = source.find(":", how_to_start)
    if colon_pos == -1:
        return source

    val_start = colon_pos + 1
    while val_start < len(source) and source[val_start] in " \t\n":
        val_start += 1

    if val_start >= len(source):
        return source

    if source[val_start] == "(":
        val_end = _find_matching_paren(source, val_start)
    elif source[val_start] in ('"', "'"):
        val_end = _find_string_end(source, val_start)
    else:
        return source

    if val_end == -1:
        return source

    expr = source[val_start:val_end + 1]
    try:
        current_value: str = ast.literal_eval(expr)
    except Exception as exc:
        logger.debug("Could not parse how_to value: {}", exc)
        return source

    sandbox_marker = "<h3>Sandbox test values</h3>"
    if sandbox_marker in current_value:
        current_value = current_value[:current_value.find(sandbox_marker)]

    new_value = current_value + sandbox_html
    new_expr = "(\n        " + json.dumps(new_value) + "\n    )"
    return source[:val_start] + new_expr + source[val_end + 1:]


def _find_matching_paren(source: str, pos: int) -> int:
    """Index of the ) matching the ( at pos. Skips string literal contents."""
    depth = 0
    i = pos
    n = len(source)
    while i < n:
        ch = source[i]
        if ch in ('"', "'"):
            triple = source[i:i + 3]
            if triple in ('"""', "'''"):
                end = source.find(triple, i + 3)
                if end == -1:
                    return -1
                i = end + 3
                continue
            q = ch
            i += 1
            while i < n:
                if source[i] == "\\" and i + 1 < n:
                    i += 2
                    continue
                if source[i] == q:
                    i += 1
                    break
                i += 1
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def _find_string_end(source: str, pos: int) -> int:
    """Index of the closing quote for a string starting at pos."""
    q = source[pos]
    triple = source[pos:pos + 3]
    if triple in ('"""', "'''"):
        end = source.find(triple, pos + 3)
        return (end + 2) if end != -1 else -1
    i = pos + 1
    n = len(source)
    while i < n:
        if source[i] == "\\" and i + 1 < n:
            i += 2
            continue
        if source[i] == q:
            return i
        i += 1
    return -1
