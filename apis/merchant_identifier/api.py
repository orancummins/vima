"""Merchant Identifier API — OAuth 1.0a implementation."""
from __future__ import annotations

import os
from typing import Any
from urllib.parse import urlencode

_MANIFEST_DESC = (
    "Retrieve merchant data by using merchant descriptor, card acceptor ID, "
    "or tax ID."
)

_SANDBOX_DATASET_URL = (
    "https://static.developer.mastercard.com/content/merchant-identifier/uploads/"
    "merchant-identifier-sandbox-merchant-descriptors.xlsx"
)

MANIFEST: dict[str, Any] = {
    "id": "merchant_identifier",
    "name": "Merchant Identifier",
    "description": _MANIFEST_DESC,
    "docs_url": "https://developer.mastercard.com/merchant-identifier/documentation/api-reference/",
    "how_to": (
        "<p><strong>Merchant Identifier</strong> helps resolve merchant information "
        "from noisy payment metadata.</p>"
        "<h3>How to use</h3>"
        "<ol>"
        "<li>Use <strong>Merchants → Match by descriptor</strong> with a merchant descriptor "
        "string from your transaction feed (e.g. card statement text).</li>"
        "<li>Use <strong>Match by card acceptor ID</strong> when you have one or more card "
        "acceptor IDs.</li>"
        "<li>Use <strong>Match by tax ID</strong> when tax IDs are available.</li>"
        "</ol>"
        "<h3>Results</h3>"
        "<ul>"
        "<li>Matched merchant records from Mastercard's merchant dataset.</li>"
        "<li>Useful for merchant normalization, enrichment, and analytics.</li>"
        "</ul>"
        "<h3>Sandbox test values</h3>"
        "<p>Use official Mastercard sandbox values for reliable non-empty responses. "
        "<a href='" + _SANDBOX_DATASET_URL + "' target='_blank'>"
        "Merchant Identifier sandbox dataset (xlsx)</a>.</p>"
        "<ul>"
        "<li><strong>Match by descriptor</strong>: "
        "<code>DOLIUMPTYLTDWELSHPOOLWA</code>, "
        "<code>FAMOUSFOOTWEAR#1749O'FALLONMO</code>, "
        "<code>PAY*LAKEPROPERTYMANA314-614-7602MO</code>.</li>"
        "<li><strong>Match by card acceptor ID</strong>: "
        "<code>000001020455702</code>, <code>00081362435</code>, "
        "<code>000101000400056</code>.</li>"
        "<li><strong>Match by tax ID</strong>: "
        "<code>tax_id=15065786007458</code>, <code>country_code=BRA</code> "
        "(also valid: <code>27905491000176</code>, <code>34763997000153</code>).</li>"
        "</ul>"
    ),
    "categories": ["Merchants"],
    "state_schema": [],
    "configured": bool(
        os.environ.get("MERCHANT_IDENTIFIER_CONSUMER_KEY")
        and os.environ.get("MERCHANT_IDENTIFIER_CONSUMER_KEY") != "your-consumer-key-here"
        and os.environ.get("MERCHANT_IDENTIFIER_SIGNING_KEY_PATH")
    ),
    "operations": [
        {
            "id": "match_merchants",
            "name": "Match by descriptor",
            "category": "Merchants",
            "method": "GET",
            "description": "Get matched merchants for a given merchant descriptor.",
            "params": [
                {
                    "name": "merchant_descriptor",
                    "label": "Merchant descriptor",
                    "type": "text",
                    "default": "DOLIUMPTYLTDWELSHPOOLWA",
                    "required": True,
                },
            ],
        },
        {
            "id": "match_by_card_acceptor_ids",
            "name": "Match by card acceptor ID",
            "category": "Merchants",
            "method": "GET",
            "description": "Get matched merchant information for one or more card acceptor IDs.",
            "params": [
                {
                    "name": "card_acceptor_id",
                    "label": "Card acceptor ID",
                    "type": "text",
                    "default": "000001020455702",
                    "required": True,
                },
            ],
        },
        {
            "id": "match_by_tax_ids",
            "name": "Match by tax ID",
            "category": "Merchants",
            "method": "GET",
            "description": "Get merchant information for one or more tax IDs.",
            "params": [
                {
                    "name": "tax_id",
                    "label": "Tax ID",
                    "type": "text",
                    "default": "15065786007458",
                    "required": True,
                },
                {
                    "name": "country_code",
                    "label": "Country code (ISO-3)",
                    "type": "text",
                    "default": "BRA",
                    "required": True,
                },
            ],
        },
    ],
}

_SANDBOX_BASE_URL = "https://sandbox.api.mastercard.com/merchant-identifier"
_PROD_BASE_URL = "https://api.mastercard.com/merchant-identifier"


