"""Republic Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from republicbank_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Trinidad and Tobago's largest bank as five discs that stack into one platform, from a TT$134.6 billion group "
       "across 16 countries at the bottom to RepublicOnline, 38 branches and 130 ATMs at the top. Click the stack to open "
       "it. Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined "
       "in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("travel", "Travellers & cardholders", "plane"),
    ("home", "Homebuyers & borrowers", "house"),
    ("sme", "Small businesses & merchants", "briefcase"),
    ("corp", "Corporates & government", "factory"),
    ("inv", "Savers & investors", "coins"),
]
USERS_DESC = ("Six kinds of customer: everyday customers, travellers and cardholders, homebuyers and borrowers, small "
              "businesses and merchants, corporates and government, and savers and investors. Republic does not publish "
              "a customer count.")

WHO = {"con": "A Republic customer", "travel": "A traveller", "home": "A homebuyer", "sme": "A small business",
       "corp": "A corporate treasurer", "inv": "A saver"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "Open online, pay with Visa/LINX debit, bank in the app and get alerts.",
     "steps": [("3.2", "onboard", "Open an account with RepublicOnboard"), ("2.3", "debit", "Pay with Visa/LINX debit"),
               ("5.1", "online", "Bank in RepublicOnline"), ("3.1", "alerts", "Get alerts and lock a card")]},
    {"id": "card", "who": "con", "name": "Take a credit card",
     "why": "A Visa or Mastercard credit card with cash back and balance cover.",
     "steps": [("2.1", "visacc", "Choose a Visa card"), ("2.1", "mccc", "Or a Mastercard"), ("3.3", "cashback", "Earn cash back"),
               ("4.4", "life", "Insure the balance with BalanceCover")]},
    {"id": "travel", "who": "travel", "name": "Travel and earn miles",
     "why": "American Airlines co-brands on both networks, and a prepaid card for US-dollar spend.",
     "steps": [("2.2", "aadvantage", "Earn AAdvantage miles"), ("2.3", "prepaid", "Load a travel prepaid card"),
               ("3.3", "priceless", "Win a Priceless experience")]},
    {"id": "wallet", "who": "con", "name": "Pay by phone",
     "why": "Endcash QR payments, Yooz top-ups and peer-to-peer transfers.",
     "steps": [("2.4", "endcash", "Pay with Endcash"), ("2.4", "yooz", "Top up with Yooz"), ("5.1", "online", "Send money to a friend")]},
    {"id": "home", "who": "home", "name": "Buy a home or a car",
     "why": "Mortgages and loans from T&T's largest branch network.",
     "steps": [("5.2", "branches", "Visit a branch"), ("4.1", "loans", "Take a mortgage or car loan")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business package, card acceptance for every network, and ACH payroll.",
     "steps": [("4.2", "sme", "Open a business package"), ("2.5", "pos", "Take cards at the counter"), ("2.5", "amex", "Accept Amex too"),
               ("2.5", "epay", "Sell online with EPay"), ("2.6", "ach", "Pay staff by ACH")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Corporate banking, corporate cards, wires and ACH.",
     "steps": [("4.3", "cib", "Bank with corporate banking"), ("4.2", "bizcards", "Issue corporate cards"), ("2.6", "wires", "Send wires and RTGS")]},
    {"id": "invest", "who": "inv", "name": "Save and invest",
     "why": "Republic's funds, retirement plans and digital life insurance.",
     "steps": [("4.4", "funds", "Invest in a Republic fund"), ("4.4", "life", "Buy life cover online")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Half the credit range, the AAdvantage co-brand, the Priceless Carnival, the BVI's Mastercard Black and acceptance at Republic's terminals.",
     "steps": [("2.1", "mccc", "Mastercard Classic and Platinum"), ("2.2", "aadvantage", "AAdvantage Mastercard"),
               ("3.3", "priceless", "Priceless Carnival"), ("4.5", "bvi", "Mastercard Black in the BVI"), ("2.5", "pos", "Acceptance at Republic terminals")]},
    {"id": "mcnext", "who": "mc", "name": "Where Mastercard could land",
     "why": "Where Republic has needs and Mastercard is not yet in: tokenised phone wallets, Endcash funding, identity for digital onboarding, commercial cards and the coming instant-payment rail.",
     "steps": [("2.4", "cardinwallet", "Tokenised cards in phone wallets"), ("2.4", "endcash", "Tokens behind Endcash"),
               ("3.2", "onboard", "Identity checks for onboarding"), ("4.2", "bizcards", "Virtual and fleet cards"),
               ("2.6", "instant", "A2A tools for the instant rail")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Republic Bank's map",
    "title": "Visa on every debit card, Mastercard on part of the credit book",
    "lead": "Republic is Trinidad and Tobago's largest credit card operator and issues on both networks: about five of its twelve credit programmes are Mastercard, including the AAdvantage co-brand and Platinum, while Visa has the top tiers, the PriceSmart co-brand, prepaid and every debit card (co-badged with the domestic LINX network). Mastercard ran a Priceless Carnival with Republic in 2024 and powers the BVI bank's Mastercard Black. Both networks paid incentives in FY2025. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are RFHL's own (2025 Annual Report; results to 30 June 2026) or from Republic's product pages, the Central Bank and press. No network agreement has been published; Apple Pay and Google Pay status in T&T and Endcash's current status are unconfirmed.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa/LINX", "Every card; domestic LINX use"],
        ["Credit", "Visa and Mastercard", "About 7 Visa and 5 Mastercard programmes"],
        ["Co-brands", "AAdvantage on both; PriceSmart Visa", "Visa Infinite at the top"],
        ["Prepaid", "Visa", "Gift and travel cards"],
        ["Acquiring", "Visa, Mastercard, LINX, Amex", "Republic's own terminals and EPay"],
        ["Marketing", "Mastercard Priceless", "Carnival, Feb 2024"],
        ["Group", "Visa in Barbados and Ghana", "Mastercard Black in the BVI, Apr 2024"],
        ["Incentives", "Visa and Mastercard", "Booked in FY2025"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard Classic, Platinum and the AAdvantage cards, the AAdvantage Corporate card, Priceless, acceptance at Republic's terminals and ATMs, and the BVI's Mastercard Black.",
                "deals": "What it does not do: debit, prepaid, the top credit tiers, wallets, fraud tools or A2A payments."},
        "snb": {"dir": "Visa debit, prepaid, the Signature, Infinite and PriceSmart cards and the Barbados and Ghana books; LINX for domestic debit; Amex acceptance; Endcash, ACH and the coming instant rail.",
                "deals": "Where they meet: the credit book, the AAdvantage co-brand and Republic's terminals."},
    },
    "tl": [
        ["Nov 2018", "Scotiabank Caribbean deal agreed"],
        ["Mar 2021", "Endcash QR wallet launched"],
        ["Sep 2023", "US$ card limit halved"],
        ["Feb 2024", "Priceless Carnival with Mastercard"],
        ["Apr 2024", "Mastercard Black in the BVI"],
        ["May 2025", "PCI DSS on Visa's registry"],
        ["FY2025", "Visa and Mastercard incentives booked"],
        ["Aug 2025", "Cayman National stake to 86.91%"],
        ["Jul 2026", "Digital onboarding across most banks"],
        ["Sep 2026", "US$750m sustainable finance goal"],
    ],
    "l": {
        "U": {"d": 1, "s": "Mastercard credit holders, AAdvantage members and BVI Black holders.",
              "gap": "Every debit holder carries Visa/LINX; credit holders split between the networks.",
              "neo": "Mastercard credit and AAdvantage holders.", "snb": "Debit holders, Visa credit and prepaid holders, Barbados and Ghana cardholders."},
        "L5": {"d": 1, "s": "The front doors are Republic's; ATMs take Mastercard.", "gap": "Online, app and branches are Republic's own.",
               "neo": "ATM acceptance.", "snb": "RepublicOnline, SMS banking, branches, partners."},
        "L4": {"d": 1, "s": "Mastercard Black in the BVI and one corporate card.", "gap": "Accounts carry Visa/LINX debit; Barbados and Ghana are Visa.",
               "neo": "BVI Mastercard Black, AAdvantage Corporate.", "snb": "Accounts, loans, Visa Business, regional Visa books, funds."},
        "L3": {"d": 1, "s": "Priceless is Mastercard's; security and onboarding are Republic's.", "gap": "No public Mastercard fraud, identity or data tools.",
               "neo": "Priceless Carnival.", "snb": "Card security, alerts, onboarding, cash back."},
        "L2": {"d": 1, "s": "Credit split; debit and prepaid on Visa.", "gap": "Mastercard has about five credit programmes and acceptance; Visa has debit, prepaid and the top tiers.",
               "neo": "Mastercard credit, AAdvantage, acceptance.", "snb": "Visa/LINX debit, Visa credit and prepaid, Amex, Endcash, ACH."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, footprint, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
