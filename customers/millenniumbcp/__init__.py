"""Millennium bcp (Banco Comercial Português, S.A.).

The page (``Millennium_BCP_Platform.html``) reads Portugal's second-largest
bank as five discs, Foundation to Access, with the segments it reports (Retail
Banking, Companies, Corporate & Investment Banking, Private Banking and the
international activity in Poland and Mozambique), a Mastercard lens (a Visa bank
at home, dual-network in Poland) and ten journeys, two of them for Mastercard.
Public sources as at 17 October 2026; the research behind it is in
``Millennium_BCP_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``millenniumbcp_inventory.py`` and ``millenniumbcp_story.py``::

    python customers/build_page.py millenniumbcp
"""

CUSTOMER = {
    "id": "millenniumbcp",
    "order": 570,
    "name": "Millennium BCP",
    "short": "Millennium bcp",
    "brands": ["Millennium bcp", "ActivoBank", "Bank Millennium", "Millennium bim", "Millenniumbcp Ageas"],
    "country": "Portugal",
    "region": "Europe",
    "type": "bank",
    "accent": "#d1005d",   # Millennium magenta, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Millennium bcp", "bg": "#ffffff", "source": "https://www.millenniumbcp.pt/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Portugal's second-largest bank as five discs: 7.4 million customers in three countries, Visa and "
               "Multibanco on every new card at home, and Mastercard holding on through Bank Millennium in Poland.",
    "stats": [
        {"label": "Active customers", "value": "7.4m"},
        {"label": "Net income H1 2026", "value": "€566m"},
        {"label": "ROE H1 2026", "value": "14.6%"},
        {"label": "Mobile customers", "value": "75%"},
    ],
    "page": "Millennium_BCP_Platform.html",
    "notes": (
        ("Research notes", "Millennium_BCP_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "mcbiz": {"apis": ["business_payment_controls", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "bizcredit": {"apis": ["business_payment_controls"], "use_cases": ["bin_lookup"]},
        "tpa": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "payme": {"apis": ["match", "merchant_identifier"], "use_cases": ["recurring"], "bundles": ["acquirer_risk", "subscriptions"]},
        "c2p": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "dmm": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials", "findacard"],
                    "bundles": ["loyalty_stack"]},
        "tpaanalytics": {"apis": ["merchant_identifier", "places"], "use_cases": ["places", "enrichment"], "bundles": ["merchant_resolution"]},
        "apis": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L4 Business lines
        "companies": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "loyalty_stack", "merchant_resolution"),
        "mcnow": ("issuer_toolkit", "subscriptions"),
        "everyday": ("pfm_stack",),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "sme": ("issuer_toolkit", "sustainability"),
    },
}
