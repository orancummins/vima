"""ICICI Bank Limited.

The page (``ICICI_Bank_Platform.html``) reads India's second-largest private
bank as five discs, Foundation to Access, with the segments it reports (Retail
Banking, Wholesale Banking, Treasury, Other Banking), a Mastercard lens (the
other half of ICICI's dual-network card pairs, while Visa holds Amazon Pay and
the top end) and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in ``ICICI_Bank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``icici_inventory.py`` and ``icici_story.py``::

    python customers/build_page.py icici
"""

CUSTOMER = {
    "id": "icici",
    "order": 1550,
    "name": "ICICI Bank",
    "short": "ICICI Bank",
    "brands": ["ICICI Bank", "iMobile", "InstaBIZ", "Money2India", "ICICI Prudential Life", "ICICI Lombard", "ICICI Prudential AMC", "ICICI Securities"],
    "country": "India",
    "region": "Asia-Pacific",
    "type": "bank",
    "accent": "#ad1f24",   # ICICI Bank maroon, the site's primary; the logo runs #be2a2a to #ef7f1a
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "ICICI Bank", "bg": "#ffffff", "source": "https://www.icici.bank.in/content/dam/icicibank-revamp/logo-hamb.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "India's second-largest private bank as five discs: 16% of the country's credit cards, issued in Mastercard-and-Amex "
               "or Visa-and-RuPay pairs, Amazon Pay and the top end on Visa, and credit on UPI through RuPay.",
    "stats": [
        {"label": "Q1 FY27 profit", "value": "₹148bn"},
        {"label": "Credit-card share", "value": "16.1%"},
        {"label": "Branches", "value": "7,608"},
        {"label": "Return on assets", "value": "2.49%"},
    ],
    "page": "ICICI_Bank_Platform.html",
    "notes": (
        ("Research notes", "ICICI_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "cards": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                  "bundles": ["issuer_toolkit"]},
        "gemstone": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "emeralde": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator", "priceless_cities"], "use_cases": ["specials"],
                     "bundles": ["loyalty_stack"]},
        "amazonpay": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"],
                      "bundles": ["loyalty_stack"]},
        "makemytrip": {"apis": ["enhanced_currency_conversion_calculator", "offers_merchant_content"], "use_cases": ["specials", "settle_in"]},
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "bizcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "xborder": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "wallets": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "mcmarketing": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "subscriptions", "loyalty_stack"),
        "mcnow": ("loyalty_stack", "pfm_stack"),
        "amazon": ("loyalty_stack",),
        "merchant": ("acquirer_risk", "merchant_resolution"),
    },
}
