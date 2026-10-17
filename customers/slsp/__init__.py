"""Slovenská sporiteľňa, a.s.

The page (``Slovenska_sporitelna_Platform.html``) reads Slovakia's largest
bank, a subsidiary of Erste Group, as five discs, Foundation to Access, with
the segments it reports (Retail, Corporates, Group Markets, and ALM & Local
Corporate Center), a Mastercard lens (Slovakia's biggest card issuer,
Visa-only since 2021, with Mastercard present only at acceptance) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``Slovenska_sporitelna_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes the template page and
swaps in the data from ``page_data.py``, ``slsp_inventory.py`` and
``slsp_story.py``::

    python customers/build_page.py slsp
"""

CUSTOMER = {
    "id": "slsp",
    "order": 640,
    "name": "Slovenská sporiteľňa",
    "short": "Slovenská sporiteľňa",
    "brands": ["Slovenská sporiteľňa", "George", "SPACE", "George Moneyback", "Dobrá karta", "Prvá stavebná sporiteľňa"],
    "country": "Slovakia",
    "region": "Europe",
    "type": "bank",
    "accent": "#2870ed",   # Erste blue, the colour behind the white logo on slsp.sk
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Slovenská sporiteľňa", "bg": "#2870ed",
         "source": "https://cdn.erstegroup.com/content/dam/sk/slsp/common/icons/logo-slsp.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Slovakia's largest bank as five discs: 1.8 million customers, a quarter of retail lending, 1.94 million "
               "cards that have all been Visa since 2021, and Mastercard only at the merchant's terminal.",
    "stats": [
        {"label": "Customers", "value": "1.8m"},
        {"label": "Loans", "value": "€20.7bn"},
        {"label": "ROE H1 2026", "value": "15.3%"},
        {"label": "George users", "value": "1.4m"},
    ],
    "page": "Slovenska_sporitelna_Platform.html",
    "notes": (
        ("Research notes", "Slovenska_sporitelna_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "bizdebit": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "accept": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "webpay": {"apis": ["automatic_billing_updater", "merchant_identifier"], "use_cases": ["recurring"], "bundles": ["subscriptions", "merchant_resolution"]},
        "qr": {"apis": ["open_finance_eu"], "use_cases": ["identity"]},
        "dobra": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications", "open_finance_eu"], "use_cases": ["txnotify", "identity"]},
        "georgeai": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "moneyback": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "accounts": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "corporate": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "loyalty_stack", "issuer_toolkit"),
        "mcnow": ("acquirer_risk", "merchant_resolution"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "subscriptions"),
        "rewards": ("loyalty_stack", "sustainability"),
    },
}
