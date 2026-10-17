"""Banque de Développement Local (BDL).

The page (``Banque_de_Developpement_Local_BDL_Platform.html``) reads an Algerian
public bank, listed since March 2025, as five discs, Foundation to Access, with
the segments it reports (households, private sector, public sector, and
treasury and central items), a Mastercard lens (Mastercard's sponsor bank in a
country that pays by CIB) and ten journeys, two of them for Mastercard. Public
sources, mostly French, as at 17 October 2026; the research behind it is in
``Banque_de_Developpement_Local_BDL_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``bdl_inventory.py`` and ``bdl_story.py``::

    python customers/build_page.py bdl
"""

CUSTOMER = {
    "id": "bdl",
    "order": 1060,
    "name": "Banque de Développement Local (BDL)",
    "short": "BDL",
    "brands": ["BDL", "BDL Finance Islamique", "DigitBDL", "WIMPAY BDL"],
    "country": "Algeria",
    "region": "EEMEA",
    "accent": "#711e80",   # BDL purple, from the logo and the site's CSS
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Banque de Développement Local", "bg": "#ffffff",
         "source": "https://www.bdl.dz/wp-content/uploads/2022/12/logo-1.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "An Algerian public bank as five discs: listed in 2025, everyday cards and 17,000 terminals on the "
               "domestic CIB scheme, and Mastercard on its international cards, cross-border acquiring and SATIM's "
               "local processing.",
    "stats": [
        {"label": "Assets", "value": "DA 2.4trn"},
        {"label": "Profit H1 2026", "value": "DA 22.3bn"},
        {"label": "Terminals", "value": "17,246"},
        {"label": "DigitBDL subscribers", "value": "153k"},
    ],
    "page": "Banque_de_Developpement_Local_BDL_Platform.html",
    "notes": (
        ("Research notes", "Banque_de_Developpement_Local_BDL_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mastercard": {"apis": ["bin_lookup", "consumer_clarity", "enhanced_currency_conversion_calculator", "transaction_notifications"],
                       "use_cases": ["txnotify", "consumer_clarity"], "bundles": ["issuer_toolkit"]},
        "allowance": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility"], "use_cases": ["findacard"]},
        "corpcard": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "tpe": {"apis": ["merchant_identifier", "places"], "use_cases": ["places"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "webmarchand": {"apis": ["match", "merchant_identifier"], "bundles": ["acquirer_risk"]},
        "ecomint": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi", "bin_lookup"], "bundles": ["acquirer_risk"]},
        "cnas": {"apis": ["bin_lookup"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "wimpay": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment"]},
        "satim": {"apis": ["bin_lookup"], "use_cases": ["bin_lookup"]},
        # L3 Services
        "secure": {"apis": ["transaction_notifications"], "use_cases": ["identity", "txnotify"]},
        # L5 Access
        "digit": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["pfm", "txnotify"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "export": ("acquirer_risk", "merchant_resolution"),
        "travel": ("issuer_toolkit",),
        "everyday": ("pfm_stack",),
    },
}
