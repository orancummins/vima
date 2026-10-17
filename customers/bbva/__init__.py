"""Banco Bilbao Vizcaya Argentaria, S.A. (BBVA).

The page (``BBVA_Platform.html``) reads Spain's second bank and Mexico's
first as five discs, Foundation to Access, with the areas it reports (Spain,
Mexico, South America, Rest of Business, Corporate Center), a Mastercard lens
(two Visa home markets, with Mastercard at the digital edges) and ten
journeys, two of them for Mastercard. Garanti BBVA is a separate customer.
Public sources as at 17 October 2026; the research behind it is in
``BBVA_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``bbva_inventory.py`` and ``bbva_story.py``::

    python customers/build_page.py bbva
"""

CUSTOMER = {
    "id": "bbva",
    "order": 1480,
    "name": "BBVA",
    "short": "BBVA",
    "brands": ["BBVA", "BBVA México", "BBVA Spain", "BBVA Italy", "BBVA Germany", "Openpay"],
    "country": "Spain",
    "region": "Europe",
    "type": "bank",
    "accent": "#001391",   # BBVA electric blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "BBVA", "bg": "#ffffff", "source": "https://commons.wikimedia.org/wiki/File:BBVA_logo_2025.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Spain's second bank and Mexico's first as five discs: 82.8 million customers on Visa at home, with "
               "Mastercard on the Italian and German digital banks' credit cards and Mexican virtual cards.",
    "stats": [
        {"label": "Active customers", "value": "82.8m"},
        {"label": "Profit H1 2026", "value": "€6.1bn"},
        {"label": "ROTE H1 2026", "value": "22.2%"},
        {"label": "Mexico customers", "value": "34.5m"},
    ],
    "page": "BBVA_Platform.html",
    "notes": (
        ("Research notes", "BBVA_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mxcredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "mxdebit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "escredit": {"apis": ["bin_lookup", "benefits_eligibility"], "use_cases": ["findacard"], "bundles": ["issuer_toolkit"]},
        "decredit": {"apis": ["enhanced_currency_conversion_calculator", "consumer_clarity"], "use_cases": ["consumer_clarity", "settle_in"],
                     "bundles": ["issuer_toolkit"]},
        "vcn": {"apis": ["business_payment_controls", "merchant_identifier"], "use_cases": ["enrichment"]},
        "barrio": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "spei": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "bizum": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L3 Services
        "agentic": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
        "blue": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "puntos": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "smes": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "merchant_resolution", "pfm_stack"),
        "mcnow": ("issuer_toolkit",),
        "mexico": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk",),
        "firstcard": ("issuer_toolkit", "loyalty_stack"),
    },
}
