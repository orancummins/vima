"""ANZ Group Holdings Limited.

The page (``ANZ_Platform.html``) reads ANZ Group, with ANZ Plus, ANZ New
Zealand and Suncorp Bank, as five discs, Foundation to Access, with the
segments it reports (Australia Retail, Business & Private Bank,
Institutional, New Zealand, Suncorp Bank, Pacific & Group Centre), a
Mastercard lens (a Visa group where Mastercard is only accepted) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``ANZ_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``anz_inventory.py`` and ``anz_story.py``::

    python customers/build_page.py anz
"""

CUSTOMER = {
    "id": "anz",
    "order": 1590,
    "name": "ANZ",
    "short": "ANZ",
    "brands": ["ANZ", "ANZ Plus", "ANZ New Zealand", "Suncorp Bank", "ANZ Worldline", "ANZ Transactive"],
    "country": "Australia",
    "region": "Asia-Pacific",
    "type": "bank",
    "accent": "#007dba",   # ANZ blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "ANZ", "bg": "#ffffff",
         "source": "https://commons.wikimedia.org/wiki/File:ANZ-Logo-2009.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "ANZ Group as five discs: every ANZ, ANZ NZ and Suncorp Bank card on Visa, Suncorp Bank moving onto "
               "ANZ by June 2027, and ANZ Worldline, now wholly ANZ's, taking Mastercard at the till.",
    "stats": [
        {"label": "1H26 cash profit", "value": "A$3.78bn"},
        {"label": "Customers", "value": "11m+"},
        {"label": "Cash RoTE", "value": "11.6%"},
        {"label": "Suncorp customers", "value": "1.26m"},
    ],
    "page": "ANZ_Platform.html",
    "notes": (
        ("Research notes", "ANZ_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "plusdebit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "enrichment"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "commercial": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "worldline": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi", "bin_lookup"],
                      "bundles": ["acquirer_risk", "merchant_resolution"]},
        "npp": {"apis": ["open_finance"], "use_cases": ["identity", "recurring"], "bundles": ["subscriptions"]},
        "imt": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "security": {"apis": ["open_finance", "transaction_notifications"], "use_cases": ["identity", "txnotify"]},
        "scams": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials", "findacard"],
                    "bundles": ["loyalty_stack"]},
        "loop": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 / L5
        "accounts": {"apis": ["consumer_clarity", "easy_savings"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
        "bpb": {"apis": ["business_payment_controls", "places"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "loyalty_stack", "issuer_toolkit"),
        "mcnow": ("acquirer_risk", "merchant_resolution"),
        "everyday": ("pfm_stack",),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "card": ("loyalty_stack", "issuer_toolkit"),
    },
}
