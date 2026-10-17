"""Crédit Agricole Group.

The page (``Credit_Agricole_Platform.html``) reads the cooperative group
(the Regional Banks and Crédit Agricole S.A., with LCL, CA Italia, CA
Personal Finance & Mobility and CA Payment Services) as five discs,
Foundation to Access, with the segments it reports (Retail Banking, Asset
Gathering, Specialised Financial Services, Large Customers, Corporate
Centre), a Mastercard lens (Mastercard leads the cards, but CB, Wero and the
group's own wallet carry the payments) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``Credit_Agricole_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``creditagricole_inventory.py`` and ``creditagricole_story.py``::

    python customers/build_page.py creditagricole
"""

CUSTOMER = {
    "id": "creditagricole",
    "order": 1440,
    "name": "Crédit Agricole",
    "short": "Crédit Agricole",
    "brands": ["Crédit Agricole", "LCL", "BforBank", "Crédit Agricole Italia", "Sofinco", "Agos", "Amundi", "CACIB", "CAWL"],
    "country": "France",
    "region": "Europe",
    "type": "bank",
    "accent": "#006c50",   # Crédit Agricole green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Crédit Agricole", "bg": "#ffffff", "source": "https://commons.wikimedia.org/wiki/File:Cr%C3%A9dit_Agricole_logo_2017.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "France's largest retail banking group as five discs: Regional Bank cards on Cartes Bancaires and mostly "
               "Mastercard, LCL and Italy leaning to Visa, and Wero, its own wallet and CAWL growing beside them.",
    "stats": [
        {"label": "Customers", "value": "55m"},
        {"label": "Group net income 2025", "value": "€8.8bn"},
        {"label": "Monthly Wero users", "value": "~5m"},
        {"label": "Group CET1", "value": "17.2%"},
    ],
    "page": "Credit_Agricole_Platform.html",
    "notes": (
        ("Research notes", "Credit_Agricole_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "racards": {"apis": ["bin_lookup", "transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"],
                    "bundles": ["issuer_toolkit"]},
        "cartwin": {"apis": ["automatic_billing_updater", "consumer_clarity"], "use_cases": ["recurring", "consumer_clarity"], "bundles": ["subscriptions"]},
        "procards": {"apis": ["business_payment_controls", "merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["issuer_toolkit"]},
        "paiementmobile": {"apis": ["transaction_notifications", "merchant_identifier"], "use_cases": ["txnotify", "enrichment"], "bundles": ["pfm_stack"]},
        "wero": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "cawl": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi", "bin_lookup"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "caps": {"apis": ["bin_lookup", "match"], "use_cases": ["bin_lookup"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "agentpay": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["identity", "txnotify"]},
        "fraud": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "premium": {"apis": ["benefits_eligibility", "offers_for_publishers", "priceless_cities"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "capfm": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "regional": {"apis": ["consumer_clarity", "easy_savings"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "issuer_toolkit", "merchant_resolution"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "premium": ("loyalty_stack",),
        "borrow": ("subscriptions", "sustainability"),
    },
}
