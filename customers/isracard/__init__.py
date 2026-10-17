"""Isracard Ltd.

The page (``Isracard_Platform.html``) reads Israel's largest card group as five
discs, Foundation to Access, with the segments it reports (private customers,
business customers), a Mastercard lens (the brand on most of its own cards,
with American Express in the same house) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``Isracard_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``isracard_inventory.py`` and ``isracard_story.py``::

    python customers/build_page.py isracard
"""

CUSTOMER = {
    "id": "isracard",
    "order": 960,
    "name": "Isracard",
    "short": "Isracard",
    "brands": ["Isracard", "American Express Israel", "FLY CARD", "LifeStyle", "Superfly", "Isracard Finance"],
    "country": "Israel",
    "region": "EEMEA",
    "accent": "#101820",   # Isracard ink, from the logo and the website's theme (the 2023 logo is monochrome)
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Isracard", "bg": "#ffffff", "source": "https://www.isracard.co.il/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Israel's largest card group as five discs: Mastercard on most of its own and co-brand cards, El Al's "
               "FLY CARD won in 2026, and an exclusive American Express licence under Delek's control.",
    "stats": [
        {"label": "Active cards", "value": "4.8m"},
        {"label": "Credit Q2 2026", "value": "NIS 13.1bn"},
        {"label": "Businesses", "value": "100k+"},
        {"label": "FLY CARD members", "value": "3.6m"},
    ],
    "page": "Isracard_Platform.html",
    "notes": (
        ("Research notes", "Isracard_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "top": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                "bundles": ["issuer_toolkit"]},
        "cashback": {"apis": ["benefits_eligibility", "offers_for_publishers"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "flycard": {"apis": ["automatic_billing_updater", "enhanced_currency_conversion_calculator", "priceless_cities"],
                    "use_cases": ["recurring", "settle_in"], "bundles": ["subscriptions", "loyalty_stack"]},
        "prepaid": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "wallets": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring", "bin_lookup"], "bundles": ["subscriptions"]},
        "agentpay": {"apis": ["merchant_identifier", "transaction_notifications"], "use_cases": ["identity", "txnotify"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"], "bundles": ["merchant_resolution"]},
        "clubs": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "b2b": {"apis": ["business_payment_controls", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "lifestyle": {"apis": ["offers_merchant_content", "places"], "use_cases": ["places", "specials"], "bundles": ["loyalty_stack"]},
        "bizaccount": {"apis": ["merchant_identifier", "places"], "use_cases": ["places", "psi"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("subscriptions", "loyalty_stack", "acquirer_risk"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "fly": ("loyalty_stack", "subscriptions"),
        "everyday": ("issuer_toolkit", "merchant_resolution"),
        "sme": ("acquirer_risk", "merchant_resolution"),
    },
}
