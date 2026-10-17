"""ABA Bank (Advanced Bank of Asia Limited).

The page (``ABA_Bank_Platform.html``) reads Cambodia's largest bank, a subsidiary of
National Bank of Canada, as five discs, Foundation to Access, with the businesses it
describes (retail, SME, corporate and investment banking, payments and cards), a Mastercard
lens (a Visa-first card book in a QR country, with Mastercard in debit) and ten journeys,
two of them for Mastercard. Public sources as at 17 October 2026; the research behind it
is in ``ABA_Bank_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the template and swaps in
the data from ``page_data.py``, ``aba_inventory.py`` and ``aba_story.py``::

    python customers/build_page.py aba
"""

CUSTOMER = {
    "id": "aba",
    "order": 870,
    "name": "ABA Bank",
    "short": "ABA",
    "brands": ["ABA Bank", "ABA Mobile", "ABA PAY", "ABA PayWay", "ABA Business"],
    "country": "Cambodia",
    "region": "Asia-Pacific",
    "accent": "#005d86",   # ABA teal, from verify.ababank.com's stylesheet
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "ABA Bank, National Bank of Canada Group", "bg": "#0d2b3d",
         "source": "https://verify.ababank.com/_nuxt/aba-logo.DSphYpjW.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Cambodia's largest bank as five discs: about 6 million customers on ABA Mobile and KHQR, affluent cards "
               "on Visa, and Mastercard in debit, virtual cards and card-to-card transfers.",
    "stats": [
        {"label": "Customers", "value": "6m+"},
        {"label": "Assets 2025", "value": "US$16.2bn"},
        {"label": "Net profit 2025", "value": "US$378m"},
        {"label": "Branches", "value": "104"},
    ],
    "page": "ABA_Bank_Platform.html",
    "notes": (
        ("Research notes", "ABA_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mcdebit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"], "bundles": ["issuer_toolkit"]},
        "visacredit": {"apis": ["benefits_eligibility", "priceless_cities", "consumer_clarity"], "use_cases": ["findacard", "consumer_clarity"],
                       "bundles": ["issuer_toolkit", "loyalty_stack"]},
        "virtual": {"apis": ["automatic_billing_updater", "transaction_notifications"], "use_cases": ["recurring", "txnotify"], "bundles": ["subscriptions"]},
        "swift": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "pos": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "payway": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi", "bin_lookup"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        # L3 Services
        "facepass": {"apis": ["transaction_notifications"], "use_cases": ["identity", "txnotify"]},
        "analytics": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
        "etiqa": {"apis": ["benefits_eligibility"], "use_cases": ["findacard"]},
        # L4 Business lines
        "ababusiness": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "smeloan": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "acquirer_risk"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "affluent": ("loyalty_stack",),
    },
}
