"""Société Générale S.A.

The page (``Societe_Generale_Platform.html``) reads the Paris-based group as
five discs, Foundation to Access, with the pillars it reports (French Retail,
Private Banking and Insurance; Global Banking and Investor Solutions;
Mobility, International Retail Banking and Financial Services), a Mastercard
lens (Visa holds French retail; Mastercard keeps corporates, Romania and
premium credit) and ten journeys, two of them for Mastercard. Public sources
as at 17 October 2026; the research behind it is in
``Societe_Generale_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``socgen_inventory.py`` and ``socgen_story.py``::

    python customers/build_page.py socgen
"""

CUSTOMER = {
    "id": "socgen",
    "order": 1450,
    "name": "Société Générale",
    "short": "SocGen",
    "brands": ["SG", "BoursoBank", "Komerční banka", "BRD", "Ayvens", "Fiditalia", "Hanseatic Bank", "SG-Forge"],
    "country": "France",
    "region": "Europe",
    "type": "bank",
    "accent": "#e60028",   # Société Générale red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Société Générale", "bg": "#ffffff", "source": "https://www.societegenerale.com/sites/default/files/image/logo/soc103-1.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A Paris-based group as five discs: French retail and BoursoBank on Cartes Bancaires and Visa, Mastercard "
               "on corporate cards, BRD, KB's World Elite and Fiditalia, and Wero growing beside them.",
    "stats": [
        {"label": "Net income 2025", "value": "€6.0bn"},
        {"label": "Net income H1 2026", "value": "€3.5bn"},
        {"label": "Clients", "value": "27m"},
        {"label": "BoursoBank clients", "value": "9.1m"},
    ],
    "page": "Societe_Generale_Platform.html",
    "notes": (
        ("Research notes", "Societe_Generale_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "corpmc": {"apis": ["business_payment_controls", "transaction_notifications"], "use_cases": ["txnotify", "enrichment"], "bundles": ["issuer_toolkit"]},
        "boursocards": {"apis": ["transaction_notifications", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["txnotify", "recurring"],
                        "bundles": ["pfm_stack", "subscriptions"]},
        "brdcards": {"apis": ["bin_lookup", "offers_for_publishers", "transaction_notifications"], "use_cases": ["specials", "txnotify"], "bundles": ["issuer_toolkit", "loyalty_stack"]},
        "kbwe": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "fiditalia": {"apis": ["consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"], "bundles": ["subscriptions"]},
        "wero": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "payxpert": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "boursoenc": {"apis": ["merchant_identifier", "bin_lookup"], "use_cases": ["bin_lookup", "psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "priceless": {"apis": ["priceless_cities", "offers_merchant_content"], "use_cases": ["specials", "places"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "ayvens": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "bourso": {"apis": ["open_finance_eu", "consumer_clarity"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "sustainability"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "online": ("pfm_stack", "subscriptions"),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "drive": ("sustainability",),
    },
}
