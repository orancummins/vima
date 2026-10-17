"""Société Générale's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from socgen_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A Paris bank built on France, Czechia and Romania as five discs that stack into one platform, from €476 billion of loans "
       "at the bottom to L'Appli SG, BoursoBank, KB+ and about 1,400 branches at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in "
       "the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Young & online clients", "smartphone"),
    ("borrower", "Credit customers", "hand-coins"),
    ("driver", "Drivers & fleets", "plane"),
    ("saver", "Savers & private clients", "gem"),
    ("sme", "Professionals & small businesses", "briefcase"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Seven kinds of customer: everyday customers of the SG network, KB and BRD, BoursoBank's young online clients "
              "and teenagers, credit customers of CGI, Fiditalia and Hanseatic, Ayvens' drivers and fleets, savers and "
              "private clients, professionals and small businesses, and the corporates and institutions the investment bank serves.")

WHO = {"con": "An SG customer", "young": "A BoursoBank client", "borrower": "A borrower", "driver": "A driver",
       "saver": "A saver", "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day in France",
     "why": "The everyday loop at SG: an account, a CB Visa card, L'Appli SG, Wero and card security.",
     "steps": [("4.1", "sgnetwork", "Open an account at SG"), ("2.1", "sgcards", "Pay with a CB Visa card"), ("5.1", "sgapp", "Run it in L'Appli SG"),
               ("2.6", "wero", "Pay friends with Wero"), ("3.1", "security", "Protected by a dynamic CVV")]},
    {"id": "online", "who": "young", "name": "Bank online with BoursoBank",
     "why": "France's leading online bank: a free Visa, virtual cards, wallets, instant transfers and Wero by the end of 2026.",
     "steps": [("4.2", "bourso", "Open a BoursoBank account"), ("2.3", "boursocards", "Get a Visa Ultim"), ("5.3", "wallets", "Add it to Apple Pay"),
               ("2.6", "instant", "Send an instant transfer"), ("3.2", "aiops", "Get answers from AI")]},
    {"id": "teen", "who": "young", "name": "Give a teenager a card",
     "why": "Banxup, a Mastercard for 10–17s issued by Treezor, now owned by Shares.",
     "steps": [("2.3", "banxup", "Order a Banxup Mastercard"), ("5.1", "sgapp", "Set limits as a parent"), ("2.6", "wero", "Receive pocket money")]},
    {"id": "east", "who": "con", "name": "Bank in Czechia or Romania",
     "why": "KB's Visa debit in KB+ and World Elite credit; BRD's Mastercard-led range with Priceless.",
     "steps": [("4.5", "kb", "Bank with KB"), ("2.4", "kbcards", "Open a virtual Visa in KB+"), ("2.4", "kbwe", "Carry a World Elite"),
               ("2.4", "brdcards", "Or a BRD Mastercard"), ("3.3", "priceless", "Use Priceless benefits")]},
    {"id": "borrow", "who": "borrower", "name": "Borrow on a card",
     "why": "Consumer finance across France, Germany and Italy: Fiditalia on Mastercard, Hanseatic on Visa.",
     "steps": [("5.3", "partners", "Apply through a retailer"), ("4.6", "consumer", "Borrow from consumer finance"),
               ("2.5", "fiditalia", "Carry a Carta Bianca Mastercard"), ("2.5", "hanseatic", "Or a Hanseatic Visa")]},
    {"id": "drive", "who": "driver", "name": "Lease a car",
     "why": "Ayvens' 3.2 million vehicles and consumer finance for car buyers.",
     "steps": [("4.6", "ayvens", "Lease with Ayvens"), ("4.6", "consumer", "Or finance a car"), ("5.3", "partners", "Through BYD or Chery")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "SG professional cards, acceptance through PayXpert or BoursoBank with Stancer, and Wero.",
     "steps": [("2.2", "procards", "Pay with a CB Visa Business"), ("2.7", "payxpert", "Take payments with PayXpert"),
               ("2.7", "boursoenc", "Or Tap to Pay with BoursoBank"), ("2.6", "instant", "Get paid instantly")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Corporate cards on Visa and Mastercard, transaction banking and SG-Forge's stablecoins.",
     "steps": [("4.4", "financing", "Bank with SG CIB"), ("2.2", "corpmc", "Give staff Corporate Mastercards"),
               ("2.8", "gtps", "Run cash and trade with GTPS"), ("2.8", "forge", "Settle in EURCV")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "SG's corporate cards and Cirrus, BRD's Mastercard-led range with Priceless, KB's World Elite, Fiditalia and Banxup.",
     "steps": [("2.2", "corpmc", "Corporate Mastercard"), ("2.1", "cirrus", "Cirrus withdrawals"), ("2.4", "brdcards", "BRD cards"),
               ("3.3", "priceless", "Priceless at BRD and KB"), ("2.4", "kbwe", "KB World Elite"), ("2.5", "fiditalia", "Fiditalia")]},
    {"id": "mcnext", "who": "mc", "name": "Where corporates, the east and agents could land",
     "why": "Where SG has needs and Mastercard is thin: corporate and virtual cards, KB and BRD issuing, instalments, fraud on Wero and instant payments, agentic payments with SG's AI push, acquiring risk and Ayvens' fleet.",
     "steps": [("2.2", "corpmc", "Virtual and commercial cards"), ("2.4", "brdcards", "Tokens and offers at BRD"), ("2.4", "kbwe", "Click to Pay in KB+"),
               ("2.5", "fiditalia", "Instalments at Fiditalia"), ("2.6", "wero", "Fraud scores on instant payments"),
               ("1.3", "ai", "Agent Pay alongside Anthropic"), ("2.7", "payxpert", "Merchant risk for PayXpert"), ("4.6", "ayvens", "Fleet payments")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Société Générale's map",
    "title": "Visa holds French retail; Mastercard keeps corporates, Romania and premium credit",
    "lead": "SG's French retail and BoursoBank cards are Cartes Bancaires and Visa, and SG moved its last retail Mastercard holders to Visa in autumn 2025. Mastercard keeps SG's corporate cards and Cirrus, BRD's Mastercard-led range with Priceless, KB's World Elite and Fiditalia; Treezor, in which it held 5%, left the group on 6 October 2026. Meanwhile SG co-owns Wero. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (Q2 2026 results, 30 July 2026; Capital Markets Day, 21 September 2026; 2026 URD) or from SG, BoursoBank, KB, BRD and press pages. The Mastercard and Visa newsrooms were not reachable; Ayvens' fleet cards and KB's 4U and A cards were not verified.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["SG France retail", "CB and Visa", "Mastercard cards dropped Jun 2025"],
        ["BoursoBank", "Visa", "9.1 million clients"],
        ["SG corporates", "Visa and Mastercard", "Corporate and Executive Mastercard"],
        ["Romania (BRD)", "Mostly Mastercard", "Priceless on Gold and Platinum"],
        ["Czechia (KB)", "Visa debit", "Mastercard World Elite credit"],
        ["Consumer credit", "Split", "Fiditalia Mastercard, Hanseatic Visa"],
        ["Treezor", "Sold Oct 2026", "Mastercard held 5%"],
        ["Wallet", "Wero", "55 million users"],
    ],
    "sides": {
        "neo": {"dir": "SG corporate cards and Cirrus, BRD's cards and Priceless, KB World Elite, Fiditalia, and Banxup through Treezor.",
                "deals": "What it does not do: French retail and BoursoBank cards, KB debit, Hanseatic, Wero, SG-Forge or the group's AI."},
        "snb": {"dir": "Cartes Bancaires and Visa in France and at BoursoBank, Visa debit at KB and Hanseatic, Wero, SG-Forge's stablecoins and Anthropic's AI.",
                "deals": "Where they meet: corporate cards, where SG offers both Visa and Mastercard."},
    },
    "tl": [
        ["Sep 2019", "League of Legends Mastercard"],
        ["Jul 2021", "KB launches Mastercard World Elite"],
        ["2022", "Mastercard buys 5% of Treezor"],
        ["Oct 2024", "Wero replaces Paylib at SG"],
        ["Apr 2025", "Mastercard launches Agent Pay"],
        ["Jun 2025", "SG stops selling CB Mastercard"],
        ["Oct 2025", "SG Mastercard holders moved to Visa"],
        ["Mar 2026", "KB virtual Visa in KB+"],
        ["Sep 2026", "2029 roadmap and Anthropic deal"],
        ["Oct 2026", "Treezor sold to Shares"],
    ],
    "l": {
        "U": {"d": 1, "s": "Corporates and Romanians carry Mastercard.",
              "gap": "SG corporates, BRD cardholders, KB premium clients and Fiditalia borrowers carry Mastercard; French retail and BoursoBank customers carry Visa.",
              "neo": "Corporate cardholders, BRD, KB World Elite and Fiditalia customers, Banxup teens.", "snb": "SG and BoursoBank customers, savers, Hanseatic borrowers."},
        "L5": {"d": 0, "s": "The front doors are the group's.", "gap": "Apps, branches and partners are SG's; wallet token services are not stated.", "neo": "None in public view.", "snb": "L'Appli SG, BoursoBank, KB+, branches."},
        "L4": {"d": 1, "s": "Mastercard inside BRD, KB and consumer finance.", "gap": "BRD and KB carry Mastercard in part and Fiditalia wholly; the SG network, BoursoBank, private banking, CIB and Ayvens have no Mastercard role in view.",
               "neo": "BRD, KB premium credit, Fiditalia.", "snb": "SG network, BoursoBank, Ayvens, CIB."},
        "L3": {"d": 1, "s": "Priceless in the east; Visa perks at home.", "gap": "Priceless at BRD and KB and Identity Check at Fiditalia are Mastercard's; Visa Infinite and SmartDelay serve France; AI is Anthropic's.",
               "neo": "Priceless, Identity Check.", "snb": "Visa Infinite, SmartDelay, Anthropic."},
        "L2": {"d": 1, "s": "Visa and CB at home; Mastercard in corporates and the east; Wero rising.", "gap": "Mastercard carries SG corporate cards, Cirrus, BRD, KB World Elite, Fiditalia and Banxup; Visa and CB hold French retail and BoursoBank; Wero and stablecoins are outside the card schemes.",
               "neo": "Corporate Mastercard, Cirrus, BRD, KB World Elite, Fiditalia, Banxup.", "snb": "CB and Visa, BoursoBank Visa, Wero, EURCV."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, heritage, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
