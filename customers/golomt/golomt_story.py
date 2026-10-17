"""Golomt Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from golomt_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Mongolia's second-largest bank as five discs that stack into one platform, from 22% of the country's banking assets "
       "and 30 years of history at the bottom to SocialPay, the internet bank and 108 branches at the top. Click the stack "
       "to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Children & young people", "graduation-cap"),
    ("vip", "Premier & affluent clients", "gem"),
    ("sme", "Small businesses & merchants", "store"),
    ("trader", "Importers & travellers to China", "plane"),
    ("corp", "Corporates & miners", "factory"),
]
USERS_DESC = ("Six kinds of customer, more than 1.3 million in all, about a third of Mongolians: everyday customers, children "
              "and young people, Premier clients, small businesses and merchants, importers and travellers to China, and the "
              "corporates and mining suppliers Golomt is best known for.")

WHO = {"con": "A Golomt customer", "young": "A student", "vip": "A Premier client", "sme": "A shop owner",
       "trader": "An importer", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: savings, a debit card on one of four schemes, SocialPay QR, the AI assistant and fraud checks.",
     "steps": [("4.3", "savings", "Open an account"), ("2.1", "debit", "Pay with a debit card"), ("2.5", "socialpay", "Pay by QR in SocialPay"),
               ("3.2", "aiassist", "Ask the AI assistant"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "phone", "who": "con", "name": "Pay with a phone",
     "why": "A virtual card from SocialPay, then Apple Pay, Google Pay or Samsung Pay; the scheme decides which.",
     "steps": [("3.4", "ekyc", "Open an account remotely"), ("2.5", "virtual", "Get a virtual card"), ("2.4", "applepay", "Add it to Apple Pay"),
               ("2.4", "googlepay", "Or Google Pay"), ("2.4", "samsungpay", "Or Samsung Pay with Visa")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Credit cards on Visa, Mastercard or Amex, and Wide Loyalty points.",
     "steps": [("2.2", "visacredit", "Take a Visa credit card"), ("2.2", "goldmc", "Or a Gold Mastercard"), ("2.2", "amex", "Or an Amex"),
               ("3.3", "loyalty", "Earn Wide Loyalty points")]},
    {"id": "premium", "who": "vip", "name": "Travel on a metal card",
     "why": "The World Mastercard with concierge, scheme offers and wealth services.",
     "steps": [("2.3", "worldmc", "Carry the World Mastercard"), ("3.3", "offers", "Use Priceless and travel offers"),
               ("4.5", "wealth", "Invest with Premiere"), ("4.5", "gold", "Hold digital gold")]},
    {"id": "young", "who": "young", "name": "Start young",
     "why": "Children's savings, the Color and Skate cards and Gen Z loyalty.",
     "steps": [("4.3", "savings", "Save in Altantulkhuur"), ("2.1", "youth", "Wear the Skate card"), ("3.3", "loyalty", "Join Gen Z loyalty")]},
    {"id": "china", "who": "trader", "name": "Pay and send to China",
     "why": "UnionPay and WeChat QR for travellers, CIPS for RMB transfers and trade finance for importers.",
     "steps": [("2.6", "unionpay", "Pay by WeChat QR with UnionPay"), ("2.6", "cips", "Send RMB via CIPS"), ("4.4", "tradefin", "Open a letter of credit")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "An SME loan, POS and QR acceptance, instalments and coupons.",
     "steps": [("4.2", "sme", "Borrow as an SME"), ("2.7", "acquiring", "Take cards and QR"), ("2.7", "easypay", "Offer instalments"),
               ("3.3", "loyalty", "Sell coupons in the marketplace")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Corporate lending, Corporate Gateway and payroll, international transfers and trade finance.",
     "steps": [("4.1", "corporate", "Borrow as a corporate"), ("4.1", "gateway", "Pay through Corporate Gateway"),
               ("2.6", "swift", "Send money abroad"), ("4.4", "tradefin", "Finance imports")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The World and Gold cards, first place on Apple Pay and Google Pay, scheme offers and the M/Chip under the ₮ Card.",
     "steps": [("2.3", "worldmc", "World Mastercard at the top"), ("2.2", "goldmc", "Gold Mastercard"), ("2.4", "applepay", "Mastercard first on Apple Pay"),
               ("2.1", "tcard", "M/Chip under the ₮ Card"), ("3.3", "offers", "Priceless and Travel Rewards")]},
    {"id": "mcnext", "who": "mc", "name": "Where Samsung Pay, scams and the AI bank could land",
     "why": "Where Golomt has needs and Mastercard is not yet in: Samsung Pay, fraud scoring, acceptance, offers for Wide Loyalty, agentic payments, corporate cards and cross-border transfers.",
     "steps": [("2.4", "samsungpay", "Mastercard tokens on Samsung Pay"), ("3.1", "fraud", "Scam and fraud scoring"), ("2.7", "acquiring", "Acquirer risk and merchant data"),
               ("3.3", "loyalty", "Card-linked offers for Wide Loyalty"), ("3.2", "aiassist", "Agent Pay for the assistant"),
               ("4.1", "gateway", "Corporate and fuel cards"), ("2.6", "swift", "Transfers by card number")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Golomt Bank's map",
    "title": "A four-scheme bank where Mastercard leads on phones and metal",
    "lead": "Golomt issues on Visa, Mastercard, UnionPay and American Express, and the national ₮ Card. Mastercard, with it since 1999, holds the top of the range with the World Mastercard metal card (2025) and was the first scheme Golomt put on Apple Pay (December 2024) and Google Pay (November 2025); its M/Chip specification also runs under the ₮ Card. Visa carries more of the credit range, joined Apple Pay in 2026 and, with UnionPay, is alone on Samsung Pay. UnionPay, WeChat and CIPS own the China corridor. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (2025 annual report and MD&A; Q2 2026 statement, 21 July 2026) or from the Bank of Mongolia, Mastercard and QPay. No split of cards by network is published; several pages, including Mastercard's 2022 ₮-Card release and SocialPay's own site, could not be read.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa, Mastercard, UnionPay, ₮ Card", "Classic debit on all four"],
        ["Credit", "Visa, Mastercard, Amex", "39% of Mongolia's card lending"],
        ["Top card", "World Mastercard", "Metal, launched 2025"],
        ["Phones", "Mastercard first", "Apple Pay Dec 2024, Google Pay Nov 2025"],
        ["Samsung Pay", "Visa and UnionPay", "July 2026, no Mastercard"],
        ["National card", "₮ Card on M/Chip", "2m+ cards, 45% of cards ⚠"],
        ["China", "UnionPay, WeChat, CIPS", "RMB since Sep 2025"],
        ["Wallet", "SocialPay QR", "78% of digital users"],
    ],
    "sides": {
        "neo": {"dir": "World and Gold Mastercard, Mastercard debit and virtual cards, first place on Apple Pay and Google Pay, Priceless and Travel Rewards, and the M/Chip under the ₮ Card.",
                "deals": "What it does not do: Samsung Pay, the Visa and Amex credit range, the China corridor, SocialPay QR, fraud models or loyalty."},
        "snb": {"dir": "Visa's credit range, Samsung Pay and B2B transfers, UnionPay and WeChat for China, Amex, the domestic ₮ Card switch, QPay and Golomt's own fraud, AI and loyalty.",
                "deals": "Where they meet: debit, virtual cards and phone wallets, where every scheme sits side by side."},
    },
    "tl": [
        ["1999", "Golomt becomes a Mastercard issuer"],
        ["2000", "Visa follows"],
        ["2010", "UnionPay RMB card"],
        ["2013", "American Express agreement"],
        ["Nov 2019", "Bank of Mongolia picks Mastercard M/Chip for the ₮ Card"],
        ["2022", "IPO; CardZone processing"],
        ["Dec 2024", "Apple Pay with Mastercard and ₮ cards"],
        ["2025", "World Mastercard metal card; Universe range"],
        ["Nov 2025", "Google Pay with Mastercard and ₮ cards"],
        ["Apr 2026", "Visa added to Apple Pay ⚠"],
        ["Jul 2026", "Samsung Pay with Visa and UnionPay"],
        ["Sep 2026", "Bank of China MoU"],
    ],
    "l": {
        "U": {"d": 1, "s": "Many customers carry Mastercard, but beside three other schemes.",
              "gap": "Premier clients reach for the World card; everyday customers hold Visa, Mastercard, UnionPay or ₮ debit; travellers to China use UnionPay.",
              "neo": "World and Gold cardholders, Mastercard debit and virtual card users.", "snb": "Visa and Amex credit holders, ₮ Card and UnionPay users, corporates."},
        "L5": {"d": 0, "s": "The front doors are Golomt's.", "gap": "Internet bank, branches and agents are the bank's own.", "neo": "None.", "snb": "Internet bank, branches, ATMs, agents."},
        "L4": {"d": 0, "s": "The business lines have no network role.", "gap": "Corporate, SME, mortgage, trade and gold business runs on Golomt's balance sheet.",
               "neo": "None.", "snb": "Corporate and SME lending, mortgages, trade finance, gold."},
        "L3": {"d": 0, "s": "Services are Golomt's own, apart from scheme offers.", "gap": "Fraud models, AI assistants and Wide Loyalty are in-house; Priceless and Travel Rewards ride on Mastercard cards.",
               "neo": "Priceless and Travel Rewards.", "snb": "Fraud models, AI, Wide Loyalty, eKYC."},
        "L2": {"d": 1, "s": "Mastercard at the top and first on phones; shared everywhere else.", "gap": "Visa has more credit cards and Samsung Pay; UnionPay owns China; SocialPay and the ₮ Card run on domestic rails.",
               "neo": "World and Gold Mastercard, debit, Apple and Google Pay, M/Chip under the ₮ Card.", "snb": "Visa credit and Samsung Pay, UnionPay, Amex, SocialPay QR, CIPS."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, owners, funding, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
