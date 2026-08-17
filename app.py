"""Vima — Mastercard APIs explorer.

A small Flask app on port 9021 that exposes a tabbed UI for testing
Mastercard Developer APIs (Open Finance, BIN Lookup, …) and demoing use
cases composed from them.
"""
import warnings

warnings.filterwarnings("ignore", message="resource_tracker", category=UserWarning)
import argparse
import json
import os
import queue
import subprocess
import sys
import threading
import time
import uuid
from collections import deque
from functools import wraps

import truststore

truststore.inject_into_ssl()

import requests as _requests
from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request, send_from_directory, url_for

_CONFIG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config")
load_dotenv(os.path.join(_CONFIG_DIR, ".env"))

import live_demo  # noqa: E402
from apis import registry as api_registry  # noqa: E402
from apis import spotlights as api_spotlights  # noqa: E402
from simulator.blueprint import sim_bp  # noqa: E402
from simulator.capture import capture_response  # noqa: E402
from simulator.switcher import is_simulated  # noqa: E402
from usecases import registry as usecase_registry  # noqa: E402

app = Flask(__name__)
from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

# Suppress Werkzeug's per-request stdout log lines ("GET /... 200")
import logging as _logging

_logging.getLogger("werkzeug").setLevel(_logging.ERROR)

# Register the in-process Vima Chat blueprint at /chat. Vima Chat is no
# longer a standalone service — it lives inside Mastercard Solution Studio.
from chat.app import chat_bp  # noqa: E402

app.register_blueprint(chat_bp)
app.secret_key = os.environ.get("SECRET_KEY", "vima-dev-secret")
app.register_blueprint(sim_bp)

# Test results dashboard — mounted at /vima/test
# Lives in tests/ to keep it separate from production app code.
# The DB (tests/results.db) and config (tests/test_config.ini) are gitignored.
try:
    from tests.dashboard import test_bp as _test_bp  # noqa: E402
    app.register_blueprint(_test_bp)
except Exception as _e:  # pragma: no cover
    import logging as _lg
    _lg.getLogger(__name__).warning("Test dashboard unavailable: %s", _e)

# Eagerly trigger Open Finance customer seeding in the background so that
# the state strip is populated by the time the user navigates to the tab.
def _eager_seed_ofin():
    try:
        ofin_mod = api_registry.get_module("open_finance")
        if ofin_mod and hasattr(ofin_mod, "_trigger_background_seed"):
            ofin_mod._trigger_background_seed()
    except Exception:
        pass

import threading as _threading

_threading.Thread(target=_eager_seed_ofin, daemon=True, name="ofin-eager-seed").start()

# In-memory store for TxPush events (last 50)
_txpush_events: deque = deque(maxlen=50)

# ---------------------------------------------------------------------------
# Outbound API call logger — intercepts all `requests` calls to external APIs
# ---------------------------------------------------------------------------
_api_call_log: deque = deque(maxlen=50)
_api_call_seq = 0
_api_call_lock = threading.Lock()

# URLs containing these substrings are considered "internal" and are skipped
_INTERNAL_HOSTS = ("localhost", "127.0.0.1", "0.0.0.0", "::1", "cloudflare.com")  # nosec B104

_orig_send = _requests.Session.send  # keep reference before patching


def _patched_send(self, prepared_request, **kwargs):
    url = prepared_request.url or ""
    # Log simulator requests (/api-sim/) even though they're on localhost
    is_simulator = "/api-sim/" in url
    is_external = is_simulator or not any(h in url for h in _INTERNAL_HOSTS)

    # Skip internal-only requests (no capturing needed)
    if not is_external:
        return _orig_send(self, prepared_request, **kwargs)

    global _api_call_seq
    t0 = time.time()
    try:
        body_bytes = prepared_request.body
        if isinstance(body_bytes, bytes):
            try:
                import json as _json
                req_body = _json.loads(body_bytes)
            except Exception:
                req_body = body_bytes.decode("utf-8", errors="replace")
        elif isinstance(body_bytes, str):
            try:
                import json as _json
                req_body = _json.loads(body_bytes)
            except Exception:
                req_body = body_bytes
        else:
            req_body = None
    except Exception:
        req_body = None

    entry: dict = {
        "seq": None,
        "ts": time.strftime("%H:%M:%S"),
        "method": (prepared_request.method or "").upper(),
        "url": url,
        "requestBody": req_body,
        "requestHeaders": {k: v for k, v in prepared_request.headers.items() if k.lower() != "authorization"},
        "status": None,
        "responseBody": None,
        "responseHeaders": None,
        "elapsed_ms": None,
    }

    try:
        resp = _orig_send(self, prepared_request, **kwargs)
    except Exception:
        entry["status"] = "ERR"
        entry["elapsed_ms"] = round((time.time() - t0) * 1000)
        with _api_call_lock:
            _api_call_seq += 1
            entry["seq"] = _api_call_seq
            _api_call_log.appendleft(entry)
        raise

    entry["status"] = resp.status_code
    entry["elapsed_ms"] = round((time.time() - t0) * 1000)
    entry["responseHeaders"] = dict(resp.headers)
    try:
        entry["responseBody"] = resp.json()
    except Exception:
        entry["responseBody"] = resp.text

    with _api_call_lock:
        _api_call_seq += 1
        entry["seq"] = _api_call_seq
        _api_call_log.appendleft(entry)

    return resp


_requests.Session.send = _patched_send

# ---------------------------------------------------------------------------
# Client geo/IP status cache (for Open Finance US VPN indicator)
# ---------------------------------------------------------------------------
_ip_status_cache = {
    "ts": 0.0,
    "payload": None,
}


def _parse_runtime_flags(argv: list[str]) -> argparse.Namespace:
    """Parse runtime flags used when launching app.py directly.

    parse_known_args is used so unknown flags from external launchers do not
    break startup.
    """
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument(
        "--server",
        action="store_true",
        help="Run in server mode: hide/disable sensitive config surfaces.",
    )
    parser.add_argument(
        "--non-us",
        action="store_true",
        help="Force non-US behavior: disable Open Finance US API and dependent use cases.",
    )
    parser.add_argument(
        "--host",
        default=os.environ.get("HOST", "0.0.0.0"),  # nosec B104 — configurable dev server binding
        help="Host interface to bind.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("PORT", "9021")),
        help="Port to bind.",
    )
    args, _ = parser.parse_known_args(argv)
    return args


_RUNTIME_FLAGS = _parse_runtime_flags(sys.argv[1:] if __name__ == "__main__" else [])
_SERVER_MODE = _RUNTIME_FLAGS.server or os.environ.get("VIMA_SERVER_MODE", "").strip().lower() in {
    "1", "true", "yes", "on"
}
_FORCE_NON_US = _RUNTIME_FLAGS.non_us or os.environ.get("VIMA_NON_US", "").strip().lower() in {
    "1", "true", "yes", "on"
}
_OPEN_FINANCE_US_API_ID = "open_finance"
_NON_US_DISABLED_HINT = (
    "Disabled in --non-us mode. This Open Finance US capability requires a US IP. "
    "If running on a US IP, this item would be enabled."
)


def _server_mode_enabled() -> bool:
    return bool(_SERVER_MODE)


def _non_us_mode_enabled() -> bool:
    return bool(_FORCE_NON_US)


def _server_mode_forbidden_response():
    return jsonify({"error": "Disabled in server mode."}), 403


def _non_us_forbidden_response():
    return jsonify({
        "error": _NON_US_DISABLED_HINT
    }), 403


def _require_not_server_mode(fn):
    @wraps(fn)
    def _wrapped(*args, **kwargs):
        if _server_mode_enabled():
            return _server_mode_forbidden_response()
        return fn(*args, **kwargs)
    return _wrapped


def _is_non_us_blocked_api(api_id: str) -> bool:
    return _non_us_mode_enabled() and api_id == _OPEN_FINANCE_US_API_ID


def _is_non_us_blocked_usecase(uc_id: str) -> bool:
    if not _non_us_mode_enabled():
        return False
    mod = usecase_registry.get_module(uc_id)
    if mod is None:
        return False
    manifest = getattr(mod, "MANIFEST", {}) or {}
    return _OPEN_FINANCE_US_API_ID in (manifest.get("apis") or [])


@app.before_request
def _enforce_server_mode_surfaces():
    """Block sensitive surfaces that must be unavailable in server mode."""
    if _server_mode_enabled() and request.path.startswith("/chat"):
        return _server_mode_forbidden_response()
    return None


def _fetch_geo_payload(client_ip: str) -> dict:
    """Resolve country and public IP using external geo services."""
    # Prefer a plain-text trace endpoint that exposes the egress country directly.
    attempts = [
        ("https://www.cloudflare.com/cdn-cgi/trace", "cloudflare-trace"),
        ("https://ipapi.co/json/", "ipapi"),
        ("https://ipwho.is/", "ipwhois"),
        ("https://ipinfo.io/json", "ipinfo"),
    ]

    for url, provider in attempts:
        try:
            # verify=False: VPN SSL-inspection injects a self-signed cert into the
            # chain, causing standard cert verification to fail.  These requests
            # carry no credentials so disabling verification here is safe.
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            resp = _requests.get(url, timeout=4.0, verify=False)  # nosec B501
            resp.raise_for_status()
            raw = resp.text
            if provider == "cloudflare-trace":
                trace = {}
                for line in raw.splitlines():
                    if "=" in line:
                        key, value = line.split("=", 1)
                        trace[key.strip()] = value.strip()
                country = (trace.get("loc") or "").upper()
                detected_ip = trace.get("ip") or client_ip
            else:
                data = json.loads(raw)
                if provider == "ipapi":
                    country = (data.get("country_code") or data.get("country") or "").upper()
                    detected_ip = data.get("ip") or client_ip
                elif provider == "ipwhois":
                    country = (data.get("country_code") or data.get("country") or "").upper()
                    detected_ip = data.get("ip") or client_ip
                else:
                    country = (data.get("country") or "").upper()
                    detected_ip = data.get("ip") or client_ip
            if country:
                return {
                    "ok": True,
                    "provider": provider,
                    "country_code": country,
                    "ip": str(detected_ip or ""),
                }
        except Exception:
            continue

    return {
        "ok": False,
        "provider": None,
        "country_code": "",
        "ip": str(client_ip or ""),
    }


# ----------------------------------------------------------------------------
# Pages
# ----------------------------------------------------------------------------

# Ordered stylesheet list (loaded as individual <link>s in this exact order so
# the cascade matches the former single styles.css). base.css must stay first.
CSS_FILES = [
    "css/base.css",
    "css/features/enrichment.css",
    "css/features/psi.css",
    "css/platform/api-calls.css",
    "css/features/bin-lookup.css",
    "css/features/consumer-clarity.css",
    "css/features/easy-savings.css",
    "css/platform/chat-modal.css",
    "css/features/sonic.css",
    "css/platform/home.css",
    "css/platform/config-modal.css",
    "css/features/idv.css",
    "css/features/medicare.css",
    "css/features/mastercard-connect.css",
    "css/platform/about-panel.css",
    "css/platform/provision.css",
    "css/platform/explorer-dark.css",
    "css/platform/bundles.css",
    "css/platform/theme-coverage.css",
    "css/platform/api-guide.css",
    "css/platform/launch-banner.css",
    "css/platform/sdk-panel.css",
    "css/platform/info-modal.css",
    "css/platform/search.css",
]


def _css_bust() -> int:
    """Newest mtime across the split stylesheets, for cache-busting links."""
    base = os.path.dirname(__file__)
    newest = 0.0
    for rel in CSS_FILES:
        try:
            newest = max(newest, os.path.getmtime(os.path.join(base, "static", *rel.split("/"))))
        except OSError:
            pass
    return int(newest)


@app.route("/")
def home():
    return redirect(url_for("index"))


@app.route("/app")
def index():
    _apis = api_registry.manifests()
    return render_template(
        "index.html",
        apis=_apis,
        api_groups=api_registry.manifests_grouped(),
        solutions=api_registry.solutions(),
        bundles=api_registry.solutions(),
        use_cases=usecase_registry.manifests(),
        spotlight=_build_spotlight(_apis),
        provision_catalog=_build_provision_catalog(),
        runtime_mode={
            "server_mode": _server_mode_enabled(),
            "non_us_mode": _non_us_mode_enabled(),
        },
        cache_bust=int(os.path.getmtime(os.path.join(os.path.dirname(__file__), 'static', 'js', 'app', 'main.js'))),
        css_files=CSS_FILES,
        css_bust=_css_bust(),
    )


def _build_spotlight(apis):
    """Combine today's spotlight pick with its catalog metadata.

    Returns ``None`` when no APIs are registered (fresh install) so the
    template can render a graceful no-op rather than a broken card.

    The returned dict also carries an ``all`` list — every registered API
    with its spotlight content — so the modal can let users browse every
    "API of the day" with prev/next navigation. The ``index`` field marks
    where today's pick sits in that list so the modal can open on it.
    """
    if not apis:
        return None
    spotlight_id = api_spotlights.pick_today([a["id"] for a in apis])
    if not spotlight_id:
        return None
    api = next((a for a in apis if a["id"] == spotlight_id), None)
    if not api:
        return None
    content = api_spotlights.for_api(spotlight_id)

    def _entry(a):
        c = api_spotlights.for_api(a["id"])
        return {
            "id": a["id"],
            "name": a.get("name", a["id"]),
            "group": a.get("group", ""),
            "docs_url": a.get("docs_url", ""),
            "configured": bool(a.get("configured")),
            "insight": c["insight"],
            "example": c["example"],
        }

    all_entries = [_entry(a) for a in apis]
    today_index = next(
        (i for i, e in enumerate(all_entries) if e["id"] == spotlight_id),
        0,
    )

    return {
        "id": api["id"],
        "name": api.get("name", api["id"]),
        "group": api.get("group", ""),
        "docs_url": api.get("docs_url", ""),
        "configured": bool(api.get("configured")),
        "insight": content["insight"],
        "example": content["example"],
        "studio_url": f"/app?tab=apis&api={api['id']}",
        "all": all_entries,
        "index": today_index,
    }


# ----------------------------------------------------------------------------
# API explorer endpoints
# ----------------------------------------------------------------------------

@app.route("/explorer/apis")
def explorer_apis():
    """Return the manifests for every registered API."""
    return jsonify({"apis": api_registry.manifests()})


