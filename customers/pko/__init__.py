"""PKO Bank Polski S.A.

The page (``PKO_Bank_Polski_Platform.html``) reads Poland's largest bank as
five discs, Foundation to Access, with the segments it reports (Retail,
Corporate & Investment, Transfer centre & other), a Mastercard lens (a Visa
debit bank whose phones tap on Mastercard through contactless BLIK) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026;
the research behind it is in ``PKO_Bank_Polski_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``pko_inventory.py``
and ``pko_story.py``::

    python customers/build_page.py pko
"""

CUSTOMER = {
    "id": "pko",
    "order": 550,
    "name": "PKO Bank Polski",
    "short": "PKO",
    "brands": ["PKO Bank Polski", "IKO", "PKO Bank Hipoteczny", "PKO Leasing", "PKO TFI", "KREDOBANK"],
    "country": "Poland",
    "region": "Europe",
    "type": "bank",
    "accent": "#000066",   # PKO navy, the site's theme colour; the logo is black with a red dot
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "PKO Bank Polski", "bg": "#ffffff",
         "source": "https://www.pkobp.pl/api/public/63086f97-c7b3-436b-a060-a2947f8713f4.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Poland's largest bank as five discs: 12.6 million customers, 9.9 million debit cards on Visa, and 516 million "
               "contactless BLIK payments tapped on Mastercard terminals.",
    "stats": [
        {"label": "Customers", "value": "12.6m"},
        {"label": "Net profit 1H 2026", "value": "PLN 5.3bn"},
        {"label": "ROE 1H 2026", "value": "18.4%"},
        {"label": "Contactless BLIK", "value": "517m"},
    ],
    "page": "PKO_Bank_Polski_Platform.html",
    "notes": (
        ("Research notes", "PKO_Bank_Polski_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "enrichment"]},
        "mcplat": {"apis": ["benefits_eligibility", "priceless_cities", "enhanced_currency_conversion_calculator"],
                   "use_cases": ["findacard"], "bundles": ["issuer_toolkit"]},
        "przejrzysta": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                        "bundles": ["issuer_toolkit"]},
        "blikc": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications", "merchant_identifier"],
                  "use_cases": ["txnotify", "enrichment"], "bundles": ["pfm_stack"]},
        "terminals": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "wallets": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        # L3 Services
        "behav": {"apis": ["open_finance_eu", "transaction_notifications"], "use_cases": ["identity", "txnotify"]},
        "allegro": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "kropka": {"apis": ["offers_for_publishers", "consumer_clarity"], "use_cases": ["specials", "pfm"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "accounts": {"apis": ["consumer_clarity", "open_finance_eu"], "use_cases": ["pfm"], "bundles": ["merchant_resolution"]},
        "leasing": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "firms": {"apis": ["business_payment_controls", "places"], "use_cases": ["places"], "bundles": ["acquirer_risk"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "sustainability"),
        "mcnow": ("pfm_stack", "issuer_toolkit", "acquirer_risk"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "shop": ("loyalty_stack", "subscriptions"),
        "sme": ("acquirer_risk",),
    },
}
