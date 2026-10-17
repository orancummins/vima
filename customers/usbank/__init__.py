"""U.S. Bancorp (U.S. Bank).

The page (``US_Bank_Platform.html``) reads America's fifth-largest commercial
bank as five discs, Foundation to Access, with the segments it reports (Wealth,
Corporate, Commercial & Institutional Banking; Consumer & Business Banking;
Payment Services; Treasury & Corporate Support), Elavon's acquiring and Elan's
agent cards, a Mastercard lens (a Visa bank whose biggest new co-brand runs on
Mastercard) and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in ``US_Bank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``usbank_inventory.py`` and ``usbank_story.py``::

    python customers/build_page.py usbank
"""

CUSTOMER = {
    "id": "usbank",
    "order": 1150,
    "name": "U.S. Bank",
    "short": "U.S. Bank",
    "brands": ["U.S. Bank", "Elavon", "Elan Financial Services", "Opayo", "Avvance", "BTIG", "Voyager"],
    "country": "United States",
    "region": "Americas",
    "type": "bank",
    "accent": "#001e79",   # U.S. Bank navy, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "U.S. Bank", "bg": "#ffffff",
         "source": "https://www.usbank.com/etc.clientlibs/ecm-global/clientlibs/clientlib-resources/resources/images/svg/logo-personal.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "America's fifth-largest commercial bank as five discs: Visa on its debit and own-brand cards, "
               "Mastercard on the Amazon, Edward Jones and BMW co-brands, with Elavon acquiring and Elan issuing for 1,300 banks.",
    "stats": [
        {"label": "Assets", "value": "$703bn"},
        {"label": "ROTCE Q3 2026", "value": "18.5%"},
        {"label": "Clients", "value": "15m"},
        {"label": "Elavon merchants", "value": "2m"},
    ],
    "page": "US_Bank_Platform.html",
    "notes": (
        ("Research notes", "US_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "split": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["consumer_clarity", "pfm"], "bundles": ["pfm_stack"]},
        "amazon": {"apis": ["business_payment_controls", "offers_for_publishers", "merchant_identifier"], "use_cases": ["enrichment", "specials"],
                   "bundles": ["issuer_toolkit", "loyalty_stack"]},
        "edwardjones": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "elan": {"apis": ["bin_lookup", "automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["issuer_toolkit"]},
        "commcard": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "elavon": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        # L3 Services
        "protect": {"apis": ["open_finance", "transaction_notifications"], "use_cases": ["identity", "txnotify"]},
        "subs": {"apis": ["automatic_billing_updater", "consumer_clarity"], "use_cases": ["recurring", "consumer_clarity"], "bundles": ["subscriptions"]},
        "spend": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("acquirer_risk", "issuer_toolkit", "merchant_resolution"),
        "mcnow": ("issuer_toolkit", "loyalty_stack", "subscriptions"),
        "card": ("subscriptions", "pfm_stack"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "amazon": ("issuer_toolkit",),
    },
}