@app.route("/diagnostics/us-ip-status")
def diagnostics_us_ip_status():
    """Return whether the caller appears to be on a US IP address."""
    now = time.time()
    if _non_us_mode_enabled():
        payload = {
            "success": True,
            "is_us": False,
            "country_code": "NON-US",
            "ip": "runtime-flag",
            "provider": "runtime-flag",
            "source": "runtime-flag",
            "checked_at": int(now),
            "forced": True,
        }
        resp = jsonify(payload)
        resp.headers["Cache-Control"] = "no-store"
        return resp

    client_ip = (request.remote_addr or "").strip()
    cached = _ip_status_cache.get("payload")
    if cached and (now - float(_ip_status_cache.get("ts") or 0)) < 20:
        resp = jsonify(cached)
        resp.headers["Cache-Control"] = "no-store"
        return resp

    geo = _fetch_geo_payload(client_ip)
    country = (geo.get("country_code") or "").upper()
    is_us = country == "US"

    payload = {
        "success": bool(geo.get("ok")),
        "is_us": is_us,
        "country_code": country,
        "ip": geo.get("ip") or client_ip,
        "provider": geo.get("provider"),
        "checked_at": int(now),
    }
    _ip_status_cache["ts"] = now
    _ip_status_cache["payload"] = payload

    resp = jsonify(payload)
    resp.headers["Cache-Control"] = "no-store"
    return resp


@app.route("/explorer/<api_id>/state")
def explorer_state(api_id: str):
    if _is_non_us_blocked_api(api_id):
        return _non_us_forbidden_response()
    mod = api_registry.get_module(api_id)
    if mod is None:
        return jsonify({"error": "Unknown API"}), 404
    state = getattr(mod, "get_state", lambda: {})()
    return jsonify({"state": state})


def _api_credentials(
    api_id: str,
    manifest: dict,
    resolve_paths: bool = False,
) -> tuple[str, list[str], list[str], list[tuple[str, str]]]:
    """Return (env_prefix, var_names, packages, env_pairs) for an API.

    Used by /explorer/<api_id>/setup and /explorer/<api_id>/run so both
    routes resolve credentials identically without duplicating the logic.
    When *resolve_paths* is True, relative *_PATH env vars are resolved to
    absolute paths against the project root (needed when spawning a terminal
    that runs from a temp directory).
    """
    from apis import snippet as api_snippet

    env_prefix = manifest.get("env_prefix") or api_id.upper()
    of_runtime = (
        api_snippet.of_runtime_for_prefix(env_prefix)
        if api_id.startswith("open_finance")
        else None
    )
    if of_runtime:
        var_names: list[str] = of_runtime["env_var_names"]
        packages: list[str] = of_runtime["packages"]
    else:
        var_names = [
            f"{env_prefix}_CONSUMER_KEY",
            f"{env_prefix}_SIGNING_KEY_PATH",
            f"{env_prefix}_SIGNING_KEY_PASSWORD",
        ]
        packages = ["requests", "mastercard-oauth1-signer"]

    env_pairs: list[tuple[str, str]] = [(n, os.environ.get(n, "")) for n in var_names]
    if resolve_paths:
        project_root = os.path.dirname(os.path.abspath(__file__))
        resolved: list[tuple[str, str]] = []
        for name, val in env_pairs:
            if val and name.endswith("_PATH") and not os.path.isabs(val):
                candidate = os.path.normpath(os.path.join(project_root, val))
                if os.path.exists(candidate):
                    val = candidate
            resolved.append((name, val))
        env_pairs = resolved

    return env_prefix, var_names, packages, env_pairs
@app.route("/explorer/<api_id>/snippet")
def explorer_snippet(api_id: str):
    """Return an authentic Python snippet showing how to call the
    underlying Mastercard API directly (OAuth1 signing or vendor-specific
    auth) — bypassing the Solution Studio proxy.

    Query string: ``op=<operation_id>`` (defaults to the first operation
    declared in the API's MANIFEST).
    """
    from apis import snippet as api_snippet
    mod = api_registry.get_module(api_id)
    if mod is None:
        return jsonify({"error": "Unknown API"}), 404
    manifest = next(
        (m for m in api_registry.manifests() if m.get("id") == api_id),
        None,
    )
    if manifest is None:
        return jsonify({"error": "API manifest unavailable"}), 404
    op_id = (request.args.get("op") or "").strip()
    if not op_id and manifest.get("operations"):
        op_id = manifest["operations"][0]["id"]
    if not op_id:
        return jsonify({"error": "No operations defined"}), 404
    return jsonify(api_snippet.build_snippet(api_id, op_id, mod=mod, manifest=manifest))


@app.route("/explorer/<api_id>/setup")
@_require_not_server_mode
def explorer_setup(api_id: str):
    """Return OS-specific shell commands that install the snippet's
    dependencies and export the credentials the snippet needs.

    The values come from the local Solution Studio config (the same env
    vars Solution Studio itself reads), so the commands are ready to
    paste into a fresh terminal on the demo machine. Disabled in server
    mode — credentials must never leave the host that way.
    """
    manifest = next(
        (m for m in api_registry.manifests() if m.get("id") == api_id),
        None,
    )
    if manifest is None:
        return jsonify({"error": "Unknown API"}), 404

    env_prefix, var_names, packages, env_pairs = _api_credentials(
        api_id, manifest, resolve_paths=True
    )

    env: list[dict[str, str]] = [
        {
            "name": name,
            "value": val,
            "set": name in os.environ and bool(os.environ.get(name)),
        }
        for name, val in env_pairs
    ]

    return jsonify({
        "api_id": api_id,
        "env_prefix": env_prefix,
        "packages": packages,
        "env": env,
    })


@app.route("/explorer/<api_id>/run", methods=["POST"])
@_require_not_server_mode
def explorer_run(api_id: str):
    """Write the runnable snippet to a temp script and launch the host
    OS's native terminal so the user can watch it execute.

    The script does the full set-env / pip-install / run-snippet flow
    using the same credentials the rest of Solution Studio reads. After
    the snippet finishes, the terminal pauses so the user can read the
    request + response printout before the window closes.

    Disabled in server mode — spawning a terminal on the host only ever
    makes sense for the local demo workflow.
    """
    import platform
    import shlex
    import subprocess
    import tempfile
    from pathlib import Path

    from apis import snippet as api_snippet

    mod = api_registry.get_module(api_id)
    if mod is None:
        return jsonify({"error": "Unknown API"}), 404
    manifest = next(
        (m for m in api_registry.manifests() if m.get("id") == api_id),
        None,
    )
    if manifest is None:
        return jsonify({"error": "API manifest unavailable"}), 404

    body = request.get_json(silent=True) or {}
    op_id = (body.get("operation") or "").strip()
    if not op_id and manifest.get("operations"):
        op_id = manifest["operations"][0]["id"]
    if not op_id:
        return jsonify({"error": "No operations defined"}), 400

    # Allow the UI to send an edited version of the snippet. If the
    # caller provides a `code` string, run that verbatim; otherwise
    # build the canonical snippet for this operation.
    override_code = body.get("code")
    if isinstance(override_code, str) and override_code.strip():
        code = override_code
    else:
        snippet_payload = api_snippet.build_snippet(api_id, op_id, mod=mod, manifest=manifest)
        code = snippet_payload.get("snippet") or ""

    # Resolve credentials using the same helper as /setup so the spawned
    # terminal sees what the local server sees, with paths made absolute.
    _env_prefix, _var_names, packages, env_pairs = _api_credentials(
        api_id, manifest, resolve_paths=True
    )

    system = platform.system().lower()
    tmpdir = Path(tempfile.gettempdir()) / "vima-snippets"
    tmpdir.mkdir(parents=True, exist_ok=True)

    if system == "windows":
        # PowerShell script: set env vars, install deps via `py -m pip`
        # (works around corporate AV blocking pip.exe), write the snippet
        # to a .py file next to the .ps1, run it, then pause.
        py_path = tmpdir / f"{api_id}_{op_id}.py"
        ps1_path = tmpdir / f"{api_id}_{op_id}.ps1"
        py_path.write_text(code, encoding="utf-8")

        def _ps_quote(v: str) -> str:
            return "'" + (v or "").replace("'", "''") + "'"

        lines = [
            "$ErrorActionPreference = 'Continue'",
            "Write-Host 'Mastercard Solution Studio - running snippet for " + api_id + "' -ForegroundColor Cyan",
            "Write-Host ''",
            # The Flask process that launched this terminal may itself be
            # running inside a venv (e.g. tools/mcd-key-automation/.venv).
            # That venv leaks via VIRTUAL_ENV/PYTHONHOME into the child
            # shell, which makes `pip install --user` fail with
            # "User site-packages are not visible in this virtualenv".
            # Scrub the venv env vars so `py` picks the system Python
            # cleanly and --user installs into the user site as intended.
            "Remove-Item Env:VIRTUAL_ENV    -ErrorAction SilentlyContinue",
            "Remove-Item Env:PYTHONHOME     -ErrorAction SilentlyContinue",
            "Remove-Item Env:VIRTUAL_ENV_PROMPT -ErrorAction SilentlyContinue",
        ]
        for name, val in env_pairs:
            lines.append(f"$env:{name} = {_ps_quote(val)}")
        if packages:
            lines.append("Write-Host 'Installing dependencies...' -ForegroundColor DarkGray")
            lines.append(f"py -m pip install --user --quiet {' '.join(packages)}")
        lines += [
            "Write-Host ''",
            f"py {_ps_quote(str(py_path))}",
            "$code = $LASTEXITCODE",
            "Write-Host ''",
            "Write-Host ('Exit code: ' + $code) -ForegroundColor Cyan",
            "Write-Host 'Press Enter to close...' -ForegroundColor DarkGray",
            "Read-Host | Out-Null",
        ]
        ps1_path.write_text("\r\n".join(lines), encoding="utf-8")

        # Launch a new PowerShell window. Prefer Windows Terminal (wt.exe)
        # if available because it stays visible and looks better; fall
        # back to conhost-hosted powershell.exe.
        powershell_args = [
            "powershell.exe", "-NoLogo", "-ExecutionPolicy", "Bypass",
            "-File", str(ps1_path),
        ]
        try:
            subprocess.Popen(
                ["wt.exe", "new-tab", "--title", f"Mastercard Solution Studio: {api_id}", *powershell_args],
                close_fds=True,
            )
            launcher = "wt"
        except FileNotFoundError:
            subprocess.Popen(
                powershell_args,
                creationflags=getattr(subprocess, "CREATE_NEW_CONSOLE", 0),
                close_fds=True,
            )
            launcher = "powershell"

    elif system == "darwin":
        sh_path = tmpdir / f"{api_id}_{op_id}.sh"
        py_path = tmpdir / f"{api_id}_{op_id}.py"
        py_path.write_text(code, encoding="utf-8")
        lines = [
            "#!/bin/bash",
            "set +e",
            f"echo 'Mastercard Solution Studio - running snippet for {api_id}'",
            # See the Windows branch for why we scrub these — the Flask
            # process may have been launched inside a venv, and that
            # makes `pip install --user` refuse to run.
            "unset VIRTUAL_ENV PYTHONHOME VIRTUAL_ENV_PROMPT",
            "",
        ]
        for name, val in env_pairs:
            lines.append(f"export {name}={shlex.quote(val)}")
        if packages:
            lines.append("echo 'Installing dependencies...'")
            lines.append(f"python3 -m pip install --user --quiet {' '.join(packages)}")
        lines += ["echo", f"python3 {shlex.quote(str(py_path))}",
                  "echo", "echo 'Press Enter to close...'", "read"]
        sh_path.write_text("\n".join(lines), encoding="utf-8")
        sh_path.chmod(0o755)
        subprocess.Popen(["open", "-a", "Terminal", str(sh_path)], close_fds=True)
        launcher = "Terminal.app"

    else:  # Linux + other POSIX
        sh_path = tmpdir / f"{api_id}_{op_id}.sh"
        py_path = tmpdir / f"{api_id}_{op_id}.py"
        py_path.write_text(code, encoding="utf-8")
        lines = [
            "#!/bin/bash",
            "set +e",
            f"echo 'Mastercard Solution Studio - running snippet for {api_id}'",
            # See the Windows branch for why we scrub these.
            "unset VIRTUAL_ENV PYTHONHOME VIRTUAL_ENV_PROMPT",
            "",
        ]
        for name, val in env_pairs:
            lines.append(f"export {name}={shlex.quote(val)}")
        if packages:
            lines.append("echo 'Installing dependencies...'")
            lines.append(f"python3 -m pip install --user --quiet {' '.join(packages)}")
        lines += ["echo", f"python3 {shlex.quote(str(py_path))}",
                  "echo", "echo 'Press Enter to close...'", "read"]
        sh_path.write_text("\n".join(lines), encoding="utf-8")
        sh_path.chmod(0o755)
        spawned = False
        # Try common terminal emulators in order of likelihood.
        for term, args in [
            ("x-terminal-emulator", ["-e", "bash", str(sh_path)]),
            ("gnome-terminal", ["--", "bash", str(sh_path)]),
            ("konsole", ["-e", "bash", str(sh_path)]),
            ("xterm", ["-e", "bash", str(sh_path)]),
        ]:
            try:
                subprocess.Popen([term, *args], close_fds=True)
                launcher = term
                spawned = True
                break
            except FileNotFoundError:
                continue
        if not spawned:
            return jsonify({
                "error": (
                    "No supported terminal emulator found "
                    "(tried x-terminal-emulator, gnome-terminal, konsole, xterm)."
                ),
                "script": str(sh_path),
            }), 500

    return jsonify({
        "ok": True,
        "launcher": launcher,
        "platform": system,
    })


