"""Mastercard Operating System — the animated layer picture as a Solution Studio tab.

The picture itself comes from the ``maos`` project and is vendored verbatim
under ``mcos/vendor/`` (refresh it with ``python tools/sync_mcos.py``). This
package wraps it in a page that carries Solution Studio's look
(``mcos/web/mcos-theme.css``) and its links into the rest of the app
(``mcos/web/mcos-bridge.js``), and works out which products in the picture
Solution Studio can show live.

Nothing in the vendored file is edited, so a refresh never has to re-apply
local changes: the bridge drives the picture through the functions and state
its script already exposes.
"""
from __future__ import annotations

import os
import re
from functools import lru_cache

_HERE = os.path.dirname(os.path.abspath(__file__))
VENDOR_FILE = os.path.join(_HERE, "vendor", "layers.artifact.html")
WEB_DIR = os.path.join(_HERE, "web")

# Studio API id -> its home product in the picture. Products are named by the
# picture's own ids (``P("ofus", ...)`` in the vendored file).
API_PRODUCTS: dict[str, str] = {
    "open_finance": "ofus",
    "open_finance_au": "ofus",
    "open_finance_eu": "ofeu",
    "bin_lookup": "binlookup",
    "merchant_identifier": "merchantid",
    "automatic_billing_updater": "abu",
    "match": "matchpro",
    "consumer_clarity": "ethocacc",
    "priceless_cities": "priceless",
    "easy_savings": "easysavings",
    "places": "places",
    "offers_for_publishers": "offers",
    "offers_merchant_content": "offers",
    "transaction_notifications": "txnnotif",
    "benefits_eligibility": "benefits",
    "benefits_content_eligibility": "benefits",
    "enhanced_currency_conversion_calculator": "fx",
    "carbon_calculator": "carbon",
    "business_payment_controls": "bpc",
    "consent_management": "dataconnect",
    "flight_delay_pass": "benefits",
}

# Use cases built on something other than a catalogued API.
USE_CASE_PRODUCTS: dict[str, tuple[str, ...]] = {
    "sonic": ("sonic",),
}

# Picture outcome ("who am I and what do I want to solve?") -> the Studio
# bundles that put it into practice, best match first.
OUTCOME_BUNDLES: dict[str, tuple[str, ...]] = {
    "grow": ("loyalty_stack",),
    "dispute": ("merchant_resolution", "subscriptions"),
    "reach": ("loyalty_stack", "merchant_resolution"),
    "board": ("acquirer_risk",),
    "lend": ("pfm_stack",),
    "b2b": ("issuer_toolkit",),
}

NON_US_TOOLTIP = "Disabled in non-us mode. If running on US IP, this would be enabled."


@lru_cache(maxsize=4)
def _vendor_source(mtime: float) -> str:  # mtime keys the cache
    with open(VENDOR_FILE, encoding="utf-8") as f:
        return f.read()


def vendor_source() -> str:
    return _vendor_source(os.path.getmtime(VENDOR_FILE))


def picture_ids() -> tuple[set[str], set[str]]:
    """Product ids and outcome ids defined in the vendored picture."""
    src = vendor_source()
    products = set(re.findall(r'\bP\("([a-z0-9]+)",', src))
    outcomes = set(re.findall(r'\{id:"([a-z0-9]+)", who:"', src))
    return products, outcomes


def _asset_bust() -> int:
    newest = os.path.getmtime(VENDOR_FILE)
    for name in os.listdir(WEB_DIR):
        newest = max(newest, os.path.getmtime(os.path.join(WEB_DIR, name)))
    return int(newest)


