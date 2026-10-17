"""Eurobank (Eurobank S.A., with Eurobank Cyprus and Postbank Bulgaria).

The page (``Eurobank_Platform.html``) reads one of Greece's four systemic
banks as five discs, Foundation to Access, with the countries it reports
(Greece, Cyprus, Bulgaria, plus the group and Luxembourg), a Mastercard lens (a
dual-network bank moving all its Greek cards to Mastercard) and ten journeys,
two of them for Mastercard. Public sources as at 17 October 2026; the research
behind it is in ``Eurobank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``eurobank_inventory.py`` and ``eurobank_story.py``::

    python customers/build_page.py eurobank
"""

CUSTOMER = {
    "id": "eurobank",
    "order": 580,
    "name": "Eurobank",
    "short": "Eurobank",
    "brands": ["Eurobank", "Eurobank Cyprus", "Hellenic Bank", "Postbank", "Eurobank Private Bank Luxembourg", "Eurolife"],
    "country": "Greece",
    "region": "Europe",
    "type": "bank",
    "accent": "#ea002a",   # Eurobank red, from the logo mark
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Eurobank", "bg": "#ffffff",
         "source": "https://commons.wikimedia.org/wiki/File:Eurobank_logo_2021.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "One of Greece's four big banks as five discs: €113 billion across Greece, Cyprus and Bulgaria, "
               "a card book that issued on Visa and Mastercard now moving all to Mastercard, with acceptance left to Worldline.",
    "stats": [
        {"label": "Assets", "value": "€113bn"},
        {"label": "Profit H1 2026", "value": "€738m"},
        {"label": "RoTBV H1 2026", "value": "16.6%"},
        {"label": "Digital transactions", "value": "96%"},
    ],
    "page": "Eurobank_Platform.html",
    "notes": (
        ("Research notes", "Eurobank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "grcards": {"apis": ["automatic_billing_updater", "bin_lookup", "consumer_clarity"], "use_cases": ["recurring", "consumer_clarity"],
                    "bundles": ["issuer_toolkit"]},
        "bizcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "cycards": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "wallets": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "worldline": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "upi": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "eva": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "epistrofi": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "priceless": {"apis": ["priceless_cities", "benefits_eligibility"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "onboard": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L4 Business lines
        "business": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "subscriptions", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "loyalty_stack"),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "card": ("loyalty_stack",),
    },
}