@app.route("/sdk/run", methods=["POST"])
@_require_not_server_mode
def sdk_run():
    """Write the Open Finance SDK snippet to a temp script and launch the
    host OS's native terminal so the user can watch it install deps and run.

    Mirrors /explorer/<api_id>/run, but for the standalone ofin SDK: it
    pip-installs requests + cryptography, then runs the snippet. The repo's
    cli/ directory is injected onto sys.path (absolute) so the script works
    from the temp dir, and credentials are auto-discovered from config/.env.

    Disabled in server mode — spawning a terminal on the host only ever
    makes sense for the local demo workflow.
    """
    import platform
    import shlex
    import subprocess
    import tempfile
    from pathlib import Path

    project_root = os.path.dirname(os.path.abspath(__file__))
    cli_dir = os.path.join(project_root, "cli")
    packages = ["requests", "cryptography"]

    body = request.get_json(silent=True) or {}
    override_code = body.get("code")
    default_code = (
        "from ofin import OfinClient\n\n"
        "# Credentials auto-loaded from config/.env - one client, three continents\n"
        "client = OfinClient.from_env()\n\n"
        'for region in ("us", "au", "eu"):\n'
        "    res = client.region(region).auth_token(); "
        'print(f"{region}  ->  {res.status}  -  {res.token}")\n'
    )
    snippet = override_code if isinstance(override_code, str) and override_code.strip() else default_code

    # Always inject the absolute cli/ path first so the script imports the
    # ofin SDK regardless of the temp dir it runs from.
    code = (
        "import sys\n"
        f"sys.path.insert(0, {json.dumps(cli_dir)})\n\n"
        + snippet
    )

    system = platform.system().lower()
    tmpdir = Path(tempfile.gettempdir()) / "vima-snippets"
    tmpdir.mkdir(parents=True, exist_ok=True)

    if system == "windows":
        py_path = tmpdir / "ofin_sdk.py"
        ps1_path = tmpdir / "ofin_sdk.ps1"
        py_path.write_text(code, encoding="utf-8")
        lines = [
            "$ErrorActionPreference = 'Continue'",
            "Write-Host 'Mastercard Solution Studio - Open Finance SDK' -ForegroundColor Cyan",
            "Write-Host ''",
            "Remove-Item Env:VIRTUAL_ENV    -ErrorAction SilentlyContinue",
            "Remove-Item Env:PYTHONHOME     -ErrorAction SilentlyContinue",
            "Remove-Item Env:VIRTUAL_ENV_PROMPT -ErrorAction SilentlyContinue",
            "Write-Host 'Installing dependencies...' -ForegroundColor DarkGray",
            f"py -m pip install --user --quiet {' '.join(packages)}",
            "Write-Host ''",
            "py '" + str(py_path).replace("'", "''") + "'",
            "$code = $LASTEXITCODE",
            "Write-Host ''",
            "Write-Host ('Exit code: ' + $code) -ForegroundColor Cyan",
            "Write-Host 'Press Enter to close...' -ForegroundColor DarkGray",
            "Read-Host | Out-Null",
        ]
        ps1_path.write_text("\r\n".join(lines), encoding="utf-8")
        powershell_args = [
            "powershell.exe", "-NoLogo", "-ExecutionPolicy", "Bypass",
            "-File", str(ps1_path),
        ]
        try:
            subprocess.Popen(
                ["wt.exe", "new-tab", "--title", "Mastercard Solution Studio: Open Finance SDK", *powershell_args],
                close_fds=True,
            )
            launcher = "wt"
        except FileNotFoundError:
            subprocess.Popen(
                powershell_args,
                creationflags=getattr(subprocess, "CREATE_NEW_CONSOLE", 0),
                close_fds=True,
            )
            launcher = "powershell"

    elif system == "darwin":
        sh_path = tmpdir / "ofin_sdk.sh"
        py_path = tmpdir / "ofin_sdk.py"
        py_path.write_text(code, encoding="utf-8")
        lines = [
            "#!/bin/bash",
            "set +e",
            "echo 'Mastercard Solution Studio - Open Finance SDK'",
            "unset VIRTUAL_ENV PYTHONHOME VIRTUAL_ENV_PROMPT",
            "echo 'Installing dependencies...'",
            f"python3 -m pip install --user --quiet {' '.join(packages)}",
            "echo",
            f"python3 {shlex.quote(str(py_path))}",
            "echo", "echo 'Press Enter to close...'", "read",
        ]
        sh_path.write_text("\n".join(lines), encoding="utf-8")
        sh_path.chmod(0o755)
        subprocess.Popen(["open", "-a", "Terminal", str(sh_path)], close_fds=True)
        launcher = "Terminal.app"

    else:  # Linux + other POSIX
        sh_path = tmpdir / "ofin_sdk.sh"
        py_path = tmpdir / "ofin_sdk.py"
        py_path.write_text(code, encoding="utf-8")
        lines = [
            "#!/bin/bash",
            "set +e",
            "echo 'Mastercard Solution Studio - Open Finance SDK'",
            "unset VIRTUAL_ENV PYTHONHOME VIRTUAL_ENV_PROMPT",
            "echo 'Installing dependencies...'",
            f"python3 -m pip install --user --quiet {' '.join(packages)}",
            "echo",
            f"python3 {shlex.quote(str(py_path))}",
            "echo", "echo 'Press Enter to close...'", "read",
        ]
        sh_path.write_text("\n".join(lines), encoding="utf-8")
        sh_path.chmod(0o755)
        spawned = False
        for term, args in [
            ("x-terminal-emulator", ["-e", "bash", str(sh_path)]),
            ("gnome-terminal", ["--", "bash", str(sh_path)]),
            ("konsole", ["-e", "bash", str(sh_path)]),
            ("xterm", ["-e", "bash", str(sh_path)]),
        ]:
            try:
                subprocess.Popen([term, *args], close_fds=True)
                launcher = term
                spawned = True
                break
            except FileNotFoundError:
                continue
        if not spawned:
            return jsonify({
                "error": (
                    "No supported terminal emulator found "
                    "(tried x-terminal-emulator, gnome-terminal, konsole, xterm)."
                ),
                "script": str(sh_path),
            }), 500

    return jsonify({
        "ok": True,
        "launcher": launcher,
        "platform": system,
    })


@app.route("/explorer/<api_id>/execute", methods=["POST"])
def explorer_execute(api_id: str):
    # Backward-compatible API aliases (e.g. older pages still posting to
    # /explorer/consent/execute).
    resolved_api_id = "transaction_notifications" if api_id in ("consent", "consent_management") else api_id

    if _is_non_us_blocked_api(resolved_api_id):
        return _non_us_forbidden_response()
    mod = api_registry.get_module(resolved_api_id)
    if mod is None:
        return jsonify({"error": "Unknown API"}), 404
    body = request.get_json(silent=True) or {}
    op_id = body.get("operation")
    params = body.get("params") or {}
    if not op_id:
        return jsonify({"error": "'operation' is required"}), 400
    # Snapshot the call-log watermark so we can backfill request/response below.
    with _api_call_lock:
        seq_before = _api_call_seq
    try:
        result = mod.execute(op_id, params)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    # Capture live responses into the simulator DB (non-simulated calls only)
    if result.get("success") and not is_simulated(resolved_api_id):
        resp_body = (result.get("response") or {}).get("body") or result.get("data")
        try:
            capture_response(resolved_api_id, op_id, resp_body)
        except Exception:
            pass
    # If the API module did not include the 'request' or 'response' envelope
    # that the UI needs to render the panels, backfill from the HTTP-level
    # interceptor log.  This means new APIs don't have to remember to build
    # those dicts themselves — we derive them from the real HTTP exchange.
    # Also backfill headers even when the API provided its own envelope body,
    # so "Show Headers" always works regardless of which API built the envelope.
    with _api_call_lock:
        new_entries = [e for e in _api_call_log if e.get("seq", 0) > seq_before]
    if new_entries:
        first_call = new_entries[-1]
        last_call  = new_entries[0]
        if not result.get("request"):
            result["request"] = {
                "method":  first_call.get("method"),
                "url":     first_call.get("url"),
                "body":    first_call.get("requestBody"),
                "headers": first_call.get("requestHeaders"),
            }
        elif not result["request"].get("headers"):
            result["request"]["headers"] = first_call.get("requestHeaders")
        if not result.get("response"):
            result["response"] = {
                "status_code": last_call.get("status"),
                "body":        last_call.get("responseBody"),
                "headers":     last_call.get("responseHeaders"),
            }
        elif not result["response"].get("headers"):
            result["response"]["headers"] = last_call.get("responseHeaders")
    # Last-resort synthesis: if the executor returned WITHOUT making an HTTP
    # call (e.g. a stub, a validation short-circuit, a not_configured error),
    # the panels would otherwise be empty. Synthesize a minimal envelope from
    # the executor's input/output so the user always sees something — the
    # error message, the stub note, the unknown-operation hint, etc.
    if not result.get("request"):
        result["request"] = {
            "method": "(no HTTP call)",
            "url": f"explorer://{api_id}/{op_id}",
            "body": params,
        }
    if not result.get("response"):
        # Build a synthetic response body from the result minus the envelope
        # keys the UI handles separately.
        synthetic_body = {
            k: v for k, v in result.items()
            if k not in ("request", "response", "state", "state_updates")
        }
        # Derive a plausible status: explicit success → 200, explicit failure
        # markers → 400, otherwise blank.
        if result.get("success") is True or result.get("ok") is True:
            synth_status = 200
        elif (
            result.get("success") is False
            or result.get("ok") is False
            or result.get("error")
        ):
            synth_status = 400
        else:
            synth_status = None
        result["response"] = {
            "status_code": synth_status,
            "body": synthetic_body,
            "synthetic": True,
            "note": (
                "No outbound HTTP call was made — this envelope was synthesized "
                "from the executor return value."
            ),
        }
    # Merge in latest state snapshot for the UI
    result["state"] = getattr(mod, "get_state", lambda: {})()
    return jsonify(result)


# ---------------------------------------------------------------------------
# Live Demo — real Open Finance bank linking across US / AU / EU
# ---------------------------------------------------------------------------
@app.route("/live-demo/state")
def live_demo_state():
    return jsonify(live_demo.get_public_state())


@app.route("/live-demo/enable", methods=["POST"])
def live_demo_enable():
    body = request.get_json(silent=True) or {}
    region = str(body.get("region") or "")
    enabled = bool(body.get("enabled"))
    return jsonify(live_demo.set_enabled(region, enabled))


@app.route("/live-demo/connect", methods=["POST"])
def live_demo_connect():
    body = request.get_json(silent=True) or {}
    region = str(body.get("region") or "")
    return jsonify(live_demo.start_connect(region))


@app.route("/live-demo/poll", methods=["POST"])
def live_demo_poll():
    body = request.get_json(silent=True) or {}
    region = str(body.get("region") or "")
    return jsonify(live_demo.poll_connect(region))


@app.route("/live-demo/refresh", methods=["POST"])
def live_demo_refresh():
    body = request.get_json(silent=True) or {}
    region = str(body.get("region") or "")
    return jsonify(live_demo.refresh(region))


