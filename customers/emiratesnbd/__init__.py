"""Emirates NBD Bank (P.J.S.C.).

The page (``Emirates_NBD_Platform.html``) reads Dubai's biggest bank as five
discs, Foundation to Access, with the segments it reports (Retail Banking &
Wealth Management, Corporate & Institutional Banking, Global Markets &
Treasury, Islamic Banking, International), a Mastercard lens (a Visa bank that
runs its travel cards and gateway on Mastercard) and ten journeys, two of them
for Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``Emirates_NBD_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``emiratesnbd_inventory.py`` and ``emiratesnbd_story.py``::

    python customers/build_page.py emiratesnbd
"""

CUSTOMER = {
    "id": "emiratesnbd",
    "order": 940,
    "name": "Emirates NBD",
    "short": "Emirates NBD",
    "brands": ["Emirates NBD", "Emirates Islamic", "Liv", "DenizBank", "RBL Bank", "Emirates NBD Capital"],
    "country": "United Arab Emirates",
    "region": "EEMEA",
    "accent": "#072447",   # Emirates NBD navy, from the website
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Emirates NBD", "bg": "#072447",
         "source": "https://www.emiratesnbd.com/-/media/enbd/images/logos/horizontal_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Dubai's biggest bank as five discs: AED 1.3 trillion, a third of UAE card spend, Visa debit and co-brands, "
               "and Mastercard for its travel cards and merchant gateway.",
    "stats": [
        {"label": "Total assets", "value": "AED 1.3tn"},
        {"label": "H1 2026 pre-tax profit", "value": "AED 16.2bn"},
        {"label": "UAE card spend share", "value": "36%"},
        {"label": "Staff", "value": "30,000+"},
    ],
    "page": "Emirates_NBD_Platform.html",
    "notes": (
        ("Research notes", "Emirates_NBD_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "mccc": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                 "bundles": ["issuer_toolkit"]},
        "voyager": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility", "priceless_cities"],
                    "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "globalcash": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "corpcards": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        "enbdpay": {"apis": ["match", "merchant_identifier"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "aani": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "aitravel": {"apis": ["places", "offers_for_publishers"], "use_cases": ["places", "specials"], "bundles": ["loyalty_stack"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "carbon": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        # L5 Access
        "liv": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack", "subscriptions"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "issuer_toolkit", "sustainability"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "travel": ("loyalty_stack",),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "digital": ("pfm_stack", "subscriptions"),
    },
}
