"""Mitsubishi UFJ Financial Group (MUFG).

The page (``MUFG_Platform.html``) reads Japan's largest bank group as five
discs, Foundation to Access, with the business groups it reports (Retail &
Digital, Commercial Banking & Wealth Management, Japanese CIB, Global
Commercial Banking, and the global businesses), a Mastercard lens (one of four
networks on its cards, while its 2026 scheme alliance went to JCB) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026; the
research behind it is in ``MUFG_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``mufg_inventory.py`` and ``mufg_story.py``::

    python customers/build_page.py mufg
"""

CUSTOMER = {
    "id": "mufg",
    "order": 1520,
    "name": "MUFG",
    "short": "MUFG",
    "brands": ["MUFG Bank", "Mitsubishi UFJ NICOS", "Mitsubishi UFJ Card", "ACOM", "Emut", "MUFG Emut Bank", "Mitsubishi UFJ Trust and Banking", "Danamon"],
    "country": "Japan",
    "region": "Asia-Pacific",
    "type": "bank",
    "accent": "#e60000",   # MUFG red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "MUFG", "bg": "#ffffff",
         "source": "https://commons.wikimedia.org/wiki/File:MUFG_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Japan's largest bank group as five discs: a record ¥809 billion quarter, Mitsubishi UFJ Card on four networks "
               "and AC Mastercard on one, Visa and JCB debit, and a 2026 alliance with JCB.",
    "stats": [
        {"label": "Net profit FY25", "value": "¥2.43trn"},
        {"label": "Bank customers", "value": "34m"},
        {"label": "Market value", "value": "¥41.9trn"},
        {"label": "AC Mastercard holders", "value": "1.05m"},
    ],
    "page": "MUFG_Platform.html",
    "notes": (
        ("Research notes", "MUFG_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mucard": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "acmc": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "recurring"], "bundles": ["subscriptions"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "contactless": {"apis": ["transaction_notifications", "enhanced_currency_conversion_calculator"], "use_cases": ["txnotify"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "identity"]},
        "mapai": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "moneytree": {"apis": ["open_finance"], "use_cases": ["pfm", "identity"], "bundles": ["pfm_stack"]},
        "points": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "excellent": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "corpcard": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L5 Access
        "emutbank": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "pfm_stack", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "card": ("issuer_toolkit", "loyalty_stack"),
        "borrow": ("subscriptions",),
        "emutbank": ("pfm_stack",),
    },
}
