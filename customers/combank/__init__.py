"""Commercial Bank of Ceylon PLC (ComBank).

The page (``Commercial_Bank_of_Ceylon_Platform.html``) reads Sri Lanka's
largest private bank as five discs, Foundation to Access, with the segments it
reports (Personal Banking, Corporate Banking, International Operations,
Dealing/Treasury, NBFI), a Mastercard lens (four networks, with Mastercard
holding the co-brands and the gateway) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is in
``Commercial_Bank_of_Ceylon_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``combank_inventory.py`` and ``combank_story.py``::

    python customers/build_page.py combank
"""

CUSTOMER = {
    "id": "combank",
    "order": 850,
    "name": "Commercial Bank of Ceylon",
    "short": "ComBank",
    "brands": ["Commercial Bank", "ComBank Digital", "Q+", "Flash", "Prestige", "CBC Finance"],
    "country": "Sri Lanka",
    "region": "Asia-Pacific",
    "type": "bank",
    "accent": "#006fba",   # ComBank blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Commercial Bank of Ceylon", "bg": "#ffffff",
         "source": "https://www.combank.lk/assets/images/logo/commercial_bank_logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Sri Lanka's largest private bank as five discs: cards on four networks, Mastercard in the co-brands, "
               "the gateway and Soundbox, Visa on top, and the national LankaPay and LANKAQR rails pushed hard.",
    "stats": [
        {"label": "Assets", "value": "Rs 3.74tn"},
        {"label": "Customers", "value": "4m+"},
        {"label": "ROE H1 2026", "value": "20.3%"},
        {"label": "Card networks", "value": "4"},
    ],
    "page": "Commercial_Bank_of_Ceylon_Platform.html",
    "notes": (
        ("Research notes", "Commercial_Bank_of_Ceylon_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "worldmc": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "corpcard": {"apis": ["business_payment_controls", "enhanced_currency_conversion_calculator"], "bundles": ["issuer_toolkit"]},
        "fuelcard": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "gpaymc": {"apis": ["automatic_billing_updater", "transaction_notifications"], "use_cases": ["recurring", "txnotify"], "bundles": ["subscriptions"]},
        "pos": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "soundbox": {"apis": ["merchant_identifier", "places"], "use_cases": ["places", "psi"], "bundles": ["acquirer_risk"]},
        "ipg": {"apis": ["enhanced_currency_conversion_calculator", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "remit": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "threeds": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["identity", "txnotify"]},
        "rewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "enrichment"], "bundles": ["loyalty_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "loyalty_stack"),
        "mcnow": ("loyalty_stack", "acquirer_risk"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "premium": ("loyalty_stack",),
        "everyday": ("pfm_stack", "subscriptions"),
    },
}
