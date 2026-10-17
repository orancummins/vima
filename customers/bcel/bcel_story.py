"""BCEL's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bcel_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Laos's biggest commercial bank as five discs that stack into one platform, from LAK 161 trillion of assets "
       "and the state's 60% at the bottom to BCEL One, branches and village agents at the top. Click the stack to open "
       "it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("rural", "Rural customers", "house"),
    ("remit", "Remittance families", "send"),
    ("trav", "Travellers & visitors", "plane"),
    ("merch", "Merchants & SMEs", "store"),
    ("corp", "Corporates & the state", "factory"),
]
USERS_DESC = ("Six kinds of customer: everyday customers (about 1.4 million on BCEL One ⚠), rural customers served by "
              "734 agents, families receiving money from abroad, travellers and visitors, merchants and small "
              "businesses taking QR and cards, and the corporates and state bodies BCEL lends to and pays for.")

WHO = {"con": "A BCEL customer", "rural": "A villager", "remit": "A family abroad", "trav": "A traveller",
       "merch": "A merchant", "corp": "A company treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a kip account, a UnionPay card, BCEL One and OnePay QR, with slips you can check.",
     "steps": [("4.1", "deposits", "Open a savings account"), ("2.1", "updebit", "Get a UnionPay card"),
               ("5.1", "bcelone", "Run it in BCEL One"), ("2.6", "onepay", "Pay by OnePay QR"), ("3.3", "edl", "Pay the power bill automatically")]},
    {"id": "rural", "who": "rural", "name": "Bank through a village agent",
     "why": "BCOME agents open cards, take deposits and send cash where there is no branch.",
     "steps": [("5.3", "bcome", "Visit a BCOME agent"), ("2.1", "updebit", "Get a card"), ("2.7", "lapnet", "Withdraw at any LAPNet ATM")]},
    {"id": "remit", "who": "remit", "name": "Receive money from abroad",
     "why": "MoneyGram and GLN into BCEL One, cash out at an agent.",
     "steps": [("2.8", "gln", "Send from Korea"), ("2.8", "moneygram", "Or send by MoneyGram"),
               ("5.1", "bcelone", "Receive in BCEL One"), ("5.3", "bcome", "Cash out at an agent")]},
    {"id": "travel", "who": "trav", "name": "Pay abroad",
     "why": "Premium cards on Visa and Mastercard, and OnePay QR in Thailand.",
     "steps": [("2.2", "visacredit", "Carry a Visa Platinum"), ("2.3", "wmc", "Or a World Mastercard with lounge access"),
               ("2.8", "thqr", "Scan PromptPay in Thailand"), ("4.3", "tradefx", "Change money at the border")]},
    {"id": "visit", "who": "trav", "name": "Visit Laos",
     "why": "EZyKip, Chinese QR wallets and ATMs that take every card.",
     "steps": [("2.9", "ezykip", "Load EZyKip"), ("2.6", "chinaqr", "Pay with UnionPay, WeChat Pay or Alipay"),
               ("2.8", "xqr", "Scan LAO QR from home apps"), ("5.2", "atms", "Withdraw at a BCEL ATM")]},
    {"id": "merchant", "who": "merch", "name": "Take payments and grow",
     "why": "OnePay QR and LAO QR, card terminals, slip checks and 3% SME loans.",
     "steps": [("2.6", "onepay", "Take OnePay QR"), ("2.7", "laoqr", "Join LAO QR"), ("2.5", "acquiring", "Take cards"),
               ("3.1", "oneproof", "Check slips with OneProof"), ("4.2", "sme3", "Borrow at 3%")]},
    {"id": "corp", "who": "corp", "name": "Run a company's money",
     "why": "Loans, trade finance, payroll and Visa corporate cards.",
     "steps": [("4.2", "corplend", "Borrow"), ("4.3", "tradefx", "Finance trade"), ("4.4", "payroll", "Pay staff through i-Bank"),
               ("2.2", "visacorp", "Give staff Visa corporate cards")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The World Mastercard, the virtual prepaid card in BCEL One, ATM acceptance and a 2025 cardholder campaign.",
     "steps": [("2.3", "wmc", "World Mastercard credit"), ("2.3", "vpmc", "Virtual Prepaid Mastercard in BCEL One"),
               ("5.2", "atms", "Mastercard accepted at BCEL ATMs"), ("3.4", "mccampaign", "Mastercard Campaign 2025")]},
    {"id": "mcnext", "who": "mc", "name": "Where tourism, remittances and security could land",
     "why": "Where BCEL has needs and Mastercard is not yet in: debit beyond UnionPay, tourist top-ups, remittances, card security, commercial cards and offers.",
     "steps": [("2.1", "updebit", "Mastercard debit beside UnionPay"), ("2.9", "ezykip", "Mastercard top-ups for EZyKip"),
               ("2.8", "moneygram", "Move for remittances"), ("3.1", "pci", "Tokens and fraud scoring"),
               ("2.2", "visacorp", "Commercial and virtual cards"), ("3.4", "offers", "Card-linked offers")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across BCEL's map",
    "title": "A UnionPay and Visa bank with one Mastercard in the wallet",
    "lead": "UnionPay has carried BCEL's mass debit cards since 2011 and owns 15% of LAPNet, the national switch in which BCEL holds 20%. Visa is BCEL's main international brand, for premium, debit and corporate cards, and BCEL has acquired Visa since 2010. Mastercard has the World Mastercard credit card and a prepaid Mastercard, both from April 2019, a virtual prepaid card in BCEL One, acceptance at BCEL ATMs and a 2025 cardholder campaign. Most growth is in QR: OnePay, LAO QR and cross-border links built without the card schemes, except UnionPay. Each area below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are BCEL's own (2025 Annual Report; H1 2026 summary, 31 August 2026) or from UnionPay, the Vientiane Times, Tourism Laos and Vietnamese sources. BCEL publishes no card counts by network or Mastercard volumes; app users come from a State Bank of Vietnam journal.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "UnionPay", "Since July 2011; 8 in 10 Lao cards in 2019"],
        ["Premium & corporate", "Visa", "Issuer and acquirer since 2010; Platinum 2021"],
        ["World Mastercard", "Mastercard", "Credit, April 2019"],
        ["Prepaid", "Mastercard", "Prepaid 2019; virtual card in BCEL One"],
        ["JCB", "JCB", "Credit since May 2015 ⚠"],
        ["National switch", "LAPNet", "BCEL 20%, UnionPay 15%"],
        ["QR", "OnePay & LAO QR", "Links to Thailand, Vietnam, China, Cambodia"],
        ["Remittances", "MoneyGram, GLN", "In BCEL One"],
    ],
    "sides": {
        "neo": {"dir": "The World Mastercard and prepaid cards, the virtual card in BCEL One, ATM acceptance and a 2025 campaign.",
                "deals": "What it does not do: mass debit, corporate cards, QR, the national switch, remittances or security tools."},
        "snb": {"dir": "UnionPay debit and QR and its LAPNet stake, Visa premium, debit and corporate cards and acquiring, JCB credit, OnePay and LAO QR, MoneyGram and GLN.",
                "deals": "Where they meet: BCEL's ATMs and terminals take every network, and EZyKip plans top-ups from all of them."},
    },
    "tl": [
        ["2010", "Visa issuing and acquiring"],
        ["Jul 2011", "UnionPay cards with Bank of China"],
        ["May 2015", "BCEL-JCB credit card"],
        ["Apr 2019", "World Mastercard and prepaid Mastercard"],
        ["Sep 2019", "UnionPay QR, first in Laos"],
        ["Nov 2021", "Visa Platinum credit and debit"],
        ["Jan 2024", "EZyKip tourist wallet"],
        ["Dec 2024", "LAPNet links to UnionPay QR"],
        ["Jan 2025", "LAPNet links to Vietnam's NAPAS"],
        ["Q2 2026", "Mastercard Campaign 2025 draw"],
        ["Aug 2026", "OceanBase core-banking MoU"],
    ],
    "l": {
        "U": {"d": 1, "s": "World Mastercard and prepaid holders carry Mastercard.",
              "gap": "Most cardholders carry UnionPay debit; premium and corporate users carry Visa; a small group carries Mastercard.",
              "neo": "World Mastercard and prepaid cardholders, visitors using Mastercard at ATMs.", "snb": "UnionPay debit holders, Visa holders, QR users, agents' customers."},
        "L5": {"d": 1, "s": "BCEL One hosts the virtual Mastercard; ATMs take Mastercard.", "gap": "The app, branches and agents are BCEL's; ATMs accept seven networks.",
               "neo": "Virtual prepaid card in BCEL One, ATM acceptance.", "snb": "BCEL One, i-Bank, branches, BCOME."},
        "L4": {"d": 0, "s": "The business lines come with UnionPay cards.", "gap": "Deposits, loans, FX, payroll and tax have no Mastercard role.",
               "neo": "None.", "snb": "Deposits, lending, FX, securities, payroll."},
        "L3": {"d": 1, "s": "A 2025 Mastercard campaign; the rest is BCEL's.", "gap": "Security, onboarding and partners are BCEL's own; card offers apply to every BCEL card.",
               "neo": "Mastercard Campaign 2025, discounts on Mastercard cards.", "snb": "OneProof, OneCare, billers, One Heart."},
        "L2": {"d": 1, "s": "Two Mastercard cards among UnionPay, Visa, JCB and QR.", "gap": "UnionPay has debit and the switch stake, Visa the premium and corporate cards; Mastercard has a credit and a prepaid card.",
               "neo": "World Mastercard, Virtual Prepaid Mastercard, acceptance.", "snb": "UnionPay debit and QR, Visa cards, JCB, OnePay, LAO QR, MoneyGram."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's; UnionPay co-owns LAPNet.", "neo": "None.", "snb": "Capital, state ownership, BRED, JVs, strategy."},
    },
    "t": area_lens(LAYERS),
}
