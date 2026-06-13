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

import json
import os
from typing import Any, Dict

_SANDBOX_BASE_URL = "https://sandbox.api.mastercard.com/openapis/authentication"
_PROD_BASE_URL    = "https://api.mastercard.com/openapis/authentication"

# In-process sticky state — now proxied from transaction_notifications so both
# modules share the same card_ref/consent_id lifecycle.
try:
    from apis.transaction_notifications.api import STATE  # noqa: F401
except Exception:
    STATE: Dict[str, Any] = {
        "card_ref":           "",
        "consent_id":        "",
        "verify_auth_params": "{}",
    }

MANIFEST: Dict[str, Any] = {
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
    "operations": [
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
                "complete the 3DS Method in your browser, "
                "then call Start Authentication."
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
                "If no challenge is required, status can return AUTHENTICATED immediately. "
                "If challenge is required, this returns challenge parameters."
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
                        "EMV 3DS browser params from the fingerprint step. "
                        "fingerprintStatus must be one of complete/timeout/unavailable. "
                        "The sandbox requires the full browser info set (user agent, screen "
                        "size, timezone, etc). Normally this is filled automatically by the "
                        "3DS Flow browser page launched from Create Consent — only edit this "
                        "if calling start-authentication directly without that page."
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
                "Supports smart defaulting: if auth_params is left empty, the API will "
                "use available state from prior 3DS steps where possible."
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
                    "help": (
                        "Additional authentication parameters from the 3DS flow as a JSON object. "
                        "Auto-populated from Start Authentication when available. "
                        "For Mastercard 3DS, leaving this as {} is typically valid."
                    ),
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
                "Revoke and delete a specific consent (by consent ID) for a card reference. "
                "Other consents on the same card remain active."
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
    ],
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


def get_state() -> Dict[str, Any]:
    return {"configured": _configured(), **STATE}


def _get_auth_header(url: str, method: str, body_str: str | None = None) -> str:
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


def _not_configured_error() -> Dict[str, Any]:
    return {
        "success": False,
        "error": (
            "Transaction Notifications is not configured. "
            "Set TRANSACTION_NOTIFICATIONS_CONSUMER_KEY and TRANSACTION_NOTIFICATIONS_SIGNING_KEY_PATH in config/.env, "
            "then restart the server."
        ),
    }


def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
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


def _encrypt_body(body: Dict, cert_path: str) -> str:
    """JWE-encrypt the request body using the Mastercard JWE encryption library."""
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


def _http(method: str, url: str, body: Dict | None = None, _body_str: str | None = None) -> Dict[str, Any]:
    """Execute a signed OAuth 1.0a HTTP request and return a result envelope.

    Pass ``_body_str`` to use a pre-serialized (e.g. JWE-encrypted) body string
    instead of JSON-encoding ``body``.  OAuth is always signed over the wire body.
    """
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

    from simulator.switcher import is_simulated
    if is_simulated("consent_management"):
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
        "success":    success,
        "data":       resp_body if success else {},
        "error":      None if success else resp_body,
        "request":    {"method": method, "url": url, "body": body},
        "response":   {"body": resp_body, "status_code": status_code},
    }


