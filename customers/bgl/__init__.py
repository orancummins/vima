"""BGL BNP Paribas S.A.

The page (``BGL_BNP_Paribas_Platform.html``) reads BNP Paribas' Luxembourg
bank as five discs, Foundation to Access, with the lines it reports (Retail &
Corporate Banking, Wealth Management, Leasing International), a Mastercard lens
(Visa in every pocket, Mastercard in the premium one) and nine journeys, two of
them for Mastercard. Public sources as at 17 October 2026; the research behind
it is in ``BGL_BNP_Paribas_research_notes.md``. The parent group is its own
customer (``bnpparibas``).

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``bgl_inventory.py`` and
``bgl_story.py``::

    python customers/build_page.py bgl
"""

CUSTOMER = {
    "id": "bgl",
    "order": 650,
    "name": "BGL BNP Paribas",
    "short": "BGL",
    "brands": ["BGL BNP Paribas", "BNP Paribas Leasing Solutions", "Cardif Lux Vie", "Axepta BNP Paribas"],
    "country": "Luxembourg",
    "region": "Europe",
    "type": "bank",
    "accent": "#00915a",   # BNP Paribas green, the main colour of bgl.lu
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "BGL BNP Paribas", "bg": "#ffffff",
         "source": "https://www.bgl.lu/etc.clientlibs/publicsite/clientlibs/clientlib-base/resources/logo/bgl-logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "BNP Paribas' Luxembourg bank as five discs: a 1919 bank a third owned by the State, Visa debit "
               "in every pack and Mastercard on its premium credit cards, with Wero replacing Payconiq.",
    "stats": [
        {"label": "Net income 2025", "value": "€515m"},
        {"label": "Balance sheet", "value": "€64.6bn"},
        {"label": "CET1", "value": "20.6%"},
        {"label": "Branches", "value": "22"},
    ],
    "page": "BGL_BNP_Paribas_Platform.html",
    "notes": (
        ("Research notes", "BGL_BNP_Paribas_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "visadebit": {"apis": ["transaction_notifications", "enhanced_currency_conversion_calculator"], "use_cases": ["txnotify"]},
        "mcgold": {"apis": ["bin_lookup", "consumer_clarity", "benefits_eligibility"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "mcpremium": {"apis": ["benefits_eligibility", "priceless_cities", "enhanced_currency_conversion_calculator"],
                      "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "visabusiness": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "axepta": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "retour": {"apis": ["benefits_eligibility"], "bundles": ["issuer_toolkit"]},
        "threeds": {"apis": ["transaction_notifications"], "use_cases": ["identity", "txnotify"]},
        "genius": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "aggregator": {"apis": ["open_finance_eu"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "packs": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "privatebank": {"apis": ["priceless_cities", "offers_for_publishers"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "leasing": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack", "acquirer_risk"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "pro": ("acquirer_risk", "issuer_toolkit"),
        "premium": ("loyalty_stack",),
    },
}
