"""Automatic Billing Updater (ABU) API — OAuth 1.0a.

Sandbox base URL: https://sandbox.api.mastercard.com
Reference spec: https://static.developer.mastercard.com/content/automatic-billing-updater/swagger/ABURestAPI.yaml
"""
from __future__ import annotations

import json
import os
import time
from datetime import date
from typing import Any, Dict

# ABU OpenAPI servers:
# - Sandbox:   https://sandbox.api.mastercard.com/abu/accounts/
# - Production:https://api.mastercard.com/abu/accounts/
_SANDBOX_BASE_URL = "https://sandbox.api.mastercard.com/abu/accounts"
_PROD_BASE_URL = "https://api.mastercard.com/abu/accounts"
_TESTING_DOCS_URL = "https://developer.mastercard.com/automatic-billing-updater/documentation/testing/"
_DEFAULT_EXPIRY_MMYY = "1235"
_PUSH_CHECK_CACHE_TTL_S = 300
_PUSH_CHECK_CACHE: Dict[str, Any] = {
    "checked_at": 0.0,
    "ok": None,
    "reason": "",
}


def _sample_payload(account_number: str, expiry: str, request_id: str, *, sub_merchant_id: str = "") -> Dict[str, Any]:
    customer: Dict[str, Any] = {
        "ica": "1111",
        "merchantId": "XXX000000000XXX",
    }
    if sub_merchant_id:
        customer["subMerchantId"] = sub_merchant_id
    return {
        "requestId": request_id,
        "customer": customer,
        "account": {
            "accountNumber": account_number,
            "expiryDate": expiry,
        },
    }


