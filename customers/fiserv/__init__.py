"""Fiserv, Inc.

The page (``Fiserv_Platform.html``) reads America's largest merchant
acquirer, and processor for about 10,000 banks, as five discs, Foundation to
Access, with the two segments it reports (Merchant Solutions, Financial
Solutions), a Mastercard lens (a partner on the merchant side, a rival in
debit) and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in ``Fiserv_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``fiserv_inventory.py`` and ``fiserv_story.py``::

    python customers/build_page.py fiserv
"""

CUSTOMER = {
    "id": "fiserv",
    "order": 90,
    "name": "Fiserv",
    "short": "Fiserv",
    "brands": ["Fiserv", "Clover", "Carat", "STAR", "Accel"],
    "country": "United States",
    "region": "Americas",
    "accent": "#ff6600",   # Fiserv orange, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Fiserv", "bg": "#ffffff", "source": "https://www.fiserv.com/"},
    ),
    "as_of": "17 October 2026",
    "tagline": "America's largest merchant acquirer and a processor for 10,000 banks as five discs: Mastercard "
               "Merchant Cloud now inside Commerce Hub, while STAR and Accel compete with Debit Mastercard.",
    "stats": [
        {"label": "Merchant volume 2025", "value": "$4.6tn"},
        {"label": "Revenue 2025", "value": "$21.2bn"},
        {"label": "Bank clients", "value": "~10,000"},
        {"label": "Clover merchants", "value": "~900k"},
    ],
    "page": "Fiserv_Platform.html",
    "notes": (
        ("Research notes", "Fiserv_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "acquiring": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"],
                      "bundles": ["acquirer_risk"]},
        "carat": {"apis": ["merchant_identifier", "bin_lookup"], "use_cases": ["bin_lookup"], "bundles": ["acquirer_risk"]},
        "merchantcloud": {"apis": ["consumer_clarity", "merchant_identifier", "automatic_billing_updater"],
                          "use_cases": ["consumer_clarity", "recurring"],
                          "bundles": ["merchant_resolution", "subscriptions"]},
        "issuing": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater", "transaction_notifications"],
                    "use_cases": ["txnotify", "recurring"], "bundles": ["issuer_toolkit"]},
        "star": {"apis": ["bin_lookup"], "use_cases": ["bin_lookup"]},
        # L3 Services
        "agentpay": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "fraud": {"apis": ["match", "transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["acquirer_risk"]},
        "smbfinance": {"apis": ["open_finance", "business_payment_controls"], "use_cases": ["enrichment"]},
        "giftloyalty": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard"],
                        "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "clover": {"apis": ["merchant_identifier", "carbon_calculator", "places"], "use_cases": ["places"],
                   "bundles": ["sustainability"]},
        "enterprise": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "xd": {"apis": ["open_finance", "consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"],
               "bundles": ["pfm_stack"]},
        "cardservices": {"apis": ["business_payment_controls", "benefits_eligibility"], "bundles": ["issuer_toolkit"]},
        "payouts": {"apis": ["enhanced_currency_conversion_calculator"]},
    },
    "journey_bundles": {
        "mcnext": ("merchant_resolution", "issuer_toolkit", "subscriptions", "pfm_stack"),
        "mcnow": ("acquirer_risk", "merchant_resolution"),
        "clover": ("acquirer_risk", "sustainability"),
        "enterprise": ("merchant_resolution", "loyalty_stack"),
        "cards": ("issuer_toolkit",),
        "bank": ("pfm_stack", "issuer_toolkit"),
    },
}
