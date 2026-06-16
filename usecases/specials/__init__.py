"""Priceless Concierge — Priceless Specials use case.

Wraps the Priceless Specials API and shapes its three core feeds —
offers, benefits and programs — together with merchants into a single
"trip planner" experience for a Mastercard cardholder.

The user picks:
    * Issuing country  (eligible_markets)
    * Destination      (destination_markets)
    * Mastercard product  (MWE / MWP / MPL / …)
    * Category interest    (Dining / Travel / Shopping / …)

… and the page shows curated offers, card benefits, marketing programs
and participating merchants for that combination.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from typing import Any

MANIFEST: dict[str, Any] = {
    "id": "specials",
    "name": "Priceless Concierge",
    "description": (
        "Travelling abroad? Priceless Specials surfaces Mastercard's curated "
        "catalogue of merchant offers, card-product benefits and marketing "
        "programs available in your destination. Pick your card and where "
        "you're going — the concierge does the rest."
    ),
    "apis": ["priceless_cities"],
    "render": "specials",
    "defaults": {
        "eligible_markets": "US",
        "destination_markets": "JP",
        "mastercard_product": "MWE",
        "category": "",
        "language": "en-US",
    },
}

# --- Action dispatcher ----------------------------------------------------

def do_action(action: str, params: dict[str, Any]) -> dict[str, Any]:
    if action == "search":
        return _search(params)
    return {"error": f"Unknown action: {action}"}

# --- Search ---------------------------------------------------------------

def _search(params: dict[str, Any]) -> dict[str, Any]:
    from apis.priceless_cities import api as p_api

    base: dict[str, Any] = {
        "language":            params.get("language") or "en-US",
        "eligible_markets":    params.get("eligible_markets") or "",
        "destination_markets": params.get("destination_markets") or "",
        "category":            params.get("category") or "",
        "mastercard_product":  params.get("mastercard_product") or "",
    }
    # Drop empties for the merchants & programs feeds that don't use category etc.
    merchants_params = {k: v for k, v in base.items() if v}
    programs_params  = {k: v for k, v in {
        "language":         base["language"],
        "eligible_markets": base["eligible_markets"],
    }.items() if v}

    feeds = {
        "offers":    ("specials_offers",    base),
        "benefits":  ("specials_benefits",  base),
        "programs":  ("specials_programs",  programs_params),
        "merchants": ("specials_merchants", merchants_params),
    }

    results: dict[str, dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=4) as ex:
        futures = {key: ex.submit(p_api.execute, op, p) for key, (op, p) in feeds.items()}
        for key, fut in futures.items():
            try:
                results[key] = fut.result(timeout=20) or {}
            except Exception as e:  # pragma: no cover
                results[key] = {"success": False, "error": str(e)}

    all_failed = all(not r.get("success") for r in results.values())
    first_err = next((r.get("error") for r in results.values() if r.get("error")), None)

    # Shape & drop ghost rows the sandbox often emits (rows with no usable
    # content). The UI was rendering those as empty cards.
    offers    = [s for s in (_shape_offer(o)    for o in _items(results["offers"].get("data")))    if _meaningful_offer(s)]
    benefits  = [s for s in (_shape_benefit(b)  for b in _items(results["benefits"].get("data")))  if _meaningful_benefit(s)]
    programs  = [s for s in (_shape_program(p)  for p in _items(results["programs"].get("data")))  if _meaningful_program(s)]
    merchants = [s for s in (_shape_merchant(m) for m in _items(results["merchants"].get("data"))) if _meaningful_merchant(s)]

    live_total = len(offers) + len(benefits) + len(programs) + len(merchants)

    # Hybrid behaviour: if the live API gave us nothing usable (or it failed
    # outright), drop in a curated demo dataset so the use case is still a
    # compelling demo. We tag the response so the UI can show a notice.
    if live_total < _MIN_LIVE_ITEMS:
        curated = _curated_dataset(
            destination=base["destination_markets"],
            product=base["mastercard_product"],
            category=base["category"],
        )
        if all_failed:
            demo_reason = _stringify_error(first_err) or "Priceless Specials API not reachable."
        elif live_total == 0:
            demo_reason = "Sandbox returned no live perks for this combination."
        else:
            demo_reason = "Sandbox returned only sparse rows — showing curated demo perks."
        return {
            **curated,
            "demo_mode": True,
            "demo_reason": demo_reason,
            "live_total": live_total,
            "partial_errors": {
                key: _stringify_error(r.get("error"))
                for key, r in results.items()
                if not r.get("success")
            },
        }

    return {
        "offers":    offers,
        "benefits":  benefits,
        "programs":  programs,
        "merchants": merchants,
        "demo_mode": False,
        "partial_errors": {
            key: _stringify_error(r.get("error"))
            for key, r in results.items()
            if not r.get("success")
        },
    }

# --- Filters: drop ghost rows --------------------------------------------

def _meaningful_offer(o: dict[str, Any]) -> bool:
    title_ok = bool(o.get("title")) and o.get("title") != "Untitled offer"
    has_body = bool(o.get("description") or o.get("discount") or o.get("redemptionUrl"))
    return title_ok and has_body

def _meaningful_benefit(b: dict[str, Any]) -> bool:
    title_ok = bool(b.get("title")) and b.get("title") != "Benefit"
    has_body = bool(b.get("description") or b.get("url"))
    return title_ok and has_body

def _meaningful_program(p: dict[str, Any]) -> bool:
    title_ok = bool(p.get("title")) and p.get("title") != "Program"
    has_body = bool(p.get("description") or p.get("image") or p.get("url"))
    return title_ok and has_body

def _meaningful_merchant(m: dict[str, Any]) -> bool:
    name_ok = bool(m.get("name")) and m.get("name") != "Merchant"
    return name_ok and bool(m.get("category") or m.get("logo"))

# Hybrid threshold: if live data has fewer than this many usable items across
# all four feeds combined, swap in the curated demo dataset.
_MIN_LIVE_ITEMS = 4

# --- Helpers --------------------------------------------------------------

def _items(data: Any) -> list[dict[str, Any]]:
    """Normalize any Priceless Specials response shape to a flat list."""
    if data is None:
        return []
    if isinstance(data, list):
        return [x for x in data if isinstance(x, dict)]
    if isinstance(data, dict):
        for key in (
            "Offers", "offers",
            "Benefits", "benefits",
            "Programs", "programs",
            "Merchants", "merchants",
            "items", "Items",
            "data", "Data",
            "results",
        ):
            v = data.get(key)
            if isinstance(v, list):
                return [x for x in v if isinstance(x, dict)]
            if isinstance(v, dict):
                # Sometimes the inner shape is { Offers: { Offer: [...] } }
                for inner_key in ("Offer", "Benefit", "Program", "Merchant", "items"):
                    iv = v.get(inner_key)
                    if isinstance(iv, list):
                        return [x for x in iv if isinstance(x, dict)]
                    if isinstance(iv, dict):
                        return [iv]
    return []

def _first(d: dict[str, Any], *keys: str, default: str = "") -> str:
    for k in keys:
        v = d.get(k)
        if v not in (None, "", []):
            return str(v) if not isinstance(v, (dict, list)) else default
    return default

def _shape_offer(o: dict[str, Any]) -> dict[str, Any]:
    merchant = o.get("merchant") or o.get("Merchant") or {}
    if not isinstance(merchant, dict):
        merchant = {}
    dates = o.get("offerDates") or o.get("OfferDates") or {}
    if not isinstance(dates, dict):
        dates = {}
    return {
        "id":           _first(o, "id", "offerId", "OfferId", "Id"),
        "title":        _first(o, "offerTitle", "title", "Title", "name", "Name", default="Untitled offer"),
        "description":  _first(o, "offerDescription", "description", "Description", "shortDescription"),
        "merchantName": _first(merchant, "name", "Name", "merchantName") or _first(o, "merchantName"),
        "merchantLogo": _first(merchant, "logoUrl", "logo", "imageUrl") or _first(o, "merchantLogoUrl", "logoUrl"),
        "category":     _first(merchant, "categoryName", "category") or _first(o, "category", "categoryName"),
        "discount":     _first(o, "offerHeadline", "discountText", "discount", "discountValue", "savings"),
        "startDate":    _first(dates, "startDate", "from") or _first(o, "startDate"),
        "endDate":      _first(dates, "endDate", "to") or _first(o, "endDate", "expiryDate"),
        "redemptionUrl":_first(o, "redemptionUrl", "RedemptionURL", "ctaUrl", "url"),
        "termsUrl":     _first(o, "termsAndConditionsUrl", "termsUrl", "tncUrl"),
        "tags":         _list_str(o.get("tags") or o.get("Tags")),
    }

def _shape_benefit(b: dict[str, Any]) -> dict[str, Any]:
    return {
        "id":          _first(b, "id", "benefitId", "BenefitId"),
        "title":       _first(b, "benefitTitle", "title", "Title", "name", default="Benefit"),
        "description": _first(b, "benefitDescription", "description", "shortDescription"),
        "category":    _first(b, "category", "categoryName", "type"),
        "icon":        _first(b, "iconUrl", "imageUrl", "logoUrl"),
        "url":         _first(b, "redemptionUrl", "url", "detailsUrl"),
        "endDate":     _first(b, "endDate", "expiryDate"),
    }

def _shape_program(p: dict[str, Any]) -> dict[str, Any]:
    return {
        "id":          _first(p, "id", "programId", "ProgramId"),
        "title":       _first(p, "programTitle", "title", "Name", "name", default="Program"),
        "description": _first(p, "programDescription", "description"),
        "image":       _first(p, "imageUrl", "heroImageUrl", "bannerUrl"),
        "url":         _first(p, "programUrl", "url"),
    }

def _shape_merchant(m: dict[str, Any]) -> dict[str, Any]:
    return {
        "id":       _first(m, "id", "merchantId", "MerchantId"),
        "name":     _first(m, "merchantName", "name", "Name", default="Merchant"),
        "category": _first(m, "categoryName", "category"),
        "logo":     _first(m, "logoUrl", "imageUrl", "logo"),
        "country":  _first(m, "country", "countryCode"),
    }

def _list_str(v: Any) -> list[str]:
    if isinstance(v, list):
        return [str(x) for x in v if x is not None]
    if isinstance(v, str):
        return [t.strip() for t in v.split(",") if t.strip()]
    return []

def _stringify_error(err: Any) -> str:
    if err is None:
        return ""
    if isinstance(err, str):
        return err
    try:
        import json as _json
        return _json.dumps(err)[:400]
    except Exception:
        return str(err)[:400]

# --- Curated demo dataset -------------------------------------------------
#
# The Priceless Specials sandbox returns very sparse rows (lots of empty
# fields), which makes the live demo look broken. When that happens we fall
# back to this curated dataset so the use case still tells a compelling
# story. Pure presentation data — no PII, no real customer records.

_CATEGORIES = ["Dining", "Shopping", "Travel", "Entertainment", "Sports", "Wellness", "Lifestyle"]

def _curated_dataset(
    destination: str,
    product: str,
    category: str = "",
) -> dict[str, list[dict[str, Any]]]:
    """Return a curated set of offers/benefits/programs/merchants for a destination."""
    dest = (destination or "").upper()
    pack = _DEMO_PACKS.get(dest) or _DEMO_PACKS["_DEFAULT"]

    # Tier-aware benefits: World Elite & World get the premium pack.
    premium = product in ("MWE", "MWP", "MBC")
    benefits = list(_DEMO_BENEFITS_PREMIUM if premium else _DEMO_BENEFITS_CORE)

    offers    = [dict(o) for o in pack["offers"]]
    programs  = [dict(p) for p in pack["programs"]]
    merchants = [dict(m) for m in pack["merchants"]]

    # Apply category filter when set, but always keep at least 2 of each
    # so the tabs aren't empty.
    if category:
        cat = category.strip()
        def _matches(item):
            return (item.get("category") or "").lower() == cat.lower()
        offers_f    = [o for o in offers    if _matches(o)]
        merchants_f = [m for m in merchants if _matches(m)]
        if len(offers_f) >= 2:    offers = offers_f        # noqa: E701
        if len(merchants_f) >= 2: merchants = merchants_f  # noqa: E701

    return {
        "offers":    offers,
        "benefits":  benefits,
        "programs":  programs,
        "merchants": merchants,
    }

# Tier benefits — these are universal across markets.
_DEMO_BENEFITS_CORE = [
    {"id": "b-fx",    "title": "No-FX foreign transactions", "category": "Travel",
     "description": "Spend abroad in any currency with zero foreign-transaction fees on this card.",
     "icon": "", "url": "", "endDate": ""},
    {"id": "b-fraud", "title": "Zero-liability fraud protection", "category": "Security",
     "description": "You're never responsible for unauthorised charges — we cover 100% of fraudulent activity.",
     "icon": "", "url": "", "endDate": ""},
    {"id": "b-id",    "title": "Identity theft resolution", "category": "Security",
     "description": "Free 24/7 access to specialists who help you restore your identity if it's compromised.",
     "icon": "", "url": "", "endDate": ""},
    {"id": "b-price", "title": "Mastercard Price Protection", "category": "Shopping",
     "description": "Find the same item cheaper within 60 days and we'll refund the difference, up to $250 per item.",
     "icon": "", "url": "", "endDate": ""},
]

_DEMO_BENEFITS_PREMIUM = _DEMO_BENEFITS_CORE + [
    {"id": "b-lounge", "title": "LoungeKey airport access", "category": "Travel",
     "description": "Discounted entry to 1,300+ airport lounges worldwide — relax before your flight, every flight.",
     "icon": "", "url": "", "endDate": ""},
    {"id": "b-concierge", "title": "24/7 Mastercard Concierge", "category": "Lifestyle",
     "description": "Restaurant bookings, hotel upgrades, hard-to-get tickets — call once, we handle the rest.",
     "icon": "", "url": "", "endDate": ""},
    {"id": "b-rental", "title": "Car rental insurance", "category": "Travel",
     "description": "Pay with your card and skip the rental counter's collision damage waiver — you're already covered.",
     "icon": "", "url": "", "endDate": ""},
    {"id": "b-hotel",  "title": "Priceless Hotels Premium Collection", "category": "Travel",
     "description": "Complimentary breakfast, room upgrade when available, and US$25 food & beverage credit at 2,000+ hotels.",
     "icon": "", "url": "", "endDate": ""},
]

# Per-destination packs — offers, programs, merchants. Light, illustrative.
_DEMO_PACKS: dict[str, dict[str, list[dict[str, Any]]]] = {
    "JP": {
        "offers": [
            {"id": "jp-o1", "title": "10% off omakase tasting menu",
             "description": "Pay with your Mastercard at participating Tokyo and Kyoto sushi counters for 10% off the chef's omakase course.",
             "merchantName": "Sushi Hashimoto", "merchantLogo": "", "category": "Dining",
             "discount": "10% off", "startDate": "", "endDate": "2026-12-31",
             "redemptionUrl": "", "termsUrl": "", "tags": ["sushi", "omakase"]},
            {"id": "jp-o2", "title": "JR Pass: ¥3,000 cash-back",
             "description": "Get ¥3,000 back when you buy a 7-day Japan Rail Pass and pay with a Mastercard.",
             "merchantName": "Japan Rail", "merchantLogo": "", "category": "Travel",
             "discount": "¥3,000 back", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": ["rail"]},
            {"id": "jp-o3", "title": "Free yukata rental in Asakusa",
             "description": "Rent a traditional yukata for the day at no charge with any Mastercard purchase over ¥5,000 at the partner store.",
             "merchantName": "Asakusa Kimono Rental", "merchantLogo": "", "category": "Shopping",
             "discount": "Free rental", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "jp-o4", "title": "Tokyo Skytree skip-the-line + 15% off",
             "description": "Priority access to the Tembo Deck plus 15% off when you book with a World Elite Mastercard.",
             "merchantName": "Tokyo Skytree", "merchantLogo": "", "category": "Entertainment",
             "discount": "15% off", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "jp-o5", "title": "Onsen ryokan: late checkout + welcome drink",
             "description": "Complimentary 2pm late checkout and a matcha welcome drink at participating Hakone ryokan.",
             "merchantName": "Hakone Yutowa", "merchantLogo": "", "category": "Travel",
             "discount": "Late checkout", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "jp-o6", "title": "Ginza department store tax-free + 5%",
             "description": "Layer 5% off on top of the duty-free 10% you already get when shopping with Mastercard at Ginza Mitsukoshi.",
             "merchantName": "Ginza Mitsukoshi", "merchantLogo": "", "category": "Shopping",
             "discount": "5% off", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
        ],
        "programs": [
            {"id": "jp-p1", "title": "Priceless Tokyo", "image": "",
             "description": "Once-in-a-lifetime experiences across Tokyo — sake brewery tours, sumo training visits, private kaiseki dinners.",
             "url": ""},
            {"id": "jp-p2", "title": "Cherry Blossom Privileges", "image": "",
             "description": "Spring-only perks: priority access to private hanami spots, complimentary tea ceremony, festival passes.",
             "url": ""},
        ],
        "merchants": [
            {"id": "jp-m1", "name": "Sushi Hashimoto",       "category": "Dining",        "logo": "", "country": "JP"},
            {"id": "jp-m2", "name": "Japan Rail",            "category": "Travel",        "logo": "", "country": "JP"},
            {"id": "jp-m3", "name": "Tokyo Skytree",         "category": "Entertainment", "logo": "", "country": "JP"},
            {"id": "jp-m4", "name": "Ginza Mitsukoshi",      "category": "Shopping",      "logo": "", "country": "JP"},
            {"id": "jp-m5", "name": "Hakone Yutowa",         "category": "Travel",        "logo": "", "country": "JP"},
            {"id": "jp-m6", "name": "Asakusa Kimono Rental", "category": "Shopping",      "logo": "", "country": "JP"},
            {"id": "jp-m7", "name": "Robot Restaurant",      "category": "Entertainment", "logo": "", "country": "JP"},
            {"id": "jp-m8", "name": "Tsukiji Fish Market",   "category": "Dining",        "logo": "", "country": "JP"},
        ],
    },
    "GB": {
        "offers": [
            {"id": "gb-o1", "title": "Afternoon tea: 2-for-1 at The Savoy",
             "description": "Book afternoon tea at The Savoy's Thames Foyer and get the second guest free, weekdays only.",
             "merchantName": "The Savoy",  "merchantLogo": "", "category": "Dining",
             "discount": "2-for-1", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "gb-o2", "title": "West End theatre: 20% off premium seats",
             "description": "20% off Stalls and Royal Circle seats for selected West End productions when you pay with Mastercard.",
             "merchantName": "Delfont Mackintosh Theatres", "merchantLogo": "", "category": "Entertainment",
             "discount": "20% off", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "gb-o3", "title": "Fortnum & Mason: free hamper upgrade",
             "description": "Spend £150 in-store and get a complimentary upgrade to the next hamper tier.",
             "merchantName": "Fortnum & Mason", "merchantLogo": "", "category": "Shopping",
             "discount": "Free upgrade", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "gb-o4", "title": "Tower of London: skip-the-queue entry",
             "description": "Priority entry plus a complimentary audio guide for two when you book with a Mastercard.",
             "merchantName": "Historic Royal Palaces", "merchantLogo": "", "category": "Entertainment",
             "discount": "Priority entry", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "gb-o5", "title": "Heathrow Express: 10% off return tickets",
             "description": "10% off Heathrow Express return tickets booked online and paid with Mastercard.",
             "merchantName": "Heathrow Express", "merchantLogo": "", "category": "Travel",
             "discount": "10% off", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "gb-o6", "title": "Selfridges: £25 off £250 spend",
             "description": "Get £25 off when you spend £250 or more at Selfridges Oxford Street with a World Elite card.",
             "merchantName": "Selfridges", "merchantLogo": "", "category": "Shopping",
             "discount": "£25 off £250", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
        ],
        "programs": [
            {"id": "gb-p1", "title": "Priceless London", "image": "",
             "description": "Curated London moments — private after-hours museum visits, Michelin chef's tables, Royal Ascot hospitality.",
             "url": ""},
            {"id": "gb-p2", "title": "Mastercard at Wimbledon", "image": "",
             "description": "Cardholder-only access to Centre Court ballots, Pimm's lounge invitations and behind-the-scenes tours.",
             "url": ""},
        ],
        "merchants": [
            {"id": "gb-m1", "name": "The Savoy",           "category": "Dining",        "logo": "", "country": "GB"},
            {"id": "gb-m2", "name": "Fortnum & Mason",     "category": "Shopping",      "logo": "", "country": "GB"},
            {"id": "gb-m3", "name": "Selfridges",          "category": "Shopping",      "logo": "", "country": "GB"},
            {"id": "gb-m4", "name": "Heathrow Express",    "category": "Travel",        "logo": "", "country": "GB"},
            {"id": "gb-m5", "name": "Historic Royal Palaces", "category": "Entertainment", "logo": "", "country": "GB"},
            {"id": "gb-m6", "name": "Delfont Mackintosh Theatres", "category": "Entertainment", "logo": "", "country": "GB"},
            {"id": "gb-m7", "name": "Harrods",             "category": "Shopping",      "logo": "", "country": "GB"},
            {"id": "gb-m8", "name": "The Wolseley",        "category": "Dining",        "logo": "", "country": "GB"},
        ],
    },
    "SG": {
        "offers": [
            {"id": "sg-o1", "title": "Marina Bay Sands: complimentary room upgrade",
             "description": "Book a Deluxe room and get upgraded to a Premier room subject to availability when paying with a Mastercard World Elite.",
             "merchantName": "Marina Bay Sands", "merchantLogo": "", "category": "Travel",
             "discount": "Free upgrade", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "sg-o2", "title": "Hawker Chan: 1-for-1 soya chicken rice",
             "description": "Buy one, get one free at the world's cheapest Michelin-starred meal — Mastercard exclusive on weekdays.",
             "merchantName": "Hawker Chan", "merchantLogo": "", "category": "Dining",
             "discount": "1-for-1", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "sg-o3", "title": "Gardens by the Bay: 25% off conservatory pass",
             "description": "25% off the dual-conservatory pass to Flower Dome and Cloud Forest with any Mastercard.",
             "merchantName": "Gardens by the Bay", "merchantLogo": "", "category": "Entertainment",
             "discount": "25% off", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "sg-o4", "title": "Changi Airport: S$30 dining credit",
             "description": "Spend S$200 at Changi T3 retail or dining and get S$30 back as statement credit.",
             "merchantName": "Changi Airport", "merchantLogo": "", "category": "Travel",
             "discount": "S$30 back", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "sg-o5", "title": "Raffles Hotel Long Bar: complimentary Singapore Sling",
             "description": "One complimentary Singapore Sling per cardholder at the legendary Long Bar.",
             "merchantName": "Raffles Hotel", "merchantLogo": "", "category": "Dining",
             "discount": "Free drink", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
        ],
        "programs": [
            {"id": "sg-p1", "title": "Priceless Singapore", "image": "",
             "description": "Insider access to Singapore — F1 Paddock Club tours, private boat charters, hawker centre chef walks.",
             "url": ""},
        ],
        "merchants": [
            {"id": "sg-m1", "name": "Marina Bay Sands",     "category": "Travel",        "logo": "", "country": "SG"},
            {"id": "sg-m2", "name": "Gardens by the Bay",   "category": "Entertainment", "logo": "", "country": "SG"},
            {"id": "sg-m3", "name": "Hawker Chan",          "category": "Dining",        "logo": "", "country": "SG"},
            {"id": "sg-m4", "name": "Changi Airport",       "category": "Travel",        "logo": "", "country": "SG"},
            {"id": "sg-m5", "name": "Raffles Hotel",        "category": "Dining",        "logo": "", "country": "SG"},
            {"id": "sg-m6", "name": "ION Orchard",          "category": "Shopping",      "logo": "", "country": "SG"},
            {"id": "sg-m7", "name": "Universal Studios SG", "category": "Entertainment", "logo": "", "country": "SG"},
        ],
    },
    "US": {
        "offers": [
            {"id": "us-o1", "title": "OpenTable: $25 dining credit",
             "description": "Get a $25 statement credit when you spend $100 or more at OpenTable partner restaurants in NYC, LA or Miami.",
             "merchantName": "OpenTable", "merchantLogo": "", "category": "Dining",
             "discount": "$25 back", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "us-o2", "title": "Lyft: 15% off airport rides",
             "description": "15% off Lyft rides to and from major US airports, capped at $20 per ride.",
             "merchantName": "Lyft", "merchantLogo": "", "category": "Travel",
             "discount": "15% off", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "us-o3", "title": "Saks Fifth Avenue: $50 off $300",
             "description": "$50 off your purchase of $300 or more at Saks Fifth Avenue stores nationwide.",
             "merchantName": "Saks Fifth Avenue", "merchantLogo": "", "category": "Shopping",
             "discount": "$50 off $300", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "us-o4", "title": "StubHub: 10% off Broadway shows",
             "description": "10% off any Broadway ticket purchase on StubHub when you pay with Mastercard.",
             "merchantName": "StubHub", "merchantLogo": "", "category": "Entertainment",
             "discount": "10% off", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "us-o5", "title": "Marriott Bonvoy: 2,500 bonus points",
             "description": "Earn 2,500 bonus Marriott Bonvoy points on stays of 2+ nights paid with Mastercard.",
             "merchantName": "Marriott Bonvoy", "merchantLogo": "", "category": "Travel",
             "discount": "Bonus points", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
        ],
        "programs": [
            {"id": "us-p1", "title": "Priceless Cities — North America", "image": "",
             "description": "Insider access to US sporting events, broadway debuts, chef's tables and once-in-a-lifetime trips.",
             "url": ""},
            {"id": "us-p2", "title": "Stand Up to Cancer", "image": "",
             "description": "Mastercard donates to Stand Up to Cancer with every dining transaction during the program window.",
             "url": ""},
        ],
        "merchants": [
            {"id": "us-m1", "name": "OpenTable",          "category": "Dining",        "logo": "", "country": "US"},
            {"id": "us-m2", "name": "Lyft",               "category": "Travel",        "logo": "", "country": "US"},
            {"id": "us-m3", "name": "Saks Fifth Avenue",  "category": "Shopping",      "logo": "", "country": "US"},
            {"id": "us-m4", "name": "StubHub",            "category": "Entertainment", "logo": "", "country": "US"},
            {"id": "us-m5", "name": "Marriott Bonvoy",    "category": "Travel",        "logo": "", "country": "US"},
            {"id": "us-m6", "name": "Whole Foods Market", "category": "Shopping",      "logo": "", "country": "US"},
            {"id": "us-m7", "name": "Madison Square Garden", "category": "Entertainment", "logo": "", "country": "US"},
        ],
    },
    "_DEFAULT": {
        "offers": [
            {"id": "df-o1", "title": "10% off your first dinner",
             "description": "Get 10% off the bill at participating Priceless Specials restaurants in your destination.",
             "merchantName": "Priceless Restaurants", "merchantLogo": "", "category": "Dining",
             "discount": "10% off", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "df-o2", "title": "Airport transfer: 15% off",
             "description": "Save 15% on your airport transfer when you book with Mastercard via the Priceless Concierge.",
             "merchantName": "Priceless Transfers", "merchantLogo": "", "category": "Travel",
             "discount": "15% off", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "df-o3", "title": "Hotel: late checkout + welcome drink",
             "description": "Complimentary 2pm checkout and a welcome drink at any Priceless Hotels Premium Collection property.",
             "merchantName": "Priceless Hotels", "merchantLogo": "", "category": "Travel",
             "discount": "Free perk", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
            {"id": "df-o4", "title": "Local experiences: 20% off",
             "description": "Save 20% on tours, classes and experiences booked through Priceless Cities in this market.",
             "merchantName": "Priceless Cities", "merchantLogo": "", "category": "Entertainment",
             "discount": "20% off", "startDate": "", "endDate": "",
             "redemptionUrl": "", "termsUrl": "", "tags": []},
        ],
        "programs": [
            {"id": "df-p1", "title": "Priceless Cities", "image": "",
             "description": "Mastercard's global program of curated, money-can't-buy experiences in 50+ cities worldwide.",
             "url": ""},
        ],
        "merchants": [
            {"id": "df-m1", "name": "Priceless Restaurants", "category": "Dining",        "logo": "", "country": ""},
            {"id": "df-m2", "name": "Priceless Hotels",      "category": "Travel",        "logo": "", "country": ""},
            {"id": "df-m3", "name": "Priceless Cities",      "category": "Entertainment", "logo": "", "country": ""},
            {"id": "df-m4", "name": "Priceless Transfers",   "category": "Travel",        "logo": "", "country": ""},
        ],
    },
}
