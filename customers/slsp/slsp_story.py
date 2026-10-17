"""Slovenská sporiteľňa's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from slsp_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Slovakia's largest bank as five discs that stack into one platform, from €27.6 billion of assets and two "
       "hundred years of savings banking at the bottom to George, branches and ATMs at the top. Click the stack to open "
       "it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined "
       "in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Young people & families", "graduation-cap"),
    ("home", "Homebuyers", "house"),
    ("inv", "Savers & investors", "trending-up"),
    ("sme", "Small businesses & merchants", "briefcase"),
    ("corp", "Corporates & public sector", "factory"),
]
USERS_DESC = ("Six kinds of customer, about 1.8 million in all: everyday customers, young people and families on SPACE "
              "accounts, homebuyers, savers and investors, small businesses and merchants, and the corporates served "
              "from four regional centres.")

WHO = {"con": "A Sporiteľňa customer", "young": "A teenager", "home": "A homebuyer", "inv": "An investor",
       "sme": "A shopkeeper", "corp": "A finance director"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a SPACE account, a Visa debit card in the phone, George and its AI, and card security.",
     "steps": [("4.2", "accounts", "Open a SPACE account"), ("2.1", "debit", "Get a Visa debit card"), ("2.3", "wallets", "Pay by phone or watch"),
               ("5.1", "george", "Run it in George"), ("3.2", "georgeai", "Ask George AI"), ("3.1", "security", "Stay protected")]},
    {"id": "young", "who": "young", "name": "Start banking young",
     "why": "Free accounts under 26, Visa Junior for children and free virtual cards from 15.",
     "steps": [("2.1", "junior", "Get Visa Junior at 6"), ("2.3", "virtual", "Add a free virtual card at 15"), ("4.2", "accounts", "Keep a free account to 26"),
               ("5.1", "george", "Manage it in George")]},
    {"id": "rewards", "who": "con", "name": "Earn back and give back",
     "why": "Moneyback offers, fee rewards for mobile payments and the Dobrá karta's donations.",
     "steps": [("3.3", "moneyback", "Activate Moneyback offers"), ("3.3", "odmena", "Pay by phone for a free account"), ("2.3", "dobra", "Give 0.2% with Dobrá karta")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "Slovakia's leading housing lender, with building savings and insurance alongside.",
     "steps": [("5.2", "branches", "Talk to a branch"), ("4.1", "mortgages", "Take a housing loan"), ("4.1", "pss", "Save with the building society"),
               ("4.3", "insurance", "Insure it")]},
    {"id": "invest", "who": "inv", "name": "Save and invest",
     "why": "George investing from €20, government bonds and funds.",
     "steps": [("5.1", "george", "Open George"), ("4.3", "invest", "Invest from €20"), ("4.3", "bonds", "Buy government bonds"), ("3.2", "georgeai", "Ask how investments are doing")]},
    {"id": "sme", "who": "sme", "name": "Run a shop",
     "why": "A business account and Visa business card, terminals and online payments through Global Payments, and the new QR payments.",
     "steps": [("4.4", "corporate", "Bank with Sporiteľňa"), ("2.4", "bizdebit", "Use a Visa business card"), ("2.5", "accept", "Take cards on a terminal"),
               ("2.5", "webpay", "Take cards online"), ("2.6", "qr", "Take QR payments")]},
    {"id": "corp", "who": "corp", "name": "Finance a company",
     "why": "Corporate lending, leasing and factoring, markets and instant payments.",
     "steps": [("4.4", "corporate", "Borrow, lease, factor"), ("4.4", "markets", "Use Group Markets"), ("2.6", "instant", "Pay by SEPA Instant")]},
    {"id": "pay", "who": "con", "name": "Send money",
     "why": "Instant transfers, Payme links and cheap cross-border payments in George.",
     "steps": [("2.6", "instant", "Send an instant payment"), ("2.6", "payme", "Share a Payme link"), ("5.1", "george", "Pay abroad in George")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Acceptance at the bank's merchants through Global Payments, online and in store; Mastercard World, the last Mastercard the bank issued, is retired.",
     "steps": [("2.5", "accept", "Mastercard on Global Payments terminals"), ("2.5", "webpay", "Mastercard online through GP webpay"),
               ("2.2", "mcworld", "Mastercard World, retired around 2020")]},
    {"id": "mcnext", "who": "mc", "name": "Where network-free services could land",
     "why": "Where the bank has needs that do not depend on the card network: George AI's spending insight and fraud alerts, Moneyback offers, open banking beside QR and instant payments, business cards, and the Visa agreement whenever it comes up for renewal.",
     "steps": [("3.2", "georgeai", "Spending insight for George AI"), ("3.3", "moneyback", "Card-linked offers"), ("2.6", "qr", "Open banking and scam checks on A2A"),
               ("2.4", "bizdebit", "Commercial and virtual cards"), ("2.2", "credit", "A second network at renewal")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Slovenská sporiteľňa's map",
    "title": "Slovakia's biggest card issuer, Visa-only since 2021",
    "lead": "Slovenská sporiteľňa has worked with Visa since 1994 and in July 2021 agreed that every new card would carry the Visa logo. Its 1.94 million debit, credit and virtual cards, and the phone wallets on them, are Visa. Mastercard reaches the bank only at the point of sale, through the Global Payments joint venture that runs its terminals and online payments. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (H1 2026 results, 30 July 2026) or from Visa, Slovak press and the bank's card disclosures. Mastercard's newsroom was not searched; no joint Mastercard initiative with the bank was found after 2019.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "1.94m cards; exclusive since Jul 2021"],
        ["Credit", "Visa", "Classic and Gold"],
        ["Business debit", "Visa", "Electron, Business, Platinum"],
        ["Wallets", "Visa tokens", "Apple Pay since Jun 2019"],
        ["Acceptance", "Global Payments", "All networks, JV since 2016"],
        ["Mastercard World", "Retired", "Sold until about 2019–20 ⚠"],
        ["A2A", "Instant, Payme, QR", "QR live May 2026"],
    ],
    "sides": {
        "neo": {"dir": "Acceptance at the bank's merchants through Global Payments, online and in store.",
                "deals": "What it does not do: any card the bank issues, wallets, rewards, AI, or instant and QR payments."},
        "snb": {"dir": "Visa on every card and token, Dateio for cashback, OpenAI for George AI, and the Slovak banks' own Payme and QR rails.",
                "deals": "Where they meet: the Global Payments terminals that accept both networks."},
    },
    "tl": [
        ["1994", "Work with Visa begins"],
        ["Feb 2016", "1 million Visa cards, a third of Slovakia's"],
        ["Jun 2016", "Acquiring moves to the Global Payments JV"],
        ["May 2019", "Mastercard World on the Exclusive account"],
        ["Jun 2019", "Apple Pay on Visa cards"],
        ["Jan 2021", "Payme launched"],
        ["Jul 2021", "Exclusive Visa issuing agreement"],
        ["Oct 2025", "Instant payments mandatory"],
        ["Jan 2026", "Free virtual Visa cards; fees reset"],
        ["Mar 2026", "Michaela Bauer becomes chief executive"],
        ["May 2026", "National QR payments go live"],
        ["Sep 2026", "George AI rolls out"],
    ],
    "l": {
        "U": {"d": 0, "s": "Every customer carries Visa.", "gap": "All 1.94 million cards the bank issues are Visa; merchants accept Mastercard through Global Payments.",
              "neo": "Merchants taking Mastercard cards.", "snb": "Cardholders, wallet users, borrowers, investors."},
        "L5": {"d": 0, "s": "The front doors are the bank's.", "gap": "George, branches and ATMs are the bank's own.", "neo": "None.", "snb": "George, branches, ATMs, client centre."},
        "L4": {"d": 0, "s": "The business lines carry Visa cards.", "gap": "Accounts and business banking come with Visa debit; loans, investing and insurance have no network role.",
               "neo": "None.", "snb": "Accounts, housing loans, investing, corporate banking."},
        "L3": {"d": 0, "s": "Services are the bank's or its partners'.", "gap": "Security is the bank's own, George AI runs on OpenAI and Moneyback on Dateio.",
               "neo": "None.", "snb": "Security, George AI, Moneyback, credit bureau."},
        "L2": {"d": 1, "s": "Acceptance takes Mastercard; issuing is Visa.", "gap": "Global Payments accepts every network; debit, credit, virtual and business cards are Visa, and account rails are the banks' own.",
               "neo": "Terminals and GP webpay.", "snb": "Visa cards and tokens, SEPA Instant, Payme, QR."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's; the Erste parent uses Mastercard in Austria.", "neo": "None.", "snb": "Capital, Erste, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
