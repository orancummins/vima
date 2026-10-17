"""Danske Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from danske_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Denmark's largest bank as five discs that stack into one platform, from DKK 1,794 billion of loans and Forward '28 "
       "at the bottom to Danske Mobile Banking, District and the advisers at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("priv", "Private Banking customers", "gem"),
    ("home", "Homebuyers", "house"),
    ("saver", "Savers & pension members", "coins"),
    ("sme", "Businesses", "briefcase"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Six kinds of customer across Denmark, Finland, Sweden, Norway (business only) and Northern Ireland: everyday "
              "customers, Private Banking clients, homebuyers, savers and Danica members, businesses and the corporates LC&I serves.")

WHO = {"con": "A Danske customer", "priv": "A Private Banking client", "home": "A homebuyer", "saver": "A saver",
       "sme": "A business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop in Denmark: an account, a Mastercard or Visa/Dankort debit card, a phone wallet, the app and card controls.",
     "steps": [("4.1", "personal", "Open an account"), ("2.1", "hverdag", "Pay with Mastercard Hverdag+"), ("2.5", "wallets", "Tap with a phone wallet"),
               ("5.1", "app", "Run it in the app"), ("3.1", "cardcontrols", "Lock the card to one continent")]},
    {"id": "card", "who": "con", "name": "Spend on a card and earn",
     "why": "Mastercard credit cards and cashback that works on Mastercard only.",
     "steps": [("2.2", "dkcredit", "Take a Mastercard Guld"), ("3.3", "cashback", "Earn cashback"), ("3.5", "assistant", "Ask the AI Assistant")]},
    {"id": "p2p", "who": "con", "name": "Pay a friend",
     "why": "MobilePay for person-to-person, or an instant bank transfer.",
     "steps": [("2.5", "mobilepay", "Send with MobilePay"), ("2.6", "instant", "Or send an instant transfer"), ("5.1", "app", "See it in the app")]},
    {"id": "home", "who": "home", "name": "Buy a first home",
     "why": "BoligStart advice and a Realkredit Danmark mortgage.",
     "steps": [("5.3", "branches", "Meet an adviser"), ("4.2", "boligstart", "Join BoligStart"), ("4.2", "mortgages", "Take a Realkredit loan")]},
    {"id": "wealth", "who": "priv", "name": "Grow wealth",
     "why": "Private Banking, a World Elite card, Danske Invest funds and a Danica pension, planned in Panorama.",
     "steps": [("4.3", "privatebanking", "Become a Private Banking client"), ("3.5", "panorama", "Plan in Panorama"),
               ("2.2", "worldelite", "Carry World Elite Mastercard"), ("4.3", "invest", "Invest in Danske Invest"), ("4.3", "danica", "Save in Danica")]},
    {"id": "sme", "who": "sme", "name": "Run a business",
     "why": "District, a business account, Mastercard business cards and Nordania vehicles.",
     "steps": [("5.2", "district", "Bank in District"), ("4.4", "business", "Borrow as a business"), ("2.4", "corpcards", "Give staff Mastercard cards"),
               ("4.4", "nordania", "Lease vans with Nordania")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "LC&I cash management, FX, APIs, supply chain finance and the coming euro stablecoin.",
     "steps": [("4.5", "lci", "Bank with LC&I"), ("3.4", "apis", "Connect by Premium APIs"), ("2.6", "fx", "Trade FX in DanskeFX"),
               ("2.6", "scf", "Pay suppliers early"), ("2.6", "qivalis", "Settle in Qivalis euros")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Credit, premium and Hverdag+ cards in Denmark, every card in Finland, Sweden and Northern Ireland, business cards and data, cashback, and the Agent Pay pilot.",
     "steps": [("2.2", "dkcredit", "Danish credit on Mastercard"), ("2.1", "hverdag", "Hverdag+ debit"), ("2.3", "ficards", "Finland, Sweden, UK cards"),
               ("2.4", "gdr", "Corporate card data"), ("3.3", "cashback", "Cashback on Mastercard"), ("3.2", "agentpay", "Agent Pay pilot")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, debit and open finance could land",
     "why": "Where Danske has needs and Mastercard is not yet in: the remaining Visa/Dankort base, agents for corporates, open finance, passkeys at scale and virtual cards.",
     "steps": [("2.1", "visadankort", "Move Visa/Dankort holders to Mastercard debit"), ("3.2", "mcp", "Agent Pay for corporate assistants"),
               ("3.4", "aiia", "Open finance and pay-by-bank"), ("3.1", "passkeys", "Passkeys for every card"), ("2.4", "corpcards", "Virtual cards for business")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Danske Bank's map",
    "title": "A Mastercard bank with one Visa/Dankort card left",
    "lead": "Mastercard carries Danske's Danish credit, premium and Hverdag+ debit cards, all its business cards, and every card it issues in Finland, Sweden and Northern Ireland. Visa shares only the co-badged Visa/Dankort debit card. Mastercard bought Aiia from Danske in 2021, and in September 2026 the two made Denmark's first AI-agent payment. Nets processes the cards, MobilePay owns person-to-person payments, and Danske co-founded a euro stablecoin. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 interim report, 17 July 2026) or from Danske's card pages, Nationalbanken and press. No Danske–Mastercard master agreement is public, and the split of Danish debit between Mastercard and Visa/Dankort is not disclosed.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Danish debit", "Mastercard and Visa/Dankort", "Hverdag+ can replace Visa/Dankort"],
        ["Danish credit", "Mastercard", "Basis, Guld, Platin, World Elite"],
        ["Finland, Sweden, UK", "Mastercard", "Debit and credit"],
        ["Business cards", "Mastercard", "Corporate, Business Debit, Travel Account"],
        ["Processing", "Nets (Nexi)", "Five-year deal, February 2019"],
        ["Agentic", "Agent Pay", "Denmark's first, September 2026"],
        ["Open banking", "Aiia", "Sold to Mastercard, 2021 ⚠ use today"],
        ["P2P", "MobilePay", "Danske holds about 28% ⚠"],
    ],
    "sides": {
        "neo": {"dir": "Credit and premium cards, Hverdag+ debit, business cards and data, all cards outside Denmark, cashback, Priceless, Agent Pay and passkeys.",
                "deals": "What it does not do: Visa/Dankort debit, card processing, MobilePay, instant transfers, the stablecoin, APIs or AI."},
        "snb": {"dir": "Visa and Dankort on the co-badged debit card, Nets for processing, MobilePay for P2P, Danske's own fraud tools, APIs and AI, and Qivalis.",
                "deals": "Where they meet: wallets and MobilePay, which carry whichever card sits beneath."},
    },
    "tl": [
        ["Feb 2019", "Direct Dankort deal and five-year Nets processing deal"],
        ["Jun 2021", "MobilePay to merge with Vipps and Pivo"],
        ["Sep 2021", "Aiia stake sold to Mastercard"],
        ["Nov 2024", "First bank with Dankort in Apple Pay"],
        ["Nov 2024", "Norway personal banking moves to Nordea"],
        ["Sep 2025", "Founding member of Qivalis"],
        ["Dec 2025", "US DOJ probation closed"],
        ["Apr 2026", "Forward '28 update and 2028 targets"],
        ["Jun 2026", "Nationalbanken: international cards overtake Dankort"],
        ["Sep 2026", "Denmark's first Agent Pay payment"],
    ],
    "l": {
        "U": {"d": 2, "s": "Most cardholders carry Mastercard.",
              "gap": "Outside the Visa/Dankort card, Danske's personal and business cardholders carry Mastercard in every market.",
              "neo": "Credit, premium, Hverdag+, business, Finland, Sweden and UK cardholders.", "snb": "Visa/Dankort holders, MobilePay users, mortgage and pension customers."},
        "L5": {"d": 0, "s": "The front doors are Danske's.", "gap": "The app, District and advisers are Danske's own.", "neo": "None.", "snb": "Danske Mobile Banking, District, branches, partners."},
        "L4": {"d": 1, "s": "Cards come with the accounts; the rest has no network role.", "gap": "Personal, business and Northern Ireland accounts carry Mastercard cards; mortgages, Danica and LC&I do not.",
               "neo": "Cards in personal, business, Private Banking and Northern Ireland.", "snb": "Realkredit, Danske Invest, Danica, LC&I, Nordania."},
        "L3": {"d": 1, "s": "Agent Pay, passkeys and Priceless are Mastercard's; the rest is Danske's.", "gap": "Agent Pay and passkeys are pilots; APIs, AI and card controls are Danske's own.",
               "neo": "Agent Pay, passkeys, Priceless, cashback on Mastercard, Aiia ⚠.", "snb": "Card controls, Premium APIs, MCP server, AI Assistant, Panorama."},
        "L2": {"d": 2, "s": "Most cards are Mastercard; Visa/Dankort and Nets remain.", "gap": "Mastercard has credit, business and all non-Danish cards; Visa/Dankort, Nets, MobilePay and instant transfers are not Mastercard.",
               "neo": "Hverdag+, credit and premium cards, Finland, Sweden, UK and business cards.", "snb": "Visa/Dankort, Nets processing, MobilePay, instant transfers, Qivalis."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, governance, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
