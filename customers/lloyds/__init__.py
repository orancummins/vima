"""Lloyds Banking Group plc.

The page (``Lloyds_Banking_Group_Platform.html``) reads Britain's biggest
retail bank as five discs, Foundation to Access, with the segments it reports
(Retail, Commercial Banking, Insurance, Pensions & Investments), a Mastercard
lens (a Visa bank buying a Mastercard wallet) and ten journeys, two of them
for Mastercard. Public sources as at 17 October 2026; the research behind it
is in ``Lloyds_Banking_Group_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``lloyds_inventory.py`` and ``lloyds_story.py``::

    python customers/build_page.py lloyds
"""

CUSTOMER = {
    "id": "lloyds",
    "order": 270,
    "name": "Lloyds Banking Group",
    "short": "Lloyds",
    "brands": ["Lloyds", "Halifax", "Bank of Scotland", "MBNA", "Scottish Widows", "Curve"],
    "country": "United Kingdom",
    "region": "Europe",
    "accent": "#006a4a",   # Lloyds green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Lloyds Banking Group", "bg": "#ffffff", "source": "https://www.lloydsbankinggroup.com/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Britain's biggest retail bank as five discs: half of UK adults, debit on Visa and 10 million credit "
               "cards moving there too, while it builds a wallet on Curve's Mastercard.",
    "stats": [
        {"label": "Customers", "value": "28m"},
        {"label": "Loans", "value": "£491bn"},
        {"label": "RoTE H1 2026", "value": "17.1%"},
        {"label": "Curve customers", "value": "6m+"},
    ],
    "page": "Lloyds_Banking_Group_Platform.html",
    "notes": (
        ("Research notes", "Lloyds_Banking_Group_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "curve": {"apis": ["enhanced_currency_conversion_calculator", "consumer_clarity", "merchant_identifier"],
                  "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "accept": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "payfrom": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "assistant": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "accounts": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "auto": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "business": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "loyalty_stack", "sustainability"),
        "mcnow": ("pfm_stack", "issuer_toolkit"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "loyalty_stack"),
        "drive": ("sustainability",),
    },
}
