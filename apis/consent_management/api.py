"""Consent Management API — OAuth 1.0a.

Sandbox base URL: https://sandbox.api.mastercard.com/openapis/authentication

Key endpoints:
  POST   /consents                                        — create a consent (requires JWE payload encryption in production)
  GET    /consents/{card_ref}                             — get consents for a card
  POST   /consents/{card_ref}/start-authentication       — start 3DS authentication
  POST   /consents/{card_ref}/verify-authentication      — verify 3DS authentication result
  DELETE /consents/{card_ref}                            — delete all consents for a card
  DELETE /consents/{card_ref}/consents/{consent_id}      — delete a single consent

Auth: OAuth 1.0a (Mastercard signing library).
Note: POST endpoints that accept card details (PAN) require JWE payload encryption.
      In sandbox the test PAN 2303779951000297 can be used without full encryption.

Docs:
  https://developer.mastercard.com/consent-management/documentation/
  https://developer.mastercard.com/consent-management/documentation/api-reference/
"""
from __future__ import annotations

import os
from typing import Any

_SANDBOX_BASE_URL = "https://sandbox.api.mastercard.com/openapis/authentication"
_PROD_BASE_URL    = "https://api.mastercard.com/openapis/authentication"

# In-process sticky state — now proxied from transaction_notifications so both
# modules share the same card_ref/consent_id lifecycle.
try:
    from apis.transaction_notifications.api import STATE, _CONSENT_OPERATIONS  # noqa: F401, I001
except Exception:
    STATE: dict[str, Any] = {
        "card_ref":           "",
        "consent_id":        "",
        "verify_auth_params": "{}",
    }
    _CONSENT_OPERATIONS: list = []

MANIFEST: dict[str, Any] = {
    "id": "consent_management",
    "name": "Consent Management",
    "description": (
        "Mastercard Consent Management — securely capture, manage, and verify "
        "cardholder consent for data-sharing use cases such as Transaction "
        "Notifications. Supports card-based enrollment with optional 3DS authentication."
    ),
    "docs_url": "https://developer.mastercard.com/consent-management/documentation/",
    "how_to": (
        "<p><strong>Consent Management</strong> enables partners to capture explicit, "
        "traceable cardholder consent before accessing card transaction data.</p>"
        "<h3>Card enrollment flow</h3>"
        "<ol>"
        "<li><strong>Create Consent</strong> — POST /consents with the cardholder's PAN "
        "and expiry details. The response contains a <code>cardReference</code> (UUID) "
        "and an <code>auth</code> object indicating whether authentication is required "
        "(e.g. THREEDS or ASI). Use the <strong>Launch 3DS Method</strong> button shown "
        "at the top of the hint area to run the browser flow.</li>"
        "<li><strong>Complete browser 3DS flow</strong> — fingerprint runs first, then "
        "challenge only if required.</li>"
        "<li><strong>Start Authentication</strong> — call "
        "POST /consents/{card_ref}/start-authentication after the browser flow.</li>"
        "<li><strong>Verify Authentication</strong> — call "
        "POST /consents/{card_ref}/verify-authentication to complete enrollment.</li>"
        "<li><strong>Get Consents</strong> — retrieve all consents and their statuses "
        "for a card reference. Status <code>APPROVED</code> means the card is enrolled.</li>"
        "<li>Store the <code>cardReference</code> and use it with the "
        "<a href='#txnotify'>Transaction Notifications API</a> to receive real-time alerts.</li>"
        "</ol>"
        "<h3>Troubleshooting</h3>"
        "<ul>"
        "<li>If Verify Authentication fails after a successful launch, ensure you used "
        "the same <code>cardReference</code> and ran Start Authentication first.</li>"
        "<li>If auth state is invalid, delete consents for that card and restart from "
        "Create Consent.</li>"
        "</ul>"
        "<h3>Sandbox notes</h3>"
        "<ul>"
        "<li>Use test PAN <code>2303779951000297</code> (any future expiry, CVC 123) for sandbox testing.</li>"
        "<li>POST /consents requires JWE payload encryption for live card data. "
        "In sandbox the test PAN works without full encryption.</li>"
        "<li>The <code>cardReference</code> from this API is used as the "
        "<code>card_reference</code> input for Transaction Notifications.</li>"
        "</ul>"
    ),
    "categories": ["Consent"],
    "state_schema": [
        {"key": "card_ref",   "label": "Card Reference"},
        {"key": "consent_id", "label": "Consent ID"},
        {"key": "verify_auth_params", "label": "Verify Auth Params (JSON)"},
    ],
    "configured": bool(
        os.environ.get("TRANSACTION_NOTIFICATIONS_CONSUMER_KEY")
        and os.environ.get("TRANSACTION_NOTIFICATIONS_CONSUMER_KEY") != "your-consumer-key-here"
        and os.environ.get("TRANSACTION_NOTIFICATIONS_SIGNING_KEY_PATH")
    ),
    # Defined once in transaction_notifications (same credentials / endpoints).
    # Imported at the top of this module to avoid duplicating ~300 lines.
    "operations": _CONSENT_OPERATIONS,
}


def _base_url() -> str:
    from simulator.switcher import sim_base_url
    env = os.environ.get("TRANSACTION_NOTIFICATIONS_ENV", "sandbox").lower()
    real = _PROD_BASE_URL if env == "production" else _SANDBOX_BASE_URL
    return sim_base_url("consent_management", real)


def _configured() -> bool:
    key  = os.environ.get("TRANSACTION_NOTIFICATIONS_CONSUMER_KEY", "")
    path = os.environ.get("TRANSACTION_NOTIFICATIONS_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return _configured() or is_simulated("consent_management")


def get_state() -> dict[str, Any]:
    return {"configured": _configured(), **STATE}


def execute(op_id: str, params: dict[str, Any]) -> dict[str, Any]:
    # All consent operations are implemented in transaction_notifications since
    # both APIs share the same credentials, endpoint base URL and STATE.
    # Delegating avoids maintaining a duplicate ~350-line implementation here.
    import apis.transaction_notifications.api as _txnotif
    _handlers: dict[str, Any] = {
        "create_consent":        _txnotif._create_consent,
        "get_consents":          _txnotif._get_consents,
        "start_authentication":  _txnotif._start_authentication,
        "verify_authentication": _txnotif._verify_authentication,
        "delete_consents":       _txnotif._delete_consents,
        "delete_single_consent": _txnotif._delete_single_consent,
    }
    handler = _handlers.get(op_id)
    if handler:
        return handler(params)
    return {"success": False, "error": f"Unknown operation: {op_id}"}
