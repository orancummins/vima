"""Priceless API — covers three Mastercard "Priceless" services:

* **Priceless Platform** (a.k.a. Mastercard Benefits & Experiences Portal) — the
  catalogue of products and experiences sold on priceless.com, exposed for
  partners.
* **Priceless Cities** — the location-driven slice of the Priceless Platform
  used to power priceless.com/cities. Implemented using the Platform's
  ``/locations``, ``/products?location_id=…`` and ``/products-locations``
  endpoints.
* **Priceless Specials** — the offers/benefits catalogue Mastercard publishes
  to issuers.

All three sit behind the same one-legged OAuth 1.0a scheme and (per the user
configuration) share a single ``pricelessgroup.p12`` keystore + consumer key.

References:
* https://developer.mastercard.com/mastercard-benefits-and-experiences-portal/documentation/
* https://developer.mastercard.com/priceless-specials/documentation/
"""
from __future__ import annotations

import os
from typing import Any, Dict, List, Tuple
from urllib.parse import urlencode

# --- Base URLs ------------------------------------------------------------

_PLATFORM_PROD    = "https://api.mastercard.com/the-portal"
_PLATFORM_SANDBOX = "https://sandbox.api.mastercard.com/the-portal"

_SPECIALS_PROD    = "https://api.mastercard.com/priceless/specials/platform"
_SPECIALS_SANDBOX = "https://sandbox.api.mastercard.com/priceless/specials/platform"


def _is_prod() -> bool:
    return os.environ.get("PRICELESS_ENV", "sandbox").lower() == "production"


def _platform_base() -> str:
    from simulator.switcher import is_simulated
    if is_simulated("priceless"):
        port = int(os.environ.get("PORT", 9021))
        return f"http://localhost:{port}/api-sim/priceless/platform"
    return _PLATFORM_PROD if _is_prod() else _PLATFORM_SANDBOX


def _specials_base() -> str:
    from simulator.switcher import is_simulated
    if is_simulated("priceless"):
        port = int(os.environ.get("PORT", 9021))
        return f"http://localhost:{port}/api-sim/priceless/specials"
    return _SPECIALS_PROD if _is_prod() else _SPECIALS_SANDBOX


# --- Configuration --------------------------------------------------------

def _configured() -> bool:
    key = os.environ.get("PRICELESS_CONSUMER_KEY", "")
    path = os.environ.get("PRICELESS_SIGNING_KEY_PATH", "")
    return bool(key and key != "your-consumer-key-here" and path)


def is_configured() -> bool:
    from simulator.switcher import is_simulated
    return _configured() or is_simulated("priceless")


def get_state() -> Dict[str, Any]:
    return {"configured": _configured()}


# --- Common option lists --------------------------------------------------

_LANGUAGE_OPTIONS = [
    {"value": "",       "label": "(default — English)"},
    {"value": "en-US",  "label": "en-US — English (United States)"},
    {"value": "en-GB",  "label": "en-GB — English (United Kingdom)"},
    {"value": "es-ES",  "label": "es-ES — Spanish"},
    {"value": "fr-FR",  "label": "fr-FR — French"},
    {"value": "de-DE",  "label": "de-DE — German"},
    {"value": "zh-CN",  "label": "zh-CN — Chinese (Simplified)"},
    {"value": "ja-JP",  "label": "ja-JP — Japanese"},
]

_LANGUAGE_CODE_OPTIONS = [  # Platform endpoints expect short codes (e.g. en, fr)
    {"value": "",   "label": "(default — English)"},
    {"value": "en", "label": "en — English"},
    {"value": "fr", "label": "fr — French"},
    {"value": "es", "label": "es — Spanish"},
    {"value": "de", "label": "de — German"},
    {"value": "it", "label": "it — Italian"},
    {"value": "pt", "label": "pt — Portuguese"},
    {"value": "zh", "label": "zh — Chinese"},
    {"value": "ja", "label": "ja — Japanese"},
]

