"""HBL (Habib Bank Limited).

The page (``HBL_Platform.html``) reads Pakistan's largest bank by customers as
five discs, Foundation to Access, with the segments it reports (retail,
consumer, SME and agriculture; corporate and investment banking; treasury;
branchless banking and microfinance; international), a Mastercard lens (one of
four networks at the country's biggest card bank) and nine journeys, two of
them for Mastercard. Public sources as at 17 October 2026; the research behind
it is in ``HBL_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``, ``hbl_inventory.py`` and
``hbl_story.py``::

    python customers/build_page.py hbl
"""

CUSTOMER = {
    "id": "hbl",
    "order": 830,
    "name": "HBL",
    "short": "HBL",
    "brands": ["HBL", "Konnect by HBL", "HBL Microfinance Bank", "HBL Prestige", "HBL Nisa", "HBL Asset Management"],
    "country": "Pakistan",
    "region": "Asia-Pacific",
    "accent": "#008078",   # HBL teal-green, from the 2026 logo and hbl.com
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "HBL", "bg": "#ffffff",
         "source": "https://commons.wikimedia.org/wiki/File:Habib_Bank_Limited_logo_(2026).png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Pakistan's largest bank by customers as five discs: one in five of the country's debit cards on "
               "Mastercard, Visa, UnionPay and PayPak, a third of its credit-card spend, and Konnect's 54,000 agents.",
    "stats": [
        {"label": "Customers", "value": "40m"},
        {"label": "Balance sheet", "value": "Rs 8.0tn"},
        {"label": "Debit cards", "value": "6.4m"},
        {"label": "Credit spend share", "value": "39%"},
    ],
    "page": "HBL_Platform.html",
    "notes": (
        ("Research notes", "HBL_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"]},
        "world": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["findacard"], "bundles": ["loyalty_stack"]},
        "bizdebit": {"apis": ["business_payment_controls", "easy_savings"], "use_cases": ["specials"], "bundles": ["issuer_toolkit"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "remit": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "hblpay": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "offers": {"apis": ["offers_for_publishers", "offers_merchant_content", "easy_savings"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines and L5 Access
        "sme": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "g2p": {"apis": ["transaction_notifications", "places"], "use_cases": ["txnotify", "places"]},
        "app": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack", "merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "sme": ("acquirer_risk", "issuer_toolkit"),
        "prestige": ("loyalty_stack",),
    },
}
