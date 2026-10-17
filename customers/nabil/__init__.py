"""Nabil Bank Limited.

The page (``Nabil_Bank_Platform.html``) reads Nepal's most profitable bank as
five discs, Foundation to Access, with the product lines it reports (financial
intermediation, treasury, trade finance, and cards, e-banking and channels), a
Mastercard lens (a Visa-first bank where QR moves the money and Mastercard is
building in debit) and ten journeys, two of them for Mastercard. Public sources
as at 17 October 2026; the research behind it is in
``Nabil_Bank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``nabil_inventory.py``
and ``nabil_story.py``::

    python customers/build_page.py nabil
"""

CUSTOMER = {
    "id": "nabil",
    "order": 860,
    "name": "Nabil Bank",
    "short": "Nabil",
    "brands": ["Nabil Bank", "nBank", "Nabil Remit", "nRemit", "Nabil Investment Banking", "Nabil Stock Dealer"],
    "country": "Nepal",
    "region": "Asia-Pacific",
    "accent": "#12b25a",   # Nabil green, from the logo and nabilbank.com
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Nabil Bank", "bg": "#ffffff",
         "source": "https://assets.nabilbank.com/uploads/logo/nabil%20logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Nepal's most profitable bank as five discs: debit and credit on Visa and Mastercard, prepaid on Visa, "
               "QR on Fonepay, and a new Mastercard debit card in a market where QR and NCHL's rails move most of the money.",
    "stats": [
        {"label": "Customers", "value": "2.5m+"},
        {"label": "Deposits", "value": "NPR 603bn"},
        {"label": "Profit FY2025/26", "value": "NPR 7.9bn"},
        {"label": "nBank users", "value": "1.8m"},
    ],
    "page": "Nabil_Bank_Platform.html",
    "notes": (
        ("Research notes", "Nabil_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debitmc": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"],
                    "bundles": ["issuer_toolkit"]},
        "creditmc": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "qr": {"apis": ["merchant_identifier", "places"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
        "pos": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "epg": {"apis": ["match", "merchant_identifier", "bin_lookup"], "use_cases": ["psi", "bin_lookup"], "bundles": ["acquirer_risk"]},
        "nremit": {"apis": ["enhanced_currency_conversion_calculator", "bin_lookup"], "use_cases": ["bin_lookup"]},
        "nepalnow": {"apis": ["enhanced_currency_conversion_calculator", "places", "priceless_cities"], "use_cases": ["places", "specials"]},
        # L3 Services
        "fraudops": {"apis": ["transaction_notifications", "merchant_identifier"], "use_cases": ["txnotify", "enrichment"],
                     "bundles": ["merchant_resolution"]},
        "openapi": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "offers": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "installment": {"apis": ["consumer_clarity", "benefits_eligibility"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        # L5 Access
        "app": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "credit": ("loyalty_stack", "issuer_toolkit"),
    },
}