_MARKET_OPTIONS = [
    {"value": "",   "label": "(any)"},
    {"value": "US", "label": "US — United States"},
    {"value": "GB", "label": "GB — United Kingdom"},
    {"value": "SG", "label": "SG — Singapore"},
    {"value": "HK", "label": "HK — Hong Kong"},
    {"value": "JP", "label": "JP — Japan"},
    {"value": "AU", "label": "AU — Australia"},
    {"value": "DE", "label": "DE — Germany"},
    {"value": "FR", "label": "FR — France"},
    {"value": "BR", "label": "BR — Brazil"},
    {"value": "IN", "label": "IN — India"},
]

_SPECIALS_CATEGORY_OPTIONS = [
    {"value": "",              "label": "(any)"},
    {"value": "Dining",        "label": "Dining"},
    {"value": "Shopping",      "label": "Shopping"},
    {"value": "Travel",        "label": "Travel"},
    {"value": "Entertainment", "label": "Entertainment"},
    {"value": "Sports",        "label": "Sports"},
    {"value": "Wellness",      "label": "Wellness"},
    {"value": "Lifestyle",     "label": "Lifestyle"},
]

_MC_PRODUCT_OPTIONS = [
    {"value": "",    "label": "(any)"},
    {"value": "MST", "label": "MST — Standard"},
    {"value": "MGD", "label": "MGD — Gold"},
    {"value": "MPL", "label": "MPL — Platinum"},
    {"value": "MWE", "label": "MWE — World Elite"},
    {"value": "MWP", "label": "MWP — World"},
    {"value": "MBC", "label": "MBC — Business"},
]


def _specials_filter_params() -> List[Dict[str, Any]]:
    return [
        {"name": "language",            "label": "Language",            "type": "select", "default": "", "required": False, "options": _LANGUAGE_OPTIONS},
        {"name": "eligible_markets",    "label": "Eligible Markets",    "type": "select", "default": "", "required": False, "options": _MARKET_OPTIONS,
         "help": "Country where the card is issued (ISO alpha-2)."},
        {"name": "destination_markets", "label": "Destination Markets", "type": "select", "default": "", "required": False, "options": _MARKET_OPTIONS,
         "help": "Country where the offer is redeemed (ISO alpha-2)."},
        {"name": "category",            "label": "Category",            "type": "select", "default": "", "required": False, "options": _SPECIALS_CATEGORY_OPTIONS},
        {"name": "mastercard_product",  "label": "Mastercard Product",  "type": "select", "default": "", "required": False, "options": _MC_PRODUCT_OPTIONS},
    ]


# --- Manifest -------------------------------------------------------------

_HOW_TO = (
    "<p><strong>Priceless</strong> bundles three Mastercard APIs that surface "
    "Mastercard's branded merchant-offer and experience catalogues:</p>"
    "<ul>"
    "<li><strong>Priceless Platform</strong> — the partner-facing catalogue "
    "behind <a href='https://priceless.com' target='_blank'>priceless.com</a>: "
    "products, categories, programs, languages, locations.</li>"
    "<li><strong>Priceless Cities</strong> — the city-by-city slice of the "
    "Platform that powers <em>priceless.com/cities</em>: list of supported "
    "cities/regions and the experiences available in each.</li>"
    "<li><strong>Priceless Specials</strong> — the lighter-weight offers and "
    "benefits feed issuers embed inside mobile/web banking.</li>"
    "</ul>"
    "<h3>How to use</h3>"
    "<ol>"
    "<li>Pick an operation from the panel on the left — they're grouped by "
    "service (Platform / Cities / Specials).</li>"
    "<li>Fill in the parameters. Most Platform &amp; Cities operations require "
    "a <code>partner_id</code> — your partner ID is provided by Priceless when "
    "the project is set up.</li>"
    "<li>Click <strong>Send</strong>. Responses are JSON; the Platform format "
    "is always <code>{ msg, data }</code>.</li>"
    "</ol>"
)

_PARTNER_ID_PARAM: Dict[str, Any] = {
    "name": "partner_id",
    "label": "Partner ID",
    "type": "text",
    "default": "1",
    "required": True,
    "help": "Your partner ID assigned by Priceless (integer).",
}


