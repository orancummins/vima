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
)
from tests.dashboard.mailer import load_config, save_config, send_test_email

_PAGE_SIZE = 15

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
    # Group by suite
    suites: dict = {}
    for r in results:
        s = r["suite"]
        if s not in suites:
            suites[s] = []
        suites[s].append(r)
    return render_template("test_run.html", run=run, suites=suites)


# ── Config view ────────────────────────────────────────────────────────────────

@test_bp.route("/config", methods=["GET", "POST"])
def config():
    cfg = load_config()
    saved = False
    test_result = None

    if request.method == "POST":
        action = request.form.get("action", "save")
        new_cfg = {
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
    import shlex
    from flask import jsonify

    # Run smoke tests against the existing working directory, non-interactive.
    cmd = "bash ./test.sh --existing --smoke --no-server"
    try:
        # Launch in background so the web request returns immediately.
        p = subprocess.Popen(
            shlex.split(cmd),
            cwd=os.getcwd(),
            stdout=open("tests/last_run.log", "ab"),
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    except Exception as exc:
        return jsonify({"ok": False, "error": str(exc)}), 500

    # Persist PID so status endpoint can detect a running run
    try:
        with open("tests/last_run.pid", "w") as f:
            f.write(str(p.pid))
    except Exception:
        pass

    return jsonify({"ok": True, "pid": p.pid, "message": "Test run started in background."}), 202



@test_bp.route("/run_status", methods=["GET"])
def run_status():
    """Return current run status and tail of the log file."""
    pid = None
    running = False
    pid_path = os.path.join(os.getcwd(), "tests", "last_run.pid")
    log_path = os.path.join(os.getcwd(), "tests", "last_run.log")

    # Read pid if present
    try:
        if os.path.exists(pid_path):
            with open(pid_path, "r") as f:
                pid = int(f.read().strip() or 0)
            # Check whether process exists
            try:
                os.kill(pid, 0)
                running = True
            except Exception:
                running = False
    except Exception:
        pid = None
        running = False

    # Tail log file
    tail_lines = []
    try:
        if os.path.exists(log_path):
            with open(log_path, "r") as f:
                lines = f.readlines()
            tail_lines = [l.rstrip("\n") for l in lines[-400:]]
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
        # Use the full log if available for accurate counts, else tail_lines
        full_lines = []
        try:
            with open(log_path, 'r') as f:
                full_lines = [l.rstrip('\n') for l in f.readlines()]
        except Exception:
            full_lines = tail_lines

        for ln in full_lines:
            m = re.match(r"^>>\s*(.*)", ln)
            if m:
                # start new suite
                current = {"name": m.group(1).strip(), "passed": 0, "failed": 0, "total": 0, "tests": []}
                suites.append(current)
                continue

            if "[PASS]" in ln or "[FAIL]" in ln or "[OK]" in ln:
                status = 'pass' if ('[PASS]' in ln or '[OK]' in ln) else 'fail'
                desc = ln.strip()
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
            pct = int((s['passed'] / s['total'] * 100) if s['total'] > 0 else 0)
            progress['suites'].append({
                'name': s['name'], 'passed': s['passed'], 'failed': s['failed'], 'total': s['total'], 'pct': pct
            })
    except Exception:
        progress = {"total": 0, "passed": 0, "failed": 0, "suites": []}

    return jsonify({"ok": True, "pid": pid, "running": running, "log": tail_lines, "progress": progress})
