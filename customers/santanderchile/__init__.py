"""Banco Santander Chile.

The page (``Banco_Santander_Chile_Platform.html``) reads Chile's largest bank
by loans, a listed subsidiary two-thirds owned by Banco Santander, as five
discs, Foundation to Access, with the segments it reports (Retail &
Commercial, Wealth Management & Insurance, CIB, Payments and Digital Consumer
Bank), a Mastercard lens (one of three networks, with Visa first to the
agents) and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in
``Banco_Santander_Chile_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``santanderchile_inventory.py`` and ``santanderchile_story.py``::

    python customers/build_page.py santanderchile
"""

CUSTOMER = {
    "id": "santanderchile",
    "order": 380,
    "name": "Banco Santander Chile",
    "short": "Santander Chile",
    "brands": ["Santander", "Santander Life", "Getnet", "Work/Café", "Santander Consumer Finance", "Santander Private Bank"],
    "country": "Chile",
    "region": "Latin America",
    "accent": "#ec0000",   # Santander red, from the logo and the brand
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Santander", "bg": "#ffffff",
         "source": "https://commons.wikimedia.org/wiki/File:Banco_Santander_Logotipo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Chile's largest bank by loans as five discs: 4.8 million customers, a quarter of the country's card "
               "purchases on Mastercard, Visa and Amex, Getnet at 229,000 merchants, and Visa first to the AI agents.",
    "stats": [
        {"label": "Customers", "value": "4.8m"},
        {"label": "ROAE H1 2026", "value": "27.2%"},
        {"label": "Card purchases share", "value": "24.4%"},
        {"label": "Getnet merchants", "value": "229k"},
    ],
    "page": "Banco_Santander_Chile_Platform.html",
    "notes": (
        ("Research notes", "Banco_Santander_Chile_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "latampass": {"apis": ["benefits_eligibility", "bin_lookup", "enhanced_currency_conversion_calculator"],
                      "use_cases": ["findacard", "consumer_clarity"], "bundles": ["issuer_toolkit", "loyalty_stack"]},
        "lifedebit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "pfm"],
                      "bundles": ["pfm_stack"]},
        "lifecredit": {"apis": ["bin_lookup", "automatic_billing_updater"], "use_cases": ["recurring"],
                       "bundles": ["issuer_toolkit"]},
        "wallets": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring", "bin_lookup"],
                    "bundles": ["subscriptions"]},
        "getnet": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "smartpos": {"apis": ["merchant_identifier", "places"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
        "agentpay": {"apis": ["bin_lookup"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"],
                    "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "openfinance": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L4 Business lines
        "consumer": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["consumer_clarity", "enrichment"],
                     "bundles": ["merchant_resolution"]},
        "sme": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("subscriptions", "acquirer_risk", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "travel": ("loyalty_stack",),
        "sme": ("acquirer_risk", "merchant_resolution"),
    },
}
