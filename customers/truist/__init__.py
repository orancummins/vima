"""Truist Financial Corporation.

The page (``Truist_Platform.html``) reads the Charlotte super-regional as five
discs, Foundation to Access, with the segments it reports (Consumer & Small
Business Banking, Wholesale Banking, Other, Treasury & Corporate), a Mastercard
lens (a Visa bank that made Mastercard its first open banking partner) and ten
journeys, two of them for Mastercard. Public sources as at 17 October 2026; the
research behind it is in ``Truist_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``truist_inventory.py`` and ``truist_story.py``::

    python customers/build_page.py truist
"""

CUSTOMER = {
    "id": "truist",
    "order": 1160,
    "name": "Truist",
    "short": "Truist",
    "brands": ["Truist", "Truist Wealth", "Truist Securities", "Sheffield Financial", "Service Finance", "LightStream"],
    "country": "United States",
    "region": "Americas",
    "type": "bank",
    "accent": "#2e1a47",   # Truist purple, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Truist", "bg": "#ffffff",
         "source": "https://static.truist.com/content/dam/global-images/truist-logo.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A $554 billion super-regional as five discs: Visa on every consumer and small business card, Mastercard "
               "in commercial cards and its first open banking partner, and a new CEO from Fiserv reviewing the lot.",
    "stats": [
        {"label": "Assets", "value": "$554bn"},
        {"label": "Branches", "value": "1,912"},
        {"label": "Card spend 3Q26", "value": "$32bn"},
        {"label": "Open banking on Mastercard", "value": "Feb 2026"},
    ],
    "page": "Truist_Platform.html",
    "notes": (
        ("Research notes", "Truist_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications"], "use_cases": ["txnotify"]},
        "enjoy": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"],
                  "use_cases": ["consumer_clarity", "recurring"], "bundles": ["issuer_toolkit"]},
        "commcards": {"apis": ["business_payment_controls", "enhanced_currency_conversion_calculator"],
                      "bundles": ["issuer_toolkit"]},
        "merchant": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"],
                     "bundles": ["acquirer_risk"]},
        "engage": {"apis": ["merchant_identifier", "offers_merchant_content"], "use_cases": ["places"],
                   "bundles": ["acquirer_risk", "merchant_resolution"]},
        # L3 Services
        "openbanking": {"apis": ["open_finance"], "use_cases": ["identity", "enrichment"], "bundles": ["pfm_stack"]},
        "dds": {"apis": ["automatic_billing_updater", "open_finance"], "use_cases": ["recurring"],
                "bundles": ["subscriptions"]},
        "insights": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["pfm", "enrichment"],
                     "bundles": ["pfm_stack"]},
        "assist": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "fraud": {"apis": ["transaction_notifications"], "use_cases": ["identity", "txnotify"]},
        "offers": {"apis": ["offers_for_publishers", "easy_savings"], "use_cases": ["findacard", "specials"],
                   "bundles": ["loyalty_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("pfm_stack", "issuer_toolkit", "acquirer_risk", "merchant_resolution"),
        "mcnow": ("pfm_stack", "issuer_toolkit", "acquirer_risk"),
        "everyday": ("pfm_stack", "merchant_resolution"),
        "switch": ("subscriptions", "loyalty_stack"),
        "smallbiz": ("acquirer_risk",),
    },
}