@app.route("/explorer/consent/3ds-flow")
def consent_3ds_flow():
    """Unified 3DS browser flow page.

    Runs the EMV 3DS protocol end-to-end inside the user's browser, matching
    Mastercard's reference implementation:

      1. Fingerprint (hidden iframe POSTs threeDSMethodData to the ACS URL).
         The ACS returns JS that runs in that iframe, collects browser caps,
         posts to /process_browser_attributes, which then posts to Mastercard's
         server-to-server notification URL. When done it sends a postMessage
         (threeds-method-notification) to this page. We also have a 10s timeout.

      2. Start authentication — POST start-authentication with auth.params
         containing fingerprintStatus + browser info (user agent, screen size,
         timezone, etc). Response is one of:
            AUTHENTICATED      — frictionless, done.
            AUTH_IN_PROGRESS   — challenge required, params include acsUrl + encodedCReq.
            AUTH_FAILED        — failure.

      3. Challenge (only if AUTH_IN_PROGRESS) — visible iframe POSTs creq to acsUrl.
         The ACS shows the OTP UI (sandbox OTP: 123456). When the user submits
         and the challenge completes the ACS posts to a CRes notification URL
         which sends a threeds-challenge-notification postMessage to this page.

      4. Verify authentication — POST verify-authentication (empty params) to
         finalise the consent.
    """
    card_ref    = request.args.get("card_ref", "")
    method_url  = request.args.get("method_url", "")
    method_data = request.args.get("method_data", "")
    trans_id    = request.args.get("trans_id", "")
    method_notify = request.args.get("method_notify", "")
    if not card_ref:
        return "Missing card_ref", 400

    import html as _html
    import json as _json
    safe = {
        "card_ref":    _html.escape(card_ref, quote=True),
        "method_url":  _html.escape(method_url, quote=True),
        "method_data": _html.escape(method_data, quote=True),
        "trans_id":    _html.escape(trans_id, quote=True),
        "method_notify": _html.escape(method_notify, quote=True),
    }
    cfg_json = _json.dumps(safe)

    page = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>3DS Authentication — Consent enrollment</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, sans-serif;
           display: flex; flex-direction: column; align-items: center;
           min-height: 100vh; margin: 0; background: #f4f6fa; color: #333; padding: 20px; }
    .card { background: #fff; border-radius: 10px; padding: 32px 40px;
            box-shadow: 0 2px 16px rgba(0,0,0,.1); text-align: center;
            max-width: 560px; width: 100%; margin-top: 40px; }
    h2 { margin: 0 0 8px; font-size: 20px; }
    .step { color: #666; font-size: 13px; margin: 4px 0; }
    .status { font-size: 14px; margin: 12px 0; min-height: 20px; }
    .spinner { width: 32px; height: 32px; border: 3px solid #e0e0e0;
               border-top-color: #005b99; border-radius: 50%;
               animation: spin .8s linear infinite; margin: 16px auto; }
    @keyframes spin { to { transform: rotate(360deg); } }
    .ok   { color: #1a7f4b; font-weight: 600; }
    .err  { color: #b00020; font-weight: 600; }
    pre { text-align: left; background: #f5f5f5; padding: 12px; border-radius: 6px;
          font-size: 12px; overflow: auto; max-height: 240px; }
    #fp-frame  { display: none; }
    #challenge-wrap { display: none; margin-top: 24px; }
    #challenge-frame { width: 600px; max-width: 100%; height: 440px;
                       border: 1px solid #ccc; border-radius: 6px; background: #fff; }
  </style>
</head>
<body>
  <div class="card">
    <h2>3DS Authentication</h2>
    <div class="step" id="step-fp">1. Device fingerprint…</div>
    <div class="step" id="step-sa">2. Start authentication…</div>
    <div class="step" id="step-ch">3. Challenge (if needed)…</div>
    <div class="step" id="step-vf">4. Verify authentication…</div>
    <div class="spinner" id="spinner"></div>
    <div class="status" id="status">Starting…</div>
    <pre id="result" style="display:none"></pre>
  </div>

  <div id="challenge-wrap" class="card">
    <h2>Please complete the challenge</h2>
    <div class="step">Sandbox OTP: <strong>123456</strong></div>
    <iframe id="challenge-frame" name="challenge-frame"></iframe>
  </div>

  <iframe id="fp-frame" name="fp-frame"></iframe>

  <script>
  (function() {
    var CFG = __CFG__;
    var statusEl = document.getElementById('status');
    var resultEl = document.getElementById('result');
    var spinnerEl = document.getElementById('spinner');

    function setStatus(msg, cls) {
      statusEl.textContent = msg;
      statusEl.className = 'status ' + (cls || '');
    }
    function markStep(id, mark) {
      var el = document.getElementById(id);
      if (el) el.textContent = mark + ' ' + el.textContent.replace(/^[✓✗•]\\s*/, '');
    }
    function showJSON(obj) {
      resultEl.style.display = 'block';
      resultEl.textContent = JSON.stringify(obj, null, 2);
    }
    function hideSpinner() { spinnerEl.style.display = 'none'; }

    function post(url, body) {
      return fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      }).then(function(r) { return r.json(); });
    }

    function browserInfo(fpStatus) {
      return {
        fingerprintStatus:   fpStatus,
        challengeWindowSize: '04',
        browserAcceptHeader: 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        browserColorDepth:   String(window.screen.colorDepth),
        browserJavaEnabled:  false,
        browserLanguage:     navigator.language || 'en-US',
        browserScreenHeight: String(window.screen.height),
        browserScreenWidth:  String(window.screen.width),
        browserTZ:           String(new Date().getTimezoneOffset()),
        browserUserAgent:    window.navigator.userAgent,
      };
    }

    // ---- step 1: fingerprint ----
    function doFingerprint() {
      return new Promise(function(resolve) {
        if (!CFG.method_url || !CFG.method_data) {
          markStep('step-fp', '•');
          resolve('unavailable');
          return;
        }
        var done = false;
        function finish(status) {
          if (done) return;
          done = true;
          window.removeEventListener('message', onMsg);
          markStep('step-fp', status === 'complete' ? '✓' : '•');
          resolve(status);
        }
        function onMsg(e) {
          if (e && e.data && e.data.type === 'threeds-method-notification') {
            finish('complete');
          }
        }
        window.addEventListener('message', onMsg);

        // The reference impl writes an HTML doc into the iframe that submits
        // its own form to the ACS URL. We do the same so the iframe controls
        // the navigation; the ACS will later navigate the iframe back to the
        // notification page which posts the message to our window.
        var html =
          '<script>document.addEventListener("DOMContentLoaded",function(){'
          + 'var f=document.createElement("form");f.method="POST";'
          + 'f.action=' + JSON.stringify(CFG.method_url) + ';'
                    + 'if(' + JSON.stringify(CFG.method_notify) + '){'
                    + 'var n=document.createElement("input");n.name="threeDSMethodNotificationURL";'
                    + 'n.value=' + JSON.stringify(CFG.method_notify) + ';f.appendChild(n);}'
          + 'var i=document.createElement("input");i.name="threeDSMethodData";'
          + 'i.value=' + JSON.stringify(CFG.method_data) + ';'
                    + 'if(' + JSON.stringify(CFG.trans_id) + '){'
                    + 'var t=document.createElement("input");t.name="threeDSServerTransID";'
                    + 't.value=' + JSON.stringify(CFG.trans_id) + ';f.appendChild(t);}'
          + 'f.appendChild(i);document.body.appendChild(f);f.submit();'
          + '});<\\/script>';
        var iframe = document.getElementById('fp-frame');
        var doc = iframe.contentWindow.document;
        doc.open(); doc.write('<html><body>' + html + '</body></html>'); doc.close();

        setTimeout(function() { finish('timeout'); }, 10000);
      });
    }

    // ---- step 3: challenge (only if AUTH_IN_PROGRESS) ----
    function doChallenge(acsUrl, creq) {
      return new Promise(function(resolve) {
        document.getElementById('challenge-wrap').style.display = 'block';
        function onMsg(e) {
          if (e && e.data && e.data.type === 'threeds-challenge-notification') {
            window.removeEventListener('message', onMsg);
            markStep('step-ch', '✓');
            resolve();
          }
        }
        window.addEventListener('message', onMsg);

        var html =
          '<script>document.addEventListener("DOMContentLoaded",function(){'
          + 'var f=document.createElement("form");f.method="POST";'
          + 'f.action=' + JSON.stringify(acsUrl) + ';'
          + 'var i=document.createElement("input");i.name="creq";'
          + 'i.value=' + JSON.stringify(creq) + ';'
          + 'f.appendChild(i);document.body.appendChild(f);f.submit();'
          + '});<\\/script>';
        var iframe = document.getElementById('challenge-frame');
        var doc = iframe.contentWindow.document;
        doc.open(); doc.write('<html><body>' + html + '</body></html>'); doc.close();
      });
    }

    // ---- main ----
    function run() {
      setStatus('Running 3DS Method (device fingerprint)…');
      doFingerprint().then(function(fpStatus) {
        setStatus('Calling start-authentication (' + fpStatus + ')…');
        return post('/explorer/transaction_notifications/execute', {
          operation: 'start_authentication',
          params: Object.assign(
            { card_ref: CFG.card_ref, auth_type: 'THREEDS',
              auth_params: JSON.stringify(browserInfo(fpStatus)) },
            {}
          ),
        });
      }).then(function(sa) {
        if (!sa.success) {
          markStep('step-sa', '✗');
          hideSpinner();
          setStatus('start-authentication failed', 'err');
          showJSON(sa.error || sa);
          return;
        }
        markStep('step-sa', '✓');
        var auth   = (sa.data && sa.data.auth) || {};
        var status = auth.status;
        var params = auth.params || {};
        if (status === 'AUTHENTICATED') {
          hideSpinner();
          markStep('step-ch', '•');
          markStep('step-vf', '•');
          setStatus('Frictionless authentication succeeded.', 'ok');
          showJSON(sa.data);
          return;
        }
        if (status === 'AUTH_FAILED') {
          hideSpinner();
          markStep('step-ch', '✗');
          setStatus('Authentication failed.', 'err');
          showJSON(sa.data);
          return;
        }
        if (status !== 'AUTH_IN_PROGRESS') {
          hideSpinner();
          setStatus('Unexpected status: ' + status, 'err');
          showJSON(sa.data);
          return;
        }
        // challenge required
        setStatus('Challenge required — please complete the OTP in the iframe below.');
        var acsUrl = params.acsUrl || params.acsURL;
        var creq   = params.encodedCReq || params.creq;
        return doChallenge(acsUrl, creq).then(function() {
          setStatus('Verifying authentication…');
          return post('/explorer/transaction_notifications/execute', {
            operation: 'verify_authentication',
            params: { card_ref: CFG.card_ref, auth_type: 'THREEDS', auth_params: '{}' },
          });
        }).then(function(vr) {
          document.getElementById('challenge-wrap').style.display = 'none';
          hideSpinner();
          if (vr && vr.success) {
            markStep('step-vf', '✓');
            setStatus('Authentication complete.', 'ok');
            showJSON(vr.data);
          } else {
            markStep('step-vf', '✗');
            setStatus('verify-authentication failed', 'err');
            showJSON((vr && vr.error) || vr);
          }
        });
      }).catch(function(err) {
        hideSpinner();
        setStatus('Error: ' + (err && err.message ? err.message : err), 'err');
      });
    }
    run();
  })();
  </script>
</body>
</html>"""
    page = page.replace("__CFG__", cfg_json)
    return page, 200, {"Content-Type": "text/html; charset=utf-8"}


# ----------------------------------------------------------------------------
# Use cases
# ----------------------------------------------------------------------------

@app.route("/testchat/<path:filename>")
def testchat_files(filename: str):
    """Serve files from the self-contained testchat use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "testchat")
    return _serve_prefixed_static(directory, filename)


@app.route("/sonic/<path:filename>")
def sonic_files(filename: str):
    """Serve files from the self-contained sonic use-case directory."""
    directory = os.path.join(os.path.dirname(__file__), "usecases", "sonic")
    return _serve_prefixed_static(directory, filename)


# ---------------------------------------------------------------------------
# Dynamic per-usecase static-asset routes.
# Every folder under ``usecases/`` containing an ``index.html`` is mounted at
# ``/<folder>/<path:filename>``.  Adding a new usecase only requires creating
# the folder — no edits here.
# ---------------------------------------------------------------------------

def _script_root_prefix() -> str:
    return (request.script_root or "").rstrip("/")


def _prefix_html_routes(html: str) -> str:
    prefix = _script_root_prefix()
    if not prefix:
        return html
    replacements = (
        ('href="/', f'href="{prefix}/'),
        ("href='/", f"href='{prefix}/"),
        ('src="/', f'src="{prefix}/'),
        ("src='/", f"src='{prefix}/"),
        ('action="/', f'action="{prefix}/'),
        ("action='/", f"action='{prefix}/"),
        ('fetch("/', f'fetch("{prefix}/'),
        ("fetch('/", f"fetch('{prefix}/"),
    )
    for old, new in replacements:
        html = html.replace(old, new)
    return html


def _serve_prefixed_static(directory: str, filename: str):
    if filename.lower().endswith('.html'):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            with open(path, encoding='utf-8') as f:
                html = f.read()
            return _prefix_html_routes(html), 200, {"Content-Type": "text/html; charset=utf-8"}
    return send_from_directory(directory, filename)

def _register_usecase_static_routes() -> None:
    usecases_dir = os.path.join(os.path.dirname(__file__), "usecases")
    if not os.path.isdir(usecases_dir):
        return
    for name in sorted(os.listdir(usecases_dir)):
        folder = os.path.join(usecases_dir, name)
        if not os.path.isdir(folder) or name.startswith(("_", ".")):
            continue
        # Skip the special static-route names already mounted explicitly above.
        if name in {"sonic"}:
            continue
        endpoint = f"usecase_files__{name}"

        def _make_view(_dir: str):
            def _view(filename: str):
                return _serve_prefixed_static(_dir, filename)
            return _view

        app.add_url_rule(
            f"/{name}/<path:filename>",
            endpoint=endpoint,
            view_func=_make_view(folder),
        )


_register_usecase_static_routes()


@app.route("/catalog")
def catalog():
    """Unified catalog of all registered APIs, Use Cases and Solutions."""
    apis = api_registry.manifests()
    use_cases = usecase_registry.manifests()
    solutions = api_registry.solutions()
    return jsonify({
        "apis": [
            {
                "id": a["id"],
                "name": a["name"],
                "configured": a.get("configured", False),
                "categories": a.get("categories", []),
                "operations": [op["id"] for op in a.get("operations", [])],
                "complements": a.get("complements", []),
                "requires": a.get("requires", []),
                "bundles": a.get("bundles", []),
            }
            for a in apis
        ],
        "use_cases": [
            {
                "id": u["id"],
                "name": u["name"],
                "apis": u.get("apis", []),
                "render": u.get("render", ""),
            }
            for u in use_cases
        ],
        "solutions": solutions,
        "summary": {
            "total_apis": len(apis),
            "configured_apis": sum(1 for a in apis if a.get("configured")),
            "total_use_cases": len(use_cases),
            "total_solutions": len(solutions),
        },
    })


@app.route("/catalog/bundles")
def catalog_bundles():
    """Return solution-shaped bundles enriched with per-bundle status.

    See :func:`apis.registry.solutions` for the response shape. Drives the
    Solutions sidebar section in the explorer and feeds the chat agent's
    "what should I add next?" recommendations.
    """
    return jsonify({"bundles": api_registry.solutions()})


@app.route("/usecases")
def usecases_list():
    return jsonify({"use_cases": usecase_registry.manifests()})


@app.route("/usecases/<uc_id>/data")
def usecase_data(uc_id: str):
    if _is_non_us_blocked_usecase(uc_id):
        return _non_us_forbidden_response()
    mod = usecase_registry.get_module(uc_id)
    if mod is None:
        return jsonify({"error": "Unknown use case"}), 404
    # Use cases that expose a no-arg data fetcher (e.g. enrichment static data)
    if hasattr(mod, "get_enrichment_data"):
        try:
            return jsonify(mod.get_enrichment_data())
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    if not hasattr(mod, "get_data"):
        return jsonify({"error": "Unknown use case"}), 404
    # Resolve customer_id: explicit query param wins, else fall back to Open Finance's active state.
    customer_id = request.args.get("customer_id")
    if not customer_id:
        ofin_mod = api_registry.get_module("open_finance")
        if ofin_mod is not None:
            state = getattr(ofin_mod, "get_state", lambda: {})()
            customer_id = state.get("customer_id")
    # Use cases can opt out of the customer-required gate (curated/offline demos)
    # by exposing ``REQUIRES_CUSTOMER = False`` at module level.
    requires_customer = getattr(mod, "REQUIRES_CUSTOMER", True)
    if not customer_id and requires_customer:
        return jsonify({"error": "No customer linked. Use the Open Finance tab "
                                 "to create or select a customer first."}), 400
    try:
        return jsonify(mod.get_data(customer_id or ""))
    except Exception as e:  # pragma: no cover
        return jsonify({"error": str(e)}), 500


@app.route("/usecases/<uc_id>/action", methods=["POST"])
def usecase_action(uc_id: str):
    if _is_non_us_blocked_usecase(uc_id):
        return _non_us_forbidden_response()
    mod = usecase_registry.get_module(uc_id)
    if mod is None or not hasattr(mod, "do_action"):
        return jsonify({"error": "Unknown action"}), 404
    body = request.get_json(silent=True) or {}
    action = body.get("action")
    params = body.get("params") or {}
    if not action:
        return jsonify({"error": "'action' is required"}), 400
    try:
        result = mod.do_action(action, params)
        # If the use case produced a customer_id, propagate it to Open Finance STATE
        # so it becomes the global default for all APIs and use cases.
        cid = result.get("customer_id") if isinstance(result, dict) else None
        if cid and not result.get("error"):
            ofin_mod = api_registry.get_module("open_finance")
            if ofin_mod is not None and hasattr(ofin_mod, "STATE"):
                ofin_mod.STATE["customer_id"] = str(cid)
                if result.get("username") and not ofin_mod.STATE.get("customer_username"):
                    ofin_mod.STATE["customer_username"] = result["username"]
        return jsonify(result)
    except Exception as e:  # pragma: no cover
        return jsonify({"error": str(e)}), 500


# ----------------------------------------------------------------------------
# TxPush listener  (use as callback URL with ngrok)
# ----------------------------------------------------------------------------

@app.route("/txpush-listener", methods=["GET", "POST"])
def txpush_listener():
    """Receive TxPush notifications from Finicity and store them."""
    if request.method == "GET":
        code = request.args.get("txpush_verification_code", "")
        return code, 200, {"Content-Type": "text/plain"}
    import datetime
    payload = request.get_json(silent=True) or request.get_data(as_text=True)
    _txpush_events.appendleft({
        "received_at": datetime.datetime.utcnow().isoformat() + "Z",
        "payload": payload,
    })
    return "", 200


@app.route("/txpush-events")
def txpush_events():
    """Return the last received TxPush events (for the UI to poll)."""
    return jsonify({"events": list(_txpush_events)})


# ----------------------------------------------------------------------------
# Transaction Notifications webhook receiver
# ----------------------------------------------------------------------------

@app.route("/txnotify/webhook", methods=["GET", "POST"])
def txnotify_webhook():
    """Receive Mastercard transaction notifications forwarded via ngrok.

    GET  — health-check used by Mastercard during webhook registration.
    POST — the actual notification payload; stored in the txnotify inbox
           so the live-demo use-case UI can pick it up via polling.
    """
    if request.method == "GET":
        return jsonify({"ok": True, "endpoint": "Transaction Notifications webhook receiver"})
    payload = request.get_json(silent=True) or {}
    mod = usecase_registry.get_module("txnotify")
    if mod and hasattr(mod, "receive_webhook"):
        mod.receive_webhook(payload)
    return "", 200


