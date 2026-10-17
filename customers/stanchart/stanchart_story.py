"""Standard Chartered's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from stanchart_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("An international bank for Asia, Africa and the Middle East as five discs that stack into one platform, from a "
       "$993 billion balance sheet across 55 markets at the bottom to SC Mobile, Straight2Bank and wealth hubs at the top. "
       "Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up "
       "across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("aff", "Affluent & private clients", "gem"),
    ("con", "Everyday customers", "user-round"),
    ("dig", "Digital-bank customers", "smartphone"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
    ("fi", "Financial institutions", "landmark"),
]
USERS_DESC = ("Six kinds of client: affluent and private clients, the growth engine; everyday customers in the markets the "
              "bank keeps; about 1.75 million Mox and Trust customers; small businesses; more than 17,000 corporate and "
              "institutional clients; and the banks, funds and digital-asset firms it serves.")

WHO = {"aff": "An affluent client", "con": "A customer", "dig": "A Mox or Trust customer", "sme": "A small business",
       "corp": "A corporate treasurer", "fi": "A financial institution"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "wealth", "who": "aff", "name": "Grow wealth across borders",
     "why": "Priority banking, AI-assisted advice, a premium card and, in the UAE, crypto in the same account.",
     "steps": [("5.3", "branches", "Meet a relationship manager in a wealth hub"), ("4.1", "wealth", "Become a Priority client"),
               ("3.2", "wealthai", "Get advice through myWealth Advisor"), ("3.5", "cryptotrade", "Buy bitcoin in the UAE"),
               ("2.2", "sgmc", "Spend on a Beyond card")]},
    {"id": "everyday", "who": "con", "name": "Bank and spend day to day",
     "why": "An account, the app and a card whose network depends on the market.",
     "steps": [("4.2", "retail", "Open an account"), ("5.1", "scmobile", "Run it in SC Mobile"),
               ("2.1", "hkcathay", "Pay with a Cathay Mastercard in Hong Kong"), ("2.3", "mecards", "Or a Visa card in the UAE"),
               ("3.4", "rewards", "Earn miles")]},
    {"id": "digital", "who": "dig", "name": "Bank on a phone in Hong Kong",
     "why": "Mox: an account, Mox Credit on Mastercard and Asia Miles.",
     "steps": [("4.3", "mox", "Open a Mox account"), ("2.4", "moxcard", "Spend on Mox Credit"), ("5.4", "partners", "Earn Asia Miles with Cathay")]},
    {"id": "trustsg", "who": "dig", "name": "Bank with Trust in Singapore",
     "why": "Trust Bank with FairPrice, a Visa card and TrustInvest.",
     "steps": [("4.3", "trust", "Open a Trust account"), ("2.4", "trustcard", "Use the Trust card"), ("3.4", "agentic", "Try agentic payments")]},
    {"id": "sme", "who": "sme", "name": "Run a small business across borders",
     "why": "SME banking, Straight2Bank and cross-border payments.",
     "steps": [("4.2", "retail", "Open a business account"), ("5.2", "s2b", "Bank in Straight2Bank"),
               ("2.5", "payments", "Pay suppliers abroad"), ("2.3", "pkcards", "Use a business card in Pakistan")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Cash management, B2B rails, tokenised deposits and stablecoins.",
     "steps": [("4.4", "cib", "Bank with CIB"), ("3.3", "apis", "Connect by API"), ("2.5", "visab2b", "Pay through Visa B2B Connect"),
               ("2.6", "tokdep", "Move liquidity as tokenised deposits"), ("2.6", "stablecoins", "Settle in HKDAP or USDC")]},
    {"id": "fi", "who": "fi", "name": "Hold and trade digital assets",
     "why": "Custody, trading and stablecoin access for institutions.",
     "steps": [("4.4", "fss", "Use securities services"), ("3.5", "custody", "Hold crypto in custody"),
               ("3.5", "cryptotrade", "Trade bitcoin and ether"), ("2.6", "stablecoins", "Mint and redeem USDC")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Hong Kong's Cathay card, Mox Credit, half of Singapore, all of Pakistan, a tokenisation pilot and Send.",
     "steps": [("2.1", "hkcathay", "Cathay Mastercard in Hong Kong"), ("2.4", "moxcard", "Mox Credit"),
               ("2.2", "sgmc", "Beyond and Simply Cash in Singapore"), ("2.3", "pkcards", "Every card in Pakistan"),
               ("2.6", "mtn", "Multi-Token Network pilot"), ("2.5", "mcsend", "Send in the Middle East and Africa")]},
    {"id": "mcnext", "who": "mc", "name": "Where stablecoins, agents and wealth could land",
     "why": "Where Standard Chartered has needs and Mastercard is not yet in: stablecoin spend and settlement, agentic payments, affluent card experiences, cross-border corridors and Mox's growing Hong Kong book.",
     "steps": [("2.6", "stablecoins", "Stablecoin card spend and settlement"), ("3.4", "agentic", "Agent Pay against Visa's pilot"),
               ("4.1", "wealth", "World Legend and Priceless for affluent clients"), ("2.5", "payments", "Move for corridor payments"),
               ("4.3", "mox", "More Hong Kong spend through Mox"), ("2.3", "mecards", "Win back the UAE")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Standard Chartered's map",
    "title": "Mastercard in Hong Kong, Pakistan and Mox; Visa almost everywhere else",
    "lead": "Standard Chartered picks its card network market by market. Mastercard carries the Cathay co-brand in Hong Kong, Mox Credit, half of Singapore's range and every card in Pakistan under a 2023 exclusive. Visa carries the UAE, India, Kenya, Ghana and Trust Bank, and also has the B2B rail (2024) and the first agentic pilot (2026). The bank's fastest-moving work, in stablecoins and tokenised deposits, runs on its own rails and partners. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 results, 29 July 2026). Networks are read from the bank's local card pages on 17 October 2026; Trust Bank's network and India's are from secondary or partial sources. No group-wide network agreement is public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Hong Kong", "Cathay on Mastercard", "Smart and Simply Cash on Visa"],
        ["Singapore", "Split", "Beyond and Simply Cash Mastercard; Journey and Smart Visa"],
        ["Pakistan", "Mastercard", "Exclusive, renewed May 2023"],
        ["UAE, India, Africa", "Visa", "Card pages name Visa"],
        ["Mox / Trust", "Mastercard / Visa", "About 750,000 / over 1 million customers"],
        ["B2B", "Visa B2B Connect", "Settlement partner since 2024"],
        ["Agentic", "Visa Agentic Ready", "April 2026"],
        ["Digital money", "Own rails", "HKDAP, USDC, tokenised deposits"],
    ],
    "sides": {
        "neo": {"dir": "The Cathay card, Mox Credit, Singapore's Mastercard half, all of Pakistan, a 2024 tokenisation pilot and Send in the Middle East and Africa.",
                "deals": "What it does not do: the UAE, India, Africa and Trust cards, B2B rails, agentic tests or stablecoins."},
        "snb": {"dir": "Visa cards in most markets, Visa B2B Connect and Visa Agentic Ready; the bank's own tokenised deposits, HKDAP and USDC with Circle.",
                "deals": "Where they meet: Singapore, Hong Kong and Bangladesh, where both networks issue."},
    },
    "tl": [
        ["Oct 2017", "Mastercard Send for the Middle East and Africa"],
        ["Sep 2020", "Mox launches with a Mastercard card"],
        ["Jul 2021", "Cathay Mastercard range in Hong Kong"],
        ["May 2023", "Pakistan renews Mastercard as sole network"],
        ["Apr 2024", "Visa B2B Connect settlement partner"],
        ["May 2024", "Mastercard tokenisation pilot with Mox"],
        ["Apr 2026", "Visa Agentic Ready; HKDAP licence"],
        ["May 2026", "Mox takes part of the Hong Kong retail book"],
        ["Jul 2026", "USDC with Circle"],
        ["Oct 2026", "Crypto trading for UAE affluent clients"],
    ],
    "l": {
        "U": {"d": 1, "s": "Hong Kong, Mox, Pakistan and part of Singapore carry Mastercard.",
              "gap": "Most customers in the UAE, India and Africa, and Trust's, carry Visa; corporates and institutions use the bank's own rails.",
              "neo": "Cathay and Mox cardholders, Pakistan, Singapore's Mastercard half.", "snb": "UAE, India, Kenya, Ghana and Trust cardholders; corporates; institutions."},
        "L5": {"d": 0, "s": "The front doors are the bank's.", "gap": "Apps, Straight2Bank and branches are its own; the Cathay co-brand is the one partner on Mastercard.",
               "neo": "Cathay co-brand.", "snb": "SC Mobile, Straight2Bank, branches, FairPrice, Alipay+."},
        "L4": {"d": 1, "s": "Wealth and retail cards are split; CIB has no card role.", "gap": "Mox Credit is Mastercard and Trust Visa; premium cards split by market.",
               "neo": "Mox, part of wealth and retail cards.", "snb": "Trust, CIB, securities services."},
        "L3": {"d": 0, "s": "Services are the bank's own or Visa's.", "gap": "No Mastercard fraud, AI or agentic tool is public; Visa runs the agentic pilot.",
               "neo": "The Cathay rewards link.", "snb": "AI with Alibaba, BlackRock and Ant; Visa Agentic Ready; custody and trading."},
        "L2": {"d": 1, "s": "Cards split by market; payments and digital money are not Mastercard's.", "gap": "Mastercard has Hong Kong's flagship, Mox, Pakistan and half of Singapore; Visa has the rest and B2B.",
               "neo": "Cathay, Mox Credit, Pakistan, Singapore Mastercard cards, MTN pilot, Send.", "snb": "Visa cards, Visa B2B Connect, tokenised deposits, stablecoins."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, network, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