def render_page() -> str:
    """The vendored picture as a full page, dressed in Solution Studio's theme.

    Mirrors ``maos/src/assemble.py``: everything up to the first ``</style>``
    goes in the head, the rest is the body. The picture's own title and Geist
    font links are dropped; Solution Studio's fonts replace them.
    """
    src = vendor_source()
    cut = src.index("</style>") + len("</style>")
    head, body = src[:cut], src[cut:]
    head = re.sub(r"<title>.*?</title>\s*", "", head, flags=re.S)
    head = re.sub(r'<link rel="preconnect"[^>]*>\s*', "", head)
    head = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\s*', "", head)
    v = _asset_bust()
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mastercard Operating System</title>
<script src="/static/js/usecase-theme.js"></script>
<script>if (/[?&]glide=1/.test(location.search)) document.documentElement.classList.add("mcos-glide-wait", "mcos-hero");</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap">
<style>html,body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head}
<link rel="stylesheet" href="/mcos/mcos-theme.css?v={v}">
</head>
<body>
{body}
<script src="/mcos/mcos-bridge.js?v={v}"></script>
</body>
</html>
"""


def build_links(apis: list[dict], bundles: list[dict], use_cases: list[dict], *,
                non_us_blocked_api, non_us_blocked_use_case) -> dict:
    """Join the picture's products to Solution Studio's APIs, bundles and use cases.

    ``apis`` / ``bundles`` / ``use_cases`` are the registry manifests the
    ``/app`` page already renders; the two callables answer the ``--non-us``
    gating question for an API or use case id.

    Returns ``products`` (picture product id -> what Studio has for it),
    ``outcomes`` (picture outcome id -> bundles), ``targets`` (Studio item ->
    where it sits in the picture, as the picture's hash) and ``warnings``
    for mappings that no longer resolve.
    """
    picture_products, picture_outcomes = picture_ids()
    warnings: list[str] = []
    api_by_id = {a["id"]: a for a in apis}
    bundle_by_id = {b["id"]: b for b in bundles}

    for api_id, pid in API_PRODUCTS.items():
        if pid not in picture_products:
            warnings.append(f"API {api_id!r} maps to {pid!r}, which the picture does not define")
    for uc_id, pids in USE_CASE_PRODUCTS.items():
        for pid in pids:
            if pid not in picture_products:
                warnings.append(f"use case {uc_id!r} maps to {pid!r}, which the picture does not define")
    for oid, bids in OUTCOME_BUNDLES.items():
        if oid not in picture_outcomes:
            warnings.append(f"outcome {oid!r} is not defined in the picture")
        for bid in bids:
            if bid not in bundle_by_id:
                warnings.append(f"outcome {oid!r} names unknown bundle {bid!r}")

    def api_products(api_ids) -> list[str]:
        out: list[str] = []
        for api_id in api_ids:
            pid = API_PRODUCTS.get(api_id)
            if api_id in api_by_id and pid in picture_products and pid not in out:
                out.append(pid)
        return out

    products: dict[str, dict] = {}

    def entry(pid: str) -> dict:
        return products.setdefault(pid, {"apis": [], "bundles": [], "use_cases": []})

    for a in apis:
        pid = API_PRODUCTS.get(a["id"])
        if pid not in picture_products:
            continue
        blocked = bool(non_us_blocked_api(a["id"]))
        entry(pid)["apis"].append({
            "id": a["id"],
            "name": a.get("name") or a["id"],
            "configured": bool(a.get("configured")),
            "blocked": blocked,
            "title": NON_US_TOOLTIP if blocked else "",
        })

    bundle_products: dict[str, list[str]] = {}
    for b in bundles:
        ids = [x["id"] if isinstance(x, dict) else x for x in b.get("apis", [])]
        bundle_products[b["id"]] = api_products(ids)
        for pid in bundle_products[b["id"]]:
            entry(pid)["bundles"].append({"id": b["id"], "name": b.get("name") or b["id"]})

    use_case_products: dict[str, list[str]] = {}
    for uc in use_cases:
        pids = api_products(uc.get("apis") or [])
        pids += [p for p in USE_CASE_PRODUCTS.get(uc["id"], ()) if p in picture_products and p not in pids]
        use_case_products[uc["id"]] = pids
        blocked = bool(non_us_blocked_use_case(uc["id"]))
        for pid in pids:
            entry(pid)["use_cases"].append({
                "id": uc["id"],
                "name": uc.get("name") or uc["id"],
                "blocked": blocked,
                "title": NON_US_TOOLTIP if blocked else "",
            })

    outcomes = {
        oid: {"bundles": [{"id": b, "name": bundle_by_id[b].get("name") or b}
                          for b in bids if b in bundle_by_id]}
        for oid, bids in OUTCOME_BUNDLES.items() if oid in picture_outcomes
    }

    bundle_outcome: dict[str, str] = {}
    for oid, bids in OUTCOME_BUNDLES.items():
        if oid not in picture_outcomes:
            continue
        for bid in bids:
            bundle_outcome.setdefault(bid, oid)

    targets = {
        "api": {a["id"]: f"p-{API_PRODUCTS[a['id']]}" for a in apis
                if API_PRODUCTS.get(a["id"]) in picture_products},
        "bundle": {},
        "use_case": {uc_id: f"p-{pids[0]}" for uc_id, pids in use_case_products.items() if pids},
    }
    for bid, pids in bundle_products.items():
        if bid in bundle_outcome:
            targets["bundle"][bid] = f"o-{bundle_outcome[bid]}"
        elif pids:
            targets["bundle"][bid] = f"p-{pids[0]}"

    return {"products": products, "outcomes": outcomes, "targets": targets, "warnings": warnings}
