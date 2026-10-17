"""Bank of China Limited (BOC), with BOC Hong Kong (Holdings).

The page (``Bank_of_China_Platform.html``) reads China's oldest and most
international bank as five discs, Foundation to Access, with the segments it
reports (Corporate banking, Personal banking, Treasury operations, Investment
banking and insurance), a Mastercard lens (Mastercard's first Chinese member,
now a small RMB lane in a UnionPay bank) and nine journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``Bank_of_China_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``bankofchina_inventory.py`` and ``bankofchina_story.py``::

    python customers/build_page.py bankofchina
"""

CUSTOMER = {
    "id": "bankofchina",
    "order": 1600,
    "name": "Bank of China",
    "short": "BOC",
    "brands": ["Bank of China", "Great Wall", "BOCHK", "BOC Credit Card (International)", "BoC Pay+", "BOCI", "BOC Life", "BOC Aviation"],
    "country": "China",
    "region": "Asia-Pacific",
    "type": "bank",
    "accent": "#b10a32",   # BOC red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Bank of China", "bg": "#ffffff", "source": "https://en.wikipedia.org/wiki/File:Bank_of_China.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "China's oldest bank as five discs: 900 million cards issued, mostly on UnionPay, the leading acquirer of "
               "visitors' foreign cards, and Great Wall Mastercard RMB cards since 2024 from Mastercard's first Chinese member.",
    "stats": [
        {"label": "Assets", "value": "RMB40.2trn"},
        {"label": "Personal customers", "value": "554m"},
        {"label": "Credit cards issued", "value": "152m"},
        {"label": "Mobile MAUs", "value": "105m"},
    ],
    "page": "Bank_of_China_Platform.html",
    "notes": (
        ("Research notes", "Bank_of_China_research_notes.md"),
    ),
    "studio": {
        # L1 Foundation
        "ai": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        # L2 Rails
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "transaction_notifications"], "use_cases": ["consumer_clarity", "txnotify"],
                   "bundles": ["issuer_toolkit"]},
        "gwmc": {"apis": ["enhanced_currency_conversion_calculator", "bin_lookup", "benefits_eligibility"], "use_cases": ["bin_lookup", "findacard"],
                 "bundles": ["issuer_toolkit"]},
        "mcdual": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["txnotify"]},
        "xborder": {"apis": ["priceless_cities", "enhanced_currency_conversion_calculator", "benefits_eligibility", "places"],
                    "use_cases": ["places", "specials"], "bundles": ["loyalty_stack"]},
        "foreigncard": {"apis": ["merchant_identifier", "match", "places"], "use_cases": ["psi", "settle_in"],
                        "bundles": ["acquirer_risk", "merchant_resolution"]},
        "chill": {"apis": ["offers_for_publishers", "consumer_clarity", "carbon_calculator"], "use_cases": ["specials", "pfm"],
                  "bundles": ["loyalty_stack", "sustainability"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "merchant_identifier"], "use_cases": ["txnotify", "identity"]},
        "benefits": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "corporate": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "bochk": {"apis": ["bin_lookup", "automatic_billing_updater", "consumer_clarity"], "use_cases": ["recurring", "consumer_clarity"],
                  "bundles": ["issuer_toolkit", "subscriptions"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "loyalty_stack", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "merchant_resolution"),
        "travel": ("loyalty_stack",),
        "visit": ("merchant_resolution", "acquirer_risk"),
        "hk": ("issuer_toolkit", "subscriptions"),
    },
}
