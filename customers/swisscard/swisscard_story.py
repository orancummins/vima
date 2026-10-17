"""Swisscard AECS's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from swisscard_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Switzerland's three-network card issuer as five discs that stack into one platform, from American Express "
       "ownership and a 1998 card platform at the bottom to the Swisscard app, SWISS and private banks at the top. Click "
       "the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across "
       "the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday cardholders", "user-round"),
    ("trav", "Frequent flyers", "plane"),
    ("prem", "Premium members", "gem"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "building-2"),
    ("pb", "Private-bank clients", "landmark"),
    ("merch", "Merchants", "store"),
]
USERS_DESC = ("Seven kinds of customer: everyday cardholders on free cards, SWISS frequent flyers, Platinum and Centurion "
              "members, small businesses, corporates, private-bank clients and the merchants that take American Express. "
              "Swisscard does not publish how many there are; its app has more than 400,000 users.")

WHO = {"con": "A cardholder", "trav": "A frequent flyer", "prem": "A Platinum member", "sme": "A small business",
       "corp": "A corporate treasurer", "pb": "A private-bank client", "merch": "A merchant"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Get a free card in minutes",
     "why": "The swisscard Visa card: apply in the app, pay at once from the phone, approve online payments with 3-D Secure.",
     "steps": [("5.1", "app", "Apply in the Swisscard app"), ("2.3", "sccard", "Get the swisscard Visa card"),
               ("2.7", "wallets", "Pay with Apple Pay or Google Pay"), ("3.1", "threeds", "Approve online payments")]},
    {"id": "cashback", "who": "con", "name": "Earn money back",
     "why": "Two free duos: Cashback Cards with a Mastercard or Visa, and poinz Cards with a Visa.",
     "steps": [("2.3", "cashback", "Take the Cashback Cards"), ("2.3", "poinz", "Or the poinz Cards"),
               ("4.1", "instalment", "Spread a big month"), ("2.7", "c2p", "Check out with Click to Pay")]},
    {"id": "fly", "who": "trav", "name": "Fly with SWISS",
     "why": "SWISS Miles & More duos: Amex plus a Mastercard or Visa, with travel insurance and Priceless.",
     "steps": [("2.2", "mm", "Choose a Miles & More duo"), ("3.2", "mr", "Earn and spend miles"),
               ("3.4", "insurance", "Travel insured"), ("3.2", "priceless", "Book Priceless experiences")]},
    {"id": "premium", "who": "prem", "name": "Live the Platinum life",
     "why": "American Express Platinum and Centurion with dining, shopping and service.",
     "steps": [("2.1", "amexcards", "Hold a Platinum card"), ("3.2", "selects", "Dine with Caminada, shop at Globus"),
               ("3.2", "mr", "Pay with points"), ("3.5", "service", "Call service at any hour")]},
    {"id": "sme", "who": "sme", "name": "Equip a small business",
     "why": "Mastercard business cards with the firm's logo, or a SWISS SME package.",
     "steps": [("4.2", "bizline", "Open a business account online"), ("2.4", "mcbiz", "Issue Mastercard business cards"),
               ("3.3", "picture", "Add the company logo"), ("2.4", "smepkg", "Earn miles with a SWISS SME package")]},
    {"id": "corp", "who": "corp", "name": "Control corporate spending",
     "why": "Amex corporate and supplier payments, Mastercard data feeds and the company portal.",
     "steps": [("2.4", "amexcorp", "Issue Amex corporate cards"), ("2.5", "supplier", "Pay suppliers with vPayment"),
               ("3.3", "sdg2", "Feed Mastercard data to expenses"), ("5.3", "portals", "Manage cards online")]},
    {"id": "pb", "who": "pb", "name": "Pay as a private-bank client",
     "why": "Cards that private banks hand to wealth clients, in francs, euros or dollars.",
     "steps": [("5.2", "partners", "Apply through the bank"), ("4.3", "wmc", "Hold a World Mastercard"),
               ("4.3", "wmcfx", "Spend in EUR or USD"), ("4.3", "pbamex", "Add an Amex Platinum")]},
    {"id": "merch", "who": "merch", "name": "Accept American Express",
     "why": "Swisscard signs Swiss merchants for Amex and markets them to cardmembers.",
     "steps": [("2.6", "acceptance", "Sign up for Amex acceptance"), ("4.4", "merchline", "Get marketing support"),
               ("5.3", "portals", "Reconcile in the merchant portal")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The business range, World Mastercards for private banks, the second card in two duos, SDG2 data and Priceless.",
     "steps": [("2.4", "mcbiz", "Mastercard business cards"), ("4.3", "wmc", "World Mastercard for private banks"),
               ("2.2", "mm", "Miles & More Mastercard option"), ("2.3", "cashback", "Cashback Mastercard option"),
               ("3.3", "sdg2", "SDG2 data"), ("3.2", "priceless", "Priceless Cities")]},
    {"id": "mcnext", "who": "mc", "name": "Where the second card, scams and agents could land",
     "why": "Where Swisscard has needs and Mastercard is not yet in: the free-card and poinz slots that went to Visa, scam protection, virtual supplier cards, Click to Pay enrolment and agentic payments.",
     "steps": [("2.3", "sccard", "A Mastercard option on the free card"), ("2.3", "poinz", "The poinz companion card"),
               ("3.1", "phishing", "Scam and identity tools"), ("2.5", "supplier", "Virtual cards against vPayment"),
               ("2.7", "c2p", "Click to Pay through the app"), ("1.4", "tech", "Agent Pay")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Swisscard's map",
    "title": "Amex's Swiss issuer, with Mastercard as the second card",
    "lead": "American Express has owned all of Swisscard since January 2026, and every consumer offer leads with an Amex card. Mastercard carries the business and corporate range and the World Mastercards for private banks, and is one of two choices for the second card in the SWISS Miles & More and Cashback duos. The newest launches, poinz in 2022 and the free swisscard card in 2025, went to Visa, and the Credit Suisse cards left for UBS. Each area below is marked by how deep Mastercard goes in it.",
    "qnote": "Swisscard publishes no accounts or card counts. Networks come from Swisscard's product pages and brand sites, read on 17 October 2026; the launch date of the swisscard card rests on a consumer forum.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Owner", "American Express", "Sole owner since 21 January 2026"],
        ["Consumer cards", "Amex first", "Mastercard or Visa as the second card"],
        ["New free cards", "Visa", "poinz 2022, swisscard 2025 ⚠"],
        ["Business cards", "Mastercard and Amex", "Standard, Gold, Euro, Dollar"],
        ["Private banks", "World Mastercard", "CHF, EUR and USD"],
        ["Acceptance", "Amex only", "More than 149,000 points"],
        ["Leadership", "Guido Müller", "Mastercard Switzerland head 2012–17"],
    ],
    "sides": {
        "neo": {"dir": "Business and corporate Mastercards, World Mastercards for private banks, the Mastercard option in Miles & More and Cashback, SDG2 data, Priceless and Click to Pay.",
                "deals": "What it does not do: the Amex cards, supplier payments, acceptance, the poinz and swisscard cards, or rewards."},
        "snb": {"dir": "American Express owns the issuer, leads every consumer card and is the only network acquired; Visa takes the new free cards and shares the duos.",
                "deals": "Where they meet: the second card in each duo, and business cards."},
    },
    "tl": [
        ["1998", "Swisscard founded by Amex and Credit Suisse"],
        ["2010", "3-D Secure pilot for Mastercard and Visa"],
        ["2018", "Cashback Cards on Mastercard or Visa; Swatch Pay"],
        ["Jan 2021", "Ex-Mastercard Switzerland head becomes CEO"],
        ["2022", "poinz Cards on Amex and Visa"],
        ["Jun 2024", "Joint venture not renewed"],
        ["Oct 2024", "Amex agrees to buy UBS's half"],
        ["2025", "swisscard free card on Visa ⚠"],
        ["Jan 2026", "Amex sole owner; Credit Suisse cards at UBS"],
    ],
    "l": {
        "U": {"d": 1, "s": "Business cardholders and some duo holders carry Mastercard.",
              "gap": "Every consumer holds an Amex; Mastercard reaches companies, private-bank clients and duo holders who choose it.",
              "neo": "Business cardholders, private-bank clients, some Miles & More and Cashback holders.", "snb": "Amex members, poinz and swisscard holders, merchants."},
        "L5": {"d": 0, "s": "The front doors are Swisscard's and its partners'.", "gap": "App, SWISS, poinz and private banks.", "neo": "None.", "snb": "App, partners, portals."},
        "L4": {"d": 1, "s": "Mastercard in business and private-bank lines.", "gap": "Private customers lead with Amex; merchants are Amex-only.",
               "neo": "Business range, World Mastercards.", "snb": "Amex cards, merchant services."},
        "L3": {"d": 1, "s": "SDG2 and Priceless are Mastercard's; the rest is Amex or Swisscard.", "gap": "Rewards and lifestyle are Amex's; no public fraud partner.",
               "neo": "SDG2, Picture Card, Priceless.", "snb": "Membership Rewards, Selects, service, insurance."},
        "L2": {"d": 1, "s": "Business cards on Mastercard; consumer cards Amex first.", "gap": "Mastercard shares the duos with Visa and has lost the newest launches to it.",
               "neo": "Business cards, duo option, wallets, Click to Pay.", "snb": "Amex cards, Visa free cards, Amex acceptance and supplier payments."},
        "L1": {"d": 0, "s": "Owned and rated through American Express.", "gap": "Nothing in the foundation is Mastercard's, though the CEO once ran Mastercard Switzerland.", "neo": "None.", "snb": "Ownership, ratings, platform, strategy."},
    },
    "t": area_lens(LAYERS),
}
