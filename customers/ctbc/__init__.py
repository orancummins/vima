"""CTBC Bank Co., Ltd.

The page (``CTBC_Bank_Platform.html``) reads Taiwan's largest card issuer as
five discs, Foundation to Access, with its main business lines (consumer
banking and cards, wealth management, corporate banking, overseas
subsidiaries, group), a Mastercard lens (Mastercard on the uniopen co-brand,
Visa on LINE Pay and the newest launches) and ten journeys, two of them for
Mastercard. Public sources as at 17 October 2026; the research behind it is
in ``CTBC_Bank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``ctbc_inventory.py`` and ``ctbc_story.py``::

    python customers/build_page.py ctbc
"""

CUSTOMER = {
    "id": "ctbc",
    "order": 770,
    "name": "CTBC Bank",
    "short": "CTBC",
    "brands": ["CTBC Bank", "CTBC Financial Holding", "Tokyo Star Bank", "LH Bank", "Taiwan Life", "Taiwan Lottery"],
    "country": "Taiwan",
    "region": "Asia-Pacific",
    "accent": "#007979",   # CTBC teal, from the logo wordmark and ctbcbank.com
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "CTBC Bank", "bg": "#ffffff",
         "source": "https://www.ctbcbank.com/content/dam/twrbo/ctbc-web_mix/images/components/header/logo-lg-3x.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Taiwan's largest card issuer as five discs: NT$1 trillion of card spend on every network, Mastercard on "
               "the million-card uniopen co-brand, and Visa on LINE Pay and the newest launches.",
    "stats": [
        {"label": "Card spend 2025", "value": "NT$1trn+"},
        {"label": "Bank profit 9M26", "value": "NT$49.5bn"},
        {"label": "Digital users", "value": "8m+"},
        {"label": "uniopen cards", "value": "1m+"},
    ],
    "page": "CTBC_Bank_Platform.html",
    "notes": (
        ("Research notes", "CTBC_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "cards": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                  "bundles": ["issuer_toolkit"]},
        "uniopen": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "premium": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["specials"]},
        "smartpay": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "softpos": {"apis": ["places"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
        "openbanking": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "fx": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "cardalerts": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "fastid": {"use_cases": ["identity"]},
        "recurring": {"apis": ["automatic_billing_updater", "consumer_clarity"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "aisecretary": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("subscriptions", "pfm_stack", "issuer_toolkit"),
        "mcnow": ("loyalty_stack", "acquirer_risk"),
        "everyday": ("pfm_stack", "subscriptions"),
        "cobrand": ("loyalty_stack",),
        "merchant": ("acquirer_risk", "merchant_resolution"),
    },
}
