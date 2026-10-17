"""Nu Holdings Ltd. (Nubank).

The page (``Nubank_Platform.html``) reads Brazil's largest private financial
institution by customers as five discs, Foundation to Access, with its reported gross-profit mix
(credit, fees, float), a Mastercard lens (Mastercard on every Nu card, while
Pix takes the spend) and ten journeys, two of them for Mastercard. Public
sources as at 17 October 2026; the research behind it is in
``Nubank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``nubank_inventory.py`` and ``nubank_story.py``::

    python customers/build_page.py nubank
"""

CUSTOMER = {
    "id": "nubank",
    "order": 170,
    "name": "Nu Holdings",
    "short": "Nubank",
    "brands": ["Nubank", "Nu", "Nu Empresas", "Ultravioleta", "Croma", "NuPay", "NuCel"],
    "country": "Brazil",
    "region": "Latin America",
    "accent": "#820ad1",   # Nubank purple, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Nubank", "bg": "#ffffff", "source": "static/logos/financial-logos-500/01-financial-institutions/nubank.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A Latin American digital bank as five discs: 139 million customers and every named card on "
               "Mastercard, while Pix, Pix financing and NuPay move spend off the card rails.",
    "stats": [
        {"label": "Customers", "value": "139m"},
        {"label": "Net income Q2 2026", "value": "$1.06bn"},
        {"label": "Card book", "value": "$26bn"},
        {"label": "ROE", "value": "33%"},
    ],
    "page": "Nubank_Platform.html",
    "notes": (
        ("Research notes", "Nubank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "ccbr": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                 "bundles": ["issuer_toolkit"]},
        "ultravioleta": {"apis": ["benefits_eligibility", "priceless_cities", "enhanced_currency_conversion_calculator"], "use_cases": ["specials"],
                         "bundles": ["loyalty_stack"]},
        "croma": {"apis": ["benefits_eligibility", "automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "debitmx": {"apis": ["transaction_notifications", "places"], "use_cases": ["txnotify", "places"]},
        "paybytap": {"apis": ["bin_lookup", "transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "nuglobal": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["settle_in", "txnotify"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "identity"], "bundles": ["merchant_resolution"]},
        "openfinance": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "points": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials", "findacard"],
                   "bundles": ["loyalty_stack"]},
        # L1 Foundation
        "aiagents": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "smeaccept": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "uscard": {"apis": ["benefits_eligibility", "consumer_clarity", "easy_savings"], "use_cases": ["consumer_clarity"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "merchant_resolution", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "premium": ("loyalty_stack", "subscriptions"),
        "sme": ("acquirer_risk",),
    },
}
