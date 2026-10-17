"""The Mauritius Commercial Bank (MCB Group).

The page (``Mauritius_Commercial_Bank_Platform.html``) reads Mauritius' largest
bank as five discs, Foundation to Access, with the segments it reports (Retail
and Business Banking, Mauritian and Regional Corporates, the overseas banks in
Madagascar, Seychelles and Maldives, and African corporate, investment and
private banking), a Mastercard lens (Mastercard debit for the mass market, Visa
on the premium and digital front) and ten journeys, two of them for Mastercard.
Public sources as at 17 October 2026; the research behind it is in
``Mauritius_Commercial_Bank_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``mcb_inventory.py`` and ``mcb_story.py``::

    python customers/build_page.py mcb
"""

CUSTOMER = {
    "id": "mcb",
    "order": 1130,
    "name": "Mauritius Commercial Bank (MCB)",
    "short": "MCB",
    "brands": ["MCB", "MCB Juice", "JuicePro", "MCB Madagascar", "MCB Seychelles", "MCB Maldives", "MCB Capital Markets"],
    "country": "Mauritius",
    "region": "EEMEA",
    "accent": "#c41230",   # MCB red, from the caravelle logo
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "MCB", "bg": "#ffffff",
         "source": "https://mcb.mu/images/mcb/default-album/logo-mcb-color.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "Mauritius' largest bank as five discs: a Mastercard debit card in most Mauritian wallets, Visa on "
               "premium, SME and island cards, and MauCAS QR in the Juice app growing fastest.",
    "stats": [
        {"label": "Profit FY26", "value": "Rs 20.1bn"},
        {"label": "Rupee deposit share", "value": "~50%"},
        {"label": "Juice subscribers", "value": "709k"},
        {"label": "Founded", "value": "1838"},
    ],
    "page": "Mauritius_Commercial_Bank_Platform.html",
    "notes": (
        ("Research notes", "Mauritius_Commercial_Bank_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "debit": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["txnotify", "bin_lookup"]},
        "credit": {"apis": ["bin_lookup", "consumer_clarity", "automatic_billing_updater"], "use_cases": ["consumer_clarity", "recurring"],
                   "bundles": ["issuer_toolkit"]},
        "premium": {"apis": ["benefits_eligibility", "priceless_cities"], "use_cases": ["specials", "findacard"], "bundles": ["loyalty_stack"]},
        "corpcard": {"apis": ["business_payment_controls", "enhanced_currency_conversion_calculator"], "bundles": ["issuer_toolkit"]},
        "fleetman": {"apis": ["business_payment_controls", "carbon_calculator"], "bundles": ["sustainability"]},
        "acquiring": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "ecom": {"apis": ["merchant_identifier", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk", "merchant_resolution"]},
        "remit": {"apis": ["enhanced_currency_conversion_calculator"], "use_cases": ["settle_in"]},
        "juicetap": {"apis": ["automatic_billing_updater", "transaction_notifications"], "use_cases": ["recurring", "txnotify"], "bundles": ["subscriptions"]},
        # L3 Services
        "security": {"apis": ["transaction_notifications", "bin_lookup"], "use_cases": ["identity", "txnotify"]},
        "offers": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials", "enrichment"], "bundles": ["loyalty_stack"]},
        # L5 Access
        "juice": {"apis": ["consumer_clarity", "merchant_identifier"], "use_cases": ["enrichment", "pfm"], "bundles": ["pfm_stack"]},
    },
    "journey_bundles": {
        "mcnext": ("issuer_toolkit", "loyalty_stack", "acquirer_risk"),
        "mcnow": ("issuer_toolkit", "subscriptions"),
        "everyday": ("pfm_stack", "subscriptions"),
        "sme": ("acquirer_risk", "merchant_resolution"),
        "premium": ("loyalty_stack",),
    },
}
