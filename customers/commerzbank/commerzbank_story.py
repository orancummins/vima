"""Commerzbank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from commerzbank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Germany's bank for the Mittelstand as five discs that stack into one platform, from a record €1.8 billion half-year "
       "profit and UniCredit's 49.65% position at the bottom to the apps, about 400 locations and a network in 40 countries "
       "at the top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it "
       "light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard "
       "goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("home", "Homebuyers", "house"),
    ("inv", "Investors & savers", "trending-up"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Mittelstand & corporates", "factory"),
    ("pl", "mBank customers", "flag"),
]
USERS_DESC = ("Six kinds of customer: everyday customers, homebuyers, comdirect investors and savers, small businesses, "
              "about 24,000 corporate client groups and about 6 million mBank customers in Poland, the Czech Republic and Slovakia.")

WHO = {"con": "A Commerzbank customer", "home": "A homebuyer", "inv": "An investor", "sme": "A small business",
       "corp": "A Mittelstand treasurer", "pl": "An mBank customer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account with a girocard carrying Visa Debit, a phone wallet, the app with Ava, and fraud checks.",
     "steps": [("4.1", "retail", "Open a current account"), ("2.1", "girocard", "Pay with the girocard"), ("2.5", "wallets", "Pay by phone"),
               ("5.1", "app", "Run it in the app"), ("3.2", "ava", "Ask Ava"), ("3.1", "fraudai", "Protected by Fraud AI")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "Classic, Gold and Premium credit cards, now on Visa, or a standalone Mastercard Debit.",
     "steps": [("2.2", "credit", "Take a credit card"), ("2.1", "mcdebit", "Or choose Mastercard Debit"), ("3.1", "idcheck", "Confirm online with 3-D Secure"),
               ("3.3", "offers", "Use the card perks")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "Mortgages through branches and the advice centre.",
     "steps": [("5.2", "branches", "Talk to an adviser"), ("4.1", "mortgages", "Take a mortgage")]},
    {"id": "invest", "who": "inv", "name": "Invest and trade",
     "why": "comdirect brokerage and digital portfolio management.",
     "steps": [("5.1", "app", "Open the comdirect app"), ("4.2", "comdirect", "Trade with comdirect"), ("4.2", "wealth", "Hand it to portfolio management")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account and cards, Pliant corporate cards and card acceptance with Commerz Globalpay.",
     "steps": [("4.1", "retail", "Open a business account"), ("2.3", "bizcards", "Take a Business Card"), ("2.3", "pliant", "Issue Pliant cards to staff"),
               ("2.4", "globalpay", "Take cards with Commerz Globalpay")]},
    {"id": "corp", "who": "corp", "name": "Finance trade as the Mittelstand",
     "why": "Corporate Clients, cash management and trade finance in more than 40 countries.",
     "steps": [("4.3", "corporates", "Bank with Corporate Clients"), ("2.6", "cash", "Move money and finance trade"), ("5.3", "network", "Use the network abroad"),
               ("2.6", "crypto", "Hold digital assets")]},
    {"id": "poland", "who": "pl", "name": "Bank with mBank in Poland",
     "why": "mBank's app, Visa debit, Mastercard credit and BLIK.",
     "steps": [("4.4", "mbank", "Open an mBank account"), ("2.7", "mbcards", "Pay with an mBank card"), ("2.7", "blik", "Pay with BLIK")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The standalone Mastercard Debit, the credit cards not yet switched, Identity Check, acceptance at Commerz Globalpay and mBank's Mastercard credit cards.",
     "steps": [("2.1", "mcdebit", "Mastercard Debit"), ("2.2", "credit", "Mastercard Classic until switched"), ("3.1", "idcheck", "Identity Check"),
               ("2.4", "globalpay", "Acceptance at Commerz Globalpay"), ("2.7", "mbcards", "World Elite at mBank")]},
    {"id": "mcnext", "who": "mc", "name": "Where UniCredit, commercial cards and agents could land",
     "why": "Where Commerzbank has needs and Mastercard is not yet in: UniCredit's group card choice, business and Mittelstand cards, scam and identity tools, Agent Pay for Ava, and merchant services.",
     "steps": [("1.6", "unicredit", "UniCredit's Mastercard partnership"), ("2.3", "bizcards", "Business and virtual cards"), ("4.3", "corporates", "Commercial cards for the Mittelstand"),
               ("3.1", "fraudai", "Scam and identity scores"), ("3.2", "ava", "Agent Pay for Ava"), ("2.4", "globalpay", "Merchant risk and data")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Commerzbank's map",
    "title": "A Visa bank with a Mastercard owner at the door",
    "lead": "Since February 2025 Visa has been Commerzbank's preferred card partner. Girocards carry Visa Debit, the credit range is Visa, and Mastercard Classic holders have been switched since July 2026; comdirect has been Visa since 2020. Mastercard keeps a standalone Mastercard Debit, acceptance at Commerz Globalpay and mBank's credit cards. UniCredit, which made Mastercard its issuing partner across 13 banks in 2023, now holds about 49.65%. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (Q2 2026 results, 6 August 2026; FY2025 results, 11 February 2026) or from Commerzbank, mBank and press pages. Card counts by network are not public; the business cards' network is not stated; UniCredit's stake and approvals rest on UniCredit's documents, which could not be re-read here ⚠.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "girocard + Visa Debit", "Every current account, from Feb 2025"],
        ["Mastercard Debit", "Mastercard", "Standalone, €3.50 a month"],
        ["Credit", "Mastercard to Visa", "Switch letters from July 2026"],
        ["comdirect", "Visa", "Preferred partner since 2020"],
        ["Business cards", "Not stated ⚠", "Pliant on Visa"],
        ["Acceptance", "Commerz Globalpay", "Global Payments JV, all networks"],
        ["mBank", "Visa debit, Mastercard credit", "World Elite Mastercard"],
        ["Owner", "UniCredit ~49.65% ⚠", "Mastercard's partner since 2023"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard Debit, credit cards until switched, Identity Check, acceptance at Commerz Globalpay, mBank credit, and BLIK's contactless tie-up.",
                "deals": "What it does not do: the girocard co-badge, the new credit book, comdirect, Pliant, Wero, fraud AI or perks."},
        "snb": {"dir": "Visa on the girocards, credit, comdirect and Pliant; girocard at home; Wero to come; Amex Platinum; and Commerzbank's own Fraud AI and Ava.",
                "deals": "Where they meet: UniCredit's control, which would put a Mastercard group above a Visa bank."},
    },
    "tl": [
        ["2020", "comdirect makes Visa its preferred partner"],
        ["Oct 2021", "Mastercard Debit co-badge reported ⚠"],
        ["May 2023", "UniCredit makes Mastercard its group partner"],
        ["Jan 2024", "Commerz Globalpay with Global Payments"],
        ["Feb 2025", "Visa becomes preferred card partner"],
        ["Feb 2026", "Commerzbank will join Wero"],
        ["Mar 2026", "UniCredit exchange offer"],
        ["Jul 2026", "Mastercard Classic holders asked to switch to Visa"],
        ["Oct 2026", "UniCredit approvals arrive ⚠"],
    ],
    "l": {
        "U": {"d": 1, "s": "Mastercard Debit holders, unconverted credit holders and mBank credit holders carry Mastercard.",
              "gap": "girocard holders carry Visa Debit and credit holders are moving to Visa; mBank credit and the standalone debit stay Mastercard.",
              "neo": "Mastercard Debit, legacy credit, mBank credit holders.", "snb": "girocard holders, comdirect, Pliant users, investors, corporates."},
        "L5": {"d": 0, "s": "The front doors are the group's.", "gap": "Apps, branches and the corporate network are Commerzbank's; Global Payments is the only network-neutral partner.",
               "neo": "Acceptance through Global Payments.", "snb": "Apps, branches, Visa and Pliant partners."},
        "L4": {"d": 1, "s": "Accounts carry Visa; mBank credit carries Mastercard.", "gap": "German accounts come with Visa Debit girocards; mBank's credit cards are Mastercard.",
               "neo": "mBank credit.", "snb": "Accounts, mortgages, comdirect, wealth, Corporate Clients."},
        "L3": {"d": 1, "s": "Identity Check on Mastercard cards; the rest is Commerzbank's or Visa's.", "gap": "Fraud AI and Ava are in-house; perks are Visa's.",
               "neo": "Identity Check.", "snb": "Fraud AI, Ava, cobaGPT, Visa perks."},
        "L2": {"d": 1, "s": "Mastercard Debit, legacy credit, acceptance and mBank credit; Visa takes the rest.", "gap": "Visa holds the girocard co-badge, new credit, comdirect and Pliant; Wero and corporate rails are not card-based.",
               "neo": "Mastercard Debit, legacy credit, Commerz Globalpay, mBank credit, BLIK contactless.", "snb": "girocard, Visa, Amex, Wero, SEPA, crypto custody."},
        "L1": {"d": 0, "s": "The group's own foundation; UniCredit is the open question.", "gap": "Nothing in the foundation is Mastercard's; UniCredit's group partner is.",
               "neo": "None directly.", "snb": "Capital, brands, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
