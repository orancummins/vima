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
from typing import Any

_SANDBOX_BASE_URL = "https://sandbox.api.mastercard.com/openapis"
_PROD_BASE_URL    = "https://api.mastercard.com/openapis"

MANIFEST: dict[str, Any] = {
    "id": "txnotify",
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
    ),
    "categories": ["Notifications"],
    "state_schema": [],
    "configured": bool(
        os.environ.get("TXNOTIFY_CONSUMER_KEY")
        and os.environ.get("TXNOTIFY_CONSUMER_KEY") != "your-consumer-key-here"
        and os.environ.get("TXNOTIFY_SIGNING_KEY_PATH")
    ),
    "operations": [
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
                    "help": "UUID returned by the Consent API when a card is enrolled.",
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
    env = os.environ.get("TXNOTIFY_ENV", "sandbox").lower()
    return _PROD_BASE_URL if env == "production" else _SANDBOX_BASE_URL


def _configured() -> bool:
    key = os.environ.get("TXNOTIFY_CONSUMER_KEY", "")
    path = os.environ.get("TXNOTIFY_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    return _configured()


def get_state() -> dict[str, Any]:
    return {"configured": _configured()}


def execute(op_id: str, params: dict[str, Any]) -> dict[str, Any]:
    if op_id == "trigger_test_transaction":
        return _trigger_test_transaction(params)
    if op_id == "get_undelivered":
        return _get_undelivered(params)
    return {"success": False, "error": f"Unknown operation: {op_id}"}


def _get_auth_header(url: str, method: str, body_str: str | None = None):
    """Build an OAuth 1.0a Authorization header."""
    import oauth1.authenticationutils as authutils
    from oauth1.oauth import OAuth

    consumer_key = os.environ["TXNOTIFY_CONSUMER_KEY"]
    key_path     = os.environ["TXNOTIFY_SIGNING_KEY_PATH"]
    key_password = os.environ.get("TXNOTIFY_SIGNING_KEY_PASSWORD", "keystorepassword")

    if not os.path.isabs(key_path):
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        key_path = os.path.join(project_root, key_path)

    signing_key = authutils.load_signing_key(key_path, key_password)
    return OAuth.get_authorization_header(url, method, body_str, consumer_key, signing_key)


def _not_configured_error(op: str) -> dict[str, Any]:
    return {
        "success": False,
        "error": (
            "Transaction Notifications is not configured. "
            "Set TXNOTIFY_CONSUMER_KEY and TXNOTIFY_SIGNING_KEY_PATH in .env, "
            "then restart the server."
        ),
    }


def _trigger_test_transaction(params: dict[str, Any]) -> dict[str, Any]:
    if not _configured():
        return _not_configured_error("trigger_test_transaction")

    card_reference = (params.get("card_reference") or "").strip()
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
    try:
        last_numbers = int(last_numbers_str)
    except (ValueError, TypeError):
        last_numbers = 1234

    url = f"{_base_url()}/notifications/transactions"
    body = {
        "cardholderAmount": amount,
        "cardholderCurrency": currency,
        "cardReference": card_reference,
        "cardLastNumbers": last_numbers,
        "merchantName": merchant,
    }
    body_str = json.dumps(body)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    import requests

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
    return {
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


def _get_undelivered(params: dict[str, Any]) -> dict[str, Any]:
    if not _configured():
        return _not_configured_error("get_undelivered")

    page_number = params.get("page_number", "1")
    page_size   = params.get("page_size", "10")
    url = f"{_base_url()}/undelivered-notifications?pageNumber={page_number}&pageSize={page_size}"

    headers = {
        "Accept": "application/json",
    }

    import requests

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
