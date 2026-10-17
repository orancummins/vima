"""Amazon.com, Inc.

The page (``Amazon_Platform.html``) reads the world's largest online store
through payments, as five discs, Foundation to Access, with the segments it
reports (North America, International, AWS), a Mastercard lens (accepted
everywhere, but Visa holds the cards that matter) and ten journeys, two of
them for Mastercard. Public sources as at 17 October 2026; the research behind
it is in ``Amazon_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``amazon_inventory.py`` and ``amazon_story.py``::

    python customers/build_page.py amazon
"""

CUSTOMER = {
    "id": "amazon",
    "order": 350,
    "name": "Amazon",
    "short": "Amazon",
    "brands": ["Amazon", "Amazon Pay", "Prime", "Buy with Prime", "AWS", "Amazon Business", "Whole Foods Market"],
    "country": "United States",
    "region": "Global",
    "type": "merchant",
    "accent": "#ff9900",   # Amazon orange, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Amazon", "bg": "#ffffff", "source": "https://commons.wikimedia.org/wiki/File:Amazon_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The world's largest online store as five discs: $716.9 billion of sales and Mastercard accepted "
               "everywhere, but Visa holds the US, UK and German co-brands and the agentic tools on AWS.",
    "stats": [
        {"label": "Net sales 2025", "value": "$717bn"},
        {"label": "Q2 2026 sales", "value": "$200.6bn"},
        {"label": "Amazon Business", "value": "$60bn"},
        {"label": "Rufus users", "value": "300m+"},
    ],
    "page": "Amazon_Platform.html",
    "notes": (
        ("Research notes", "Amazon_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "amazonpay": {"apis": ["merchant_identifier", "bin_lookup"], "use_cases": ["psi", "bin_lookup"], "bundles": ["merchant_resolution"]},
        "japanmc": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "recargable": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "synpaylater": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "accept": {"apis": ["bin_lookup", "merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "prime": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "rufus": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "buyforme": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
        # L4 Business lines
        "onlinestores": {"apis": ["consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "wholefoods": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        "marketplace": {"apis": ["merchant_identifier", "match"], "bundles": ["acquirer_risk"]},
        "business": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("merchant_resolution", "issuer_toolkit"),
        "mcnow": ("acquirer_risk", "issuer_toolkit"),
        "shop": ("merchant_resolution", "acquirer_risk"),
        "prime": ("subscriptions", "loyalty_stack"),
        "seller": ("acquirer_risk",),
    },
}
