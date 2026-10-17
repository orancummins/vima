"""Bread Financial's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from breadfinancial_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("A private-label and co-brand card issuer as five discs that stack into one platform, from $18.5 billion of "
       "loans and two Comenity banks at the bottom to the tills of Victoria's Secret, Ulta, Signet and Ford's dealers at "
       "the top. Click the stack to open it. Choose who you are and what you want to do, and the areas that deliver it "
       "light up across the layers, joined in the order they act. Switch to the Mastercard lens to see how deep "
       "Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Shoppers", "user-round"),
    ("fan", "Travellers & fans", "plane"),
    ("home", "Homeowners & drivers", "house"),
    ("save", "Savers", "coins"),
    ("smb", "Small merchants", "briefcase"),
    ("partner", "Brand partners", "store"),
    ("corp", "Investors & regulators", "landmark"),
]
USERS_DESC = ("Seven kinds of user around about 34 million open accounts: shoppers at about 100 brands, travellers and "
              "fans of Caesars, Hard Rock and the NFL, homeowners and drivers, savers with $9.4 billion on deposit, the "
              "small merchants that offer Bread Pay, the brand partners themselves, and Bread's investors and regulators.")

WHO = {
    "con": "A shopper", "fan": "A traveller", "home": "A homeowner", "save": "A saver", "smb": "A merchant",
    "partner": "A brand partner", "corp": "An investor",
}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "shop", "who": "con", "name": "Get a store card at the till",
     "why": "The core loop: pre-qualify at the brand, get a decision, and earn the brand's rewards.",
     "steps": [("5.1", "pos", "Pre-qualify at the till or online"), ("3.1", "underwriting", "Get a credit decision"),
               ("2.1", "privatelabel", "Use the store card"), ("3.3", "loyalty", "Earn the brand's rewards")]},
    {"id": "beauty", "who": "con", "name": "Earn beauty and fashion rewards everywhere",
     "why": "Bread's biggest Mastercard programmes: Ulta and Victoria's Secret cards that work beyond the store.",
     "steps": [("4.2", "ulta", "Join Ulta Beauty Rewards"), ("2.2", "vsmc", "Or get the Victoria's Secret Mastercard"),
               ("2.2", "mccobrand", "Spend anywhere on Mastercard"), ("2.6", "wallets", "Tap it from a phone wallet")]},
    {"id": "travel", "who": "fan", "name": "Play, stay and travel on a co-brand",
     "why": "Casino, motoring and sports loyalty turned into cards: mostly Visa, with Hard Rock and PENN on Mastercard.",
     "steps": [("4.3", "caesars", "Get a Caesars Rewards Visa"), ("4.3", "casinos", "Or Unity by Hard Rock Mastercard"),
               ("4.3", "aaa", "Use the AAA card on the road"), ("4.3", "sports", "Back your team")]},
    {"id": "home", "who": "home", "name": "Furnish a home or buy a car",
     "why": "Home and auto are Bread's growth verticals in 2026, with cards and instalment loans side by side.",
     "steps": [("4.4", "home", "Furnish with Raymour or Ethan Allen"), ("2.5", "instalments", "Spread it with Bread Pay"),
               ("5.1", "pos", "Apply at a Ford dealer"), ("2.3", "ford", "Earn with the Ford Rewards Visa")]},
    {"id": "save", "who": "save", "name": "Save and earn with Bread",
     "why": "Bread's direct business: the deposits that fund half the book and its own cards.",
     "steps": [("4.6", "savings", "Open a high-yield savings account"), ("2.4", "cashback", "Get the Bread Cashback card"),
               ("2.4", "rewardsamex", "Or Bread Rewards"), ("5.2", "app", "Manage it in the app")]},
    {"id": "smb", "who": "smb", "name": "Offer pay-over-time at checkout",
     "why": "Bread Pay for smaller merchants: instalments and pay in four built into the checkout.",
     "steps": [("5.3", "smbs", "Sign up as a merchant"), ("3.4", "apis", "Add Bread with APIs or SDKs"),
               ("2.5", "splitpay", "Offer pay in four"), ("2.5", "instalments", "Or longer instalment loans")]},
    {"id": "partner", "who": "partner", "name": "Run a card programme as a brand",
     "why": "What a brand gets: a card, a credit decision, a digital suite, loyalty run for it, and a share of the economics.",
     "steps": [("1.4", "partners", "Sign a five-to-ten-year agreement"), ("4.4", "signet", "Renew it, as Signet did"),
               ("3.4", "eds", "Use the Enhanced Digital Suite"), ("3.3", "loyalty", "Run the rewards"),
               ("3.3", "rsa", "Share the economics")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Mastercard carries two of Bread's three largest programmes and a set of fashion, casino and sport cards.",
     "steps": [("2.2", "vsmc", "The Victoria's Secret Mastercard"), ("4.2", "ulta", "The Ulta Beauty Rewards Mastercard"),
               ("2.2", "saksmc", "Saks World Elite"), ("4.3", "casinos", "Hard Rock and PENN"),
               ("4.5", "academy", "myAcademy Rewards"), ("2.6", "wallets", "Tokens in the wallets")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, tokens and fraud tools could land",
     "why": "Where Bread has needs and Mastercard is not yet in: agentic commerce, tokens for private label, fraud at instant credit, instalments, loyalty costs, and the co-brands Visa has been winning.",
     "steps": [("3.5", "agentic", "Agent Pay for the co-brands"), ("2.1", "privatelabel", "Tokens and Click to Pay for store cards"),
               ("3.2", "fraud", "Identity and fraud at instant credit"), ("2.5", "instalments", "Bread Pay on Mastercard Installments"),
               ("3.3", "loyalty", "Merchant-funded offers"), ("2.3", "visacobrand", "Visa programmes at renewal")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Bread Financial's map",
    "title": "Mastercard holds the biggest brands; Visa is winning the new ones",
    "lead": "Bread chooses a network programme by programme. Mastercard carries two of its three largest partners, Victoria's Secret and Ulta Beauty, and Saks, Hard Rock, PENN and Academy. Visa has AAA, Caesars, Toyota and most of the new co-brands of 2025–26, Ford and Crypto.com among them. American Express has Bread's own cards, and private label and Bread Pay use no network. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are Bread's own (2Q26 results, 23 July 2026; FY2025 10-K). Networks come from partner releases and the CFPB agreement database, which lists agreements on file rather than volumes. No enterprise network agreement is public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Largest partners", "VS, Ulta on Mastercard", "Signet, the third, is private label"],
        ["Co-brand", "About 52%", "Of 2025 credit sales; split Mastercard and Visa"],
        ["Programmes on file", "About 18 v 17", "Mastercard v Visa ⚠ by count, not volume"],
        ["Newest co-brands", "Visa", "Ford (2026), Crypto.com (2025)"],
        ["Own cards", "American Express", "Bread Cashback and Bread Rewards"],
        ["Private label", "About 43%", "No network"],
        ["Bread Pay", "Bread's own", "AAA, Dell, Ford, Vivint"],
        ["Agentic", "Use cases", "No network partner named"],
    ],
    "sides": {
        "neo": {"dir": "Victoria's Secret, Ulta, Saks, Hard Rock, PENN, Academy and the fashion and team cards, and the tokens behind them in wallets.",
                "deals": "What it does not do: private label, Bread Pay, Bread's own cards, fraud, loyalty, or the Visa programmes."},
        "snb": {"dir": "Visa on AAA, Caesars, Ford, Toyota, Crypto.com, NFL and Sephora; American Express on Bread's own cards; private label and Bread Pay off-network.",
                "deals": "Where they meet: every renewal and every new co-brand, and the move to agentic commerce."},
    },
    "tl": [
        ["Jul 2016", "Ulta Beauty signs, on Mastercard"],
        ["Jan 2022", "Ulta renewed"],
        ["Mar 2022", "Victoria's Secret Mastercard launched"],
        ["Apr 2022", "Bread Cashback on American Express"],
        ["Jun 2024", "Saks World Elite Mastercard won"],
        ["2025", "Crypto.com Visa; Caesars renewed"],
        ["Mar 2026", "Ford Rewards Visa Signature"],
        ["Jul 2026", "Agentic use cases with partners"],
        ["Sep 2026", "Signet renewed, private label"],
    ],
    "l": {
        "U": {"d": 1, "s": "Beauty, fashion and casino cardholders carry Mastercard.",
              "gap": "Mastercard reaches holders of the Victoria's Secret, Ulta, Saks and Hard Rock cards; store-card holders, Bread Pay borrowers, savers and Visa co-brand holders do not touch it.",
              "neo": "Victoria's Secret, Ulta, Saks, Hard Rock, PENN and Academy cardholders.", "snb": "Store-card holders, AAA, Caesars and Ford holders, Bread Pay borrowers, savers."},
        "L5": {"d": 0, "s": "The front doors are the brands'.", "gap": "Applications happen at partner tills, sites and dealers, and in Bread's app.",
               "neo": "None.", "snb": "Partner stores, dealers, the Bread app, Bread Pay merchants."},
        "L4": {"d": 1, "s": "Mastercard inside the biggest brands, Visa in travel and auto.",
               "gap": "Victoria's Secret, Ulta and the casinos are Mastercard; Caesars, AAA and the auto brands are Visa; Signet and home are private label.",
               "neo": "Victoria's Secret, Ulta, Hard Rock, PENN, Academy, fashion brands.", "snb": "Signet, home, Caesars, AAA, Ford, Toyota, savings."},
        "L3": {"d": 0, "s": "The engine room is Bread's own.", "gap": "Underwriting, fraud, loyalty and the digital suite are Bread's; agentic work names no network.",
               "neo": "None announced.", "snb": "Credit, fraud, loyalty, digital suite, APIs."},
        "L2": {"d": 1, "s": "Co-brands split between Mastercard and Visa; the rest off-network.",
               "gap": "Mastercard and Visa each carry about half the co-brand programmes; Amex has Bread's own cards; private label and Bread Pay use no network.",
               "neo": "Mastercard co-brands, Victoria's Secret, Saks, wallet tokens.", "snb": "Visa co-brands, Ford, Amex cards, private label, Bread Pay."},
        "L1": {"d": 0, "s": "The balance sheet and banks are Bread's.", "gap": "Nothing in the foundation is Mastercard's.",
               "neo": "None.", "snb": "Capital, banks, technology, partner contracts."},
    },
    "t": area_lens(LAYERS),
}
