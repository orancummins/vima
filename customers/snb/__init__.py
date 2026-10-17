"""Saudi National Bank and NEO, its digital bank.

The page (``SNB_Operating_System.html``) reads the Kingdom's largest bank as
five discs, Foundation to Access, with NEO in every layer it touches, a NEO
lens that raises each area by NEO's depth in it, and twelve journeys, two of
them for Mastercard: "Where Mastercard already is" and "Where Open Finance,
data and loyalty could land". Built from public sources as at 16 October
2026; the research behind it is in ``SNB_NEO_research_notes.md`` and the
walkthrough video's script in ``SNB_Operating_System_narration.md``.

``STUDIO`` puts Solution Studio's APIs, use cases and bundles on the SNB
products where the page's own Mastercard notes say they fit. Product ids
are the page's own (``P("openbanking", ...)``); ``tools/sync_customer.py``
checks they are all still there when the page is refreshed.
"""

CUSTOMER = {
    "id": "snb",
    "order": 10,
    "name": "Saudi National Bank",
    "short": "SNB",
    "brands": ["SNB", "AlAhli", "NEO"],
    "country": "Saudi Arabia",
    "region": "EEMEA",
    "accent": "#00a862",   # SNB green, on the Customers tab card
    "as_of": "16 October 2026",
    "tagline": "The Kingdom's largest bank as five discs, with NEO, its digital bank, "
               "in every layer it touches, and where Mastercard already is.",
    "stats": [
        {"label": "Assets", "value": "SAR 1.24tn"},
        {"label": "Customers", "value": "~15m"},
        {"label": "NEO customers", "value": "~1.9m"},
        {"label": "Mastercard partner", "value": "since 2019"},
    ],
    "page": "SNB_Operating_System.html",
    "notes": (
        ("Research notes", "SNB_NEO_research_notes.md"),
        ("Video narration", "SNB_Operating_System_narration.md"),
    ),
    # Studio calls these platforms; the page calls itself an operating system.
    "text_swaps": (
        ('<h1>SNB <span class="os">Operating System</span></h1>',
         '<h1>SNB <span class="os">Platform</span></h1>'),
        ("as five discs that stack into one system", "as five discs that stack into one platform"),
    ),
    "studio": {
        # L5 Access
        "neoonb": {"use_cases": ["identity"]},
        "neoplaces": {"apis": ["places", "offers_for_publishers"], "use_cases": ["places"]},
        "neoeveryday": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"],
                        "bundles": ["pfm_stack"]},
        "ecorp": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L4 Business lines
        "neomcy": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "flexi": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "poslending": {"apis": ["open_finance", "merchant_identifier"], "use_cases": ["enrichment"],
                       "bundles": ["merchant_resolution"]},
        "msme": {"apis": ["open_finance", "business_payment_controls"]},
        "gtb": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "worldlegend": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["specials"]},
        # L3 Services
        "nafath": {"use_cases": ["identity"]},
        "cardsec": {"apis": ["transaction_notifications", "consumer_clarity"],
                    "use_cases": ["txnotify", "consumer_clarity"]},
        "digidecision": {"apis": ["open_finance"], "use_cases": ["psi"], "bundles": ["pfm_stack"]},
        "mcashflow": {"apis": ["open_finance", "merchant_identifier"], "use_cases": ["enrichment"],
                      "bundles": ["acquirer_risk"]},
        "openbanking": {"apis": ["open_finance", "open_finance_eu"], "use_cases": ["enrichment", "identity"],
                        "bundles": ["pfm_stack"]},
        "ai": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment"]},
        "lak": {"apis": ["priceless_cities", "easy_savings"], "bundles": ["loyalty_stack"]},
        "neons": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["findacard"],
                  "bundles": ["loyalty_stack"]},
        "priceless": {"apis": ["priceless_cities"], "use_cases": ["specials"]},
        "service": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"],
                    "bundles": ["merchant_resolution"]},
        # L2 Rails
        "cards": {"apis": ["bin_lookup", "automatic_billing_updater"], "use_cases": ["bin_lookup", "recurring"],
                  "bundles": ["issuer_toolkit"]},
        "neosky": {"apis": ["enhanced_currency_conversion_calculator", "benefits_eligibility"],
                   "use_cases": ["settle_in"]},
        "quickpay": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "sadad": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "acquiring": {"apis": ["merchant_identifier", "match", "places"], "bundles": ["acquirer_risk"]},
        "mcgateway": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["psi"]},
        "sustainable": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
    },
    # The page's journeys (its "outcomes") -> the Studio bundles that put them into practice.
    "journey_bundles": {
        "mcnext": ("pfm_stack", "loyalty_stack", "merchant_resolution"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "accept": ("acquirer_risk", "merchant_resolution"),
        "pay": ("subscriptions",),
        "wealth": ("loyalty_stack",),
        "corp": ("issuer_toolkit",),
        "plug": ("pfm_stack",),
    },
}
