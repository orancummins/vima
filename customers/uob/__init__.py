"""United Overseas Bank Limited (UOB).

The page (``UOB_Platform.html``) reads Singapore's UOB as five discs, Foundation
to Access, with the segments it reports (Group Retail, Group Wholesale Banking,
Global Markets), a Mastercard lens (Visa holds the premium tier, Mastercard holds
regional debit, SME cards and agentic payments) and nine journeys, two of them
for Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``UOB_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``uob_inventory.py``
and ``uob_story.py``::

    python customers/build_page.py uob
"""

CUSTOMER = {
    "id": "uob",
    "order": 1580,
    "name": "UOB",
    "short": "UOB",
    "brands": ["UOB", "UOB TMRW", "UOB Infinity", "UOB Privilege Banking", "UOB Private Bank", "UOB Malaysia", "UOB Thailand", "UOB Indonesia", "UOB Vietnam"],
    "country": "Singapore",
    "region": "Asia-Pacific",
    "type": "bank",
    "accent": "#005cb9",   # UOB blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "UOB", "bg": "#ffffff", "source": "https://www.uob.com.sg/assets/iwov-resources/assets/BrandAssets/UOB_Logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Singapore's UOB as five discs: ASEAN's top card issuer by billings with Citi's four consumer books "
               "absorbed, premium cards on Visa, regional debit and Agent Pay on Mastercard.",
    "stats": [
        {"label": "Retail customers", "value": "8.5m+"},
        {"label": "2Q26 net profit", "value": "S$1.48bn"},
        {"label": "Total assets", "value": "S$572bn"},
        {"label": "HNW AUM", "value": "S$204bn"},
    ],
    "page": "UOB_Platform.html",
    "notes": (
        ("Research notes", "UOB_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "sgmc": {"apis": ["bin_lookup", "consumer_clarity", "benefits_eligibility"], "use_cases": ["consumer_clarity", "findacard"],
                 "bundles": ["issuer_toolkit"]},
        "regdebit": {"apis": ["transaction_notifications", "enhanced_currency_conversion_calculator"], "use_cases": ["txnotify"]},
        "fxplus": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "regal": {"apis": ["business_payment_controls", "benefits_eligibility"], "bundles": ["issuer_toolkit"]},
        "commercial": {"apis": ["business_payment_controls", "easy_savings"], "bundles": ["issuer_toolkit"]},
        "smartpay": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "scantopay": {"apis": ["places", "merchant_identifier"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "agentpay": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["enrichment"]},
        "insights": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["findacard", "specials"],
                    "bundles": ["loyalty_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "issuer_toolkit", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "pfm_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "travel": ("merchant_resolution", "loyalty_stack"),
        "sme": ("issuer_toolkit",),
    },
}
