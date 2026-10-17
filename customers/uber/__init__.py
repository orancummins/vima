"""Uber Technologies, Inc.

The page (``Uber_Platform.html``) reads the rides, delivery and freight
platform through payments, as five discs, Foundation to Access, with the
segments it reports (Mobility, Delivery, Freight), a Mastercard lens
(Mastercard pays the drivers, Amex rewards the riders) and ten journeys, two
of them for Mastercard. Public sources as at 17 October 2026; the research
behind it is in ``Uber_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``uber_inventory.py`` and ``uber_story.py``::

    python customers/build_page.py uber
"""

CUSTOMER = {
    "id": "uber",
    "order": 1400,
    "name": "Uber",
    "short": "Uber",
    "brands": ["Uber", "Uber Eats", "Uber One", "Uber Pro Card", "Uber Cash", "Uber for Business", "Uber Freight"],
    "country": "United States",
    "region": "Global",
    "type": "merchant",
    "accent": "#191c1f",   # Uber black, from the wordmark
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Uber", "bg": "#ffffff", "source": "https://commons.wikimedia.org/wiki/File:Uber_logo_2018.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The rides, delivery and freight platform as five discs: $193.5 billion of bookings in 2025, drivers "
               "paid onto a Mastercard and by Mastercard Move, but American Express holds the richest rider benefit.",
    "stats": [
        {"label": "Gross Bookings 2025", "value": "$193.5bn"},
        {"label": "Q2 2026 bookings", "value": "$58.0bn"},
        {"label": "Monthly users", "value": "208m"},
        {"label": "Uber One members", "value": "50m"},
    ],
    "page": "Uber_Platform.html",
    "notes": (
        ("Research notes", "Uber_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "accept": {"apis": ["bin_lookup", "merchant_identifier", "match"], "use_cases": ["psi", "bin_lookup"], "bundles": ["acquirer_risk"]},
        "mcgateway": {"apis": ["bin_lookup", "match"], "use_cases": ["psi"], "bundles": ["acquirer_risk"]},
        "procardus": {"apis": ["transaction_notifications", "consumer_clarity"], "use_cases": ["txnotify", "pfm"], "bundles": ["issuer_toolkit"]},
        "procarduk": {"apis": ["transaction_notifications", "open_finance"], "use_cases": ["txnotify", "identity"], "bundles": ["issuer_toolkit"]},
        "onecard": {"apis": ["benefits_eligibility", "consumer_clarity"], "use_cases": ["findacard"], "bundles": ["issuer_toolkit"]},
        "ubercash": {"apis": ["consumer_clarity"], "use_cases": ["consumer_clarity"], "bundles": ["merchant_resolution"]},
        # L3 Services
        "uberone": {"apis": ["automatic_billing_updater"], "use_cases": ["recurring"], "bundles": ["subscriptions"]},
        "mcoffers": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "easysavings": {"apis": ["easy_savings"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "backup": {"apis": ["open_finance"], "use_cases": ["identity", "pfm"], "bundles": ["pfm_stack"]},
        # L4 Business lines
        "u4b": {"apis": ["business_payment_controls", "consumer_clarity"], "use_cases": ["enrichment"], "bundles": ["issuer_toolkit"]},
        "delivery": {"apis": ["merchant_identifier", "consumer_clarity", "places"], "use_cases": ["places"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("subscriptions", "issuer_toolkit"),
        "mcnow": ("issuer_toolkit", "loyalty_stack", "acquirer_risk"),
        "earn": ("issuer_toolkit", "pfm_stack"),
        "member": ("subscriptions", "loyalty_stack"),
        "eat": ("merchant_resolution",),
    },
}
