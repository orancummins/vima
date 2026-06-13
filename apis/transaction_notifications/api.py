"""Transaction Notifications API — OAuth 1.0a.

Sandbox base URL: https://sandbox.api.mastercard.com/openapis

Key endpoints:
  POST /openapis/notifications/transactions    — trigger a sandbox test transaction
  GET  /openapis/undelivered-notifications     — retrieve failed/undelivered notifications

Auth: OAuth 1.0a (Mastercard signing library).

Docs:
  https://developer.mastercard.com/transaction-notifications/documentation/
  https://developer.mastercard.com/transaction-notifications/documentation/api-reference/transaction-notification-webhook/
"""
from __future__ import annotations

import json
import os
from typing import Any, Dict

_SANDBOX_BASE_URL = "https://sandbox.api.mastercard.com/openapis"
_PROD_BASE_URL    = "https://api.mastercard.com/openapis"

_CONSENT_SANDBOX_BASE_URL = "https://sandbox.api.mastercard.com/openapis/authentication"
_CONSENT_PROD_BASE_URL    = "https://api.mastercard.com/openapis/authentication"

# In-process state for card enrollment (consent lifecycle).
STATE: Dict[str, Any] = {
    "card_ref":           "",
    "consent_id":        "",
    "verify_auth_params": "{}",
}

