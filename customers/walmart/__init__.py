"""Walmart Inc.

The page (``Walmart_Platform.html``) reads the world's largest retailer
through payments, as five discs, Foundation to Access, with the segments it
reports (Walmart U.S., Walmart International, Sam's Club U.S.), a Mastercard
lens (Mastercard carries Walmart's cards while Walmart fights its fees) and
ten journeys, two of them for Mastercard. Public sources as at 17 October
2026; the research behind it is in ``Walmart_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``walmart_inventory.py`` and ``walmart_story.py``::

    python customers/build_page.py walmart
"""

CUSTOMER = {
    "id": "walmart",
    "order": 1390,
    "name": "Walmart",
    "short": "Walmart",
    "brands": ["Walmart", "OnePay", "Walmart+", "Walmart Pay", "Sam's Club", "PhonePe", "Flipkart", "Cashi"],
    "country": "United States",
    "region": "Global",
    "type": "merchant",
    "accent": "#0053e2",   # Walmart True Blue, from the wordmark and corporate.walmart.com
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Walmart", "bg": "#ffffff",
         "source": "https://corporate.walmart.com/content/dam/corporate/site-images/WMT-Wordmark-New-Small-Black_RGB.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The world's largest retailer as five discs: $713.2 billion of revenue, its flagship cards on "
               "Mastercard through OnePay and Sam's Club, and the loudest objector to the Visa–Mastercard fee settlement.",
    "stats": [
        {"label": "Revenue FY26", "value": "$713bn"},
        {"label": "Q2 FY27 revenue", "value": "$187.9bn"},
        {"label": "Stores & clubs", "value": "11,000"},
        {"label": "OnePay monthly users", "value": "6m"},
    ],
    "page": "Walmart_Platform.html",
    "notes": (
        ("Research notes", "Walmart_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "cashrewards": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "samsmc": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "accept": {"apis": ["bin_lookup", "merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "taptopay": {"apis": ["bin_lookup"], "use_cases": ["bin_lookup"], "bundles": ["merchant_resolution"]},
        "klarna": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "moneyservices": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "walmartplus": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "onepayagents": {"apis": ["open_finance"], "use_cases": ["pfm", "identity"], "bundles": ["pfm_stack"]},
        "fincrimes": {"use_cases": ["identity"], "bundles": ["issuer_toolkit"]},
        "connect": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "onepaycash": {"apis": ["open_finance", "consumer_clarity"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        "marketplace": {"apis": ["merchant_identifier", "match"], "bundles": ["acquirer_risk"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "pfm_stack"),
        "mcnow": ("acquirer_risk", "issuer_toolkit"),
        "shop": ("merchant_resolution", "acquirer_risk"),
        "plus": ("subscriptions", "loyalty_stack"),
        "onepay": ("pfm_stack",),
    },
}