@app.route("/txnotify/launch-ngrok", methods=["POST"])
@_require_not_server_mode
def txnotify_launch_ngrok():
    """Open a native terminal running: ngrok http <port>

    Points ngrok at this Solution Studio instance so Mastercard can POST
    transaction notifications to /txnotify/webhook via the tunnel URL.
    """
    import platform
    import subprocess
    import tempfile
    from pathlib import Path

    system = platform.system().lower()
    port = int(os.environ.get("PORT", "9021"))
    webhook_path = "/txnotify/webhook"
    tmpdir = Path(tempfile.gettempdir()) / "vima-snippets"
    tmpdir.mkdir(parents=True, exist_ok=True)

    if system == "windows":
        ps1_path = tmpdir / "txnotify_ngrok.ps1"
        lines = [
            "$ErrorActionPreference = 'Continue'",
            "Write-Host 'Mastercard Solution Studio — ngrok webhook tunnel' -ForegroundColor Cyan",
            "Write-Host ''",
            f"Write-Host 'Exposing port {port}  →  public HTTPS URL' -ForegroundColor DarkGray",
            f"Write-Host 'After it starts, copy the Forwarding HTTPS URL and append: {webhook_path}' -ForegroundColor Yellow",
            "Write-Host ''",
            f"ngrok http {port}",
            "Write-Host ''",
            "Write-Host 'ngrok exited. Press Enter to close...' -ForegroundColor DarkGray",
            "Read-Host | Out-Null",
        ]
        ps1_path.write_text("\r\n".join(lines), encoding="utf-8")
        powershell_args = [
            "powershell.exe", "-NoLogo", "-ExecutionPolicy", "Bypass",
            "-File", str(ps1_path),
        ]
        try:
            subprocess.Popen(
                ["wt.exe", "new-tab", "--title", "ngrok — Transaction Notifications", *powershell_args],
                close_fds=True,
            )
            launcher = "wt"
        except FileNotFoundError:
            subprocess.Popen(
                powershell_args,
                creationflags=getattr(subprocess, "CREATE_NEW_CONSOLE", 0),
                close_fds=True,
            )
            launcher = "powershell"

    elif system == "darwin":
        sh_path = tmpdir / "txnotify_ngrok.sh"
        lines = [
            "#!/bin/bash",
            "set +e",
            "echo 'Mastercard Solution Studio — ngrok webhook tunnel'",
            f"echo 'After it starts, copy the Forwarding URL and append: {webhook_path}'",
            "echo ''",
            f"ngrok http {port}",
            "echo ''",
            "echo 'Press Enter to close...'",
            "read",
        ]
        sh_path.write_text("\n".join(lines), encoding="utf-8")
        sh_path.chmod(0o755)
        subprocess.Popen(["open", "-a", "Terminal", str(sh_path)], close_fds=True)
        launcher = "Terminal.app"

    else:  # Linux / other POSIX
        sh_path = tmpdir / "txnotify_ngrok.sh"
        lines = [
            "#!/bin/bash",
            "set +e",
            "echo 'Mastercard Solution Studio — ngrok webhook tunnel'",
            f"echo 'After it starts, copy the Forwarding URL and append: {webhook_path}'",
            "echo ''",
            f"ngrok http {port}",
            "echo ''",
            "echo 'Press Enter to close...'",
            "read",
        ]
        sh_path.write_text("\n".join(lines), encoding="utf-8")
        sh_path.chmod(0o755)
        spawned = False
        for term, args in [
            ("x-terminal-emulator", ["-e", "bash", str(sh_path)]),
            ("gnome-terminal",      ["--", "bash", str(sh_path)]),
            ("konsole",             ["-e", "bash", str(sh_path)]),
            ("xterm",               ["-e", "bash", str(sh_path)]),
        ]:
            try:
                subprocess.Popen([term, *args], close_fds=True)
                launcher = term
                spawned = True
                break
            except FileNotFoundError:
                continue
        if not spawned:
            return jsonify({"error": "No terminal emulator found"}), 500

    return jsonify({"ok": True, "launcher": launcher, "platform": system})


# ----------------------------------------------------------------------------
# BIN Lookup — server-side SQLite FTS5 BIN ranges cache
# ----------------------------------------------------------------------------
import sqlite3 as _sqlite3

_BIN_CACHE = {"status": "idle", "count": 0, "loaded_at": None, "error": None, "persisted": False}
_BIN_CACHE_LOCK = threading.Lock()
_BIN_DB_CONN = None  # sqlite3 connection (disk-backed, persists across restarts)
_BIN_DB_PATH = os.path.join(os.path.dirname(__file__), "data", "bin_ranges.db")
_BIN_DB_TMP  = _BIN_DB_PATH + ".tmp"


def _bin_try_load_from_disk():
    """Called at startup: open the persisted disk DB if it exists."""
    global _BIN_DB_CONN
    if not os.path.exists(_BIN_DB_PATH):
        return
    try:
        conn = _sqlite3.connect(_BIN_DB_PATH, check_same_thread=False)
        conn.row_factory = _sqlite3.Row
        meta = conn.execute("SELECT count, loaded_at FROM meta LIMIT 1").fetchone()
        if not meta:
            conn.close()
            return
        actual = conn.execute("SELECT COUNT(*) FROM bin_ranges").fetchone()[0]
        if actual == 0:
            conn.close()
            return
        with _BIN_CACHE_LOCK:
            _BIN_DB_CONN = conn
            _BIN_CACHE["count"] = actual
            _BIN_CACHE["loaded_at"] = meta["loaded_at"]
            _BIN_CACHE["status"] = "loaded"
            _BIN_CACHE["persisted"] = True
            _BIN_CACHE["error"] = None
    except Exception:
        pass  # corrupt / incompatible DB — user can reload via UI


def _bin_build_sqlite(rows):
    """Build a disk-backed SQLite database with FTS5 index and persist it."""
    import shutil
    os.makedirs(os.path.dirname(_BIN_DB_PATH), exist_ok=True)
    # Write to a temp file first so a crash mid-build doesn't corrupt the live DB
    if os.path.exists(_BIN_DB_TMP):
        os.remove(_BIN_DB_TMP)
    conn = _sqlite3.connect(_BIN_DB_TMP, check_same_thread=False)
    conn.row_factory = _sqlite3.Row
    conn.execute("""CREATE TABLE meta (count INTEGER, loaded_at INTEGER)""")
    conn.execute("""
        CREATE TABLE bin_ranges (
            binNum TEXT, lowAccountRange TEXT, highAccountRange TEXT,
            binLength TEXT, acceptanceBrand TEXT, ica TEXT, customerName TEXT,
            smartDataEnabled TEXT, countryCode TEXT, countryAlpha3 TEXT, countryName TEXT,
            localUse TEXT, authorizationOnly TEXT, productCode TEXT, productDescription TEXT,
            governmentRange TEXT, nonReloadableIndicator TEXT, anonymousPrepaidIndicator TEXT,
            cardholderCurrencyIndicator TEXT, billingCurrencyDefault TEXT,
            comboCardIndicator TEXT, flexCardIndicator TEXT, fasterFundsIndicator TEXT,
            moneySendIndicator TEXT, gamblingBlockEnabled TEXT, programName TEXT,
            vertical TEXT, fundingSource TEXT, consumerType TEXT,
            affiliate TEXT, paymentAccountType TEXT, mastercardOneParticipationIndicator TEXT
        )
    """)
    conn.execute("CREATE INDEX idx_bin ON bin_ranges(binNum)")
    conn.execute("CREATE INDEX idx_low ON bin_ranges(lowAccountRange)")
    # FTS5 content table — fast full-text search on text columns
    conn.execute("""
        CREATE VIRTUAL TABLE bin_fts USING fts5(
            customerName, productDescription, countryName, acceptanceBrand, programName, vertical,
            content='bin_ranges', content_rowid='rowid', tokenize='unicode61'
        )
    """)

    records = []
    for row in rows:
        c = row.get("country", {})
        if isinstance(c, dict):
            cc, ca3, cn = str(c.get("code", "")), str(c.get("alpha3", "")), str(c.get("name", ""))
        else:
            cc, ca3, cn = "", "", str(c)
        records.append((
            str(row.get("binNum", "")), str(row.get("lowAccountRange", "")),
            str(row.get("highAccountRange", "")), str(row.get("binLength", "")),
            str(row.get("acceptanceBrand", "")), str(row.get("ica", "")),
            str(row.get("customerName", "")), str(row.get("smartDataEnabled", "")),
            cc, ca3, cn,
            str(row.get("localUse", "")), str(row.get("authorizationOnly", "")),
            str(row.get("productCode", "")), str(row.get("productDescription", "")),
            str(row.get("governmentRange", "")), str(row.get("nonReloadableIndicator", "")),
            str(row.get("anonymousPrepaidIndicator", "")),
            str(row.get("cardholderCurrencyIndicator", "")), str(row.get("billingCurrencyDefault", "")),
            str(row.get("comboCardIndicator", "")), str(row.get("flexCardIndicator", "")),
            str(row.get("fasterFundsIndicator", "")), str(row.get("moneySendIndicator", "")),
            str(row.get("gamblingBlockEnabled", "")), str(row.get("programName", "")),
            str(row.get("vertical", "")), str(row.get("fundingSource", "")),
            str(row.get("consumerType", "")), str(row.get("affiliate", "")),
            str(row.get("paymentAccountType", "")),
            str(row.get("mastercardOneParticipationIndicator", "")),
        ))

    conn.executemany(
        "INSERT INTO bin_ranges VALUES (" + ",".join(["?"] * 32) + ")",  # nosec B608 — values via ? params
        records,
    )
    conn.execute("INSERT INTO bin_fts(bin_fts) VALUES('rebuild')")
    conn.execute("INSERT INTO meta VALUES (?, ?)", (len(records), int(time.time())))
    conn.commit()
    conn.close()
    # Atomically replace the live DB file
    shutil.move(_BIN_DB_TMP, _BIN_DB_PATH)
    # Re-open a persistent connection to the final path
    final_conn = _sqlite3.connect(_BIN_DB_PATH, check_same_thread=False)
    final_conn.row_factory = _sqlite3.Row
    return final_conn


def _bin_row_to_dict(r):
    return {
        "binNum": r["binNum"], "lowAccountRange": r["lowAccountRange"],
        "highAccountRange": r["highAccountRange"], "binLength": r["binLength"],
        "acceptanceBrand": r["acceptanceBrand"], "ica": r["ica"],
        "customerName": r["customerName"], "smartDataEnabled": r["smartDataEnabled"],
        "country": {"code": r["countryCode"], "alpha3": r["countryAlpha3"], "name": r["countryName"]},
        "localUse": r["localUse"], "authorizationOnly": r["authorizationOnly"],
        "productCode": r["productCode"], "productDescription": r["productDescription"],
        "governmentRange": r["governmentRange"], "nonReloadableIndicator": r["nonReloadableIndicator"],
        "anonymousPrepaidIndicator": r["anonymousPrepaidIndicator"],
        "cardholderCurrencyIndicator": r["cardholderCurrencyIndicator"],
        "billingCurrencyDefault": r["billingCurrencyDefault"],
        "comboCardIndicator": r["comboCardIndicator"], "flexCardIndicator": r["flexCardIndicator"],
        "fasterFundsIndicator": r["fasterFundsIndicator"], "moneySendIndicator": r["moneySendIndicator"],
        "gamblingBlockEnabled": r["gamblingBlockEnabled"], "programName": r["programName"],
        "vertical": r["vertical"], "fundingSource": r["fundingSource"],
        "consumerType": r["consumerType"], "affiliate": r["affiliate"],
        "paymentAccountType": r["paymentAccountType"],
        "mastercardOneParticipationIndicator": r["mastercardOneParticipationIndicator"],
    }


