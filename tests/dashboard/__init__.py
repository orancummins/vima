"""tests/dashboard/__init__.py — Flask Blueprint for the Vima test results dashboard.

Mounted at /vima/test by app.py.

Routes:
  GET  /vima/test/            — paginated table of all test runs
  GET  /vima/test/<run_id>    — detail view for a single run
  GET  /vima/test/config      — email / SMTP settings
  POST /vima/test/config      — save settings (or send test email)
"""
from __future__ import annotations

import math
import os
from flask import Blueprint, render_template, request, redirect, url_for, jsonify

from tests.dashboard.db import (
    init_db,
    count_runs,
    list_runs,
    get_run,
    get_run_results,
    get_stats,
)
from tests.dashboard.mailer import load_config, save_config, send_test_email

_PAGE_SIZE = 10

test_bp = Blueprint(
    "test_dashboard",
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "templates"),
    url_prefix="/vima/test",
)


@test_bp.before_request
def _ensure_db():
    init_db()


# ── List view ──────────────────────────────────────────────────────────────────

@test_bp.route("/", methods=["GET"])
@test_bp.route("", methods=["GET"])
def run_list():
    page = max(1, int(request.args.get("page", 1)))
    total = count_runs()
    total_pages = max(1, math.ceil(total / _PAGE_SIZE))
    page = min(page, total_pages)
    runs = list_runs(page=page, page_size=_PAGE_SIZE)
    return render_template(
        "test_runs.html",
        runs=runs,
        page=page,
        total_pages=total_pages,
        total=total,
        page_size=_PAGE_SIZE,
    )


# ── History fragment (AJAX refresh) ───────────────────────────────────────────

@test_bp.route("/history_fragment", methods=["GET"])
def history_fragment():
    """Returns just the inner HTML of the history section for client-side refresh."""
    page = max(1, int(request.args.get("page", 1)))
    total = count_runs()
    total_pages = max(1, math.ceil(total / _PAGE_SIZE))
    page = min(page, total_pages)
    runs = list_runs(page=page, page_size=_PAGE_SIZE)
    return render_template(
        "_history_fragment.html",
        runs=runs,
        page=page,
        total_pages=total_pages,
        total=total,
        page_size=_PAGE_SIZE,
    )


# ── Detail view ────────────────────────────────────────────────────────────────

@test_bp.route("/<int:run_id>", methods=["GET"])
def run_detail(run_id: int):
    run = get_run(run_id)
    if run is None:
        return render_template(
            "test_runs.html",
            runs=[],
            page=1,
            total_pages=1,
            total=0,
            error=f"Run #{run_id} not found.",
        ), 404
    results = get_run_results(run_id)
    # Group by suite; convert sqlite3.Row → plain dict so tojson works in templates
    suites: dict = {}
    for r in results:
        s = r["suite"]
        if s not in suites:
            suites[s] = []
        suites[s].append(dict(r))
    run = dict(run)
    return render_template("test_run.html", run=run, suites=suites)


# ── Stats view ────────────────────────────────────────────────────────────────

@test_bp.route("/stats", methods=["GET"])
def stats():
    data = get_stats()
    return render_template("test_stats.html", stats=data)


# ── Config view ────────────────────────────────────────────────────────────────

