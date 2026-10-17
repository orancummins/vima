"""Tencent Holdings Limited, as a payments player.

The page (``Tencent_Platform.html``) reads Tencent through Weixin Pay, Tenpay,
TenPay Global and WeChat Pay HK, as five discs, Foundation to Access, with the
segments Tencent reports (FinTech and Business Services, Marketing Services,
VAS), a Mastercard lens (a wallet for 1.4 billion that runs off the card rails,
with Mastercard at the border) and ten journeys, two of them for Mastercard.
Public sources as at 17 October 2026; the research behind it is in
``Tencent_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``tencent_inventory.py`` and ``tencent_story.py``::

    python customers/build_page.py tencent
"""

CUSTOMER = {
    "id": "tencent",
    "order": 1430,
    "name": "Tencent",
    "short": "Tencent",
    "brands": ["Weixin Pay", "WeChat Pay", "Tenpay", "TenPay Global", "WeChat Pay HK", "QQ Wallet", "Licaitong", "WeSure"],
    "country": "China",
    "region": "Asia-Pacific",
    "type": "tech",
    "accent": "#0050d8",   # Tencent blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.png", "alt": "Tencent", "bg": "#ffffff", "source": "https://www.tencent.com/wp-content/uploads/2024/05/logo@2x-en.png"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Tencent's payments as five discs: Weixin Pay for 1.4 billion on domestic rails, with Mastercard "
               "among the networks visitors can bind and, since December 2025, Mastercard Move paying remittances in.",
    "stats": [
        {"label": "Weixin & WeChat MAU", "value": "1.44bn"},
        {"label": "FinTech & Business Services Q2 2026", "value": "RMB60.3bn"},
        {"label": "Visitor card payments Jan–Apr 2026", "value": "+80%"},
        {"label": "Overseas wallets linked", "value": "40+"},
    ],
    "page": "Tencent_Platform.html",
    "notes": (
        ("Research notes", "Tencent_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "wxpay": {"apis": ["merchant_identifier", "places"], "use_cases": ["enrichment", "places"], "bundles": ["merchant_resolution"]},
        "foreigncard": {"apis": ["enhanced_currency_conversion_calculator", "bin_lookup", "transaction_notifications"],
                        "use_cases": ["bin_lookup", "txnotify"], "bundles": ["issuer_toolkit"]},
        "cpg": {"apis": ["enhanced_currency_conversion_calculator", "merchant_identifier"], "use_cases": ["psi"], "bundles": ["merchant_resolution"]},
        "outbound": {"apis": ["merchant_identifier", "places", "match"], "use_cases": ["places", "psi"], "bundles": ["acquirer_risk"]},
        "mcmove": {"apis": ["enhanced_currency_conversion_calculator", "transaction_notifications"], "use_cases": ["settle_in", "txnotify"]},
        "wphk": {"apis": ["bin_lookup", "consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "merchantplat": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "marketing": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "xiaowei": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["identity", "enrichment"], "bundles": ["merchant_resolution"]},
        "realname": {"apis": ["bin_lookup"], "use_cases": ["identity"], "bundles": ["issuer_toolkit"]},
        "taxrefund": {"apis": ["enhanced_currency_conversion_calculator", "priceless_cities"], "use_cases": ["settle_in"]},
        # L4 Business lines
        "licaitong": {"apis": ["consumer_clarity"], "use_cases": ["pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "merchant_resolution", "acquirer_risk"),
        "mcnow": ("issuer_toolkit",),
        "visit": ("issuer_toolkit", "merchant_resolution"),
        "merchant": ("acquirer_risk", "loyalty_stack"),
        "save": ("pfm_stack",),
    },
}