def _bin_cache_do_load():
    """Background thread: fetch all BIN range pages and load into SQLite."""
    global _BIN_DB_CONN
    import ast

    import oauth1.authenticationutils as authutils
    import requests as _req
    from oauth1.oauth import OAuth

    consumer_key = os.environ.get("BIN_LOOKUP_CONSUMER_KEY", "")
    key_path = os.environ.get("BIN_LOOKUP_SIGNING_KEY_PATH", "")
    key_password = os.environ.get("BIN_LOOKUP_SIGNING_KEY_PASSWORD", "keystorepassword")
    env = os.environ.get("BIN_LOOKUP_ENV", "sandbox").lower()
    base_url = (
        "https://api.mastercard.com/bin-resources"
        if env == "production"
        else "https://sandbox.api.mastercard.com/bin-resources"
    )

    if not os.path.isabs(key_path):
        key_path = os.path.join(os.path.dirname(__file__), key_path)

    try:
        signing_key = authutils.load_signing_key(key_path, key_password)
    except Exception as e:
        with _BIN_CACHE_LOCK:
            _BIN_CACHE["status"] = "error"
            _BIN_CACHE["error"] = f"Could not load signing key: {e}"
        return

    rows = []
    page = 1
    total_pages = None
    try:
        while total_pages is None or page <= total_pages:
            url = f"{base_url}/bin-ranges?page={page}&size=10000"
            body_str = "[]"
            auth_header = OAuth.get_authorization_header(url, "POST", body_str, consumer_key, signing_key)
            headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": auth_header}
            resp = _req.post(url, data=body_str, headers=headers, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            items = data.get("items", [])
            total_pages = data.get("totalPages", 1)
            for item in items:
                c = item.get("country", "")
                if isinstance(c, str) and c.startswith("{"):
                    try:
                        item["country"] = ast.literal_eval(c)
                    except Exception:
                        pass
            rows.extend(items)
            page += 1
    except Exception as e:
        with _BIN_CACHE_LOCK:
            _BIN_CACHE["status"] = "error"
            _BIN_CACHE["error"] = str(e)
        return

    try:
        db_conn = _bin_build_sqlite(rows)
    except Exception as e:
        with _BIN_CACHE_LOCK:
            _BIN_CACHE["status"] = "error"
            _BIN_CACHE["error"] = f"SQLite build failed: {e}"
        return

    with _BIN_CACHE_LOCK:
        old_conn = _BIN_DB_CONN
        _BIN_DB_CONN = db_conn
        _BIN_CACHE["count"] = len(rows)
        _BIN_CACHE["status"] = "loaded"
        _BIN_CACHE["loaded_at"] = int(time.time())
        _BIN_CACHE["persisted"] = True
        _BIN_CACHE["error"] = None
    if old_conn is not None:
        try:
            old_conn.close()
        except Exception:
            pass


@app.route("/usecases/bin_lookup/bin-ranges/status")
def binlookup_bin_ranges_status():
    with _BIN_CACHE_LOCK:
        return jsonify({
            "status": _BIN_CACHE["status"],
            "count": _BIN_CACHE["count"],
            "loaded_at": _BIN_CACHE["loaded_at"],
            "error": _BIN_CACHE["error"],
            "persisted": _BIN_CACHE["persisted"],
        })


@app.route("/usecases/bin_lookup/bin-ranges/load", methods=["POST"])
def binlookup_bin_ranges_load():
    with _BIN_CACHE_LOCK:
        if _BIN_CACHE["status"] == "loading":
            return jsonify({"ok": False, "message": "Already loading"})
        _BIN_CACHE["status"] = "loading"
        _BIN_CACHE["error"] = None
    t = threading.Thread(target=_bin_cache_do_load, daemon=True)
    t.start()
    return jsonify({"ok": True, "message": "Loading started"})


@app.route("/usecases/bin_lookup/bin-ranges/search")
def binlookup_bin_ranges_search():
    q = request.args.get("q", "").strip()
    per_page = 50
    page = max(1, int(request.args.get("page", 1)))
    offset = (page - 1) * per_page

    with _BIN_CACHE_LOCK:
        status = _BIN_CACHE["status"]
        conn = _BIN_DB_CONN

    if status != "loaded" or conn is None:
        return jsonify({"error": "BIN ranges not loaded", "results": [], "total": 0, "pages": 0, "page": 1})
    if not q:
        return jsonify({"results": [], "total": 0, "pages": 0, "page": 1})

    # Detect quoted exact-issuer mode: query starts and ends with " or '
    _exact_match = None
    if (q.startswith('"') and q.endswith('"') and len(q) > 2) or \
       (q.startswith("'") and q.endswith("'") and len(q) > 2):
        _exact_match = q[1:-1].strip()

    is_numeric = q.isdigit()
    try:
        if _exact_match is not None:
            # Exact case-insensitive match on customerName (issuer)
            total = conn.execute(
                "SELECT COUNT(*) FROM bin_ranges WHERE customerName = ? COLLATE NOCASE",
                (_exact_match,),
            ).fetchone()[0]
            cur = conn.execute(
                "SELECT * FROM bin_ranges WHERE customerName = ? COLLATE NOCASE ORDER BY binNum LIMIT ? OFFSET ?",
                (_exact_match, per_page, offset),
            )
        elif is_numeric:
            total = conn.execute(
                "SELECT COUNT(*) FROM bin_ranges WHERE binNum LIKE ? OR lowAccountRange LIKE ?",
                (q + "%", q + "%"),
            ).fetchone()[0]
            cur = conn.execute(
                "SELECT * FROM bin_ranges WHERE binNum LIKE ? OR lowAccountRange LIKE ? LIMIT ? OFFSET ?",
                (q + "%", q + "%", per_page, offset),
            )
        else:
            tokens = [t for t in q.replace('"', "").replace("'", "").replace("(", "").replace(")", "").split() if t]
            if not tokens:
                return jsonify({"results": [], "total": 0, "pages": 0, "page": 1})
            fts_q = " ".join(f'"{t}"*' for t in tokens)
            total = conn.execute(
                "SELECT COUNT(*) FROM bin_fts WHERE bin_fts MATCH ?",
                (fts_q,),
            ).fetchone()[0]
            cur = conn.execute(
                """SELECT bin_ranges.* FROM bin_fts
                   JOIN bin_ranges ON bin_fts.rowid = bin_ranges.rowid
                   WHERE bin_fts MATCH ?
                   ORDER BY rank LIMIT ? OFFSET ?""",
                (fts_q, per_page, offset),
            )
        results = [_bin_row_to_dict(r) for r in cur.fetchall()]
        import math
        pages = math.ceil(total / per_page) if total else 0
        return jsonify({"results": results, "total": total, "page": page, "pages": pages})
    except Exception as e:
        return jsonify({"error": str(e), "results": [], "total": 0, "pages": 0, "page": 1})


# BIN Lookup — download all BIN ranges as CSV
# ----------------------------------------------------------------------------

@app.route("/usecases/bin_lookup/download-bins")
def binlookup_download_bins():
    """Stream all BIN ranges from the Mastercard BIN Resource API as a CSV."""
    import csv
    import io

    import oauth1.authenticationutils as authutils
    import requests as _req
    from flask import Response, stream_with_context
    from oauth1.oauth import OAuth

    consumer_key = os.environ.get("BIN_LOOKUP_CONSUMER_KEY", "")
    key_path = os.environ.get("BIN_LOOKUP_SIGNING_KEY_PATH", "")
    key_password = os.environ.get("BIN_LOOKUP_SIGNING_KEY_PASSWORD", "keystorepassword")
    env = os.environ.get("BIN_LOOKUP_ENV", "sandbox").lower()
    base_url = "https://api.mastercard.com/bin-resources" if env == "production" else "https://sandbox.api.mastercard.com/bin-resources"

    if not consumer_key or consumer_key == "your-consumer-key-here" or not key_path:
        return jsonify({"error": "BIN Lookup is not configured."}), 400

    if not os.path.isabs(key_path):
        key_path = os.path.join(os.path.dirname(__file__), key_path)

    try:
        signing_key = authutils.load_signing_key(key_path, key_password)
    except Exception as e:
        return jsonify({"error": f"Could not load signing key: {e}"}), 500

    def generate():
        output = io.StringIO()
        writer = None
        page = 1
        total_pages = None

        while total_pages is None or page <= total_pages:
            url = f"{base_url}/bin-ranges?page={page}&size=10000"
            body_str = "[]"
            try:
                auth_header = OAuth.get_authorization_header(url, "POST", body_str, consumer_key, signing_key)
                headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": auth_header}
                resp = _req.post(url, data=body_str, headers=headers, timeout=30)
                resp.raise_for_status()
                data = resp.json()
            except Exception as e:
                yield f"# Error on page {page}: {e}\n"
                break

            items = data.get("items", [])
            total_pages = data.get("totalPages", 1)

            for item in items:
                if writer is None:
                    writer = csv.DictWriter(output, fieldnames=list(item.keys()), extrasaction="ignore")
                    writer.writeheader()
                    yield output.getvalue()
                    output.seek(0); output.truncate(0)  # noqa: E702
                writer.writerow(item)
                yield output.getvalue()
                output.seek(0); output.truncate(0)  # noqa: E702

            page += 1

    return Response(
        stream_with_context(generate()),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=bin_ranges.csv"},
    )


@app.route("/usecases/findacard/health")
def findacard_health():
    """Check whether the Find A Card service is reachable on localhost:5432."""
    import socket
    try:
        sock = socket.create_connection(("127.0.0.1", 5432), timeout=1)
        sock.close()
        # If request came through a reverse proxy, the browser must reach fac
        # via an absolute URL so path-rewriting patches don't corrupt it.
        # fac lives at nginx-level /fac, outside the /vima/ proxy.
        proto = request.headers.get("X-Forwarded-Proto", "")
        host = request.headers.get("X-Forwarded-Host") or request.headers.get("Host", "")
        if proto and host:
            url = f"{proto}://{host}/fac"
        else:
            url = "http://localhost:5432"
        return jsonify({"online": True, "url": url})
    except (TimeoutError, ConnectionRefusedError, OSError):
        return jsonify({"online": False, "url": "http://localhost:5432"})


@app.route("/api-call-log")
def api_call_log():
    """Return the last outbound API calls captured by the request logger."""
    since = request.args.get("since", type=int, default=0)
    with _api_call_lock:
        entries = [e for e in _api_call_log if e.get("seq", 0) > since]
    return jsonify({"calls": list(reversed(entries))})


# ----------------------------------------------------------------------------
# Config management
# ----------------------------------------------------------------------------

_ENV_PATH = os.path.join(_CONFIG_DIR, ".env")
_KEYS_DIR = os.path.join(_CONFIG_DIR, "keys")


def _build_config_schema() -> list[dict]:
    """Build the Settings UI schema dynamically from ``apis.catalog``.

    Each catalog entry produces one group with the appropriate set of fields
    for its auth scheme (OAuth 1.0a, OAuth 1.0a + client-encryption, OAuth 2.0).
    Adding a new API to the catalog automatically surfaces it in Settings.
    """
    from apis.catalog import (
        AUTH_JWT_RS256,
        AUTH_OAUTH1,
        AUTH_OAUTH1_ENC,
        AUTH_OAUTH2,
        iter_ordered,
    )

    groups: list[dict] = []
    for entry in iter_ordered():
        # consent_management is merged into transaction_notifications —
        # its credentials are shown under the TxNotify group instead.
        if entry.id == "consent_management":
            continue
        p = entry.env_prefix
        fields: list[dict] = []
        if entry.auth in (AUTH_OAUTH1, AUTH_OAUTH1_ENC):
            fields = [
                {"key": f"{p}_CONSUMER_KEY",        "label": "Consumer Key",     "type": "password", "info": f"OAuth 1.0a Consumer Key. Create a project on developer.mastercard.com, add the {entry.display_name} API, and copy the Consumer Key."},
                {"key": f"{p}_SIGNING_KEY_PATH",     "label": "Signing Key File", "type": "file",     "info": "PKCS12 (.p12) signing key file. Click 'Generate signing keys' in your Mastercard Developers project to download it."},
                {"key": f"{p}_SIGNING_KEY_ALIAS",    "label": "Key Alias",        "type": "text",     "info": "Alias for the private key within the .p12 file. Shown when generating keys on Mastercard Developers."},
                {"key": f"{p}_SIGNING_KEY_PASSWORD", "label": "Key Password",     "type": "password", "info": "Password protecting the .p12 key file. The default is 'keystorepassword'."},
                {"key": f"{p}_ENV",                  "label": "Environment",      "type": "text",     "info": "API environment: 'sandbox' or 'production'."},
            ]
            if entry.auth == AUTH_OAUTH1_ENC:
                fields.append(
                    {"key": f"{p}_ENCRYPTION_KEY_PATH", "label": "Client Encryption Key", "type": "file", "info": "Client encryption .pem file. Download from your Mastercard Developers project under 'Client Encryption Keys → Actions → Download'."}
                )
        elif entry.auth == AUTH_OAUTH2:
            fields = [
                {"key": f"{p}_PARTNER_ID",     "label": "Partner ID",     "type": "text",     "info": f"{entry.display_name} Partner ID from your Mastercard Developers project credentials."},
                {"key": f"{p}_PARTNER_SECRET", "label": "Partner Secret", "type": "password", "info": "Partner Secret paired with the Partner ID. Keep this confidential."},
                {"key": f"{p}_APP_KEY",        "label": "App Key",        "type": "password", "info": "Application key for your project, alongside the Partner ID in the portal."},
                {"key": f"{p}_API_BASE_URL",   "label": "API Base URL",   "type": "text",     "info": "Base URL for the API. Use https://api.finicity.com for production or the sandbox URL for testing."},
                {"key": f"{p}_SIG_KEY_PATH",   "label": "Signature Verification Key", "type": "file", "info": "Optional public key (.pem) used to verify webhook signatures from the platform."},
            ]
        elif entry.auth == AUTH_JWT_RS256:
            # Mastercard Open Finance Europe (Aiia) — OAuth 2.0 client_credentials
            # with an RS256-signed JWT client assertion. Manual onboarding only:
            # generate an RSA-4096 keypair, email the public PEM to
            # openbankingeu_support@mastercard.com, then paste the returned
            # clientId below.
            fields = [
                {"key": f"{p}_CLIENT_ID",        "label": "Client ID",        "type": "text",     "info": f"{entry.display_name} clientId issued by Mastercard's EU onboarding officer after they add your public RSA cert to the sandbox trust list. UUID format."},
                {"key": f"{p}_APPLICATION_ID",   "label": "Application ID",   "type": "text",     "info": f"{entry.display_name} applicationId. Sent on every consent / data call as the X-Application-Id header. Issued by the EU onboarding officer alongside the clientId. UUID format."},
                {"key": f"{p}_USE_CASE_ID",      "label": "Use Case Configuration ID", "type": "text", "info": "useCaseConfigurationId provisioned by Mastercard onboarding. Sent as the request body field `useCaseConfigurationId` on Create Consent. UUID format."},
                {"key": f"{p}_REDIRECT_URL",     "label": "Redirect URL",     "type": "text",     "info": "Whitelisted return URL for the hosted Aiia Flow. Pre-configured on the use-case configuration by Mastercard onboarding (not sent per request). Example: https://httpbun.com/any/*"},
                {"key": f"{p}_PRIVATE_KEY_PATH", "label": "Private Key File", "type": "file",     "info": "RSA private key (.key / .pem). Generate locally with: openssl req -x509 -sha256 -nodes -newkey rsa:4096 -keyout private.key -days 730 -out public.pem"},
                {"key": f"{p}_PUBLIC_CERT_PATH", "label": "Public Certificate", "type": "file",    "info": "Public X.509 certificate (.pem) matching the private key. Email this file to openbankingeu_support@mastercard.com to be added to the trust list — the JWT kid is its SHA-256 thumbprint."},
                {"key": f"{p}_AUTH_BASE_URL",    "label": "Auth Base URL",    "type": "text",     "info": "OAuth token endpoint host. Sandbox: https://mtf.auth.openbanking.mastercard.eu"},
                {"key": f"{p}_API_BASE_URL",     "label": "API Base URL",     "type": "text",     "info": "Open Finance API host. Sandbox: https://mtf.api.openbanking.mastercard.eu"},
            ]
        groups.append({
            "id": entry.id,
            "title": entry.display_name,
            "subtitle": f"Mastercard {entry.display_name} API",
            "docs_url": entry.docs_url,
            "fields": fields,
        })

    # Mastercard Developer portal login — required for automated provisioning.
    groups.insert(0, {
        "id": "mastercard_portal",
        "title": "Mastercard Developer Portal",
        "subtitle": "Login credentials for automated API key provisioning",
        "docs_url": "https://developer.mastercard.com/account/log-in",
        "fields": [
            {"key": "MCD_PORTAL_EMAIL",    "label": "Portal Email",    "type": "text",
             "info": "Your Mastercard Developer account email (e.g. you@company.com). Used to log in to developer.mastercard.com and provision API keys automatically."},
            {"key": "MCD_PORTAL_PASSWORD", "label": "Portal Password", "type": "password",
             "info": "Your Mastercard Developer account password. Stored locally in config/.env and never sent anywhere except the Mastercard login page."},
        ],
    })

    # Non-API tools shown in the same Settings UI but excluded from export.
    groups.append({
        "id": "claude_chat",
        "title": "Claude Chat",
        "subtitle": "Anthropic Claude API for the embedded coding assistant",
        "docs_url": "https://console.anthropic.com/",
        "exclude_export": True,
        "fields": [
            {"key": "ANTHROPIC_API_KEY", "label": "API Key", "type": "password",
             "info": "Your Anthropic API key. Sign up at console.anthropic.com, go to Settings → API Keys, and create a new key. Keys start with 'sk-ant-'."},
        ],
    })

    return groups


_CONFIG_SCHEMA = _build_config_schema()


def _read_env_values() -> dict:
    """Parse .env file, return {KEY: value} preserving raw values."""
    result: dict = {}
    try:
        with open(_ENV_PATH, encoding="utf-8") as fh:
            for line in fh:
                s = line.strip()
                if s and not s.startswith("#") and "=" in s:
                    key, _, val = s.partition("=")
                    result[key.strip()] = val.strip()
    except OSError:
        pass
    return result


def _write_env_values(updates: dict) -> None:
    """Write updated key=value pairs into .env, preserving comments and order."""
    try:
        with open(_ENV_PATH, encoding="utf-8") as fh:
            lines = fh.readlines()
    except OSError:
        lines = []

    written: set = set()
    new_lines = []
    for line in lines:
        s = line.strip()
        if s and not s.startswith("#") and "=" in s:
            key, _, _ = s.partition("=")
            key = key.strip()
            if key in updates:
                new_lines.append(f"{key}={updates[key]}\n")
                written.add(key)
                continue
        new_lines.append(line)

    # Section headers to prepend when adding a key for the first time
    _SECTION_HEADERS = {
        "ANTHROPIC_API_KEY": "\n# CLAUDE / VIMA CHAT\n",
    }
    for key, val in updates.items():
        if key not in written:
            if key in _SECTION_HEADERS:
                new_lines.append(_SECTION_HEADERS[key])
            new_lines.append(f"{key}={val}\n")

    _atomic_write_text(_ENV_PATH, "".join(new_lines))


@app.route("/config", methods=["GET"])
@_require_not_server_mode
def config_get():
    env = _read_env_values()
    groups = []
    for g in _CONFIG_SCHEMA:
        fields = []
        for f in g["fields"]:
            fields.append({
                "key":   f["key"],
                "label": f["label"],
                "type":  f["type"],
                "info":  f["info"],
                "value": env.get(f["key"], ""),
            })
        groups.append({
            "id":       g["id"],
            "title":    g["title"],
            "subtitle": g["subtitle"],
            "docs_url": g["docs_url"],
            "fields":   fields,
        })
    resp = jsonify({"groups": groups})
    resp.headers["Cache-Control"] = "no-store"
    return resp


@app.route("/config", methods=["POST"])
@_require_not_server_mode
def config_save_route():
    body = request.get_json(silent=True) or {}
    updates = body.get("updates") or {}
    if not isinstance(updates, dict):
        return jsonify({"error": "updates must be an object"}), 400
    # Whitelist: only keys declared in the schema are accepted
    allowed = {f["key"] for g in _CONFIG_SCHEMA for f in g["fields"]}
    filtered = {k: str(v) for k, v in updates.items() if k in allowed}
    try:
        _write_env_values(filtered)
    except OSError as exc:
        return jsonify({"error": str(exc)}), 500
    load_dotenv(_ENV_PATH, override=True)
    return jsonify({"saved": list(filtered.keys())})


@app.route("/config/export", methods=["GET"])
@_require_not_server_mode
def config_export():
    """Export config/.env + all referenced keystore material as a zip.

    Bundles the redacted .env, every file already under config/keys/, and any
    keystore file referenced by a ``*_KEY_PATH`` entry in .env (which may live
    at the project root). Referenced paths are rewritten to
    ``config/keys/<name>`` so the bundle is self-contained and imports cleanly
    on another machine.
    """
    import io
    import re as _re
    import zipfile

    _base_dir = os.path.dirname(os.path.abspath(__file__))

    env_text = ""
    if os.path.isfile(_ENV_PATH):
        with open(_ENV_PATH, encoding="utf-8") as fh:
            env_text = fh.read()

    # Collect keystore files referenced by *_KEY_PATH entries and rewrite the
    # paths to a canonical config/keys/<name> location inside the bundle.
    added_keys: dict[str, str] = {}  # source abspath -> zip basename

    def _rewrite_key_path(match):
        key = match.group(1)
        raw_val = match.group(2).strip().strip('"').strip("'")
        if not raw_val:
            return match.group(0)
        candidate = raw_val if os.path.isabs(raw_val) else os.path.join(_base_dir, raw_val)
        if os.path.isfile(candidate):
            base = os.path.basename(raw_val)
            added_keys[os.path.abspath(candidate)] = base
            return f"{key}=config/keys/{base}"
        return match.group(0)

    env_text = _re.sub(
        r"(?m)^([A-Z0-9_]*_KEY_PATH)\s*=\s*(.*)$", _rewrite_key_path, env_text
    )

    # .env — redact ANTHROPIC_API_KEY
    env_text = _re.sub(
        r"(?m)^(ANTHROPIC_API_KEY\s*=\s*).*$",
        r"\1YOUR_ANTHROPIC_API_KEY_HERE",
        env_text,
    )

    buf = io.BytesIO()
    written_entries: set[str] = set()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        if env_text:
            zf.writestr("config/.env", env_text)
        # all key files already under config/keys/ — always use forward slashes
        # in zip entries (cross-platform)
        if os.path.isdir(_KEYS_DIR):
            for fname in os.listdir(_KEYS_DIR):
                fpath = os.path.join(_KEYS_DIR, fname)
                if os.path.isfile(fpath):
                    entry = "config/keys/" + fname
                    zf.write(fpath, entry)
                    written_entries.add(entry)
        # keystore files referenced by .env that live outside config/keys/
        for src, base in added_keys.items():
            entry = "config/keys/" + base
            if entry in written_entries:
                continue
            zf.write(src, entry)
            written_entries.add(entry)

    buf.seek(0)
    from flask import send_file
    return send_file(
        buf,
        mimetype="application/zip",
        as_attachment=True,
        download_name="vima-config.zip",
    )


def _merge_env_text(existing_text: str, new_text: str) -> str:
    """Merge two .env file texts into a canonical, catalog-ordered layout.

    Values from ``new_text`` take precedence for keys that appear in both.
    Keys that only exist in ``existing_text`` are preserved so previously
    configured APIs are not wiped when provisioning a subset.

    The output is always re-rendered in catalog order with a short header
    for each API and a blank line between API blocks. Each env var is
    matched to the catalog entry with the **longest** matching prefix —
    e.g. ``OPEN_FINANCE_AU_PARTNER_ID`` is assigned to ``OPEN_FINANCE_AU``
    rather than the shorter ``OPEN_FINANCE`` prefix it also starts with.
    Keys that don't belong to any catalogued API (e.g. ``ANTHROPIC_API_KEY``)
    are emitted in a trailing ``# Other`` block, also one variable per line.
    """
    import re as _re

    from apis.catalog import iter_ordered

    _KEY_RE = _re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)=(.*)$")

    def _extract(text: str) -> dict[str, str]:
        out: dict[str, str] = {}
        for raw_line in text.splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            m = _KEY_RE.match(line)
            if m:
                out[m.group(1)] = m.group(2)
        return out

    # New wins where both define the same key; otherwise preserve old.
    merged: dict[str, str] = {**_extract(existing_text), **_extract(new_text)}

    # Build display order + a longest-first prefix list so that
    # OPEN_FINANCE_AU_* is captured by OPEN_FINANCE_AU, not OPEN_FINANCE.
    entries = list(iter_ordered())
    prefix_to_entry = {entry.env_prefix: entry for entry in entries}
    prefixes_longest_first = sorted(prefix_to_entry, key=len, reverse=True)
    display_order = [entry.env_prefix for entry in entries]

    def _match_prefix(key: str) -> str | None:
        for p in prefixes_longest_first:
            if key == p or key.startswith(p + "_"):
                return p
        return None

    grouped: dict[str, list[str]] = {p: [] for p in display_order}
    other_keys: list[str] = []
    for k in sorted(merged):
        p = _match_prefix(k)
        if p is None:
            other_keys.append(k)
        else:
            grouped[p].append(k)

    lines: list[str] = ["# Generated by vima — do not hand-edit lightly.", ""]
    for prefix in display_order:
        keys = grouped.get(prefix) or []
        if not keys:
            continue
        lines.append(f"# {prefix_to_entry[prefix].display_name}")
        for k in keys:
            lines.append(f"{k}={merged[k]}")
        lines.append("")

    if other_keys:
        lines.append("# Other")
        for k in other_keys:
            lines.append(f"{k}={merged[k]}")
        lines.append("")

    # Collapse any accidental trailing blank lines down to exactly one newline.
    while len(lines) >= 2 and lines[-1] == "" and lines[-2] == "":
        lines.pop()
    return "\n".join(lines)


