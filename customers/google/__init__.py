"""Google (Alphabet Inc.), as a payments player.

The page (``Google_Platform.html``) reads Google through payments, as five
discs, Foundation to Access, with the segments Alphabet reports (Google
Services, Google Cloud), a Mastercard lens (in every wallet and every
protocol, but Visa gets the exclusives) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``Google_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``google_inventory.py`` and ``google_story.py``::

    python customers/build_page.py google
"""

CUSTOMER = {
    "id": "google",
    "order": 1290,
    "name": "Google",
    "short": "Google",
    "brands": ["Google Pay", "Google Wallet", "Flex by Google Pay", "Chrome", "Gemini", "Google Cloud", "Google Play"],
    "country": "United States",
    "region": "Global",
    "type": "tech",
    "accent": "#4285f4",   # Google blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Google", "bg": "#ffffff", "source": "https://commons.wikimedia.org/wiki/File:Google_2015_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Google's payments as five discs: Mastercard tokenised in every wallet and a partner in AP2 and UCP, "
               "but Visa carries Google Pay's BNPL and Europe's new authentication, and RuPay its own card in India.",
    "stats": [
        {"label": "Revenue 2025", "value": "$403bn"},
        {"label": "Q2 2026 revenue", "value": "$119.8bn"},
        {"label": "UPI share", "value": "32.7%"},
        {"label": "Gemini app users", "value": "950m"},
    ],
    "page": "Google_Platform.html",
    "notes": (
        ("Research notes", "Google_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "gpay": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["psi", "bin_lookup"], "bundles": ["merchant_resolution"]},
        "tokens": {"apis": ["automatic_billing_updater", "transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "bnpl": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["issuer_toolkit"]},
        "billing": {"apis": ["automatic_billing_updater", "bin_lookup", "match"], "use_cases": ["recurring"], "bundles": ["subscriptions", "acquirer_risk"]},
        "ap2": {"apis": ["merchant_identifier", "consumer_clarity"], "use_cases": ["identity", "enrichment"], "bundles": ["merchant_resolution"]},
        # L3 Services
        "spa": {"apis": ["bin_lookup"], "use_cases": ["identity"], "bundles": ["acquirer_risk"]},
        "benefits": {"apis": ["benefits_eligibility", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "passes": {"apis": ["offers_for_publishers", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "ucart": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
        "idpass": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L4 Business lines
        "play": {"apis": ["automatic_billing_updater", "match"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "flex": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("merchant_resolution", "loyalty_stack", "acquirer_risk"),
        "mcnow": ("issuer_toolkit", "merchant_resolution"),
        "online": ("merchant_resolution", "acquirer_risk"),
        "issuer": ("issuer_toolkit", "loyalty_stack"),
        "biz": ("subscriptions", "acquirer_risk"),
    },
}
