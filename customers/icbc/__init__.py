"""Industrial and Commercial Bank of China Limited (ICBC).

The page (``ICBC_Platform.html``) reads the world's largest bank as five
discs, Foundation to Access, with the segments it reports (Corporate banking,
Personal banking, Treasury operations), a Mastercard lens (a UnionPay giant
opening a Mastercard travel lane) and nine journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``ICBC_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``icbc_inventory.py`` and ``icbc_story.py``::

    python customers/build_page.py icbc
"""

CUSTOMER = {
    "id": "icbc",
    "order": 710,
    "name": "ICBC",
    "short": "ICBC",
    "brands": ["ICBC", "Peony", "ICBC e-Life", "ICBC (Asia)", "ICBC (Macau)", "ICBC (Argentina)", "ICBC Standard Bank"],
    "country": "China",
    "region": "Asia-Pacific",
    "accent": "#c7000b",   # ICBC red, from the website and logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "ICBC", "bg": "#ffffff", "source": "https://commons.wikimedia.org/wiki/File:ICBC_China_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The world's largest bank as five discs: 1.3 billion cards mostly on UnionPay at home, and a Mastercard "
               "lane for travellers opened since 2024 with RMB, multi-currency and European travel cards.",
    "stats": [
        {"label": "Assets", "value": "RMB57trn"},
        {"label": "Personal customers", "value": "780m+"},
        {"label": "Bank cards", "value": "1.34bn"},
        {"label": "Mobile MAUs", "value": "300m+"},
    ],
    "page": "ICBC_Platform.html",
    "notes": (
        ("Research notes", "ICBC_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "transaction_notifications"], "use_cases": ["consumer_clarity", "txnotify"],
                   "bundles": ["issuer_toolkit"]},
        "mcrmb": {"apis": ["enhanced_currency_conversion_calculator", "bin_lookup", "benefits_eligibility"], "use_cases": ["bin_lookup", "findacard"],
                  "bundles": ["issuer_toolkit"]},
        "etc": {"apis": ["priceless_cities", "enhanced_currency_conversion_calculator", "benefits_eligibility", "places"],
                "use_cases": ["places", "specials"], "bundles": ["loyalty_stack"]},
        "peonyintl": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["txnotify"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "inbound": {"apis": ["places", "merchant_identifier"], "use_cases": ["places", "settle_in"], "bundles": ["merchant_resolution"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "merchant_identifier"], "use_cases": ["txnotify", "identity"]},
        "ibonus": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "elife": {"apis": ["priceless_cities", "places", "offers_merchant_content"], "use_cases": ["places", "specials"], "bundles": ["loyalty_stack"]},
        "agents": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "inclusive": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "asia": {"apis": ["bin_lookup", "automatic_billing_updater", "consumer_clarity"], "use_cases": ["recurring", "consumer_clarity"],
                 "bundles": ["issuer_toolkit", "subscriptions"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "acquirer_risk", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "travel": ("loyalty_stack",),
        "visit": ("merchant_resolution", "acquirer_risk"),
        "hk": ("issuer_toolkit", "subscriptions"),
    },
}
