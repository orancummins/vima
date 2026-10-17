"""Grupo Financiero Galicia S.A.

The page (``Grupo_Financiero_Galicia_Platform.html``) reads Argentina's
largest private financial group as five discs, Foundation to Access, with
the companies it reports (Galicia, Naranja X, Galicia Seguros, Fondos Fima
and Galicia Securities), a Mastercard lens (second to Visa, and closing in at
the bank) and nine journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in
``Grupo_Financiero_Galicia_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``galicia_inventory.py`` and ``galicia_story.py``::

    python customers/build_page.py galicia
"""

CUSTOMER = {
    "id": "galicia",
    "order": 370,
    "name": "Grupo Financiero Galicia (Banco Galicia)",
    "short": "Galicia",
    "brands": ["Galicia", "Naranja X", "Galicia Más", "Nave", "Galicia Seguros", "Fondos Fima", "Inviu"],
    "country": "Argentina",
    "region": "Latin America",
    "type": "bank",
    "accent": "#fa6400",   # Galicia orange, from the logo on galicia.ar
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Galicia", "bg": "#fa6400", "source": "https://commons.wikimedia.org/wiki/File:Banco-Galicia_Logo_2024.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Argentina's largest private financial group as five discs: Banco Galicia with HSBC's Argentine bank "
               "folded in, and Naranja X, with 15 million credit cards split between Visa, Mastercard and Naranja's own brand.",
    "stats": [
        {"label": "Loan share", "value": "15.9%"},
        {"label": "Credit cards", "value": "15.0m"},
        {"label": "Mastercard cards", "value": "3.6m"},
        {"label": "ROE Q2 2026", "value": "11.3%"},
    ],
    "page": "Grupo_Financiero_Galicia_Platform.html",
    "notes": (
        ("Research notes", "Grupo_Financiero_Galicia_research_notes.md"),
    ),
    "studio": {
        # L1 Foundation
        "risk": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        # L2 Rails
        "gcredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                    "bundles": ["issuer_toolkit"]},
        "nxcredit": {"apis": ["bin_lookup", "automatic_billing_updater"], "use_cases": ["bin_lookup", "recurring"], "bundles": ["issuer_toolkit"]},
        "naranjabrand": {"apis": ["bin_lookup"], "use_cases": ["findacard"]},
        "nxdebit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "enrichment"]},
        "nave": {"apis": ["merchant_identifier", "match", "places"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "mexico": {"apis": ["enhanced_currency_conversion_calculator", "bin_lookup"], "use_cases": ["settle_in"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["identity", "txnotify"]},
        "quiero": {"apis": ["offers_for_publishers", "offers_merchant_content", "easy_savings"], "use_cases": ["specials", "findacard"],
                   "bundles": ["loyalty_stack"]},
        "eminent": {"apis": ["priceless_cities", "benefits_eligibility"], "use_cases": ["specials"]},
        # L4 Business lines
        "commercial": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L5 Access
        "gapp": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "loyalty_stack"),
        "mcnow": ("issuer_toolkit",),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "premium": ("loyalty_stack",),
    },
}
