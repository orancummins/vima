"""Mastercard Benefits Content Eligibility Service (BCES).

OAuth 1.0a one-legged, body-signed.

Sandbox test data (from Mastercard Testing page):
    cardNumber:    5291070000000000   (integer, mandatory)
    effectiveDate: YYYY-MM-DD          (optional)
    benefitCode:   CDW                 (optional)
    productCode:   DCG                 (optional)
    locale:        en-US               (optional)

Endpoint:
    POST /benefit-contents/searches

Docs: https://developer.mastercard.com/bces-service/documentation/
Spec: /bces-service/swagger/eligibility-with-content-specs.yaml
"""
from __future__ import annotations

import json
import os
import uuid
from typing import Any, Dict, List, Optional


_PROD_BASE    = "https://api.mastercard.com/loyalty/eligibility"
_SANDBOX_BASE = "https://sandbox.api.mastercard.com/loyalty/eligibility"


def _base() -> str:
    from simulator.switcher import sim_base_url
    real = _PROD_BASE if os.environ.get("BCES_ENV", "sandbox").lower() == "production" else _SANDBOX_BASE
    return sim_base_url("bces", real)


def _configured() -> bool:
    key  = os.environ.get("BCES_CONSUMER_KEY", "")
    path = os.environ.get("BCES_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return _configured() or is_simulated("bces")


def get_state() -> Dict[str, Any]:
    return {"configured": _configured()}


_CARD_OPTIONS = [
    {"value": "5291070000000000", "label": "5291070000000000 — Sandbox test PAN (BCES)"},
    {"value": "5341676355168133", "label": "5341676355168133 — Sandbox test PAN (Eligibility)"},
]

_LOCALE_OPTIONS = [
    {"value": "en-US", "label": "en-US — English (sandbox default)"},
    {"value": "es-ES", "label": "es-ES — Spanish"},
    {"value": "fr-FR", "label": "fr-FR — French"},
    {"value": "de-DE", "label": "de-DE — German"},
    {"value": "pt-BR", "label": "pt-BR — Portuguese (BR)"},
    {"value": "ja-JP", "label": "ja-JP — Japanese"},
]

_PRODUCT_CODE_OPTIONS = [
    {"value": "",    "label": "(none)"},
    {"value": "DCG", "label": "DCG — Sandbox test product"},
    {"value": "MST", "label": "MST — Standard"},
    {"value": "MWE", "label": "MWE — World Elite"},
]

_BENEFIT_CODE_OPTIONS = [
    {"value": "",    "label": "(any benefit)"},
    {"value": "CDW", "label": "CDW — Sandbox test benefit"},
]


_HOW_TO = (
    "<p><strong>Benefits Content Eligibility Service (BCES)</strong> returns "
    "rich renderable content (display names, descriptions, imagery, T&amp;Cs, "
    "FAQ + privacy URLs, CTA links) for the bundles &amp; benefits a card is "
    "eligible for.</p>"
    "<h3>Encryption requirement</h3>"
    "<p>BCES requires <strong>JWE field-level encryption</strong> of the request "
    "body (RSA-OAEP-256 + A256GCM). The whole plaintext body is encrypted and "
    "wrapped as <code>{\"encryptedValue\": \"&lt;JWE&gt;\"}</code>. You must "
    "download the BCES <em>Client Encryption</em> <code>.pem</code> from your "
    "Mastercard Developers project and set "
    "<code>BCES_ENCRYPTION_CERT_PATH</code> in <code>.env</code>.</p>"
    "<h3>Sandbox test data</h3>"
    "<ul>"
    "<li><code>cardNumber</code>: <code>5291070000000000</code> (mandatory, integer)</li>"
    "<li><code>benefitCode</code>: <code>CDW</code></li>"
    "<li><code>productCode</code>: <code>DCG</code></li>"
    "<li><code>locale</code>: <code>en-US</code></li>"
    "</ul>"
    "<h3>How to use</h3>"
    "<ol>"
    "<li>Optional — run Benefits Eligibility → <em>Search benefits</em> first to "
    "discover real <code>benefitCode</code> + <code>productCode</code> for a card.</li>"
    "<li>Open <strong>Content → Search benefit contents</strong>. Supply a "
    "<code>cardNumber</code> and optionally narrow by <code>benefitCode</code>, "
    "<code>productCode</code>, <code>effectiveDate</code> or <code>locale</code>.</li>"
    "<li>Render the response — each <code>bundle</code> has localized "
    "<code>contents[]</code> (display name, descriptions, image) plus a list of "
    "<code>benefits[]</code> with their own localized content, T&amp;Cs, "
    "<code>ctaFields</code>, etc.</li>"
    "</ol>"
    "<p class='muted'>cardNumber is sent as an integer per the spec. Sandbox PANs only.</p>"
)


_CONTENT_PARAMS: List[Dict[str, Any]] = [
    {"name": "cardNumber",    "label": "Card number / BIN", "type": "select", "default": "5291070000000000", "required": True,  "options": _CARD_OPTIONS, "help": "Mandatory. 6-digit BIN or 12–19-digit PAN."},
    {"name": "effectiveDate", "label": "Effective date",    "type": "text",   "default": "",                 "required": False, "help": "YYYY-MM-DD. Defaults to today."},
    {"name": "benefitCode",   "label": "Benefit code",      "type": "select", "default": "",                 "required": False, "options": _BENEFIT_CODE_OPTIONS, "help": "Narrows to a specific benefit (3–5 char)."},
    {"name": "productCode",   "label": "Product code",      "type": "select", "default": "",                 "required": False, "options": _PRODUCT_CODE_OPTIONS, "help": "Required if the BIN/card has multiple products."},
    {"name": "locale",        "label": "Locale",            "type": "select", "default": "en-US",            "required": False, "options": _LOCALE_OPTIONS},
]


MANIFEST: Dict[str, Any] = {
    "id": "bces",
    "name": "Benefits Content Eligibility",
    "description": (
        "Mastercard BCES — returns rich renderable content (titles, "
        "descriptions, imagery, T&Cs, FAQ links, CTAs) for bundles and "
        "benefits a card is eligible for. OAuth 1.0a, body-signed."
    ),
    "docs_url": "https://developer.mastercard.com/bces-service/documentation/",
    "how_to": _HOW_TO,
    "categories": ["Content"],
    "state_schema": [],
    "configured": _configured(),
    "operations": [
        {
            "id": "search_contents",
            "name": "Search benefit contents",
            "category": "Content",
            "method": "POST",
            "description": "Returns bundles & benefits with rich, localized renderable content.",
            "params": _CONTENT_PARAMS,
        },
    ],
}


def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if op_id == "search_contents":
        return _search_contents(params)
    return {"success": False, "error": f"Unknown operation: {op_id}"}


def _search_contents(params: Dict[str, Any]) -> Dict[str, Any]:
    card_str = (params.get("cardNumber") or "").strip()
    if not card_str:
        return {"success": False, "error": "cardNumber is required."}
    if not card_str.isdigit():
        return {"success": False, "error": "cardNumber must be numeric (BIN or PAN)."}

    body: Dict[str, Any] = {"cardNumber": int(card_str)}

    for opt in ("effectiveDate", "benefitCode", "productCode", "locale"):
        v = (params.get(opt) or "").strip()
        if v:
            body[opt] = v

    return _signed_request("POST", "/benefit-contents/searches", body=body)


def _signed_request(
    method: str,
    path: str,
    *,
    body: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("bces"):
        return {
            "success": False,
            "error": (
                "BCES is not configured. Set BCES_CONSUMER_KEY and "
                "BCES_SIGNING_KEY_PATH in .env, then restart the server."
            ),
        }

    import requests

    url = f"{_base()}{path}"

    if is_simulated("bces"):
        body_str = json.dumps(body) if body is not None else None
        headers: Dict[str, str] = {
            "Accept": "application/json",
            "x-openapi-transid": str(uuid.uuid4()),
        }
        if body_str is not None:
            headers["Content-Type"] = "application/json"
        headers["Authorization"] = "Simulated"
    else:
        consumer_key = os.environ["BCES_CONSUMER_KEY"]
        key_path     = os.environ["BCES_SIGNING_KEY_PATH"]
        key_password = os.environ.get("BCES_SIGNING_KEY_PASSWORD", "keystorepassword")
        enc_cert     = os.environ.get("BCES_ENCRYPTION_CERT_PATH", "").strip()

        project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        if not os.path.isabs(key_path):
            key_path = os.path.join(project_root, key_path)
        if enc_cert and not os.path.isabs(enc_cert):
            enc_cert = os.path.join(project_root, enc_cert)

        import oauth1.authenticationutils as authutils
        from oauth1.oauth import OAuth

        if body is not None:
            if not enc_cert or not os.path.isfile(enc_cert):
                return {
                    "success": False,
                    "error": (
                        "BCES requires JWE payload encryption. Download the "
                        "'Client Encryption' .pem from your Mastercard Developers "
                        "project (BCES service) and set BCES_ENCRYPTION_CERT_PATH "
                        "in .env, then restart."
                    ),
                    "request": {"method": method, "url": url, "body": body},
                }
            try:
                body_str = _encrypt_body(body, enc_cert)
            except Exception as e:
                return {"success": False, "error": f"JWE encryption failed: {e}"}
        else:
            body_str = None

        headers = {
            "Accept": "application/json",
            "X-OpenApi-ClientId": consumer_key.split("!", 1)[0],
            "x-openapi-transid":  str(uuid.uuid4()),
        }
        if body_str is not None:
            headers["Content-Type"] = "application/json"

        try:
            signing_key = authutils.load_signing_key(key_path, key_password)
            headers["Authorization"] = OAuth.get_authorization_header(
                url, method, body_str, consumer_key, signing_key,
            )
        except Exception as e:
            return {"success": False, "error": f"OAuth signing failed: {e}"}

    try:
        resp = requests.request(method, url, data=body_str, headers=headers, timeout=20)
        status_code = resp.status_code
        try:
            resp_body: Any = resp.json()
        except Exception:
            resp_body = {"raw": resp.text}
    except Exception as e:
        return {"success": False, "error": f"Request failed: {e}"}

    success = 200 <= status_code < 300
    return {
        "success": success,
        "data":    resp_body if success else {},
        "error":   None if success else (resp_body.get("Errors", {}) if isinstance(resp_body, dict) else resp_body),
        "request": {"method": method, "url": url, "body": body, "body_encrypted": body_str if body is not None else None},
        "response": {"status_code": status_code, "body": resp_body},
        "state_updates": {},
    }


def _encrypt_body(body: Dict[str, Any], cert_path: str) -> str:
    """JWE-encrypt the entire request body into {\"encryptedValue\": \"<JWE>\"}."""
    from client_encryption.jwe_encryption_config import JweEncryptionConfig
    from client_encryption.jwe_encryption import encrypt_payload

    config = JweEncryptionConfig({
        "paths": {
            "$": {
                "toEncrypt": {"$": "$"},
                "toDecrypt": {},
            }
        },
        "encryptedValueFieldName": "encryptedValue",
        "encryptionCertificate":   cert_path,
    })
    encrypted = encrypt_payload(json.dumps(body), config)
    return json.dumps(encrypted)
