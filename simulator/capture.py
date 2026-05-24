"""Capture live sandbox responses into per-API simulator DBs.

When a real Mastercard sandbox call succeeds, the response body is passed to
capture_response(). CAPTURE_MAP maps (api_slug, op_id) → list of
(resource_collection, extractor_fn, id_field) tuples. Each extractor pulls a
list of records from the raw response body and upserts them into the per-API DB.
"""
from __future__ import annotations
from typing import Any, Callable

from simulator.datastore import store

# ---------------------------------------------------------------------------
# Mapping: (api_slug, op_id) → [(resource, extractor, id_field), ...]
# extractor(resp_body) must return a list of dicts
# ---------------------------------------------------------------------------
CaptureSpec = tuple[str, Callable[[Any], list[dict]], str]

CAPTURE_MAP: dict[tuple[str, str], list[CaptureSpec]] = {
    # ── BIN Lookup ─────────────────────────────────────────────────────────
    ("binlookup", "lookup_bin"): [
        ("bins", lambda r: r.get("items", []) if isinstance(r, dict) else [], "binNum"),
    ],

    # ── BCES ───────────────────────────────────────────────────────────────
    ("bces", "search_contents"): [
        ("benefit_contents", lambda r: r.get("bundles", []) if isinstance(r, dict) else [], "id"),
    ],

    # ── Clarity ────────────────────────────────────────────────────────────
    ("clarity", "search_merchant"): [
        (
            "merchants",
            lambda r: [
                mr.get("merchantResult", {})
                for mr in (r.get("searchResults", []) if isinstance(r, dict) else [])
                if mr.get("merchantResult")
            ],
            "merchantId",
        ),
    ],

    # ── Eligibility ────────────────────────────────────────────────────────
    ("eligibility", "search_benefits"): [
        ("benefits", lambda r: r.get("data", []) if isinstance(r, dict) else [], "benefitCode"),
    ],
    ("eligibility", "search_products"): [
        ("products", lambda r: r.get("data", []) if isinstance(r, dict) else [], "productCode"),
    ],

    # ── Places ─────────────────────────────────────────────────────────────
    ("places", "search_places"): [
        ("places", lambda r: r.get("items", []) if isinstance(r, dict) else [], "locationId"),
    ],
    ("places", "get_place"): [
        ("places", lambda r: [r] if isinstance(r, dict) and r.get("locationId") else [], "locationId"),
    ],
    ("places", "list_mcc_codes"): [
        ("mcc_codes", lambda r: r.get("items", []) if isinstance(r, dict) else [], "merchantCategoryCode"),
    ],
    ("places", "get_mcc_code"): [
        ("mcc_codes", lambda r: [r] if isinstance(r, dict) and r.get("merchantCategoryCode") else [], "merchantCategoryCode"),
    ],
    ("places", "list_industry_codes"): [
        ("industry_codes", lambda r: r.get("items", []) if isinstance(r, dict) else [], "industry"),
    ],
    ("places", "get_industry_code"): [
        ("industry_codes", lambda r: [r] if isinstance(r, dict) and r.get("industry") else [], "industry"),
    ],

    # ── TxNotify ───────────────────────────────────────────────────────────
    ("txnotify", "trigger_transaction"): [
        ("transactions", lambda r: [r] if isinstance(r, dict) and r.get("transUid") else [], "transUid"),
    ],
    ("txnotify", "get_undelivered"): [
        ("undelivered_notifications", lambda r: r.get("notifications", []) if isinstance(r, dict) else [], "id"),
    ],

    # ── Consent ────────────────────────────────────────────────────────────
    ("consent", "create_consent"): [
        ("consents", lambda r: [r] if isinstance(r, dict) and r.get("cardReference") else [], "cardReference"),
    ],
    ("consent", "get_consents"): [
        ("consents", lambda r: [r] if isinstance(r, dict) and r.get("cardReference") else [], "cardReference"),
    ],

    # ── EasySavings ────────────────────────────────────────────────────────
    ("easysavings", "list_countries"): [
        ("countries", lambda r: r if isinstance(r, list) else [], "countryCode"),
    ],
    ("easysavings", "list_offers"): [
        ("offers", lambda r: r.get("offers", []) if isinstance(r, dict) else [], "id"),
    ],
    ("easysavings", "get_offer"): [
        ("offers", lambda r: [r] if isinstance(r, dict) and r.get("id") else [], "id"),
    ],
    ("easysavings", "redeem_offer"): [
        ("redemptions", lambda r: [r] if isinstance(r, dict) and r.get("orderId") else [], "orderId"),
    ],

    # ── OFMC ───────────────────────────────────────────────────────────────
    ("ofmc", "search_categories"): [
        ("categories", lambda r: r.get("categories", []) if isinstance(r, dict) else [], "id"),
    ],
    ("ofmc", "list_sources"): [
        ("sources", lambda r: r.get("sources", []) if isinstance(r, dict) else [], "uuid"),
    ],
    ("ofmc", "get_source"): [
        ("sources", lambda r: [r] if isinstance(r, dict) and r.get("uuid") else [], "uuid"),
    ],
    ("ofmc", "create_merchant"): [
        ("merchants", lambda r: [r] if isinstance(r, dict) and r.get("uuid") else [], "uuid"),
    ],
    ("ofmc", "get_merchant"): [
        ("merchants", lambda r: [r] if isinstance(r, dict) and r.get("uuid") else [], "uuid"),
    ],
    ("ofmc", "list_offers"): [
        ("offers", lambda r: r.get("offers", []) if isinstance(r, dict) else [], "id"),
    ],
    ("ofmc", "get_offer"): [
        ("offers", lambda r: [r] if isinstance(r, dict) and r.get("id") else [], "id"),
    ],

    # ── OFPUB ──────────────────────────────────────────────────────────────
    ("ofpub", "list_offers"): [
        ("offers", lambda r: r.get("offers", []) if isinstance(r, dict) else [], "id"),
    ],
    ("ofpub", "get_offer"): [
        ("offers", lambda r: [r] if isinstance(r, dict) and r.get("id") else [], "id"),
    ],

    # ── Priceless ──────────────────────────────────────────────────────────
    ("priceless", "platform_products"): [
        (
            "platform_products",
            lambda r: r.get("data", []) if isinstance(r, dict) and isinstance(r.get("data"), list) else [],
            "id",
        ),
    ],
    ("priceless", "platform_categories"): [
        (
            "platform_categories",
            lambda r: r.get("data", []) if isinstance(r, dict) and isinstance(r.get("data"), list) else [],
            "id",
        ),
    ],
    ("priceless", "platform_programs"): [
        (
            "platform_programs",
            lambda r: r.get("data", []) if isinstance(r, dict) and isinstance(r.get("data"), list) else [],
            "id",
        ),
    ],
    ("priceless", "specials_offers"): [
        ("specials_offers", lambda r: r if isinstance(r, list) else [], "id"),
    ],
    ("priceless", "specials_benefits"): [
        ("specials_benefits", lambda r: r if isinstance(r, list) else [], "id"),
    ],
    ("priceless", "specials_programs"): [
        ("specials_programs", lambda r: r if isinstance(r, list) else [], "id"),
    ],
    ("priceless", "specials_merchants"): [
        ("specials_merchants", lambda r: r if isinstance(r, list) else [], "id"),
    ],
    ("priceless", "specials_categories"): [
        ("specials_categories", lambda r: r if isinstance(r, list) else [], "id"),
    ],
    ("priceless", "specials_countries"): [
        ("specials_countries", lambda r: r if isinstance(r, list) else [], "countryCode"),
    ],
    ("priceless", "specials_languages"): [
        ("specials_languages", lambda r: r if isinstance(r, list) else [], "id"),
    ],
    ("priceless", "specials_mastercard_products"): [
        ("specials_mastercard_products", lambda r: r if isinstance(r, list) else [], "id"),
    ],

    # ── Open Finance (OFIN) ────────────────────────────────────────────────
    ("ofin", "list_customers"): [
        ("customers", lambda r: r.get("customers", []) if isinstance(r, dict) else [], "id"),
    ],
    ("ofin", "get_customer"): [
        ("customers", lambda r: [r] if isinstance(r, dict) and r.get("id") else [], "id"),
    ],
    ("ofin", "refresh_accounts"): [
        ("accounts", lambda r: r.get("accounts", []) if isinstance(r, dict) else [], "id"),
    ],
    ("ofin", "get_accounts"): [
        ("accounts", lambda r: r.get("accounts", []) if isinstance(r, dict) else [], "id"),
    ],
    ("ofin", "get_transactions"): [
        ("transactions", lambda r: r.get("transactions", []) if isinstance(r, dict) else [], "id"),
    ],
    ("ofin", "get_account_transactions"): [
        ("transactions", lambda r: r.get("transactions", []) if isinstance(r, dict) else [], "id"),
    ],
    ("ofin", "list_institutions"): [
        ("institutions", lambda r: r.get("institutions", []) if isinstance(r, dict) else [], "id"),
    ],
    ("ofin", "generate_transactions_report"): [
        ("reports", lambda r: [r] if isinstance(r, dict) and r.get("id") else [], "id"),
    ],
}


def capture_response(api: str, op_id: str, resp_body: Any) -> int:
    """Upsert records from a live API response into the simulator DB.

    Returns the number of records captured (0 if no mapping exists or body is None).
    """
    if resp_body is None:
        return 0
    specs = CAPTURE_MAP.get((api, op_id))
    if not specs:
        return 0

    total = 0
    for resource, extractor, id_field in specs:
        try:
            records = extractor(resp_body)
            if records:
                store.upsert_many(api, resource, records, id_field)
                total += len(records)
        except Exception:
            pass
    return total
