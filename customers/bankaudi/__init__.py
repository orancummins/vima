"""Bank Audi sal.

The page (``Bank_Audi_Platform.html``) reads one of Lebanon's largest banks as
five discs, Foundation to Access, with the businesses it reports (retail and
personal, corporate and SME, private banking, France and other entities), a
Mastercard lens (a Mastercard issuer in a cash economy, now selling acceptance)
and ten journeys, two of them for Mastercard. Public sources as at 17 October
2026; the research behind it is in ``Bank_Audi_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``bankaudi_inventory.py`` and ``bankaudi_story.py``::

    python customers/build_page.py bankaudi
"""

CUSTOMER = {
    "id": "bankaudi",
    "order": 1020,
    "name": "Bank Audi",
    "short": "Bank Audi",
    "brands": ["Bank Audi", "neo by Bank Audi", "Banque Audi (Suisse)", "Audi Capital", "Bank Audi France"],
    "country": "Lebanon",
    "region": "EEMEA",
    "accent": "#191c1f",   # Bank Audi black, from the wordmark logo on bankaudi.com.lb
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Bank Audi", "bg": "#ffffff",
         "source": "https://commons.wikimedia.org/wiki/File:Bank_Audi_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "One of Lebanon's largest banks as five discs: every card it and neo issue is a Mastercard, while "
               "fresh dollars, wallets and cash still move most money and the bank waits on its restructuring.",
    "stats": [
        {"label": "Deposits", "value": "$12.9bn"},
        {"label": "Profit 2025", "value": "$83m"},
        {"label": "Fresh deposits", "value": "$3.4bn"},
        {"label": "SMEs with Mastercard", "value": "10,000"},
    ],
    "page": "Bank_Audi_Platform.html",
    "notes": (
        ("Research notes", "Bank_Audi_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "cedar": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "debit": {"apis": ["transaction_notifications", "enhanced_currency_conversion_calculator"], "use_cases": ["txnotify"]},
        "neocard": {"apis": ["enhanced_currency_conversion_calculator", "consumer_clarity"], "use_cases": ["pfm", "enrichment"],
                    "bundles": ["pfm_stack"]},
        "gpay": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "pos": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "secure": {"apis": ["transaction_notifications"], "use_cases": ["identity", "txnotify"]},
        "offers": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "experiences": {"apis": ["priceless_cities", "benefits_eligibility"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "neobiz": {"apis": ["business_payment_controls", "merchant_identifier"], "use_cases": ["psi", "places"],
                   "bundles": ["acquirer_risk", "merchant_resolution"]},
        "neobank": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["pfm", "txnotify"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "loyalty_stack", "subscriptions"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "digital": ("pfm_stack", "subscriptions"),
        "travel": ("loyalty_stack",),
    },
}
