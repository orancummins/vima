"""Booking Holdings Inc.

The page (``Booking_Holdings_Platform.html``) reads the world's largest online
travel group through payments, as five discs, Foundation to Access, with the
revenue types it reports (merchant, agency, advertising and other), a
Mastercard lens (Mastercard pays the hotels; Visa holds the cards travellers
carry) and ten journeys, two of them for Mastercard. Public sources as at
17 October 2026; the research behind it is in
``Booking_Holdings_research_notes.md``.

Built like Citi's: ``customers/build_page.py`` takes SNB's page as the
template and swaps in the data from ``page_data.py``,
``booking_inventory.py`` and ``booking_story.py``::

    python customers/build_page.py booking
"""

CUSTOMER = {
    "id": "booking",
    "order": 1410,
    "name": "Booking Holdings",
    "short": "Booking",
    "brands": ["Booking.com", "Priceline", "Agoda", "KAYAK", "OpenTable", "Rentalcars.com", "Booking Holdings Financial Services"],
    "country": "United States",
    "region": "Global",
    "type": "merchant",
    "accent": "#003680",   # Booking navy, from bookingholdings.com's stylesheet (the logo itself is black)
    "logos": (   # file in this folder, alt text, the chip behind it, where it came from
        {"file": "logo.svg", "alt": "Booking Holdings", "bg": "#ffffff",
         "source": "https://www.bookingholdings.com/wp-content/themes/booking-group/img/svg/bkng_global-desktop-logoblack.svg"},
    ),
    "as_of": "17 October 2026",
    "tagline": "The world's largest online travel group as five discs: $186.1 billion booked, 70% of it with Booking "
               "as merchant, hotels paid on Mastercard virtual cards, and Visa on the Priceline and OpenTable perks.",
    "stats": [
        {"label": "Gross bookings 2025", "value": "$186.1bn"},
        {"label": "Merchant share", "value": "70%"},
        {"label": "Room nights 2025", "value": "1.24bn"},
        {"label": "Q2 2026 bookings", "value": "$51.0bn"},
    ],
    "page": "Booking_Holdings_Platform.html",
    "notes": (
        ("Research notes", "Booking_Holdings_research_notes.md"),
    ),
    "studio": {
        # L2 Rails
        "mor": {"apis": ["merchant_identifier", "bin_lookup", "match"], "use_cases": ["psi", "bin_lookup"], "bundles": ["merchant_resolution", "acquirer_risk"]},
        "accept": {"apis": ["bin_lookup", "enhanced_currency_conversion_calculator"], "use_cases": ["bin_lookup"], "bundles": ["acquirer_risk"]},
        "vcc": {"apis": ["business_payment_controls", "transaction_notifications"], "use_cases": ["txnotify"], "bundles": ["issuer_toolkit"]},
        "banktransfer": {"apis": ["open_finance"], "use_cases": ["identity"]},
        "bookingcard": {"apis": ["benefits_eligibility", "consumer_clarity"], "use_cases": ["findacard"], "bundles": ["issuer_toolkit"]},
        # L3 Services
        "genius": {"apis": ["offers_for_publishers", "offers_merchant_content"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "agodaredeem": {"apis": ["offers_for_publishers", "priceless_cities"], "use_cases": ["specials"], "bundles": ["loyalty_stack"]},
        "trust": {"apis": ["match", "merchant_identifier"], "use_cases": ["identity"], "bundles": ["acquirer_risk"]},
        # L4 Business lines
        "stays": {"apis": ["places", "enhanced_currency_conversion_calculator"], "use_cases": ["places", "settle_in"]},
        "flights": {"apis": ["carbon_calculator"], "bundles": ["sustainability"]},
        "biztravel": {"apis": ["business_payment_controls"], "bundles": ["issuer_toolkit"]},
        # L5 Access
        "chatgpt": {"apis": ["merchant_identifier", "consumer_clarity"], "use_cases": ["enrichment"], "bundles": ["merchant_resolution"]},
    },
    "journey_bundles": {
        "mcnext": ("merchant_resolution", "acquirer_risk", "loyalty_stack"),
        "mcnow": ("issuer_toolkit", "loyalty_stack"),
        "stay": ("merchant_resolution", "acquirer_risk"),
        "getpaid": ("issuer_toolkit",),
        "trip": ("sustainability", "loyalty_stack"),
    },
}
