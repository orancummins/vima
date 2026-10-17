"""Citi (Citigroup).

The page (``Citi_Platform.html``) reads Citi as five discs, Foundation to
Access, with the five segments it has reported since 1Q26 (Services,
Markets, Banking, Wealth, U.S. Consumer Cards), a Mastercard lens that raises
each area by how deep Mastercard goes in it, and twelve journeys, two of them
for Mastercard. Public sources as at 17 October 2026; the research behind it
is in ``Citi_research_notes.md``.

Unlike SNB's page, which was built elsewhere and copied in, Citi's is built
here: ``customers/build_page.py`` takes SNB's page as the template (the same engine)
and swaps in Citi's data from ``page_data.py``, ``citi_foundation.py``,
``citi_inventory.py`` and ``citi_story.py``. Edit those and rebuild::

    python customers/build_page.py citi

``STUDIO`` puts Solution Studio's APIs, use cases and bundles on the Citi
products where the page's own Mastercard notes say they fit.
"""

CUSTOMER = {
    "id": "citi",
    "order": 20,
    "name": "Citi",
    "short": "Citi",
    "brands": ["Citi", "Citibank", "Banamex"],
    "country": "United States",
    "region": "Global",
    "accent": "#1c4882",   # Citi blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Citi", "bg": "#ffffff", "source": "static/logos/financial-logos-500/01-financial-institutions/citi.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A global bank in nearly 160 countries as five discs: $6 trillion a day of payments at the "
               "institutional end, 70 million American cardmembers at the other, and Mastercard under the cards.",
    "stats": [
        {"label": "Assets", "value": "$2.94tn"},
        {"label": "Payments a day", "value": "~$6tn"},
        {"label": "US card customers", "value": "~70m"},
        {"label": "Mastercard network deal", "value": "since 2015"},
    ],
    "page": "Citi_Platform.html",
    "notes": (
        ("Research notes", "Citi_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "commcards": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "vca": {"apis": ["business_payment_controls"]},
        "smartpay": {"apis": ["business_payment_controls"]},
        "worldlink": {"apis": ["enhanced_currency_conversion_calculator"]},
        "payex": {"apis": ["enhanced_currency_conversion_calculator"]},
        "spring": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"],
                   "bundles": ["acquirer_risk"]},
        # L3 Services
        "cardrisk": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "underwrite": {"apis": ["open_finance"], "use_cases": ["enrichment"]},
        "openfin": {"apis": ["open_finance", "open_finance_eu"], "use_cases": ["enrichment", "identity"],
                    "bundles": ["pfm_stack"]},
        "thankyou": {"apis": ["offers_for_publishers", "easy_savings"], "bundles": ["loyalty_stack"]},
        "cititravel": {"apis": ["enhanced_currency_conversion_calculator", "priceless_cities"], "use_cases": ["specials"]},
        "priceless": {"apis": ["priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "offers": {"apis": ["offers_for_publishers", "offers_merchant_content", "places"], "use_cases": ["findacard"],
                   "bundles": ["loyalty_stack"]},
        "kard": {"apis": ["offers_merchant_content"]},
        "service": {"apis": ["consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                    "bundles": ["merchant_resolution", "subscriptions"]},
        # L4 Business lines
        "brandedcards": {"apis": ["bin_lookup", "automatic_billing_updater"], "use_cases": ["bin_lookup", "recurring"],
                         "bundles": ["issuer_toolkit"]},
        "stratae": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["specials"]},
        "aacards": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator"]},
        "citigold": {"use_cases": ["pfm"]},
        # L5 Access
        "mobile": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"],
                   "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "loyalty_stack", "merchant_resolution", "subscriptions"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "card": ("issuer_toolkit", "subscriptions"),
        "fly": ("loyalty_stack",),
        "checkout": ("loyalty_stack",),
        "grow": ("issuer_toolkit",),
        "treasury": ("issuer_toolkit",),
    },
}
