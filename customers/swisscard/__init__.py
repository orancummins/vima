"""Swisscard AECS GmbH.

The page (``Swisscard_Platform.html``) reads Switzerland's three-network card
issuer as five discs, Foundation to Access, with the lines it sells to
(private customers, business customers, private banks, merchants), a
Mastercard lens (Amex's Swiss issuer, with Mastercard as the second card) and
ten journeys, two of them for Mastercard. Public sources as at 17 October
2026; the research behind it is in ``Swisscard_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``swisscard_inventory.py`` and
``swisscard_story.py``::

    python customers/build_page.py swisscard
"""

CUSTOMER = {
    "id": "swisscard",
    "order": 490,
    "name": "Swisscard",
    "short": "Swisscard",
    "brands": ["Swisscard", "American Express", "SWISS Miles & More", "Cashback Cards", "poinz Cards"],
    "country": "Switzerland",
    "region": "Europe",
    "type": "issuer",
    "accent": "#263c53",   # Swisscard navy, the site's theme colour (the logo itself is black)
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Swisscard AECS", "bg": "#ffffff", "source": "https://www.swisscard.ch/en"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Switzerland's three-network card issuer as five discs: owned outright by American Express since "
               "January 2026, Amex first on every consumer card, Mastercard on business cards and as one choice "
               "for the second card.",
    "stats": [
        {"label": "Staff", "value": "650+"},
        {"label": "App users", "value": "400k+"},
        {"label": "Amex acceptance points", "value": "149k+"},
        {"label": "Amex ownership", "value": "100%"},
    ],
    "page": "Swisscard_Platform.html",
    "notes": (
        ("Research notes", "Swisscard_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mm": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility"], "use_cases": ["findacard"],
               "bundles": ["loyalty_stack"]},
        "cashback": {"apis": ["offers_for_publishers", "consumer_clarity"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "sccard": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["pfm", "txnotify"], "bundles": ["pfm_stack"]},
        "mcbiz": {"apis": ["business_payment_controls", "bin_lookup"], "use_cases": ["bin_lookup"], "bundles": ["issuer_toolkit"]},
        "supplier": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "acceptance": {"apis": ["match", "merchant_identifier"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "c2p": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        # L3 Services
        "phishing": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "priceless": {"apis": ["priceless_cities", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "sdg2": {"apis": ["merchant_identifier", "carbon_calculator"], "use_cases": ["enrichment"],
                 "bundles": ["merchant_resolution", "sustainability"]},
        # L4 Business lines
        "wmcfx": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "pfm_stack", "subscriptions"),
        "mcnow": ("loyalty_stack", "issuer_toolkit"),
        "corp": ("issuer_toolkit", "sustainability"),
        "merch": ("acquirer_risk",),
        "cashback": ("loyalty_stack",),
    },
}
