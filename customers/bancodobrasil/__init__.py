"""Banco do Brasil S.A.

The page (``Banco_do_Brasil_Platform.html``) reads Brazil's state-controlled
bank as five discs, Foundation to Access, with its loan segments
(individuals, companies, agribusiness, government, and group items), a
Mastercard lens (Mastercard third, behind the Elo it owns and Visa's premium
cards) and ten journeys, two of them for Mastercard. Public sources as at 17
October 2026; the research behind it is in ``Banco_do_Brasil_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``bancodobrasil_inventory.py`` and
``bancodobrasil_story.py``::

    python customers/build_page.py bancodobrasil
"""

CUSTOMER = {
    "id": "bancodobrasil",
    "order": 250,
    "name": "Banco do Brasil",
    "short": "Banco do Brasil",
    "brands": ["Banco do Brasil", "Ourocard", "BB Seguridade", "BB Asset", "Banco Patagonia"],
    "country": "Brazil",
    "region": "Latin America",
    "accent": "#465eff",   # BB blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Banco do Brasil", "bg": "#FCFC30", "source": "https://commons.wikimedia.org/wiki/File:Banco_do_Brasil_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Brazil's state-controlled bank as five discs: 92 million customers and Ourocard on Visa, Elo and "
               "Mastercard, with Elo co-owned, Visa on the premium tier and Mastercard third.",
    "stats": [
        {"label": "Customers", "value": "92m"},
        {"label": "Loans", "value": "R$1.31tn"},
        {"label": "Farm credit", "value": "R$422bn"},
        {"label": "Card spend 2Q26", "value": "R$128bn"},
    ],
    "page": "Banco_do_Brasil_Platform.html",
    "notes": (
        ("Research notes", "Banco_do_Brasil_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "ourocard": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"], "bundles": ["issuer_toolkit"]},
        "mcblack": {"apis": ["benefits_eligibility", "priceless_cities", "enhanced_currency_conversion_calculator"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "bbpay": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "cielo": {"apis": ["merchant_identifier", "match"], "bundles": ["acquirer_risk"]},
        "fx": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "agentic": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"], "bundles": ["merchant_resolution"]},
        "minhasfinancas": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "universo": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "agro": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "sme": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "pfm_stack", "sustainability"),
        "mcnow": ("loyalty_stack", "issuer_toolkit"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "premium": ("loyalty_stack",),
        "sme": ("acquirer_risk",),
    },
}
