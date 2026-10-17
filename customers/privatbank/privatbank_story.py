"""PrivatBank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from privatbank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Ukraine's largest bank as five discs that stack into one platform, from UAH 925 billion of assets and a state "
       "owner at the bottom to Privat24, 1,000 branches and cards posted to 60 countries at the top. Click the stack to "
       "open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Young people & gamers", "graduation-cap"),
    ("abroad", "Ukrainians abroad", "plane"),
    ("benef", "Pensioners & state-payment recipients", "hand-coins"),
    ("sme", "Entrepreneurs & small firms", "briefcase"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer, 18 million individuals and 950,000 businesses in all: everyday customers, young "
              "people and gamers, Ukrainians living abroad, pensioners and people receiving state payments, "
              "entrepreneurs and small firms, and the corporates whose loans quadrupled in 2025.")

WHO = {"con": "A PrivatBank customer", "young": "A young gamer", "abroad": "A Ukrainian abroad",
       "benef": "A state-payment recipient", "sme": "An entrepreneur", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Visa or Mastercard card, Privat24, Pryvit cashback and AI transfer limits.",
     "steps": [("4.1", "deposits", "Open an account"), ("2.1", "debit", "Pay with a Visa or Mastercard card"), ("5.1", "p24app", "Run it in Privat24"),
               ("3.3", "pryvit", "Collect Pryvit cashback"), ("3.1", "p2pai", "Protected by AI transfer limits")]},
    {"id": "credit", "who": "con", "name": "Borrow and pay over time",
     "why": "The Universal credit card, Payment in Parts and the new paid subscription.",
     "steps": [("2.2", "universal", "Take a Universal card"), ("2.5", "parts", "Split a purchase into parts"), ("3.3", "subs", "Upgrade to Privat PRO")]},
    {"id": "gamer", "who": "young", "name": "Game and pay",
     "why": "Katka24 on Visa with NAVI, a phone wallet and split bills.",
     "steps": [("2.2", "katka", "Get a Katka24 card"), ("2.3", "wallets", "Add it to a phone wallet"), ("2.6", "rtp", "Split a bill with Request to Pay")]},
    {"id": "abroad", "who": "abroad", "name": "Send money home from abroad",
     "why": "Cards posted to 60 countries, Mastercard cross-border transfers, PrivatMoney and remittance networks.",
     "steps": [("5.4", "delivery", "Get a card posted abroad"), ("2.6", "p2pintl", "Send from a Mastercard currency card"),
               ("2.6", "pmoney", "Or use PrivatMoney"), ("2.6", "remit", "Or Ria and Western Union")]},
    {"id": "benef", "who": "benef", "name": "Receive state and aid payments",
     "why": "Diia.Card, UNHCR aid and a payout card, with branches for those who need them.",
     "steps": [("4.5", "diia", "Open a Diia.Card"), ("4.5", "unhcr", "Receive humanitarian aid"), ("2.1", "debit", "Spend on a payout card"),
               ("5.3", "branches", "Get help at a branch")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Privat24 for Business, phone and online acceptance, instalments and AI tools.",
     "steps": [("5.2", "p24biz", "Open an account online"), ("2.4", "terminal", "Take cards on a phone"), ("2.4", "liqpay", "Sell online with LiqPay"),
               ("2.5", "instbiz", "Pay over time"), ("3.2", "aibiz", "Let AI draft payments")]},
    {"id": "corp", "who": "corp", "name": "Finance a corporate",
     "why": "Corporate loans backed by IFI risk-sharing, and acquiring for the shop floor.",
     "steps": [("4.3", "corp", "Borrow for energy or defence"), ("1.4", "ifi", "Backed by EBRD risk-sharing"), ("2.4", "pos", "Take cards at the till")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Half the card base, cross-border P2P, card delivery abroad, community programmes and Agent Pay.",
     "steps": [("2.1", "debit", "Mastercard debit and payout cards"), ("2.2", "universal", "Mastercard credit cards ⚠"),
               ("2.6", "p2pintl", "Cross-border P2P on Mastercard"), ("5.4", "delivery", "Free delivery abroad"),
               ("3.4", "community", "Superhumans and business schools"), ("3.2", "agentpay", "Agent Pay")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, offers and acceptance could land",
     "why": "Where PrivatBank has needs and Mastercard is not yet in: scaling Agent Pay, offers for Pryvit and Subscriptions, identity and scam tools, scheme instalments, phone acceptance and commercial cards.",
     "steps": [("3.2", "agentpay", "Scale Agent Pay in Privat24"), ("3.3", "pryvit", "Card-linked offers"), ("3.1", "docfraud", "Identity and scam scoring"),
               ("2.5", "parts", "Instalments at checkout"), ("2.4", "terminal", "Tap on Phone for Terminal merchants"), ("4.3", "corp", "Commercial cards")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across PrivatBank's map",
    "title": "Europe's biggest card issuer, split between two networks",
    "lead": "PrivatBank holds about 32 million active cards, more than half of Ukraine's, and issues Visa and Mastercard side by side without publishing a split. Nationally the two are level: Visa leads on cards in circulation since 2025 and Mastercard on active cards. Visa has the premium flagship, the gamer card and a run of firsts; Mastercard has cross-border P2P, card delivery abroad and, since June 2026, Ukraine's first Agent Pay payment. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (H1 2026 results, 27 July 2026; 2025 financial statements) or from NBU data via Interfax, Visa, Mastercard and press. Mastercard's newsroom could not be read directly; card-product networks are inferred where the bank's pages do not name them.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Active cards", "Visa & Mastercard", "About 32m, 54% of Ukraine ⚠"],
        ["Market split", "Level", "Visa 50.4% of cards, Mastercard 50.3% of active (Apr 2025)"],
        ["Premium", "Visa Infinite", "Flagship card"],
        ["Cross-border P2P", "Mastercard", "Sending only from Mastercard cards"],
        ["Agentic", "Mastercard Agent Pay", "Ukraine's first, June 2026"],
        ["Firsts with Visa", "DAF, Request to Pay", "2023, 2025"],
        ["Scheme fees", "UAH 21.7bn paid", "2025, to international payment systems"],
    ],
    "sides": {
        "neo": {"dir": "Roughly half the card base, cross-border P2P sending, card delivery abroad, transfer campaigns, community programmes and Agent Pay.",
                "deals": "What it does not do: premium, the gamer card, authentication, Request to Pay, Pryvit or instalments."},
        "snb": {"dir": "Visa on the other half of the cards plus premium, Katka24, DAF and Request to Pay; PROSTIR, PrivatMoney, SEP instant and the bank's own instalments and loyalty.",
                "deals": "Where they meet: every debit and credit card, where the customer picks the network."},
    },
    "tl": [
        ["2006", "Joins Visa (March) and Mastercard (July)"],
        ["Dec 2016", "Nationalised"],
        ["May 2018", "First Apple Pay bank in Ukraine, both networks"],
        ["Sep 2019", "FacePay24 with Visa"],
        ["Aug 2023", "Visa Digital Authentication Framework"],
        ["Jul 2025", "Nilson: Europe's largest Visa and Mastercard issuer"],
        ["Sep 2025", "Free card delivery abroad with Mastercard"],
        ["Dec 2025", "Visa and NAVI gamer ecosystem"],
        ["Jun 2026", "Mastercard Agent Pay, a first in Ukraine"],
        ["Sep 2026", "Subscriptions launched"],
    ],
    "l": {
        "U": {"d": 1, "s": "About half of cardholders carry Mastercard ⚠.",
              "gap": "Customers choose the network; Ukrainians abroad lean on Mastercard to send money home.",
              "neo": "Mastercard cardholders, cross-border senders.", "snb": "Visa cardholders, premium and gamer customers, PROSTIR users."},
        "L5": {"d": 1, "s": "Cards posted abroad with Mastercard; the rest is the bank's.", "gap": "Privat24 and branches are the bank's own; free delivery runs with both networks ⚠.",
               "neo": "Free delivery abroad.", "snb": "Privat24, branches, payment partners."},
        "L4": {"d": 1, "s": "Accounts come with cards on either network.", "gap": "Corporate, investment and state-payment lines have no visible Mastercard role.",
               "neo": "Cards on retail accounts.", "snb": "Corporate loans, bonds, Diia.Card ⚠, UNHCR payments."},
        "L3": {"d": 1, "s": "Agent Pay is Mastercard's own; the rest is the bank's or Visa's.", "gap": "Fraud, loyalty and subscriptions run without Mastercard; Visa has DAF and FacePay24.",
               "neo": "Agent Pay, community programmes.", "snb": "AI limits, Visa DAF, Pryvit, Subscriptions."},
        "L2": {"d": 1, "s": "Half the cards and cross-border P2P on Mastercard.", "gap": "Visa leads premium, gamer and Request to Pay; instalments, PrivatMoney and SEP are network-free.",
               "neo": "Debit and credit cards, cross-border P2P, acceptance.", "snb": "Visa cards and premium, PROSTIR, PrivatMoney, SEP, instalments."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, state owner, technology, IFIs."},
    },
    "t": area_lens(LAYERS),
}