def _atomic_write_text(path: str, text: str) -> None:
    """Write ``text`` to ``path`` atomically.

    Writes to a sibling temp file in the same directory, fsyncs it, then
    os.replace()s it over the target. This guarantees readers either see
    the previous fully-written file or the new fully-written file — never
    a truncated/partial state if the process is killed mid-write
    (e.g. user cancels provisioning).
    """
    import tempfile
    parent = os.path.dirname(os.path.abspath(path)) or "."
    os.makedirs(parent, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(
        prefix=".env.", suffix=".tmp", dir=parent,
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
            fh.flush()
            try:
                os.fsync(fh.fileno())
            except OSError:
                pass
        os.replace(tmp_path, path)
    except Exception:
        try:
            os.remove(tmp_path)
        except OSError:
            pass
        raise


def _atomic_write_bytes(path: str, data: bytes) -> None:
    """Binary counterpart of ``_atomic_write_text`` for key files."""
    import tempfile
    parent = os.path.dirname(os.path.abspath(path)) or "."
    os.makedirs(parent, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(
        prefix=os.path.basename(path) + ".", suffix=".tmp", dir=parent,
    )
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
            fh.flush()
            try:
                os.fsync(fh.fileno())
            except OSError:
                pass
        os.replace(tmp_path, path)
    except Exception:
        try:
            os.remove(tmp_path)
        except OSError:
            pass
        raise


@app.route("/config/import", methods=["POST"])
@_require_not_server_mode
def config_import():
    """Import a vima-config.zip or upload_bundle_xxx.zip — merges into existing .env."""
    import importlib.util as _ilu
    import io as _io
    import tempfile
    import zipfile
    from pathlib import Path as _Path

    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    fobj = request.files["file"]
    try:
        data = fobj.read()
        with zipfile.ZipFile(_io.BytesIO(data)) as zf:
            names = zf.namelist()
            norm_names = {n: n.replace("\\", "/") for n in names}
            norm_set = set(norm_names.values())

            # ----------------------------------------------------------------
            # Detect upload_bundle_xxx format: has manifest.json + certs/ dir
            # ----------------------------------------------------------------
            is_bundle_format = (
                any(v == "manifest.json" for v in norm_set) and
                any(v.startswith("certs/") for v in norm_set)
            )

            if is_bundle_format:
                # Extract certs/* to a temp directory so export_vima_config.py
                # can process them (it expects the same normalized-dir layout)
                with tempfile.TemporaryDirectory() as _tmp:
                    norm_dir = _Path(_tmp) / "normalized"
                    norm_dir.mkdir()
                    for orig, name in norm_names.items():
                        if name.startswith("certs/") and not name.endswith("/"):
                            fname = name.split("/", 1)[-1]
                            if fname:
                                with open(norm_dir / fname, "wb") as fh:
                                    fh.write(zf.read(orig))

                    # Determine keystore password: reuse any existing value in .env
                    _password = "foobar!!"
                    if os.path.isfile(_ENV_PATH):
                        import re as _re
                        _env_text = open(_ENV_PATH, encoding="utf-8").read()
                        _m = _re.search(r"_SIGNING_KEY_PASSWORD=(.+)", _env_text)
                        if _m:
                            _password = _m.group(1).strip()

                    # Convert to vima-config.zip using export_vima_config.py
                    _tool_dir = os.path.join(os.path.dirname(__file__),
                                             "tools", "mcd-key-automation")
                    _ec_file = os.path.join(_tool_dir, "export_vima_config.py")
                    _spec = _ilu.spec_from_file_location("export_vima_config", _ec_file)
                    _mod = _ilu.module_from_spec(_spec)
                    _spec.loader.exec_module(_mod)

                    _out_zip = _Path(_tmp) / "vima-config.zip"
                    _mod.build_vima_config_zip(norm_dir, _password, _out_zip)
                    data = _out_zip.read_bytes()

            # ----------------------------------------------------------------
            # Import vima-config layout (config/.env + config/keys/*)
            # ----------------------------------------------------------------
            with zipfile.ZipFile(_io.BytesIO(data)) as zf2:
                names2 = zf2.namelist()
                norm2 = {n: n.replace("\\", "/") for n in names2}

                valid_entries = [v for v in norm2.values()
                                 if v.startswith("config/.env") or v.startswith("config/keys/")]
                if not valid_entries:
                    return jsonify({"error": "Zip does not contain a valid vima config layout"}), 400

                os.makedirs(_KEYS_DIR, exist_ok=True)
                imported = []
                for orig, name in norm2.items():
                    if name == "config/.env":
                        new_env_text = zf2.read(orig).decode("utf-8")
                        if os.path.isfile(_ENV_PATH):
                            existing = open(_ENV_PATH, encoding="utf-8").read()
                            env_text = _merge_env_text(existing, new_env_text)
                        else:
                            env_text = new_env_text
                        _atomic_write_text(_ENV_PATH, env_text)
                        load_dotenv(_ENV_PATH, override=True)
                        imported.append(".env")
                    elif name.startswith("config/keys/") and not name.endswith("/"):
                        fname = name.split("/")[-1]
                        if not fname:
                            continue
                        ext = os.path.splitext(fname)[1].lower()
                        if ext not in (".p12", ".pkcs12", ".pem", ".key"):
                            continue
                        dest = os.path.join(_KEYS_DIR, fname)
                        _atomic_write_bytes(dest, zf2.read(orig))
                        imported.append("config/keys/" + fname)

        return jsonify({"imported": imported})
    except zipfile.BadZipFile:
        return jsonify({"error": "Not a valid zip file"}), 400
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/config/upload-key", methods=["POST"])
@_require_not_server_mode
def config_upload_key():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    fobj = request.files["file"]
    fname = (fobj.filename or "").strip()
    if not fname:
        return jsonify({"error": "Empty filename"}), 400
    ext = os.path.splitext(fname)[1].lower()
    if ext not in (".p12", ".pkcs12", ".pem", ".key"):
        return jsonify({"error": "Only .p12, .pkcs12, .pem, or .key files are accepted"}), 400
    # Use only basename to prevent path traversal
    safe_name = os.path.basename(fname)
    os.makedirs(_KEYS_DIR, exist_ok=True)
    save_path = os.path.join(_KEYS_DIR, safe_name)
    fobj.save(save_path)
    # Always use forward slashes — works on Windows, Mac, and Linux
    rel_path = "config/keys/" + safe_name
    return jsonify({"filename": safe_name, "path": rel_path})


# ----------------------------------------------------------------------------
# Auto-provision endpoints
# ----------------------------------------------------------------------------

@app.route("/config/purge", methods=["POST"])
@_require_not_server_mode
def config_purge():
    """Remove all provisioned keys and .env files, then clear matching env vars from memory."""
    import shutil
    removed = []

    # Clear key files
    if os.path.isdir(_KEYS_DIR):
        shutil.rmtree(_KEYS_DIR)
        os.makedirs(_KEYS_DIR, exist_ok=True)
        removed.append("keys")

    # Remove .env and any stale .env.TEMP
    for env_file in [_ENV_PATH, _ENV_PATH + ".TEMP"]:
        if os.path.isfile(env_file):
            os.remove(env_file)
            removed.append(os.path.basename(env_file))

    # Clear all credential-related env vars from the running process
    prefixes_to_clear = [
        "BIN_LOOKUP_", "PLACES_", "EASY_SAVINGS_", "CONSUMER_CLARITY_",
        "PRICELESS_CITIES_", "TRANSACTION_NOTIFICATIONS_", "CONSENT_MANAGEMENT_",
        "OFFERS_FOR_PUBLISHERS_", "OFFERS_MERCHANT_CONTENT_", "BENEFITS_ELIGIBILITY_",
        "BENEFITS_CONTENT_ELIGIBILITY_", "OPEN_FINANCE_",
        # Legacy prefixes
        "BINLOOKUP_", "CLARITY_", "EASYSAVINGS_", "PRICELESS_", "TXNOTIFY_",
        "CONSENT_", "OFPUB_", "OFMC_", "ELIGIBILITY_", "BCES_", "OFIN_",
    ]
    cleared = []
    for key in list(os.environ.keys()):
        if any(key.startswith(p) for p in prefixes_to_clear):
            del os.environ[key]
            cleared.append(key)

    return jsonify({"removed": removed, "env_vars_cleared": len(cleared)})


_provision_jobs: dict = {}


def _tool_setup_command() -> str:
    """Return the user-facing command that prepares the key automation tool."""
    return "run.bat" if os.name == "nt" else "./run.sh"


def _provisioner_python(tool_dir: str) -> str:
    """Return the platform-specific key automation venv Python path."""
    if os.name == "nt":
        return os.path.join(tool_dir, ".venv", "Scripts", "python.exe")
    return os.path.join(tool_dir, ".venv", "bin", "python")


def _provisioner_setup_error(tool_dir: str) -> str | None:
    """Return a setup error if the key automation tool is missing/incomplete."""
    python_bin = _provisioner_python(tool_dir)
    setup_cmd = _tool_setup_command()
    if not os.path.isfile(python_bin):
        return (
            "Mastercard key automation is not set up. "
            f"Run `{setup_cmd}` from the repo root, then try provisioning again."
        )

    main_path = os.path.join(tool_dir, "app", "main.py")
    if not os.path.isfile(main_path):
        return (
            "Mastercard key automation files are missing. "
            f"Run `{setup_cmd}` from the repo root, then try provisioning again."
        )

    try:
        subprocess.run(
            [
                python_bin,
                "-c",
                "import cryptography, loguru, playwright, typer, yaml",
            ],
            cwd=tool_dir,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=10,
            check=True,
        )
    except Exception:
        return (
            "Mastercard key automation dependencies are incomplete. "
            f"Run `{setup_cmd}` from the repo root so the tool venv can be repaired, "
            "then try provisioning again."
        )
    return None


def _build_provision_catalog() -> list[dict]:
    """Return canonical API metadata for the auto-provisioning UI."""
    from apis.catalog import DISABLED_API_IDS, iter_ordered

    apis = api_registry.manifests()
    by_id = {a.get("id"): a for a in apis}
    catalog: list[dict] = []
    for entry in iter_ordered():
        api_id = entry.id
        if api_id in DISABLED_API_IDS:
            continue
        api = by_id.get(api_id, {})
        note = entry.provision_note or ""
        # consent_management is provisioned as part of the Transaction
        # Notifications project — surface a note on the TxNotify entry.
        if api_id == "transaction_notifications":
            note = (
                (note + " " if note else "") +
                "Consent Management is automatically added to this project — "
                "both APIs share the same signing key."
            )
        catalog.append({
            "id": api_id,
            "legacy_id": entry.legacy_id,
            "name": api.get("name") or entry.display_name,
            "configured": bool(api.get("configured")),
            "docs_url": entry.docs_url,
            "requires_owner_approval": bool(note),
            "provision_note": note,
            "auto_provisionable": bool(entry.auto_provisionable) and api_id != "consent_management",
            "manual_onboarding_url": entry.manual_onboarding_url or "",
            "disabled_in_non_us": _is_non_us_blocked_api(api_id),
            "disabled_reason": _NON_US_DISABLED_HINT if _is_non_us_blocked_api(api_id) else "",
        })
    return catalog


@app.route("/provision/catalog")
@_require_not_server_mode
def provision_catalog():
    """Return canonical API metadata used by the auto-provisioning modal."""
    resp = jsonify({"apis": _build_provision_catalog()})
    resp.headers["Cache-Control"] = "no-store"
    return resp


@app.route("/provision/status")
@_require_not_server_mode
def provision_status():
    has_env = os.path.isfile(_ENV_PATH)
    apis = api_registry.manifests()
    configured = sum(1 for a in apis if a.get("configured"))
    needs_setup = not has_env or configured == 0
    resp = jsonify({"needs_setup": needs_setup, "configured": configured, "total": len(apis), "apis": apis})
    resp.headers["Cache-Control"] = "no-store"
    return resp


@app.route("/provision/start", methods=["POST"])
@_require_not_server_mode
def provision_start():
    body = request.get_json(silent=True) or {}
    selected_apis = body.get("apis", [])
    password = body.get("password", "foobar!!")
    if not selected_apis:
        return jsonify({"error": "No APIs selected"}), 400
    if _non_us_mode_enabled() and _OPEN_FINANCE_US_API_ID in selected_apis:
        return _non_us_forbidden_response()

    # Allow the caller (e.g. tests/run.py in a clean run) to override the tool
    # directory so the cloned temp server can use the original repo's .venv
    # rather than failing because the clone doesn't have a .venv installed.
    _default_tool_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools", "mcd-key-automation")
    override_tool_dir = (body.get("tool_dir") or "").strip()
    if override_tool_dir and os.path.isdir(override_tool_dir):
        tool_dir = os.path.normpath(os.path.abspath(override_tool_dir))
    else:
        tool_dir = _default_tool_dir

    setup_error = _provisioner_setup_error(tool_dir)
    if setup_error:
        return jsonify({"error": setup_error, "setup_required": True}), 503
    python_bin = _provisioner_python(tool_dir)

    # transaction_notifications and consent_management must live in the
    # same Mastercard project so they share one signing key.
    # Build projects, merging consent_management into txnotify's project.
    project_lines: list[str] = []
    for api in selected_apis:
        if api == "consent_management":
            continue  # handled by transaction_notifications entry below
        if api == "transaction_notifications":
            project_lines.append(
                f"  - name: {api}\n    apis: [{api}, consent_management]"
            )
        else:
            project_lines.append(f"  - name: {api}\n    apis: [{api}]")
    projects_yaml = "\n".join(project_lines)
    project_prefix = body.get("project_prefix", "SS")
    cfg_text = f"""environment: sandbox
organization: mastercard
login_url: https://developer.mastercard.com/account/log-in
dashboard_url_pattern: "**/dashboard**"
key_password: "{password}"
project_prefix: "{project_prefix}"
projects:
{projects_yaml}
"""
    import tempfile
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(cfg_text)
        cfg_path = f.name

    job_id = str(uuid.uuid4())[:8]
    q = queue.Queue()
    _provision_jobs[job_id] = {"queue": q, "done": False, "proc": None}

    # Remove any stale zip so we only import a zip produced by this run
    zip_path = os.path.join(tool_dir, "output", "vima-config.zip")
    try:
        os.remove(zip_path)
    except OSError:
        pass

    cmd = [python_bin, "-m", "app.main", "run", "-c", cfg_path]

    def _import_from_zip() -> tuple[bool, str]:
        """Import the current vima-config.zip into config/.env + config/keys/.

        Returns (ok, message). Safe to call repeatedly — each invocation
        re-merges the .env (idempotent for unchanged entries) and overwrites
        key files for any APIs newly added to the zip.
        """
        if not os.path.isfile(zip_path):
            return False, "no zip yet"
        try:
            import io as _io
            import zipfile
            with open(zip_path, "rb") as zf_file:
                data = zf_file.read()
            updated_apis: set[str] = set()
            with zipfile.ZipFile(_io.BytesIO(data)) as zf:
                names = zf.namelist()
                norm = {n: n.replace("\\", "/") for n in names}
                os.makedirs(_KEYS_DIR, exist_ok=True)
                for orig, name in norm.items():
                    if name == "config/.env":
                        new_env_text = zf.read(orig).decode("utf-8")
                        if os.path.isfile(_ENV_PATH):
                            existing = open(_ENV_PATH, encoding="utf-8").read()
                            env_text = _merge_env_text(existing, new_env_text)
                        else:
                            env_text = _merge_env_text("", new_env_text)
                        _atomic_write_text(_ENV_PATH, env_text)
                        load_dotenv(_ENV_PATH, override=True)
                    elif name.startswith("config/keys/") and not name.endswith("/"):
                        fname = name.split("/")[-1]
                        ext = os.path.splitext(fname)[1].lower()
                        if ext in (".p12", ".pkcs12", ".pem", ".key"):
                            dest = os.path.join(_KEYS_DIR, fname)
                            _atomic_write_bytes(dest, zf.read(orig))
                            updated_apis.add(os.path.splitext(fname)[0])
            return True, ", ".join(sorted(updated_apis)) or "ok"
        except Exception as exc:
            return False, str(exc)

    def _run():
        rc = None
        launched = False
        try:
            proc = subprocess.Popen(
                cmd,
                cwd=tool_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
            launched = True
            _provision_jobs[job_id]["proc"] = proc
            for line in proc.stdout:
                stripped = line.rstrip()
                # The orchestrator emits this marker after each successful
                # API so we can update config/.env + config/keys/
                # incrementally rather than waiting for the whole run.
                if stripped == "__VIMA_ZIP_READY__":
                    ok, info = _import_from_zip()
                    if ok:
                        q.put(f"💾  Updated .env (apis on disk: {info})")
                    else:
                        q.put(f"⚠️  Incremental .env update skipped: {info}")
                    continue
                # The provisioner learned a working strategy that differs
                # from the declared one — surface it so the user can promote
                # it into providers/mastercard/api_config.py.
                if stripped.startswith("__VIMA_LEARNED__"):
                    q.put(f"🧠  Learned: {stripped[len('__VIMA_LEARNED__ '):]} "
                          f"(see tools/mcd-key-automation/learned/ to promote)")
                    continue
                # All provisioning strategies failed — surface the report
                # path so the user can open the JSON and the screenshot.
                if stripped.startswith("__VIMA_PROVISION_REPORT__"):
                    q.put(f"📄  Failure report written: "
                          f"{stripped[len('__VIMA_PROVISION_REPORT__ '):]}")
                    continue
                q.put(stripped)
            proc.wait()
            rc = proc.returncode
        except Exception as exc:
            q.put(f"ERROR launching provisioner: {exc}")

        if rc is not None and rc != 0:
            q.put(f"ERROR: provisioner exited with code {rc}")

        # If the provisioner subprocess didn't produce a zip (e.g. build_vima_config_zip
        # raised a non-fatal exception inside the subprocess), fall back to building it
        # directly from the Flask process so we still get a .env on Windows.
        if launched and not os.path.isfile(zip_path):
            q.put("ℹ️  vima-config.zip not produced by provisioner — attempting direct build…")
            try:
                import importlib.util as _ilu
                from pathlib import Path as _Path
                _ec_file = os.path.join(tool_dir, "export_vima_config.py")
                _spec = _ilu.spec_from_file_location("export_vima_config", _ec_file)
                _mod = _ilu.module_from_spec(_spec)
                _spec.loader.exec_module(_mod)
                _norm_dir = _Path(tool_dir) / "temp" / "normalized"
                os.makedirs(os.path.join(tool_dir, "output"), exist_ok=True)
                _result = _mod.build_vima_config_zip(_norm_dir, password, _Path(zip_path))
                _included = len(_result.get("apis", []))
                _skipped = _result.get("skipped", [])
                q.put(f"Direct build: {_included} API(s) included" + (f", skipped: {_skipped}" if _skipped else ""))
                if _included == 0:
                    try:
                        os.remove(zip_path)
                    except OSError:
                        pass
                    q.put("__PROVISION_FAILED__:No credentials were collected. Run the key automation setup with "
                          f"`{_tool_setup_command()}`, then try provisioning again.")
            except Exception as _fb_exc:
                q.put(f"Direct build also failed: {_fb_exc}")
                q.put(f"__PROVISION_FAILED__:Could not build vima-config.zip: {_fb_exc}")
        elif not launched:
            q.put("__PROVISION_FAILED__:Provisioner could not be launched.")

        # Final reconciliation — idempotent. Catches anything the
        # incremental imports missed (e.g. OAuth2 / OFin credentials that
        # only finalize at the very end).
        if os.path.isfile(zip_path):
            ok, info = _import_from_zip()
            if ok:
                q.put("__IMPORT_COMPLETE__")
            else:
                q.put(f"__IMPORT_ERROR__: {info}")
        else:
            q.put("__NO_ZIP__")

        _provision_jobs[job_id]["done"] = True
        q.put(None)

    t = threading.Thread(target=_run, daemon=True)
    t.start()
    return jsonify({"job_id": job_id})


@app.route("/provision/stream/<job_id>")
@_require_not_server_mode
def provision_stream(job_id):
    job = _provision_jobs.get(job_id)
    if not job:
        return jsonify({"error": "Unknown job"}), 404

    _SENTINELS = {"__DONE__", "__IMPORT_COMPLETE__", "__NO_ZIP__"}

    def generate():
        q = job["queue"]
        while True:
            try:
                line = q.get(timeout=60)
            except queue.Empty:
                yield "data: \n\n"
                continue
            if line is None:
                yield "data: __DONE__\n\n"
                yield ": end\n\n"  # flush keepalive so __DONE__ clears browser buffer
                break
            # Send sentinel control strings raw; JSON-encode all other log lines
            if (
                line in _SENTINELS
                or (isinstance(line, str) and line.startswith("__IMPORT_ERROR__"))
                or (isinstance(line, str) and line.startswith("__PROVISION_FAILED__:"))
            ):
                yield f"data: {line}\n\n"
            else:
                yield f"data: {json.dumps(line)}\n\n"

    return app.response_class(
        generate(),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


if __name__ == "__main__":
    _bin_try_load_from_disk()
    port = _RUNTIME_FLAGS.port
    host = _RUNTIME_FLAGS.host
    apis = api_registry.manifests()
    print("\n" + "=" * 60)
    print("Solution Studio")
    print("=" * 60)
    for a in apis:
        flag = "+" if a.get("configured") else "-"
        print(f"  {flag} {a['name']:<20} ({len(a['operations'])} operations)")
    if _server_mode_enabled() or _non_us_mode_enabled():
        print("\nRuntime mode:")
        print(f"  - server mode: {'ON' if _server_mode_enabled() else 'OFF'}")
        print(f"  - non-us mode: {'ON' if _non_us_mode_enabled() else 'OFF'}")
    print(f"\nListening on http://{host}:{port}")
    print("=" * 60 + "\n")
    app.run(host=host, port=port, debug=True, use_reloader=False)  # nosec B201 — local dev server only
