"""Enhanced Currency Conversion Calculator (ECCC) — OAuth 1.0a implementation.

API host:
  https://sandbox.api.mastercard.com/enhanced/settlement/currencyrate
  https://api.mastercard.com/enhanced/settlement/currencyrate

Operations (all GET):
  /summary-rates    — Mastercard + ECB rate summary for a currency pair
  /rate-statuses    — are Mastercard + ECB rates issued for a given date?
  /mc-currencies    — list of Mastercard currencies
  /ecb-currencies   — list of ECB-published EEA currencies
"""
from __future__ import annotations

import os
from typing import Any, Dict
from urllib.parse import urlencode

MANIFEST: Dict[str, Any] = {
    "id": "enhanced_currency_conversion_calculator",
    "name": "Enhanced Currency Conversion Calculator",
    "description": (
        "Mastercard's daily and historical currency conversion rates plus "
        "European Central Bank (ECB) reference rates. Used by EEA issuers "
        "to comply with EU Regulation 2019/518 by disclosing the % mark-up "
        "between Mastercard FX rates and ECB reference rates."
    ),
    "docs_url": (
        "https://developer.mastercard.com/"
        "enhanced-currency-conversion-calculator/documentation/"
    ),
    "how_to": (
        "<p><strong>Enhanced Currency Conversion Calculator</strong> returns "
        "Mastercard's currency conversion rate, the ECB reference rate, and the "
        "percentage difference between them for a given currency pair — including "
        "any issuer fees you supply.</p>"
        "<h3>How to use</h3>"
        "<ol>"
        "<li>Select <strong>Rates → Summary Rate</strong> from the operations panel.</li>"
        "<li>Choose a <strong>transaction currency</strong> (e.g. <code>USD</code>) and a "
        "<strong>cardholder billing currency</strong> (e.g. <code>EUR</code>).</li>"
        "<li>Enter a <strong>transaction amount</strong> (default <code>100</code>) and an "
        "optional <strong>bank fee</strong>.</li>"
        "<li>Leave <strong>fxDate</strong> as <code>0000-00-00</code> to use today's effective "
        "rates, or set an ISO date for a historical lookup.</li>"
        "<li>Click <strong>Send</strong>.</li>"
        "</ol>"
        "<h3>What you get back</h3>"
        "<ul>"
        "<li><strong>conversionRate</strong> — Mastercard's rate for the currency pair.</li>"
        "<li><strong>ecbReferenceRate</strong> — European Central Bank reference rate "
        "(and <code>ecbReferenceRateDate</code>).</li>"
        "<li><strong>crdhldBillAmtExclAllFees</strong> / <strong>InclAllFees</strong> — "
        "billed amount before and after issuer fees.</li>"
        "<li><strong>pctDifferenceMastercardInclAllFeesAndEcb</strong> — % mark-up vs ECB "
        "(the EU 2019/518 disclosure figure).</li>"
        "</ul>"
        "<h3>Helper operations</h3>"
        "<ul>"
        "<li><strong>Rate Statuses</strong> — check whether MC and ECB rates have been "
        "published for a given date.</li>"
        "<li><strong>MC / ECB Currencies</strong> — list the supported currency codes you "
        "can drop into a UI picker.</li>"
        "</ul>"
    ),
    "categories": ["FX", "Settlement"],
    "state_schema": [],
    "configured": bool(
        os.environ.get("ENHANCED_CURRENCY_CONVERSION_CALCULATOR_CONSUMER_KEY")
        and os.environ.get("ENHANCED_CURRENCY_CONVERSION_CALCULATOR_CONSUMER_KEY")
        != "your-consumer-key-here"
        and os.environ.get("ENHANCED_CURRENCY_CONVERSION_CALCULATOR_SIGNING_KEY_PATH")
    ),
    "operations": [
        {
            "id": "summary_rate",
            "name": "Summary Rate",
            "category": "Rates",
            "method": "GET",
            "description": (
                "Mastercard + ECB rate summary for a currency pair, including the "
                "% mark-up vs ECB required by EU Regulation 2019/518."
            ),
            "params": [
                {
                    "name": "fx_date",
                    "label": "fxDate (ISO date, 0000-00-00 = today)",
                    "type": "text",
                    "default": "0000-00-00",
                    "required": True,
                },
                {
                    "name": "trans_curr",
                    "label": "Transaction currency (ISO 4217)",
                    "type": "select",
                    "default": "USD",
                    "required": True,
                    "options": [
                        {"value": "USD", "label": "USD — US Dollar"},
                        {"value": "EUR", "label": "EUR — Euro"},
                        {"value": "GBP", "label": "GBP — British Pound"},
                        {"value": "JPY", "label": "JPY — Japanese Yen"},
                        {"value": "CHF", "label": "CHF — Swiss Franc"},
                    ],
                },
                {
                    "name": "crdhld_bill_curr",
                    "label": "Cardholder billing currency (ISO 4217)",
                    "type": "select",
                    "default": "EUR",
                    "required": True,
                    "options": [
                        {"value": "EUR", "label": "EUR — Euro"},
                        {"value": "GBP", "label": "GBP — British Pound"},
                        {"value": "USD", "label": "USD — US Dollar"},
                        {"value": "SEK", "label": "SEK — Swedish Krona"},
                        {"value": "PLN", "label": "PLN — Polish Złoty"},
                    ],
                },
                {
                    "name": "trans_amt",
                    "label": "Transaction amount",
                    "type": "text",
                    "default": "100.00",
                    "required": True,
                },
                {
                    "name": "bank_fee",
                    "label": "Bank fee (fixed, optional)",
                    "type": "text",
                    "default": "0.00",
                    "required": False,
                },
                {
                    "name": "bank_fee_pct",
                    "label": "Bank fee percent (optional)",
                    "type": "text",
                    "default": "0.00",
                    "required": False,
                },
            ],
        },
        {
            "id": "rate_status",
            "name": "Rate Status",
            "category": "Rates",
            "method": "GET",
            "description": "Check whether Mastercard + ECB rates have been issued for a date.",
            "params": [
                {
                    "name": "fx_date",
                    "label": "fxDate (ISO date)",
                    "type": "text",
                    "default": "0000-00-00",
                    "required": True,
                },
            ],
        },
        {
            "id": "list_mc_currencies",
            "name": "List Mastercard Currencies",
            "category": "Reference",
            "method": "GET",
            "description": "List of currencies for which Mastercard publishes a rate.",
            "params": [],
        },
        {
            "id": "list_ecb_currencies",
            "name": "List ECB Currencies",
            "category": "Reference",
            "method": "GET",
            "description": "List of EEA currencies for which the ECB publishes a reference rate.",
            "params": [],
        },
    ],
}


