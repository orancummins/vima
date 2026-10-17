"""BIAT (Banque Internationale Arabe de Tunisie).

The page (``BIAT_Platform.html``) reads Tunisia's largest bank by deposits and income
as five discs, Foundation to Access, with the businesses it describes (retail, corporate,
financing and investment banking, markets), a Mastercard lens (a Visa-first bank where
Mastercard carries the travel and business cards) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026, mostly French; the research behind it
is in ``BIAT_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the template and swaps in
the data from ``page_data.py``, ``biat_inventory.py`` and ``biat_story.py``::

    python customers/build_page.py biat
"""

CUSTOMER = {
    "id": "biat",
    "order": 1070,
    "name": "BIAT",
    "short": "BIAT",
    "brands": ["BIAT", "MyBIAT", "BIAT France", "Assurances BIAT", "Tunisie Valeurs", "BIAT Privilèges"],
    "country": "Tunisia",
    "region": "EEMEA",
    "accent": "#204070",   # BIAT navy, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "BIAT, Banque Internationale Arabe de Tunisie", "bg": "#ffffff",
         "source": "https://www.biat.com.tn/sites/default/files/logobiat_0_0.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Tunisia's largest bank as five discs: first in deposits and income, Visa at the top of the card range, "
               "and Mastercard in the travel-allowance, business and Platinum cards.",
    "stats": [
        {"label": "Deposits H1 2026", "value": "TND 23.0bn"},
        {"label": "Net profit 2025", "value": "TND 385m"},
        {"label": "Customers", "value": "950k"},
        {"label": "Branches", "value": "206"},
    ],
    "page": "BIAT_Platform.html",
    "notes": (
        ("Research notes", "BIAT_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "classic": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "platinum": {"apis": ["benefits_eligibility", "priceless_cities", "consumer_clarity"], "use_cases": ["findacard", "consumer_clarity"],
                     "bundles": ["issuer_toolkit", "loyalty_stack"]},
        "flexy": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["consumer_clarity", "txnotify"], "bundles": ["issuer_toolkit"]},
        "travel": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility", "priceless_cities"], "use_cases": ["settle_in", "findacard"],
                   "bundles": ["loyalty_stack"]},
        "business": {"apis": ["business_payment_controls", "transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "tpe": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "ecom": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi", "bin_lookup"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "biatfrance": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "privileges": {"apis": ["offers_for_publishers", "offers_merchant_content", "places"], "use_cases": ["specials", "places"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "overt": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        # L5 Access
        "mybiat": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "acquirer_risk"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "affluent": ("loyalty_stack",),
        "everyday": ("pfm_stack", "issuer_toolkit"),
    },
}