def _base_url() -> str:
    from simulator.switcher import sim_base_url
    env = os.environ.get("MERCHANT_IDENTIFIER_ENV", "sandbox").lower()
    real = _PROD_BASE_URL if env == "production" else _SANDBOX_BASE_URL
    return sim_base_url("merchant_identifier", real)


def _configured() -> bool:
    key = os.environ.get("MERCHANT_IDENTIFIER_CONSUMER_KEY", "")
    path = os.environ.get("MERCHANT_IDENTIFIER_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return _configured() or is_simulated("merchant_identifier")


def get_state() -> dict[str, Any]:
    return {"configured": _configured()}


def _not_configured_err() -> dict[str, Any]:
    return {
        "success": False,
        "error": (
            "Merchant Identifier is not configured. Set MERCHANT_IDENTIFIER_CONSUMER_KEY and "
            "MERCHANT_IDENTIFIER_SIGNING_KEY_PATH in .env, then restart the server."
        ),
    }


def _resolve_key_path(path: str) -> str:
    if os.path.isabs(path):
        return path
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(project_root, path)


def _signed_request(url: str) -> dict[str, Any]:
    import requests

    from simulator.switcher import is_simulated

    headers = {"Accept": "application/json"}

    if is_simulated("merchant_identifier"):
        headers["Authorization"] = "Simulated"
    else:
        import oauth1.authenticationutils as authutils
        from oauth1.oauth import OAuth

        consumer_key = os.environ["MERCHANT_IDENTIFIER_CONSUMER_KEY"]
        key_path = _resolve_key_path(os.environ["MERCHANT_IDENTIFIER_SIGNING_KEY_PATH"])
        key_password = os.environ.get("MERCHANT_IDENTIFIER_SIGNING_KEY_PASSWORD", "keystorepassword")

        try:
            signing_key = authutils.load_signing_key(key_path, key_password)
            auth_header = OAuth.get_authorization_header(url, "GET", "", consumer_key, signing_key)
            headers["Authorization"] = auth_header
        except Exception as exc:
            return {"success": False, "error": f"OAuth signing failed: {exc}"}

    try:
        resp = requests.get(url, headers=headers, timeout=15)
        status_code = resp.status_code
        try:
            resp_body = resp.json()
        except Exception:
            resp_body = {"raw": resp.text}
    except Exception as exc:
        return {"success": False, "error": f"Request failed: {exc}"}

    success = 200 <= status_code < 300
    return {
        "success": success,
        "data": resp_body if success else {},
        "error": None if success else (resp_body.get("Errors") if isinstance(resp_body, dict) else resp_body),
        "request": {"method": "GET", "url": url, "body": None},
        "response": {"status_code": status_code, "body": resp_body},
        "state_updates": {},
    }


def execute(op_id: str, params: dict[str, Any]) -> dict[str, Any]:
    if op_id == "match_merchants":
        return _match_merchants(params)
    if op_id == "match_by_card_acceptor_ids":
        return _match_by_card_acceptor_ids(params)
    if op_id == "match_by_tax_ids":
        return _match_by_tax_ids(params)
    return {"success": False, "error": f"Unknown operation: {op_id}"}


def _match_merchants(params: dict[str, Any]) -> dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("merchant_identifier"):
        return _not_configured_err()

    descriptor = (params.get("merchant_descriptor") or "").strip()
    if not descriptor:
        return {"success": False, "error": "merchant_descriptor is required."}

    qs = urlencode({"merchant_descriptor": descriptor})
    return _signed_request(f"{_base_url()}/merchants?{qs}")


def _match_by_card_acceptor_ids(params: dict[str, Any]) -> dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("merchant_identifier"):
        return _not_configured_err()

    card_acceptor_id = (
        params.get("card_acceptor_id")
        or params.get("card_acceptor_ids")
        or ""
    ).strip()
    if not card_acceptor_id:
        return {"success": False, "error": "card_acceptor_id is required."}

    # API expects a singular card_acceptor_id query field.
    if "," in card_acceptor_id:
        card_acceptor_id = card_acceptor_id.split(",", 1)[0].strip()

    qs = urlencode({"card_acceptor_id": card_acceptor_id})
    return _signed_request(f"{_base_url()}/merchants-by-card-acceptor-ids?{qs}")


def _match_by_tax_ids(params: dict[str, Any]) -> dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("merchant_identifier"):
        return _not_configured_err()

    tax_id = (
        params.get("tax_id")
        or params.get("tax_ids")
        or ""
    ).strip()
    if not tax_id:
        return {"success": False, "error": "tax_id is required."}

    country_code = (params.get("country_code") or "USA").strip().upper()
    if not country_code:
        return {"success": False, "error": "country_code is required."}

    # API expects a singular tax_id query field.
    if "," in tax_id:
        tax_id = tax_id.split(",", 1)[0].strip()

    qs = urlencode({"tax_id": tax_id, "country_code": country_code})
    return _signed_request(f"{_base_url()}/merchants-by-tax-ids?{qs}")
