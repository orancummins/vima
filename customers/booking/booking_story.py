"""Booking Holdings' kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from booking_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The world's largest online travel group, read through payments, as five discs that stack into one platform, from "
       "$186.1 billion of gross bookings at the bottom to the apps, ChatGPT and partners' sites at the top. Click the stack "
       "to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("trav", "Travellers", "user-round"),
    ("genius", "Genius members", "gift"),
    ("prop", "Hotels & hosts", "building-2"),
    ("rest", "Restaurants & diners", "store"),
    ("partner", "Banks & distribution partners", "landmark"),
    ("biz", "Business travellers", "briefcase-business"),
]
USERS_DESC = ("Six kinds of user: travellers in 220+ countries, Genius members, the hotels and hosts behind 31 million "
              "listings who are paid by Booking, restaurants and diners on OpenTable, the banks and airlines that "
              "distribute Booking's inventory, and business travellers.")

WHO = {"trav": "A traveller", "genius": "A Genius member", "prop": "A hotel or host", "rest": "A restaurant or diner",
       "partner": "A bank or airline partner", "biz": "A business traveller"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "stay", "who": "trav", "name": "Book and pay for a stay",
     "why": "The everyday loop: the app, a property, Booking.com as merchant of record, and instalments if wanted.",
     "steps": [("5.1", "apps", "Open the app"), ("4.1", "stays", "Choose a stay"), ("2.1", "mor", "Pay Booking.com by card"),
               ("2.5", "affirm", "Or spread it with Affirm")]},
    {"id": "trip", "who": "trav", "name": "Build a connected trip",
     "why": "Flights, a car and attractions around the stay, with Genius benefits across them.",
     "steps": [("4.2", "flights", "Add a flight"), ("4.2", "cars", "Add a car"), ("4.2", "attractions", "Add attractions"),
               ("3.1", "genius", "Use Genius discounts")]},
    {"id": "ai", "who": "trav", "name": "Plan with AI",
     "why": "Start in ChatGPT or the AI planner, finish on Booking.com.",
     "steps": [("5.2", "chatgpt", "Ask in ChatGPT"), ("3.3", "tripplanner", "Refine with the Trip Planner"),
               ("3.3", "aiagents", "Get help from an AI agent"), ("2.1", "mor", "Pay on Booking.com")]},
    {"id": "getpaid", "who": "prop", "name": "Get paid for a booking",
     "why": "A property chooses how Booking.com pays it: a virtual card per booking, bank transfer or Stripe.",
     "steps": [("3.4", "connapi", "Set payouts through the API"), ("2.2", "vcc", "Charge the virtual card"),
               ("2.2", "banktransfer", "Or take a bank transfer"), ("5.3", "extranet", "Reconcile in the extranet")]},
    {"id": "asia", "who": "trav", "name": "Travel with Agoda in Asia",
     "why": "Agoda bookings with the KTC card, card instalments and bank points.",
     "steps": [("4.4", "agoda", "Book on Agoda"), ("2.4", "ktcagoda", "Pay with the KTC–Agoda Mastercard"),
               ("2.5", "agodavisa", "Or split it with Visa instalments"), ("3.2", "agodaredeem", "Pay with bank points")]},
    {"id": "priceline", "who": "trav", "name": "Save with Priceline",
     "why": "Priceline deals and its Visa co-brand.",
     "steps": [("4.3", "priceline", "Find an Express Deal"), ("2.4", "pricelinevisa", "Earn 5x with the Priceline Visa")]},
    {"id": "dine", "who": "rest", "name": "Book a table",
     "why": "OpenTable's reservations, with Visa's dining collection for some cardholders.",
     "steps": [("4.6", "opentable", "Reserve on OpenTable"), ("3.2", "visadining", "Unlock a Visa Dining table")]},
    {"id": "distribute", "who": "partner", "name": "Sell Booking's stays to my customers",
     "why": "Banks and airlines put Booking's inventory inside their own loyalty.",
     "steps": [("5.4", "airindia", "Sell stays on an airline's site"), ("3.2", "agodaredeem", "Offer Agoda in bank rewards")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Virtual cards that pay hotels for Booking.com and Agoda, the KTC–Agoda card, Agoda in Mastercard's redemption suite, and acceptance on every booking.",
     "steps": [("2.3", "mcvcc", "Mastercard Virtual Cards for Pay by Booking"), ("2.3", "agodab2b", "Agoda B2B payments"),
               ("2.4", "ktcagoda", "KTC–Agoda Mastercard"), ("3.2", "agodaredeem", "Agoda redemptions for banks"),
               ("2.1", "accept", "Mastercard accepted at checkout")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, tokens and payouts could land",
     "why": "Where Booking has needs and Mastercard is not yet in: Agent Pay for bookings made in ChatGPT, Click to Pay and tokens on $130 billion of merchant bookings, Move for bank payouts, a Genius card, and redemption beyond Agoda.",
     "steps": [("5.2", "chatgpt", "Agent Pay for bookings made by AI"), ("2.1", "mor", "Click to Pay and tokens at checkout"),
               ("2.2", "banktransfer", "Mastercard Move for property payouts"), ("2.4", "bookingcard", "A Genius co-brand"),
               ("3.4", "trust", "Fraud and identity tools")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Booking Holdings' map",
    "title": "Mastercard pays the hotels; Visa holds the cards travellers carry",
    "lead": "Mastercard's place at Booking Holdings is in the plumbing: virtual cards that pay properties for Booking.com (since January 2024) and Agoda (since 2023), and Agoda's ties with Asian banks through the KTC card and Mastercard's redemption suite. Visa holds the consumer programmes in North America, the Priceline co-brand and OpenTable's dining collection, and Agoda's instalments. Affirm, Stripe and JCB have their own deals. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Booking Holdings' own (Q2 2026 results, 4 August 2026; FY2025 10-K) or from Mastercard, Visa, Affirm, KTC, Booking.com's developer docs and press. Booking does not publish a network split. The virtual-card network rests on an integrator page and Mastercard's 2024 release; the issuer is not public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Property payouts", "Mastercard virtual cards ⚠", "Pay by Booking, January 2024"],
        ["Agoda B2B", "Mastercard", "Virtual cards, 2023"],
        ["Priceline co-brand", "Visa", "Barclays"],
        ["Agoda card (Thailand)", "Mastercard", "KTC, since March 2022"],
        ["Agoda instalments", "Visa", "HSBC Malaysia first, 2022"],
        ["OpenTable perks", "Visa", "Dining Collection, 2024; renewed 2026 ⚠"],
        ["Bank redemptions", "Mastercard", "Agoda in Global Redemption Suite, 2026"],
        ["Pay later", "Affirm", "Booking.com since September 2023"],
    ],
    "sides": {
        "neo": {"dir": "Virtual cards that pay hotels for Booking.com and Agoda, the KTC–Agoda card, Agoda in Mastercard's redemption suite, and acceptance on every booking.",
                "deals": "What it does not do: the Priceline or OpenTable card perks, instalments, agentic checkout, tokens or Click to Pay at Booking.com."},
        "snb": {"dir": "Visa's Priceline co-brand, Agoda instalments and OpenTable dining collection, Affirm across four brands, Stripe payouts for US and Canadian homes, bank transfers, and JCB at Agoda.",
                "deals": "Where they meet: every guest checkout, and payouts to 4.4 million properties."},
    },
    "tl": [
        ["Mar 2022", "KTC–Agoda Mastercard launched in Thailand"],
        ["May 2022", "Agoda and Visa launch card instalments"],
        ["Sep 2022", "Priceline VIP Rewards Visa with Barclays"],
        ["Jun 2023", "Booking.com AI Trip Planner on OpenAI"],
        ["Sep 2023", "Affirm at Booking.com"],
        ["2023", "Mastercard and Agoda: B2B virtual cards"],
        ["Jan 2024", "Mastercard and Booking.com: virtual cards for Pay by Booking"],
        ["May 2024", "EU names Booking a DMA gatekeeper"],
        ["Jul 2024", "OpenTable & Visa Dining Collection; Spain's €413m fine"],
        ["Nov 2025", "JCB and Agoda agreement"],
        ["Jan 2026", "Agoda in Mastercard's Global Redemption Suite"],
        ["Feb 2026", "FY2025: $186.1bn booked, 70% merchant"],
        ["May 2026", "Car rentals in the Booking.com app in ChatGPT"],
        ["Aug 2026", "Q2 2026: merchant bookings +14.5%"],
    ],
    "l": {
        "U": {"d": 1, "s": "Hotels are paid on Mastercard; travellers' Booking cards are Visa.",
              "gap": "Properties paid by virtual card take Mastercard; Thai Agoda card holders carry it; Priceline card holders and OpenTable's Visa diners do not.",
              "neo": "Properties paid by virtual card, KTC–Agoda card holders, bank customers redeeming on Agoda.", "snb": "Priceline Visa holders, Visa Infinite diners, Affirm users, Stripe-paid hosts."},
        "L5": {"d": 0, "s": "The front doors are Booking's, OpenAI's and partners'.", "gap": "Apps, ChatGPT and Air India's site carry no Mastercard role; the extranet shows virtual-card payouts.",
               "neo": "Virtual-card payouts in the extranet.", "snb": "Apps, ChatGPT, Air India, UEFA."},
        "L4": {"d": 1, "s": "Every line takes Mastercard; none is built on it.", "gap": "Stays, flights, cars, Priceline and Agoda accept every network; KAYAK and OpenTable earn from ads and software.",
               "neo": "Card acceptance across the brands.", "snb": "KAYAK ads, OpenTable software, business travel."},
        "L3": {"d": 1, "s": "Mastercard in Agoda's bank loyalty; Visa at OpenTable.", "gap": "Agoda sits in Mastercard's redemption suite; Visa runs OpenTable's perks and JCB has Agoda offers; AI tools name no network.",
               "neo": "Agoda in the Global Redemption Suite.", "snb": "Visa Dining Collection, JCB offers, Genius, AI planners."},
        "L2": {"d": 2, "s": "Mastercard pays the hotels; Visa and Affirm finance the guests.", "gap": "Virtual cards for Booking.com and Agoda payouts are Mastercard; Priceline's card and Agoda instalments are Visa; Affirm, Stripe and bank transfers are off the networks.",
               "neo": "Pay by Booking virtual cards, Agoda B2B, KTC–Agoda card, acceptance.", "snb": "Priceline Visa, Agoda Visa instalments, Affirm, Stripe, bank transfers."},
        "L1": {"d": 0, "s": "Booking's own scale, licences and regulators.", "gap": "Nothing in the foundation is Mastercard's; BHFS holds Booking's own payment licences.", "neo": "None.", "snb": "Results, leadership, BHFS licences, regulation."},
    },
    "t": area_lens(LAYERS),
}
