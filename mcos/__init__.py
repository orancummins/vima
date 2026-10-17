"""Mastercard's platform for the world's economies — the animated layer picture (from maos,
where it is the Mastercard Operating System) as a Solution Studio tab.

The picture itself comes from the ``maos`` project and is vendored verbatim
under ``mcos/vendor/`` (refresh it with ``python tools/sync_mcos.py``). This
package wraps it in a page that carries Solution Studio's look
(``mcos/web/mcos-theme.css``) and its links into the rest of the app
(``mcos/web/mcos-bridge.js``), and works out which products in the picture
Solution Studio can show live. It also reads the picture's inventory out of
the vendored source (``search_catalog``) so Studio's ⌘K palette can search
the platform's layers, areas, products and outcomes and open them.

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


# ---------------------------------------------------------------------------
# Search catalogue
# ---------------------------------------------------------------------------
# Studio's ⌘K palette searches the picture as well as the APIs, bundles and
# use cases. The picture's inventory lives inside the vendored file's own
# script scope, so it is read out of the source here (like picture_ids above)
# rather than by editing the vendored copy or running its script.

_JS_STR = r'"((?:[^"\\]|\\.)*)"'
_LAYER_RE = re.compile(r'\{id:"(U|L[1-5])", name:' + _JS_STR + r', analogy:' + _JS_STR)
_TILE_RE = re.compile(r'\{id:"([\w.\-]+)", (?:ic:"[\w\-]+", )?name:' + _JS_STR)
_BLURB_RE = re.compile(r'blurb:' + _JS_STR)
_DESC_RE = re.compile(r'desc:' + _JS_STR)
_PRODUCT_RE = re.compile(r'\bP\("([a-z0-9]+)",' + _JS_STR + r',' + _JS_STR)
_OUTCOME_RE = re.compile(r'\{id:"([a-z0-9]+)", who:"(\w+)", name:' + _JS_STR + r', why:' + _JS_STR)
_USERS_RE = re.compile(r'(\w+):' + _JS_STR)
_DEV_API_RE = re.compile(r'\[' + _JS_STR + r',' + _JS_STR + r',"([a-z0-9]+)"\]')


def _js_text(raw: str) -> str:
    """A JS double-quoted string literal's value."""
    return re.sub(r'\\(.)', r'\1', raw)


def _inventory_source(src: str) -> str:
    """The MAP IIFE: the picture's product inventory."""
    start = src.index("const MAP=(function(){")
    return src[start:src.index("const TILES = {}, PRODUCTS = {}", start)]


def parse_catalog(src: str) -> list[dict]:
    """Read the picture's layers, areas, products and outcomes out of ``src``.

    Each entry carries the ``target`` (the picture's own hash) that opens it,
    so a search result can go straight to it.
    """
    inv = _inventory_source(src)
    entries: list[dict] = []

    def add(kind: str, ident: str, name: str, sub: str, target: str, *text: str) -> None:
        entries.append({
            "kind": kind,
            "id": ident,
            "name": name,
            "sub": sub,
            "target": target,
            "text": " ".join(t for t in (name, sub, *text) if t),
        })

    # Developer API products, so searching an API name finds its home product.
    dev_apis: dict[str, list[str]] = {}
    api_block = inv[inv.index("const APIS"):] if "const APIS" in inv else ""
    for name, _slug, home in _DEV_API_RE.findall(api_block):
        dev_apis.setdefault(home, []).append(_js_text(name))

    # The eight kinds of user are the tiles of the Users layer, built in the
    # picture from the USERS map rather than written out as tiles.
    users_match = re.search(r"const USERS = \{(.*?)\n\};", inv, re.S)
    user_names = dict(_USERS_RE.findall(users_match.group(1))) if users_match else {}
    for key, raw in user_names.items():
        add("user", "u-" + key, _js_text(raw), "Users", "t-u-" + key)

    # Layers, areas and products, matched in source order so each product
    # picks up the area and layer it sits inside.
    marks: list[tuple[int, str, tuple]] = []
    for m in _LAYER_RE.finditer(inv):
        marks.append((m.start(), "layer", (m.group(1), _js_text(m.group(2)), _js_text(m.group(3)), m.end())))
    for m in _TILE_RE.finditer(inv):
        if _LAYER_RE.match(inv, m.start()):
            continue
        marks.append((m.start(), "area", (m.group(1), _js_text(m.group(2)), m.end())))
    for m in _PRODUCT_RE.finditer(inv):
        marks.append((m.start(), "product", (m.group(1), _js_text(m.group(2)), _js_text(m.group(3)))))
    marks.sort(key=lambda x: x[0])

    layer_name = area_name = ""
    for _pos, kind, data in marks:
        if kind == "layer":
            lid, layer_name, analogy, end = data
            desc = _DESC_RE.search(inv, end, end + 600)
            add("layer", lid, layer_name, analogy, lid, _js_text(desc.group(1)) if desc else "")
            area_name = ""
        elif kind == "area":
            aid, area_name, end = data
            blurb = _BLURB_RE.search(inv, end, end + 300)
            add("area", aid, area_name, layer_name, "t-" + aid, _js_text(blurb.group(1)) if blurb else "")
        else:
            pid, pname, pdesc = data
            sub = " · ".join(x for x in (area_name, layer_name) if x)
            add("product", pid, pname, sub, "p-" + pid, pdesc, *dev_apis.get(pid, ()))

    # Outcomes ("who am I and what do I want to solve?") live outside the
    # inventory, in the picture's own script.
    who_block = re.search(r"const WHO = \{(.*?)\};", src, re.S)
    who = dict(_USERS_RE.findall(who_block.group(1))) if who_block else {}
    for oid, wid, name, why in _OUTCOME_RE.findall(src):
        add("outcome", oid, _js_text(name), _js_text(who.get(wid, "")), "o-" + oid, _js_text(why))

    return entries


