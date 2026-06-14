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
from flask import Blueprint, render_template, request, redirect, url_for

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
