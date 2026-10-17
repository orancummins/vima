"""BNP Paribas SA.

The page (``BNP_Paribas_Platform.html``) reads the Paris-based group as five
discs, Foundation to Access, with the divisions it reports (Corporate &
Institutional Banking; Commercial, Personal Banking & Services; Investment &
Protection Services), a Mastercard lens (Mastercard on the challengers, Visa
and domestic schemes at the home banks) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``BNP_Paribas_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``bnpparibas_inventory.py`` and ``bnpparibas_story.py``::

    python customers/build_page.py bnpparibas
"""

CUSTOMER = {
    "id": "bnpparibas",
    "order": 280,
    "name": "BNP Paribas",
    "short": "BNP Paribas",
    "brands": ["BNP Paribas", "BNP Paribas Fortis", "BNL", "BGL BNP Paribas", "Hello bank!", "Nickel", "Cetelem", "Floa", "Arval", "Cardif"],
    "country": "France",
    "region": "Europe",
    "accent": "#008053",   # BNP Paribas green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "BNP Paribas", "bg": "#ffffff", "source": "https://commons.wikimedia.org/wiki/File:BNP_Paribas_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A Paris-based group as five discs: French and Belgian cards on Visa and domestic schemes, Mastercard "
               "on Nickel, Cetelem, Floa, BNL and Poland, and Wero growing beside them.",
    "stats": [
        {"label": "Revenue 2025", "value": "€51.2bn"},
        {"label": "Net income 2025", "value": "€12.2bn"},
        {"label": "Personal Finance customers", "value": "25m"},
        {"label": "Nickel accounts", "value": "4.9m"},
    ],
    "page": "BNP_Paribas_Platform.html",
    "notes": (
        ("Research notes", "BNP_Paribas_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "nickelcard": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "pfm"], "bundles": ["pfm_stack"]},
        "cpay": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                 "bundles": ["issuer_toolkit", "subscriptions"]},
        "floacard": {"apis": ["offers_for_publishers", "consumer_clarity"], "use_cases": ["specials", "enrichment"], "bundles": ["loyalty_stack"]},
        "bnlmc": {"apis": ["bin_lookup", "transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "estreem": {"apis": ["bin_lookup", "merchant_identifier", "match"], "use_cases": ["bin_lookup", "psi"], "bundles": ["acquirer_risk"]},
        "axepta": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "wero": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        # L3 Services
        "screening": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "priceless": {"apis": ["priceless_cities", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "floabnpl": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "recurring"], "bundles": ["merchant_resolution"]},
        "arval": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "nickelpro": {"apis": ["business_payment_controls", "merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "sustainability"),
        "mcnow": ("issuer_toolkit", "loyalty_stack", "pfm_stack"),
        "borrow": ("subscriptions", "merchant_resolution"),
        "sme": ("acquirer_risk",),
        "drive": ("sustainability",),
    },
}
