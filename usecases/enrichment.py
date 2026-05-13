"""Data Enrichment — use case backed by the Open Finance enrichment API.

Sends a curated batch of raw transaction descriptions to
POST /data-enrichment/transactions and returns the before/after pairs.

A persistent JSON cache keyed by transaction id is used so that, once a
transaction has been successfully enriched, repeat lookups never hit the
upstream API.  This keeps the demo working even after the (limited)
sandbox quota has been exhausted.
"""
from __future__ import annotations

import json
import os
import time
from typing import Any, Dict, List

MANIFEST: Dict[str, Any] = {
    "id": "enrichment",
    "name": "Data Enrichment",
    "description": (
        "Raw bank statement text like \"AMZN MKTP US*MK7G3B2X1\" tells consumers nothing. "
        "The Open Finance Data Enrichment API instantly resolves those cryptic strings into "
        "clean merchant names, recognisable brand logos, granular spend categories, and "
        "confidence scores — turning opaque payment data into powerful, actionable intelligence "
        "that drives better customer experiences, richer analytics, and stronger engagement."
    ),
    "apis": ["ofin"],
    "render": "enrichment",
}

# ---------------------------------------------------------------------------
# Curated raw transaction descriptions — chosen because they produce strong
# API enrichment results with logo URLs and accurate categories.
# ---------------------------------------------------------------------------
_RAW_TRANSACTIONS = [
    {"id": "t1", "description": "SBUX 00654321 CARD 12345",       "amount": -6.75,  "date": "May 9",  "ts": "2026-05-09T10:30:00Z"},
    {"id": "t2", "description": "AMZN MKTP US*MK7G3B2X1",         "amount": -34.99, "date": "May 8",  "ts": "2026-05-08T14:22:00Z"},
    {"id": "t3", "description": "UBER* TRIP HELP.UBER.COM",        "amount": -18.25, "date": "May 7",  "ts": "2026-05-07T19:45:00Z"},
    {"id": "t4", "description": "NETFLIX.COM 866-579-7172 CA",     "amount": -15.99, "date": "May 5",  "ts": "2026-05-05T00:00:00Z"},
    {"id": "t5", "description": "WHOLEFDS MKT #10452 SFCA",        "amount": -91.37, "date": "May 6",  "ts": "2026-05-06T11:15:00Z"},
    {"id": "t6", "description": "LYFT *RIDE 855-865-9553",         "amount": -12.50, "date": "May 4",  "ts": "2026-05-04T08:00:00Z"},
    {"id": "t7", "description": "APPLE.COM/BILL 866-712-7753",     "amount": -9.99,  "date": "May 3",  "ts": "2026-05-03T12:00:00Z"},
    {"id": "t8", "description": "TARGET 00012345 SAN FRANCISCO CA","amount": -52.14, "date": "May 2",  "ts": "2026-05-02T09:00:00Z"},
]


# ---------------------------------------------------------------------------
# Persistent cache: { txn_id: shaped_enriched_dict }
# Stored next to this module so it survives restarts.
# ---------------------------------------------------------------------------
_CACHE_PATH = os.path.join(os.path.dirname(__file__), ".enrichment_cache.json")
_cache: Dict[str, Dict[str, Any]] | None = None


def _load_cache() -> Dict[str, Dict[str, Any]]:
    global _cache
    if _cache is not None:
        return _cache
    try:
        with open(_CACHE_PATH, "r", encoding="utf-8") as fh:
            _cache = json.load(fh) or {}
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        _cache = {}
    return _cache


def _save_cache() -> None:
    if _cache is None:
        return
    try:
        with open(_CACHE_PATH, "w", encoding="utf-8") as fh:
            json.dump(_cache, fh, indent=2)
    except OSError:
        pass


def _client():
    from apis.ofin import api as ofin_api
    return ofin_api._get_client()


def _shape_row(raw: Dict[str, Any], enriched: Dict[str, Any]) -> Dict[str, Any]:
    """Combine a raw preset and a cached/enriched payload into a UI row."""
    return {
        "id":     raw["id"],
        "raw":    raw["description"],
        "amount": raw["amount"],
        "date":   raw["date"],
        "enriched": enriched,
    }