@test_bp.route("/config", methods=["GET", "POST"])
def config():
    cfg = load_config()
    saved = False
    test_result = None

    if request.method == "POST":
        action = request.form.get("action", "save")
        section = request.form.get("section", "email")

        if section == "portal":
            # Portal credentials form — merge into existing config
            existing = load_config()
            existing["portal_email"] = request.form.get("portal_email", "").strip()
            existing["portal_sso"]   = "1" if request.form.get("portal_sso") else "0"
            existing["key_password"] = request.form.get("key_password", "foobar!!").strip() or "foobar!!"
            existing["test_port"]    = request.form.get("test_port", "9022").strip()
            save_config(existing)
            cfg = existing
            saved = True
        else:
            new_cfg = {
                **load_config(),  # preserve portal section
                "smtp_host":     request.form.get("smtp_host", "").strip(),
                "smtp_port":     request.form.get("smtp_port", "587").strip(),
                "smtp_user":     request.form.get("smtp_user", "").strip(),
                "smtp_password": request.form.get("smtp_password", "").strip(),
                "from_address":  request.form.get("from_address", "").strip(),
                "to_addresses":  request.form.get("to_addresses", "").strip(),
                "use_tls":       "1" if request.form.get("use_tls") else "0",
            }
            save_config(new_cfg)
            cfg = new_cfg

            if action == "test_email":
                ok, msg = send_test_email(new_cfg)
                test_result = (ok, msg)
            else:
                saved = True

    return render_template("test_config.html", cfg=cfg, saved=saved, test_result=test_result)


# Trigger a test run from the dashboard (best-effort background launch)
@test_bp.route("/run", methods=["POST"])
def run_trigger():
    import subprocess
    import sys
    from flask import jsonify

    cwd = os.getcwd()
    is_windows = sys.platform == "win32"

    # scope: 'smoke' | 'full' | 'clean'
    # smoke/full use --existing (safe — never touches keys or portal).
    # clean uses --clean: clones repo, starts a fresh server on a SEPARATE
    # port (test_port from settings, default 9022), provisions SST-* keys
    # into that isolated server, runs tests, then cleans up portal projects
    # and the temp dir.  The running app on port 9021 is never touched.
    # If portal_email isn't configured, falls back to --skip-provision so
    # the button still works safely without credentials.
    scope = request.form.get("scope", "smoke")

    if scope == "lint":
        # Lint is server-independent: no install type, no provisioning, no port.
        # Pass --lint --no-server --existing so run.py takes the lint-only path.
        install_flag    = "--existing"
        scope_flag      = "--lint"
        needs_no_server = True
        lint_tools      = request.form.get("lint_tools", "").strip()
        extra_flags     = (["--lint-tools", lint_tools] if lint_tools else [])

    elif scope == "clean":
        portal_cfg    = load_config()
        portal_email  = portal_cfg.get("portal_email", "").strip()
        portal_sso    = portal_cfg.get("portal_sso", "1").strip()
        test_port     = portal_cfg.get("test_port", "9022").strip() or "9022"
        test_base_url = f"http://127.0.0.1:{test_port}"

        install_flag = "--clean"
        scope_flag   = "--full"
        needs_no_server = False  # clean starts its own server on test_port
        lint_tools   = request.form.get("lint_tools", "").strip()

        if portal_email:
            key_password = portal_cfg.get("key_password", "foobar!!") or "foobar!!"
            extra_flags = ["--email", portal_email, "--base-url", test_base_url, "--storepass", key_password]
            if portal_sso in ("1", "true", "yes", "on"):
                extra_flags.append("--sso")
        else:
            # No credentials → safe fallback: reuse running server, skip provision
            needs_no_server = True
            extra_flags = ["--skip-provision"]
        if lint_tools:
            extra_flags += ["--lint-tools", lint_tools]
    else:
        install_flag    = "--existing"
        scope_flag      = "--full" if scope == "full" else "--smoke"
        lint_tools      = request.form.get("lint_tools", "").strip()
        extra_flags     = (["--lint-tools", lint_tools] if lint_tools else [])
        needs_no_server = True  # existing always reuses the running server

    no_server_flags = ["--no-server"] if needs_no_server else []

    # Force unbuffered Python output so every print() flushes to last_run.log
    # immediately — without this, stdout is block-buffered when piped to a file
    # and nothing appears in the live log until the buffer fills (~8 KB) or the
    # process exits.
    _env = os.environ.copy()
    _env["PYTHONUNBUFFERED"] = "1"

    if is_windows:
        cmd = ["cmd", "/c", "test.bat", install_flag, scope_flag] + no_server_flags + extra_flags
        popen_kwargs = dict(
            cwd=cwd,
            env=_env,
            stdout=open(os.path.join(cwd, "tests", "last_run.log"), "wb"),
            stderr=subprocess.STDOUT,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
        )
    else:
        cmd = ["bash", "./test.sh", install_flag, scope_flag] + no_server_flags + extra_flags
        popen_kwargs = dict(
            cwd=cwd,
            env=_env,
            stdout=open(os.path.join(cwd, "tests", "last_run.log"), "wb"),
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )

    try:
        p = subprocess.Popen(cmd, **popen_kwargs)
    except Exception as exc:
        return jsonify({"ok": False, "error": str(exc)}), 500

    # Persist PID so status endpoint can detect a running run
    try:
        with open(os.path.join(cwd, "tests", "last_run.pid"), "w") as f:
            f.write(str(p.pid))
        # Remove any stale done-sentinel so run_status reports running=True
        _done_path = os.path.join(cwd, "tests", "last_run.done")
        if os.path.exists(_done_path):
            os.remove(_done_path)
    except Exception:
        pass

    return jsonify({"ok": True, "pid": p.pid, "scope": scope, "message": "Test run started in background."}), 202