def catalog_problems(src: str) -> list[str]:
    """Why the search catalogue could not be read out of ``src`` (empty if fine).

    ``tools/sync_mcos.py`` runs this, so a refresh that moves the inventory
    out of reach fails loudly instead of quietly emptying Studio's search.
    """
    try:
        entries = parse_catalog(src)
    except ValueError as exc:   # the inventory is no longer where it was
        return [f"the search catalogue cannot be read from the picture: {exc}"]
    counts: dict[str, int] = {}
    for e in entries:
        counts[e["kind"]] = counts.get(e["kind"], 0) + 1
    problems = []
    for kind, least in (("layer", 5), ("area", 20), ("product", 100), ("outcome", 10), ("user", 7)):
        if counts.get(kind, 0) < least:
            problems.append(
                f"the search catalogue found only {counts.get(kind, 0)} {kind} entries in the picture "
                f"(expected at least {least}); its shape has changed"
            )
    products = set(re.findall(r'\bP\("([a-z0-9]+)",', src))
    missed = products - {e["id"] for e in entries if e["kind"] == "product"}
    if missed:
        problems.append(f"the search catalogue missed products: {', '.join(sorted(missed))}")
    return problems


@lru_cache(maxsize=4)
def _search_catalog(mtime: float) -> tuple[dict, ...]:  # mtime keys the cache
    src = vendor_source()
    for old, new in TEXT_SWAPS:   # search the wording the page shows
        src = src.replace(old, new)
    return tuple(parse_catalog(src))


def search_catalog() -> list[dict]:
    """Everything in the picture the ⌘K palette can search and open."""
    return [dict(e) for e in _search_catalog(os.path.getmtime(VENDOR_FILE))]


def _asset_bust() -> int:
    newest = os.path.getmtime(VENDOR_FILE)
    for name in os.listdir(WEB_DIR):
        newest = max(newest, os.path.getmtime(os.path.join(WEB_DIR, name)))
    return int(newest)


# The picture calls itself the Mastercard Operating System; Solution Studio
# calls it the platform for the world's economies. Each swap must match the
# vendored copy (tools/sync_mcos.py checks), so a refresh can't lose one.
PLATFORM_NAME = "Platform for the world's economies"
TEXT_SWAPS = (
    ('<h1>Mastercard <span class="os">Operating System</span></h1>',
     f'<h1>Mastercard <span class="os">{PLATFORM_NAME}</span></h1>'),
    ("Five discs that stack into one system.", "Five discs that stack into one platform."),
    ("one for each layer of the Mastercard Operating System",
     "one for each layer of Mastercard's platform for the world's economies"),
    ("One front door for the whole OS.", "One front door for the whole platform."),
    ("the ecosystem the OS serves", "the ecosystem the platform serves"),
    # Mastercard's own figure (2025): Bacs Direct Credit pays over 95% of UK
    # monthly salaries. The picture's "98% of state benefits" has no current source.
    ('t:"Bacs carries about 98% of UK state benefits"', 't:"Bacs pays benefits and over 95% of UK salaries"'),
)


def render_page() -> str:
    """The vendored picture as a full page, dressed in Solution Studio's theme.

    Mirrors ``maos/src/assemble.py``: everything up to the first ``</style>``
    goes in the head, the rest is the body. The picture's own title and Geist
    font links are dropped; Solution Studio's fonts replace them.
    """
    src = vendor_source()
    for old, new in TEXT_SWAPS:
        src = src.replace(old, new)
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
<title>Mastercard {PLATFORM_NAME}</title>
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
