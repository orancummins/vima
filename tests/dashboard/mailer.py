"""tests/dashboard/mailer.py — Email notifications for test run results.

Configuration lives in tests/test_config.ini (gitignored).
A checked-in example is at tests/test_config.example.ini.
"""
from __future__ import annotations

import configparser
import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any, Dict, Optional, Tuple

_TESTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CONFIG_PATH = os.path.join(_TESTS_DIR, "test_config.ini")

_EMAIL_DEFAULTS: Dict[str, str] = {
    "smtp_host": "",
    "smtp_port": "587",
    "smtp_user": "",
    "smtp_password": "",
    "from_address": "",
    "to_addresses": "",
    "use_tls": "1",
}

# Keep backwards-compatible alias
_DEFAULTS = _EMAIL_DEFAULTS

_PORTAL_DEFAULTS: Dict[str, str] = {
    "portal_email": "",
    "portal_sso": "1",
    "test_port": "9022",
    "key_password": "foobar!!",
}


def load_config() -> Dict[str, str]:
    """Load email + portal config from tests/test_config.ini.  Returns defaults on missing file."""
    cfg = {**_EMAIL_DEFAULTS, **_PORTAL_DEFAULTS}
    if not os.path.exists(_CONFIG_PATH):
        return cfg
    parser = configparser.ConfigParser()
    try:
        parser.read(_CONFIG_PATH, encoding="utf-8")
        if parser.has_section("email"):
            for key in _EMAIL_DEFAULTS:
                if parser.has_option("email", key):
                    cfg[key] = parser.get("email", key)
        if parser.has_section("portal"):
            for key in _PORTAL_DEFAULTS:
                if parser.has_option("portal", key):
                    cfg[key] = parser.get("portal", key)
    except Exception:
        pass
    return cfg


def save_config(cfg: Dict[str, str]) -> None:
    """Persist email + portal config to tests/test_config.ini."""
    parser = configparser.ConfigParser()
    parser["email"] = {k: cfg.get(k, _EMAIL_DEFAULTS.get(k, "")) for k in _EMAIL_DEFAULTS}
    parser["portal"] = {k: cfg.get(k, _PORTAL_DEFAULTS.get(k, "")) for k in _PORTAL_DEFAULTS}
    with open(_CONFIG_PATH, "w", encoding="utf-8") as fh:
        parser.write(fh)


def _build_message(
    cfg: Dict[str, str],
    subject: str,
    html_body: str,
) -> MIMEMultipart:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = cfg.get("from_address") or cfg.get("smtp_user", "vima-test")
    to_list = [a.strip() for a in cfg.get("to_addresses", "").split(",") if a.strip()]
    msg["To"] = ", ".join(to_list)
    msg.attach(MIMEText(html_body, "html", "utf-8"))
    return msg


def _smtp_send(cfg: Dict[str, str], msg: MIMEMultipart) -> None:
    host = cfg["smtp_host"]
    port = int(cfg.get("smtp_port") or 587)
    use_tls = str(cfg.get("use_tls", "1")).strip() in ("1", "true", "yes", "on")
    user = cfg.get("smtp_user", "")
    password = cfg.get("smtp_password", "")
    to_list = [a.strip() for a in cfg.get("to_addresses", "").split(",") if a.strip()]

    ctx = ssl.create_default_context()
    if port == 465:
        with smtplib.SMTP_SSL(host, port, context=ctx) as server:
            if user:
                server.login(user, password)
            server.sendmail(msg["From"], to_list, msg.as_string())
    else:
        with smtplib.SMTP(host, port) as server:
            if use_tls:
                server.starttls(context=ctx)
            if user:
                server.login(user, password)
            server.sendmail(msg["From"], to_list, msg.as_string())


def send_test_email(cfg: Dict[str, str]) -> Tuple[bool, str]:
    """Send a connectivity test email. Returns (ok, message)."""
    try:
        subject = "Vima Test Dashboard — connectivity test"
        body = "<p>This is a test email from the Vima Test Dashboard. Configuration is working.</p>"
        msg = _build_message(cfg, subject, body)
        _smtp_send(cfg, msg)
        return True, "Test email sent successfully."
    except Exception as exc:
        return False, str(exc)


