"""Marqeta, Inc.

The page (``Marqeta_Platform.html``) reads the card-issuing processor as five
discs, Foundation to Access, with its customer verticals (financial services,
lending and BNPL, expense management, on-demand), a Mastercard lens (a
Mastercard investee whose biggest cards are Visa) and ten journeys, two of them
for Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``Marqeta_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``marqeta_inventory.py`` and ``marqeta_story.py``::

    python customers/build_page.py marqeta
"""

CUSTOMER = {
    "id": "marqeta",
    "order": 1330,
    "name": "Marqeta",
    "short": "Marqeta",
    "brands": ["Marqeta", "TransactPay", "Marqeta Hub", "Real-Time Decisioning", "UX Toolkit"],
    "country": "United States",
    "region": "Global",
    "type": "payments",
    "accent": "#2f0046",   # Marqeta deep purple, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Marqeta", "bg": "#ffffff",
         "source": "https://cdn.sanity.io/images/kcoh87zr/production/5135ac8ec40af9a8732d15f3211868e9a4423a75-154x16.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A card-issuing processor as five discs: $383 billion of volume and a Mastercard stake, while Cash App, "
               "Klarna, Affirm and Ramp issue on Visa.",
    "stats": [
        {"label": "Volume 2025", "value": "$383bn"},
        {"label": "Volume Q2 2026", "value": "$120bn"},
        {"label": "Net revenue 2025", "value": "$625m"},
        {"label": "Block share Q2", "value": "41%"},
    ],
    "page": "Marqeta_Platform.html",
    "notes": (
        ("Research notes", "Marqeta_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "processing": {"apis": ["bin_lookup", "transaction_notifications"], "use_cases": ["bin_lookup", "txnotify"], "bundles": ["issuer_toolkit"]},
        "debit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"]},
        "credit": {"apis": ["automatic_billing_updater", "consumer_clarity"], "use_cases": ["recurring"], "bundles": ["issuer_toolkit"]},
        "onecred": {"apis": ["bin_lookup", "consumer_clarity"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        "payouts": {"apis": ["enhanced_currency_conversion_calculator", "open_finance"], "use_cases": ["identity"]},
        "virtual": {"apis": ["business_payment_controls", "merchant_identifier"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "rtd": {"apis": ["merchant_identifier", "consumer_clarity"], "use_cases": ["enrichment", "consumer_clarity"], "bundles": ["merchant_resolution"]},
        "risk": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content", "benefits_eligibility"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "mcp": {"apis": ["business_payment_controls", "transaction_notifications"], "use_cases": ["txnotify"]},
        # L4 Business lines
        "expense": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "digbank": {"apis": ["open_finance", "consumer_clarity"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "merchant_resolution", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "pfm_stack"),
        "launch": ("issuer_toolkit", "merchant_resolution"),
        "credit": ("issuer_toolkit", "loyalty_stack"),
        "expense": ("sustainability",),
    },
}
