"""PayPal Holdings, Inc.

The page (``PayPal_Platform.html``) reads the digital wallet as five discs,
Foundation to Access, with its three businesses (Checkout Solutions & PayPal,
Consumer Financial Services & Venmo, Payment Services & Crypto), a Mastercard
lens (Mastercard's debit partner, with Visa in Venmo credit and cash-out) and
ten journeys, two of them for Mastercard. Public sources as at 17 October
2026; the research behind it is in ``PayPal_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``paypal_inventory.py`` and ``paypal_story.py``::

    python customers/build_page.py paypal
"""

CUSTOMER = {
    "id": "paypal",
    "order": 240,
    "name": "PayPal Holdings",
    "short": "PayPal",
    "brands": ["PayPal", "Venmo", "Braintree", "Xoom", "Hyperwallet", "Honey", "Paidy", "PYUSD"],
    "country": "United States",
    "region": "Global",
    "accent": "#003087",   # PayPal navy, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "PayPal", "bg": "#ffffff", "source": "static/logos/financial-logos-500/02-payments-and-processors/paypal.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The digital wallet as five discs: 439 million accounts and $1.79 trillion of volume, every debit card "
               "on Mastercard and Agent Pay in the wallet, with Visa in Venmo credit and a takeover bid in the air.",
    "stats": [
        {"label": "Active accounts", "value": "439m"},
        {"label": "TPV 2025", "value": "$1.79tn"},
        {"label": "Revenue 2025", "value": "$33.2bn"},
        {"label": "Pay Later TPV", "value": "$40bn+"},
    ],
    "page": "PayPal_Platform.html",
    "notes": (
        ("Research notes", "PayPal_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "fastlane": {"apis": ["bin_lookup", "automatic_billing_updater"], "use_cases": ["bin_lookup", "recurring"], "bundles": ["subscriptions"]},
        "braintree": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "xoom": {"apis": ["enhanced_currency_conversion_calculator"]},
        "ppdebit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "pfm"], "bundles": ["issuer_toolkit", "pfm_stack"]},
        "venmodebit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "cashback": {"apis": ["consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity"], "bundles": ["issuer_toolkit"]},
        "paylater": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L3 Services
        "fraud": {"apis": ["consumer_clarity", "match"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "agentpay": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "workingcapital": {"apis": ["open_finance", "business_payment_controls"], "use_cases": ["identity"]},
        "merchant": {"apis": ["merchant_identifier", "carbon_calculator"], "bundles": ["merchant_resolution", "sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("merchant_resolution", "loyalty_stack", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "subscriptions"),
        "instore": ("issuer_toolkit", "loyalty_stack"),
        "ent": ("acquirer_risk", "subscriptions"),
        "pay": ("merchant_resolution",),
    },
}
