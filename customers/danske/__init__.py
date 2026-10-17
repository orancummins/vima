"""Danske Bank A/S.

The page (``Danske_Bank_Platform.html``) reads Denmark's largest bank as five
discs, Foundation to Access, with the segments it reports (Personal Customers,
Business Customers, Large Corporates & Institutions, Danica, Northern Ireland),
a Mastercard lens (a Mastercard bank with one Visa/Dankort card left) and nine
journeys, two of them for Mastercard. Public sources as at 17 October 2026; the
research behind it is in ``Danske_Bank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``danske_inventory.py`` and ``danske_story.py``::

    python customers/build_page.py danske
"""

CUSTOMER = {
    "id": "danske",
    "order": 520,
    "name": "Danske Bank",
    "short": "Danske Bank",
    "brands": ["Danske Bank", "Realkredit Danmark", "Danica", "Danske Invest", "Nordania", "MobilePay (associate)"],
    "country": "Denmark",
    "region": "Europe",
    "type": "bank",
    "accent": "#002346",   # Danske Bank navy, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Danske Bank", "bg": "#ffffff",
         "source": "https://danskebank.dk/-/media/danske-bank-images/logo/danske-bank-logo-svg.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Denmark's largest bank as five discs: Mastercard on almost every card it issues, Visa only on the "
               "co-badged Visa/Dankort, and Denmark's first agent payment made with Mastercard.",
    "stats": [
        {"label": "Loans", "value": "DKK 1,794bn"},
        {"label": "Net profit H1 2026", "value": "DKK 11.9bn"},
        {"label": "ROE H1 2026", "value": "13.9%"},
        {"label": "Staff (FTE)", "value": "19,472"},
    ],
    "page": "Danske_Bank_Platform.html",
    "notes": (
        ("Research notes", "Danske_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "hverdag": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "visadankort": {"apis": ["bin_lookup"], "use_cases": ["bin_lookup"], "bundles": ["issuer_toolkit"]},
        "dkcredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit", "subscriptions"]},
        "ficards": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["txnotify"]},
        "corpcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "gdr": {"apis": ["merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
        # L3 Services
        "agentpay": {"apis": ["merchant_identifier"], "use_cases": ["identity"]},
        "cashback": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "priceless": {"apis": ["priceless_cities", "places"], "use_cases": ["places"]},
        "aiia": {"apis": ["open_finance_eu"], "use_cases": ["identity"], "bundles": ["pfm_stack"]},
        "assistant": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "nordania": {"apis": ["carbon_calculator", "business_payment_controls"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "pfm_stack", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack",),
        "card": ("loyalty_stack", "subscriptions"),
        "sme": ("sustainability", "issuer_toolkit"),
    },
}
