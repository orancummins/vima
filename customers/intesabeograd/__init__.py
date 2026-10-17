"""Banca Intesa a.d. Beograd.

The page (``Banca_Intesa_Beograd_Platform.html``) reads Serbia's largest bank,
a wholly owned subsidiary of Intesa Sanpaolo, as five discs, Foundation to
Access, with its divisions (Retail & Wealth Management, Small business &
farmers, Corporate & SME, Treasury & central functions), a Mastercard lens
(Serbia's first Mastercard issuer, now Visa on debit and Mastercard on credit)
and ten journeys, two of them for Mastercard. Public sources as at 17 October
2026; the research behind it is in ``Banca_Intesa_Beograd_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``intesabeograd_inventory.py`` and
``intesabeograd_story.py``::

    python customers/build_page.py intesabeograd
"""

CUSTOMER = {
    "id": "intesabeograd",
    "order": 690,
    "name": "Banca Intesa Beograd",
    "short": "Banca Intesa",
    "brands": ["Banca Intesa", "Intesa Sanpaolo", "Intesa Mobi", "Intesa Magnifica", "Intesa Invest", "Intesa Farmer"],
    "country": "Serbia",
    "region": "Europe",
    "type": "bank",
    "accent": "#006935",   # Banca Intesa green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Banca Intesa, Intesa Sanpaolo Group", "bg": "#ffffff",
         "source": "https://res.cloudinary.com/bib-bank/image/upload/prod/publicportal/logo/BANCA_INTESA/SVG/BANCA_INTESA_Color.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Serbia's largest bank as five discs: 1.34 million clients, the country's first Mastercard issuer now "
               "on Visa and DinaCard for debit, Mastercard and Amex on credit, and the biggest merchant network.",
    "stats": [
        {"label": "Clients", "value": "1.34m"},
        {"label": "Assets 2024", "value": "RSD 1.03tn"},
        {"label": "Net profit 2025", "value": "€265m"},
        {"label": "Online acquiring", "value": "71%"},
    ],
    "page": "Banca_Intesa_Beograd_Platform.html",
    "notes": (
        ("Research notes", "Banca_Intesa_Beograd_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mccredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "mcplatinum": {"apis": ["benefits_eligibility", "priceless_cities", "enhanced_currency_conversion_calculator"],
                       "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "mcbusiness": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "applepay": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "ecom": {"apis": ["automatic_billing_updater", "merchant_identifier"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        # L3 Services
        "tds": {"apis": ["transaction_notifications"], "use_cases": ["identity", "txnotify"]},
        "galerija": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "airserbia": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator"], "use_cases": ["findacard"],
                      "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "corporate": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        # L5 Access
        "mobi": {"apis": ["consumer_clarity", "open_finance_eu"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "issuer_toolkit", "acquirer_risk"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "merchant": ("acquirer_risk", "subscriptions"),
        "credit": ("issuer_toolkit", "loyalty_stack"),
    },
}
