"""Mastercard Offers Merchant Content (eop-admin) API — OAuth 1.0a.

Lets external partners (merchants, aggregators) push merchant profiles,
offers, images and category metadata into the Offers platform.

Base URLs:
  Sandbox    https://sandbox.api.mastercard.com/loyalty/offers/eop
  Production https://api.mastercard.com/loyalty/offers/eop

Docs:
  https://developer.mastercard.com/eop-admin/documentation/
  https://developer.mastercard.com/eop-admin/documentation/api-reference/
"""
from __future__ import annotations

import json
import os
from typing import Any, Dict
from urllib.parse import urlencode

_SANDBOX_BASE = "https://sandbox.api.mastercard.com/loyalty/offers/eop"
_PROD_BASE    = "https://api.mastercard.com/loyalty/offers/eop"


MANIFEST: Dict[str, Any] = {
    "id": "ofmc",
    "name": "Offers Merchant Content",
    "description": (
        "Mastercard Offers Merchant Content — push merchant profiles, offers, "
        "images and categories into the Mastercard Offers platform so they "
        "can be presented to cardholders via the Offers for Publishers API."
    ),
    "docs_url": "https://developer.mastercard.com/eop-admin/documentation/",
    "how_to": (
        "<p><strong>Offers Merchant Content</strong> is the ingestion side of "
        "the Mastercard Offers platform. Partners use it to onboard merchants "
        "and load offers that are later surfaced through "
        "<strong>Offers for Publishers</strong>.</p>"
        "<h3>Typical flow</h3>"
        "<ol>"
        "<li>Use <strong>Categories → Search categories</strong> to find the "
        "<code>uuid</code> of the category your merchant belongs to.</li>"
        "<li>Use <strong>Sources → List sources</strong> to find the "
        "<code>uuid</code> of the source / publisher contract you are loading "
        "content for.</li>"
        "<li>Use <strong>Merchants → Create merchant</strong> with the chosen "
        "<code>category</code> + <code>source</code> to register a merchant "
        "profile, then optionally <strong>Add merchant address</strong>.</li>"
        "<li>Use <strong>Merchants → Upload image</strong> (under 900 KB, "
        "Base64-encoded) to attach a logo or lifestyle image.</li>"
        "<li>Use <strong>Offers → Create offer</strong> to publish an offer "
        "tied to the merchant and source.</li>"
        "</ol>"
        "<h3>Sandbox tips</h3>"
        "<ul>"
        "<li>The sandbox accepts arbitrary UUIDs as long as the request body "
        "validates — use it to exercise schemas and OAuth signing.</li>"
        "<li>Image uploads must be Base64-encoded; this Explorer accepts the "
        "raw Base64 string in the <code>imageBase64</code> field.</li>"
        "</ul>"
    ),
    "categories": ["Categories", "Sources", "Merchants", "Images", "Offers"],
    "state_schema": [],
    "configured": bool(
        os.environ.get("OFMC_CONSUMER_KEY")
        and os.environ.get("OFMC_CONSUMER_KEY") != "your-consumer-key-here"
        and os.environ.get("OFMC_SIGNING_KEY_PATH")
    ),
    "operations": [
        # ---- Categories --------------------------------------------------
        {
            "id": "search_categories",
            "name": "Search categories",
            "category": "Categories",
            "method": "POST",
            "description": "Search for categories that can be assigned when creating a merchant.",
            "params": [
                {"name": "countries", "label": "countries (comma-separated ISO-3)", "type": "text", "default": "USA", "required": False},
                {"name": "limit",     "label": "limit",                              "type": "text", "default": "10", "required": False},
                {"name": "offset",    "label": "offset",                             "type": "text", "default": "0",  "required": False},
            ],
        },
        # ---- Sources -----------------------------------------------------
        {
            "id": "list_sources",
            "name": "List sources",
            "category": "Sources",
            "method": "GET",
            "description": "List the merchant-content sources available to the caller.",
            "params": [
                {"name": "limit",  "label": "limit",  "type": "text", "default": "10", "required": False},
                {"name": "offset", "label": "offset", "type": "text", "default": "0",  "required": False},
            ],
        },
        {
            "id": "get_source",
            "name": "Get source by UUID",
            "category": "Sources",
            "method": "GET",
            "description": "Retrieve a single source (with assigned publishers and their programmes).",
            "params": [
                {"name": "source_uuid", "label": "source_uuid", "type": "text", "default": "", "required": True},
            ],
        },
        # ---- Merchants ---------------------------------------------------
        {
            "id": "create_merchant",
            "name": "Create merchant",
            "category": "Merchants",
            "method": "POST",
            "description": "Create a new merchant profile using a category + source.",
            "params": [
                {"name": "name",                  "label": "name",                     "type": "text", "default": "acme_shoes", "required": True},
                {"name": "display_name",          "label": "displayName",              "type": "text", "default": "Acme Shoes", "required": True},
                {"name": "external_merchant_id",  "label": "externalMerchantId",       "type": "text", "default": "ext-001",   "required": True},
                {"name": "country",               "label": "country (ISO-3)",          "type": "text", "default": "USA",       "required": True},
                {"name": "language",              "label": "language (e.g. en-US)",    "type": "text", "default": "en-US",     "required": True},
                {"name": "channel",               "label": "channel (ONLINE/INSTORE/UNKNOWN)", "type": "select", "options": ["ONLINE", "INSTORE", "UNKNOWN"], "default": "ONLINE", "required": True},
                {"name": "source_type",           "label": "sourceType",               "type": "select", "options": ["SINGLE_SOURCE", "MULTI_SOURCE"], "default": "SINGLE_SOURCE", "required": True},
                {"name": "origin",                "label": "origin",                   "type": "select", "options": ["BMI_API", "AGGREGATOR_API"], "default": "AGGREGATOR_API", "required": True},
                {"name": "website_url",           "label": "websiteUrl",               "type": "text", "default": "https://example.com", "required": False},
                {"name": "description",           "label": "description",              "type": "text", "default": "Sample merchant.",     "required": False},
                {"name": "category",              "label": "category (name)",          "type": "text", "default": "Shoes", "required": True},
                {"name": "subcategory_uuid",      "label": "subCategory.uuid",         "type": "text", "default": "", "required": True},
                {"name": "source_uuid",           "label": "source.uuid",              "type": "text", "default": "", "required": True},
                {"name": "source_name",           "label": "source.name",              "type": "text", "default": "", "required": False},
            ],
        },
        {
            "id": "get_merchant",
            "name": "Get merchant by ID",
            "category": "Merchants",
            "method": "GET",
            "description": "Retrieve a merchant by UUID.",
            "params": [
                {"name": "merchant_id", "label": "merchant_id (UUID)", "type": "text", "default": "", "required": True},
            ],
        },
        {
            "id": "update_merchant",
            "name": "Update merchant",
            "category": "Merchants",
            "method": "PUT",
            "description": "Update mutable fields on an existing merchant.",
            "params": [
                {"name": "merchant_id",  "label": "merchant_id (UUID)", "type": "text", "default": "", "required": True},
                {"name": "display_name", "label": "displayName",        "type": "text", "default": "", "required": False},
                {"name": "description",  "label": "description",        "type": "text", "default": "", "required": False},
                {"name": "website_url",  "label": "websiteUrl",         "type": "text", "default": "", "required": False},
                {"name": "status",       "label": "status",             "type": "select", "options": ["", "ACTIVE"], "default": "", "required": False},
            ],
        },
        {
            "id": "add_merchant_address",
            "name": "Add merchant address",
            "category": "Merchants",
            "method": "POST",
            "description": "Add the physical address + Mastercard location IDs for a merchant.",
            "params": [
                {"name": "merchant_id",  "label": "merchant_id (UUID)", "type": "text", "default": "", "required": True},
                {"name": "address_line1","label": "addressLine1",       "type": "text", "default": "1 Main St", "required": True},
                {"name": "city",         "label": "city",               "type": "text", "default": "New York",  "required": True},
                {"name": "postal_code",  "label": "postalCode",         "type": "text", "default": "10001",     "required": True},
                {"name": "country",      "label": "country (ISO-3)",    "type": "text", "default": "USA",       "required": True},
                {"name": "location_id",  "label": "Mastercard locationId", "type": "text", "default": "", "required": True},
            ],
        },
        # ---- Images ------------------------------------------------------
        {
            "id": "list_merchant_images",
            "name": "List merchant images",
            "category": "Images",
            "method": "GET",
            "description": "Return all images attached to a merchant.",
            "params": [
                {"name": "merchant_id", "label": "merchant_id (UUID)", "type": "text", "default": "", "required": True},
            ],
        },
        {
            "id": "upload_merchant_image",
            "name": "Upload merchant image (<900 KB)",
            "category": "Images",
            "method": "POST",
            "description": "Upload an image (Base64-encoded) to be used as a logo or lifestyle image.",
            "params": [
                {"name": "merchant_id",  "label": "merchant_id (UUID)",        "type": "text",     "default": "", "required": True},
                {"name": "image_class",  "label": "class (MERCHANT_LOGO / OFFER_IMAGE)", "type": "select", "options": ["MERCHANT_LOGO", "OFFER_IMAGE"], "default": "MERCHANT_LOGO", "required": True},
                {"name": "image_name",   "label": "name",                       "type": "text",     "default": "logo.png", "required": True},
                {"name": "image_base64", "label": "imageBase64 (raw Base64)",   "type": "textarea", "default": "", "required": True},
            ],
        },
        # ---- Offers ------------------------------------------------------
        {
            "id": "create_offer",
            "name": "Create offer",
            "category": "Offers",
            "method": "POST",
            "description": "Create an offer for a merchant under a publisher contract.",
            "params": [
                {"name": "merchant_uuid",        "label": "merchant.uuid",         "type": "text",     "default": "", "required": True},
                {"name": "source_uuid",          "label": "source.uuid",           "type": "text",     "default": "", "required": True},
                {"name": "name",                 "label": "name",                  "type": "text",     "default": "sample_offer", "required": True},
                {"name": "headline",             "label": "headline",              "type": "text",     "default": "Save 10% at Acme Shoes", "required": True},
                {"name": "description_long",     "label": "descriptionLong",       "type": "textarea", "default": "Get 10% off your next purchase at Acme Shoes when you pay with your Mastercard.", "required": True},
                {"name": "terms",                "label": "terms",                 "type": "textarea", "default": "Offer valid for one transaction. T&Cs apply.", "required": False},
                {"name": "event_start_date",     "label": "eventStartDate (YYYY-MM-DD)", "type": "text", "default": "2026-01-01", "required": True},
                {"name": "event_end_date",       "label": "eventEndDate (YYYY-MM-DD)",   "type": "text", "default": "2026-12-31", "required": True},
                {"name": "discount_type",        "label": "rewards.discountType",  "type": "select",   "options": ["PERCENTAGE", "ABSOLUTE"], "default": "PERCENTAGE", "required": True},
                {"name": "percentage",           "label": "rewards.percentage",    "type": "text",     "default": "10", "required": False},
                {"name": "cash_value_absolute",  "label": "rewards.cashValueAbsolute", "type": "text", "default": "",   "required": False},
                {"name": "currency",             "label": "currency (ISO-4217)",   "type": "text",     "default": "USD", "required": True},
                {"name": "redemption_channel",   "label": "redemptionChannel",     "type": "select",   "options": ["INSTORE", "ONLINE", "ONLINE-INSTORE"], "default": "ONLINE", "required": True},
                {"name": "lang",                 "label": "localizations[].lang",  "type": "text",     "default": "en-US", "required": True},
            ],
        },
    ],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _base_url() -> str:
    env = os.environ.get("OFMC_ENV", "sandbox").lower()
    return _PROD_BASE if env == "production" else _SANDBOX_BASE


def _configured() -> bool:
    key = os.environ.get("OFMC_CONSUMER_KEY", "")
    path = os.environ.get("OFMC_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    return _configured()


def get_state() -> Dict[str, Any]:
    return {"configured": _configured()}


def _not_configured_err() -> Dict[str, Any]:
    return {
        "success": False,
        "error": (
            "Offers Merchant Content is not configured. Set OFMC_CONSUMER_KEY "
            "and OFMC_SIGNING_KEY_PATH in .env, then restart the server."
        ),
    }


def _resolve_key_path(path: str) -> str:
    if os.path.isabs(path):
        return path
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(project_root, path)


def _signed_request(method: str, url: str, body_str: str | None) -> Dict[str, Any]:
    import requests
    import oauth1.authenticationutils as authutils
    from oauth1.oauth import OAuth

    consumer_key = os.environ["OFMC_CONSUMER_KEY"]
    key_path     = _resolve_key_path(os.environ["OFMC_SIGNING_KEY_PATH"])
    key_password = os.environ.get("OFMC_SIGNING_KEY_PASSWORD", "keystorepassword")

    headers = {"Accept": "application/json"}
    if body_str is not None:
        headers["Content-Type"] = "application/json"

    try:
        signing_key = authutils.load_signing_key(key_path, key_password)
        auth_header = OAuth.get_authorization_header(
            url, method, body_str or "", consumer_key, signing_key
        )
        headers["Authorization"] = auth_header
    except Exception as exc:
        return {"success": False, "error": f"OAuth signing failed: {exc}"}

    try:
        resp = requests.request(
            method=method,
            url=url,
            data=body_str,
            headers=headers,
            timeout=20,
        )
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
        "request": {"method": method, "url": url, "body": body_str},
        "response": {"status_code": status_code, "body": resp_body},
        "state_updates": {},
    }


def _qs(params: Dict[str, Any]) -> str:
    items = {k: v for k, v in params.items() if v not in (None, "", [])}
    return ("?" + urlencode(items)) if items else ""


# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------
def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if not _configured():
        return _not_configured_err()
    dispatch = {
        "search_categories":     _search_categories,
        "list_sources":          _list_sources,
        "get_source":            _get_source,
        "create_merchant":       _create_merchant,
        "get_merchant":          _get_merchant,
        "update_merchant":       _update_merchant,
        "add_merchant_address":  _add_merchant_address,
        "list_merchant_images":  _list_merchant_images,
        "upload_merchant_image": _upload_merchant_image,
        "create_offer":          _create_offer,
    }
    fn = dispatch.get(op_id)
    if not fn:
        return {"success": False, "error": f"Unknown operation: {op_id}"}
    return fn(params)


def _search_categories(p: Dict[str, Any]) -> Dict[str, Any]:
    countries = [c.strip() for c in (p.get("countries") or "").split(",") if c.strip()]
    body: Dict[str, Any] = {
        "limit":  int((p.get("limit")  or "10").strip() or 10),
        "offset": int((p.get("offset") or "0").strip()  or 0),
    }
    if countries:
        body["countries"] = countries
    return _signed_request("POST", f"{_base_url()}/categories/category-searches", json.dumps(body))


def _list_sources(p: Dict[str, Any]) -> Dict[str, Any]:
    qs = _qs({"limit": p.get("limit") or "10", "offset": p.get("offset") or "0"})
    return _signed_request("GET", f"{_base_url()}/sources{qs}", None)


def _get_source(p: Dict[str, Any]) -> Dict[str, Any]:
    uuid_ = (p.get("source_uuid") or "").strip()
    if not uuid_:
        return {"success": False, "error": "'source_uuid' is required."}
    return _signed_request("GET", f"{_base_url()}/sources/{uuid_}", None)


def _create_merchant(p: Dict[str, Any]) -> Dict[str, Any]:
    sub_uuid    = (p.get("subcategory_uuid") or "").strip()
    source_uuid = (p.get("source_uuid") or "").strip()
    if not sub_uuid or not source_uuid:
        return {"success": False, "error": "'subcategory_uuid' and 'source_uuid' are required."}

    body: Dict[str, Any] = {
        "name":               (p.get("name") or "").strip(),
        "displayName":        (p.get("display_name") or "").strip(),
        "externalMerchantId": (p.get("external_merchant_id") or "").strip(),
        "country":            (p.get("country") or "USA").strip(),
        "language":           (p.get("language") or "en-US").strip(),
        "channel":            (p.get("channel") or "ONLINE").strip(),
        "sourceType":         (p.get("source_type") or "SINGLE_SOURCE").strip(),
        "origin":             (p.get("origin") or "AGGREGATOR_API").strip(),
        "category":           (p.get("category") or "").strip(),
        "subCategory":        {"uuid": sub_uuid, "categoryType": "CATEGORY"},
        "source":             {"uuid": source_uuid},
    }
    src_name = (p.get("source_name") or "").strip()
    if src_name:
        body["source"]["name"] = src_name
    for k_in, k_out in (("website_url", "websiteUrl"), ("description", "description")):
        v = (p.get(k_in) or "").strip()
        if v:
            body[k_out] = v
    return _signed_request("POST", f"{_base_url()}/merchants", json.dumps(body))


def _get_merchant(p: Dict[str, Any]) -> Dict[str, Any]:
    mid = (p.get("merchant_id") or "").strip()
    if not mid:
        return {"success": False, "error": "'merchant_id' is required."}
    return _signed_request("GET", f"{_base_url()}/merchants/{mid}", None)


def _update_merchant(p: Dict[str, Any]) -> Dict[str, Any]:
    mid = (p.get("merchant_id") or "").strip()
    if not mid:
        return {"success": False, "error": "'merchant_id' is required."}
    body: Dict[str, Any] = {}
    for k_in, k_out in (
        ("display_name", "displayName"),
        ("description",  "description"),
        ("website_url",  "websiteUrl"),
        ("status",       "status"),
    ):
        v = (p.get(k_in) or "").strip()
        if v:
            body[k_out] = v
    return _signed_request("PUT", f"{_base_url()}/merchants/{mid}", json.dumps(body))


def _add_merchant_address(p: Dict[str, Any]) -> Dict[str, Any]:
    mid = (p.get("merchant_id") or "").strip()
    if not mid:
        return {"success": False, "error": "'merchant_id' is required."}
    body = {
        "addressLine1": (p.get("address_line1") or "").strip(),
        "city":         (p.get("city") or "").strip(),
        "postalCode":   (p.get("postal_code") or "").strip(),
        "country":      (p.get("country") or "").strip(),
        "locationIds":  [(p.get("location_id") or "").strip()],
    }
    return _signed_request("POST", f"{_base_url()}/merchants/{mid}/addresses", json.dumps(body))


def _list_merchant_images(p: Dict[str, Any]) -> Dict[str, Any]:
    mid = (p.get("merchant_id") or "").strip()
    if not mid:
        return {"success": False, "error": "'merchant_id' is required."}
    return _signed_request("GET", f"{_base_url()}/merchants/{mid}/images", None)


def _upload_merchant_image(p: Dict[str, Any]) -> Dict[str, Any]:
    mid    = (p.get("merchant_id") or "").strip()
    b64    = (p.get("image_base64") or "").strip()
    name   = (p.get("image_name") or "").strip() or "image"
    klass  = (p.get("image_class") or "MERCHANT_LOGO").strip()
    if not mid or not b64:
        return {"success": False, "error": "'merchant_id' and 'image_base64' are required."}
    body = {"name": name, "class": klass, "image": b64}
    return _signed_request("POST", f"{_base_url()}/merchants/{mid}/images", json.dumps(body))


def _create_offer(p: Dict[str, Any]) -> Dict[str, Any]:
    merchant_uuid = (p.get("merchant_uuid") or "").strip()
    source_uuid   = (p.get("source_uuid") or "").strip()
    if not merchant_uuid or not source_uuid:
        return {"success": False, "error": "'merchant_uuid' and 'source_uuid' are required."}

    rewards: Dict[str, Any] = {
        "discountType": (p.get("discount_type") or "PERCENTAGE").strip(),
        "type":         "STATEMENT_CREDIT",
        "mode":         "CASH",
    }
    pct = (p.get("percentage") or "").strip()
    if pct:
        try:
            rewards["percentage"] = float(pct)
        except ValueError:
            pass
    cva = (p.get("cash_value_absolute") or "").strip()
    if cva:
        try:
            rewards["cashValueAbsolute"] = float(cva)
        except ValueError:
            pass

    body = {
        "name":              (p.get("name") or "").strip(),
        "merchant":          {"uuid": merchant_uuid},
        "source":            {"uuid": source_uuid},
        "currency":          (p.get("currency") or "USD").strip(),
        "redemptionChannel": (p.get("redemption_channel") or "ONLINE").strip(),
        "eventStartDate":    (p.get("event_start_date") or "").strip(),
        "eventEndDate":      (p.get("event_end_date") or "").strip(),
        "rewards":           [rewards],
        "localizations": [{
            "lang":            (p.get("lang") or "en-US").strip(),
            "headline":        (p.get("headline") or "").strip(),
            "descriptionLong": (p.get("description_long") or "").strip(),
            "termsLong":       (p.get("terms") or "").strip(),
        }],
    }
    return _signed_request("POST", f"{_base_url()}/offers", json.dumps(body))
