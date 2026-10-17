"""DBS Group Holdings Ltd.

The page (``DBS_Platform.html``) reads Singapore's largest bank as five
discs, Foundation to Access, with the segments it reports (Consumer
Banking/Wealth Management, Institutional Banking, Markets Trading), a
Mastercard lens (an even split, with Visa on the miles cards and Mastercard
first with agents) and nine journeys, two of them for Mastercard. Public
sources as at 17 October 2026; the research behind it is in
``DBS_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``dbs_inventory.py`` and ``dbs_story.py``::

    python customers/build_page.py dbs
"""

CUSTOMER = {
    "id": "dbs",
    "order": 340,
    "name": "DBS Group",
    "short": "DBS",
    "brands": ["DBS", "POSB", "digibank", "PayLah!", "DBS IDEAL", "DBS Treasures", "DBS Digital Exchange"],
    "country": "Singapore",
    "region": "Asia-Pacific",
    "accent": "#ff3333",   # DBS red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "DBS", "bg": "#ffffff", "source": "https://www.dbs.com/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Singapore's largest bank as five discs: cards split evenly between Visa and Mastercard, the first live "
               "Agent Pay payments in Singapore and Hong Kong, and PayLah! at the hawker stall.",
    "stats": [
        {"label": "Assets", "value": "S$966bn"},
        {"label": "2Q26 net profit", "value": "S$3.08bn"},
        {"label": "Wealth assets", "value": "S$516bn"},
        {"label": "PayLah! users", "value": "3m+"},
    ],
    "page": "DBS_Platform.html",
    "notes": (
        ("Research notes", "DBS_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "altitude": {"apis": ["bin_lookup", "consumer_clarity", "enhanced_currency_conversion_calculator"], "use_cases": ["consumer_clarity"],
                     "bundles": ["issuer_toolkit"]},
        "womans": {"apis": ["offers_for_publishers", "benefits_eligibility"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "posbeveryday": {"apis": ["consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                         "bundles": ["issuer_toolkit"]},
        "hkcards": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "debitcards": {"apis": ["transaction_notifications", "enhanced_currency_conversion_calculator"], "use_cases": ["txnotify"]},
        "remit": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "scams": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "agentpay": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["enrichment"]},
        "digibot": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "points": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L5 Access
        "digibank": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "consumer_clarity", "settle_in"],
                     "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "pfm_stack", "merchant_resolution"),
        "mcnow": ("loyalty_stack", "issuer_toolkit"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "card": ("loyalty_stack", "issuer_toolkit"),
    },
}
