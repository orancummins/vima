"""UniCredit Bulbank AD.

The page (``UniCredit_Bulbank_Platform.html``) reads Bulgaria's leading
corporate bank, a 99.45% subsidiary of UniCredit, as five discs, Foundation to
Access, with corporate, retail, private, consumer-finance and leasing lines, a
Mastercard lens (every card moved to Mastercard in 2024, instant payments on
BORICA) and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in
``UniCredit_Bulbank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``bulbank_inventory.py`` and ``bulbank_story.py``::

    python customers/build_page.py bulbank
"""

CUSTOMER = {
    "id": "bulbank",
    "order": 610,
    "name": "UniCredit Bulbank",
    "short": "Bulbank",
    "brands": ["UniCredit Bulbank", "Bulbank Mobile", "Bulbank Online", "UniCredit Consumer Financing",
               "UniCredit Leasing", "Comfort by UniCredit"],
    "country": "Bulgaria",
    "region": "Europe",
    "type": "bank",
    "accent": "#e51e26",   # UniCredit red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "UniCredit Bulbank", "bg": "#ffffff",
         "source": "https://www.unicreditbulbank.bg/static/svg/logo__unicredit.3aca52bc5789.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Bulgaria's leading corporate bank as five discs: a million customers, a quarter of the system's "
               "profit, and a card book moved wholly to Mastercard in 2024 while instant payments run on BORICA's Blink.",
    "stats": [
        {"label": "Customers", "value": "1m+"},
        {"label": "Assets H1 2026", "value": "€20.7bn"},
        {"label": "Corporate loan share", "value": "27.1%"},
        {"label": "Mastercard migration support 2024", "value": "BGN 28m"},
    ],
    "page": "UniCredit_Bulbank_Platform.html",
    "notes": (
        ("Research notes", "UniCredit_Bulbank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "pos": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "ecom": {"apis": ["match", "merchant_identifier"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "p2p": {"apis": ["places", "merchant_identifier"], "use_cases": ["places", "enrichment"], "bundles": ["merchant_resolution"]},
        "offers": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials", "findacard"],
                   "bundles": ["loyalty_stack"]},
        "psd2": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L4 Business lines
        "private": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard"]},
        "corp": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "leasing": {"apis": ["carbon_calculator", "business_payment_controls"], "bundles": ["sustainability"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "merchant_resolution"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack",),
        "borrow": ("issuer_toolkit", "loyalty_stack"),
        "sme": ("acquirer_risk", "merchant_resolution"),
    },
}
