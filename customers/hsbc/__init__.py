"""HSBC Holdings plc.

The page (``HSBC_Platform.html``) reads the bank built on Hong Kong and London
as five discs, Foundation to Access, with the businesses it reports (Hong
Kong, UK, Corporate & Institutional Banking, International Wealth & Premier
Banking), a Mastercard lens (Mastercard on credit and corporate cards, Visa on
debit and the first agent) and ten journeys, two of them for Mastercard.
Public sources as at 17 October 2026; the research behind it is in
``HSBC_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``hsbc_inventory.py``
and ``hsbc_story.py``::

    python customers/build_page.py hsbc
"""

CUSTOMER = {
    "id": "hsbc",
    "order": 150,
    "name": "HSBC Holdings",
    "short": "HSBC",
    "brands": ["HSBC", "Hang Seng Bank", "first direct", "M&S Bank", "HSBC Innovation Bank", "PayMe"],
    "country": "United Kingdom",
    "region": "Global",
    "accent": "#db0011",   # HSBC red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "HSBC", "bg": "#ffffff", "source": "static/logos/financial-logos-500/01-financial-institutions/hsbc.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A bank built on Hong Kong and London as five discs: 41 million customers, Mastercard on UK credit, "
               "Hong Kong debit and corporate cards, Visa on UK debit and the first agentic trial.",
    "stats": [
        {"label": "Customers", "value": "41m"},
        {"label": "Total assets", "value": "$3.4tn"},
        {"label": "RoTE H1 2026", "value": "18.2%"},
        {"label": "Card balances", "value": "$25bn"},
    ],
    "page": "HSBC_Platform.html",
    "notes": (
        ("Research notes", "HSBC_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "ukcredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "hkmc": {"apis": ["priceless_cities", "benefits_eligibility"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "hkdebit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "enrichment"], "bundles": ["pfm_stack"]},
        "globalmoney": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["txnotify", "settle_in"]},
        "trackc2a": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "hkvirtual": {"apis": ["business_payment_controls", "merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["issuer_toolkit"]},
        "dms": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi", "bin_lookup"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        # L3 Services
        "fincrime": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "agentic": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["identity", "enrichment"], "bundles": ["merchant_resolution"]},
        "ukrewards": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "sustain": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        # L4 Business lines
        "ukretail": {"apis": ["consumer_clarity", "open_finance_eu"], "use_cases": ["pfm", "consumer_clarity"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "merchant_resolution"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "issuer_toolkit"),
        "premier": ("loyalty_stack",),
        "corp": ("issuer_toolkit",),
    },
}