@test_bp.route("/run_status", methods=["GET"])
def run_status():
    """Return current run status and tail of the log file."""
    pid = None
    running = False
    pid_path = os.path.join(os.getcwd(), "tests", "last_run.pid")
    log_path = os.path.join(os.getcwd(), "tests", "last_run.log")

    # Check if done sentinel written by run.py exists — if so the run has
    # finished regardless of PID state (Windows recycles PIDs quickly).
    done_path = os.path.join(os.getcwd(), "tests", "last_run.done")
    done_file_present = os.path.exists(done_path)

    # Read pid if present
    try:
        if os.path.exists(pid_path) and not done_file_present:
            with open(pid_path, "r") as f:
                pid = int(f.read().strip() or 0)
            # Check whether process is still alive (cross-platform)
            try:
                import sys as _sys
                if _sys.platform == "win32":
                    import ctypes
                    SYNCHRONIZE = 0x00100000
                    handle = ctypes.windll.kernel32.OpenProcess(SYNCHRONIZE, False, pid)
                    if handle:
                        import ctypes.wintypes
                        result = ctypes.windll.kernel32.WaitForSingleObject(handle, 0)
                        ctypes.windll.kernel32.CloseHandle(handle)
                        running = (result == 0x102)  # WAIT_TIMEOUT means still running
                    else:
                        running = False
                else:
                    os.kill(pid, 0)
                    running = True
            except Exception:
                running = False
    except Exception:
        pid = None
        running = False

    # Tail log file — strip ANSI escape codes so the browser receives clean text
    import re as _re
    _ANSI_RE = _re.compile(r'\x1b\[[0-9;]*[A-Za-z]')

    def _read_log_lines(path):
        """Read log, decode robustly, strip ANSI codes, return list of stripped lines."""
        try:
            with open(path, "rb") as f:
                raw = f.read()
            text = raw.decode("utf-8", errors="replace")
            return [_ANSI_RE.sub("", l).rstrip("\n") for l in text.splitlines()]
        except Exception:
            return []

    tail_lines = []
    try:
        if os.path.exists(log_path):
            all_log_lines = _read_log_lines(log_path)
            tail_lines = all_log_lines[-400:]
        if not tail_lines:
            tail_lines = []
    except Exception:
        tail_lines = ["(error reading log)"]

    # Simple progress parser: detect suite headers (lines starting with '>>')
    # and test result lines containing [PASS] or [FAIL]. Build a lightweight
    # progress summary for the UI.
    try:
        import re
        suites = []
        current = None
        total = passed = failed = 0
        full_lines = all_log_lines if 'all_log_lines' in dir() else tail_lines

        for ln in full_lines:
            m = re.match(r"^>>\s+(.+)", ln)
            if m:
                name = m.group(1).strip()
                # Skip non-suite header lines (e.g. ">> Skipping server start")
                if name.lower().startswith("skipping"):
                    continue
                # Start new suite
                current = {"name": name, "passed": 0, "failed": 0, "total": 0, "tests": []}
                suites.append(current)
                continue

            if "[PASS]" in ln or "[FAIL]" in ln:
                status = 'pass' if '[PASS]' in ln else 'fail'
                # Extract just the description after the tag
                desc = re.sub(r'^\s*\[(?:PASS|FAIL)\]\s*', '', ln).strip()
                if current is None:
                    current = {"name": "Other", "passed": 0, "failed": 0, "total": 0, "tests": []}
                    suites.append(current)
                current['tests'].append({"name": desc, "status": status})
                current['total'] += 1
                total += 1
                if status == 'pass':
                    current['passed'] += 1
                    passed += 1
                else:
                    current['failed'] += 1
                    failed += 1

        progress = {"total": total, "passed": passed, "failed": failed, "suites": []}
        for s in suites:
            if s['total'] == 0:
                continue  # skip header-only lines with no tests
            pct = int((s['passed'] / s['total'] * 100) if s['total'] > 0 else 0)
            progress['suites'].append({
                'name': s['name'], 'passed': s['passed'], 'failed': s['failed'], 'total': s['total'], 'pct': pct
            })
    except Exception:
        progress = {"total": 0, "passed": 0, "failed": 0, "suites": []}

    return jsonify({"ok": True, "pid": pid, "running": running, "log": tail_lines, "progress": progress})