MANIFEST: Dict[str, Any] = {
    "id": "transaction_notifications",
    "name": "Transaction Notifications",
    "description": (
        "Mastercard Transaction Notifications — receive real-time push notifications "
        "when enrolled cardholders make purchases. Trigger sandbox test transactions "
        "and retrieve any undelivered notifications."
    ),
    "docs_url": "https://developer.mastercard.com/transaction-notifications/documentation/",
    "how_to": (
        "<p><strong>Transaction Notifications</strong> enables your application to receive "
        "real-time purchase data for enrolled cardholders immediately after a transaction "
        "is authorised on the Mastercard network.</p>"
        "<h3>Integration flow</h3>"
        "<ol>"
        "<li>Obtain cardholder consent via the "
        "<a href='https://developer.mastercard.com/consent-management/documentation/' target='_blank'>"
        "Consent Management API</a>. This returns a <code>cardReference</code> you store.</li>"
        "<li>Register a webhook URL at project setup. Mastercard POSTs transaction data "
        "to this endpoint in real time after each purchase.</li>"
        "<li>In sandbox, use <strong>Notifications → Trigger test transaction</strong> to "
        "simulate a purchase and see the notification payload on your webhook.</li>"
        "<li>Use <strong>Notifications → Get undelivered notifications</strong> to retrieve "
        "any notifications your webhook failed to acknowledge (HTTP 2xx).</li>"
        "</ol>"
        "<h3>Payload fields</h3>"
        "<ul>"
        "<li><strong>cardReference</strong> — unique token for the enrolled card (from consent flow).</li>"
        "<li><strong>cardholderAmount / cardholderCurrency</strong> — transaction value.</li>"
        "<li><strong>merchantName</strong> — merchant at which the purchase was made.</li>"
        "<li><strong>transUid</strong> — unique ID for each authorisation notification "
        "(use to deduplicate retries).</li>"
        "</ul>"
        "<h3>Sandbox notes</h3>"
        "<ul>"
        "<li>A webhook must be registered with Mastercard before test transactions are delivered.</li>"
        "<li>The <code>cardReference</code> is obtained through the consent flow — "
        "use the sandbox card reference from your project dashboard for testing.</li>"
        "</ul>"
        "<h3>Receiving simulated transactions locally via ngrok</h3>"
        "<p>Mastercard requires a public HTTPS URL to POST notifications to. Use "
        "<a href='https://ngrok.com/download' target='_blank'>ngrok</a> to expose a local "
        "listener so you can see test payloads land in real time.</p>"
        "<ol>"
        "<li><strong>Run a local webhook listener</strong> on any port, e.g. with "
        "<a href='https://webhook.site/' target='_blank'>webhook.site</a>'s local CLI, "
        "<code>npx http-echo-server 4000</code>, or a tiny Flask app:"
        "<pre><code>from flask import Flask, request\n"
        "app = Flask(__name__)\n"
        "@app.post('/webhook')\n"
        "def hook():\n"
        "    print(request.json)\n"
        "    return '', 200\n"
        "app.run(port=4000)</code></pre></li>"
        "<li><strong>Expose it with ngrok</strong> (one-time: <code>brew install ngrok</code> "
        "or download from ngrok.com, then <code>ngrok config add-authtoken &lt;token&gt;</code>):"
        "<pre><code>ngrok http 4000</code></pre>"
        "Copy the HTTPS forwarding URL it prints (e.g. "
        "<code>https://abc123.ngrok-free.app</code>).</li>"
        "<li><strong>Register the webhook</strong> on your Mastercard Developer project: "
        "<a href='https://developer.mastercard.com/dashboard' target='_blank'>"
        "developer.mastercard.com/dashboard</a> → your project → "
        "<em>Transaction Notifications</em> → <em>Webhooks</em> → set "
        "<code>https://abc123.ngrok-free.app/webhook</code>. The endpoint must return "
        "HTTP 2xx within a few seconds or the notification is queued for retry "
        "(retrievable via <em>Get undelivered notifications</em>).</li>"
        "<li><strong>Enroll a card</strong> via <a href='#consent'>Consent Management</a> "
        "and capture the <code>cardReference</code> returned by <em>Create consent</em>.</li>"
        "<li><strong>Trigger a test transaction</strong> below using that "
        "<code>card_reference</code>. The signed payload arrives at your ngrok tunnel "
        "within seconds — watch the ngrok inspector at "
        "<a href='http://127.0.0.1:4040' target='_blank'>http://127.0.0.1:4040</a> "
        "to see the full request body and headers.</li>"
        "</ol>"
        "<p><em>Tip:</em> ngrok free URLs change on each restart — re-register the webhook "
        "in the dashboard, or use a reserved domain (<code>ngrok http --domain=... 4000</code>) "
        "to keep it stable.</p>"
        "<h3>Card enrollment (Consent)</h3>"
        "<p>Before triggering test transactions, enroll a card using the "
        "<strong>Consent</strong> operations below. These use the same project "
        "credentials — no separate Consent Management project is needed.</p>"
    ),
    "categories": ["Consent", "Notifications"],
    # Step-by-step guide for the floating API Guide coach. Three simple steps.
    # step types:
    #   "api_call" (default) — selects the op; advances after a 2xx response
    #   "manual"             — instruction only; user clicks the button to advance
    "guide": [
        {
            "op": "create_consent",
            "title": "Create Consent",
            "summary": "Enroll the card. Click Send below.",
        },
        {
            "type": "manual",
            "id": "launch_3ds",
            "title": "Launch 3DS Method",
            "summary": "Click the orange Launch 3DS Method button, then continue.",
            "done_label": "I've completed 3DS",
        },
        {
            "op": "trigger_test_transaction",
            "title": "Trigger Test Transaction",
            "summary": "Simulate a purchase. Click Send below.",
        },
    ],
    "state_schema": [
        {"key": "card_ref",           "label": "Card Reference"},
        {"key": "consent_id",         "label": "Consent ID"},
        {"key": "verify_auth_params", "label": "Verify Auth Params (JSON)"},
    ],
    "configured": bool(
        os.environ.get("TRANSACTION_NOTIFICATIONS_CONSUMER_KEY")
        and os.environ.get("TRANSACTION_NOTIFICATIONS_CONSUMER_KEY") != "your-consumer-key-here"
        and os.environ.get("TRANSACTION_NOTIFICATIONS_SIGNING_KEY_PATH")
    ),
    "operations": [
        # ---- Consent enrollment operations ----
        {
            "id": "create_consent",
            "name": "Create consent",
            "category": "Consent",
            "method": "POST",
            "browser_action": True,
            "description": (
                "Enroll a card by submitting PAN and expiry details. Returns a "
                "cardReference (UUID) and a 3DS Method URL for device fingerprinting. "
                "Click Launch 3DS Method (shown at the top of the hint area) to "
                "complete the 3DS Method in your browser, then call Start Authentication."
            ),
            "params": [
                {
                    "name": "pan",
                    "label": "Card Number (PAN)",
                    "type": "text",
                    "default": "2303779951000297",
                    "required": True,
                    "placeholder": "16-digit PAN",
                    "help": "Sandbox test PAN: 2303779951000297",
                },
                {
                    "name": "expiry_month",
                    "label": "Expiry Month",
                    "type": "select",
                    "default": "1",
                    "required": True,
                    "options": [
                        {"value": str(i), "label": f"{i:02d}"} for i in range(1, 13)
                    ],
                },
                {
                    "name": "expiry_year",
                    "label": "Expiry Year",
                    "type": "select",
                    "default": "2028",
                    "required": True,
                    "options": [
                        {"value": str(y), "label": str(y)} for y in range(2026, 2035)
                    ],
                },
                {
                    "name": "cvc",
                    "label": "CVC",
                    "type": "text",
                    "default": "123",
                    "required": False,
                    "placeholder": "3-digit CVC",
                },
                {
                    "name": "cardholder_name",
                    "label": "Cardholder Name",
                    "type": "text",
                    "default": "John Smith",
                    "required": False,
                    "placeholder": "e.g. John Smith",
                },
                {
                    "name": "consent_name",
                    "label": "Consent Type",
                    "type": "select",
                    "default": "notification",
                    "required": True,
                    "options": [
                        {"value": "notification", "label": "notification — Transaction Notifications"},
                    ],
                },
            ],
        },
        {
            "id": "get_consents",
            "name": "Get consents",
            "category": "Consent",
            "method": "GET",
            "description": (
                "Retrieve all consents and their current statuses for a card reference. "
                "Status APPROVED means the card is enrolled and active."
            ),
            "params": [
                {
                    "name": "card_ref",
                    "label": "Card Reference",
                    "type": "text",
                    "default": "",
                    "source": "state:card_ref",
                    "required": True,
                    "placeholder": "UUID from Create Consent",
                    "help": "Auto-filled after Create Consent.",
                },
            ],
        },
        {
            "id": "start_authentication",
            "name": "Start authentication",
            "category": "Consent",
            "method": "POST",
            "description": (
                "Initiate 3DS authentication after completing Launch 3DS Method. "
                "If no challenge is required, status can return AUTHENTICATED immediately."
            ),
            "params": [
                {
                    "name": "card_ref",
                    "label": "Card Reference",
                    "type": "text",
                    "default": "",
                    "source": "state:card_ref",
                    "required": True,
                    "placeholder": "UUID from Create Consent",
                },
                {
                    "name": "auth_type",
                    "label": "Auth Type",
                    "type": "select",
                    "default": "THREEDS",
                    "required": True,
                    "options": [
                        {"value": "THREEDS", "label": "THREEDS — 3D Secure"},
                        {"value": "ASI",     "label": "ASI — Account Status Inquiry"},
                    ],
                },
                {
                    "name": "auth_params",
                    "label": "Auth Params (JSON)",
                    "type": "text",
                    "default": (
                        '{"fingerprintStatus":"complete",'
                        '"challengeWindowSize":"04",'
                        '"browserAcceptHeader":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",'
                        '"browserColorDepth":"24",'
                        '"browserJavaEnabled":false,'
                        '"browserLanguage":"en-US",'
                        '"browserScreenHeight":"1080",'
                        '"browserScreenWidth":"1920",'
                        '"browserTZ":"0",'
                        '"browserUserAgent":"Mozilla/5.0"}'
                    ),
                    "required": False,
                    "help": (
                        "EMV 3DS browser params. Normally auto-filled by the 3DS flow "
                        "browser page launched from Create Consent."
                    ),
                },
            ],
        },
        {
            "id": "verify_authentication",
            "name": "Verify authentication",
            "category": "Consent",
            "method": "POST",
            "description": (
                "Complete consent enrollment after Start Authentication. "
                "If auth_params is left empty, the API auto-uses state from prior 3DS steps."
            ),
            "params": [
                {
                    "name": "card_ref",
                    "label": "Card Reference",
                    "type": "text",
                    "default": "",
                    "source": "state:card_ref",
                    "required": True,
                    "placeholder": "UUID from Create Consent",
                },
                {
                    "name": "auth_type",
                    "label": "Auth Type",
                    "type": "select",
                    "default": "THREEDS",
                    "required": True,
                    "options": [
                        {"value": "THREEDS", "label": "THREEDS — 3D Secure"},
                    ],
                },
                {
                    "name": "auth_params",
                    "label": "Auth Params (JSON)",
                    "type": "text",
                    "default": "{}",
                    "source": "state:verify_auth_params",
                    "required": False,
                    "placeholder": '{"key": "value"}',
                    "help": "Auto-populated from Start Authentication when available.",
                },
            ],
        },
        {
            "id": "delete_consents",
            "name": "Delete all consents",
            "category": "Consent",
            "method": "DELETE",
            "description": (
                "Revoke and delete all consents for a card reference. "
                "The card will no longer receive transaction notifications."
            ),
            "params": [
                {
                    "name": "card_ref",
                    "label": "Card Reference",
                    "type": "text",
                    "default": "",
                    "source": "state:card_ref",
                    "required": True,
                    "placeholder": "UUID from Create Consent",
                },
            ],
        },
        {
            "id": "delete_single_consent",
            "name": "Delete single consent",
            "category": "Consent",
            "method": "DELETE",
            "description": (
                "Revoke and delete a specific consent (by consent ID) for a card reference."
            ),
            "params": [
                {
                    "name": "card_ref",
                    "label": "Card Reference",
                    "type": "text",
                    "default": "",
                    "source": "state:card_ref",
                    "required": True,
                    "placeholder": "UUID from Create Consent",
                },
                {
                    "name": "consent_id",
                    "label": "Consent ID",
                    "type": "text",
                    "default": "",
                    "source": "state:consent_id",
                    "required": True,
                    "placeholder": "Auto-filled after Get Consents",
                    "help": "Auto-filled from the first consent returned by Get Consents.",
                },
            ],
        },
        # ---- Notification operations ----
        {
            "id": "trigger_test_transaction",
            "name": "Trigger test transaction",
            "category": "Notifications",
            "method": "POST",
            "description": (
                "Sandbox only — simulate a cardholder purchase that generates a "
                "real-time transaction notification to your registered webhook URL."
            ),
            "params": [
                {
                    "name": "card_reference",
                    "label": "Card Reference",
                    "type": "text",
                    "default": "",
                    "required": True,
                    "placeholder": "e.g. 6c9a079c-18dc-4881-9907-467aad648333",
                    "help": (
                        "UUID returned by Consent Management when a card is enrolled. "
                        "If left blank, the API will try the latest Consent card reference in memory."
                    ),
                },
                {
                    "name": "amount",
                    "label": "Amount",
                    "type": "select",
                    "default": "9.99",
                    "required": True,
                    "options": [
                        {"value": "9.99",  "label": "9.99"},
                        {"value": "24.50", "label": "24.50"},
                        {"value": "49.00", "label": "49.00"},
                        {"value": "100.00","label": "100.00"},
                        {"value": "1.00",  "label": "1.00"},
                    ],
                },
                {
                    "name": "currency",
                    "label": "Currency",
                    "type": "select",
                    "default": "USD",
                    "required": True,
                    "options": [
                        {"value": "USD", "label": "USD — US Dollar"},
                        {"value": "EUR", "label": "EUR — Euro"},
                        {"value": "GBP", "label": "GBP — British Pound"},
                        {"value": "AUD", "label": "AUD — Australian Dollar"},
                        {"value": "CAD", "label": "CAD — Canadian Dollar"},
                    ],
                },
                {
                    "name": "merchant_name",
                    "label": "Merchant Name",
                    "type": "select",
                    "default": "Coffee Corner",
                    "required": True,
                    "options": [
                        {"value": "Coffee Corner",  "label": "Coffee Corner"},
                        {"value": "Centra",         "label": "Centra"},
                        {"value": "Fuel & Go",      "label": "Fuel & Go"},
                        {"value": "QuickMart",      "label": "QuickMart"},
                        {"value": "Acme Online",    "label": "Acme Online"},
                    ],
                },
                {
                    "name": "card_last_numbers",
                    "label": "Card Last 4 Digits",
                    "type": "text",
                    "default": "1234",
                    "required": False,
                    "placeholder": "e.g. 1234",
                },
            ],
        },
        {
            "id": "get_undelivered",
            "name": "Get undelivered notifications",
            "category": "Notifications",
            "method": "GET",
            "description": (
                "Retrieve transaction notifications that Mastercard was unable to "
                "deliver to your webhook (after up to 24 hours of retries)."
            ),
            "params": [
                {
                    "name": "page_number",
                    "label": "Page",
                    "type": "select",
                    "default": "1",
                    "required": False,
                    "options": [
                        {"value": "1", "label": "1"},
                        {"value": "2", "label": "2"},
                        {"value": "3", "label": "3"},
                    ],
                },
                {
                    "name": "page_size",
                    "label": "Page size",
                    "type": "select",
                    "default": "10",
                    "required": False,
                    "options": [
                        {"value": "10", "label": "10"},
                        {"value": "25", "label": "25"},
                        {"value": "50", "label": "50"},
                    ],
                },
            ],
        },
    ],
}


