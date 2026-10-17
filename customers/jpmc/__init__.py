"""JPMorgan Chase & Co.

The page (``JPMorgan_Chase_Platform.html``) reads America's largest bank as
five discs, Foundation to Access, with the segments it reports (Consumer &
Community Banking, Commercial & Investment Bank, Asset & Wealth Management),
a Mastercard lens (a Visa bank, with eight Mastercards and Apple Card coming)
and eleven journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in
``JPMorgan_Chase_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``jpmc_inventory.py``
and ``jpmc_story.py``::

    python customers/build_page.py jpmc
"""

CUSTOMER = {
    "id": "jpmc",
    "order": 80,
    "name": "JPMorgan Chase",
    "short": "JPMC",
    "brands": ["Chase", "J.P. Morgan", "J.P. Morgan Payments", "Kinexys", "Chase UK"],
    "country": "United States",
    "region": "Americas",
    "type": "bank",
    "accent": "#004fc2",   # Chase blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Chase", "bg": "#ffffff", "source": "static/logos/financial-logos-500/01-financial-institutions/jpmorgan-chase.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "America's largest bank as five discs: $5.1 trillion of assets and the biggest US card book, "
               "mostly on Visa, with Apple Card arriving on Mastercard around 2028.",
    "stats": [
        {"label": "Assets", "value": "$5.1tn"},
        {"label": "Customers", "value": "94m"},
        {"label": "Card sales 2025", "value": "$1.94tn"},
        {"label": "Apple Card", "value": "$20bn+"},
    ],
    "page": "JPMorgan_Chase_Platform.html",
    "notes": (
        ("Research notes", "JPMorgan_Chase_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "acquiring": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"],
                      "bundles": ["acquirer_risk"]},
        "mccards": {"apis": ["benefits_eligibility", "priceless_cities", "consumer_clarity", "bin_lookup"],
                    "use_cases": ["specials", "consumer_clarity"], "bundles": ["issuer_toolkit", "loyalty_stack"]},
        "applecard": {"apis": ["automatic_billing_updater", "consumer_clarity", "transaction_notifications"],
                      "use_cases": ["recurring", "txnotify", "consumer_clarity"],
                      "bundles": ["issuer_toolkit", "subscriptions"]},
        "visacards": {"apis": ["bin_lookup"], "use_cases": ["bin_lookup"]},
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "commcards": {"apis": ["business_payment_controls", "carbon_calculator"],
                      "bundles": ["issuer_toolkit", "sustainability"]},
        "treasury": {"apis": ["enhanced_currency_conversion_calculator"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "dataaccess": {"apis": ["open_finance"], "use_cases": ["identity", "enrichment"], "bundles": ["pfm_stack"]},
        "offers": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard"],
                   "bundles": ["loyalty_stack"]},
        "agentic": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        # L4 Business lines
        "checking": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"],
                     "bundles": ["pfm_stack"]},
        "business": {"apis": ["business_payment_controls", "open_finance"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "pfm_stack", "subscriptions", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "apple": ("issuer_toolkit", "subscriptions"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "merchant": ("acquirer_risk", "loyalty_stack"),
        "corp": ("issuer_toolkit", "sustainability"),
    },
}
