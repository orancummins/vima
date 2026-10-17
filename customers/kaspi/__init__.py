"""Kaspi.kz.

The page (``Kaspi_kz_Platform.html``) reads Kazakhstan's payments, marketplace
and fintech super-app as five discs, Foundation to Access, with the platforms
it reports (Payments, Marketplace, Fintech), a Mastercard lens (a closed loop
with a Visa card, and Mastercard only at the edges) and nine journeys, two of
them for Mastercard. Public sources as at 17 October 2026; the research
behind it is in ``Kaspi_kz_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``kaspi_inventory.py`` and ``kaspi_story.py``::

    python customers/build_page.py kaspi
"""

CUSTOMER = {
    "id": "kaspi",
    "order": 1640,
    "name": "Kaspi.kz",
    "short": "Kaspi.kz",
    "brands": ["Kaspi.kz", "Kaspi Gold", "Kaspi QR", "Kaspi Pay", "Kaspi Red", "Hepsiburada", "Hepsi Bank"],
    "country": "Kazakhstan",
    "region": "EEMEA",
    "type": "wallet",
    "accent": "#f14635",   # Kaspi red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Kaspi.kz", "bg": "#ffffff", "source": "https://kaspi.kz/img/Logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Kazakhstan's super-app as five discs: KZT44 trillion of payments a year, most of it on its own Kaspi QR "
               "network, a Kaspi Gold card on Visa, and Mastercard only in acceptance and transfers, with Hepsi Bank "
               "in Türkiye still to choose.",
    "stats": [
        {"label": "Revenue 2025", "value": "$8.0bn"},
        {"label": "TPV Q2 2026", "value": "$26.3bn"},
        {"label": "Monthly users", "value": "15.7m"},
        {"label": "Active merchants", "value": "764k"},
    ],
    "page": "Kaspi_kz_Platform.html",
    "notes": (
        ("Research notes", "Kaspi_kz_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "gold": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"],
                 "bundles": ["issuer_toolkit"]},
        "kaspiqr": {"apis": ["merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
        "pos": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi", "bin_lookup"], "bundles": ["acquirer_risk"]},
        "magazincards": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "intl": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "b2b": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "kaspiid": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "kasper": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["merchant_resolution"]},
        "cashback": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "bonus": {"apis": ["offers_for_publishers"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "travel": {"apis": ["places", "priceless_cities"], "use_cases": ["places"]},
        "hepsibank": {"apis": ["bin_lookup", "consumer_clarity", "transaction_notifications"], "use_cases": ["txnotify"],
                      "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "merchant_resolution", "acquirer_risk"),
        "mcnow": ("acquirer_risk", "subscriptions"),
        "accept": ("acquirer_risk", "merchant_resolution"),
        "grow": ("loyalty_stack",),
        "everyday": ("issuer_toolkit", "loyalty_stack"),
    },
}
