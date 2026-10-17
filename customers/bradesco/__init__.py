"""Banco Bradesco S.A.

The page (``Bradesco_Platform.html``) reads the Brazilian bank as five
discs, Foundation to Access, with its reported segments (banking, split by
individuals, small firms and large corporates, and insurance), a Mastercard
lens (Elo's co-owner, with Mastercard at the edges) and ten journeys, two of
them for Mastercard. Public sources as at 17 October 2026; the research
behind it is in ``Bradesco_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``bradesco_inventory.py`` and
``bradesco_story.py``::

    python customers/build_page.py bradesco
"""

CUSTOMER = {
    "id": "bradesco",
    "order": 210,
    "name": "Banco Bradesco",
    "short": "Bradesco",
    "brands": ["Bradesco", "Digio", "Bradesco Seguros", "Bradescard", "Ágora"],
    "country": "Brazil",
    "region": "Latin America",
    "accent": "#cc092f",   # Bradesco red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Bradesco", "bg": "#ffffff", "source": "https://commons.wikimedia.org/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A Brazilian bank as five discs: 74 million clients and R$360 billion of card spending across Elo, "
               "which it co-owns, Visa, Amex and Mastercard, with Mastercard in Black and the Amazon card.",
    "stats": [
        {"label": "Clients", "value": "74.3m"},
        {"label": "Loans", "value": "R$1.14tn"},
        {"label": "ROAE 2Q26", "value": "16.2%"},
        {"label": "Card spend 2025", "value": "R$360bn"},
    ],
    "page": "Bradesco_Platform.html",
    "notes": (
        ("Research notes", "Bradesco_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"], "bundles": ["issuer_toolkit"]},
        "mcblack": {"apis": ["benefits_eligibility", "priceless_cities", "enhanced_currency_conversion_calculator"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "principalcard": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "amazon": {"apis": ["automatic_billing_updater", "consumer_clarity"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "cielo": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "intlaccount": {"apis": ["enhanced_currency_conversion_calculator", "open_finance"], "use_cases": ["settle_in"]},
        # L3 Services
        "bia": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"], "bundles": ["merchant_resolution"]},
        "surpreenda": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "smes": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "digio": {"apis": ["bin_lookup", "transaction_notifications"], "use_cases": ["bin_lookup", "txnotify"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "pfm_stack", "issuer_toolkit"),
        "mcnow": ("loyalty_stack", "issuer_toolkit"),
        "credit": ("issuer_toolkit", "subscriptions"),
        "merch": ("acquirer_risk",),
    },
}