MANIFEST: Dict[str, Any] = {
    "id": "automatic_billing_updater",
    "name": "Automatic Billing Updater",
    "description": (
        "ABU supports pull inquiries and push subscription lifecycle operations "
        "for recurring or card-on-file account updates."
    ),
    "docs_url": "https://developer.mastercard.com/automatic-billing-updater/documentation/",
    "how_to": (
        "<p><strong>Automatic Billing Updater (ABU)</strong> provides account lifecycle "
        "updates for recurring and credential-on-file use cases.</p>"
        "<h3>How to use</h3>"
        "<ol>"
        "<li>Use <strong>Pull → Account inquiry</strong> to fetch current account status on demand.</li>"
        "<li>Use <strong>Push → Subscribe account</strong> to watch an account for future updates.</li>"
        "<li>Use <strong>Push → Subscription inquiry</strong> to verify whether an account is currently watched.</li>"
        "<li>Use <strong>Push → Delete subscription</strong> to stop future notifications for an account.</li>"
        "</ol>"
        "<p><strong>Push entitlement:</strong> push operations require your Mastercard project to be "
        "registered for ABU Push service. If pull works but push returns 401 "
        "<code>Client not registered for ABU Push service</code>, update project entitlements in "
        "Mastercard Developers and reprovision keys.</p>"
        "<h3>Sandbox test values</h3>"
        "<p>ABU mock responses are driven by the final digit of <code>accountNumber</code>. "
        "See official test cases: <a href='" + _TESTING_DOCS_URL + "' target='_blank'>ABU Sandbox Testing</a>.</p>"
        "<ul>"
        "<li><strong>VALID</strong>: account ending in <code>2</code> or <code>9</code>, e.g. "
        "<code>5200000000000002</code>.</li>"
        "<li><strong>ACCOUNT_UPDATE</strong>: ending in <code>0</code> or <code>3</code>, e.g. "
        "<code>5200000000000003</code>.</li>"
        "<li><strong>EXPIRY</strong>: ending in <code>5</code>, e.g. <code>5200000000000005</code>.</li>"
        "<li><strong>CONTACT</strong>: ending in <code>4</code>, e.g. <code>5200000000000004</code>.</li>"
        "<li><strong>UNKNOWN</strong>: ending in <code>7</code>, e.g. <code>5200000000000007</code>.</li>"
        "</ul>"
    ),
    "categories": ["Pull", "Push"],
    "state_schema": [],
    "configured": bool(
        os.environ.get("AUTOMATIC_BILLING_UPDATER_CONSUMER_KEY")
        and os.environ.get("AUTOMATIC_BILLING_UPDATER_CONSUMER_KEY") != "your-consumer-key-here"
        and os.environ.get("AUTOMATIC_BILLING_UPDATER_SIGNING_KEY_PATH")
    ),
    "operations": [
        {
            "id": "account_inquiry",
            "name": "Account inquiry",
            "category": "Pull",
            "method": "POST",
            "description": "Get latest account update status for a payment account.",
            "params": [
                {"name": "request_id", "label": "Request ID", "type": "text", "default": "abu-inquiry-1", "required": True},
                {"name": "ica", "label": "ICA", "type": "text", "default": "1111", "required": True},
                {"name": "merchant_id", "label": "Merchant ID", "type": "text", "default": "XXX000000000XXX", "required": True},
                {"name": "sub_merchant_id", "label": "Sub-merchant ID (optional)", "type": "text", "default": "", "required": False},
                {"name": "account_number", "label": "Account number", "type": "text", "default": "5200000000000002", "required": True},
                {"name": "expiry_date", "label": "Expiry (MMYY)", "type": "text", "default": _DEFAULT_EXPIRY_MMYY, "required": True},
            ],
        },
        {
            "id": "account_subscription",
            "name": "Subscribe account",
            "category": "Push",
            "method": "POST",
            "description": "Subscribe to account updates and receive current status.",
            "params": [
                {"name": "request_id", "label": "Request ID", "type": "text", "default": "abu-sub-1", "required": True},
                {"name": "ica", "label": "ICA", "type": "text", "default": "1111", "required": True},
                {"name": "merchant_id", "label": "Merchant ID", "type": "text", "default": "XXX000000000XXX", "required": True},
                {"name": "sub_merchant_id", "label": "Sub-merchant ID (optional)", "type": "text", "default": "", "required": False},
                {"name": "account_number", "label": "Account number", "type": "text", "default": "5200000000000012", "required": True},
                {"name": "expiry_date", "label": "Expiry (MMYY)", "type": "text", "default": _DEFAULT_EXPIRY_MMYY, "required": True},
            ],
        },
        {
            "id": "subscription_inquiry",
            "name": "Subscription inquiry",
            "category": "Push",
            "method": "POST",
            "description": "Check if this merchant/sub-merchant is subscribed to the account.",
            "params": [
                {"name": "request_id", "label": "Request ID", "type": "text", "default": "abu-subinq-1", "required": True},
                {"name": "ica", "label": "ICA", "type": "text", "default": "1111", "required": True},
                {"name": "merchant_id", "label": "Merchant ID", "type": "text", "default": "XXX000000000XXX", "required": True},
                {"name": "sub_merchant_id", "label": "Sub-merchant ID (optional)", "type": "text", "default": "", "required": False},
                {"name": "account_number", "label": "Account number", "type": "text", "default": "5200000000000001", "required": True},
                {"name": "expiry_date", "label": "Expiry (MMYY)", "type": "text", "default": _DEFAULT_EXPIRY_MMYY, "required": True},
            ],
        },
        {
            "id": "subscription_deletion",
            "name": "Delete subscription",
            "category": "Push",
            "method": "POST",
            "description": "Unsubscribe from future account update notifications.",
            "params": [
                {"name": "request_id", "label": "Request ID", "type": "text", "default": "abu-del-1", "required": True},
                {"name": "ica", "label": "ICA", "type": "text", "default": "1111", "required": True},
                {"name": "merchant_id", "label": "Merchant ID", "type": "text", "default": "XXX000000000XXX", "required": True},
                {"name": "sub_merchant_id", "label": "Sub-merchant ID (optional)", "type": "text", "default": "", "required": False},
                {"name": "account_number", "label": "Account number", "type": "text", "default": "5200000000000002", "required": True},
                {"name": "expiry_date", "label": "Expiry (MMYY)", "type": "text", "default": _DEFAULT_EXPIRY_MMYY, "required": True},
            ],
        },
    ],
}


def _parse_expiry_mmyy(expiry_date: str) -> tuple[int, int]:
    if len(expiry_date) != 4 or not expiry_date.isdigit():
        raise ValueError("expiry_date must be MMYY (for example 1235)")
    month = int(expiry_date[:2])
    year = 2000 + int(expiry_date[2:])
    if month < 1 or month > 12:
        raise ValueError("expiry_date month must be between 01 and 12")
    return year, month


