"""tests/lib/provision.py — drive the auto-provisioning endpoint.

Provides:
  start_provision_job(base_url, apis, key_password) → str (job_id)
  stream_provision(base_url, job_id)                → generator[str]
  wait_provision_complete(base_url, job_id, email,
                          timeout=600)              → bool (success)

The provision flow requires the user to log in to the Mastercard Developers
portal manually in the browser that the automation tool opens.  This module
streams the SSE log to stdout so the operator can follow progress.

Sentinel values emitted by the server's SSE stream:
  __IMPORT_COMPLETE__          — success; credentials imported
  __NO_ZIP__                   — provisioner finished but no zip produced
  __IMPORT_ERROR__:<msg>       — zip found but import failed
  __PROVISION_FAILED__:<msg>   — provisioner reported a hard failure
  __DONE__                     — stream closed (always last)
"""
from __future__ import annotations

import json
import time
import webbrowser
from typing import Generator

import requests


# ── Portal credentials ─────────────────────────────────────────────────────────
def save_portal_credentials(
    base_url: str,
    email: str,
    password: str = "",
) -> None:
    """Save Mastercard portal login credentials to the running server's config.

    The key-automation provisioner subprocess reads MCD_PORTAL_EMAIL (and
    optionally MCD_PORTAL_PASSWORD) from the environment.  Calling this
    before start_provision_job ensures the server writes them to
    config/.env and reloads them with load_dotenv(override=True) so the
    provisioner subprocess inherits both vars.

    SSO flows (password="" ): only MCD_PORTAL_EMAIL is written.
        The key-automation login page detects email-only mode and auto-fills
        just the email field, then waits for the SSO redirect to complete.
    Non-SSO flows (password given): both fields are written and the login
        form is submitted with email + password automatically.
    """
    updates: dict = {"MCD_PORTAL_EMAIL": email}
    if password:
        updates["MCD_PORTAL_PASSWORD"] = password
    try:
        resp = requests.post(
            f"{base_url}/config",
            json={"updates": updates},
            timeout=10,
        )
        if resp.status_code != 200:
            print(
                f"  [WARN] Could not save portal credentials to server config: "
                f"HTTP {resp.status_code}"
            )
    except Exception as exc:
        print(f"  [WARN] save_portal_credentials failed: {exc}")


# ── Start ──────────────────────────────────────────────────────────────────────
def start_provision_job(
    base_url: str,
    apis: list[str],
    key_password: str = "foobar!!",
) -> str:
    """POST /provision/start and return the job_id string."""
    url = f"{base_url}/provision/start"
    resp = requests.post(
        url,
        json={"apis": apis, "password": key_password, "project_prefix": "SST"},
        timeout=30,
    )
    if resp.status_code != 200:
        raise RuntimeError(
            f"POST /provision/start returned {resp.status_code}: {resp.text[:400]}"
        )
    data = resp.json()
    if "error" in data:
        raise RuntimeError(f"Provision start error: {data['error']}")
    job_id = data.get("job_id")
    if not job_id:
        raise RuntimeError(f"No job_id in response: {data}")
    return job_id


# ── Stream ─────────────────────────────────────────────────────────────────────
def stream_provision(base_url: str, job_id: str) -> Generator[str, None, None]:
    """Yield each log line from the SSE stream for *job_id*.

    Handles JSON-encoded log lines and raw sentinel strings.
    Stops when __DONE__ is received or the connection drops.
    """
    url = f"{base_url}/provision/stream/{job_id}"
    with requests.get(url, stream=True, timeout=None) as resp:
        if resp.status_code != 200:
            raise RuntimeError(
                f"GET /provision/stream/{job_id} returned {resp.status_code}"
            )
        for raw in resp.iter_lines(decode_unicode=True):
            if not raw or not raw.startswith("data:"):
                continue
            payload = raw[len("data:"):].strip()
            if not payload:
                continue
            if payload == "__DONE__":
                return
            # Sentinel control strings are sent as plain text
            if payload.startswith("__"):
                yield payload
                if payload == "__IMPORT_COMPLETE__":
                    return
            else:
                # Regular log lines are JSON-encoded strings
                try:
                    yield json.loads(payload)
                except json.JSONDecodeError:
                    yield payload


# ── Wait ───────────────────────────────────────────────────────────────────────
def wait_provision_complete(
    base_url: str,
    job_id: str,
    email: str,
    timeout: float = 600.0,
) -> bool:
    """Stream provisioning output to stdout; return True on success.

    Opens the app in the default browser so the operator can complete the
    Mastercard Developers portal SSO login.
    """
    app_url = f"{base_url}/app"
    print(f"\n  Opening {app_url} for Mastercard portal SSO login …")
    print(f"  Account: {email}")
    print(f"  Please log in when the browser opens and complete the portal flow.")
    print(f"  (Timeout: {timeout:.0f}s)\n")

    deadline = time.time() + timeout
    success = False
    failed_msg = ""

    print("  Provisioning log:")
    for line in stream_provision(base_url, job_id):
        if time.time() > deadline:
            print("\n  ⚠  Provision timeout exceeded.")
            return False

        if isinstance(line, str):
            if line == "__IMPORT_COMPLETE__":
                success = True
                print("  [OK]  Credentials imported successfully.")
                break
            if line.startswith("__NO_ZIP__"):
                print("  [FAIL]  No zip produced -- check that the portal flow completed.")
                return False
            if line.startswith("__IMPORT_ERROR__:"):
                print(f"  [FAIL]  Import error: {line[len('__IMPORT_ERROR__:'):]}")
                return False
            if line.startswith("__PROVISION_FAILED__:"):
                failed_msg = line[len("__PROVISION_FAILED__:"):]
                print(f"  [FAIL]  Provision failed: {failed_msg}")
                return False

        print(f"    {line}")

    return success
