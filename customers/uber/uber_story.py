"""Uber's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from uber_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The rides, delivery and freight platform, read through payments, as five discs that stack into one, from "
       "$193.5 billion of Gross Bookings at the bottom to the apps, kiosks and partners at the top. Click the stack to "
       "open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("rider", "Riders", "user-round"),
    ("eater", "Eaters & shoppers", "store"),
    ("member", "Uber One members", "gift"),
    ("earner", "Drivers & couriers", "wallet-cards"),
    ("mer", "Restaurants & merchants", "building-2"),
    ("biz", "Businesses", "briefcase-business"),
    ("shipper", "Shippers & carriers", "factory"),
]
USERS_DESC = ("Seven kinds of user: 208 million monthly riders and eaters, 50 million Uber One members, more than "
              "8.5 million drivers and couriers, the restaurants and stores on Uber Eats, more than 300,000 businesses, "
              "and the shippers and carriers on Uber Freight.")

WHO = {"rider": "A rider", "eater": "An eater", "member": "An Uber One member", "earner": "A driver or courier",
       "mer": "A restaurant", "biz": "A business", "shipper": "A shipper"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "ride", "who": "rider", "name": "Take a ride and pay",
     "why": "The everyday loop: the app, a saved card or wallet, processed by Adyen.",
     "steps": [("5.1", "app", "Open the app"), ("4.1", "mobility", "Book a ride"), ("2.1", "accept", "Pay with a saved card"),
               ("2.2", "adyen", "Processed by Adyen")]},
    {"id": "eat", "who": "eater", "name": "Order food and groceries",
     "why": "Uber Eats, paid by card, wallet or Uber Cash, with the restaurant paid out.",
     "steps": [("5.1", "app", "Open Uber Eats"), ("4.2", "delivery", "Order"), ("2.7", "ubercash", "Pay with Uber Cash"),
               ("4.2", "merchants", "Restaurant is settled")]},
    {"id": "earn", "who": "earner", "name": "Get paid after every trip",
     "why": "Earnings land on the Mastercard Uber Pro Card in seconds, with fuel cash back by tier.",
     "steps": [("5.1", "driverapp", "Finish a trip"), ("2.4", "mcmove", "Paid out on Mastercard Move"), ("2.5", "procardus", "Land on the Uber Pro Card"),
               ("3.2", "easysavings", "Earn extra at Easy Savings pumps"), ("3.2", "backup", "Fall back on Backup Balance")]},
    {"id": "ukearner", "who": "earner", "name": "Bank with Uber in the UK",
     "why": "The UK Pro Card and Griffin savings, announced with Mastercard in July 2025.",
     "steps": [("2.5", "procarduk", "Open the UK Pro Card"), ("3.2", "savings", "Save at up to 3.30% AER"), ("2.5", "onecred", "Pay with One Credential")]},
    {"id": "member", "who": "member", "name": "Get more from Uber One",
     "why": "Membership, Amex Uber Cash and Mastercard offers on top.",
     "steps": [("3.1", "uberone", "Join Uber One"), ("2.6", "amex", "Collect Amex Uber Cash"), ("3.1", "mcoffers", "Use Mastercard offers")]},
    {"id": "brazil", "who": "rider", "name": "Pay without a card",
     "why": "Pix in Brazil, UPI in India, wallets and cash where cards are scarce.",
     "steps": [("2.3", "pix", "Pay by Pix"), ("2.3", "localpay", "Or UPI and WeChat Pay"), ("2.1", "cash", "Or cash")]},
    {"id": "biz", "who": "biz", "name": "Run rides and meals for staff",
     "why": "Uber for Business with monthly billing and expense tools.",
     "steps": [("4.4", "u4b", "Set up Uber for Business"), ("2.7", "giftcards", "Send vouchers and gift cards"), ("5.3", "integrations", "Sync to the expense tool")]},
    {"id": "freight", "who": "shipper", "name": "Move freight",
     "why": "Uber Freight in North America and Europe.",
     "steps": [("4.3", "freight", "Book a load"), ("1.4", "deals", "Backed by Transplace")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The Uber Pro Card in three countries, Move payouts, Gateway collections, Offers and Easy Savings, and acceptance everywhere.",
     "steps": [("2.5", "procardus", "Uber Pro Card on Mastercard"), ("2.4", "mcmove", "Payouts on Mastercard Move"),
               ("2.2", "mcgateway", "Collections on Mastercard Gateway"), ("3.1", "mcoffers", "Offers for cardholders"),
               ("2.1", "accept", "Mastercard accepted everywhere")]},
    {"id": "mcnext", "who": "mc", "name": "Where an Uber One card, B2B and Delivery Hero could land",
     "why": "Where Uber has needs and Mastercard is not yet in: a card for 50 million Uber One members, tokens and billing updates for subscriptions, commercial cards for Uber for Business, cash conversion and payouts in more markets, and Delivery Hero's payments.",
     "steps": [("2.6", "onecard", "An Uber One card"), ("3.1", "uberone", "Billing updates for Uber One"), ("4.4", "u4b", "Virtual cards for Uber for Business"),
               ("2.1", "cash", "Convert cash markets"), ("1.4", "deliveryhero", "Delivery Hero's payments")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Uber's map",
    "title": "Mastercard pays Uber's drivers; Amex rewards its riders",
    "lead": "Mastercard is Uber's earner network: the Uber Pro Card is a Mastercard in the US, Canada and the UK, and the July 2025 agreement added Mastercard Move for payouts, One Credential, Gateway for collections and Offers for cardholders. On the consumer side every network is accepted through Adyen, American Express holds the richest US benefit, the Visa co-brand with Barclays has lapsed, and Pix, UPI, wallets and cash take a share. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Uber's own (Q2 2026 results, 5 August 2026; FY2025 10-K) or from Uber's product pages, Mastercard's July 2025 release (through trade coverage) and press. Uber does not publish a network split or Move's share of payouts.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Earner card (US)", "Mastercard", "Uber Pro Card, Evolve and Branch"],
        ["Earner card (UK)", "Mastercard", "Transact Payments and Griffin, 2025"],
        ["Payouts", "Mastercard Move", "July 2025; any debit card too"],
        ["Collections", "Adyen; Mastercard Gateway", "Adyen since 2012"],
        ["Consumer co-brand", "None", "Barclays Visa lapsed ⚠"],
        ["Premium benefit", "American Express", "Up to $200 Uber Cash"],
        ["Brazil", "Pix", "EBANX, since 2020"],
        ["Cash", "About 6% of bookings", "2025"],
    ],
    "sides": {
        "neo": {"dir": "The Uber Pro Card in the US, Canada and the UK, Move for payouts, One Credential, Gateway for collections, Offers and Easy Savings, and acceptance in every market.",
                "deals": "What it does not do: a consumer co-brand, Uber One benefits, commercial cards for Uber for Business or agentic payments."},
        "snb": {"dir": "American Express Uber Cash, the lapsed Visa co-brand and Green Dot debit card, Adyen as processor, Pix, UPI, WeChat Pay, PayPal, Apple Pay and cash.",
                "deals": "Where they meet: every card checkout, Instant Pay to any debit card, and the next Uber card."},
    },
    "tl": [
        ["2012", "Adyen starts processing for Uber"],
        ["Oct 2017", "Uber Visa co-brand with Barclays; Visa card push in Nigeria and Kenya"],
        ["Oct 2019", "Uber Money with a Green Dot Visa debit card"],
        ["Nov 2020", "Pix in Brazil with EBANX"],
        ["Dec 2022", "Uber Pro Card on Mastercard with Branch and Evolve"],
        ["Jul 2025", "Mastercard and Uber: Move, One Credential, Gateway, Offers, UK Pro Card"],
        ["Dec 2025", "Uber kiosks on Adyen terminals"],
        ["Feb 2026", "Adyen adds local acquiring, Pix, Afterpay, WeChat Pay"],
        ["May 2026", "Uber One reaches 50 million members"],
        ["Jul 2026", "Offer for Delivery Hero"],
    ],
    "l": {
        "U": {"d": 1, "s": "Earners carry Mastercard; riders carry anything.",
              "gap": "Drivers and couriers are paid onto the Mastercard Pro Card; riders and Uber One members pay with any card, and Amex rewards them most.",
              "neo": "Pro Card holders, Mastercard cardholders using Offers.", "snb": "Amex Platinum and Gold holders, Pix and UPI users, cash riders."},
        "L5": {"d": 0, "s": "The front doors are Uber's.", "gap": "The apps, kiosks and mini-program are Uber's; kiosks take any card on Adyen terminals.",
               "neo": "None.", "snb": "Apps, Adyen kiosks, WeChat, expense partners."},
        "L4": {"d": 1, "s": "Every line takes Mastercard; none is built on it.", "gap": "Mobility, Delivery and Uber for Business accept every network; restaurant payouts and Freight have no Mastercard role found.",
               "neo": "Acceptance in rides and delivery.", "snb": "Freight, Uber Health, Waymo."},
        "L3": {"d": 1, "s": "Offers and Easy Savings run on Mastercard.", "gap": "Mastercard Offers and Easy Savings sit in the earner and cardholder benefits; Uber One and fraud tools are Uber's own.",
               "neo": "Offers, Easy Savings, Backup Balance on the Pro Card.", "snb": "Uber One, advertising, risk controls."},
        "L2": {"d": 1, "s": "Mastercard runs earner money; consumer rails are mixed.", "gap": "Pro Card, Move, One Credential and Gateway are Mastercard; Adyen, Amex, Pix, UPI, wallets and cash carry the rest.",
               "neo": "Pro Card, Move, One Credential, Gateway.", "snb": "Adyen, Amex Uber Cash, Pix, UPI, PayPal, cash."},
        "L1": {"d": 0, "s": "Uber's own scale and entities.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Bookings, leadership, e-money licences, deals."},
    },
    "t": area_lens(LAYERS),
}
