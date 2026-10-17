"""Emirates NBD's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from emiratesnbd_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Dubai's biggest bank as five discs that stack into one platform, from a balance sheet above AED 1.3 trillion at the "
       "bottom to the ENBD X app, Liv and 1,425 branches at the top. Click the stack to open it. Choose who you are and "
       "what you want to do, and the areas that deliver it light up across the layers, joined in the order they act. "
       "Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("prem", "Priority & private clients", "gem"),
    ("dig", "Liv customers", "rocket"),
    ("isl", "Islamic banking customers", "landmark"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Six kinds of customer across 13 countries: everyday UAE customers, priority and private clients, Liv's "
              "half a million digital customers, Emirates Islamic's customers, small businesses and the corporates and "
              "institutions wholesale banking serves.")

WHO = {"con": "An Emirates NBD customer", "prem": "A priority client", "dig": "A Liv customer", "isl": "An Emirates Islamic customer",
       "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "An account, a Visa debit card, the ENBD X app, Aani transfers and fraud checks.",
     "steps": [("4.1", "retail", "Open an account"), ("2.1", "debit", "Pay with Visa debit"), ("5.1", "app", "Run it in ENBD X"),
               ("2.7", "aani", "Send money with Aani"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "The UAE's largest card book: Visa co-brands, Mastercard cards, rewards and instalments.",
     "steps": [("2.2", "visacc", "Take a Skywards or SHARE Visa card"), ("2.2", "mccc", "Or a LuLu or dnata Mastercard"),
               ("3.3", "rewards", "Collect points and miles"), ("3.3", "instalments", "Spread a purchase into instalments")]},
    {"id": "travel", "who": "prem", "name": "Travel on the bank",
     "why": "Voyager and Marriott Bonvoy on Mastercard, the AI Travel Assistant with Visa, and GlobalCash for currency.",
     "steps": [("3.2", "aitravel", "Plan a trip with the AI assistant"), ("2.3", "voyager", "Book on the Voyager portal"),
               ("2.3", "marriott", "Stay with a Marriott Bonvoy card"), ("2.4", "globalcash", "Carry currencies on GlobalCash")]},
    {"id": "digital", "who": "dig", "name": "Bank with Liv",
     "why": "A digital bank in three minutes: Visa debit, multicurrency, Liv credit cards and crypto.",
     "steps": [("5.2", "liv", "Open Liv on the phone"), ("2.1", "livdebit", "Spend with the Multicurrency Visa card"),
               ("2.2", "livcc", "Earn with a Tamayaz card"), ("2.8", "crypto", "Buy crypto with rewards")]},
    {"id": "domestic", "who": "con", "name": "Pay on UAE rails",
     "why": "The central bank's new rails, where Emirates NBD was first: Jaywan cards and Aani.",
     "steps": [("2.5", "jaywan", "Carry a Jaywan card"), ("2.7", "aani", "Pay by QR or phone number")]},
    {"id": "islamic", "who": "isl", "name": "Bank the Islamic way",
     "why": "Emirates Islamic, with AED 250 billion of Islamic assets in the group.",
     "steps": [("4.4", "islamic", "Bank with Emirates Islamic"), ("5.1", "app", "Use the digital channels")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Business Banking with a Visa Infinite debit card, Emirates NBD Pay on Mastercard Gateway, and corporate cards.",
     "steps": [("4.2", "sme", "Join VIP Privilege"), ("2.6", "enbdpay", "Take payments with Emirates NBD Pay"),
               ("2.4", "corpcards", "Give staff corporate cards"), ("5.1", "bizonline", "Run it on businessONLINE")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Wholesale banking, the DP World card, APIs, Visa settlement and a digital bond.",
     "steps": [("4.3", "cib", "Bank with wholesale"), ("2.4", "dpworld", "Pay suppliers on the DP World card"),
               ("3.4", "apis", "Connect by API"), ("2.8", "digitalbond", "Invest in the digital bond")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "A third of the credit cards, the travel cards, prepaid and corporate cards, Egypt, and the acquiring gateway.",
     "steps": [("2.2", "mccc", "Mastercard credit cards"), ("2.3", "voyager", "Voyager World Elite"), ("2.3", "marriott", "Marriott Bonvoy"),
               ("2.4", "dpworld", "DP World corporate card"), ("2.6", "enbdpay", "Gateway and Brighterion"), ("4.5", "egypt", "Emirates NBD Egypt")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, Jaywan and India could land",
     "why": "Where Emirates NBD has needs and Mastercard is not yet in: the AI assistant and agentic payments, Jaywan co-badging, issuer fraud tools, commercial virtual cards and RBL Bank in India.",
     "steps": [("3.2", "aitravel", "Agent Pay for the AI assistant"), ("2.5", "jaywan", "Co-badge Jaywan cards"),
               ("3.1", "fraud", "Issuer fraud and scam scoring"), ("2.4", "corpcards", "Virtual cards and spend controls"),
               ("4.5", "rbl", "Cards at RBL Bank")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Emirates NBD's map",
    "title": "A Visa bank that runs its travel cards and gateway on Mastercard",
    "lead": "Visa carries every Emirates NBD debit card, the biggest co-brands and, since April 2026, the bank's settlement of Visa's UAE domestic transactions. Mastercard carries about a third of the credit cards, including the bank's own Voyager travel card and Marriott Bonvoy, plus prepaid, corporate and Egyptian cards, and its Gateway and Brighterion run Emirates NBD Pay. Jaywan and Aani are the new domestic rails. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 results, 23 July 2026). Networks are read from the bank's card listings on 17 October 2026 and counted by product, not by spend; no network split by volume is published.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "All 16 cards; five-year deal, 2020"],
        ["Credit", "Visa and Mastercard", "About 21 Visa, 12 Mastercard of 35"],
        ["Travel", "Voyager, Marriott", "Mastercard World Elite, 2024–25"],
        ["Acquiring", "Emirates NBD Pay", "Mastercard Gateway and Brighterion, 2025"],
        ["Settlement", "Visa NNSS", "AED settlement agent, April 2026"],
        ["Domestic", "Jaywan and Aani", "First issuer; Aani launch bank"],
        ["Egypt", "Mastercard", "Partnership 2024; TMG co-brands"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard credit cards, Voyager and Marriott Bonvoy, GlobalCash, corporate and DP World cards, Liv credit ⚠, Egypt, and the Emirates NBD Pay gateway with Brighterion.",
                "deals": "What it does not do: debit, the flagship co-brands, domestic settlement, AI travel or Jaywan."},
        "snb": {"dir": "Visa debit and the Skywards, SHARE, Emaar and Etihad co-brands, Visa+ and NNSS settlement, the AI Travel Assistant, Jaywan and Aani, Diners Club.",
                "deals": "Where they meet: the credit-card book, corporate cards and Duo."},
    },
    "tl": [
        ["Jun 2020", "Visa partnership renewed for five years"],
        ["Oct 2023", "Aani launches with Emirates NBD"],
        ["Jan 2024", "Mastercard partnership in Egypt"],
        ["Mar 2024", "Marriott Bonvoy World Elite Mastercard"],
        ["Sep 2024", "DP World Mastercard corporate card"],
        ["Jan 2025", "First Jaywan debit cards"],
        ["Feb 2025", "Mastercard Gateway and Brighterion on Emirates NBD Pay"],
        ["Apr 2025", "Visa+ transfers"],
        ["Dec 2025", "Voyager Mastercard"],
        ["Apr 2026", "Visa settlement agent"],
        ["Jun 2026", "RBL Bank completed"],
        ["Oct 2026", "AI Travel Assistant with Visa"],
    ],
    "l": {
        "U": {"d": 1, "s": "Travel and retail cardholders carry Mastercard; everyone has Visa debit.",
              "gap": "Every account holder carries Visa debit; about a third of credit cards and the travel cards are Mastercard.",
              "neo": "Voyager, Marriott, LuLu and dnata cardholders, corporate cardholders, Liv credit ⚠.", "snb": "Debit holders, Skywards and SHARE cardholders, Jaywan holders."},
        "L5": {"d": 0, "s": "The front doors are the bank's.", "gap": "ENBD X, Liv and branches are its own; most big co-brand partners sit on Visa.",
               "neo": "Some co-brand partners.", "snb": "Apps, branches, the largest co-brands."},
        "L4": {"d": 0, "s": "The business lines carry Visa debit.", "gap": "Retail and SME accounts come with Visa; Egypt is the exception with Mastercard.",
               "neo": "Emirates NBD Egypt.", "snb": "Retail, SME, wholesale, Emirates Islamic, DenizBank, RBL."},
        "L3": {"d": 1, "s": "Rewards run on both networks; AI went to Visa.", "gap": "Rewards and instalments sit on both networks; the AI Travel Assistant was built with Visa; issuer fraud tools are not public.",
               "neo": "Rewards and instalments on Mastercard cards.", "snb": "AI Travel Assistant, contact-centre AI, APIs."},
        "L2": {"d": 1, "s": "Mastercard holds credit and acquiring; Visa holds debit and settlement.", "gap": "Visa has debit, the big co-brands and settlement; Mastercard has a third of credit, travel, prepaid, corporate and the gateway.",
               "neo": "Mastercard credit, Voyager, Marriott, GlobalCash, DP World, Emirates NBD Pay.", "snb": "Visa debit and co-brands, Visa+, NNSS, Jaywan, Aani."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, ownership, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
