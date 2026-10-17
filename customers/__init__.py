"""Customers — a customer's business read as a platform, in Solution Studio.

Each customer lives in its own folder, ``customers/<id>/``:

* a **standalone page**: one self-contained HTML file (fonts embedded, no
  network needed) that opens on its own in any browser. It is built on the
  same layer-picture engine as the Platform tab (``mcos/``): the customer's
  business as five discs, the kinds of customer above them, and journeys
  that light up across the layers. It is copied in (refresh it with
  ``python tools/sync_customer.py <id> <file>``, which adds the logos) or
  built here (``customers/build_page.py``), and never edited by hand.
* ``__init__.py`` with a ``CUSTOMER`` dict: who the customer is, the page's
  file name, and which Solution Studio APIs, use cases and bundles land on
  which of the customer's products (``STUDIO``) and journeys (``JOURNEY_BUNDLES``).
* ``studio-theme.css``: the customer's own colours on Studio's skin.
* the customer's logos (``CUSTOMER["logos"]``: ``logo.svg`` or ``logo.png``,
  sometimes a second brand), taken from ``static/logos/financial-logos-500/``
  or the customer's own website, and shown on its card, over its page and in
  the standalone page's header (embedded there by :func:`with_brand`).
* any research notes behind the page.

Inside Studio the page is served at ``/customers/<id>/`` dressed like the
Platform tab: ``mcos/web/mcos-theme.css`` for Studio's look, then the
customer's ``studio-theme.css``, then ``mcos/web/mcos-bridge.js``, which adds
the "Try it in Solution Studio" links and talks to the Customers tab
(``static/js/app/features/customers.js``). The standalone file itself is
served untouched at ``/customers/<id>/<file>``.
"""
from __future__ import annotations

import base64
import html
import importlib
import os
import re
from functools import lru_cache

import mcos

_HERE = os.path.dirname(os.path.abspath(__file__))

# Keys every customer's CUSTOMER dict must carry.
_REQUIRED = ("id", "name", "short", "page", "as_of")


def _customer_dirs() -> list[str]:
    return sorted(
        d for d in os.listdir(_HERE)
        if not d.startswith(("_", "."))
        and os.path.isfile(os.path.join(_HERE, d, "__init__.py"))
    )


@lru_cache(maxsize=1)
def _load() -> tuple[dict, ...]:
    out = []
    for d in _customer_dirs():
        mod = importlib.import_module(f"customers.{d}")
        c = dict(getattr(mod, "CUSTOMER", {}))
        missing = [k for k in _REQUIRED if not c.get(k)]
        if missing:
            raise ValueError(f"customers/{d}: CUSTOMER is missing {', '.join(missing)}")
        if c["id"] != d:
            raise ValueError(f"customers/{d}: CUSTOMER id {c['id']!r} must match its folder")
        c["dir"] = os.path.join(_HERE, d)
        c.setdefault("order", 100)
        c.setdefault("studio", {})
        c.setdefault("journey_bundles", {})
        c.setdefault("text_swaps", ())
        c.setdefault("notes", ())
        c.setdefault("logos", ())
        out.append(c)
    out.sort(key=lambda c: (c["order"], c["name"]))
    return tuple(out)


def all_customers() -> list[dict]:
    return list(_load())


def get(cid: str) -> dict | None:
    return next((c for c in _load() if c["id"] == cid), None)


def page_path(c: dict) -> str:
    """The standalone page on disk."""
    return os.path.join(c["dir"], c["page"])


@lru_cache(maxsize=16)
def _read(path: str, mtime: float) -> str:  # mtime keys the cache
    with open(path, encoding="utf-8") as f:
        return f.read()


def page_source(c: dict) -> str:
    path = page_path(c)
    return _read(path, os.path.getmtime(path))


def _swapped(c: dict) -> str:
    src = page_source(c)
    for old, new in c["text_swaps"]:
        src = src.replace(old, new)
    return src


