"""CrediMax B.S.C. (c).

The page (``CrediMax_Platform.html``) reads Bahrain's first card issuer and
main acquirer, wholly owned by BBK, as five discs, Foundation to Access, with
the lines it sells (card issuing, merchant acquiring, corporate cards), a
Mastercard lens (a two-network issuer where Mastercard holds the top and the
checkout) and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in ``CrediMax_research_notes.md``.

Built like Lloyds': ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``credimax_inventory.py`` and ``credimax_story.py``::

    python customers/build_page.py credimax
"""

CUSTOMER = {
    "id": "credimax",
    "order": 990,
    "name": "CrediMax",
    "short": "CrediMax",
    "brands": ["CrediMax", "Thameen", "Tayseer", "iLead", "Cardy", "talabat Credit Card", "Danat"],
    "country": "Bahrain",
    "region": "EEMEA",
    "accent": "#10143b",   # CrediMax navy, from the logo (red #c4091e is the second colour)
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "CrediMax", "bg": "#ffffff",
         "source": "https://credimax.com.bh/wp-content/uploads/2024/02/cm_logo_full_new-1.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Bahrain's first card issuer and main acquirer as five discs: wholly owned by BBK, a credit range split "
               "seven to six between Mastercard and Visa, with Mastercard on World Elite, the talabat co-brand and Click to Pay.",
    "stats": [
        {"label": "First card", "value": "1991"},
        {"label": "Credit cards on Mastercard", "value": "7 of 14"},
        {"label": "BBK ownership", "value": "100%"},
        {"label": "Staff (2024)", "value": "109"},
    ],
    "page": "CrediMax_Platform.html",
    "notes": (
        ("Research notes", "CrediMax_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mccredit": {"apis": ["benefits_eligibility", "enhanced_currency_conversion_calculator", "consumer_clarity"],
                     "use_cases": ["findacard", "consumer_clarity"], "bundles": ["issuer_toolkit", "loyalty_stack"]},
        "talabat": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "mccorp": {"apis": ["business_payment_controls", "bin_lookup"], "use_cases": ["bin_lookup"], "bundles": ["issuer_toolkit"]},
        "vcp": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        "gateway": {"apis": ["match", "merchant_identifier", "automatic_billing_updater"], "use_cases": ["psi", "recurring"],
                    "bundles": ["acquirer_risk", "subscriptions"]},
        "pos": {"apis": ["match", "merchant_identifier", "places"], "use_cases": ["psi", "places"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "cardyex": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        # L3 Services
        "mccyber": {"apis": ["transaction_notifications"], "use_cases": ["txnotify", "identity"]},
        "thameen": {"apis": ["offers_for_publishers", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "offers": {"apis": ["offers_merchant_content", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L5 Access
        "app": {"apis": ["consumer_clarity", "transaction_notifications"], "use_cases": ["pfm", "txnotify"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "acquirer_risk", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack", "acquirer_risk"),
        "merch": ("acquirer_risk", "merchant_resolution"),
        "corp": ("issuer_toolkit",),
        "cobrand": ("loyalty_stack",),
    },
}