def _create_consent(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("consent_management"):
        return _not_configured_error()

    pan  = (params.get("pan") or "").strip()
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

    url = f"{_base_url()}/consents"
    cert_path = _resolve_cert_path()
    if not cert_path and not is_simulated("consent_management"):
        return {
            "success": False,
            "error": (
                "Create Consent requires JWE payload encryption. "
                "Download the encryption certificate (PEM) from your Mastercard Developer "
                "project page (Client Encryption Keys section) and set "
                "CONSENT_MANAGEMENT_ENCRYPTION_KEY_PATH=/path/to/cert.pem in .env, then restart."
            ),
        }
    try:
        if cert_path:
            encrypted_str = _encrypt_body(body, cert_path)
            result = _http("POST", url, body=body, _body_str=encrypted_str)
        else:
            result = _http("POST", url, body=body)
        if result["success"]:
            card_ref = result["data"].get("cardReference", "")
            STATE["card_ref"] = card_ref
            consents = result["data"].get("consents", [])
            if consents:
                STATE["consent_id"] = str(consents[0].get("id", ""))
            # Start each enrollment from a clean verify payload to avoid stale values.
            STATE["verify_auth_params"] = "{}"
            result["state_updates"] = {
                "card_ref": STATE["card_ref"],
                "consent_id": STATE["consent_id"],
                "verify_auth_params": STATE["verify_auth_params"],
            }
            # Build 3DS Method launch hint — the new flow page runs fingerprint,
            # start-authentication (with browser params), challenge iframe and
            # verify-authentication all in one browser tab.
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
                q = {"card_ref": STATE["card_ref"]}
                if method_url:  q["method_url"]  = method_url
                if method_data: q["method_data"] = method_data
                if trans_id:    q["trans_id"]    = trans_id
                if method_notify: q["method_notify"] = method_notify
                launch_path = "/explorer/consent/3ds-flow?" + urlencode(q)
                result["hints"] = {
                    "browser_launch_url": launch_path,
                    "browser_launch_note": (
                        "Click Launch to run the 3DS Method (device fingerprint) "
                        "and complete authentication in your browser. The page "
                        "will handle frictionless and challenge flows automatically."
                    ),
                }
        return result
    except Exception as e:
        return {"success": False, "error": f"JWE encryption failed: {e}"}


def _get_consents(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("consent_management"):
        return _not_configured_error()

    card_ref = (params.get("card_ref") or "").strip()
    if not card_ref:
        return {"success": False, "error": "card_ref is required"}

    url = f"{_base_url()}/consents/{card_ref}"
    result = _http("GET", url)
    if result["success"]:
        consents = result["data"].get("consents", [])
        if consents:
            STATE["consent_id"] = str(consents[0].get("id", ""))
            result["state_updates"] = {"consent_id": STATE["consent_id"]}
    return result


def _resolve_cert_path() -> str | None:
    """Return the absolute cert path if configured and exists, else None."""
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


def _http_encrypted(method: str, url: str, body: Dict) -> Dict[str, Any]:
    """POST/PUT with JWE encryption if cert is configured, else plain JSON."""
    from simulator.switcher import is_simulated
    if is_simulated("consent_management"):
        return _http(method, url, body)
    cert_path = _resolve_cert_path()
    if cert_path:
        try:
            encrypted_str = _encrypt_body(body, cert_path)
            return _http(method, url, body=body, _body_str=encrypted_str)
        except Exception as e:
            return {"success": False, "error": f"JWE encryption failed: {e}"}
    return _http(method, url, body)


def _start_authentication(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("consent_management"):
        return _not_configured_error()

    card_ref  = (params.get("card_ref") or "").strip()
    auth_type = (params.get("auth_type") or "THREEDS").strip()
    if not card_ref:
        return {"success": False, "error": "card_ref is required"}

    # EMV 3DS browser params from the fingerprint step. The browser page that
    # runs the 3DS Method (hidden iframe) collects these and passes them in.
    auth_params_str = (params.get("auth_params") or "").strip()
    if auth_params_str:
        try:
            auth_params = json.loads(auth_params_str)
        except json.JSONDecodeError:
            return {"success": False, "error": "auth_params must be valid JSON"}
    else:
        auth_params = {}

    # If individual fields were passed instead of a JSON blob, accept them too.
    for k in (
        "fingerprintStatus", "challengeWindowSize",
        "browserAcceptHeader", "browserColorDepth", "browserJavaEnabled",
        "browserLanguage", "browserScreenHeight", "browserScreenWidth",
        "browserTZ", "browserUserAgent",
    ):
        if k in params and params[k] not in (None, ""):
            auth_params[k] = params[k]

    # Smart defaults for manual runs: Mastercard's 3DS tutorial shows these
    # browser fields are expected by start-authentication.
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
    url  = f"{_base_url()}/consents/{card_ref}/start-authentication"
    result = _http_encrypted("POST", url, body)

    if result.get("success"):
        auth_obj = (result.get("data") or {}).get("auth") or {}
        returned_params = auth_obj.get("params") if isinstance(auth_obj.get("params"), dict) else {}

        # Mastercard's reference verify step accepts an empty params object, but
        # some partner flows echo auth artifacts. Keep a best-effort subset ready.
        verify_subset = {}
        for key in (
            "authenticationValue", "eci", "cavv", "xid", "transStatus",
            "dsTransId", "directoryServerTransactionId", "threeDSServerTransID",
        ):
            val = returned_params.get(key)
            if val not in (None, ""):
                verify_subset[key] = val

        STATE["verify_auth_params"] = json.dumps(verify_subset or {}, separators=(",", ":"))
        updates = result.setdefault("state_updates", {})
        updates["verify_auth_params"] = STATE["verify_auth_params"]

    # Surface a friendlier hint when the consent has already completed auth.
    try:
        errs = (result.get("response", {}).get("body", {}) or {}).get("Errors", {})
        codes = [e.get("reasonCode") for e in (errs.get("Error") or [])]
        if "invalid.auth.state" in codes:
            result.setdefault("hints", {})["next_step"] = (
                "This consent is no longer in PENDING_AUTHENTICATION (it has likely "
                "already been authenticated or was abandoned). Run delete_consents "
                "for this card_ref and create_consent again to start a fresh 3DS flow."
            )
    except Exception:
        pass
    return result


def _verify_authentication(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("consent_management"):
        return _not_configured_error()

    card_ref  = (params.get("card_ref") or "").strip()
    auth_type = (params.get("auth_type") or "THREEDS").strip()
    if not card_ref:
        return {"success": False, "error": "card_ref is required"}

    auth_params_raw = params.get("auth_params")
    auth_params_str = str(auth_params_raw).strip() if auth_params_raw is not None else ""
    auth_params_source = "explicit-input"

    # Smart defaulting: use last start-authentication values only when the field
    # is blank or left at the default "{}".
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

    # Accept flattened inputs in case callers pass fields directly.
    for k in (
        "authenticationValue", "eci", "cavv", "xid", "transStatus",
        "dsTransId", "directoryServerTransactionId", "threeDSServerTransID",
    ):
        if k in params and params[k] not in (None, ""):
            auth_params[k] = params[k]

    body = {"auth": {"type": auth_type, "params": auth_params}}
    url  = f"{_base_url()}/consents/{card_ref}/verify-authentication"
    result = _http_encrypted("POST", url, body)

    source_label = {
        "explicit-input": "verify used auth_params from your input",
        "explicit-empty": "verify used explicit empty auth_params {}",
        "default-empty": "verify used default empty auth_params {}",
        "state-fallback": "verify auto-filled auth_params from Start Authentication state",
    }.get(auth_params_source, auth_params_source)
    result.setdefault("hints", {})["note"] = source_label

    if result.get("success"):
        # Keep the state strip and source-backed form in sync with what was sent.
        STATE["verify_auth_params"] = json.dumps(auth_params, separators=(",", ":"))
        updates = result.setdefault("state_updates", {})
        updates["verify_auth_params"] = STATE["verify_auth_params"]
    return result


def _delete_consents(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("consent_management"):
        return _not_configured_error()

    card_ref = (params.get("card_ref") or "").strip()
    if not card_ref:
        return {"success": False, "error": "card_ref is required"}

    url = f"{_base_url()}/consents/{card_ref}"
    return _http("DELETE", url)


def _delete_single_consent(params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("consent_management"):
        return _not_configured_error()

    card_ref   = (params.get("card_ref") or "").strip()
    consent_id = (params.get("consent_id") or "").strip()
    if not card_ref:
        return {"success": False, "error": "card_ref is required"}
    if not consent_id:
        return {"success": False, "error": "consent_id is required"}

    url = f"{_base_url()}/consents/{card_ref}/consents/{consent_id}"
    return _http("DELETE", url)
