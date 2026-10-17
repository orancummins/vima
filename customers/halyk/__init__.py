"""JSC Halyk Bank of Kazakhstan.

The page (``Halyk_Bank_Platform.html``) reads Central Asia's largest bank as
five discs, Foundation to Access, with the segments it reports (retail,
corporate, SME, and insurance, international and other), a Mastercard lens
(Mastercard at the top, Visa underneath, QR everywhere) and ten journeys, two
of them for Mastercard. Public sources as at 17 October 2026; the research
behind it is in ``Halyk_Bank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``halyk_inventory.py`` and ``halyk_story.py``::

    python customers/build_page.py halyk
"""

CUSTOMER = {
    "id": "halyk",
    "order": 900,
    "name": "Halyk Bank",
    "short": "Halyk",
    "brands": ["Halyk Bank", "Halyk Super-App", "Onlinebank", "Halyk Market", "Halyk Life", "Tenge Bank"],
    "country": "Kazakhstan",
    "region": "EEMEA",
    "accent": "#068c6e",   # Halyk green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Halyk Bank", "bg": "#ffffff", "source": "https://halykbank.com/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Central Asia's largest bank as five discs: 11.5 million active clients, Mastercard World Elite at the "
               "top of a Visa-led card range, and most payments moving by Halyk QR and the national instant-payment system.",
    "stats": [
        {"label": "Active retail clients", "value": "11.5m"},
        {"label": "Assets", "value": "KZT 22trn"},
        {"label": "RoAE 1H 2026", "value": "24.8%"},
        {"label": "Super-App MAU", "value": "8.6m"},
    ],
    "page": "Halyk_Bank_Platform.html",
    "notes": (
        ("Research notes", "Halyk_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"]},
        "mcpremium": {"apis": ["benefits_eligibility", "priceless_cities", "enhanced_currency_conversion_calculator"],
                      "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "wallets": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "xborder": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "match"], "use_cases": ["txnotify", "identity"]},
        "baas": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "ai": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "loyalty": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "places"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "bizcards": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        "lifestyle": {"apis": ["offers_merchant_content", "places"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "acquirer_risk", "pfm_stack"),
        "mcnow": ("loyalty_stack", "issuer_toolkit"),
        "everyday": ("pfm_stack", "issuer_toolkit"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "sme": ("issuer_toolkit", "sustainability"),
    },
}