# ---------------------------------------------------------------------------
# Logos
# ---------------------------------------------------------------------------

_MIME = {".svg": "image/svg+xml", ".png": "image/png"}
_BRAND_RE = re.compile(r"<!--brand-->.*?<!--/brand-->\s*", re.S)
_BRAND_CSS = (
    ".brand{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin:0 0 14px}"
    ".brand img{display:block;box-sizing:border-box;height:46px;width:auto;max-width:230px;padding:9px 14px;"
    "border-radius:12px;background:var(--chip);object-fit:contain;"
    "box-shadow:0 0 0 1px color-mix(in oklab,var(--line,#ccc) 70%,transparent),0 8px 22px -14px rgba(0,0,0,.45)}"
)


def logo_files(c: dict) -> set[str]:
    return {lg["file"] for lg in c["logos"]}


def logo_urls(c: dict) -> list[dict]:
    """The logos as Studio links them: ``file``, ``v`` (cache-buster), ``url``, ``alt`` and the chip colour ``bg``."""
    out = []
    for lg in c["logos"]:
        path = os.path.join(c["dir"], lg["file"])
        if os.path.isfile(path):
            v = int(os.path.getmtime(path))
            out.append({"file": lg["file"], "v": v, "url": f"/customers/{c['id']}/{lg['file']}?v={v}",
                        "alt": lg["alt"], "bg": lg.get("bg", "#ffffff")})
    return out


def brand_block(c: dict) -> str:
    """The logos as a self-contained block (images embedded) for the top of a standalone page."""
    imgs = []
    for lg in c["logos"]:
        path = os.path.join(c["dir"], lg["file"])
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode("ascii")
        mime = _MIME[os.path.splitext(lg["file"])[1].lower()]
        imgs.append(f'<img src="data:{mime};base64,{data}" alt="{html.escape(lg["alt"])}" '
                    f'style="--chip:{lg.get("bg", "#ffffff")}">')
    if not imgs:
        return ""
    return f'<!--brand--><style>{_BRAND_CSS}</style><div class="brand">{"".join(imgs)}</div><!--/brand-->\n      '


def with_brand(src: str, c: dict) -> str:
    """``src`` (a standalone page) with ``c``'s logos above its kicker, replacing any logos already there."""
    src = _BRAND_RE.sub("", src)
    at = src.find('<div class="kicker">')
    if at < 0:
        raise ValueError(f"customers/{c['id']}: no kicker to put the logos above")
    return src[:at] + brand_block(c) + src[at:]


# ---------------------------------------------------------------------------
# The page inside Studio
# ---------------------------------------------------------------------------

# The standalone pages embed their fonts so they work offline. Inside Studio
# the theme sets Inter and JetBrains Mono, so the embedded fonts (most of the
# file's weight) are dropped.
_EMBEDDED_FONTS_RE = re.compile(r"<style>/\*[^*]*embedded[^*]*\*/\s*@font-face.*?</style>\s*", re.S)


def _asset_bust(c: dict) -> int:
    newest = os.path.getmtime(page_path(c))
    for path in (os.path.join(c["dir"], "studio-theme.css"),
                 *(os.path.join(mcos.WEB_DIR, n) for n in os.listdir(mcos.WEB_DIR))):
        if os.path.isfile(path):
            newest = max(newest, os.path.getmtime(path))
    return int(newest)


