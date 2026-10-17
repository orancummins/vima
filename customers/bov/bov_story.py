"""Bank of Valletta's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bov_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Malta's largest bank as five discs that stack into one platform, from €17.6 billion of assets and a quarter-state "
       "shareholding at the bottom to BOV Mobile, branches and business hubs at the top. Click the stack to open it. Choose "
       "who you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("home", "Homebuyers", "house"),
    ("saver", "Savers & investors", "coins"),
    ("sme", "Small businesses", "briefcase"),
    ("merch", "Merchants", "store"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer: Maltese households who bank day to day, homebuyers, savers and investors, small "
              "businesses, the merchants who take cards through SmartPay, and the corporates behind Malta's lending growth.")

WHO = {"con": "A BOV customer", "home": "A homebuyer", "saver": "A saver", "sme": "A small business", "merch": "A merchant", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Cashlink Visa debit card, the app and payee checks.",
     "steps": [("4.1", "accounts", "Open a current account"), ("2.1", "debit", "Pay with Cashlink Visa"), ("5.1", "app", "Run it in BOV Mobile"),
               ("3.1", "vop", "Payee checked on transfers")]},
    {"id": "card", "who": "con", "name": "Pay and borrow on a card",
     "why": "A BOV Visa credit card in Apple Pay or BOV Pay, earning loyalty points.",
     "steps": [("2.2", "credit", "Take a Visa credit card"), ("2.4", "applepay", "Add it to Apple Pay"), ("2.4", "bovpay", "Or tap with BOV Pay"),
               ("3.3", "loyalty", "Collect loyalty rewards")]},
    {"id": "send", "who": "con", "name": "Send money instantly",
     "why": "SEPA Instant in under ten seconds, to an IBAN or a mobile number.",
     "steps": [("5.1", "app", "Open BOV Mobile"), ("2.6", "mobilepay", "Pay a mobile number"), ("2.6", "sepainst", "Send by SEPA Instant"),
               ("3.1", "vop", "Payee name checked")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "Home loans from the new finance hubs, with Mapfre cover sold in branch.",
     "steps": [("5.2", "hubs", "Visit a Home Finance Hub"), ("4.2", "homeloans", "Take a home loan"), ("4.6", "insurance", "Insure it with Mapfre")]},
    {"id": "save", "who": "saver", "name": "Save and invest",
     "why": "Advice, funds and stockbroking from Malta's largest wealth franchise.",
     "steps": [("5.2", "branches", "See an investment adviser"), ("4.4", "wealth", "Get wealth advice"), ("4.4", "funds", "Buy BOV funds"),
               ("4.4", "stockbroking", "Trade on the Malta Stock Exchange")]},
    {"id": "merchant", "who": "merch", "name": "Take card payments",
     "why": "SmartPay terminals, an online gateway and MobilePOS, settling into a BOV business account.",
     "steps": [("4.3", "business", "Open a business account"), ("2.5", "smartpay", "Take cards with SmartPay"), ("2.5", "mobilepos", "Or with MobilePOS")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account, Visa business cards and trade finance from the Business Hub.",
     "steps": [("5.2", "hubs", "Bank at the Business Hub"), ("4.3", "business", "Open a business account"), ("2.3", "corpcards", "Spend on a Visa business card"),
               ("2.7", "trade", "Finance trade")]},
    {"id": "corp", "who": "corp", "name": "Borrow and move money as a corporate",
     "why": "Commercial lending, trade finance and instant euro payments.",
     "steps": [("4.3", "corplending", "Borrow for investment"), ("2.7", "trade", "Pay suppliers abroad"), ("2.6", "sepainst", "Pay instantly in euro")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Mastercard cards accepted at SmartPay merchants; the credit programme it lost in 2021; gift cards from 2011.",
     "steps": [("2.5", "smartpay", "Mastercard accepted at SmartPay ⚠"), ("2.5", "mobilepos", "And on MobilePOS ⚠"),
               ("2.2", "mcexit", "Credit cards moved to Visa, 2021"), ("2.2", "prepaid", "Prepaid gift cards, 2011 ⚠")]},
    {"id": "mcnext", "who": "mc", "name": "Where Mastercard could land at BOV",
     "why": "Where BOV has needs and the card network does not decide: scam scoring for instant payments, data for its CRM programme, merchant tools for SmartPay, and a second network for a premium or business card.",
     "steps": [("3.1", "vop", "Scam scoring beside the payee check"), ("3.2", "crm", "Enrichment and open finance for CRM"),
               ("2.5", "smartpay", "Merchant risk and offers for SmartPay"), ("5.1", "omnichannel", "Identity checks in digital onboarding"),
               ("2.3", "corpcards", "A Mastercard commercial or premium card")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Bank of Valletta's map",
    "title": "Malta's biggest issuer, all Visa since Mastercard left in 2021",
    "lead": "Bank of Valletta closed its only Mastercard programme, a credit card, on 1 December 2021 and moved the holders to Visa. Every BOV card since, from Cashlink debit to the 2025 corporate range, runs on Visa, and its Apple Pay and BOV Pay tokens are Visa's. Mastercard's live presence is acceptance at BOV's SmartPay merchants. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (H1 2026 interim report, 29 July 2026; FY2025 results, 26 March 2026) or from Maltese business press. bov.com refused automated reads, so card networks come from product guides, press releases and the 2021 coverage of the Mastercard exit.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "Cashlink Visa"],
        ["Credit", "Visa", "Mastercard closed 1 Dec 2021"],
        ["Corporate cards", "Visa", "New suite, June 2025"],
        ["Wallets", "Apple Pay, BOV Pay", "Visa tokens"],
        ["Acceptance", "BOV SmartPay", "Accepts Mastercard ⚠"],
        ["Instant payments", "SEPA Instant", "Outgoing from Oct 2025"],
        ["Rival issuer", "BNF Bank", "Mastercard partnership, Feb 2026"],
    ],
    "sides": {
        "neo": {"dir": "Acceptance at SmartPay terminals and MobilePOS, and the prepaid gift cards of 2011 ⚠.",
                "deals": "What it does not do: debit, credit, corporate cards, wallets, instant payments, fraud or data."},
        "snb": {"dir": "Visa on every BOV card and token, BOV's own SEPA Instant, payee checks, CRM and AI.",
                "deals": "Where they meet: SmartPay merchants take both networks."},
    },
    "tl": [
        ["2011", "UEFA Champions League Mastercard prepaid cards ⚠"],
        ["Nov 2019", "BOV Pay wallet for Visa cards"],
        ["Apr 2021", "All cards contactless; Apple Pay live"],
        ["Oct 2021", "BOV announces end of Mastercard"],
        ["Dec 2021", "Mastercard credit cards moved to Visa"],
        ["Jun 2025", "Corporate Visa suite and SmartPay"],
        ["Oct 2025", "Outgoing SEPA Instant with payee checks"],
        ["Feb 2026", "BNF Bank partners with Mastercard"],
        ["Late 2026", "2027–29 strategy due"],
    ],
    "l": {
        "U": {"d": 0, "s": "BOV's cardholders carry Visa.",
              "gap": "Every personal and business card is Visa; merchants on SmartPay take Mastercard from other banks' customers.",
              "neo": "Merchants accepting Mastercard ⚠.", "snb": "Every cardholder, saver, homebuyer and business."},
        "L5": {"d": 0, "s": "The front doors are BOV's.", "gap": "App, omnichannel platform, branches and hubs are the bank's own.", "neo": "None.", "snb": "BOV Mobile, branches, hubs."},
        "L4": {"d": 0, "s": "The business lines carry Visa cards.", "gap": "Accounts come with Visa debit; loans, wealth and insurance have no network role.",
               "neo": "None.", "snb": "Accounts, home loans, business banking, wealth, Mapfre."},
        "L3": {"d": 0, "s": "Fraud, data and loyalty are BOV's own.", "gap": "Payee checks, CRM and AI are in-house or with unnamed providers; loyalty sits on Visa cards.",
               "neo": "None.", "snb": "Payee checks, CRM, AI, loyalty."},
        "L2": {"d": 1, "s": "Acceptance takes Mastercard; issuing is all Visa.", "gap": "Visa has debit, credit, corporate cards and tokens; Mastercard is accepted at SmartPay.",
               "neo": "SmartPay and MobilePOS acceptance ⚠.", "snb": "Visa cards and tokens, SEPA Instant, trade."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's; BOV holds Visa shares ⚠.", "neo": "None.", "snb": "Capital, owners, technology, strategy, Visa shares."},
    },
    "t": area_lens(LAYERS),
}
