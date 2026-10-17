"""Krungsri (Bank of Ayudhya PCL).

The page (``Krungsri_Platform.html``) reads Thailand's largest card issuer as
five discs, Foundation to Access, with the loan segments it reports (Retail &
Consumer, Corporate, SME, ASEAN), a Mastercard lens (a Visa-led card book with
Central The 1 on Mastercard) and ten journeys, two of them for Mastercard.
Public sources as at 17 October 2026; the research behind it is in
``Krungsri_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``krungsri_inventory.py`` and ``krungsri_story.py``::

    python customers/build_page.py krungsri
"""

CUSTOMER = {
    "id": "krungsri",
    "order": 790,
    "name": "Krungsri",
    "short": "Krungsri",
    "brands": ["Krungsri", "Krungsri Consumer", "Central The 1", "First Choice", "Lotus's Money", "Krungsri Auto", "Ngern Tid Lor"],
    "country": "Thailand",
    "region": "Asia-Pacific",
    "accent": "#ffd400",   # Krungsri yellow, from the logo's symbol
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Krungsri", "bg": "#6f5f5e",
         "source": "https://commons.wikimedia.org/wiki/File:Krungsri_Logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Thailand's largest card issuer as five discs: MUFG-owned, number one in cards, car loans and personal loans, "
               "with a Visa-led card book and Central The 1 on Mastercard.",
    "stats": [
        {"label": "Loans", "value": "฿1.94trn"},
        {"label": "Card share", "value": "15%"},
        {"label": "Card customers", "value": "2.4m"},
        {"label": "Central The 1 cards", "value": "960k"},
    ],
    "page": "Krungsri_Platform.html",
    "notes": (
        ("Research notes", "Krungsri_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "kccards": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                    "bundles": ["issuer_toolkit"]},
        "central": {"apis": ["offers_for_publishers", "offers_merchant_content", "consumer_clarity"], "use_cases": ["specials", "enrichment"],
                    "bundles": ["loyalty_stack"]},
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "boarding": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "edc": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "promptpay": {"apis": ["open_finance"], "use_cases": ["identity"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "ai": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "mcperks": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "sme": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "ploan": {"apis": ["consumer_clarity"], "use_cases": ["pfm"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "pfm_stack", "loyalty_stack"),
        "mcnow": ("loyalty_stack", "acquirer_risk"),
        "shop": ("loyalty_stack", "merchant_resolution"),
        "sme": ("acquirer_risk",),
        "travel": ("loyalty_stack",),
    },
}
