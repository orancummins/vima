"""Banco Nacional de Bolivia S.A.

The page (``Banco_Nacional_de_Bolivia_Platform.html``) reads Bolivia's
third-largest bank as five discs, Foundation to Access, with its business
areas (Corporate & Business, Mass Banking, SME & Microcredit, Finance &
International), a Mastercard lens (a Visa bank that gave Mastercard its
company cards) and ten journeys, two of them for Mastercard. Public sources
as at 17 October 2026; the research behind it is in
``Banco_Nacional_de_Bolivia_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``bnb_inventory.py`` and
``bnb_story.py``::

    python customers/build_page.py bnb
"""

CUSTOMER = {
    "id": "bnb",
    "order": 440,
    "name": "Banco Nacional de Bolivia",
    "short": "BNB",
    "brands": ["BNB", "BNB Móvil", "Bille", "Cuenta Cripto BNB", "BNB Leasing", "BNB SAFI", "BNB Valores"],
    "country": "Bolivia",
    "region": "Latin America",
    "type": "bank",
    "accent": "#2bb461",   # BNB green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Banco Nacional de Bolivia", "bg": "#ffffff", "source": "https://commons.wikimedia.org/wiki/File:Banco_Nacional_de_Bolivia_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Bolivia's third-largest bank as five discs: Visa on every consumer card, Mastercard on a new corporate "
               "range since September 2025, and QR and USDT moving money outside the networks.",
    "stats": [
        {"label": "Assets 2025", "value": "$5.4bn"},
        {"label": "Loan share", "value": "11.4%"},
        {"label": "ROE 2025", "value": "14.6%"},
        {"label": "Digital txns", "value": "97%"},
    ],
    "page": "Banco_Nacional_de_Bolivia_Platform.html",
    "notes": (
        ("Research notes", "Banco_Nacional_de_Bolivia_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "visacredit": {"apis": ["bin_lookup", "consumer_clarity"], "use_cases": ["consumer_clarity", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "mccorp": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        "cta": {"apis": ["business_payment_controls", "enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "qr": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "intl": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "analytics": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "apis": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "cashback": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        # L4 / L5
        "sme": {"apis": ["business_payment_controls"], "bundles": ["merchant_resolution"]},
        "app": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["pfm", "txnotify"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "loyalty_stack", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "sustainability"),
        "corp": ("issuer_toolkit",),
        "everyday": ("pfm_stack", "loyalty_stack"),
        "sme": ("acquirer_risk", "merchant_resolution"),
    },
}
