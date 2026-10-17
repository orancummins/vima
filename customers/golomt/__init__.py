"""Golomt Bank JSC.

The page (``Golomt_Bank_Platform.html``) reads Mongolia's second-largest bank
as five discs, Foundation to Access, with its corporate, SME, retail and
treasury and international business, a Mastercard lens (a four-scheme bank
where Mastercard leads on phones and metal) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is in
``Golomt_Bank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``golomt_inventory.py`` and ``golomt_story.py``::

    python customers/build_page.py golomt
"""

CUSTOMER = {
    "id": "golomt",
    "order": 890,
    "name": "Golomt Bank",
    "short": "Golomt",
    "brands": ["Golomt Bank", "SocialPay", "Universe cards", "Premiere Banking", "Golomt Financial Group"],
    "country": "Mongolia",
    "region": "Asia-Pacific",
    "accent": "#0061b3",   # Golomt blue, from the logo on golomtbank.com
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Golomt Bank", "bg": "#ffffff", "source": "https://www.golomtbank.com/en"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Mongolia's second-largest bank as five discs: a third of Mongolians as customers, cards on four schemes "
               "and the national ₮ Card, with Mastercard at the top of the range and first on Apple Pay and Google Pay.",
    "stats": [
        {"label": "Customers", "value": "1.3m"},
        {"label": "Assets H1 2026", "value": "MNT 19.9tn"},
        {"label": "ROE 2025", "value": "23.8%"},
        {"label": "Card-loan share", "value": "39%"},
    ],
    "page": "Golomt_Bank_Platform.html",
    "notes": (
        ("Research notes", "Golomt_Bank_research_notes.md"),
    ),
    "studio": {
        # L1 Foundation
        "green": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "goldmc": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "worldmc": {"apis": ["benefits_eligibility", "priceless_cities", "enhanced_currency_conversion_calculator"], "use_cases": ["specials"],
                    "bundles": ["loyalty_stack"]},
        "socialpay": {"apis": ["consumer_clarity", "places"], "use_cases": ["enrichment", "places"], "bundles": ["pfm_stack"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "swift": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "aiassist": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "loyalty": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "gateway": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "loyalty_stack", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "loyalty_stack"),
        "corp": ("issuer_toolkit",),
    },
}