def _shape_api_response(api: Dict[str, Any], raw: Dict[str, Any]) -> Dict[str, Any]:
    """Shape one Mastercard API transaction record into a flat enriched dict."""
    entities: list = api.get("entities") or []
    primary = entities[0] if entities else {}
    addr: dict = api.get("address") or {}

    if addr.get("city") and addr.get("state"):
        location = f"{addr['city']}, {addr['state']}"
    elif api.get("isEcommerce"):
        location = "Online"
    else:
        location = None

    return {
        "name":            primary.get("name") or raw["description"],
        "category":        api.get("transactionCategory"),
        "categoryGroup":   api.get("transactionCategoryGroup"),
        "confidence":      round(primary.get("entityStandardizationConfidenceScore") or 0, 1),
        "categoryScore":   round(api.get("transactionCategoryScore") or 0, 1),
        "logoUrl":         primary.get("logoUrl"),
        "website":         primary.get("website"),
        "location":        location,
        "isRecurring":     api.get("isRecurringTransaction") or False,
        "isEcommerce":     api.get("isEcommerce") or False,
        "_cachedAt":       int(time.time()),
    }


def get_enrichment_data() -> Dict[str, Any]:
    """Return the raw transaction list — does NOT call the enrichment API.

    The UI renders the raw transactions immediately and only calls the
    enrichment API (via ``do_action``) when the user clicks Enrich.
    """
    transactions: List[Dict[str, Any]] = [
        {
            "id":     t["id"],
            "raw":    t["description"],
            "amount": t["amount"],
            "date":   t["date"],
            "enriched": None,
        }
        for t in _RAW_TRANSACTIONS
    ]
    return {"transactions": transactions}


def do_action(action: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """Run the enrichment API on demand, with a smart per-transaction cache.

    Action ``enrich`` accepts:
      - ``ids``: optional list limiting which transactions to enrich.
      - ``force``: optional bool — if true, bypass the cache and re-call the API.

    Behaviour:
      1. Cached transactions are returned immediately (no API call).
      2. Uncached transactions are sent to the API in a single batch.
      3. Successful API responses are persisted to the cache.
      4. If the API call fails, any cached transactions are still returned;
         only uncached transactions report the error.
    """
    if action == "clear_cache":
        global _cache
        _cache = {}
        _save_cache()
        return {"cleared": True}

    if action != "enrich":
        return {"error": f"Unknown action: {action}"}

    cache = _load_cache()
    force = bool(params.get("force"))

    requested_ids = params.get("ids")
    if requested_ids:
        wanted = set(requested_ids)
        targets = [t for t in _RAW_TRANSACTIONS if t["id"] in wanted]
    else:
        targets = list(_RAW_TRANSACTIONS)

    if not targets:
        return {"transactions": []}

    # Split into cached (served instantly) and uncached (need API call)
    results_by_id: Dict[str, Dict[str, Any]] = {}
    cache_hits: List[str] = []
    needs_api: List[Dict[str, Any]] = []

    for raw in targets:
        if not force and raw["id"] in cache:
            results_by_id[raw["id"]] = _shape_row(raw, cache[raw["id"]])
            cache_hits.append(raw["id"])
        else:
            needs_api.append(raw)

    api_error: Dict[str, Any] | None = None

    if needs_api:
        client = _client()
        api_txns = [
            {
                "externalCustomerId": "vima_demo",
                "externalAccountId":  "vima_acct",
                "accountType":        "checking",
                "externalTransactionId": t["id"],
                "transactionTimestamp":  t["ts"],
                "description":           t["description"],
                "amount":                t["amount"],
                "directionIndicator":    "debit",
            }
            for t in needs_api
        ]

        data, status = client.enrich_transactions(api_txns)
        if status >= 400 or not isinstance(data, dict):
            api_error = {
                "message": f"Enrichment API returned {status}",
                "detail":  data,
                "failedIds": [t["id"] for t in needs_api],
            }
        else:
            api_by_id: Dict[str, Any] = {
                t["externalTransactionId"]: t
                for t in (data.get("transactions") or [])
            }
            for raw in needs_api:
                api = api_by_id.get(raw["id"], {})
                shaped = _shape_api_response(api, raw)
                cache[raw["id"]] = shaped
                results_by_id[raw["id"]] = _shape_row(raw, shaped)
            _save_cache()

    # Preserve original input order
    transactions = [results_by_id[t["id"]] for t in targets if t["id"] in results_by_id]

    response: Dict[str, Any] = {
        "transactions": transactions,
        "cacheHits":    cache_hits,
        "fromApi":      [t["id"] for t in needs_api if t["id"] in results_by_id],
    }
    if api_error:
        response["error"]  = api_error["message"]
        response["detail"] = api_error["detail"]
        response["failedIds"] = api_error["failedIds"]
    return response
