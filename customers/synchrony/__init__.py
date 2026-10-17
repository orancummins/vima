"""Synchrony Financial.

The page (``Synchrony_Platform.html``) reads America's largest private-label
card issuer as five discs, Foundation to Access, with the five sales platforms
it reports (Digital, Home & Auto, Diversified & Value, Health & Wellness,
Lifestyle), a Mastercard lens (most named co-brands on Mastercard, private
label off-network) and ten journeys, two of them for Mastercard. Public
sources as at 17 October 2026; the research behind it is in
``Synchrony_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``synchrony_inventory.py`` and ``synchrony_story.py``::

    python customers/build_page.py synchrony
"""

CUSTOMER = {
    "id": "synchrony",
    "order": 140,
    "name": "Synchrony",
    "short": "Synchrony",
    "brands": ["Synchrony", "CareCredit", "Synchrony Bank", "Synchrony Pay Later"],
    "country": "United States",
    "region": "Americas",
    "type": "issuer",
    "accent": "#ffd549",   # Synchrony gold, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Synchrony", "bg": "#ffffff", "source": "static/logos/financial-logos-500/01-financial-institutions/synchrony.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "America's largest private-label card issuer as five discs: $102 billion of receivables across "
               "Amazon, Lowe's, PayPal, Walmart and CareCredit, with most co-brands on Mastercard.",
    "stats": [
        {"label": "Receivables", "value": "$102bn"},
        {"label": "Active accounts", "value": "68m"},
        {"label": "Purchase volume 2025", "value": "$182bn"},
        {"label": "Co-brand growth", "value": "+25%"},
    ],
    "page": "Synchrony_Platform.html",
    "notes": (
        ("Research notes", "Synchrony_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "privatelabel": {"apis": ["bin_lookup"], "use_cases": ["bin_lookup"]},
        "mcdual": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater", "benefits_eligibility"],
                   "use_cases": ["consumer_clarity", "recurring"], "bundles": ["issuer_toolkit"]},
        "onepay": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify"],
                   "bundles": ["issuer_toolkit"]},
        "paylater": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "wallets": {"apis": ["bin_lookup"], "use_cases": ["bin_lookup"]},
        # L3 Services
        "underwriting": {"apis": ["open_finance"], "use_cases": ["identity", "enrichment"]},
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "loyalty": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"],
                    "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "agentic": {"apis": ["bin_lookup"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "embedded": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L4 Business lines
        "paypal": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment"],
                   "bundles": ["pfm_stack"]},
        "sams": {"apis": ["business_payment_controls", "benefits_eligibility"], "bundles": ["issuer_toolkit"]},
        "carecredit": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"],
                       "bundles": ["merchant_resolution"]},
        "deposits": {"apis": ["open_finance"], "use_cases": ["pfm"]},
        # L5 Access
        "service": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("subscriptions", "loyalty_stack", "merchant_resolution"),
        "mcnow": ("issuer_toolkit", "pfm_stack"),
        "shop": ("loyalty_stack",),
        "walmart": ("issuer_toolkit",),
        "care": ("merchant_resolution",),
        "partner": ("loyalty_stack", "issuer_toolkit"),
    },
}
