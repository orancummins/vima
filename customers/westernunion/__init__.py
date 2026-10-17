"""Western Union.

The page (``Western_Union_Platform.html``) reads the world's best-known
remitter as five discs, Foundation to Access, with its business lines (money
transfer, bill payment, travel money, money orders, digital assets), a
Mastercard lens (an old Send partner, while the stablecoin card went to Visa)
and ten journeys, two of them for Mastercard. Figures are Western Union's own
results and filings, as at 17 October 2026, with the Intermex deal still
pending; the research behind it is in ``Western_Union_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``westernunion_inventory.py`` and ``westernunion_story.py``::

    python customers/build_page.py westernunion
"""

CUSTOMER = {
    "id": "westernunion",
    "order": 1380,
    "name": "Western Union",
    "short": "Western Union",
    "brands": ["Western Union", "Vigo Money", "Eurochange", "Stablecard", "USDPT", "Western Union Rewards"],
    "country": "United States",
    "region": "Global",
    "type": "payments",
    "accent": "#ffdd00",   # Western Union yellow, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Western Union", "bg": "#000000", "source": "https://www.westernunion.com/staticassets/media/Primary_YellowWhite.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The world's best-known remitter as five discs: $4.05 billion of revenue and a USDPT stablecoin, "
               "with Mastercard Send for payouts to cards but Visa behind Stablecard and Intermex still pending.",
    "stats": [
        {"label": "Revenue 2025", "value": "$4.05bn"},
        {"label": "Transfers 2025", "value": "286m"},
        {"label": "Digital share of transfers", "value": "43%"},
        {"label": "Active locations", "value": "360k"},
    ],
    "page": "Western_Union_Platform.html",
    "notes": (
        ("Research notes", "Western_Union_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "digital": {"apis": ["bin_lookup", "enhanced_currency_conversion_calculator"], "use_cases": ["bin_lookup"]},
        "cardfund": {"apis": ["bin_lookup", "match"], "use_cases": ["bin_lookup", "psi"], "bundles": ["acquirer_risk"]},
        "mcsend": {"apis": ["bin_lookup", "enhanced_currency_conversion_calculator"], "use_cases": ["findacard"], "bundles": ["issuer_toolkit"]},
        "a2a": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "stablecard": {"apis": ["transaction_notifications", "enhanced_currency_conversion_calculator"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "netspend": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "vigo": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        # L3 Services
        "compliance": {"apis": ["consumer_clarity", "match"], "use_cases": ["identity"], "bundles": ["acquirer_risk"]},
        "kyc": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "billpay": {"apis": ["automatic_billing_updater", "merchant_identifier"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "travel": {"apis": ["enhanced_currency_conversion_calculator", "places"], "use_cases": ["places"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "acquirer_risk"),
        "mcnow": ("issuer_toolkit",),
        "senddigital": ("acquirer_risk", "loyalty_stack"),
        "stable": ("issuer_toolkit", "pfm_stack"),
        "bills": ("subscriptions",),
    },
}