def render_page(c: dict) -> str:
    """The customer's standalone page dressed as a Solution Studio tab.

    Nothing in the page is removed but its title and embedded fonts. Studio's
    theme goes in after the page's own styles (which these pages keep in the
    body), the customer's colours after that, and the bridge at the end.
    """
    src = _swapped(c)
    src = _EMBEDDED_FONTS_RE.sub("", src)
    src = re.sub(r"<title>.*?</title>\s*", "", src, count=1, flags=re.S)
    v = _asset_bust(c)

    head = (
        f"<title>{c['name']} · Mastercard Solution Studio</title>\n"
        '<script src="/static/js/usecase-theme.js"></script>\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700'
        '&family=JetBrains+Mono:wght@400;500&display=swap">\n'
    )
    theme = f'<link rel="stylesheet" href="/mcos/mcos-theme.css?v={v}">\n'
    if os.path.isfile(os.path.join(c["dir"], "studio-theme.css")):
        theme += f'<link rel="stylesheet" href="/customers/{c["id"]}/studio-theme.css?v={v}">\n'
    bridge = f'<script src="/mcos/mcos-bridge.js?v={v}"></script>\n'

    src = src.replace("</head>", head + "</head>", 1) if "</head>" in src else head + src
    # After the last style block before the picture, so the theme wins.
    anchor = src.find('<div class="wrap">')
    cut = src.rfind("</style>", 0, anchor if anchor >= 0 else len(src))
    if cut >= 0:
        cut += len("</style>")
        src = src[:cut] + "\n" + theme + src[cut:]
    else:
        src = src.replace("</head>", theme + "</head>", 1)
    end = src.rfind("</body>")
    src = src[:end] + bridge + src[end:] if end >= 0 else src + bridge
    return src


# ---------------------------------------------------------------------------
# What the page holds, and what Studio has for it
# ---------------------------------------------------------------------------

@lru_cache(maxsize=16)
def _catalog(cid: str, mtime: float) -> tuple[dict, ...]:  # mtime keys the cache
    c = get(cid)
    return tuple(mcos.parse_catalog(_swapped(c)))


def search_catalog(c: dict) -> list[dict]:
    """The customer's layers, areas, products, journeys and kinds of user."""
    return [dict(e) for e in _catalog(c["id"], os.path.getmtime(page_path(c)))]


def picture_ids(c: dict) -> tuple[set[str], set[str]]:
    """Product ids and journey (outcome) ids defined in the customer's page."""
    entries = search_catalog(c)
    return ({e["id"] for e in entries if e["kind"] == "product"},
            {e["id"] for e in entries if e["kind"] == "outcome"})


def mapping_problems(c: dict, apis=(), bundles=(), use_cases=()) -> list[str]:
    """Studio mappings in ``c`` that no longer resolve (empty if fine).

    ``apis`` / ``bundles`` / ``use_cases`` are Studio's ids; leave them empty
    to check only against the page (as ``tools/sync_customer.py`` does).
    """
    products, outcomes = picture_ids(c)
    known = {"apis": set(apis), "bundles": set(bundles), "use_cases": set(use_cases)}
    problems = []
    for pid, items in c["studio"].items():
        if pid not in products:
            problems.append(f"{c['id']}: product {pid!r} is not in the page")
        for kind in ("apis", "use_cases", "bundles"):
            for x in items.get(kind, ()):
                if known[kind] and x not in known[kind]:
                    problems.append(f"{c['id']}: product {pid!r} names unknown {kind[:-1].replace('_', ' ')} {x!r}")
    for oid, bids in c["journey_bundles"].items():
        if oid not in outcomes:
            problems.append(f"{c['id']}: journey {oid!r} is not in the page")
        for b in bids:
            if known["bundles"] and b not in known["bundles"]:
                problems.append(f"{c['id']}: journey {oid!r} names unknown bundle {b!r}")
    return problems


