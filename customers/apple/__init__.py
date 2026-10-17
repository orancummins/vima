"""Apple Inc., read through payments.

The page (``Apple_Platform.html``) reads Apple through Apple Pay, Apple Wallet,
Apple Card, Apple Cash and Tap to Pay on iPhone, as five discs, Foundation to
Access, with the segments it reports (Americas, Europe, Greater China, Japan,
Rest of Asia Pacific), a Mastercard lens (Mastercard owns Apple's card, but
Apple owns the wallet) and ten journeys, two of them for Mastercard. Public
sources as at 17 October 2026; the research behind it is in
``Apple_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``apple_inventory.py`` and ``apple_story.py``::

    python customers/build_page.py apple
"""

CUSTOMER = {
    "id": "apple",
    "order": 1280,
    "name": "Apple",
    "short": "Apple",
    "brands": ["Apple Pay", "Apple Wallet", "Apple Card", "Apple Cash", "Tap to Pay on iPhone"],
    "country": "United States",
    "region": "Global",
    "type": "tech",
    "accent": "#1d1d1f",   # Apple graphite, the logo's ink as apple.com sets it
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Apple", "bg": "#ffffff", "source": "https://www.apple.com/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Apple's payments as five discs: Apple Pay in 101 countries on every network, and Apple Card on "
               "Mastercard through its move to Chase, but Apple Cash on Visa and the wallet, tokens and NFC terms Apple's own.",
    "stats": [
        {"label": "Net sales FY2025", "value": "$416bn"},
        {"label": "Services Q3 FY2026", "value": "$30.7bn"},
        {"label": "Apple Pay markets", "value": "101"},
        {"label": "Apple Card balances", "value": "$20bn+"},
    ],
    "page": "Apple_Platform.html",
    "notes": (
        ("Research notes", "Apple_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "applepay": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["psi", "bin_lookup"], "bundles": ["merchant_resolution"]},
        "applecard": {"apis": ["benefits_eligibility", "consumer_clarity", "transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "chase": {"apis": ["automatic_billing_updater", "transaction_notifications"], "use_cases": ["recurring"], "bundles": ["subscriptions", "issuer_toolkit"]},
        "acmi": {"apis": ["consumer_clarity"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        "instalments": {"apis": ["consumer_clarity"], "bundles": ["issuer_toolkit"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "india": {"apis": ["bin_lookup", "enhanced_currency_conversion_calculator"], "use_cases": ["findacard"]},
        "taptopay": {"apis": ["match", "merchant_identifier", "bin_lookup"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "taptoshare": {"apis": ["offers_merchant_content", "places"], "use_cases": ["specials", "places"], "bundles": ["loyalty_stack"]},
        "digitalid": {"use_cases": ["identity"]},
        # L4 Business lines and L5 Access
        "savings": {"apis": ["open_finance", "easy_savings"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
        "walletapp": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["enrichment", "txnotify"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "merchant_resolution"),
        "card": ("issuer_toolkit", "pfm_stack"),
        "merchant": ("acquirer_risk", "loyalty_stack"),
        "issuer": ("issuer_toolkit",),
    },
}
