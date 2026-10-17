"""OCBC's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from ocbc_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Singapore's oldest bank as five discs that stack into one platform, from a record S$4.19 billion half-year "
       "profit and Aa1 ratings at the bottom to the OCBC app, OCBC WoW and close to 400 branches at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("card", "Cardholders", "credit-card"),
    ("senior", "Seniors", "users-round"),
    ("remit", "Foreign workers & remitters", "plane"),
    ("wealth", "Wealth clients", "gem"),
    ("sme", "SMEs", "briefcase"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Seven kinds of customer across 19 markets: everyday customers, cardholders in Singapore, Malaysia and "
              "Indonesia, seniors, the foreign workers who send money home, wealth clients with S$350 billion of assets, "
              "one in two Singapore SMEs, and the corporates and institutions of Global Wholesale Banking.")

WHO = {"con": "An OCBC customer", "card": "A cardholder", "senior": "A senior", "remit": "A foreign worker",
       "wealth": "A wealth client", "sme": "An SME", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a 360 Account, a Visa debit card that also works on NETS, PayNow in the app and Money Lock.",
     "steps": [("4.1", "accounts", "Open a 360 Account"), ("2.2", "debit", "Pay with the Visa debit card"), ("2.4", "paynow", "Pay by PayNow"),
               ("5.1", "app", "Run it in the OCBC app"), ("3.1", "moneylock", "Lock savings against scams")]},
    {"id": "cashback", "who": "card", "name": "Earn on everyday spending",
     "why": "The 365 card on Visa, or INFINITY, Rewards and NXT on Mastercard, with OCBC$ and the 360 bonus.",
     "steps": [("2.1", "c365", "Take the 365 card"), ("2.1", "infinity", "Or INFINITY cashback"), ("2.1", "nxt", "Split a big purchase with NXT"),
               ("3.4", "ocbcdollars", "Earn OCBC$ and 360 bonus interest")]},
    {"id": "travel", "who": "card", "name": "Travel and pay abroad",
     "why": "90°N miles on Mastercard or Visa, and QR payments from the account in 57 destinations.",
     "steps": [("2.1", "n90", "Earn miles with 90°N"), ("2.4", "scanpay", "Scan & Pay in China"), ("3.4", "ocbcdollars", "Redeem miles in the app")]},
    {"id": "remit", "who": "remit", "name": "Send money home",
     "why": "Fee-free transfers to 10 wallets in China and Southeast Asia, powered by Visa Direct.",
     "steps": [("5.1", "app", "Open the OCBC app"), ("2.5", "paytowallet", "Send to GCash, GoPay or Weixin Pay")]},
    {"id": "senior", "who": "senior", "name": "Bank safely in later life",
     "why": "SeniorCare, PayNow, Money Lock and in-app calls.",
     "steps": [("5.3", "branches", "Get help from a CARE Ambassador"), ("4.1", "accounts", "Join SeniorCare"), ("2.4", "paynow", "Shop online by PayNow"),
               ("3.1", "inappcalls", "Call the bank inside the app")]},
    {"id": "wealth", "who": "wealth", "name": "Grow and protect wealth",
     "why": "Premier, Bank of Singapore and Great Eastern, onboarded by agentic AI and served by avatars.",
     "steps": [("3.2", "helios", "Onboard in 15 days with HELIOS"), ("4.2", "wealth", "Invest with Premier or Bank of Singapore"),
               ("3.3", "wow", "Ask Wendy or Wayne in OCBC WoW"), ("4.3", "greateastern", "Insure with Great Eastern"), ("2.2", "worldelite", "Spend on World Elite debit")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account, QR collection, card acquiring and Singpass onboarding across the Causeway.",
     "steps": [("4.4", "sme", "Bank with OCBC"), ("3.2", "singpass", "Open in Malaysia with Singpass"), ("2.6", "onecollect", "Collect by QR with OneCollect"),
               ("2.6", "acquiring", "Take cards"), ("2.2", "bizdebit", "Pay with a business card")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Transaction banking and tokenised deposits across ASEAN and Greater China.",
     "steps": [("4.5", "gtb", "Bank with Global Wholesale Banking"), ("2.7", "tokdeposits", "Settle 24/7 with tokenised deposits"), ("4.5", "markets", "Hedge with Global Markets")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "INFINITY, Rewards, NXT and 90°N in Singapore, World Elite debit, most of Malaysia's cards and Indonesia's 1st Card.",
     "steps": [("2.1", "infinity", "INFINITY on Mastercard"), ("2.1", "nxt", "NXT instalments on Mastercard"), ("2.1", "n90", "90°N Mastercard"),
               ("2.2", "worldelite", "World Elite debit"), ("2.3", "mycards", "Malaysia's Mastercard range"), ("2.3", "idcards", "OCBC 1st Card in Indonesia")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, transfers and new card books could land",
     "why": "Where OCBC has needs and Mastercard is not yet in: Agent Pay for an AI-native app, scam tools after phishing losses, Move against Visa Direct, the HSBC Indonesia card book and commercial cards.",
     "steps": [("3.3", "wow", "Agent Pay for OCBC WoW"), ("3.1", "inappcalls", "Passkeys and scam scores"), ("2.5", "paytowallet", "Move against Visa Direct"),
               ("2.3", "hsbccards", "The HSBC Indonesia card book in 2027"), ("4.5", "gtb", "Commercial and virtual cards")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across OCBC's map",
    "title": "Visa's flagship and transfers, Mastercard's newer cards and Malaysia",
    "lead": "In Singapore OCBC's most-held card, the 365, and its main debit card are on Visa, as are the Visa Infinite wealth cards, and Visa Direct has powered its cross-border wallet transfers since 2024. Mastercard carries the INFINITY, Rewards and NXT cards, half of 90°N, World Elite debit, six of seven cards in Malaysia and a new youth card in Indonesia. PayNow, NETS and QR carry the rest. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (1H26 results, 7 August 2026; Annual Report 2025). Networks were read from OCBC's card pages and card faces on 17 October 2026; Hong Kong and China card lineups and any network contracts were not found.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["365 Credit (flagship)", "Visa", "Three in five OCBC cardholders"],
        ["INFINITY, Rewards, NXT", "Mastercard", "Singapore, 2026"],
        ["90°N", "Mastercard and Visa", "Mastercard since 2019"],
        ["Debit", "Visa + NETS; World Elite Mastercard", "Mass vs Premier"],
        ["Malaysia", "Mastercard", "Six of seven cards"],
        ["Remittance", "Visa Direct", "10 wallets since 2024"],
        ["Agent Pay", "Not OCBC", "DBS and UOB went first, Mar 2026"],
        ["Tokenised deposits", "Swift, Ant", "Sep–Oct 2026"],
    ],
    "sides": {
        "neo": {"dir": "INFINITY, Rewards, NXT and 90°N Mastercard, World Elite debit, the Malaysian range, Indonesia's 1st Card, and acceptance at OCBC's merchants.",
                "deals": "What it does not do: the 365 and main debit cards, Visa Infinite, cross-border transfers, PayNow, QR or tokenised money."},
        "snb": {"dir": "Visa on the flagship, debit, wealth cards and Visa Direct; NETS, PayNow and six QR networks; OCBC's own scam tools, AI and tokens.",
                "deals": "Where they meet: 90°N, issued on both networks."},
    },
    "tl": [
        ["Aug 2019", "OCBC 90°N Mastercard launched"],
        ["Oct 2019", "JCB acceptance added"],
        ["May 2022", "MAS capital add-on after phishing losses"],
        ["Nov 2024", "Pay-to-wallet on Visa Direct"],
        ["Jan 2026", "Tan Teck Long becomes CEO"],
        ["Feb 2026", "OCBC 1st Card with Mastercard in Indonesia; Weixin Pay QR"],
        ["Mar 2026", "Mastercard Agent Pay live in Singapore with DBS and UOB"],
        ["May 2026", "HSBC Indonesia deal; light-up cards"],
        ["Jul 2026", "OCBC WoW and HELIOS"],
        ["Oct 2026", "365 refresh; Ant tokenised deposits"],
    ],
    "l": {
        "U": {"d": 1, "s": "Mastercard reaches newer-card holders, Premier debit users and Malaysians.",
              "gap": "Most Singapore cardholders and every debit customer carry Visa; Malaysians mostly carry Mastercard.",
              "neo": "INFINITY, Rewards, NXT and 90°N holders, World Elite debit, Malaysia.", "snb": "365 and debit holders, remitters, PayNow users."},
        "L5": {"d": 0, "s": "The front doors are OCBC's.", "gap": "App, WoW, business channels and branches are the bank's.", "neo": "None.", "snb": "OCBC app, WoW, Velocity, branches."},
        "L4": {"d": 0, "s": "The business lines carry Visa and Mastercard cards but no network role.", "gap": "Accounts come with Visa debit; wealth splits Visa Infinite and World Elite; SME and corporate cards not found.",
               "neo": "None.", "snb": "Accounts, wealth, Great Eastern, SME and corporate banking."},
        "L3": {"d": 0, "s": "Scam tools, identity and AI are OCBC's own.", "gap": "Money Lock, in-app calls, HELIOS and WoW use no Mastercard service; rewards draw on Mastercard Travel Rewards on Mastercard cards.",
               "neo": "Mastercard Travel Rewards.", "snb": "Money Lock, in-app calls, Singpass, HELIOS, WoW, Disney."},
        "L2": {"d": 1, "s": "Singapore credit is split; Malaysia leans Mastercard; transfers go to Visa.", "gap": "Visa has the 365, debit and Visa Direct; Mastercard has four Singapore credit cards and Malaysia; PayNow, QR and tokens bypass both.",
               "neo": "INFINITY, Rewards, NXT, 90°N, World Elite, Malaysia.", "snb": "365, debit, Visa Infinite, Visa Direct, PayNow, QR, tokenised deposits."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, ratings, leadership, strategy."},
    },
    "t": area_lens(LAYERS),
}
