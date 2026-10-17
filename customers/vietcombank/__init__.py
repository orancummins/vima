"""Vietcombank (Joint Stock Commercial Bank for Foreign Trade of Vietnam).

The page (``Vietcombank_Platform.html``) reads Vietnam's most profitable bank
as five discs, Foundation to Access, with its retail, wholesale and capital
markets businesses and its subsidiaries, a Mastercard lens (five card brands,
Visa first, NAPAS and VietQR at home) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is in
``Vietcombank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``vietcombank_inventory.py`` and ``vietcombank_story.py``::

    python customers/build_page.py vietcombank
"""

CUSTOMER = {
    "id": "vietcombank",
    "order": 800,
    "name": "Vietcombank",
    "short": "Vietcombank",
    "brands": ["Vietcombank", "VCB Digibank", "VCB DigiBiz", "VCBNeo", "VCBS", "Vietcombank Laos"],
    "country": "Vietnam",
    "region": "Asia-Pacific",
    "type": "bank",
    "accent": "#005028",   # Vietcombank green, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Vietcombank", "bg": "#ffffff",
         "source": "https://www.vietcombank.com.vn/-/media/Project/VCB-Sites/VCB/Home-page/VCB-Logo/Logo-VCB-no-60.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Vietnam's most profitable bank as five discs: a state-owned foreign-trade bank issuing five card brands, "
               "with Visa first, Mastercard on three cards and NAPAS and VietQR carrying everyday payments.",
    "stats": [
        {"label": "Total assets", "value": "VND 2,660tn"},
        {"label": "Pre-tax profit H1 2026", "value": "VND 29.2tn"},
        {"label": "Acceptance points", "value": "121k"},
        {"label": "Card brands issued", "value": "4 + NAPAS"},
    ],
    "page": "Vietcombank_Platform.html",
    "notes": (
        ("Research notes", "Vietcombank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mccredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "mcdebit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "wallets": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "ecom": {"apis": ["merchant_identifier"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
        "remit": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications"], "use_cases": ["identity", "txnotify"]},
        "offers": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials", "findacard"],
                   "bundles": ["loyalty_stack"]},
        "green": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        # L5 Access
        "digibank": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "digibiz": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "cashup": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "sustainability"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "everyday": ("pfm_stack",),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "travel": ("loyalty_stack",),
    },
}
