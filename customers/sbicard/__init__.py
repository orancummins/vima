"""SBI Cards and Payment Services Limited (SBI Card).

The page (``SBI_Card_Platform.html``) reads India's largest pure-play credit-card
issuer as five discs, Foundation to Access, with its spends split the way it
reports them (retail and corporate cards), a Mastercard lens (one of four
networks, winning co-brands card by card) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is in
``SBI_Card_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``sbicard_inventory.py`` and ``sbicard_story.py``::

    python customers/build_page.py sbicard
"""

CUSTOMER = {
    "id": "sbicard",
    "order": 1560,
    "name": "SBI Card",
    "short": "SBI Card",
    "brands": ["SBI Card", "AURUM", "ELITE", "SimplySAVE", "SimplyCLICK", "SBI Card SPRINT", "Ask ILA"],
    "country": "India",
    "region": "Asia-Pacific",
    "type": "issuer",
    "accent": "#1a287b",   # SBI Card navy, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "SBI Card", "bg": "#ffffff", "source": "https://www.sbicard.com/static-resources/img/svg-icons/sbi-card-logo-light.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "India's largest pure-play card issuer as five discs: 2.26 crore cards on Visa, Mastercard, RuPay and Amex, "
               "with Mastercard on Flipkart and Eternal, Visa on PhonePe and Google Pay, and RuPay on UPI.",
    "stats": [
        {"label": "Cards in force", "value": "2.26 crore"},
        {"label": "Q1 FY27 spends", "value": "₹1.18 lakh cr"},
        {"label": "Card share", "value": "18.6%"},
        {"label": "Q1 FY27 profit", "value": "₹664 cr"},
    ],
    "page": "SBI_Card_Platform.html",
    "notes": (
        ("Research notes", "SBI_Card_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "core": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                 "bundles": ["issuer_toolkit"]},
        "elite": {"apis": ["benefits_eligibility", "priceless_cities", "enhanced_currency_conversion_calculator"], "use_cases": ["specials"],
                  "bundles": ["loyalty_stack"]},
        "eternal": {"apis": ["offers_for_publishers", "offers_merchant_content", "benefits_eligibility"], "use_cases": ["specials", "findacard"],
                    "bundles": ["loyalty_stack"]},
        "flipkart": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "krisflyer": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility"], "use_cases": ["settle_in"]},
        "mdes": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "corpcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "sprint": {"apis": ["bin_lookup"], "use_cases": ["identity"]},
        "hyper": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "offers": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "pfm_stack"),
        "mcnow": ("loyalty_stack", "issuer_toolkit"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "partner": ("loyalty_stack",),
        "corp": ("issuer_toolkit",),
    },
}
