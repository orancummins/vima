"""Zagrebačka banka's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from zaba_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Croatia's largest bank as five discs that stack into one platform, from a quarter of the country's banking assets "
       "and UniCredit's ownership at the bottom to m-zaba, e-zaba and more than 100 locations at the top. Click the stack "
       "to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, "
       "joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Students & young people", "graduation-cap"),
    ("prime", "Prime clients & investors", "gem"),
    ("home", "Homebuyers", "house"),
    ("sme", "Small businesses & merchants", "store"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer, more than 1.3 million account holders among them: everyday customers, students and "
              "young people, Prime clients and investors, homebuyers, small businesses and merchants, and corporates.")

WHO = {"con": "A Zaba customer", "young": "A student", "prime": "A Prime client", "home": "A homebuyer",
       "sme": "A shop owner", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "An account, a Debit Mastercard, m-zaba, card controls and IziPay.",
     "steps": [("4.1", "accounts", "Open an account"), ("2.1", "debit", "Pay with Debit Mastercard"),
               ("5.1", "mzaba", "Run it in m-zaba"), ("3.1", "cardsec", "Approve online payments with m-token"),
               ("2.6", "izipay", "Send money to a phone number")]},
    {"id": "card", "who": "con", "name": "Pay by card and spread the cost",
     "why": "A Mastercard credit card, interest-free instalments, a phone wallet and points.",
     "steps": [("2.2", "credit", "Open a credit card in m-zaba"), ("2.4", "wallets", "Add it to Apple Pay or Google Pay"),
               ("2.3", "instal", "Pay in up to 36 instalments"), ("3.3", "mpc", "Collect MultiPlusCard points")]},
    {"id": "online", "who": "con", "name": "Shop online safely",
     "why": "A single-use virtual card, 3-D Secure and Zaba's anti-fraud advice.",
     "steps": [("2.1", "virtual", "Create a single-use virtual card"), ("3.1", "cardsec", "Confirm with m-token"),
               ("3.1", "fraudcamp", "Learn to spot scams"), ("2.3", "postsplit", "Split it later if needed")]},
    {"id": "student", "who": "young", "name": "Start out as a student",
     "why": "A youth package, m-student in the canteen and a first credit card.",
     "steps": [("4.1", "accounts", "Open a youth package"), ("5.1", "mstudent", "Pay for lunch with m-student"),
               ("2.2", "credit", "Take a Student Mastercard")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "Property data, an adviser and a fixed-rate home loan.",
     "steps": [("3.4", "npuls", "Read Nekretninski puls"), ("5.3", "branches", "See an adviser"),
               ("4.1", "homeloans", "Take a home loan")]},
    {"id": "prime", "who": "prime", "name": "Grow wealth with a Prime banker",
     "why": "Prime banking, UniCredit Invest funds, pensions and premium card benefits.",
     "steps": [("4.2", "prime", "Get a Prime banker"), ("4.3", "ucinv", "Invest in UniCredit Invest funds"),
               ("4.3", "btc", "Take a Bitcoin ETF certificate"), ("3.3", "lounge", "Use airport lounges")]},
    {"id": "merchant", "who": "sme", "name": "Take card payments",
     "why": "POS, SoftPOS or Fiskal POS, online acceptance and the merchant portal.",
     "steps": [("2.5", "accept", "Get a free POS terminal"), ("2.5", "softpos", "Or take taps on a phone"),
               ("2.5", "fiskal", "Combine till and terminal"), ("2.5", "ecom", "Sell online"),
               ("5.4", "bizdigital", "Track sales in the portal")]},
    {"id": "corp", "who": "corp", "name": "Finance a company",
     "why": "Corporate banking, mini bonds, DealSync, business cards and leasing.",
     "steps": [("4.5", "corp", "Borrow and trade"), ("4.5", "minibond", "Issue a mini bond"),
               ("3.4", "dealsync", "Find a partner on DealSync"), ("4.4", "bizcards", "Give staff business Mastercards"),
               ("4.6", "leasing", "Lease vehicles")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Every card Zaba issues since the switch from Visa, every wallet token, Priceless and LoungeKey.",
     "steps": [("2.1", "debit", "Debit Mastercard on every account"), ("2.2", "credit", "Mastercard credit cards"),
               ("4.4", "bizcards", "Business Mastercards"), ("2.4", "wallets", "Mastercard tokens in wallets"),
               ("3.3", "priceless", "Priceless offers")]},
    {"id": "mcnext", "who": "mc", "name": "Where scam tools, Click to Pay and acquiring could land",
     "why": "Where Zaba has needs and Mastercard is not yet in: scam scoring as instant payments arrive, tokenised checkout beside the virtual card, instalments and acquiring tools, virtual commercial cards and card-linked offers.",
     "steps": [("3.1", "fraudcamp", "Scam scoring for instant transfers"), ("2.1", "virtual", "Click to Pay beside the virtual card"),
               ("2.5", "accept", "Gateway and risk tools for merchants"), ("4.4", "bizcards", "Virtual cards and spend controls"),
               ("3.3", "perks", "Card-linked offers")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Zaba's map",
    "title": "Croatia's biggest bank went all-Mastercard in 2024–25; the next step is beyond the card",
    "lead": "In May 2024 Zagrebačka banka and Mastercard began moving about two million debit cards from Visa, and Mastercard became the only brand on the cards Zaba issues: debit, consumer and business credit, the new single-use virtual card and every wallet token. The switch follows UniCredit's 2023 group deal with Mastercard. Zaba still accepts Visa and Diners as an acquirer, runs its own instalments and IziPay transfers, and SEPA Instant arrived in October 2025. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (H1 2026 statements, 22 July 2026; zaba.hr, read 17 October 2026) or from press on the 2024 switch. Card counts by product, the acquiring share and the migration's completion date are not published; the Lider articles could not be opened.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Mastercard", "~2m cards moved from Visa, 2024–25"],
        ["Consumer credit", "Mastercard", "Standard, Platinum, Student, go!card"],
        ["Business credit", "Mastercard", "Three Business Mastercards"],
        ["Virtual card", "Mastercard", "Single-use, January 2026"],
        ["Wallets", "Mastercard tokens", "Apple, Google, Garmin Pay"],
        ["Benefits", "Priceless, LoungeKey", "Platinum and Business"],
        ["Acquiring", "All networks", "Mastercard, Visa, Maestro, Diners"],
        ["Account-to-account", "IziPay, SEPA Instant", "Instant mandatory since Oct 2025"],
    ],
    "sides": {
        "neo": {"dir": "Every card Zaba issues, every wallet token, 3-D Secure on those cards, Priceless and LoungeKey.",
                "deals": "What it does not do: Zaba's own instalments and offers, IziPay and SEPA Instant, the m-token, open banking or AI, as far as public sources show."},
        "snb": {"dir": "Visa and Diners on Zaba's terminals, IziPay and SEPA Instant between accounts, MultiPlusCard for points, UniCredit for APIs and AI.",
                "deals": "Where they meet: every Zaba terminal, which takes any network, and every transfer that could have been a card payment."},
    },
    "tl": [
        ["Mar 2002", "Zaba joins UniCredit"],
        ["Feb 2019", "m-novčanik phone payments on Mastercard and Maestro"],
        ["Mar 2019", "PSD2 APIs through UniCredit"],
        ["Jan 2023", "Croatia adopts the euro"],
        ["May 2023", "UniCredit–Mastercard group deal"],
        ["May 2024", "Two million debit cards start moving from Visa"],
        ["2025", "Mastercard the only brand on Zaba cards"],
        ["Oct 2025", "SEPA Instant mandatory in Croatia"],
        ["Jan 2026", "Single-use virtual card"],
        ["Sep 2026", "Gold Mastercard loses lounge access"],
    ],
    "l": {
        "U": {"d": 2, "s": "Every Zaba cardholder carries Mastercard.", "gap": "Debit, credit and business cardholders all carry Mastercard; merchants take every network; transfers go account to account.",
              "neo": "Every cardholder, consumer and business.", "snb": "Merchants taking Visa and Diners; IziPay and instant-transfer users."},
        "L5": {"d": 0, "s": "The front doors are Zaba's.", "gap": "m-zaba, e-zaba, branches and portals are the bank's own.", "neo": "None.", "snb": "m-zaba, e-zaba, e-poslovnica, branches."},
        "L4": {"d": 1, "s": "Accounts and business cards carry Mastercard; lending and investing do not.", "gap": "Every account comes with Debit Mastercard and business cards are Mastercard; loans, Prime, funds, leasing and Bosnia are not card lines.",
               "neo": "Account debit cards, business cards.", "snb": "Loans, Prime, UniCredit Invest, pensions, corporate finance, Bosnia ⚠."},
        "L3": {"d": 1, "s": "Priceless and LoungeKey are Mastercard's; fraud, APIs and points are not.", "gap": "Priceless and lounges ride on Mastercard; the anti-fraud work, PSD2 APIs, MultiPlusCard and AI are Zaba's, UniCredit's or partners'.",
               "neo": "Priceless, LoungeKey, 3-D Secure.", "snb": "ZABAci oko campaign, PSD2 APIs, MultiPlusCard, DealSync."},
        "L2": {"d": 2, "s": "All issuing on Mastercard; acceptance neutral; transfers account to account.", "gap": "Mastercard holds debit, credit, the virtual card and wallets; Visa shares the terminals; IziPay and SEPA Instant move money without cards.",
               "neo": "Debit, credit, virtual card, wallet tokens.", "snb": "Visa and Diners acceptance, IziPay, SEPA Instant, correspondent banking."},
        "L1": {"d": 0, "s": "The bank's and UniCredit's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, UniCredit, heritage, m-token, strategy."},
    },
    "t": area_lens(LAYERS),
}
