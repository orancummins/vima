"""HDFC Bank Limited.

The page (``HDFC_Bank_Platform.html``) reads India's largest private bank as
five discs, Foundation to Access, with the segments it reports (Retail
Banking, Wholesale Banking, Treasury, Other Banking Business), a Mastercard
lens (one network of four at India's biggest card issuer) and ten journeys,
two of them for Mastercard. Public sources as at 17 October 2026; the
research behind it is in ``HDFC_Bank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``hdfc_inventory.py`` and ``hdfc_story.py``::

    python customers/build_page.py hdfc
"""

CUSTOMER = {
    "id": "hdfc",
    "order": 730,
    "name": "HDFC Bank",
    "short": "HDFC Bank",
    "brands": ["HDFC Bank", "PayZapp", "SmartHub Vyapar", "SmartGATEWAY", "Infinia", "HDFC Life", "HDFC ERGO", "HDFC AMC", "HDB Financial Services"],
    "country": "India",
    "region": "Asia-Pacific",
    "type": "bank",
    "accent": "#004c8f",   # HDFC Bank blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "HDFC Bank", "bg": "#004c8f", "source": "https://www.hdfc.bank.in/content/dam/hdfcbankpws/home-page/hdfc-bank-logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "India's largest private bank as five discs: 22% of the country's credit cards on four networks, a third of "
               "its card acquiring, Swiggy on Mastercard and credit on UPI through RuPay.",
    "stats": [
        {"label": "Customers", "value": "103.6m"},
        {"label": "Q2 FY27 profit", "value": "₹195bn"},
        {"label": "Credit-card share", "value": "22%"},
        {"label": "Acquiring share", "value": "35–36%"},
    ],
    "page": "HDFC_Bank_Platform.html",
    "notes": (
        ("Research notes", "HDFC_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "cards": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                  "bundles": ["issuer_toolkit"]},
        "premium": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator", "priceless_cities"], "use_cases": ["specials"],
                    "bundles": ["loyalty_stack"]},
        "swiggy": {"apis": ["offers_for_publishers", "offers_merchant_content", "benefits_eligibility"], "use_cases": ["specials", "findacard"],
                   "bundles": ["loyalty_stack"]},
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "vyapar": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "gateway": {"apis": ["match", "automatic_billing_updater"], "use_cases": ["psi", "recurring"], "bundles": ["acquirer_risk", "subscriptions"]},
        "xborder": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "recurring": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "bots": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines and L5 Access
        "bizcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "payzapp": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "pfm_stack"),
        "mcnow": ("loyalty_stack", "subscriptions"),
        "card": ("loyalty_stack", "issuer_toolkit"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
    },
}
