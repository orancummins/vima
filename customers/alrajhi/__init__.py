"""Al Rajhi Bank (Al Rajhi Banking & Investment Corp.).

The page (``Al_Rajhi_Bank_Platform.html``) reads the world's largest Islamic
bank as five discs, Foundation to Access, with the segments it reports
(Retail, Corporate & SME, Treasury, Investment services & brokerage), a
Mastercard lens (a mada-and-Visa bank where Mastercard works the till) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``Al_Rajhi_Bank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``alrajhi_inventory.py`` and
``alrajhi_story.py``::

    python customers/build_page.py alrajhi
"""

CUSTOMER = {
    "id": "alrajhi",
    "order": 1610,
    "name": "Al Rajhi Bank",
    "short": "Al Rajhi",
    "brands": ["alrajhi bank", "urpay", "neoleap", "Emkan", "Al Rajhi Capital", "neotek", "Drahim", "Tahweel Al Rajhi"],
    "country": "Saudi Arabia",
    "region": "EEMEA",
    "type": "bank",
    "accent": "#150fe0",   # alrajhi bank blue, the single colour of the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Al Rajhi Bank", "bg": "#ffffff",
         "source": "https://www.alrajhibank.com.sa/-/media/Project/AlRajhi/ARBRevamp/Temp/AlRajhiBankLogo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The world's largest Islamic bank as five discs: 22 million customers, mada debit and a Visa card range "
               "with 38% of the Kingdom's credit cards, and Mastercard on its terminals and in urpay's transfers.",
    "stats": [
        {"label": "Customers", "value": "22m"},
        {"label": "Assets", "value": "SAR 1.06tn"},
        {"label": "Profit H1 2026", "value": "SAR 13.8bn"},
        {"label": "Share of POS terminals", "value": "43.5%"},
    ],
    "page": "Al_Rajhi_Bank_Platform.html",
    "notes": (
        ("Research notes", "Al_Rajhi_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "madadebit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater", "benefits_eligibility"],
                   "use_cases": ["consumer_clarity", "recurring", "findacard"], "bundles": ["issuer_toolkit"]},
        "prepaid": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "corpcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "pos": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "ecom": {"apis": ["match", "bin_lookup"], "use_cases": ["bin_lookup", "recurring"], "bundles": ["acquirer_risk", "subscriptions"]},
        "urpaycards": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "pfm"], "bundles": ["pfm_stack"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "ai": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "neotek": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "mokafaa": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "sme": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "pfm_stack", "loyalty_stack"),
        "mcnow": ("acquirer_risk", "subscriptions"),
        "merchant": ("acquirer_risk", "loyalty_stack"),
        "card": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
    },
}