# --- Internal operation descriptors ---------------------------------------
#
# Each operation declares which service base URL it uses, the endpoint
# template (optionally with {path_params}), and the HTTP method.

_OPS: Dict[str, Dict[str, Any]] = {
    # Priceless Platform
    "platform_health":              {"service": "platform", "endpoint": "/health-checks",            "path_params": ()},
    "platform_products":            {"service": "platform", "endpoint": "/products",                 "path_params": ()},
    "platform_product_info":        {"service": "platform", "endpoint": "/products/{product_id}",    "path_params": ("product_id",)},
    "platform_product_inventory":   {"service": "platform", "endpoint": "/products/{product_id}/inventories",  "path_params": ("product_id",)},
    "platform_product_translations":{"service": "platform", "endpoint": "/products/{product_id}/translations", "path_params": ("product_id",)},
    "platform_categories":          {"service": "platform", "endpoint": "/categories",               "path_params": ()},
    "platform_programs":            {"service": "platform", "endpoint": "/programs",                 "path_params": ()},
    "platform_languages":           {"service": "platform", "endpoint": "/languages",                "path_params": ()},
    "platform_subscriptions":       {"service": "platform", "endpoint": "/subscriptions",            "path_params": ()},

    # Priceless Cities (uses Platform endpoints)
    "cities_list":                  {"service": "platform", "endpoint": "/locations",                "path_params": ()},
    "cities_products":              {"service": "platform", "endpoint": "/products",                 "path_params": ()},
    "cities_products_near_me":      {"service": "platform", "endpoint": "/products-locations",       "path_params": ()},

    # Priceless Specials
    "specials_offers":              {"service": "specials", "endpoint": "/offers",                   "path_params": ()},
    "specials_benefits":            {"service": "specials", "endpoint": "/benefits",                 "path_params": ()},
    "specials_programs":            {"service": "specials", "endpoint": "/programs",                 "path_params": ()},
    "specials_merchants":           {"service": "specials", "endpoint": "/merchants",                "path_params": ()},
    "specials_categories":          {"service": "specials", "endpoint": "/categories",               "path_params": ()},
    "specials_countries":           {"service": "specials", "endpoint": "/countries",                "path_params": ()},
    "specials_languages":           {"service": "specials", "endpoint": "/languages",                "path_params": ()},
    "specials_mastercard_products": {"service": "specials", "endpoint": "/mastercard-products",      "path_params": ()},
    "specials_card_products":       {"service": "specials", "endpoint": "/card-products",            "path_params": ()},
}


