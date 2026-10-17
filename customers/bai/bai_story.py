"""Banco Angolano de Investimentos (BAI): kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bai_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Angola's largest bank as five discs that stack into one platform, from Kz 5.3 trillion of assets at the bottom "
       "to the BAI Directo app, branches, ATMs and banking agents at the top. Click the stack to open it. Choose who you "
       "are and what you want to do, and the areas that deliver it light up across the layers, joined in the order they "
       "act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("unb", "Newly banked & wallet users", "wallet"),
    ("trav", "Travellers & families abroad", "plane"),
    ("prem", "Affluent & Premium", "gem"),
    ("sme", "Small businesses & merchants", "store"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Six kinds of customer, about 3.1 million active in all: everyday customers, the newly banked reached through "
              "agents and the é-Kwanza wallet, travellers and families with relatives abroad, affluent and Premium clients, "
              "small businesses and merchants, and 3,251 corporates and institutions.")

WHO = {"con": "A BAI customer", "unb": "A newly banked customer", "trav": "A traveller", "prem": "A Premium client",
       "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Multicaixa debit card, the app, KWiK and QR payments, and BAI's own fraud defences.",
     "steps": [("4.1", "accounts", "Open a current account"), ("2.1", "mcxdebit", "Pay with Multicaixa debit"),
               ("5.1", "app", "Run it in BAI Directo"), ("2.7", "kwik", "Send money by KWiK"),
               ("2.7", "baipaga", "Pay by QR with BAI Paga"), ("3.1", "security", "Protected from fraud")]},
    {"id": "banked", "who": "unb", "name": "Get banked",
     "why": "Agents in shops, a simplified account, prepaid cards and the é-Kwanza wallet.",
     "steps": [("5.3", "agents", "Visit a banking agent"), ("4.1", "accounts", "Open a simplified account"),
               ("2.1", "mcxprepaid", "Get a Multicaixa card"), ("2.7", "ekwanza", "Use the é-Kwanza wallet")]},
    {"id": "abroad", "who": "trav", "name": "Pay abroad",
     "why": "The new multi-brand debit card on Mastercard, or a Kamba Visa prepaid card loaded in the app.",
     "steps": [("2.2", "multibrand", "Take the multi-brand debit card"), ("2.3", "kamba", "Or load a Kamba Visa card"),
               ("5.1", "app", "Load and track it in BAI Directo"), ("2.4", "taag", "Fly TAAG on the co-brand card")]},
    {"id": "borrow", "who": "con", "name": "Borrow",
     "why": "A personal loan in minutes in the app, with life cover, or a home.",
     "steps": [("4.2", "cpo", "Take a personal loan online"), ("4.5", "nossa", "Add Vida Digital cover"),
               ("4.2", "housing", "Buy or build a home"), ("2.4", "mcxcredit", "Use a Multicaixa credit card")]},
    {"id": "premium", "who": "prem", "name": "Bank as a Premium client",
     "why": "A personal manager, Visa credit, partner offers and investments.",
     "steps": [("4.4", "premium", "Work with a Premium manager"), ("2.3", "visacredit", "Spend on Visa credit"),
               ("3.3", "prestige", "Use Prestige offers"), ("4.5", "markets", "Invest through ÁUREA")]},
    {"id": "merchant", "who": "sme", "name": "Take payments as a merchant",
     "why": "Multicaixa terminals, the TPA+ account, Visa online and QR.",
     "steps": [("2.6", "tpa", "Install a BAI terminal"), ("2.6", "ebai", "Sell online with e-BAI"),
               ("2.7", "baipaga", "Take QR payments"), ("4.3", "agri", "Borrow to grow")]},
    {"id": "corp", "who": "corp", "name": "Run a company's money",
     "why": "Corporate credit, mass payments, corporate and fuel cards, and cross-border flows now including China.",
     "steps": [("4.3", "corporate", "Bank with a corporate centre"), ("4.3", "collections", "Pay salaries and suppliers"),
               ("2.5", "mccorp", "Give staff Mastercard corporate cards"), ("2.5", "flex", "Fuel the fleet with FLEX"),
               ("2.8", "correspondent", "Pay abroad through correspondents"), ("2.8", "cips", "Settle in renminbi")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "A small corporate prepaid card and, since August 2026, a debit card that is Multicaixa at home and Mastercard abroad.",
     "steps": [("2.5", "mccorp", "Mastercard corporate prepaid"), ("2.2", "multibrand", "Multi-brand debit on Mastercard abroad")]},
    {"id": "mcnext", "who": "mc", "name": "Where BAI's debit, fleet and tourism cards could land",
     "why": "Where BAI has needs and Mastercard is not yet in: 2 million debit holders who could carry the multi-brand card, fleets and corporates, fraud and tokens, remittances, online acceptance and the tourism card.",
     "steps": [("2.1", "mcxdebit", "Move debit holders to the multi-brand card"), ("2.5", "flex", "Commercial and fleet cards"),
               ("3.1", "security", "Fraud scoring and tokens for the new card"), ("2.3", "kamba", "Remittances in place of Kamba loads"),
               ("2.6", "ebai", "Mastercard acceptance online"), ("3.3", "tourism", "A network for the tourism card")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across BAI's map",
    "title": "A Multicaixa bank where Visa travels and Mastercard has just arrived",
    "lead": "Nine in ten of BAI's 2.38 million active cards run only on Angola's domestic Multicaixa scheme. Visa carries what goes abroad: about 170,000 Kamba prepaid cards, Visa credit and online acceptance, renewed by a strategic agreement on 23 September 2026. Mastercard had 796 corporate prepaid cards until August 2026, when BAI launched a debit card that is Multicaixa at home and Mastercard abroad. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are BAI's own (H1 2026 report and Q2 2026 release, 23 July 2026; 2025 annual report), translated from Portuguese, or from Angolan press. Take-up of the multi-brand card and BAI's acceptance of international cards are not published.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Multicaixa (EMIS)", "2.08 million active, June 2026"],
        ["Multi-brand debit", "Multicaixa + Mastercard", "Launched August 2026; take-up not disclosed ⚠"],
        ["Prepaid abroad", "Visa (Kamba)", "169,755 active, down 15% in H1 2026"],
        ["Credit", "Visa and Multicaixa", "6,142 Visa, 5,207 Multicaixa"],
        ["Corporate prepaid", "Mastercard", "796 active"],
        ["Scheme deal", "Visa", "Strategic agreement, 23 September 2026"],
        ["Instant and QR", "KWiK, BAI Paga, é-Kwanza", "EMIS rails and BAI's own wallet"],
        ["Online acceptance", "e-BAI", "Visa cards"],
    ],
    "sides": {
        "neo": {"dir": "The corporate prepaid card and the new multi-brand debit card abroad.",
                "deals": "What it does not do: domestic debit, credit, prepaid travel cards, acceptance, instant payments, fraud or AI."},
        "snb": {"dir": "Multicaixa for every domestic card and terminal, Visa for Kamba, credit, e-BAI and bank sponsorship, EMIS for KWiK, and BAI's own wallet, fraud and AI.",
                "deals": "Where they meet: debit holders who want to pay abroad, now offered Mastercard by BAI and Visa by its rival Atlântico."},
    },
    "tl": [
        ["Jun 2022", "IPO on BODIVA"],
        ["Feb 2023", "All Multicaixa debit cards on chip"],
        ["Jul 2023", "KWiK launched; Visa and Mastercard cards issued at FILDA"],
        ["Aug 2023", "EMIS and Mastercard agree multi-brand debit cards"],
        ["Apr 2024", "International card limits cut as dollars run short"],
        ["Aug 2025", "Finastra Essence core programme starts"],
        ["Jul 2026", "Visa co-badge debit launched by rival Atlântico"],
        ["Aug 2026", "BAI launches Multicaixa + Mastercard debit card"],
        ["Sep 2026", "Bank of China CIPS memorandum; Visa strategic agreement"],
    ],
    "l": {
        "U": {"d": 1, "s": "A few travellers and corporates carry Mastercard.",
              "gap": "Almost everyone carries a Multicaixa card; travellers mostly carry Visa Kamba; Mastercard reaches corporate prepaid holders and the first multi-brand debit holders.",
              "neo": "Multi-brand debit holders, corporate prepaid holders.", "snb": "Multicaixa debit holders, Kamba and Visa credit holders, é-Kwanza users."},
        "L5": {"d": 0, "s": "The front doors are BAI's.", "gap": "App, branches, ATMs and agents are BAI's own, on the Multicaixa network.", "neo": "None.", "snb": "BAI Directo, branches, ATMs, agents."},
        "L4": {"d": 0, "s": "The business lines carry Multicaixa cards.", "gap": "Accounts come with Multicaixa debit; loans, Premium, insurance and markets have no network role.",
               "neo": "None.", "snb": "Accounts, loans, corporate banking, NOSSA, ÁUREA."},
        "L3": {"d": 0, "s": "Fraud, AI and benefits are BAI's.", "gap": "No Mastercard fraud, token or offers tools; the tourism card has no network yet.",
               "neo": "None.", "snb": "Fraud defences, LUENA, Prestige offers."},
        "L2": {"d": 1, "s": "Multicaixa at home, Visa abroad, Mastercard at the edges.", "gap": "Multicaixa runs debit and terminals; Visa runs Kamba, credit and e-BAI; Mastercard runs the corporate prepaid card and the multi-brand card abroad.",
               "neo": "Corporate prepaid, multi-brand debit abroad.", "snb": "Multicaixa cards and terminals, Visa cards, KWiK, é-Kwanza, CIPS."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, listing, Finastra core, strategy."},
    },
    "t": area_lens(LAYERS),
}