def _expiry_older_than_12_months(expiry_date: str) -> bool:
    year, month = _parse_expiry_mmyy(expiry_date)
    now = date.today()
    expiry_idx = year * 12 + month
    cutoff_idx = now.year * 12 + now.month - 12
    return expiry_idx < cutoff_idx


def _push_expiry_error() -> Dict[str, Any]:
    return {
        "success": False,
        "error": "Invalid expiry_date for ABU Push. Use MMYY not older than 12 months (for example 1235).",
        "hints": [
            "ABU Push rejects accounts with expiry date older than 12 months.",
            "Use a recent/future MMYY and retry (for example 1235).",
        ],
    }


def _extract_error_details(error: Any) -> str:
    if isinstance(error, dict):
        err = error.get("Error")
        if isinstance(err, list) and err:
            first = err[0]
            if isinstance(first, dict):
                return str(first.get("Details") or "")
        if isinstance(err, dict):
            return str(err.get("Details") or "")
    return ""


def _push_entitlement_status(force_refresh: bool = False) -> tuple[bool | None, str]:
    from simulator.switcher import is_simulated

    if is_simulated("automatic_billing_updater"):
        return True, "simulated"
    if not _configured():
        return None, "ABU credentials missing"

    now = time.time()
    cached_ok = _PUSH_CHECK_CACHE.get("ok")
    checked_at = float(_PUSH_CHECK_CACHE.get("checked_at") or 0.0)
    if (
        not force_refresh
        and cached_ok is not None
        and (now - checked_at) < _PUSH_CHECK_CACHE_TTL_S
    ):
        return bool(cached_ok), str(_PUSH_CHECK_CACHE.get("reason") or "")

    probe = _sample_payload(
        account_number="5200000000000012",
        expiry=_DEFAULT_EXPIRY_MMYY,
        request_id="abu-entitlement-check",
    )
    result = _post("/subscription-inquiries", probe)

    ok = True
    reason = ""
    if not result.get("success"):
        status = (result.get("response") or {}).get("status_code")
        details = _extract_error_details(result.get("error"))
        if status == 401 and "Client not registered for ABU Push service" in details:
            ok = False
            reason = details

    _PUSH_CHECK_CACHE["checked_at"] = now
    _PUSH_CHECK_CACHE["ok"] = ok
    _PUSH_CHECK_CACHE["reason"] = reason
    return ok, reason


def _base_url() -> str:
    from simulator.switcher import sim_base_url
    env = os.environ.get("AUTOMATIC_BILLING_UPDATER_ENV", "sandbox").lower()
    real = _PROD_BASE_URL if env == "production" else _SANDBOX_BASE_URL
    return sim_base_url("automatic_billing_updater", real)