MANIFEST: Dict[str, Any] = {
    "id": "priceless",
    "name": "Priceless",
    "description": (
        "Mastercard's Priceless family of APIs — Priceless Platform "
        "(products/experiences), Priceless Cities (location-driven catalogue) "
        "and Priceless Specials (offers and benefits)."
    ),
    "docs_url": "https://developer.mastercard.com/product/priceless-platform-api",
    "how_to": _HOW_TO,
    "categories": ["Priceless Platform", "Priceless Cities", "Priceless Specials"],
    "deprecated_categories": ["Priceless Platform", "Priceless Cities"],
    "state_schema": [],
    "configured": _configured(),
    "operations": [
        # ===== Priceless Platform ============================================
        {
            "id": "platform_health",
            "name": "Health Check",
            "category": "Priceless Platform",
            "method": "GET",
            "description": "Pings the Priceless Platform gateway — handy to validate auth.",
            "params": [],
        },
        {
            "id": "platform_products",
            "name": "List Products",
            "category": "Priceless Platform",
            "method": "GET",
            "description": "Returns the catalogue of products mapped to your partner ID.",
            "params": [
                _PARTNER_ID_PARAM,
                {"name": "language_code", "label": "Language", "type": "select", "default": "", "required": False, "options": _LANGUAGE_CODE_OPTIONS},
                {"name": "location_id",   "label": "Location ID", "type": "text", "default": "", "required": False, "help": "Filter to a single city/region (see Cities → List Cities)."},
                {"name": "category_ids",  "label": "Category IDs", "type": "text", "default": "", "required": False, "help": "One or several comma-separated category IDs."},
                {"name": "program_id",    "label": "Program ID",  "type": "text", "default": "", "required": False},
                {"name": "bin",           "label": "BIN",         "type": "text", "default": "", "required": False, "help": "6–11 digit BIN to filter to eligible card products."},
                {"name": "checkout_only", "label": "Checkout only",
                 "type": "select", "default": "", "required": False,
                 "options": [
                     {"value": "",  "label": "(any)"},
                     {"value": "1", "label": "Yes — only products checkable via API"},
                     {"value": "0", "label": "No — show all"},
                 ]},
                {"name": "offset", "label": "Offset", "type": "text", "default": "", "required": False},
                {"name": "limit",  "label": "Limit",  "type": "text", "default": "", "required": False},
            ],
        },
        {
            "id": "platform_product_info",
            "name": "Get Product",
            "category": "Priceless Platform",
            "method": "GET",
            "description": "Returns the full details for a single product.",
            "params": [
                _PARTNER_ID_PARAM,
                {"name": "product_id",    "label": "Product ID", "type": "text", "default": "", "required": True},
                {"name": "language_code", "label": "Language", "type": "select", "default": "", "required": False, "options": _LANGUAGE_CODE_OPTIONS},
            ],
        },
        {
            "id": "platform_product_inventory",
            "name": "Get Product Inventory",
            "category": "Priceless Platform",
            "method": "GET",
            "description": "Returns the in-stock count for a product.",
            "params": [
                _PARTNER_ID_PARAM,
                {"name": "product_id", "label": "Product ID", "type": "text", "default": "", "required": True},
            ],
        },
        {
            "id": "platform_product_translations",
            "name": "Get Product Translations",
            "category": "Priceless Platform",
            "method": "GET",
            "description": "Lists the languages a product has been translated into.",
            "params": [
                _PARTNER_ID_PARAM,
                {"name": "product_id", "label": "Product ID", "type": "text", "default": "", "required": True},
            ],
        },
        {
            "id": "platform_categories",
            "name": "List Categories",
            "category": "Priceless Platform",
            "method": "GET",
            "description": "Returns the categories of products available to your partner.",
            "params": [
                _PARTNER_ID_PARAM,
                {"name": "language_code", "label": "Language", "type": "select", "default": "", "required": False, "options": _LANGUAGE_CODE_OPTIONS},
            ],
        },
        {
            "id": "platform_programs",
            "name": "List Programs",
            "category": "Priceless Platform",
            "method": "GET",
            "description": "Returns the Mastercard programs the catalogue is organised under.",
            "params": [
                _PARTNER_ID_PARAM,
                {"name": "language_code", "label": "Language", "type": "select", "default": "", "required": False, "options": _LANGUAGE_CODE_OPTIONS},
            ],
        },
        {
            "id": "platform_languages",
            "name": "List Languages",
            "category": "Priceless Platform",
            "method": "GET",
            "description": "Returns the languages product content has been translated into.",
            "params": [_PARTNER_ID_PARAM],
        },
        {
            "id": "platform_subscriptions",
            "name": "Get Subscriptions",
            "category": "Priceless Platform",
            "method": "GET",
            "description": "Returns the partner's active Mastercard subscriptions.",
            "params": [_PARTNER_ID_PARAM],
        },

        # ===== Priceless Cities =============================================
        {
            "id": "cities_list",
            "name": "List Cities & Regions",
            "category": "Priceless Cities",
            "method": "GET",
            "description": (
                "Lists every city / region (location) for which the partner has "
                "at least one Priceless experience. Each result includes a "
                "location ID that can be fed into 'List Experiences in City'."
            ),
            "params": [
                _PARTNER_ID_PARAM,
                {"name": "language_code", "label": "Language", "type": "select", "default": "", "required": False, "options": _LANGUAGE_CODE_OPTIONS},
            ],
        },
        {
            "id": "cities_products",
            "name": "List Experiences in City",
            "category": "Priceless Cities",
            "method": "GET",
            "description": "Returns Priceless experiences available in a given city/region.",
            "params": [
                _PARTNER_ID_PARAM,
                {"name": "location_id",   "label": "Location ID", "type": "text", "default": "", "required": True,
                 "help": "Get this from 'List Cities & Regions'."},
                {"name": "language_code", "label": "Language", "type": "select", "default": "", "required": False, "options": _LANGUAGE_CODE_OPTIONS},
                {"name": "category_ids",  "label": "Category IDs", "type": "text", "default": "", "required": False},
                {"name": "limit",         "label": "Limit",        "type": "text", "default": "", "required": False},
            ],
        },
        {
            "id": "cities_products_near_me",
            "name": "List Experiences Near Coordinates",
            "category": "Priceless Cities",
            "method": "GET",
            "description": "Returns Priceless experiences within a radius of a given geo location.",
            "params": [
                _PARTNER_ID_PARAM,
                {"name": "user_latitude",  "label": "Latitude",       "type": "text", "default": "40.7580",  "required": True,
                 "help": "e.g. 40.7580 for Times Square, New York."},
                {"name": "user_longitude", "label": "Longitude",      "type": "text", "default": "-73.9855", "required": True},
                {"name": "radius",         "label": "Radius (miles)", "type": "text", "default": "25",       "required": False},
                {"name": "language_code",  "label": "Language",       "type": "select", "default": "", "required": False, "options": _LANGUAGE_CODE_OPTIONS},
            ],
        },

        # ===== Priceless Specials ==========================================
        {
            "id": "specials_offers",
            "name": "Get Offers",
            "category": "Priceless Specials",
            "method": "GET",
            "description": "Returns Mastercard merchant offers (discounts / deals).",
            "params": _specials_filter_params() + [
                {"name": "offer_title", "label": "Offer Title contains", "type": "text", "default": "", "required": False},
                {"name": "tags",        "label": "Tags (comma list)",    "type": "text", "default": "", "required": False},
            ],
        },
        {
            "id": "specials_benefits",
            "name": "Get Benefits",
            "category": "Priceless Specials",
            "method": "GET",
            "description": "Returns Mastercard benefits tied to card products.",
            "params": _specials_filter_params() + [
                {"name": "sort", "label": "Sort", "type": "select", "default": "", "required": False,
                 "options": [
                     {"value": "",             "label": "(default)"},
                     {"value": "expiringsoon", "label": "Expiring soon"},
                     {"value": "newest",       "label": "Newest"},
                 ]},
            ],
        },
        {
            "id": "specials_programs",
            "name": "Get Programs",
            "category": "Priceless Specials",
            "method": "GET",
            "description": "Returns marketing programs (themed offer bundles).",
            "params": [
                {"name": "language",         "label": "Language",         "type": "select", "default": "", "required": False, "options": _LANGUAGE_OPTIONS},
                {"name": "eligible_markets", "label": "Eligible Markets", "type": "select", "default": "", "required": False, "options": _MARKET_OPTIONS},
            ],
        },
        {
            "id": "specials_merchants",
            "name": "Get Merchants",
            "category": "Priceless Specials",
            "method": "GET",
            "description": "Returns participating merchants.",
            "params": [
                {"name": "language",            "label": "Language",            "type": "select", "default": "", "required": False, "options": _LANGUAGE_OPTIONS},
                {"name": "eligible_markets",    "label": "Eligible Markets",    "type": "select", "default": "", "required": False, "options": _MARKET_OPTIONS},
                {"name": "destination_markets", "label": "Destination Markets", "type": "select", "default": "", "required": False, "options": _MARKET_OPTIONS},
                {"name": "category",            "label": "Category",            "type": "select", "default": "", "required": False, "options": _SPECIALS_CATEGORY_OPTIONS},
            ],
        },
        {
            "id": "specials_categories",
            "name": "Get Categories",
            "category": "Priceless Specials",
            "method": "GET",
            "description": "Lists the merchant offer categories.",
            "params": [{"name": "language", "label": "Language", "type": "select", "default": "", "required": False, "options": _LANGUAGE_OPTIONS}],
        },
        {
            "id": "specials_countries",
            "name": "Get Countries",
            "category": "Priceless Specials",
            "method": "GET",
            "description": "Lists the supported country codes.",
            "params": [{"name": "language", "label": "Language", "type": "select", "default": "", "required": False, "options": _LANGUAGE_OPTIONS}],
        },
        {
            "id": "specials_languages",
            "name": "Get Languages",
            "category": "Priceless Specials",
            "method": "GET",
            "description": "Lists the languages Priceless Specials supports (BCP-47).",
            "params": [],
        },
        {
            "id": "specials_mastercard_products",
            "name": "Get Mastercard Products",
            "category": "Priceless Specials",
            "method": "GET",
            "description": "Lists Mastercard product codes (Standard, Gold, Platinum, World …).",
            "params": [{"name": "language", "label": "Language", "type": "select", "default": "", "required": False, "options": _LANGUAGE_OPTIONS}],
        },
        {
            "id": "specials_card_products",
            "name": "Get Card Products",
            "category": "Priceless Specials",
            "method": "GET",
            "description": "Lists card products available to the calling client.",
            "params": [{"name": "language", "label": "Language", "type": "select", "default": "", "required": False, "options": _LANGUAGE_OPTIONS}],
        },
    ],
}


