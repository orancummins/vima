"""Rabobank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from rabobank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A Dutch cooperative bank and global food & agri lender as five discs that stack into one platform, from "
       "€639 billion of assets and a 20% CET1 ratio at the bottom to the Rabo App, 78 local banks and partners at the "
       "top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it "
       "light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep "
       "Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("home", "Homebuyers", "house"),
    ("sme", "SMEs & self-employed", "briefcase"),
    ("aff", "Private banking clients", "gem"),
    ("farm", "Farmers & food businesses", "earth"),
    ("corp", "Wholesale clients", "factory"),
]
USERS_DESC = ("Six kinds of customer: more than 9 million private and business customers in the Netherlands, among them "
              "homebuyers, 800,000 SMEs and 350,000 self-employed, private banking clients, farmers and food businesses "
              "in the Netherlands and abroad, and the 19,000-plus clients of Wholesale & Rural.")

WHO = {"con": "A Rabobank customer", "home": "A homebuyer", "sme": "A small business", "aff": "A private banking client",
       "farm": "A farmer", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a payment package, a Debit Mastercard or Visa Debit card, the Rabo App, iDEAL becoming Wero, and fraud checks.",
     "steps": [("4.1", "packages", "Open a payment package"), ("2.1", "debit", "Pay with a Mastercard or Visa debit card"),
               ("2.1", "wallets", "Add it to Apple Pay or Google Pay"), ("5.1", "app", "Run it in the Rabo App"),
               ("2.4", "ideal", "Pay online with iDEAL, then Wero"), ("3.2", "fraud", "Protected by fraud checks")]},
    {"id": "credit", "who": "con", "name": "Borrow and spend on credit",
     "why": "A GoldCard for travel and big purchases, and Freo for loans.",
     "steps": [("2.2", "credit", "Add a Rabo GoldCard"), ("4.1", "consumercredit", "Borrow with Freo"), ("3.4", "personal", "Get tips in the app")]},
    {"id": "agent", "who": "con", "name": "Let an AI agent pay for you",
     "why": "The May 2026 pilot: an agent books and pays on Mastercard Agent Pay, without seeing the card.",
     "steps": [("3.1", "agentpay", "Ask an AI agent to book"), ("2.1", "debit", "Pay with a tokenised card"), ("3.2", "fraud", "Checked for fraud")]},
    {"id": "home", "who": "home", "name": "Buy and improve a home",
     "why": "The largest Dutch mortgage lender, through local banks and Obvion.",
     "steps": [("5.2", "localbanks", "Talk to the local bank"), ("4.1", "mortgages", "Take a mortgage"), ("4.5", "bpd", "Buy a new-build home")]},
    {"id": "sme", "who": "sme", "name": "Run a shop or a business",
     "why": "A business account, cards, Smart Pay acceptance and Wero.",
     "steps": [("4.2", "sme", "Bank as an SME"), ("2.3", "bizcard", "Pay with a Rabo BusinessCard"), ("2.5", "smartpay", "Manage takings in Smart Pay"),
               ("2.5", "taptopay", "Take cards on a phone"), ("2.4", "wero", "Accept Wero online"), ("3.3", "identity", "Verify customers by API")]},
    {"id": "wealth", "who": "aff", "name": "Grow your wealth",
     "why": "Private Banking and Rabo Investments.",
     "steps": [("4.2", "private", "Bank with Private Banking"), ("5.1", "app", "Follow it in the app")]},
    {"id": "farm", "who": "farm", "name": "Finance a farm abroad",
     "why": "Rural banking in Australia, New Zealand, North America and Brazil, with DLL for machinery.",
     "steps": [("4.3", "rural", "Borrow from Rabobank's rural bank"), ("4.4", "dll", "Lease machinery through DLL"), ("4.3", "onlinesavings", "Save online in Australia or New Zealand")]},
    {"id": "corp", "who": "corp", "name": "Move money as a food & agri corporate",
     "why": "Wholesale & Rural, the business portal and a euro stablecoin.",
     "steps": [("4.3", "wholesale", "Bank with Wholesale & Rural"), ("5.3", "partners", "Run it in Rabo Business Banking"), ("2.7", "qivalis", "Settle in a euro stablecoin")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Part of debit, the GoldCard on request, business cards, Maestro until it goes, card acceptance and the agent pilot.",
     "steps": [("2.1", "debit", "Debit Mastercard, beside Visa Debit"), ("2.1", "maestro", "Maestro until replaced"), ("2.2", "credit", "Mastercard on request"),
               ("2.3", "bizcard", "BusinessCard on Mastercard"), ("2.5", "smartpin", "Mastercard accepted at SmartPin"), ("3.1", "agentpay", "Agent Pay pilot")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, debit share and agri cards could land",
     "why": "Where Rabobank has needs and Mastercard is not yet in: agents in production, more of each debit reissue, fraud and identity for instant payments and Wero, cards for food & agri clients and DLL, personal insights, and token settlement.",
     "steps": [("3.1", "agentpay", "Agent Pay in production"), ("2.1", "debit", "A bigger share of debit reissues"), ("3.2", "fraud", "Scam and identity scores for instant payments"),
               ("4.3", "wholesale", "Commercial cards for food & agri chains"), ("4.4", "dll", "Cards and carbon data in DLL programmes"),
               ("3.4", "personal", "Spend insights and offers in the app"), ("2.7", "qivalis", "Multi-token settlement beside Qivalis")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Rabobank's map",
    "title": "Debit shared with Visa, iDEAL turning into Wero, and Mastercard's first Dutch agent payment",
    "lead": "Rabobank moved off Maestro by issuing Debit Mastercard and Visa Debit side by side from 2022, in shares it does not disclose. Its GoldCard has been Visa by default since 2020, with Mastercard on request, and business cards come on either network. In May 2026 Mastercard and Rabobank ran the first AI-agent payment in the Netherlands on Agent Pay. Online, iDEAL carries most payments and is becoming Wero, which Rabobank builds with EPI; abroad, the food & agri bank lends without cards. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 results, 4 August 2026; FY2025, 10 February 2026) or from Rabobank's product pages and Dutch trade press. Rabobank's sites block direct fetches and the Mastercard and Visa newsrooms were not reached, so network splits and contract terms are not public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Mastercard and Visa", "Side by side since 2022; split undisclosed ⚠"],
        ["Maestro", "Mastercard", "Being replaced on expiry"],
        ["GoldCard", "Visa by default", "Mastercard on request, since 2020"],
        ["BusinessCard", "Visa or Mastercard", "Split undisclosed ⚠"],
        ["Agent payment", "Mastercard Agent Pay", "First in the Netherlands, May 2026"],
        ["Online", "iDEAL to Wero", "iDEAL ends end-2027"],
        ["Fraud", "INFORM RiskShield", "More than 15 years"],
        ["Stablecoin", "Qivalis", "Joined May 2026"],
    ],
    "sides": {
        "neo": {"dir": "Part of debit and Maestro until it goes, credit and business cards on request or by choice, card acceptance at Smart Pay merchants, and the Agent Pay pilot.",
                "deals": "What it does not do: iDEAL and Wero, fraud and identity, Qivalis, the food & agri bank abroad, DLL."},
        "snb": {"dir": "Visa for the other half of debit and the GoldCard default, EPI's Wero, INFORM fraud models, iDIN and itsme, AEVI and dejamobile for acceptance, and Qivalis.",
                "deals": "Where they meet: every debit and credit reissue, where Rabobank chooses between the two networks."},
    },
    "tl": [
        ["Feb 2015", "First Dutch NFC phone payments at the till"],
        ["Apr 2020", "Credit cards reissued; GoldCard defaults to Visa"],
        ["Feb 2022", "First online Debit Mastercard payment"],
        ["Mar 2022", "Visa Debit announced alongside"],
        ["Jun 2024", "Debit Mastercard rollout replaces Maestro"],
        ["Jan 2026", "iDEAL | Wero logo live"],
        ["May 2026", "First Dutch AI-agent payment on Mastercard Agent Pay"],
        ["May 2026", "Joins Qivalis"],
        ["Aug 2026", "Up to €2 billion for data, IT and AI"],
        ["End-2027", "iDEAL switched off for Wero"],
    ],
    "l": {
        "U": {"d": 1, "s": "Some cardholders carry Mastercard, others Visa.",
              "gap": "Debit holders get one network or the other; GoldCard holders mostly Visa; farmers abroad have no Rabobank card.",
              "neo": "Debit Mastercard holders, Maestro holders, Mastercard GoldCard and BusinessCard holders.", "snb": "Visa Debit and Visa GoldCard holders, farmers and corporates abroad."},
        "L5": {"d": 0, "s": "The front doors are Rabobank's.", "gap": "The app, local banks, intermediaries and the business portal are the bank's own.", "neo": "None.", "snb": "Rabo App, local banks, partners."},
        "L4": {"d": 0, "s": "The business lines carry a mix of cards or none.", "gap": "Accounts and SME banking carry cards on both networks; mortgages, food & agri, DLL and property have no network role.",
               "neo": "Cards inside accounts and SME banking.", "snb": "Mortgages, Freo, Private Banking, W&R, DLL, BPD."},
        "L3": {"d": 1, "s": "The agent pilot ran on Mastercard; the rest is Rabobank's.", "gap": "Agent Pay ran the May 2026 pilot; fraud is INFORM, identity is iDIN and itsme, personalisation is in-house.",
               "neo": "Agent Pay pilot.", "snb": "INFORM, Rabo Identity Services, app personalisation."},
        "L2": {"d": 1, "s": "Two networks on cards; Wero rising.", "gap": "Mastercard shares debit, credit and business cards with Visa; iDEAL, Wero, state payments and Qivalis sit outside the card schemes.",
               "neo": "Debit Mastercard, Maestro, Mastercard credit and business cards, card acceptance.", "snb": "Visa Debit, Visa GoldCard, iDEAL and Wero, Qivalis."},
        "L1": {"d": 0, "s": "The cooperative's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, cooperative, heritage, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
