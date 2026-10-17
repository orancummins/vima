"""Attijariwafa bank SA.

The page (``Attijariwafa_Bank_Platform.html``) reads Morocco's largest bank as
five discs, Foundation to Access, with the segments it reports (banking in
Morocco, Europe and offshore; specialised financial subsidiaries; international
retail banking; insurance and real estate), a Mastercard lens (Visa's partner,
but its new neobank runs on Mastercard) and nine journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is in
``Attijariwafa_Bank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``attijariwafa_inventory.py`` and ``attijariwafa_story.py``::

    python customers/build_page.py attijariwafa
"""

CUSTOMER = {
    "id": "attijariwafa",
    "order": 1050,
    "name": "Attijariwafa Bank",
    "short": "Attijariwafa",
    "brands": ["Attijariwafa bank", "Simple", "Attijari Payment", "Wafacash", "Wafasalaf", "Wafa Assurance", "Bank Assafa", "CBAO"],
    "country": "Morocco",
    "region": "EEMEA",
    "accent": "#e05038",   # Attijariwafa red-orange, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Attijariwafa bank", "bg": "#ffffff",
         "source": "https://ir.attijariwafabank.com/sites/g/files/knoqqb15906/themes/site/nir_pid1467/client/images/ATTIJARIWAFA_LOGO_GROUPE_CMJN.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Morocco's largest bank as five discs: more than 12 million customers in 27 countries, a Visa core range "
               "and a 2024 Visa deal, and a new neobank, Simple, whose cards mostly run on Mastercard.",
    "stats": [
        {"label": "Customers", "value": "12m+"},
        {"label": "Assets", "value": "MAD 825bn"},
        {"label": "RoaTE H1 2026", "value": "22.9%"},
        {"label": "Countries", "value": "27"},
    ],
    "page": "Attijariwafa_Bank_Platform.html",
    "notes": (
        ("Research notes", "Attijariwafa_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "wafavisa": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"]},
        "awbblack": {"apis": ["benefits_eligibility", "priceless_cities", "enhanced_currency_conversion_calculator"],
                     "use_cases": ["findacard", "specials"], "bundles": ["loyalty_stack"]},
        "simplecards": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                        "bundles": ["issuer_toolkit"]},
        "virtual": {"apis": ["transaction_notifications", "automatic_billing_updater"], "use_cases": ["txnotify", "recurring"],
                    "bundles": ["subscriptions"]},
        "attpay": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "wafacash": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "match"], "use_cases": ["txnotify", "identity"]},
        "simpleai": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "deals": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "places"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "retail": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "cib": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "issuer_toolkit", "pfm_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "simple": ("pfm_stack", "loyalty_stack", "subscriptions"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "everyday": ("merchant_resolution",),
    },
}