# --- Execute --------------------------------------------------------------

def execute(op_id: str, params: Dict[str, Any]) -> Dict[str, Any]:
    op = _OPS.get(op_id)
    if op is None:
        return {"success": False, "error": f"Unknown operation: {op_id}"}
    return _do_get(op, params or {})


def _do_get(op: Dict[str, Any], params: Dict[str, Any]) -> Dict[str, Any]:
    from simulator.switcher import is_simulated
    if not _configured() and not is_simulated("priceless"):
        return {
            "success": False,
            "error": (
                "Priceless is not configured. Set PRICELESS_CONSUMER_KEY and "
                "PRICELESS_SIGNING_KEY_PATH in .env, then restart the server."
            ),
        }

    base = _platform_base() if op["service"] == "platform" else _specials_base()

    # Resolve path placeholders ({product_id} etc.) from params, removing
    # them from the query-string copy.
    query_params: Dict[str, Any] = dict(params)
    endpoint = op["endpoint"]
    for path_key in op.get("path_params", ()):
        val = str(query_params.pop(path_key, "")).strip()
        if not val:
            return {"success": False, "error": f"{path_key} is required"}
        endpoint = endpoint.replace("{" + path_key + "}", val)

    # Drop empty / None values
    query_pairs: List[Tuple[str, str]] = [
        (k, str(v)) for k, v in query_params.items()
        if v is not None and str(v).strip() != ""
    ]
    url = f"{base}{endpoint}"
    if query_pairs:
        url = f"{url}?{urlencode(query_pairs)}"

    import requests
    import uuid
    headers = {
        "Accept": "application/json",
        "x-openapi-transid": str(uuid.uuid4()),
    }
    if is_simulated("priceless"):
        headers["Authorization"] = "Simulated"
    else:
        consumer_key = os.environ["PRICELESS_CONSUMER_KEY"]
        key_path     = os.environ["PRICELESS_SIGNING_KEY_PATH"]
        key_password = os.environ.get("PRICELESS_SIGNING_KEY_PASSWORD", "keystorepassword")

        if not os.path.isabs(key_path):
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            key_path = os.path.join(project_root, key_path)

        headers["X-OpenApi-ClientId"] = consumer_key.split("!", 1)[0]

        import oauth1.authenticationutils as authutils
        from oauth1.oauth import OAuth

        try:
            signing_key = authutils.load_signing_key(key_path, key_password)
            auth_header = OAuth.get_authorization_header(url, "GET", None, consumer_key, signing_key)
            headers["Authorization"] = auth_header
        except Exception as e:
            return {"success": False, "error": f"OAuth signing failed: {e}"}

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
    data = resp_body if success else {}

    return {
        "success": success,
        "data": data,
        "error": None if success else (resp_body.get("Errors", {}) if isinstance(resp_body, dict) else resp_body),
        "request": {"method": "GET", "url": url},
        "response": {"status_code": status_code, "body": resp_body},
        "state_updates": {},
    }
