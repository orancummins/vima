"""Arab Bank plc.

The page (``Arab_Bank_Platform.html``) reads Jordan's largest bank as five
discs, Foundation to Access, with the business lines it reports (Consumer
Banking & Wealth Management, Corporate & Institutional Banking, Treasury), a
Mastercard lens (Visa's bank in Jordan, with Mastercard on remittances and the
top tier) and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in ``Arab_Bank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``arabbank_inventory.py`` and ``arabbank_story.py``::

    python customers/build_page.py arabbank
"""

CUSTOMER = {
    "id": "arabbank",
    "order": 1010,
    "name": "Arab Bank",
    "short": "Arab Bank",
    "brands": ["Arab Bank", "Reflect", "Arabi Mobile", "Acabes", "Omnify", "Arab Bank Switzerland"],
    "country": "Jordan",
    "region": "EEMEA",
    "accent": "#1501ff",   # Arab Bank blue, the deep end of the logo's circles
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Arab Bank", "bg": "#ffffff", "source": "https://www.arabbank.com/Mvc/Content/images/logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Jordan's largest bank as five discs: a network of 600 branches since 1930, debit and most credit on "
               "Visa, and Mastercard on RemitEx remittances and the World Elite card.",
    "stats": [
        {"label": "Assets", "value": "$80bn"},
        {"label": "Profit H1 2026", "value": "$571m"},
        {"label": "Share of Jordan's assets", "value": "25.7%"},
        {"label": "Branches", "value": "600+"},
    ],
    "page": "Arab_Bank_Platform.html",
    "notes": (
        ("Research notes", "Arab_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "visacredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                       "bundles": ["issuer_toolkit"]},
        "mccredit": {"apis": ["priceless_cities", "benefits_eligibility", "enhanced_currency_conversion_calculator"], "use_cases": ["specials"],
                     "bundles": ["loyalty_stack"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "remitex": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["txnotify"]},
        "cliq": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "reva": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "omnify": {"apis": ["open_finance", "bin_lookup"], "use_cases": ["identity", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "points": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "sme": {"apis": ["business_payment_controls", "merchant_identifier"], "bundles": ["merchant_resolution"]},
        "corpcard": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "pfm_stack", "acquirer_risk"),
        "mcnow": ("loyalty_stack", "acquirer_risk"),
        "everyday": ("pfm_stack", "loyalty_stack"),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "wealth": ("loyalty_stack",),
    },
}
