"""Samsung Electronics, read through Samsung Wallet.

The page (``Samsung_Platform.html``) reads Samsung as a payments player, as
five discs, Foundation to Access, with the segments it reports (MX and
Networks, Device Solutions, TVs and appliances), a Mastercard lens (inside
every Samsung Wallet, outside Samsung's own money) and ten journeys, two of
them for Mastercard. Public sources as at 17 October 2026; the research behind
it is in ``Samsung_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``samsung_inventory.py`` and ``samsung_story.py``::

    python customers/build_page.py samsung
"""

CUSTOMER = {
    "id": "samsung",
    "order": 1300,
    "name": "Samsung",
    "short": "Samsung",
    "brands": ["Samsung Wallet", "Samsung Pay", "Samsung Pass", "Samsung Galaxy Card", "Samsung Knox", "Galaxy"],
    "country": "South Korea",
    "region": "Global",
    "type": "tech",
    "accent": "#1428a0",   # Samsung blue, the wordmark colour
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Samsung", "bg": "#ffffff", "source": "https://www.samsung.com/us/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Samsung Wallet as five discs: 62 markets and 18.7 million Korean users with Mastercard tokens inside, "
               "while Samsung's own card, transfers and stablecoin went to Visa and USDC.",
    "stats": [
        {"label": "Wallet markets", "value": "62"},
        {"label": "Korean users", "value": "18.7m"},
        {"label": "Korea payments 2024", "value": "KRW 88.6tn"},
        {"label": "US Galaxy devices", "value": "82m"},
    ],
    "page": "Samsung_Platform.html",
    "notes": (
        ("Research notes", "Samsung_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "nfc": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "overseas": {"apis": ["enhanced_currency_conversion_calculator", "priceless_cities"], "use_cases": ["places"]},
        "online": {"apis": ["merchant_identifier", "bin_lookup"], "use_cases": ["psi", "bin_lookup"], "bundles": ["merchant_resolution"]},
        "stablecoin": {"apis": ["enhanced_currency_conversion_calculator"]},
        # L3 Services
        "tokens": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring", "bin_lookup"], "bundles": ["subscriptions"]},
        "clear": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "trips": {"apis": ["priceless_cities", "places"], "use_cases": ["places"]},
        "points": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "payplanner": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "agentic": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
        # L4 Business lines
        "galaxycard": {"apis": ["benefits_eligibility", "consumer_clarity"], "use_cases": ["findacard", "consumer_clarity"], "bundles": ["issuer_toolkit"]},
        "walletexpress": {"apis": ["bin_lookup", "transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("merchant_resolution", "loyalty_stack", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "subscriptions"),
        "pay": ("issuer_toolkit",),
        "korea": ("pfm_stack", "loyalty_stack"),
        "issuer": ("issuer_toolkit",),
    },
}