def build_links(c: dict, apis: list[dict], bundles: list[dict], use_cases: list[dict], *,
                non_us_blocked_api, non_us_blocked_use_case) -> dict:
    """The customer's products joined to Studio's APIs, use cases and bundles.

    Same shape as :func:`mcos.build_links` (``products``, ``outcomes``,
    ``targets``, ``warnings``), so ``mcos-bridge.js`` reads it unchanged.
    Unlike the Platform tab, where every API has one home product, a
    customer's mapping is curated per product in ``CUSTOMER["studio"]``.
    """
    api_by_id = {a["id"]: a for a in apis}
    bundle_by_id = {b["id"]: b for b in bundles}
    uc_by_id = {u["id"]: u for u in use_cases}
    warnings = mapping_problems(c, api_by_id, bundle_by_id, uc_by_id)
    products_in_page, outcomes_in_page = picture_ids(c)

    def api_item(i):
        a = api_by_id[i]
        blocked = bool(non_us_blocked_api(i))
        return {"id": i, "name": a.get("name") or i, "configured": bool(a.get("configured")),
                "blocked": blocked, "title": mcos.NON_US_TOOLTIP if blocked else ""}

    def uc_item(i):
        u = uc_by_id[i]
        blocked = bool(non_us_blocked_use_case(i))
        return {"id": i, "name": u.get("name") or i, "blocked": blocked,
                "title": mcos.NON_US_TOOLTIP if blocked else ""}

    def bundle_item(i):
        return {"id": i, "name": bundle_by_id[i].get("name") or i}

    products: dict[str, dict] = {}
    targets: dict[str, dict] = {"api": {}, "bundle": {}, "use_case": {}}
    for pid, items in c["studio"].items():
        if pid not in products_in_page:
            continue
        entry = {
            "apis": [api_item(i) for i in items.get("apis", ()) if i in api_by_id],
            "use_cases": [uc_item(i) for i in items.get("use_cases", ()) if i in uc_by_id],
            "bundles": [bundle_item(i) for i in items.get("bundles", ()) if i in bundle_by_id],
        }
        if entry["apis"] or entry["use_cases"] or entry["bundles"]:
            products[pid] = entry
        for kind, key in (("apis", "api"), ("use_cases", "use_case"), ("bundles", "bundle")):
            for x in entry[kind]:
                targets[key].setdefault(x["id"], f"p-{pid}")

    outcomes = {
        oid: {"bundles": [bundle_item(b) for b in bids if b in bundle_by_id]}
        for oid, bids in c["journey_bundles"].items() if oid in outcomes_in_page
    }
    for oid, bids in c["journey_bundles"].items():
        for b in bids:
            if oid in outcomes_in_page and b in bundle_by_id:
                targets["bundle"].setdefault(b, f"o-{oid}")

    return {"products": products, "outcomes": outcomes, "targets": targets, "warnings": warnings}


def accent_text(accent: str | None) -> dict | None:
    """Shades of ``accent`` that read as text on Studio's dark and light cards, and the ink to put on it."""
    if not accent:
        return None
    from customers.brand_colours import contrast, toward  # noqa: PLC0415
    return {
        "dark": toward(accent, "#16130f", 4.5, darker=False),
        "light": toward(accent, "#ffffff", 4.5, darker=True),
        "ink": "#ffffff" if contrast("#ffffff", accent) >= contrast("#111111", accent) else "#111111",
    }


def summary(c: dict, links: dict | None = None) -> dict:
    """What the Customers tab shows on a customer's card (JSON-safe)."""
    counts: dict[str, int] = {}
    for e in search_catalog(c):
        counts[e["kind"]] = counts.get(e["kind"], 0) + 1
    out = {
        k: c.get(k) for k in ("id", "name", "short", "brands", "country", "region", "as_of",
                              "tagline", "stats", "accent")
    }
    out["logos"] = logo_urls(c)
    out["accent_text"] = accent_text(c.get("accent"))
    out.update({
        "counts": {
            "layers": counts.get("layer", 0),
            "areas": counts.get("area", 0),
            "products": counts.get("product", 0),
            "journeys": counts.get("outcome", 0),
            "users": counts.get("user", 0),
            "live": len((links or {}).get("products", {})),
        },
        "page": c["page"],
        "notes": [{"label": label, "file": f} for label, f in c["notes"]],
    })
    return out
