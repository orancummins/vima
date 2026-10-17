"""Bank Audi's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bankaudi_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Lebanon's oldest big bank as five discs that stack into one platform, from $15.1 billion of assets and a "
       "balance sheet waiting on the Gap law at the bottom to the Bank Audi and neo apps, branches and ATMs at the top. "
       "Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up "
       "across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("dig", "neo digital customers", "smartphone"),
    ("teen", "Teens & families", "graduation-cap"),
    ("aff", "Affluent & private clients", "gem"),
    ("sme", "Entrepreneurs & SMEs", "briefcase"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer: everyday and payroll customers in Lebanon, neo's digital customers, teens and their "
              "parents, affluent and private clients from Beirut to Geneva and the Gulf, entrepreneurs and small firms, "
              "and the corporates that are borrowing again in fresh dollars.")

WHO = {"con": "A Bank Audi customer", "dig": "A neo customer", "teen": "A teenager", "aff": "A private client",
       "sme": "An entrepreneur", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day in fresh dollars",
     "why": "The everyday loop in a two-dollar economy: a payroll account, a Mastercard debit card in fresh dollars or lira, the app and 3-D Secure.",
     "steps": [("4.1", "retail", "Get paid into Bank Audi"), ("2.2", "debit", "Pay with a debit card"), ("2.2", "fresh", "Spend fresh dollars or lira"),
               ("5.1", "app", "Run it in the app"), ("3.1", "secure", "Check out with 3-D Secure")]},
    {"id": "digital", "who": "dig", "name": "Bank on the phone with neo",
     "why": "neo: open in the app, hold several currencies, pay by QR or Google Pay, cash out at ATMs and agents.",
     "steps": [("5.1", "neoapp", "Open neo in the app"), ("4.2", "neobank", "Hold dollars, lira and more"), ("2.3", "neocard", "Get a multi-currency card"),
               ("2.4", "gpay", "Add it to Google Pay"), ("2.6", "transfers", "Pay by QR or mobile number"), ("2.6", "cashout", "Cash out without a card")]},
    {"id": "borrow", "who": "dig", "name": "Borrow without a branch",
     "why": "neo's digital loans and salary advances, and its Cedar Miles credit card.",
     "steps": [("3.3", "dlend", "Apply for a loan in the app"), ("2.3", "neocredit", "Take a neo Cedar Miles card")]},
    {"id": "teens", "who": "teen", "name": "Give a teenager a card",
     "why": "neo teens: a card and an app, with the parent watching.",
     "steps": [("4.1", "teens", "Open neo teens"), ("2.3", "neocard", "Spend with a card"), ("5.1", "neoapp", "Parents see it live")]},
    {"id": "travel", "who": "aff", "name": "Travel and earn miles",
     "why": "The MEA Cedar Miles World Elite card, lounges and the experiences reserved for top spenders.",
     "steps": [("2.1", "cedar", "Carry Cedar Miles World Elite"), ("3.2", "offers", "Use hotel, car and lounge offers"), ("3.2", "experiences", "Join a Champions League Final trip")]},
    {"id": "wealth", "who": "aff", "name": "Keep wealth abroad",
     "why": "Private banking in Geneva, wealth management in the Gulf and banking in France.",
     "steps": [("5.2", "branches", "Meet a banker"), ("4.5", "private", "Bank privately in Geneva"), ("4.5", "acap", "Invest with Audi Capital"), ("4.6", "france", "Bank in France")]},
    {"id": "sme", "who": "sme", "name": "Start taking digital payments",
     "why": "neo Business and Mastercard's programme for 10,000 entrepreneurs: an account, a business debit card, a terminal and transfers.",
     "steps": [("4.3", "neobiz", "Open neo Business free"), ("2.5", "pos", "Take cards at a terminal"), ("2.6", "transfers", "Collect by QR and transfer")]},
    {"id": "corp", "who": "corp", "name": "Borrow and move money as a corporate",
     "why": "Fresh-dollar lending, treasury and settlement over BDL's rails.",
     "steps": [("4.4", "corporate", "Borrow in fresh dollars"), ("2.6", "rtgs", "Settle over BDL-RTGS"), ("4.4", "treasury", "Place liquidity with treasury")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Every card Bank Audi and neo issue, the Cedar Miles co-brand, Google Pay tokens, neo Business and offers such as Toters.",
     "steps": [("2.1", "credit", "Credit cards on Mastercard"), ("2.1", "cedar", "Cedar Miles World Elite"), ("2.2", "debit", "Debit in fresh dollars and lira"),
               ("2.4", "gpay", "Google Pay with Mastercard tokens"), ("4.3", "neobiz", "neo Business with Mastercard"), ("3.2", "offers", "Toters offer")]},
    {"id": "mcnext", "who": "mc", "name": "Where acceptance, remittances and tokens could land",
     "why": "Where Bank Audi has needs and Mastercard is not yet in: acceptance for neo Business's merchants, remittances into fresh-dollar neo accounts, Click to Pay beyond Google Pay, fraud tools for digital onboarding and Priceless for top spenders.",
     "steps": [("2.5", "pos", "Tap on Phone and acquiring tools"), ("2.6", "cashout", "Mastercard Move for diaspora remittances"), ("2.4", "gpay", "Click to Pay and more wallets"),
               ("3.1", "secure", "Identity and fraud scoring"), ("3.2", "experiences", "Priceless for top spenders")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Bank Audi's map",
    "title": "A Mastercard issuer in a cash economy, now selling acceptance",
    "lead": "Every card on Bank Audi's and neo's pages in October 2026 is a Mastercard: World Elite credit, the MEA Cedar Miles co-brand, debit in fresh dollars and lira, and neo's multi-currency cards. Google Pay arrived for these cardholders in June 2025, and in September 2026 neo Business and Mastercard set out to put 10,000 entrepreneurs on digital payments. Lebanon still runs largely on cash, wallets and agents, and the bank is waiting on its restructuring. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (2025 Annual Report, 8 June 2026) or from Bank Audi, neo, BDL, Mastercard and press. The card listing could not be read card by card; debit and neo networks are inferred from tier names and the Google Pay launch ⚠.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit", "Mastercard", "World, World Elite, Platinum"],
        ["Co-brand", "MEA Cedar Miles", "World Elite Mastercard since 2013 ⚠"],
        ["Debit", "Mastercard ⚠", "Fresh dollars and lira"],
        ["neo", "Mastercard ⚠", "Multi-currency debit, Cedar Miles credit"],
        ["Wallet", "Google Pay", "Mastercard holders, June 2025"],
        ["SMEs", "neo Business", "10,000 entrepreneurs, September 2026"],
        ["Visa", "One co-brand", "Mercedes-Benz card, 2015 ⚠"],
        ["Transfers", "BDL rails, wallets", "No national instant scheme ⚠"],
    ],
    "sides": {
        "neo": {"dir": "Bank Audi's and neo's cards, the Cedar Miles co-brand, Google Pay tokens, neo Business debit and acceptance training, and offers such as Toters.",
                "deals": "What it does not do: transfers and QR, BDL settlement, cash-out through agents, lending, private banking and wealth."},
        "snb": {"dir": "BDL-RTGS and BDL-CLEAR, licensed wallets and cash agents, Bank Audi's own QR and transfers, and Visa at the other big Lebanese banks.",
                "deals": "Where they meet: merchant acceptance, where BDL capped fees on both networks' cards."},
    },
    "tl": [
        ["Sep 2012", "ABC contactless Mastercard co-brand"],
        ["2013", "Ultimate Cedar Miles World Elite Mastercard ⚠"],
        ["Apr 2020", "BDL Circular 150: fresh dollars for card use"],
        ["2024", "neo by Bank Audi launched"],
        ["Mar 2025", "Odea Bank sale completed"],
        ["Jun 2025", "Google Pay for Mastercard holders"],
        ["Jan 2026", "Sherine Audi becomes chair"],
        ["Jun 2026", "Dollar cards payable in lira at POS"],
        ["Sep 2026", "10,000 entrepreneurs with Mastercard; Mastercard–BDL acceptance programme"],
        ["Oct 2026", "Toters offer for Mastercard cards"],
    ],
    "l": {
        "U": {"d": 2, "s": "Card-holding customers carry Mastercard.",
              "gap": "Credit, debit and neo cardholders carry Mastercard; private clients abroad and corporates mostly do not use cards here.",
              "neo": "Cardholders, neo customers, neo Business SMEs.", "snb": "Private-banking and wealth clients, corporates."},
        "L5": {"d": 0, "s": "The front doors are Bank Audi's.", "gap": "Apps, branches, ATMs and agents are the bank's or partners'.", "neo": "None.", "snb": "Apps, branches, ATMs, agents, 1570."},
        "L4": {"d": 1, "s": "neo Business is Mastercard's; the rest carries its cards.", "gap": "The SME programme is joint; retail and neo come with Mastercard cards; corporate, private and wealth lines do not.",
               "neo": "neo Business; cards inside retail and neo.", "snb": "Corporate lending, treasury, private banking, Audi Capital, France, Qatar."},
        "L3": {"d": 1, "s": "Offers and 3-D Secure touch Mastercard ⚠.", "gap": "The Toters offer and the Champions League experience are Mastercard's; compliance, lending and AI are the bank's.",
               "neo": "Toters offer, Champions League ⚠, 3-D Secure.", "snb": "AML, digital lending, AI."},
        "L2": {"d": 2, "s": "Every card rides on Mastercard; transfers and cash do not.", "gap": "Credit, debit, neo cards and Google Pay are Mastercard; QR transfers, BDL settlement and agents are not.",
               "neo": "Credit, Cedar Miles, debit, neo cards, Google Pay.", "snb": "QR and transfers, BDL-RTGS, agents, any-network POS."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, governance, technology, restructuring."},
    },
    "t": area_lens(LAYERS),
}
