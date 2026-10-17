"""Bank of Georgia's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bog_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Georgia's largest bank as five discs that stack into one platform, from about 40% of the country's banking assets "
       "at the bottom to a mobile bank opened by a million people a day at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("aff", "SOLO premium clients", "gem"),
    ("home", "Homebuyers", "house"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
    ("merch", "Merchants", "store"),
]
USERS_DESC = ("Six kinds of customer: 2.3 million active retail customers, SOLO's mass-affluent clients, homebuyers, "
              "136,000 active businesses, the corporates CIB serves, and 28,800 merchants taking cards.")

WHO = {"con": "A Bank of Georgia customer", "aff": "A SOLO client", "home": "A homebuyer", "sme": "A small business",
       "corp": "A corporate treasurer", "merch": "A merchant"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: the mobile bank, a Visa or Mastercard card, Apple Pay and the AI assistant.",
     "steps": [("5.1", "app", "Open the mobile bank"), ("2.1", "digicard", "Issue a digital card"), ("2.1", "debit", "Pay with Visa or Mastercard"),
               ("2.1", "wallets", "Tap with Apple Pay"), ("3.1", "assistant", "Ask the AI assistant"), ("3.2", "fincrime", "Protected by fraud checks")]},
    {"id": "borrow", "who": "con", "name": "Borrow in seconds",
     "why": "Consumer loans decided in under 15 seconds, and credit cards.",
     "steps": [("5.1", "app", "Apply in the app"), ("3.1", "instantloan", "Get a loan in 15 seconds"), ("2.1", "credit", "Use a credit card or overdraft")]},
    {"id": "premium", "who": "aff", "name": "Bank with SOLO",
     "why": "SOLO's packages carry both a Mastercard World Elite and a Visa Platinum, lounges and a personal banker.",
     "steps": [("5.3", "branches", "Join SOLO"), ("4.3", "solo", "Get a personal banker"), ("2.2", "solocards", "Travel on World Elite or Visa Platinum"),
               ("3.3", "offers", "Use Priceless and cashback offers")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "Lari mortgages, now 41% of the retail book.",
     "steps": [("5.1", "app", "Start online"), ("4.2", "mortgages", "Take a lari mortgage")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account and card, software perks on Mastercard, IFC-backed credit and card acceptance.",
     "steps": [("5.2", "bizapp", "Open an account online"), ("2.3", "bizcard", "Take a business card"), ("3.3", "bizoffers", "Use software perks"),
               ("4.4", "sme", "Borrow with IFC-backed lines"), ("2.4", "pos", "Take card payments")]},
    {"id": "corp", "who": "corp", "name": "Run corporate finance",
     "why": "Corporate lending, the Mastercard Corporate Card and Galt & Taggart.",
     "steps": [("4.5", "cib", "Bank with CIB"), ("2.3", "corpcard", "Travel and spend on the Corporate Card"), ("4.5", "galt", "Raise money with Galt & Taggart")]},
    {"id": "merchant", "who": "merch", "name": "Accept payments",
     "why": "Georgia's largest acquirer, in store and online, with Digital Area's commerce software.",
     "steps": [("2.4", "pos", "Take cards in store"), ("2.4", "ecom", "Take cards online"), ("4.6", "digitalarea", "Run stock and tickets on Digital Area")]},
    {"id": "transfer", "who": "con", "name": "Send money",
     "why": "Card-to-card transfers today, the National Bank's instant payments by the end of 2026.",
     "steps": [("2.5", "p2p", "Send card to card"), ("2.6", "ips", "Pay instantly on national rails"), ("2.6", "openbanking", "Pay through open banking")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Mastercard cards beside Visa, World Elite in SOLO, the Corporate Card, business offers and Priceless, and acceptance across the bank's merchants.",
     "steps": [("2.1", "debit", "Mastercard debit beside Visa"), ("2.2", "solocards", "World Elite in every SOLO package"),
               ("2.3", "corpcard", "Mastercard Corporate Card"), ("3.3", "bizoffers", "Business software offers"),
               ("3.3", "offers", "Priceless and cashback campaigns"), ("2.4", "pos", "Acceptance at 28,800 merchants")]},
    {"id": "mcnext", "who": "mc", "name": "Where acquiring, AI and instant payments could land",
     "why": "Where the bank has needs and Mastercard is not yet in: risk and data tools for the country's largest acquirer, agentic payments for an AI bank, account-to-account and open-banking tools as national instant payments arrive, commercial cards for small businesses, and issuing at Ameriabank.",
     "steps": [("2.4", "pos", "Merchant risk and data tools"), ("3.1", "assistant", "Agent Pay for the AI assistant"),
               ("2.6", "ips", "Account-to-account services beside instant payments"), ("3.2", "fincrime", "Fraud and scam scoring"),
               ("4.4", "sme", "Virtual and expense cards for SMEs"), ("4.7", "ameria", "Issuer tools at Ameriabank")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Bank of Georgia's map",
    "title": "Half of Georgia's card market, shared with Visa and squeezed on price",
    "lead": "Bank of Georgia issues Visa and Mastercard side by side, with American Express on an exclusive deal from 2008. Mastercard has the Corporate Card launched in 2025, World Elite in every SOLO package, business offers and Priceless campaigns, and acceptance at the 56.7% of Georgian card volume the bank acquires. In 2025 the bank won better terms from the card schemes, and the National Bank is building instant payments and a national switch to reduce their role. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (1H26 results, 11 August 2026) or from the National Bank of Georgia, Mastercard and Georgian press. Bank of Georgia's website could not be read, so card networks rest on press and guides; no split by network is public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Everyday cards", "Visa and Mastercard", "Customer's choice; 1.7 million paying customers"],
        ["SOLO premium", "World Elite + Visa Platinum", "Both in every package, Feb 2025"],
        ["Amex", "Exclusive partner", "Issuing and acquiring since Dec 2008 ⚠"],
        ["Corporate Card", "Mastercard", "Region's first premium business card, 2025"],
        ["Acquiring", "All networks", "56.7% of Georgian volume, June 2026"],
        ["Scheme fees", "Renegotiated", "Better terms from 2025 onwards"],
        ["Instant payments", "National Bank", "Cardless rails due by end-2026"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard cards beside Visa, World Elite in SOLO, the Corporate Card, business offers, Priceless and cashback, and acceptance at the bank's merchants.",
                "deals": "What it does not do: the AI assistant, instant lending, fraud models, open banking or the coming national rails."},
        "snb": {"dir": "Visa on the same cards, Amex on an exclusive deal, Georgian Card processing, the National Bank's instant payments and national switch, and the bank's own AI.",
                "deals": "Where they meet: every everyday and SOLO card offers both Visa and Mastercard."},
    },
    "tl": [
        ["Dec 2008", "Exclusive American Express partner"],
        ["Sep 2019", "Apple Pay on Visa and Mastercard"],
        ["Mar 2024", "Ameriabank acquired"],
        ["Feb 2025", "Parent renamed Lion Finance Group"],
        ["Mar 2025", "National Bank plans instant payments and a national switch"],
        ["2025", "Mastercard Corporate Card launched; better scheme terms won"],
        ["Jan 2026", "New Head of Payments"],
        ["Aug 2026", "Acquiring share 56.7%; a million daily app users"],
        ["Oct 2026", "World's Best AI Bank"],
        ["End-2026", "National instant payments due"],
    ],
    "l": {
        "U": {"d": 1, "s": "Cardholders choose Visa or Mastercard; SOLO clients carry both.",
              "gap": "Everyday customers pick either network; SOLO clients hold World Elite and Visa Platinum; Amex holders and corporates on the Corporate Card are the clear splits.",
              "neo": "Mastercard cardholders, SOLO, Corporate Card users, merchants accepting Mastercard.", "snb": "Visa and Amex cardholders, borrowers, mortgage customers."},
        "L5": {"d": 0, "s": "The front doors are the bank's.", "gap": "Mobile bank, business banking, branches and terminals are its own.", "neo": "None.", "snb": "App, business bank, branches, terminals."},
        "L4": {"d": 1, "s": "Business lines carry cards on both networks.", "gap": "Retail, SOLO, SME and CIB use Mastercard among other networks; mortgages, Galt & Taggart and Digital Area have no network role.",
               "neo": "Cards in retail, SOLO, SME and CIB; Ameriabank cards.", "snb": "Mortgages, Galt & Taggart, Digital Area, BNB."},
        "L3": {"d": 1, "s": "Offers are Mastercard's; AI and fraud are the bank's.", "gap": "Priceless, cashback and business offers run with Mastercard; the AI assistant, instant lending and fraud controls are in-house.",
               "neo": "Business offers, Priceless and cashback.", "snb": "AI assistant, 15-second loans, fraud and sanctions controls."},
        "L2": {"d": 1, "s": "Dual-network cards and a Mastercard Corporate Card.", "gap": "Mastercard shares every card rail with Visa, owns the Corporate Card, and is accepted at the bank's merchants; Amex, processing and national rails are not Mastercard.",
               "neo": "Mastercard debit, World Elite, Corporate Card, acceptance.", "snb": "Visa, Amex, Georgian Card, instant payments, open banking."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, listing, leadership, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
