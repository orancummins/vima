"""Millennium bcp's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from millenniumbcp_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Portugal's second-largest bank as five discs that stack into one platform, from €566 million of half-year profit "
       "and 7.4 million customers in three countries at the bottom to the Millennium app, branches and the Empresas website "
       "at the top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it "
       "light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard "
       "goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("digital", "Digital-first customers", "smartphone"),
    ("affluent", "Prestige & private clients", "gem"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
    ("merchant", "Merchants", "store"),
    ("abroad", "Customers in Poland & Mozambique", "earth"),
]
USERS_DESC = ("Seven kinds of customer, 7.4 million active in all: 2.9 million in Portugal, from everyday and digital-first "
              "customers to Prestige clients, small businesses, corporates and the merchants who take cards, plus 3.35 "
              "million at Bank Millennium in Poland and Millennium bim's customers in Mozambique.")

WHO = {"con": "A Millennium customer", "digital": "A digital-first customer", "affluent": "A Prestige client",
       "sme": "A small business", "corp": "A corporate treasurer", "merchant": "A merchant", "abroad": "A customer abroad"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Visa debit card with Multibanco, MB WAY in the app and card controls.",
     "steps": [("4.1", "accounts", "Open an account"), ("2.1", "debit", "Pay with Visa debit"), ("5.1", "app", "Run it in the app"),
               ("2.5", "mbway", "Send money with MB WAY"), ("3.1", "fraud", "Turn card use on and off")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "GO! to Gold Prestige on Visa, in a phone wallet, with Millennium Rewards.",
     "steps": [("2.2", "credit", "Take a Visa credit card"), ("2.5", "wallets", "Add it to a phone wallet"), ("3.3", "rewards", "Earn Millennium Rewards")]},
    {"id": "travel", "who": "affluent", "name": "Travel on points and miles",
     "why": "Prestige banking with TAP miles, hotel benefits and UnionPay for Asia.",
     "steps": [("4.1", "prestige", "Bank with Prestige"), ("2.2", "tapcard", "Earn TAP miles"), ("3.3", "rewards", "Use travel benefits"),
               ("2.3", "unionpay", "Pay in Asia with UnionPay")]},
    {"id": "digital", "who": "digital", "name": "Bank from the phone",
     "why": "ActivoBank or the Millennium app, a digital card on day one and MB WAY.",
     "steps": [("4.2", "activobank", "Open with ActivoBank"), ("5.1", "app", "Get a digital card in the app"), ("2.5", "mbway", "Pay with MB WAY"),
               ("3.2", "dmm", "See spending insights")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "Credit, business cards, terminals and merchant analytics.",
     "steps": [("4.3", "companies", "Borrow as a company"), ("2.4", "bizcredit", "Give staff Visa business cards"),
               ("2.4", "mcbiz", "Or a Mastercard business debit card"), ("2.6", "tpa", "Take cards on a terminal")]},
    {"id": "merchant", "who": "merchant", "name": "Take payments",
     "why": "Terminals, the P@y.me gateway and TPA Analytics.",
     "steps": [("2.6", "tpa", "Install a Smart Moove terminal"), ("2.6", "payme", "Sell online with P@y.me"),
               ("3.4", "tpaanalytics", "Read customers with TPA Analytics"), ("5.3", "empresasweb", "Manage it on the Empresas website")]},
    {"id": "corp", "who": "corp", "name": "Finance the supply chain",
     "why": "Confirming and Cash-on-Time, open to suppliers who are not clients.",
     "steps": [("4.3", "companies", "Bank with Empresas"), ("4.3", "cashontime", "Pay suppliers early with Cash-on-Time"),
               ("3.4", "apis", "Onboard suppliers by API"), ("3.1", "identity", "Sign in with the state digital key")]},
    {"id": "poland", "who": "abroad", "name": "Bank with Bank Millennium",
     "why": "Dual-network cards, BLIK and Click to Pay in Poland.",
     "steps": [("4.5", "bankmillennium", "Open Konto 360°"), ("2.7", "plcredit", "Take an Impresja credit card"),
               ("2.7", "c2p", "Check out with Click to Pay"), ("2.7", "blik", "Pay with BLIK"), ("5.1", "plapp", "Use the app")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Bank Millennium's cards and Click to Pay, the business debit card and legacy cards in Portugal, and acceptance.",
     "steps": [("2.7", "plcredit", "Bank Millennium credit cards"), ("2.7", "c2p", "Click to Pay in Poland"),
               ("2.4", "mcbiz", "Mastercard Débito Empresas"), ("2.1", "mclegacy", "Legacy debit cards"), ("2.6", "payme", "Acceptance on P@y.me")]},
    {"id": "mcnext", "who": "mc", "name": "Where services, not cards, could land",
     "why": "Where Millennium bcp has needs and Mastercard is not yet in: fraud tools for the real-time push, merchant data, open finance for suppliers, card-linked offers, and business cards.",
     "steps": [("3.1", "fraud", "Network-agnostic fraud and scam tools"), ("3.4", "tpaanalytics", "Merchant data for TPA Analytics"),
               ("3.4", "apis", "Open finance for Cash-on-Time"), ("3.3", "rewards", "Card-linked offers"), ("2.4", "mcbiz", "Grow business cards")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Millennium bcp's map",
    "title": "A Visa bank at home, dual-network in Poland",
    "lead": "In Portugal every consumer card Millennium bcp now sells is Visa, co-badged with Multibanco, and it was Europe's first UnionPay issuer. Its Mastercard and Maestro cards are listed as no longer sold, which leaves a branch-only business debit card. In Poland, Bank Millennium issues both networks and added Mastercard Click to Pay in September 2026. Meanwhile SIBS, owner of MB WAY, is building a European rail meant to displace both schemes. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 fact sheet and institutional presentation) or from the bank's card pages and its card price list in force from 7 September 2026. The date of the switch from Mastercard to Visa in Portugal is not published; Bank Millennium's debit split and Millennium bim's networks are unconfirmed.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Portugal debit", "Visa + Multibanco", "All adult cards on sale"],
        ["Portugal credit", "Visa", "GO! to Platinum, TAP co-brand"],
        ["Legacy cards", "Mastercard, Maestro, Amex", "No longer sold ⚠ dates"],
        ["Business debit", "Mastercard", "Branch only"],
        ["UnionPay", "Since 2019", "Europe's first issuer"],
        ["Poland", "Visa and Mastercard", "Click to Pay, Sep 2026"],
        ["Mozambique", "Visa ⚠", "Millennium bim"],
        ["Rival rail", "MB WAY / EuroPA", "P2P 2026, shops 2027"],
    ],
    "sides": {
        "neo": {"dir": "Bank Millennium's Mastercard credit, prepaid and euro debit cards and Click to Pay; the Portuguese business debit card, legacy cards still in wallets, and acceptance at the bank's merchants.",
                "deals": "What it does not do: Portuguese consumer issuing, fraud tools, AI, loyalty or open banking."},
        "snb": {"dir": "Visa for every new Portuguese consumer card, UnionPay, SIBS's Multibanco and MB WAY, BLIK in Poland, and the bank's own fraud, data and AI.",
                "deals": "Where they meet: terminals and P@y.me take both, and Bank Millennium issues both."},
    },
    "tl": [
        ["Nov 2017", "UnionPay agreement"],
        ["Jan 2019", "First UnionPay cards in Europe"],
        ["Jan 2022", "GO! Changer launched on Visa"],
        ["Oct 2024", "2025-28 plan, Deliver more value"],
        ["Apr 2026", "SIBS shows EuroPA in Lisbon"],
        ["May 2026", "Maya reappointed to 2029"],
        ["Jun 2026", "Bank Millennium's Visa Raz virtual card"],
        ["Sep 2026", "Price list shows Mastercard consumer cards no longer sold"],
        ["Sep 2026", "Bank Millennium adds Mastercard Click to Pay"],
        ["End-2027", "EuroPA shop payments due"],
    ],
    "l": {
        "U": {"d": 1, "s": "Polish cardholders and Portuguese businesses carry Mastercard.",
              "gap": "Portuguese consumers get Visa; Bank Millennium's customers and a few Portuguese firms carry Mastercard.",
              "neo": "Bank Millennium cardholders, business debit users, legacy cardholders.", "snb": "Portuguese consumers, Prestige clients, ActivoBank, Mozambique."},
        "L5": {"d": 0, "s": "The front doors are the bank's.", "gap": "Apps, branches and the Empresas website are its own.", "neo": "None.", "snb": "App Millennium, branches, Empresas website."},
        "L4": {"d": 1, "s": "Bank Millennium is dual-network; Portugal is Visa.", "gap": "Polish lines carry both networks; Portuguese retail and Prestige carry Visa.",
               "neo": "Bank Millennium; one business debit card.", "snb": "Retail, Prestige, ActivoBank ⚠, bim."},
        "L3": {"d": 0, "s": "Fraud, AI and loyalty are the bank's own.", "gap": "No Mastercard service is public; Visa benefits sit on Prestige cards.",
               "neo": "None public.", "snb": "Card controls, AI money management, Millennium Rewards, TPA Analytics."},
        "L2": {"d": 1, "s": "Visa issues in Portugal; Mastercard in Poland and on terminals.", "gap": "Visa has Portuguese debit and credit; Mastercard keeps business debit, Poland and Click to Pay.",
               "neo": "Bank Millennium cards, Click to Pay, business debit, acceptance.", "snb": "Visa debit and credit, UnionPay, MB WAY, BLIK."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, owners, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
