"""Canadian Imperial Bank of Commerce (CIBC).

The page (``CIBC_Platform.html``) reads Canada's Big Six bank CIBC as five
discs, Foundation to Access, with the segments it reports (Canadian Personal
and Business Banking, Canadian Commercial Banking and Wealth Management, U.S.
Commercial Banking and Wealth Management, Capital Markets, Corporate and
Other), a Mastercard lens (a Visa bank with the Costco and Adapta cards on
Mastercard) and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in ``CIBC_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``cibc_inventory.py``
and ``cibc_story.py``::

    python customers/build_page.py cibc
"""

CUSTOMER = {
    "id": "cibc",
    "order": 1210,
    "name": "CIBC",
    "short": "CIBC",
    "brands": ["CIBC", "Simplii Financial", "CIBC Bank USA", "CIBC Wood Gundy", "CIBC Investor's Edge",
               "CIBC Capital Markets", "CIBC Caribbean"],
    "country": "Canada",
    "region": "Americas",
    "type": "bank",
    "accent": "#c41f3e",   # CIBC red, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "CIBC", "bg": "#ffffff",
         "source": "https://www.cibc.com/content/dam/global-assets/logos/cibc-logos/no-tagline/cibc-logo-colour-142x36.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Canada's Big Six bank CIBC as five discs: own-brand credit and debit on Visa and Interac, the Costco and "
               "Adapta cards and Simplii debit on Mastercard, and Click to Pay on every credit card from 21 October 2026.",
    "stats": [
        {"label": "Assets", "value": "C$1.18tn"},
        {"label": "Clients", "value": "15m"},
        {"label": "Adj. ROE Q3 2026", "value": "16.8%"},
        {"label": "Card loans", "value": "C$21.6bn"},
    ],
    "page": "CIBC_Platform.html",
    "notes": (
        ("Research notes", "CIBC_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "costco": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "adapta": {"apis": ["merchant_identifier", "consumer_clarity", "places"], "use_cases": ["enrichment", "places"], "bundles": ["pfm_stack"]},
        "costcobiz": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["issuer_toolkit", "sustainability"]},
        "simpliidebit": {"apis": ["transaction_notifications", "enhanced_currency_conversion_calculator"], "use_cases": ["txnotify"]},
        "usdebit": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"]},
        "gmt": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "globalpay": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        # L3 Services
        "offers": {"apis": ["offers_for_publishers", "offers_merchant_content", "priceless_cities"], "use_cases": ["specials", "findacard"],
                   "bundles": ["loyalty_stack"]},
        "clicktopay": {"apis": ["bin_lookup", "automatic_billing_updater"], "use_cases": ["bin_lookup", "recurring"], "bundles": ["subscriptions"]},
        "fraud": {"apis": ["consumer_clarity", "merchant_identifier", "transaction_notifications"], "use_cases": ["consumer_clarity", "txnotify"],
                  "bundles": ["merchant_resolution"]},
        "crtex": {"apis": ["consumer_clarity", "easy_savings"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
        "mx": {"apis": ["open_finance"], "use_cases": ["identity"]},
    },
    "journey_bundles": {
        "mcnext": ("loyalty_stack", "merchant_resolution", "subscriptions"),
        "mcnow": ("issuer_toolkit", "pfm_stack"),
        "shop": ("loyalty_stack", "subscriptions"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "issuer_toolkit"),
    },
}