def send_summary_email(
    cfg: Dict[str, str],
    run_id: int,
    passed: int,
    failed: int,
    total: int,
    duration: float,
    install_type: str,
    os_name: str,
    scope: str,
    suite_results: Any,  # list of dicts with suite/name/passed/message
) -> Tuple[bool, str]:
    """Send a test run summary email. Returns (ok, message)."""
    try:
        all_pass = failed == 0
        status_word = "PASSED" if all_pass else "FAILED"
        status_color = "#1f9d55" if all_pass else "#eb001b"
        subject = f"Vima Tests {status_word}: {passed}/{total} passing — Run #{run_id}"

        # Build failures table rows
        failure_rows = ""
        for r in (suite_results or []):
            if not r.get("passed", True):
                suite = r.get("suite", "")
                name = r.get("name", "")
                msg = r.get("message", "") or ""
                failure_rows += (
                    f"<tr><td style='padding:6px 10px;border-bottom:1px solid #333'>{suite}</td>"
                    f"<td style='padding:6px 10px;border-bottom:1px solid #333'>{name}</td>"
                    f"<td style='padding:6px 10px;border-bottom:1px solid #333;color:#f79e1b;font-family:monospace;font-size:12px'>{msg[:400]}</td></tr>"
                )

        failures_section = ""
        if failure_rows:
            failures_section = f"""
            <h3 style='color:#eb001b;margin-top:24px'>Failures</h3>
            <table style='width:100%;border-collapse:collapse;font-size:13px'>
              <thead>
                <tr style='background:#1e1e1e'>
                  <th style='padding:8px 10px;text-align:left;color:#aaa'>Suite</th>
                  <th style='padding:8px 10px;text-align:left;color:#aaa'>Test</th>
                  <th style='padding:8px 10px;text-align:left;color:#aaa'>Error</th>
                </tr>
              </thead>
              <tbody>{failure_rows}</tbody>
            </table>"""

        mins = int(duration // 60)
        secs = int(duration % 60)
        duration_str = f"{mins}m {secs}s" if mins else f"{secs}s"

        html_body = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"/></head>
<body style='font-family:Inter,sans-serif;background:#111;color:#f4f0ea;padding:32px;margin:0'>
  <div style='max-width:680px;margin:0 auto'>
    <div style='display:flex;align-items:center;gap:12px;margin-bottom:24px'>
      <div style='display:flex;gap:4px'>
        <div style='width:18px;height:18px;border-radius:50%;background:#eb001b'></div>
        <div style='width:18px;height:18px;border-radius:50%;background:#f79e1b'></div>
      </div>
      <span style='font-weight:700;font-size:16px'>Mastercard Solution Studio</span>
    </div>

    <h1 style='font-size:22px;margin:0 0 6px'>
      Test Run <span style='color:#f79e1b'>#{run_id}</span> —
      <span style='color:{status_color}'>{status_word}</span>
    </h1>
    <p style='color:#888;margin:0 0 24px;font-size:13px'>
      {scope.capitalize()} install &middot; {install_type} &middot; {os_name}
    </p>

    <div style='display:flex;gap:16px;flex-wrap:wrap;margin-bottom:24px'>
      <div style='background:#1a1a1a;border:1px solid #2a2a2a;border-radius:8px;padding:16px 24px;min-width:130px'>
        <div style='font-size:28px;font-weight:700;color:{status_color}'>{passed}/{total}</div>
        <div style='font-size:12px;color:#888;margin-top:4px'>Tests passing</div>
      </div>
      <div style='background:#1a1a1a;border:1px solid #2a2a2a;border-radius:8px;padding:16px 24px;min-width:130px'>
        <div style='font-size:28px;font-weight:700;color:#f4f0ea'>{duration_str}</div>
        <div style='font-size:12px;color:#888;margin-top:4px'>Duration</div>
      </div>
    </div>

    {failures_section}

    <p style='font-size:12px;color:#555;margin-top:32px;border-top:1px solid #222;padding-top:16px'>
      Vima / Mastercard Solution Studio &mdash; automated test runner
    </p>
  </div>
</body></html>"""

        msg = _build_message(cfg, subject, html_body)
        _smtp_send(cfg, msg)
        return True, ""
    except Exception as exc:
        return False, str(exc)
