"""United Services Automobile Association (USAA).

The page (``USAA_Platform.html``) reads the US military community's insurer
and bank as five discs, Foundation to Access, with the lines it reports
(Property & Casualty, Banking, Life Insurance), a Mastercard lens (thirty
years of Mastercard, then a clean break to Visa) and ten journeys, two of them
for Mastercard. Public sources as at 17 October 2026; the research behind it
is in ``USAA_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``usaa_inventory.py``
and ``usaa_story.py``::

    python customers/build_page.py usaa
"""

CUSTOMER = {
    "id": "usaa",
    "order": 1230,
    "name": "USAA",
    "short": "USAA",
    "brands": ["USAA", "USAA Federal Savings Bank", "USAA Life Insurance Company", "USAA Perks", "SafePilot"],
    "country": "United States",
    "region": "Americas",
    "type": "bank",
    "accent": "#12395b",   # USAA navy, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "USAA", "bg": "#ffffff", "source": "https://content.usaa.com/mcontent/static_assets/Media/schema-logo-blue-on-white.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The US military community's insurer and bank as five discs: 14.3 million member-owners, Visa debit and "
               "Visa and Amex credit cards since Mastercard lost the portfolio in 2016.",
    "stats": [
        {"label": "Members", "value": "14.3m"},
        {"label": "Net worth", "value": "$38.6bn"},
        {"label": "Bank deposits", "value": "$92bn"},
        {"label": "Cardholders", "value": "4m+"},
    ],
    "page": "USAA_Platform.html",
    "notes": (
        ("Research notes", "USAA_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "visacredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                       "bundles": ["issuer_toolkit"]},
        "cashbackplus": {"apis": ["benefits_eligibility", "places"], "use_cases": ["places", "specials"], "bundles": ["loyalty_stack"]},
        "funding": {"apis": ["bin_lookup", "open_finance"], "use_cases": ["bin_lookup", "identity"]},
        "zelle": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "ai": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "perks": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "relief": {"apis": ["easy_savings", "consumer_clarity"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "deposits": {"apis": ["consumer_clarity", "enhanced_currency_conversion_calculator"], "use_cases": ["consumer_clarity", "settle_in"], "bundles": ["merchant_resolution"]},
        "autoloans": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        "cardbook": {"apis": ["automatic_billing_updater", "consumer_clarity"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "pfm_stack"),
        "mcnow": ("issuer_toolkit",),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "card": ("loyalty_stack", "subscriptions"),
        "drive": ("sustainability",),
    },
}
