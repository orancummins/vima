"""Data Enrichment — use case backed by the Open Finance enrichment API.

Sends a curated batch of raw transaction descriptions to
POST /data-enrichment/transactions and returns the before/after pairs.
"""
from __future__ import annotations

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


def _client():
    from apis.ofin import api as ofin_api
    return ofin_api._get_client()


def get_enrichment_data() -> Dict[str, Any]:
    """Call the Data Enrichment API and return before/after pairs."""
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
        for t in _RAW_TRANSACTIONS
    ]

    data, status = client.enrich_transactions(api_txns)
    if status >= 400 or not isinstance(data, dict):
        return {"error": f"Enrichment API returned {status}", "detail": data}

    enriched_by_id: Dict[str, Any] = {
        t["externalTransactionId"]: t
        for t in (data.get("transactions") or [])
    }

    results: List[Dict[str, Any]] = []
    for raw in _RAW_TRANSACTIONS:
        api = enriched_by_id.get(raw["id"], {})
        entities: list = api.get("entities") or []
        primary = entities[0] if entities else {}
        addr: dict = api.get("address") or {}

        if addr.get("city") and addr.get("state"):
            location = f"{addr['city']}, {addr['state']}"
        elif api.get("isEcommerce"):
            location = "Online"
        else:
            location = None

        results.append({
            "id":     raw["id"],
            "raw":    raw["description"],
            "amount": raw["amount"],
            "date":   raw["date"],
            "enriched": {
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
            },
        })

    return {"transactions": results}
