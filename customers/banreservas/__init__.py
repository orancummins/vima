"""Banco de Reservas de la República Dominicana (Banreservas).

The page (``Banreservas_Platform.html``) reads the Dominican Republic's
state-owned bank as five discs, Foundation to Access, with the business areas
it reports (personal and SME, corporate, government, tourism, and treasury and
subsidiaries), a Mastercard lens (Mastercard holds the debit, Visa shares the
credit) and eleven journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in ``Banreservas_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``banreservas_inventory.py`` and ``banreservas_story.py``::

    python customers/build_page.py banreservas
"""

CUSTOMER = {
    "id": "banreservas",
    "order": 460,
    "name": "Banreservas",
    "short": "Banreservas",
    "brands": ["Banreservas", "MIO Banreservas", "Seguros Reservas", "AFP Reservas", "Inversiones & Reservas"],
    "country": "Dominican Republic",
    "region": "Latin America",
    "type": "bank",
    "accent": "#005088",   # Banreservas blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Banreservas", "bg": "#ffffff",
         "source": "https://cdnebrpeastus.azureedge.net/banreservas/media/5oebs3sq/banreservas_600px_db_logo.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The Dominican state bank as five discs: a third of the country's loans, 3.8 million debit cards all on "
               "Mastercard, credit shared with Visa, and a new Mastercard commercial card.",
    "stats": [
        {"label": "Assets 2025", "value": "RD$1.28tn"},
        {"label": "Debit cards", "value": "3.8m"},
        {"label": "Credit cards", "value": "1.47m"},
        {"label": "ROE 2025", "value": "20.8%"},
    ],
    "page": "Banreservas_Platform.html",
    "notes": (
        ("Research notes", "Banreservas_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "mccomercial": {"apis": ["easy_savings", "business_payment_controls", "benefits_eligibility"], "bundles": ["issuer_toolkit"]},
        "fleet": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "mio": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["identity", "pfm"], "bundles": ["pfm_stack"]},
        "cardnet": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "remit": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "cyber": {"apis": ["transaction_notifications", "match"], "use_cases": ["txnotify", "identity"]},
        "apis": {"apis": ["open_finance", "bin_lookup"], "use_cases": ["identity"]},
        "puntos": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["findacard", "specials"],
                   "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "sme": {"apis": ["business_payment_controls", "open_finance"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "loyalty_stack", "sustainability"),
        "mcnow": ("issuer_toolkit", "pfm_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "corp": ("sustainability",),
    },
}
