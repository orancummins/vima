"""Capital One Financial Corporation.

The page (``Capital_One_Platform.html``) reads America's largest card issuer
by loans, owner of the Discover network since 2025, as five discs,
Foundation to Access, with the segments it reports (Credit Card, Consumer
Banking with the Global Payment Network, Commercial Banking), a Mastercard
lens (debit and new consumer credit moving to Discover, a renewed agreement
for the rest) and ten journeys, two of them for Mastercard. Public sources as
at 17 October 2026; the research behind it is in
``Capital_One_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``capitalone_inventory.py`` and ``capitalone_story.py``::

    python customers/build_page.py capitalone
"""

CUSTOMER = {
    "id": "capitalone",
    "order": 70,
    "name": "Capital One",
    "short": "Capital One",
    "brands": ["Capital One", "Discover", "PULSE", "Diners Club", "Brex"],
    "country": "United States",
    "region": "Americas",
    "type": "bank",
    "accent": "#004977",   # Capital One navy, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Capital One", "bg": "#ffffff", "source": "static/logos/financial-logos-500/01-financial-institutions/capital-one.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "America's largest card issuer by loans, and now owner of the Discover network, as five discs: debit "
               "and new consumer credit moving off Mastercard, business and co-brand cards staying.",
    "stats": [
        {"label": "Assets", "value": "$674bn"},
        {"label": "Card loans", "value": "$275bn"},
        {"label": "Debit to Discover", "value": "~25m cards"},
        {"label": "Network volume Q2", "value": "$190bn"},
    ],
    "page": "Capital_One_Platform.html",
    "notes": (
        ("Research notes", "Capital_One_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "migration": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"],
                      "use_cases": ["consumer_clarity", "recurring"], "bundles": ["issuer_toolkit"]},
        "venturex": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility"]},
        "spark": {"apis": ["business_payment_controls", "benefits_eligibility", "carbon_calculator"],
                  "bundles": ["issuer_toolkit", "sustainability"]},
        "cobrands": {"apis": ["offers_for_publishers", "benefits_eligibility"], "bundles": ["loyalty_stack"]},
        "intl": {"apis": ["enhanced_currency_conversion_calculator", "bin_lookup"]},
        # L3 Services
        "eno": {"apis": ["transaction_notifications", "automatic_billing_updater"], "use_cases": ["txnotify", "recurring"],
                "bundles": ["subscriptions"]},
        "mcservices": {"apis": ["transaction_notifications", "consumer_clarity", "bin_lookup"],
                       "use_cases": ["txnotify", "consumer_clarity"], "bundles": ["issuer_toolkit", "merchant_resolution"]},
        "travel": {"apis": ["priceless_cities", "enhanced_currency_conversion_calculator"], "use_cases": ["specials"],
                   "bundles": ["loyalty_stack"]},
        "shopping": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard"],
                     "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "cards": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["pfm_stack"]},
        "brex": {"apis": ["business_payment_controls", "open_finance"], "bundles": ["issuer_toolkit"]},
        "bank360": {"apis": ["open_finance", "consumer_clarity"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "merchant_resolution"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "subscriptions"),
        "travel": ("loyalty_stack",),
        "sme": ("issuer_toolkit", "sustainability"),
    },
}