def _configured() -> bool:
    key = os.environ.get("AUTOMATIC_BILLING_UPDATER_CONSUMER_KEY", "")
    path = os.environ.get("AUTOMATIC_BILLING_UPDATER_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    if is_simulated("automatic_billing_updater"):
        return True
    # "Configured" means credentials are present and pull can run.
    # Push entitlement is exposed separately via get_state()/hints.
    return _configured()


def get_state() -> Dict[str, Any]:
    push_ok, push_reason = _push_entitlement_status()
    return {
        "configured": is_configured(),
        "push_entitled": push_ok,
        "push_entitlement_reason": push_reason,
    }


def _not_configured_err() -> Dict[str, Any]:
    return {
        "success": False,
        "error": (
            "Automatic Billing Updater is not configured. Set "
            "AUTOMATIC_BILLING_UPDATER_CONSUMER_KEY and "
            "AUTOMATIC_BILLING_UPDATER_SIGNING_KEY_PATH in .env, then restart the server."
        ),
    }


def _resolve_key_path(path: str) -> str:
    if os.path.isabs(path):
        return path
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(project_root, path)


def _build_payload(params: Dict[str, Any]) -> Dict[str, Any]:
    request_id = (params.get("request_id") or "abu-req-1").strip()
    ica = (params.get("ica") or "1111").strip()
    merchant_id = (params.get("merchant_id") or "XXX000000000XXX").strip()
    sub_merchant_id = (params.get("sub_merchant_id") or "").strip()
    account_number = (params.get("account_number") or "").strip()
    expiry_date = (params.get("expiry_date") or "").strip()

    if not account_number:
        raise ValueError("account_number is required")
    if not expiry_date:
        raise ValueError("expiry_date is required")

    customer: Dict[str, Any] = {
        "ica": ica,
        "merchantId": merchant_id,
    }
    if sub_merchant_id:
        customer["subMerchantId"] = sub_merchant_id

    return {
        "requestId": request_id,
        "customer": customer,
        "account": {
            "accountNumber": account_number,
            "expiryDate": expiry_date,
        },
    }


def _post(path: str, body: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    import requests

    body_str = json.dumps(body)
    url = f"{_base_url()}{path}"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    if is_simulated("automatic_billing_updater"):
        headers["Authorization"] = "Simulated"
    else:
        import oauth1.authenticationutils as authutils
        from oauth1.oauth import OAuth

        consumer_key = os.environ["AUTOMATIC_BILLING_UPDATER_CONSUMER_KEY"]
        key_path = _resolve_key_path(os.environ["AUTOMATIC_BILLING_UPDATER_SIGNING_KEY_PATH"])
        key_password = os.environ.get("AUTOMATIC_BILLING_UPDATER_SIGNING_KEY_PASSWORD", "keystorepassword")

        try:
            signing_key = authutils.load_signing_key(key_path, key_password)
            auth_header = OAuth.get_authorization_header(url, "POST", body_str, consumer_key, signing_key)
            headers["Authorization"] = auth_header
        except Exception as exc:
            return {"success": False, "error": f"OAuth signing failed: {exc}"}

    try:
        resp = requests.post(url, data=body_str, headers=headers, timeout=15)
        status_code = resp.status_code
        try:
            resp_body = resp.json()
        except Exception:
            resp_body = {"raw": resp.text}
    except Exception as exc:
        return {"success": False, "error": f"Request failed: {exc}"}

    success = 200 <= status_code < 300
    hints: list[str] = []
    if not success and isinstance(resp_body, dict):
        errors = ((resp_body.get("Errors") or {}).get("Error") or [])
        if isinstance(errors, dict):
            errors = [errors]
        for err in errors:
            if not isinstance(err, dict):
                continue
            reason = str(err.get("ReasonCode") or "")
            details = str(err.get("Details") or "")
            if reason == "INVALID_EXPIRY_DATE":
                hints.append("Use expiry_date MMYY not older than 12 months (for example 1235).")
            if reason == "AUTHENTICATION_FAILED" and "ABU Push service" in details:
                hints.append(
                    "Your current key is valid for ABU Pull but not registered for ABU Push. "
                    "Enable ABU Push service in Mastercard Developers for this project and reprovision keys."
                )

    return {
        "success": success,
        "data": resp_body if success else {},
        "error": None if success else (resp_body.get("Errors") if isinstance(resp_body, dict) else resp_body),
        "request": {"method": "POST", "url": url, "body": body},
        "response": {"status_code": status_code, "body": resp_body},
        "hints": hints,
        "state_updates": {},
    }


def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("automatic_billing_updater"):
        return _not_configured_err()

    is_push_op = op_id in {"account_subscription", "subscription_inquiry", "subscription_deletion"}

    try:
        body = _build_payload(params)
    except ValueError as exc:
        return {"success": False, "error": str(exc)}

    if is_push_op:
        try:
            if _expiry_older_than_12_months(str(body.get("account", {}).get("expiryDate", ""))):
                return _push_expiry_error()
        except ValueError as exc:
            return {"success": False, "error": str(exc)}

    if op_id == "account_inquiry":
        return _post("/inquiries", body)
    if op_id == "account_subscription":
        return _post("/subscriptions", body)
    if op_id == "subscription_inquiry":
        return _post("/subscription-inquiries", body)
    if op_id == "subscription_deletion":
        return _post("/subscription-deletions", body)
    return {"success": False, "error": f"Unknown operation: {op_id}"}