_PROD_BASE_URL    = "https://api.mastercard.com/enhanced/settlement/currencyrate"
_SANDBOX_BASE_URL = "https://sandbox.api.mastercard.com/enhanced/settlement/currencyrate"
_ENV_PREFIX       = "ENHANCED_CURRENCY_CONVERSION_CALCULATOR"
_SIM_SLUG         = "enhanced_currency_conversion_calculator"


def _base_url() -> str:
    from simulator.switcher import sim_base_url
    env = os.environ.get(f"{_ENV_PREFIX}_ENV", "sandbox").lower()
    real = _PROD_BASE_URL if env == "production" else _SANDBOX_BASE_URL
    return sim_base_url(_SIM_SLUG, real)


def _configured() -> bool:
    key = os.environ.get(f"{_ENV_PREFIX}_CONSUMER_KEY", "")
    path = os.environ.get(f"{_ENV_PREFIX}_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return _configured() or is_simulated(_SIM_SLUG)


def get_state() -> Dict[str, Any]:
    return {"configured": _configured()}


def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if op_id == "summary_rate":
        return _get(
            "/summary-rates",
            {
                "fxDate":         (params.get("fx_date") or "0000-00-00").strip(),
                "transCurr":      (params.get("trans_curr") or "").strip().upper(),
                "crdhldBillCurr": (params.get("crdhld_bill_curr") or "").strip().upper(),
                "transAmt":       (params.get("trans_amt") or "").strip(),
                "bankFee":        (params.get("bank_fee") or "").strip() or "0.00",
                "bankFeePct":     (params.get("bank_fee_pct") or "").strip() or "0.00",
            },
        )
    if op_id == "rate_status":
        return _get(
            "/rate-statuses",
            {"fxDate": (params.get("fx_date") or "0000-00-00").strip()},
        )
    if op_id == "list_mc_currencies":
        return _get("/mc-currencies", {})
    if op_id == "list_ecb_currencies":
        return _get("/ecb-currencies", {})
    return {"success": False, "error": f"Unknown operation: {op_id}"}


def _get(path: str, query: Dict[str, str]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated

    if not _configured() and not is_simulated(_SIM_SLUG):
        return {
            "success": False,
            "error": (
                "Enhanced Currency Conversion Calculator is not configured. "
                f"Set {_ENV_PREFIX}_CONSUMER_KEY and {_ENV_PREFIX}_SIGNING_KEY_PATH "
                "in .env, then restart the server."
            ),
        }

    # Drop empty values so the URL is clean.
    qs = {k: v for k, v in query.items() if v not in (None, "")}
    url = f"{_base_url()}{path}"
    if qs:
        url = f"{url}?{urlencode(qs)}"

    headers = {"Accept": "application/json"}

    if is_simulated(_SIM_SLUG):
        headers["Authorization"] = "Simulated"
    else:
        consumer_key = os.environ[f"{_ENV_PREFIX}_CONSUMER_KEY"]
        key_path     = os.environ[f"{_ENV_PREFIX}_SIGNING_KEY_PATH"]
        key_password = os.environ.get(f"{_ENV_PREFIX}_SIGNING_KEY_PASSWORD", "keystorepassword")
        if not os.path.isabs(key_path):
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            key_path = os.path.join(project_root, key_path)

        import oauth1.authenticationutils as authutils
        from oauth1.oauth import OAuth

        try:
            signing_key = authutils.load_signing_key(key_path, key_password)
            headers["Authorization"] = OAuth.get_authorization_header(
                url, "GET", None, consumer_key, signing_key,
            )
        except Exception as e:
            return {"success": False, "error": f"OAuth signing failed: {e}"}

    import requests
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        status_code = resp.status_code
        try:
            resp_body = resp.json()
        except Exception:
            resp_body = {"raw": resp.text}
    except Exception as e:
        return {"success": False, "error": f"Request failed: {e}"}

    success = 200 <= status_code < 300
    return {
        "success": success,
        "data": resp_body if success else {},
        "error": None if success else (resp_body.get("Errors", {}) or resp_body),
        "request": {"method": "GET", "url": url},
        "response": {"status_code": status_code, "body": resp_body},
        "state_updates": {},
    }