def _base_url() -> str:
    from simulator.switcher import sim_base_url
    env = os.environ.get("TRANSACTION_NOTIFICATIONS_ENV", "sandbox").lower()
    real = _PROD_BASE_URL if env == "production" else _SANDBOX_BASE_URL
    return sim_base_url("transaction_notifications", real)


def _configured() -> bool:
    key = os.environ.get("TRANSACTION_NOTIFICATIONS_CONSUMER_KEY", "")
    path = os.environ.get("TRANSACTION_NOTIFICATIONS_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return _configured() or is_simulated("transaction_notifications")


def get_state() -> Dict[str, Any]:
    return {"configured": _configured(), **STATE}


def _consent_base_url() -> str:
    from simulator.switcher import sim_base_url
    env = os.environ.get("TRANSACTION_NOTIFICATIONS_ENV", "sandbox").lower()
    real = _CONSENT_PROD_BASE_URL if env == "production" else _CONSENT_SANDBOX_BASE_URL
    # Route through the consent_management simulator handler when simulated.
    return sim_base_url("consent_management", real)


def _is_consent_simulated() -> bool:
    from simulator.switcher import is_simulated
    return is_simulated("consent_management") or is_simulated("transaction_notifications")


def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if op_id == "trigger_test_transaction":
        return _trigger_test_transaction(params)
    if op_id == "get_undelivered":
        return _get_undelivered(params)
    if op_id == "create_consent":
        return _create_consent(params)
    if op_id == "get_consents":
        return _get_consents(params)
    if op_id == "start_authentication":
        return _start_authentication(params)
    if op_id == "verify_authentication":
        return _verify_authentication(params)
    if op_id == "delete_consents":
        return _delete_consents(params)
    if op_id == "delete_single_consent":
        return _delete_single_consent(params)
    return {"success": False, "error": f"Unknown operation: {op_id}"}


def _get_auth_header(url: str, method: str, body_str: str | None = None):
    """Build an OAuth 1.0a Authorization header."""
    import oauth1.authenticationutils as authutils
    from oauth1.oauth import OAuth

    consumer_key = os.environ["TRANSACTION_NOTIFICATIONS_CONSUMER_KEY"]
    key_path     = os.environ["TRANSACTION_NOTIFICATIONS_SIGNING_KEY_PATH"]
    key_password = os.environ.get("TRANSACTION_NOTIFICATIONS_SIGNING_KEY_PASSWORD", "keystorepassword")

    if not os.path.isabs(key_path):
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        key_path = os.path.join(project_root, key_path)

    signing_key = authutils.load_signing_key(key_path, key_password)
    return OAuth.get_authorization_header(url, method, body_str, consumer_key, signing_key)


def _not_configured_error(op: str) -> Dict[str, Any]:
    return {
        "success": False,
        "error": (
            f"Transaction Notifications is not configured. "
            f"Set TRANSACTION_NOTIFICATIONS_CONSUMER_KEY and TRANSACTION_NOTIFICATIONS_SIGNING_KEY_PATH in .env, "
            f"then restart the server."
        ),
    }


def _trigger_test_transaction(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("transaction_notifications"):
        return _not_configured_error("trigger_test_transaction")

    card_reference = (params.get("card_reference") or "").strip()

    def _latest_consent_card_ref() -> str:
        return str(STATE.get("card_ref") or "").strip()

    latest_card_ref = _latest_consent_card_ref()
    if not card_reference and latest_card_ref:
        card_reference = latest_card_ref

    if not card_reference:
        return {"success": False, "error": "card_reference is required"}

    amount_str = params.get("amount", "9.99")
    try:
        amount = float(amount_str)
    except (ValueError, TypeError):
        amount = 9.99

    currency     = (params.get("currency") or "USD").strip()
    merchant     = (params.get("merchant_name") or "Coffee Corner").strip()
    last_numbers_str = (params.get("card_last_numbers") or "1234").strip()

    url = f"{_base_url()}/notifications/transactions"
    body = {
        "cardholderAmount": amount,
        "cardholderCurrency": currency,
        "cardReference": card_reference,
        "cardLastNumbers": last_numbers_str,
        "merchantName": merchant,
    }
    body_str = json.dumps(body)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    import requests

    if is_simulated("transaction_notifications"):
        headers["Authorization"] = "Simulated"
    else:
        try:
            headers["Authorization"] = _get_auth_header(url, "POST", body_str)
        except Exception as e:
            return {"success": False, "error": f"OAuth signing failed: {e}"}

    try:
        resp = requests.post(url, data=body_str, headers=headers, timeout=15)
        status_code = resp.status_code
        try:
            resp_body = resp.json()
        except Exception:
            resp_body = {"raw": resp.text} if resp.text else {}
    except Exception as e:
        return {"success": False, "error": f"Request failed: {e}"}

    success = 200 <= status_code < 300
    result = {
        "success": success,
        "data": resp_body if success else {},
        "error": None if success else resp_body,
        "request": {
            "method": "POST",
            "url": url,
            "body": body,
        },
        "response": {
            "status_code": status_code,
            "body": resp_body,
        },
        "state_updates": {},
    }

    # Provide actionable guidance for the common enrollment mismatch error.
    if not success:
        err_blob = json.dumps(resp_body).lower() if isinstance(resp_body, (dict, list)) else str(resp_body).lower()
        if "could not find a card for that reference" in err_blob:
            hints = result.setdefault("hints", {})
            hints["note"] = (
                "Card reference not found by Transaction Notifications. "
                "Use the latest cardReference from Consent Management in the same project/account."
            )
            if latest_card_ref:
                hints["next_step"] = (
                    "Try this card_reference from the latest Consent flow: "
                    f"{latest_card_ref}"
                )

    return result


def _get_undelivered(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("transaction_notifications"):
        return _not_configured_error("get_undelivered")

    page_number = params.get("page_number", "1")
    page_size   = params.get("page_size", "10")
    url = f"{_base_url()}/undelivered-notifications?pageNumber={page_number}&pageSize={page_size}"

    headers = {
        "Accept": "application/json",
    }

    import requests

    if is_simulated("transaction_notifications"):
        headers["Authorization"] = "Simulated"
    else:
        try:
            headers["Authorization"] = _get_auth_header(url, "GET", None)
        except Exception as e:
            return {"success": False, "error": f"OAuth signing failed: {e}"}

    try:
        resp = requests.get(url, headers=headers, timeout=15)
        status_code = resp.status_code
        try:
            resp_body = resp.json()
        except Exception:
            resp_body = {"raw": resp.text} if resp.text else {}
    except Exception as e:
        return {"success": False, "error": f"Request failed: {e}"}

    success = 200 <= status_code < 300
    return {
        "success": success,
        "data": resp_body if success else {},
        "error": None if success else resp_body,
        "request": {
            "method": "GET",
            "url": url,
        },
        "response": {
            "status_code": status_code,
            "body": resp_body,
        },
        "state_updates": {},
    }


# ---------------------------------------------------------------------------
# Consent management helpers (same project, same credentials)
# ---------------------------------------------------------------------------

def _resolve_cert_path() -> str | None:
    """Return the absolute encryption-cert path if configured and exists, else None."""
    cert_path = os.environ.get("TRANSACTION_NOTIFICATIONS_ENCRYPTION_KEY_PATH", "").strip()
    if not cert_path or cert_path == "your-encryption-cert.pem":
        # Migration fallback: accept the old per-module env var.
        cert_path = os.environ.get("CONSENT_MANAGEMENT_ENCRYPTION_KEY_PATH", "").strip()
    if not cert_path or cert_path == "your-encryption-cert.pem":
        return None
    if not os.path.isabs(cert_path):
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        cert_path = os.path.join(project_root, cert_path)
    return cert_path if os.path.exists(cert_path) else None


def _encrypt_body(body: Dict, cert_path: str) -> str:
    from client_encryption.jwe_encryption_config import JweEncryptionConfig
    from client_encryption.jwe_encryption import encrypt_payload
    config = JweEncryptionConfig({
        "paths": {
            "$": {
                "toEncrypt": {"$": "$"},
                "toDecrypt": {},
            }
        },
        "encryptedValueFieldName": "jweEncryptedData",
        "encryptionCertificate":   cert_path,
    })
    encrypted = encrypt_payload(json.dumps(body), config)
    return json.dumps(encrypted)


def _consent_http(method: str, url: str, body: Dict | None = None,
                  _body_str: str | None = None) -> Dict[str, Any]:
    """Execute a signed OAuth 1.0a request against the consent API."""
    import requests

    if _body_str is not None:
        body_str = _body_str
    elif body is not None:
        body_str = json.dumps(body)
    else:
        body_str = None

    headers = {"Accept": "application/json"}
    if body_str is not None:
        headers["Content-Type"] = "application/json"

    if _is_consent_simulated():
        headers["Authorization"] = "Simulated"
    else:
        try:
            headers["Authorization"] = _get_auth_header(url, method, body_str)
        except Exception as e:
            return {"success": False, "error": f"OAuth signing failed: {e}"}

    try:
        resp = requests.request(method, url, data=body_str, headers=headers, timeout=15)
        status_code = resp.status_code
        try:
            resp_body = resp.json()
        except Exception:
            resp_body = {"raw": resp.text} if resp.text else {}
    except Exception as e:
        return {"success": False, "error": f"Request failed: {e}"}

    success = 200 <= status_code < 300
    return {
        "success":  success,
        "data":     resp_body if success else {},
        "error":    None if success else resp_body,
        "request":  {"method": method, "url": url, "body": body},
        "response": {"body": resp_body, "status_code": status_code},
    }


def _consent_http_encrypted(method: str, url: str, body: Dict) -> Dict[str, Any]:
    if _is_consent_simulated():
        return _consent_http(method, url, body)
    cert_path = _resolve_cert_path()
    if cert_path:
        try:
            encrypted_str = _encrypt_body(body, cert_path)
            return _consent_http(method, url, body=body, _body_str=encrypted_str)
        except Exception as e:
            return {"success": False, "error": f"JWE encryption failed: {e}"}
    return _consent_http(method, url, body)


def _consent_not_configured_error() -> Dict[str, Any]:
    return {
        "success": False,
        "error": (
            "Transaction Notifications is not configured. "
            "Set TRANSACTION_NOTIFICATIONS_CONSUMER_KEY and "
            "TRANSACTION_NOTIFICATIONS_SIGNING_KEY_PATH in config/.env, "
            "then restart the server."
        ),
    }


def _create_consent(params: Dict[str, Any]) -> Dict[str, Any]:
    if not _configured() and not _is_consent_simulated():
        return _consent_not_configured_error()

    pan = (params.get("pan") or "").strip()
    if not pan:
        return {"success": False, "error": "pan is required"}

    try:
        expiry_month = int(params.get("expiry_month", 1))
        expiry_year  = int(params.get("expiry_year", 2025))
    except (ValueError, TypeError):
        return {"success": False, "error": "expiry_month and expiry_year must be integers"}

    cvc             = (params.get("cvc") or "").strip() or None
    cardholder_name = (params.get("cardholder_name") or "").strip() or None
    consent_name    = (params.get("consent_name") or "notification").strip()

    card_details: Dict[str, Any] = {
        "pan":         pan,
        "expiryMonth": expiry_month,
        "expiryYear":  expiry_year,
    }
    if cvc:
        card_details["cvc"] = cvc
    if cardholder_name:
        card_details["cardholderName"] = cardholder_name

    body = {
        "consents":    [{"name": consent_name}],
        "cardDetails": card_details,
    }

    url = f"{_consent_base_url()}/consents"
    cert_path = _resolve_cert_path()
    if not cert_path and not _is_consent_simulated():
        return {
            "success": False,
            "error": (
                "Create Consent requires JWE payload encryption. "
                "Download the encryption certificate (PEM) from your Mastercard Developer "
                "project page (Client Encryption Keys section) and set "
                "TRANSACTION_NOTIFICATIONS_ENCRYPTION_KEY_PATH=/path/to/cert.pem in config/.env, "
                "then restart the server."
            ),
        }
    try:
        if cert_path:
            encrypted_str = _encrypt_body(body, cert_path)
            result = _consent_http("POST", url, body=body, _body_str=encrypted_str)
        else:
            result = _consent_http("POST", url, body=body)

        if result["success"]:
            card_ref = result["data"].get("cardReference", "")
            STATE["card_ref"] = card_ref
            consents = result["data"].get("consents", [])
            if consents:
                STATE["consent_id"] = str(consents[0].get("id", ""))
            STATE["verify_auth_params"] = "{}"
            result["state_updates"] = {
                "card_ref":           STATE["card_ref"],
                "consent_id":         STATE["consent_id"],
                "verify_auth_params": STATE["verify_auth_params"],
            }
            auth_obj    = result["data"].get("auth", {}) or {}
            auth_params = auth_obj.get("params", {}) or {}
            method_url  = auth_params.get("threeDsMethodUrl", "")
            method_data = auth_params.get("threeDSMethodData", "")
            trans_id    = auth_params.get("threeDSServerTransID", "")
            method_notify = (
                auth_params.get("threeDSMethodNotificationURL", "")
                or auth_params.get("threeDsMethodNotificationURL", "")
                or auth_params.get("threeDsMethodNotificationUrl", "")
            )
            if STATE["card_ref"]:
                from urllib.parse import urlencode
                q: Dict[str, str] = {"card_ref": STATE["card_ref"]}
                if method_url:    q["method_url"]    = method_url
                if method_data:   q["method_data"]   = method_data
                if trans_id:      q["trans_id"]      = trans_id
                if method_notify: q["method_notify"] = method_notify
                launch_path = "/explorer/consent/3ds-flow?" + urlencode(q)
                result["hints"] = {
                    "browser_launch_url": launch_path,
                    "browser_launch_note": (
                        "Click Launch to run the 3DS Method (device fingerprint) "
                        "and complete authentication in your browser."
                    ),
                }
        return result
    except Exception as e:
        return {"success": False, "error": f"JWE encryption failed: {e}"}


def _get_consents(params: Dict[str, Any]) -> Dict[str, Any]:
    if not _configured() and not _is_consent_simulated():
        return _consent_not_configured_error()
    card_ref = (params.get("card_ref") or "").strip()
    if not card_ref:
        return {"success": False, "error": "card_ref is required"}
    url = f"{_consent_base_url()}/consents/{card_ref}"
    result = _consent_http("GET", url)
    if result["success"]:
        consents = result["data"].get("consents", [])
        if consents:
            STATE["consent_id"] = str(consents[0].get("id", ""))
            result["state_updates"] = {"consent_id": STATE["consent_id"]}
    return result


def _start_authentication(params: Dict[str, Any]) -> Dict[str, Any]:
    if not _configured() and not _is_consent_simulated():
        return _consent_not_configured_error()

    card_ref  = (params.get("card_ref") or "").strip()
    auth_type = (params.get("auth_type") or "THREEDS").strip()
    if not card_ref:
        return {"success": False, "error": "card_ref is required"}

    auth_params_str = (params.get("auth_params") or "").strip()
    if auth_params_str:
        try:
            auth_params = json.loads(auth_params_str)
        except json.JSONDecodeError:
            return {"success": False, "error": "auth_params must be valid JSON"}
    else:
        auth_params = {}

    for k in (
        "fingerprintStatus", "challengeWindowSize",
        "browserAcceptHeader", "browserColorDepth", "browserJavaEnabled",
        "browserLanguage", "browserScreenHeight", "browserScreenWidth",
        "browserTZ", "browserUserAgent",
    ):
        if k in params and params[k] not in (None, ""):
            auth_params[k] = params[k]

    if auth_type.upper() == "THREEDS":
        auth_params.setdefault("fingerprintStatus", "complete")
        auth_params.setdefault("challengeWindowSize", "04")
        auth_params.setdefault(
            "browserAcceptHeader",
            "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        )
        auth_params.setdefault("browserColorDepth", "24")
        auth_params.setdefault("browserJavaEnabled", False)
        auth_params.setdefault("browserLanguage", "en-US")
        auth_params.setdefault("browserScreenHeight", "1080")
        auth_params.setdefault("browserScreenWidth", "1920")
        auth_params.setdefault("browserTZ", "0")
        auth_params.setdefault("browserUserAgent", "Mozilla/5.0")

    body = {"auth": {"type": auth_type, "params": auth_params}}
    url  = f"{_consent_base_url()}/consents/{card_ref}/start-authentication"
    result = _consent_http_encrypted("POST", url, body)

    if result.get("success"):
        auth_obj = (result.get("data") or {}).get("auth") or {}
        returned_params = auth_obj.get("params") if isinstance(auth_obj.get("params"), dict) else {}
        verify_subset = {}
        for key in (
            "authenticationValue", "eci", "cavv", "xid", "transStatus",
            "dsTransId", "directoryServerTransactionId", "threeDSServerTransID",
        ):
            val = returned_params.get(key)
            if val not in (None, ""):
                verify_subset[key] = val
        STATE["verify_auth_params"] = json.dumps(verify_subset or {}, separators=(",", ":"))
        result.setdefault("state_updates", {})["verify_auth_params"] = STATE["verify_auth_params"]

    try:
        errs = (result.get("response", {}).get("body", {}) or {}).get("Errors", {})
        codes = [e.get("reasonCode") for e in (errs.get("Error") or [])]
        if "invalid.auth.state" in codes:
            result.setdefault("hints", {})["next_step"] = (
                "This consent is no longer in PENDING_AUTHENTICATION. "
                "Run delete_consents and create_consent again to start a fresh 3DS flow."
            )
    except Exception:
        pass
    return result


def _verify_authentication(params: Dict[str, Any]) -> Dict[str, Any]:
    if not _configured() and not _is_consent_simulated():
        return _consent_not_configured_error()

    card_ref  = (params.get("card_ref") or "").strip()
    auth_type = (params.get("auth_type") or "THREEDS").strip()
    if not card_ref:
        return {"success": False, "error": "card_ref is required"}

    auth_params_raw = params.get("auth_params")
    auth_params_str = str(auth_params_raw).strip() if auth_params_raw is not None else ""
    auth_params_source = "explicit-input"

    state_auth_params = str(STATE.get("verify_auth_params") or "{}").strip()
    if (not auth_params_str or auth_params_str == "{}") and state_auth_params and state_auth_params != "{}":
        auth_params_str = state_auth_params
        auth_params_source = "state-fallback"
    elif not auth_params_str:
        auth_params_str = "{}"
        auth_params_source = "default-empty"
    elif auth_params_str == "{}":
        auth_params_source = "explicit-empty"

    try:
        auth_params = json.loads(auth_params_str)
    except json.JSONDecodeError:
        return {"success": False, "error": "auth_params must be valid JSON"}

    if not isinstance(auth_params, dict):
        return {"success": False, "error": "auth_params must be a JSON object"}

    for k in (
        "authenticationValue", "eci", "cavv", "xid", "transStatus",
        "dsTransId", "directoryServerTransactionId", "threeDSServerTransID",
    ):
        if k in params and params[k] not in (None, ""):
            auth_params[k] = params[k]

    body   = {"auth": {"type": auth_type, "params": auth_params}}
    url    = f"{_consent_base_url()}/consents/{card_ref}/verify-authentication"
    result = _consent_http_encrypted("POST", url, body)

    source_label = {
        "explicit-input": "verify used auth_params from your input",
        "explicit-empty": "verify used explicit empty auth_params {}",
        "default-empty":  "verify used default empty auth_params {}",
        "state-fallback": "verify auto-filled auth_params from Start Authentication state",
    }.get(auth_params_source, auth_params_source)
    result.setdefault("hints", {})["note"] = source_label

    if result.get("success"):
        STATE["verify_auth_params"] = json.dumps(auth_params, separators=(",", ":"))
        result.setdefault("state_updates", {})["verify_auth_params"] = STATE["verify_auth_params"]
    return result


def _delete_consents(params: Dict[str, Any]) -> Dict[str, Any]:
    if not _configured() and not _is_consent_simulated():
        return _consent_not_configured_error()
    card_ref = (params.get("card_ref") or "").strip()
    if not card_ref:
        return {"success": False, "error": "card_ref is required"}
    url = f"{_consent_base_url()}/consents/{card_ref}"
    return _consent_http("DELETE", url)


def _delete_single_consent(params: Dict[str, Any]) -> Dict[str, Any]:
    if not _configured() and not _is_consent_simulated():
        return _consent_not_configured_error()
    card_ref   = (params.get("card_ref") or "").strip()
    consent_id = (params.get("consent_id") or "").strip()
    if not card_ref:
        return {"success": False, "error": "card_ref is required"}
    if not consent_id:
        return {"success": False, "error": "consent_id is required"}
    url = f"{_consent_base_url()}/consents/{card_ref}/consents/{consent_id}"
    return _consent_http("DELETE", url)
