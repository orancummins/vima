"""Standard Bank Group Limited.

The page (``Standard_Bank_Platform.html``) reads Africa's largest bank as five
discs, Foundation to Access, with the business units it reports (Personal &
Private Banking, Business & Commercial Banking, Corporate & Investment Banking,
Insurance & Asset Management), a Mastercard lens (Mastercard's retail card
book, on a bank building its own rails) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is in
``Standard_Bank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``standardbank_inventory.py`` and ``standardbank_story.py``::

    python customers/build_page.py standardbank
"""

CUSTOMER = {
    "id": "standardbank",
    "order": 1080,
    "name": "Standard Bank",
    "short": "Standard Bank",
    "brands": ["Standard Bank", "Stanbic", "Liberty", "STANLIB", "Diners Club SA", "Shyft", "SnapScan", "SimplyBlu"],
    "country": "South Africa",
    "region": "EEMEA",
    "type": "bank",
    "accent": "#0033aa",   # Standard Bank blue, from the site's header and logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Standard Bank", "bg": "#0033aa",
         "source": "https://www.standardbank.com/file_source/assets/icons/header-full.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Africa's largest bank as five discs: 19.5 million clients, a South African retail card book on Mastercard, "
               "Visa at the private end, and low-value payments moving onto PayShap and the bank's own rails.",
    "stats": [
        {"label": "Active clients", "value": "19.5m"},
        {"label": "Assets", "value": "R3.8trn"},
        {"label": "ROE H1 2026", "value": "19.8%"},
        {"label": "Card acquiring H1", "value": "R129bn"},
    ],
    "page": "Standard_Bank_Platform.html",
    "notes": (
        ("Research notes", "Standard_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "debit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "enrichment"]},
        "worldcitizen": {"apis": ["benefits_eligibility", "priceless_cities", "enhanced_currency_conversion_calculator"], "use_cases": ["findacard", "specials"]},
        "tokens": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "simplyblu": {"apis": ["merchant_identifier", "places"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
        "corpcards": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "payshap": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "personalisation": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "ucount": {"apis": ["offers_for_publishers", "offers_merchant_content", "easy_savings"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "bcb": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit", "subscriptions"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "loyalty_stack", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "merchant_resolution"),
        "everyday": ("pfm_stack", "loyalty_stack"),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "credit": ("issuer_toolkit", "subscriptions"),
    },
}
