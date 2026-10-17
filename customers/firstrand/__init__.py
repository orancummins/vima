"""FirstRand Limited (FNB, RMB, WesBank).

The page (``FirstRand_FNB_Platform.html``) reads South Africa's FirstRand
group as five discs, Foundation to Access, with the franchises it reports
(FNB, RMB, WesBank, the Centre and the UK operations now held for sale), a
Mastercard lens (a Visa bank that sends money abroad on Mastercard) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``FirstRand_FNB_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``firstrand_inventory.py`` and ``firstrand_story.py``::

    python customers/build_page.py firstrand
"""

CUSTOMER = {
    "id": "firstrand",
    "order": 1630,
    "name": "FirstRand (FNB)",
    "short": "FNB",
    "brands": ["FNB", "RMB", "WesBank", "eBucks", "FNB Connect", "nav»", "Ashburton", "Aldermore"],
    "country": "South Africa",
    "region": "EEMEA",
    "type": "bank",
    "accent": "#00a9ac",   # FNB turquoise, from the logo on fnb.co.za
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "FNB", "bg": "#ffffff",
         "source": "https://www.fnb.co.za/_assets/images/generic/skins/00/navigation/secondary-logo/header-logo_lrg.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "FirstRand as five discs: 12.8 million FNB customers on Visa cards, PayShap as the default instant payment, "
               "and Globba sending money abroad on Mastercard Move.",
    "stats": [
        {"label": "FNB active customers", "value": "12.8m"},
        {"label": "Continuing earnings FY26", "value": "R44.5bn"},
        {"label": "Continuing ROE", "value": "24.9%"},
        {"label": "Card transactions", "value": "1.39bn"},
    ],
    "page": "FirstRand_FNB_Platform.html",
    "notes": (
        ("Research notes", "FirstRand_FNB_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "cards": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                  "bundles": ["issuer_toolkit"]},
        "virtual": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "enrichment"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "speedee": {"apis": ["merchant_identifier", "places"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
        "globba": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "payshap": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "fleet": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "navi": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "ebucks": {"apis": ["offers_for_publishers", "offers_merchant_content", "easy_savings"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "commercial": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit", "subscriptions"]},
        "rmb": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "loyalty_stack", "pfm_stack"),
        "mcnow": ("merchant_resolution", "acquirer_risk"),
        "everyday": ("pfm_stack", "loyalty_stack"),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "drive": ("sustainability",),
    },
}
