"""Capture live sandbox responses into per-API simulator DBs.

When a real Mastercard sandbox call succeeds, the response body is passed to
capture_response(). CAPTURE_MAP maps (api_slug, op_id) → list of
(resource_collection, extractor_fn, id_field) tuples. Each extractor pulls a
list of records from the raw response body and upserts them into the per-API DB.
"""
from __future__ import annotations

from collections.abc import Callable
from typing import Any

from simulator.datastore import store

# ---------------------------------------------------------------------------
# Mapping: (api_slug, op_id) → [(resource, extractor, id_field), ...]
# extractor(resp_body) must return a list of dicts
# ---------------------------------------------------------------------------
CaptureSpec = tuple[str, Callable[[Any], list[dict]], str]

CAPTURE_MAP: dict[tuple[str, str], list[CaptureSpec]] = {
    # ── BIN Lookup ─────────────────────────────────────────────────────────
    ("bin_lookup", "lookup_bin"): [
        ("bins", lambda r: r.get("items", []) if isinstance(r, dict) else [], "binNum"),
    ],

    # ── BCES ───────────────────────────────────────────────────────────────
    ("benefits_content_eligibility", "search_contents"): [
        ("benefit_contents", lambda r: r.get("bundles", []) if isinstance(r, dict) else [], "id"),
    ],

    # ── Clarity ────────────────────────────────────────────────────────────
    ("consumer_clarity", "search_merchant"): [
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
    ("benefits_eligibility", "search_benefits"): [
        ("benefits", lambda r: r.get("data", []) if isinstance(r, dict) else [], "benefitCode"),
    ],
    ("benefits_eligibility", "search_products"): [
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
    ("transaction_notifications", "trigger_transaction"): [
        ("transactions", lambda r: [r] if isinstance(r, dict) and r.get("transUid") else [], "transUid"),
    ],
    ("transaction_notifications", "get_undelivered"): [
        ("undelivered_notifications", lambda r: r.get("notifications", []) if isinstance(r, dict) else [], "id"),
    ],

    # ── Consent ────────────────────────────────────────────────────────────
    ("consent_management", "create_consent"): [
        ("consents", lambda r: [r] if isinstance(r, dict) and r.get("cardReference") else [], "cardReference"),
    ],
    ("consent_management", "get_consents"): [
        ("consents", lambda r: [r] if isinstance(r, dict) and r.get("cardReference") else [], "cardReference"),
    ],

    # ── EasySavings ────────────────────────────────────────────────────────
    ("easy_savings", "list_countries"): [
        ("countries", lambda r: r if isinstance(r, list) else [], "countryCode"),
    ],
    ("easy_savings", "list_offers"): [
        ("offers", lambda r: r.get("offers", []) if isinstance(r, dict) else [], "id"),
    ],
    ("easy_savings", "get_offer"): [
        ("offers", lambda r: [r] if isinstance(r, dict) and r.get("id") else [], "id"),
    ],
    ("easy_savings", "redeem_offer"): [
        ("redemptions", lambda r: [r] if isinstance(r, dict) and r.get("orderId") else [], "orderId"),
    ],

    # ── OFMC ───────────────────────────────────────────────────────────────
    ("offers_merchant_content", "search_categories"): [
        ("categories", lambda r: r.get("categories", []) if isinstance(r, dict) else [], "id"),
    ],
    ("offers_merchant_content", "list_sources"): [
        ("sources", lambda r: r.get("sources", []) if isinstance(r, dict) else [], "uuid"),
    ],
    ("offers_merchant_content", "get_source"): [
        ("sources", lambda r: [r] if isinstance(r, dict) and r.get("uuid") else [], "uuid"),
    ],
    ("offers_merchant_content", "create_merchant"): [
        ("merchants", lambda r: [r] if isinstance(r, dict) and r.get("uuid") else [], "uuid"),
    ],
    ("offers_merchant_content", "get_merchant"): [
        ("merchants", lambda r: [r] if isinstance(r, dict) and r.get("uuid") else [], "uuid"),
    ],
    ("offers_merchant_content", "list_offers"): [
        ("offers", lambda r: r.get("offers", []) if isinstance(r, dict) else [], "id"),
    ],
    ("offers_merchant_content", "get_offer"): [
        ("offers", lambda r: [r] if isinstance(r, dict) and r.get("id") else [], "id"),
    ],

    # ── OFPUB ──────────────────────────────────────────────────────────────
    ("offers_for_publishers", "list_offers"): [
        ("offers", lambda r: r.get("offers", []) if isinstance(r, dict) else [], "id"),
    ],
    ("offers_for_publishers", "get_offer"): [
        ("offers", lambda r: [r] if isinstance(r, dict) and r.get("id") else [], "id"),
    ],

    # ── Priceless ──────────────────────────────────────────────────────────
    ("priceless_cities", "platform_products"): [
        (
            "platform_products",
            lambda r: r.get("data", []) if isinstance(r, dict) and isinstance(r.get("data"), list) else [],
            "id",
        ),
    ],
    ("priceless_cities", "platform_categories"): [
        (
            "platform_categories",
            lambda r: r.get("data", []) if isinstance(r, dict) and isinstance(r.get("data"), list) else [],
            "id",
        ),
    ],
    ("priceless_cities", "platform_programs"): [
        (
            "platform_programs",
            lambda r: r.get("data", []) if isinstance(r, dict) and isinstance(r.get("data"), list) else [],
            "id",
        ),
    ],
    ("priceless_cities", "specials_offers"): [
        ("specials_offers", lambda r: r if isinstance(r, list) else [], "id"),
    ],
    ("priceless_cities", "specials_benefits"): [
        ("specials_benefits", lambda r: r if isinstance(r, list) else [], "id"),
    ],
    ("priceless_cities", "specials_programs"): [
        ("specials_programs", lambda r: r if isinstance(r, list) else [], "id"),
    ],
    ("priceless_cities", "specials_merchants"): [
        ("specials_merchants", lambda r: r if isinstance(r, list) else [], "id"),
    ],
    ("priceless_cities", "specials_categories"): [
        ("specials_categories", lambda r: r if isinstance(r, list) else [], "id"),
    ],
    ("priceless_cities", "specials_countries"): [
        ("specials_countries", lambda r: r if isinstance(r, list) else [], "countryCode"),
    ],
    ("priceless_cities", "specials_languages"): [
        ("specials_languages", lambda r: r if isinstance(r, list) else [], "id"),
    ],
    ("priceless_cities", "specials_mastercard_products"): [
        ("specials_mastercard_products", lambda r: r if isinstance(r, list) else [], "id"),
    ],

    # ── Open Finance (OFIN) ────────────────────────────────────────────────
    ("open_finance", "list_customers"): [
        ("customers", lambda r: r.get("customers", []) if isinstance(r, dict) else [], "id"),
    ],
    ("open_finance", "get_customer"): [
        ("customers", lambda r: [r] if isinstance(r, dict) and r.get("id") else [], "id"),
    ],
    ("open_finance", "refresh_accounts"): [
        ("accounts", lambda r: r.get("accounts", []) if isinstance(r, dict) else [], "id"),
    ],
    ("open_finance", "get_accounts"): [
        ("accounts", lambda r: r.get("accounts", []) if isinstance(r, dict) else [], "id"),
    ],
    ("open_finance", "get_transactions"): [
        ("transactions", lambda r: r.get("transactions", []) if isinstance(r, dict) else [], "id"),
    ],
    ("open_finance", "get_account_transactions"): [
        ("transactions", lambda r: r.get("transactions", []) if isinstance(r, dict) else [], "id"),
    ],
    ("open_finance", "list_institutions"): [
        ("institutions", lambda r: r.get("institutions", []) if isinstance(r, dict) else [], "id"),
    ],
    ("open_finance", "generate_transactions_report"): [
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
