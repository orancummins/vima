"""ING Groep's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from ing_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A mobile-first Dutch bank in ten retail markets as five discs that stack into one platform, from more than 41 "
       "million customers and a 13% CET1 ratio at the bottom to the apps, InsideBusiness and a Madrid flagship at the "
       "top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it "
       "light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep "
       "Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("home", "Homebuyers", "house"),
    ("aff", "Private banking & wealth clients", "gem"),
    ("sme", "Business Banking clients", "briefcase"),
    ("corp", "Wholesale clients", "factory"),
]
USERS_DESC = ("Five kinds of customer, more than 41 million in all: everyday customers in ten retail markets, homebuyers, "
              "private banking and wealth clients, Business Banking clients and the corporates and institutions Wholesale "
              "Banking serves.")

WHO = {"con": "An ING customer", "home": "A homebuyer", "aff": "A private banking client", "sme": "A business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day in the Netherlands",
     "why": "The everyday loop at ING Netherlands: an account, a new Visa or Mastercard debit card, the app, iDEAL becoming Wero, and AI monitoring.",
     "steps": [("4.1", "retail", "Open an account"), ("2.1", "nldebit", "Get a new debit card"), ("5.1", "apps", "Run it in the app"),
               ("2.6", "ideal", "Pay online with iDEAL, then Wero"), ("3.2", "monitoring", "Protected by AI monitoring")]},
    {"id": "belgium", "who": "con", "name": "Bank day to day in Belgium",
     "why": "Bancontact and Debit Mastercard, Wero and a chatbot.",
     "steps": [("2.2", "bedebit", "Pay with Bancontact and Debit Mastercard"), ("2.6", "wero", "Pay friends and shops with Wero"), ("3.3", "chatbots", "Ask the chatbot")]},
    {"id": "germany", "who": "con", "name": "Bank day to day in Germany",
     "why": "Visa debit with the Girokonto, Wero and, soon, a first credit card.",
     "steps": [("2.3", "dedebit", "Pay with the VISA Card"), ("2.3", "girocard", "Add a girocard"), ("2.6", "wero", "Shop online with Wero"),
               ("2.3", "decredit", "Take ING's first German credit card")]},
    {"id": "agent", "who": "con", "name": "Let an AI agent shop for you",
     "why": "ING's agentic pilot with Mastercard and Worldline, and the principles it signed.",
     "steps": [("3.1", "agentpilot", "Buy tickets through an AI assistant"), ("3.1", "principles", "Stay in control"), ("3.2", "monitoring", "Checked for fraud")]},
    {"id": "home", "who": "home", "name": "Buy and improve a home",
     "why": "Agentic mortgage decisions and ING Upgrader.",
     "steps": [("3.3", "mortgageai", "Get a fast mortgage decision"), ("4.1", "retail", "Take the mortgage"), ("4.1", "upgrader", "Retrofit with ING Upgrader")]},
    {"id": "wealth", "who": "aff", "name": "Grow your wealth",
     "why": "Private banking spreading to Italy and Spain, and a Madrid flagship.",
     "steps": [("4.3", "wealth", "Bank with ING Private Banking"), ("5.2", "branches", "Meet at the Madrid flagship"), ("2.7", "cryptoetp", "Add crypto ETPs")]},
    {"id": "sme", "who": "sme", "name": "Run a business",
     "why": "Business Banking, card acceptance and Wero.",
     "steps": [("4.2", "business", "Open a business account"), ("2.5", "roacquiring", "Take card payments"), ("2.6", "wero", "Accept Wero online"), ("5.1", "apps", "Run it in the app")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Wholesale Banking, cash management and Qivalis.",
     "steps": [("4.4", "wholesale", "Bank with Wholesale Banking"), ("2.7", "pcm", "Pool cash and pay"), ("2.7", "qivalis", "Settle in a euro stablecoin"),
               ("5.1", "insidebusiness", "Run it in InsideBusiness")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Belgian debit, part of the Dutch reissue, Polish cards and the agentic pilot.",
     "steps": [("2.2", "bedebit", "Debit Mastercard in Belgium"), ("2.1", "nldebit", "Part of the Dutch reissue"),
               ("2.4", "plcredit", "Platinum Mastercard in Poland"), ("2.4", "plpay", "Click to Pay in Poland"), ("3.1", "agentpilot", "The agentic pilot")]},
    {"id": "mcnext", "who": "mc", "name": "Where Germany's credit card and agents could land",
     "why": "Where ING has needs and Mastercard is not yet in: the German credit card's network, a bigger share of Dutch debit, card benefits in the plans, agents in production, fraud across Wero, business cards and Qivalis.",
     "steps": [("2.3", "decredit", "The German credit card's network"), ("2.1", "nldebit", "More of the Dutch reissue"), ("3.4", "subs", "Card benefits in the plans"),
               ("3.1", "agentpilot", "Agent Pay in production"), ("3.2", "monitoring", "Fraud tools across Wero"), ("4.2", "business", "Commercial cards in Italy and Spain"),
               ("2.7", "qivalis", "Multi-token settlement for Qivalis")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across ING's map",
    "title": "A dual-sourced bank, with Wero rising beside both networks",
    "lead": "ING has split Dutch debit between two networks since 2018, and its reissue of about 10 million cards from November 2025 goes to Visa and Mastercard in shares it does not disclose. Belgium carries Debit Mastercard beside Bancontact; Germany is Visa; Poland is mixed. Mastercard and Worldline ran ING's first agentic payment in June 2026. Meanwhile ING co-owns EPI and is taking Wero into online shopping in Belgium, Germany and, by end-2027, the Netherlands. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (2Q2026 results, 30 July 2026) or from ING, its product pages and press. The Mastercard newsroom was blocked, so nothing here comes from Mastercard's side; card networks in Spain, Italy, Romania and Australia, and for Dutch and Belgian credit cards, were not found.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["NL debit", "Visa and Mastercard", "About 10 million cards; split undisclosed ⚠"],
        ["BE debit", "Mastercard", "With Bancontact, since 2023"],
        ["DE debit", "Visa", "Free with the Girokonto"],
        ["DE credit", "Undecided", "First card planned for 2026"],
        ["Poland", "Visa and Mastercard", "Platinum on Mastercard"],
        ["Agentic", "Mastercard and Worldline", "Pilot, June 2026"],
        ["Wero", "EPI", "ING is a shareholder"],
        ["Stablecoin", "Qivalis", "Licensed 14 October 2026"],
    ],
    "sides": {
        "neo": {"dir": "Belgian debit, part of Dutch debit, Polish Platinum, euro and prepaid cards, Click to Pay in Poland, and the agentic pilot.",
                "deals": "What it does not do: German debit, Wero and iDEAL, Qivalis, ING's own AI and fraud models."},
        "snb": {"dir": "Visa for German and Polish debit and half the Dutch reissue, Bancontact, girocard and BLIK, Wero, Qivalis and ING's own AI.",
                "deals": "Where they meet: Dutch debit and Polish credit, where ING uses both networks."},
    },
    "tl": [
        ["Apr 2018", "Dutch debit split between Maestro and V PAY"],
        ["May 2023", "Belgium moves from Maestro to Debit Mastercard"],
        ["Nov 2024", "Wero in Belgium"],
        ["Nov 2025", "New Visa and Mastercard debit cards in the Netherlands"],
        ["Jun 2026", "Agentic payment with Mastercard and Worldline"],
        ["Jun 2026", "Wero online shopping in Germany"],
        ["Sep 2026", "Agentic commerce principles"],
        ["Oct 2026", "Qivalis licensed"],
        ["End-2027", "iDEAL fully migrated to Wero"],
    ],
    "l": {
        "U": {"d": 1, "s": "Belgian and some Dutch and Polish customers carry Mastercard.",
              "gap": "Belgians carry Debit Mastercard and the Dutch get one network or the other; Germans carry Visa.",
              "neo": "Belgian debit holders, part of Dutch debit, Polish Platinum holders.", "snb": "German and most Polish debit holders, wealth and wholesale clients."},
        "L5": {"d": 0, "s": "The front doors are ING's.", "gap": "Apps, InsideBusiness, branches and contact centres are the group's.", "neo": "None.", "snb": "Apps, portals, branches, contact centres."},
        "L4": {"d": 1, "s": "Retail banking carries a mix of cards.", "gap": "Retail accounts carry Mastercard in Belgium and part of the Netherlands; Business Banking card data is not public; wealth and wholesale have no network role.",
               "neo": "Cards inside retail banking.", "snb": "Mortgages, wealth, wholesale lending."},
        "L3": {"d": 1, "s": "The agentic pilot ran with Mastercard; the rest is ING's.", "gap": "Mastercard and Worldline ran the agentic payment; monitoring, chatbots and plans are ING's own.",
               "neo": "Agentic pilot.", "snb": "Monitoring, chatbots, mortgage AI, subscription plans."},
        "L2": {"d": 1, "s": "Two networks by design; Wero rising.", "gap": "Mastercard holds Belgian debit and shares Dutch and Polish cards; Visa holds Germany; Wero and Qivalis sit outside the card schemes.",
               "neo": "Belgian debit, Dutch and Polish cards.", "snb": "Visa debit, Wero, iDEAL, Qivalis, cash management."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, heritage, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
