"""CRDB Bank Plc.

The page (``CRDB_Bank_Platform.html``) reads Tanzania's largest bank as five
discs, Foundation to Access, with the segments it reports (Corporate Banking,
Retail Banking, Treasury, and Insurance), a Mastercard lens (a Visa debit bank
where Mastercard keeps a small credit book and mobile money moves the money)
and ten journeys, two of them for Mastercard. Public sources as at 17 October
2026; the research behind it is in ``CRDB_Bank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``crdb_inventory.py``
and ``crdb_story.py``::

    python customers/build_page.py crdb
"""

CUSTOMER = {
    "id": "crdb",
    "order": 1120,
    "name": "CRDB Bank",
    "short": "CRDB",
    "brands": ["CRDB Bank", "TemboCard", "SimBanking", "CRDB Wakala", "Lipa Hapa", "Al Barakah Banking",
               "CRDB Bank Burundi", "CRDB Bank Congo", "CRDB Insurance"],
    "country": "Tanzania",
    "region": "EEMEA",
    "accent": "#43b02a",   # CRDB green, from the logo on crdbbank.co.tz
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "CRDB Bank", "bg": "#ffffff",
         "source": "https://crdbbank.co.tz/storage/app/media/images/logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Tanzania's largest bank as five discs: TemboCard debit on Visa in Tanzania, Burundi and the DRC, "
               "a small credit book on Mastercard, acquiring for every network, and TanQR, TIPS and mobile money moving most of the money.",
    "stats": [
        {"label": "Customers", "value": "7.95m"},
        {"label": "Assets", "value": "TZS 26.4tn"},
        {"label": "Profit 1H 2026", "value": "TZS 417bn"},
        {"label": "Registered cards", "value": "8.9m"},
    ],
    "page": "CRDB_Bank_Platform.html",
    "notes": (
        ("Research notes", "CRDB_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mccredit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                     "bundles": ["issuer_toolkit"]},
        "tembovisa": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "consumer_clarity"]},
        "pos": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "gateway": {"apis": ["match", "merchant_identifier", "bin_lookup"], "use_cases": ["psi", "bin_lookup", "recurring"],
                    "bundles": ["acquirer_risk", "subscriptions"]},
        "tanqr": {"apis": ["merchant_identifier", "places"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
        "remit": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "forexatm": {"apis": ["enhanced_currency_conversion_calculator", "places"], "use_cases": ["places"]},
        # L3 Services
        "fraud": {"apis": ["transaction_notifications", "merchant_identifier"], "use_cases": ["txnotify", "enrichment"],
                  "bundles": ["merchant_resolution"]},
        "tembopoints": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"],
                        "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "msme": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "agri": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        # L5 Access
        "simbanking": {"apis": ["transaction_notifications", "consumer_clarity", "open_finance"], "use_cases": ["pfm", "enrichment", "identity"],
                       "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "merchant_resolution"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "farmer": ("sustainability",),
    },
}
