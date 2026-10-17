"""Citizens (Citizens Financial Group).

The page (``Citizens_Platform.html``) reads Citizens as five discs,
Foundation to Access: the Consumer Bank, the Commercial Bank and the Private
Bank, a Mastercard lens that raises each area by how deep Mastercard goes in
it (Mastercard has been Citizens' only card network, and its contracted
services provider, since January 2023), and eleven journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``Citizens_research_notes.md``.

Built here like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``citizens_foundation.py``, ``citizens_inventory.py`` and
``citizens_story.py``. Edit those and rebuild::

    python customers/build_page.py citizens
"""

CUSTOMER = {
    "id": "citizens",
    "order": 30,
    "name": "Citizens",
    "short": "CFG",
    "brands": ["Citizens", "Citizens Private Bank", "Citizens Pay", "Citizens JMP"],
    "country": "United States",
    "region": "Americas",
    "type": "bank",
    "accent": "#008555",   # Citizens green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Citizens", "bg": "#ffffff", "source": "https://www.citizensbank.com/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A $234 billion regional bank as five discs, with Mastercard its only card network and "
               "contracted services provider since 2023, and a Private Bank built in three years.",
    "stats": [
        {"label": "Assets", "value": "$234bn"},
        {"label": "Branches", "value": "~1,000"},
        {"label": "Private Bank deposits", "value": "$18.5bn"},
        {"label": "Mastercard exclusive", "value": "since 2023"},
    ],
    "page": "Citizens_Platform.html",
    "notes": (
        ("Research notes", "Citizens_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "edge": {"apis": ["business_payment_controls", "enhanced_currency_conversion_calculator"],
                 "bundles": ["issuer_toolkit"]},
        "commcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "merchant": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"],
                     "bundles": ["acquirer_risk"]},
        "stablecoin": {"apis": ["enhanced_currency_conversion_calculator"]},
        # L3 Services
        "idfraud": {"use_cases": ["identity"]},
        "openapi": {"apis": ["open_finance"], "use_cases": ["enrichment", "identity"], "bundles": ["pfm_stack"]},
        "switchpay": {"apis": ["automatic_billing_updater", "open_finance"], "use_cases": ["recurring"],
                      "bundles": ["subscriptions"]},
        "cardrewards": {"apis": ["offers_for_publishers", "easy_savings"], "use_cases": ["findacard"],
                        "bundles": ["loyalty_stack"]},
        "priceless": {"apis": ["priceless_cities", "benefits_eligibility"], "use_cases": ["specials"]},
        "cashflow": {"apis": ["open_finance"], "use_cases": ["enrichment"]},
        # L4 Business lines
        "suite": {"apis": ["bin_lookup", "consumer_clarity"], "use_cases": ["bin_lookup", "consumer_clarity"],
                  "bundles": ["issuer_toolkit"]},
        "mortgage": {"apis": ["open_finance"]},
        "heloc": {"apis": ["open_finance"]},
        "student": {"apis": ["open_finance"]},
        # L5 Access
        "mobileapp": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"],
                      "bundles": ["pfm_stack"]},
        "contactcentre": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"],
                          "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "loyalty_stack", "merchant_resolution", "subscriptions"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("subscriptions", "pfm_stack"),
        "smallbiz": ("acquirer_risk",),
        "midcfo": ("issuer_toolkit",),
        "payco": ("pfm_stack",),
    },
}
