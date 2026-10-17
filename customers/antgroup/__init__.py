"""Ant International.

The page (``Ant_International_Platform.html``) reads Ant Group's Singapore-based
international arm as five discs, Foundation to Access, with its four pillars
(Alipay+, Antom, WorldFirst, Bettr), a Mastercard lens (Mastercard's tap for
Alipay+ wallets, on a network built to go around cards) and nine journeys, two
of them for Mastercard. Ant International is private: figures are its own
releases, its 2025 Sustainability Report and press, as at 17 October 2026; the
research behind it is in ``Ant_International_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``antgroup_inventory.py`` and ``antgroup_story.py``::

    python customers/build_page.py antgroup
"""

CUSTOMER = {
    "id": "antgroup",
    "order": 1420,
    "name": "Ant International",
    "short": "Ant International",
    "brands": ["Alipay+", "Antom", "WorldFirst", "Bettr", "2C2P", "MultiSafepay", "ANEXT Bank"],
    "country": "Singapore",
    "region": "Global",
    "type": "wallet",
    "accent": "#0066ff",   # Ant International blue, from the logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Ant International", "bg": "#ffffff", "source": "https://cdn.marmot-cloud.com/storage/intl_website/2025/11/18/Ys73XZ4/logo-nav-antintl-color.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "A cross-border wallet and payments group as five discs: 150 million merchants and 2 billion accounts, "
               "Mastercard the only network behind Alipay+ NFC, with most volume on its own QR and blockchain rails.",
    "stats": [
        {"label": "Merchants", "value": "150m+"},
        {"label": "User accounts", "value": "2bn+"},
        {"label": "Revenue 2024", "value": "~$3bn"},
        {"label": "Series A 2026", "value": "$1.2bn"},
    ],
    "page": "Ant_International_Platform.html",
    "notes": (
        ("Research notes", "Ant_International_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "aplusnfc": {"apis": ["bin_lookup", "transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "antomacq": {"apis": ["merchant_identifier", "match", "bin_lookup"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "worldcard": {"apis": ["business_payment_controls", "enhanced_currency_conversion_calculator"], "bundles": ["issuer_toolkit"]},
        "worldacct": {"apis": ["enhanced_currency_conversion_calculator"]},
        # L3 Services
        "antomshield": {"apis": ["match", "merchant_identifier"], "bundles": ["acquirer_risk"]},
        "smartdispute": {"apis": ["consumer_clarity", "match"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        "tokenpay": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "agentpay": {"apis": ["bin_lookup", "merchant_identifier"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "aplusrewards": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        # L4 Business lines
        "chinainbound": {"apis": ["places", "priceless_cities"], "use_cases": ["places"]},
        "antommerchants": {"apis": ["merchant_identifier", "carbon_calculator"], "bundles": ["sustainability"]},
    },
    "journey_bundles": {
        "mcnext": ("merchant_resolution", "subscriptions", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "acquirer_risk"),
        "merchant": ("acquirer_risk", "merchant_resolution"),
        "travel": ("loyalty_stack", "issuer_toolkit"),
        "agent": ("subscriptions",),
    },
}
