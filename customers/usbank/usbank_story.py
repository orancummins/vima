"""U.S. Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from usbank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("America's fifth-largest commercial bank as five discs that stack into one platform, from $703 billion of assets "
       "at the bottom to the app, branches and partners at the top, with Elavon's acquiring and Elan's agent cards in the "
       "rails. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light "
       "up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes "
       "in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("sme", "Small businesses", "briefcase"),
    ("merch", "Merchants", "store"),
    ("corp", "Corporates & institutions", "factory"),
    ("fi", "Partner banks & credit unions", "landmark"),
    ("aff", "Wealth & advisory clients", "gem"),
]
USERS_DESC = ("Six kinds of customer among 15 million clients: everyday customers, more than 2 million small businesses, "
              "Elavon's 2 million merchants, corporates and institutions, the 1,300 banks and credit unions that issue Elan "
              "cards, and wealth and Edward Jones clients.")

WHO = {"con": "A U.S. Bank customer", "sme": "A small business", "merch": "A merchant", "corp": "A corporate treasurer",
       "fi": "A partner bank", "aff": "A wealth client"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a Bank Smartly account, a Visa debit card, the app and Protect 360.",
     "steps": [("4.1", "smartly", "Open a Bank Smartly account"), ("2.1", "debit", "Pay with Visa debit"),
               ("5.1", "app", "Run it in the app"), ("3.1", "protect", "Watch my identity with Protect 360")]},
    {"id": "card", "who": "con", "name": "Spend and pay over time",
     "why": "A Smartly Visa or the Split Mastercard, with subscriptions managed in the app.",
     "steps": [("2.2", "credit", "Take a Smartly Visa"), ("2.2", "split", "Or split every purchase with Split"),
               ("3.2", "subs", "Manage subscriptions"), ("3.3", "avvance", "Finance a big purchase")]},
    {"id": "amazon", "who": "sme", "name": "Buy for the business on Amazon",
     "why": "The Prime Business and Amazon Business Mastercard, with Spend Management built in.",
     "steps": [("2.3", "amazon", "Get the Amazon business card"), ("3.2", "spend", "Set limits and virtual cards"),
               ("4.2", "smallbiz", "Bank with U.S. Bank too")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Business Essentials checking and cards, Elavon acceptance, Zelle and instant payments.",
     "steps": [("4.2", "smallbiz", "Open Business Essentials"), ("2.4", "bizcards", "Take a Business Essentials card"),
               ("2.7", "elavonsmb", "Take cards with Elavon"), ("2.8", "enhanced", "Pay suppliers instantly")]},
    {"id": "merchant", "who": "merch", "name": "Take payments",
     "why": "Elavon in the US, Canada and Europe, with AI pricing and Paze at checkout.",
     "steps": [("1.4", "stat", "Get a price from Statement Analyzer"), ("2.7", "elavon", "Process with Elavon"),
               ("2.7", "paze", "Accept Paze online"), ("3.3", "avvance", "Offer Avvance financing")]},
    {"id": "agent", "who": "fi", "name": "Issue cards under my own name",
     "why": "Elan runs credit cards for more than 1,300 banks and credit unions.",
     "steps": [("5.3", "alliances", "Partner with Elan"), ("2.5", "elan", "Issue Elan agent cards")]},
    {"id": "corp", "who": "corp", "name": "Run corporate payments",
     "why": "Commercial and fleet cards, SinglePoint, freight and healthcare payments, and a stablecoin pilot.",
     "steps": [("4.3", "cib", "Bank with WCCIB"), ("2.6", "commcard", "Issue corporate and virtual cards"),
               ("2.6", "voyager", "Fuel the fleet with Voyager"), ("3.4", "singlepoint", "Forecast cash in SinglePoint"),
               ("2.8", "usbdc", "Settle cross-border with USBDC")]},
    {"id": "wealth", "who": "aff", "name": "Bank through my adviser",
     "why": "Edward Jones Everyday Solutions and U.S. Bank Wealth Management.",
     "steps": [("5.3", "alliances", "Open through Edward Jones"), ("2.3", "edwardjones", "Take an Edward Jones Mastercard"),
               ("4.4", "wealth", "Invest with U.S. Bank Wealth")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The partner cards: Amazon, Edward Jones, BMW and Split, plus Voyager, part of commercial cards and Ethoca's subscription tools.",
     "steps": [("2.3", "amazon", "Amazon business cards on Mastercard"), ("2.3", "edwardjones", "Edward Jones World Elite"),
               ("2.3", "bmw", "BMW Mastercard"), ("2.2", "split", "Split World Mastercard"),
               ("2.6", "voyager", "Voyager Mastercard"), ("3.2", "subs", "Subscriptions via Ethoca")]},
    {"id": "mcnext", "who": "mc", "name": "Where Elavon, agents and Elan could land",
     "why": "Where U.S. Bank has needs and Mastercard is not yet in: Elavon's acceptance stack, agentic buying on the Amazon cards, identity tools beside Protect 360, commercial virtual cards, stablecoin settlement and Elan's agent-bank network.",
     "steps": [("2.7", "elavon", "Click to Pay and merchant risk at Elavon"), ("2.3", "amazon", "Agent Pay for Amazon business buying"),
               ("3.1", "protect", "Identity and scam tools"), ("4.5", "industry", "Commercial virtual cards and B2B data"),
               ("2.8", "usbdc", "Token settlement beside USBDC"), ("2.5", "elan", "Elan's network choice")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across U.S. Bank's map",
    "title": "A Visa bank whose biggest new co-brand runs on Mastercard",
    "lead": "U.S. Bank's debit card, every bank-brand consumer credit card, its new Business Essentials cards and most of Elan's agent cards are Visa, and Kroger's co-brand is moving to Smartly Visa. Mastercard holds the partner cards: Amazon's small-business portfolio, taken from American Express in 2026, Edward Jones, BMW and the Split card, plus Voyager fleet and part of commercial cards; Ethoca runs subscription management. Elavon accepts every network. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are U.S. Bancorp's own (Q3 2026 results, 15 October 2026) or from U.S. Bank, Elavon, Elan, Amazon and press releases. Mastercard's and Visa's newsrooms were not searched; Elan's and commercial cards' network split, Kroger's earlier network and the date Business Altitude Connect moved to Visa are not confirmed.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "U.S. Bank Visa Debit"],
        ["Bank-brand credit", "Visa", "Smartly, Cash+, Altitude, Shield"],
        ["Small business", "Visa", "Business Essentials, Sep 2026"],
        ["Amazon business", "Mastercard", "From Amex; live May 2026"],
        ["Partner cards", "Mastercard", "Edward Jones, BMW, Split"],
        ["Elan", "Mostly Visa ⚠", "1,300+ banks and credit unions"],
        ["Acquiring", "Elavon", "All networks; fifth in the US"],
        ["Services", "Ethoca", "Subscription management, Oct 2025"],
    ],
    "sides": {
        "neo": {"dir": "The Amazon, Edward Jones and BMW co-brands, the Split card, Voyager Mastercard, part of commercial cards, Ethoca subscriptions, and acceptance at Elavon's merchants.",
                "deals": "What it does not do: debit, bank-brand consumer and small-business cards, most of Elan, Paze, Zelle, instalments or the stablecoin."},
        "snb": {"dir": "Visa debit and credit, the Business Essentials cards, most co-brands and Elan, Paze and Zelle, real-time payments, Avvance and USBDC.",
                "deals": "Where they meet: commercial cards on both networks and Elavon's acceptance of both."},
    },
    "tl": [
        ["Feb 2016", "First bank on Mastercard Business Network"],
        ["Apr 2018", "Mobile pay on Mastercard travel cards"],
        ["Aug 2021", "Voyager Mastercard fleet card"],
        ["Feb 2023", "Business Altitude Connect World Elite Mastercard"],
        ["Sep 2024", "Smartly Visa Signature; Paze"],
        ["Oct 2025", "Subscription management with Ethoca"],
        ["Nov 2025", "Edward Jones and Split Mastercards"],
        ["Mar 2026", "Amazon picks U.S. Bank and Mastercard"],
        ["Jul 2026", "Kroger card moving to Smartly Visa"],
        ["Aug 2026", "Amex Amazon accounts convert"],
        ["Sep 2026", "Business Essentials Visa; USBDC pilot"],
        ["Oct 2026", "BMW Mastercard relaunched"],
    ],
    "l": {
        "U": {"d": 1, "s": "Amazon, Edward Jones, BMW and Split cardholders carry Mastercard.",
              "gap": "Debit and bank-brand cardholders carry Visa; partner cardholders and many corporate cardholders carry Mastercard.",
              "neo": "Amazon business owners, Edward Jones and BMW clients, Split users, fleets.", "snb": "Debit holders, bank-brand card holders, Elan banks' customers, State Farm and AAA members."},
        "L5": {"d": 1, "s": "Edward Jones is a Mastercard channel; the rest is the bank's.", "gap": "The app and branches are U.S. Bank's; Edward Jones advisers sell Mastercards, State Farm agents sell Visa.",
               "neo": "Edward Jones cards.", "snb": "App, branches, State Farm, Elan."},
        "L4": {"d": 0, "s": "The business lines carry Visa cards.", "gap": "Accounts come with Visa debit and the small-business cards are Visa; corporate payments use both networks.",
               "neo": "Some commercial cards ⚠.", "snb": "Consumer and small-business banking, WCCIB, wealth."},
        "L3": {"d": 1, "s": "Ethoca runs subscriptions; the rest is the bank's.", "gap": "Subscription management is Mastercard's; Protect 360, Avvance and SinglePoint are U.S. Bank's or other partners'.",
               "neo": "Ethoca subscriptions and receipts.", "snb": "Protect 360, Avvance, ExtendPay, Kyriba, Booking.com."},
        "L2": {"d": 1, "s": "Mastercard on the partner cards; Visa on the bank's own.", "gap": "Visa has debit, bank-brand and small-business credit and most of Elan; Mastercard has Amazon, Edward Jones, BMW, Split and Voyager.",
               "neo": "Amazon, Edward Jones, BMW, Split, Voyager, part of commercial.", "snb": "Visa debit and credit, Elan, Paze, Zelle, USBDC."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, charter, deals, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