# ── Codebase stats (used by Run tab) ──────────────────────────────────────────

@test_bp.route("/codebase_stats", methods=["GET"])
def codebase_stats():
    """Walk the source tree and return per-language file + line counts."""
    import re as _re

    # Anchor to repo root via __file__ — os.getcwd() is unreliable inside
    # Flask's test client and when the app is launched from a different directory.
    root = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
    _SKIP_DIRS = {".venv", "__pycache__", ".git", "node_modules", "tests", "tools", ".mypy_cache"}
    _TARGETS = ["apis", "usecases", "chat", "simulator", "static", "templates", "app.py", "clean_keys.py", "live_demo.py"]
    _EXT_LANG = {
        ".py":   "Python",
        ".js":   "JavaScript",
        ".html": "HTML",
        ".css":  "CSS",
        ".json": "JSON",
        ".sh":   "Shell",
        ".bat":  "Batch",
        ".md":   "Markdown",
        ".toml": "TOML",
        ".txt":  "Text",
    }

    counts: dict[str, dict] = {}  # lang -> {files, lines}

    def _scan(path: str) -> None:
        if os.path.isfile(path):
            ext = os.path.splitext(path)[1].lower()
            lang = _EXT_LANG.get(ext)
            if not lang:
                return
            try:
                with open(path, encoding="utf-8", errors="replace") as fh:
                    n = sum(1 for _ in fh)
            except OSError:
                n = 0
            if lang not in counts:
                counts[lang] = {"files": 0, "lines": 0}
            counts[lang]["files"] += 1
            counts[lang]["lines"] += n
        elif os.path.isdir(path):
            try:
                entries = os.listdir(path)
            except OSError:
                return
            for entry in entries:
                if entry in _SKIP_DIRS or entry.startswith("."):
                    continue
                _scan(os.path.join(path, entry))

    for t in _TARGETS:
        full = os.path.join(root, t)
        if os.path.exists(full):
            _scan(full)

    # Sort by lines descending for display
    ordered = sorted(counts.items(), key=lambda x: -x[1]["lines"])
    total_files = sum(v["files"] for v in counts.values())
    total_lines = sum(v["lines"] for v in counts.values())

    return jsonify({
        "ok": True,
        "languages": [{"lang": k, "files": v["files"], "lines": v["lines"]} for k, v in ordered],
        "total_files": total_files,
        "total_lines": total_lines,
    })
