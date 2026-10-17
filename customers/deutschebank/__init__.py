"""Deutsche Bank AG.

The page (``Deutsche_Bank_Platform.html``) reads the self-styled Global Hausbank as
five discs, Foundation to Access, with the divisions it reports (Private
Bank, Corporate Bank, Investment Bank, Asset Management, and group items), a
Mastercard lens (Mastercard on every card, with girocard and Wero at home)
and ten journeys, two of them for Mastercard. Public sources as at 17 October
2026; the research behind it is in ``Deutsche_Bank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``deutschebank_inventory.py`` and
``deutschebank_story.py``::

    python customers/build_page.py deutschebank
"""

CUSTOMER = {
    "id": "deutschebank",
    "order": 310,
    "name": "Deutsche Bank",
    "short": "Deutsche Bank",
    "brands": ["Deutsche Bank", "Postbank", "DWS", "BHW", "Vert"],
    "country": "Germany",
    "region": "Europe",
    "type": "bank",
    "accent": "#0018a8",   # Deutsche Bank blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Deutsche Bank", "bg": "#ffffff", "source": "static/logos/financial-logos-500/01-financial-institutions/deutsche-bank.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The self-styled Global Hausbank as five discs: Mastercard on every Deutsche Bank and Postbank card and the "
               "Miles & More card since 2025, beside girocard, Wero and Amex corporate cards.",
    "stats": [
        {"label": "Private clients (DE)", "value": "19m"},
        {"label": "Loans", "value": "€491bn"},
        {"label": "Net profit Q2 2026", "value": "€1.9bn"},
        {"label": "Miles & More members", "value": "36m+"},
    ],
    "page": "Deutsche_Bank_Platform.html",
    "notes": (
        ("Research notes", "Deutsche_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "dbcard": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"]},
        "dbcredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"], "bundles": ["issuer_toolkit"]},
        "milesmore": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility", "offers_for_publishers"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "bizcard": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "amex": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "ms": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "rtp": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "vert": {"apis": ["merchant_identifier", "match"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "cybersource": {"apis": ["match", "merchant_identifier"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "aiclient": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "milespay": {"apis": ["offers_merchant_content", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "pbanking": {"apis": ["open_finance_eu", "consumer_clarity"], "use_cases": ["identity", "consumer_clarity"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "sustainability"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("merchant_resolution", "pfm_stack"),
        "fly": ("loyalty_stack",),
        "merch": ("acquirer_risk",),
    },
}
