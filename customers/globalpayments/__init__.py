"""Global Payments Inc., including Worldpay.

The page (``Global_Payments_Platform.html``) reads the merchant company that
bought Worldpay and sold its issuer business as five discs, Foundation to
Access, with the three segments it reports from Q2 2026 (Enterprise,
Platforms, SMB), a Mastercard lens (accepted everywhere, partnered on Move in
the UAE) and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in
``Global_Payments_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``globalpayments_inventory.py`` and ``globalpayments_story.py``::

    python customers/build_page.py globalpayments
"""

CUSTOMER = {
    "id": "globalpayments",
    "order": 100,
    "name": "Global Payments",
    "short": "Global Payments",
    "brands": ["Global Payments", "Worldpay", "Genius", "Heartland", "Payrix"],
    "country": "United States",
    "region": "Global",
    "accent": "#262aff",   # Global Payments blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Global Payments", "bg": "#ffffff", "source": "static/logos/financial-logos-500/02-payments-and-processors/global-payments.png"},
        {"file": "logo-worldpay.png", "alt": "Worldpay", "bg": "#ffffff", "source": "static/logos/financial-logos-500/02-payments-and-processors/worldpay.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A pure merchant company since it bought Worldpay, as five discs: $3.7 trillion of volume at 6 million "
               "locations, Mastercard Move for payouts in the UAE, and agentic acceptance still open.",
    "stats": [
        {"label": "Volume", "value": "$3.7tn"},
        {"label": "Locations", "value": "6m+"},
        {"label": "Transactions a year", "value": "94bn"},
        {"label": "Countries", "value": "175+"},
    ],
    "page": "Global_Payments_Platform.html",
    "notes": (
        ("Research notes", "Global_Payments_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "wpenterprise": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"],
                         "bundles": ["acquirer_risk"]},
        "smbacq": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "gateway": {"apis": ["bin_lookup", "enhanced_currency_conversion_calculator"], "use_cases": ["bin_lookup"]},
        "move": {"apis": ["enhanced_currency_conversion_calculator"]},
        "fx": {"apis": ["enhanced_currency_conversion_calculator"]},
        # L3 Services
        "ravelin": {"apis": ["match", "merchant_identifier"], "bundles": ["acquirer_risk"]},
        "tokens": {"apis": ["automatic_billing_updater", "bin_lookup"], "use_cases": ["recurring"],
                   "bundles": ["subscriptions"]},
        "disputes": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "agentic": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "loyalty": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard"],
                    "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "enterprise": {"apis": ["consumer_clarity", "merchant_identifier"], "bundles": ["merchant_resolution"]},
        "platforms": {"apis": ["merchant_identifier", "match"], "bundles": ["acquirer_risk"]},
        "smb": {"apis": ["merchant_identifier", "places", "carbon_calculator"], "use_cases": ["places"],
                "bundles": ["sustainability"]},
        # L5 Access
        "genius": {"apis": ["places"], "use_cases": ["places"]},
    },
    "journey_bundles": {
        "mcnext": ("subscriptions", "merchant_resolution", "acquirer_risk"),
        "mcnow": ("acquirer_risk",),
        "genius": ("acquirer_risk", "loyalty_stack"),
        "enterprise": ("acquirer_risk", "merchant_resolution", "subscriptions"),
        "agent": ("subscriptions", "merchant_resolution"),
        "platform": ("acquirer_risk",),
    },
}
