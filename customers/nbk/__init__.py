"""National Bank of Kuwait (NBK).

The page (``National_Bank_of_Kuwait_Platform.html``) reads Kuwait's largest
bank as five discs, Foundation to Access, with the businesses it reports
(Consumer, Corporate, Islamic through Boubyan, NBK Wealth and International),
a Mastercard lens (a Visa-led bank where Mastercard owns the Aura co-brand)
and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in
``National_Bank_of_Kuwait_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``nbk_inventory.py``
and ``nbk_story.py``::

    python customers/build_page.py nbk
"""

CUSTOMER = {
    "id": "nbk",
    "order": 980,
    "name": "National Bank of Kuwait (NBK)",
    "short": "NBK",
    "brands": ["NBK", "Weyay Bank", "Boubyan Bank", "NBK Wealth", "UPayments", "NBK-Egypt"],
    "country": "Kuwait",
    "region": "EEMEA",
    "type": "bank",
    "accent": "#21376b",   # NBK navy, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "National Bank of Kuwait", "bg": "#ffffff",
         "source": "https://www.nbk.com/dam/jcr:281bc4f7-7256-48c6-a05e-761bacea00a3/nbk-logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Kuwait's largest bank as five discs: more than 30% of the country's banking assets, flagship cards "
               "on Visa under a seven-year deal, KNET for debit and WAMD, and Mastercard on the Aura co-brand and travel cards.",
    "stats": [
        {"label": "Assets", "value": "KD 46bn"},
        {"label": "Net profit H1 2026", "value": "KD 325m"},
        {"label": "Share of Kuwait assets", "value": "30%+"},
        {"label": "Countries", "value": "13"},
    ],
    "page": "National_Bank_of_Kuwait_Platform.html",
    "notes": (
        ("Research notes", "National_Bank_of_Kuwait_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "aura": {"apis": ["offers_for_publishers", "offers_merchant_content", "benefits_eligibility"], "use_cases": ["specials", "findacard"],
                 "bundles": ["loyalty_stack"]},
        "miles": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility", "priceless_cities"], "use_cases": ["findacard"]},
        "worldmc": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                    "bundles": ["issuer_toolkit"]},
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "commercial": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "upayments": {"apis": ["merchant_identifier", "automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "baas": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "weyay": {"apis": ["consumer_clarity", "easy_savings"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "issuer_toolkit", "acquirer_risk"),
        "mcnow": ("loyalty_stack", "issuer_toolkit"),
        "aura": ("loyalty_stack",),
        "sme": ("acquirer_risk", "subscriptions"),
        "youth": ("pfm_stack",),
    },
}
