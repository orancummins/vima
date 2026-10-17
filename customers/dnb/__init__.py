"""DNB Bank ASA.

The page (``DNB_Platform.html``) reads Norway's largest bank as five discs,
Foundation to Access, with the segments it reports (Personal customers,
Corporate customers Norway, Large corporates & international, Other
operations), a Mastercard lens (Mastercard on credit, Visa and BankAxept on
debit) and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in ``DNB_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``dnb_inventory.py``
and ``dnb_story.py``::

    python customers/build_page.py dnb
"""

CUSTOMER = {
    "id": "dnb",
    "order": 510,
    "name": "DNB",
    "short": "DNB",
    "brands": ["DNB", "Sbanken", "DNB Carnegie", "DNB Eiendom", "DNB Finans", "DNB Livsforsikring"],
    "country": "Norway",
    "region": "Europe",
    "accent": "#007272",   # DNB sea green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "DNB", "bg": "#ffffff", "source": "https://www.dnb.no/en"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Norway's largest bank as five discs: 2.4 million personal customers on BankAxept and Visa debit, "
               "a credit range that is all Mastercard, and a big stake in Vipps MobilePay.",
    "stats": [
        {"label": "Personal customers", "value": "2.4m"},
        {"label": "Loans", "value": "NOK 2.3trn"},
        {"label": "ROE Q2 2026", "value": "14.6%"},
        {"label": "Fraud stopped 2025", "value": "NOK 3bn"},
    ],
    "page": "DNB_Platform.html",
    "notes": (
        ("Research notes", "DNB_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "mccredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "pbcard": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "corpmc": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "wallets": {"apis": ["enhanced_currency_conversion_calculator", "merchant_identifier"], "use_cases": ["enrichment"]},
        "two": {"apis": ["business_payment_controls", "open_finance_eu"], "use_cases": ["identity"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "apis": {"apis": ["open_finance_eu"], "use_cases": ["identity", "pfm"], "bundles": ["pfm_stack"]},
        "circlek": {"apis": ["offers_for_publishers", "offers_merchant_content", "carbon_calculator"], "use_cases": ["specials"],
                    "bundles": ["loyalty_stack", "sustainability"]},
        "priceless": {"apis": ["priceless_cities", "places"], "use_cases": ["places"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "packages": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack", "merchant_resolution"]},
        "lci": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "pfm_stack", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "credit": ("issuer_toolkit", "loyalty_stack", "sustainability"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("issuer_toolkit",),
    },
}
