"""First Abu Dhabi Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from fab_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The UAE's largest bank as five discs that stack into one platform, from AED 1.41 trillion of assets at the bottom "
       "to FAB Mobile, Payit and 140-plus branches at the top. Click the stack to open it. Choose who you are and what "
       "you want to do, and the areas that deliver it light up across the layers, joined in the order they act. Switch "
       "to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("aff", "Elite, Royale & private clients", "gem"),
    ("work", "Workers & remitters", "send"),
    ("sme", "Small businesses", "briefcase"),
    ("corp", "Corporates & institutions", "factory"),
]
USERS_DESC = ("Five kinds of customer, more than 4 million in all across 20-plus markets: everyday UAE customers, Elite, "
              "Royale and private clients, the workers and remitters Payit serves, small businesses, and the corporates "
              "and institutions of wholesale and investment banking.")

WHO = {"con": "A FAB customer", "aff": "A Royale client", "work": "A Payit user", "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account opened in minutes, a Mastercard debit card, the app, Aani transfers and fraud checks.",
     "steps": [("4.1", "accounts", "Open an account with an Emirates ID"), ("2.1", "debit", "Pay with Platinum Mastercard debit"),
               ("5.1", "app", "Run it in FAB Mobile"), ("2.2", "aani", "Send money instantly on Aani"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "credit", "who": "con", "name": "Spend and earn on a card",
     "why": "Own-brand Mastercard credit, the ADNOC co-brand, the Rewards Active ring and FAB Rewards.",
     "steps": [("2.3", "credit", "Pick a FAB Mastercard"), ("2.4", "adnoc", "Fill up with the ADNOC card"),
               ("2.3", "active", "Tap the Rewards Active ring"), ("3.3", "rewards", "Collect FAB Rewards")]},
    {"id": "premium", "who": "aff", "name": "Live the Royale life",
     "why": "Privileged banking, the UAE's first World Legend Exclusive card, McLaren and Etihad miles.",
     "steps": [("4.2", "wealth", "Bank as a Royale client"), ("2.3", "royale", "Carry the World Legend Exclusive"),
               ("3.3", "mclaren", "Add the McLaren Racing pass"), ("2.4", "etihad", "Earn Etihad Guest miles on Visa")]},
    {"id": "national", "who": "con", "name": "Pay on the UAE's own rails",
     "why": "The Jaywan debit card from July 2026 and Aani instant payments.",
     "steps": [("5.1", "app", "Apply in FAB Mobile"), ("2.2", "jaywan", "Pay at home with Jaywan"), ("2.2", "aani", "Transfer by phone number on Aani")]},
    {"id": "remit", "who": "work", "name": "Get paid and send money home",
     "why": "Payit's Universal Account for salaries up to AED 5,000, cross-border transfers and Send Now Pay Later.",
     "steps": [("5.1", "payitapp", "Sign up in the Payit app"), ("2.6", "payitua", "Receive salary in a Universal Account"),
               ("2.6", "payit", "Send money home, now or later")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A business account, World debit, the Mastercard SME suite and acceptance through Network International.",
     "steps": [("4.3", "sme", "Open a business account"), ("2.1", "smedebit", "Pay with World Business Debit"),
               ("2.5", "commcards", "Take an SME commercial card"), ("2.7", "acquiring", "Accept cards via Network International")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Wholesale banking, 65 APIs, commercial cards and tokenised deposits on Swift Ledger.",
     "steps": [("4.4", "wholesale", "Bank with Wholesale Banking"), ("3.2", "apis", "Connect through the API portal"),
               ("2.5", "commcards", "Pay suppliers with In Control"), ("2.8", "digitalmoney", "Settle 24/7 with tokenised deposits")]},
    {"id": "egypt", "who": "sme", "name": "Do business in Egypt",
     "why": "FABMISR's Mastercard cards and its new POS acquiring.",
     "steps": [("4.6", "misr", "Bank with FABMISR"), ("2.7", "misrpos", "Take payments on FABMISR POS")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Debit, own-brand and premium credit, commercial cards, SlicePay, the McLaren pass and the ADNOC co-brand, all under the March 2024 exclusive deal.",
     "steps": [("2.1", "debit", "Platinum Mastercard debit"), ("2.3", "credit", "Own-brand credit on Mastercard"),
               ("2.3", "royale", "World Legend Exclusive"), ("2.5", "commcards", "In Control commercial cards"),
               ("2.3", "slicepay", "SlicePay on Mastercard Installments"), ("3.3", "mclaren", "McLaren Access Pass"), ("2.4", "adnoc", "ADNOC World Mastercard")]},
    {"id": "mcnext", "who": "mc", "name": "Where Payit, Jaywan and agents could land",
     "why": "Where FAB has needs and Mastercard is not yet in: Payit's Visa card and remittances, Jaywan co-badging, agentic payments, fraud scoring as Aani grows, the Visa co-brands at renewal and tokenised settlement.",
     "steps": [("2.6", "payitua", "Payit card and Move for salaries and remittances"), ("2.2", "jaywan", "Co-badge Jaywan with Mastercard"),
               ("3.2", "agents", "Agent Pay for FAB's agentic AI"), ("3.1", "fraud", "Scam and fraud scoring"),
               ("2.4", "etihad", "The Etihad Guest renewal by 2027"), ("2.8", "digitalmoney", "Tokenised settlement next to Swift Ledger")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across First Abu Dhabi Bank's map",
    "title": "Mastercard's exclusive partner, with Visa left in the co-brands",
    "lead": "In March 2024 FAB signed an exclusive long-term global partnership with Mastercard across the UAE, Saudi Arabia, Oman and Egypt and consolidated its portfolios on it. Debit, own-brand and premium credit, commercial cards and a string of firsts now run on Mastercard. Visa keeps the Etihad Guest, SHARE and Blue co-brands and Payit's card, while the UAE builds its own rails in Jaywan and Aani. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (H1 2026 results, 23 July 2026) or from FAB, Mastercard and press releases. Networks are read from FAB's card pages as at October 2026; card counts and network shares are not public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Mastercard", "Platinum debit; World Business debit since 2019"],
        ["Credit", "Mastercard", "Own brands consolidated after March 2024"],
        ["Premium", "World Legend Exclusive", "UAE first, September 2026"],
        ["Co-brands", "Split", "ADNOC, du, GEMS on Mastercard; Etihad, SHARE, Blue on Visa"],
        ["Commercial", "Mastercard", "In Control since 2021; SME suite 2026 ⚠"],
        ["Payit", "Split", "Mastercard remittances 2020; Visa card 2023"],
        ["Domestic rails", "Jaywan and Aani", "Jaywan debit July 2026; Aani 2023"],
        ["Acquiring", "Network International", "Magnati merged in 2025; FAB a co-owner"],
    ],
    "sides": {
        "neo": {"dir": "Debit, own-brand and premium credit, commercial cards, SlicePay instalments, the McLaren Access Pass, ADNOC, du and GEMS co-brands, FABMISR's cards and Payit's 2020 remittance rails.",
                "deals": "Exclusive long-term partnership, March 2024, in four markets; five-year commercial deal, 2021."},
        "snb": {"dir": "Visa on the Etihad Guest, SHARE and Blue FAB co-brands, Payit's card and 2020 virtual cards; Jaywan and Aani for domestic payments; Swift, Citi and J.P. Morgan for tokenised money.",
                "deals": "Where they meet: Payit, Jaywan co-badging and the co-brands as they come up for renewal."},
    },
    "tl": [
        ["May 2019", "World Business Debit Mastercard for SMEs"],
        ["Mar 2020", "payit sends money abroad on Mastercard"],
        ["Feb 2021", "Five-year Mastercard commercial cards deal"],
        ["Feb 2022", "60% of Magnati sold to Brookfield"],
        ["Nov 2023", "SlicePay on Mastercard Installments"],
        ["Mar 2024", "Exclusive long-term Mastercard partnership"],
        ["Aug 2025", "Five Mastercard credit cards in six months"],
        ["Oct 2025", "Magnati merges into Network International"],
        ["Nov 2025", "First issuer on Mastercard Access Pass"],
        ["Dec 2025", "ADNOC Rewards World Mastercard"],
        ["Jul 2026", "Jaywan debit card launched"],
        ["Sep 2026", "World Legend Exclusive; Swift Ledger tokenised deposits"],
    ],
    "l": {
        "U": {"d": 2, "s": "Most FAB cardholders carry Mastercard.",
              "gap": "Debit and own-brand credit are Mastercard; Etihad Guest, SHARE and Blue holders and Payit card users carry Visa ⚠ shares not public.",
              "neo": "Debit holders, own-brand and Royale credit holders, SMEs, FABMISR cardholders.", "snb": "Etihad, SHARE and Blue holders, Payit card users, Jaywan users."},
        "L5": {"d": 1, "s": "Channels carry both networks.", "gap": "FAB Mobile and Apple Pay carry Mastercard and Visa cards; partners are split.",
               "neo": "Cards in FAB Mobile, ADNOC, du and GEMS partners.", "snb": "Etihad, Majid Al Futtaim and Al-Futtaim partners; branches and portals."},
        "L4": {"d": 1, "s": "Accounts come with Mastercard debit.", "gap": "Personal, SME and Egyptian banking issue Mastercard; wholesale and investment banking have no network role.",
               "neo": "Accounts, business banking, FABMISR cards.", "snb": "Wholesale, investment banking, wealth."},
        "L3": {"d": 1, "s": "The McLaren pass and Priceless are Mastercard's.", "gap": "Access Pass and Priceless benefits ride on Mastercard; fraud, AI and APIs are FAB's own or not public.",
               "neo": "McLaren Access Pass, Priceless benefits.", "snb": "Agentic AI, API portal, merchant analytics, fraud ⚠."},
        "L2": {"d": 2, "s": "The card rails are Mastercard; the new rails are not.", "gap": "Debit, credit, premium and commercial cards are Mastercard; Visa keeps three co-brands and Payit's card; Jaywan, Aani and tokenised deposits are separate.",
               "neo": "Debit, credit, World Legend, In Control, SlicePay, ADNOC.", "snb": "Visa co-brands, Payit card, Jaywan, Aani, Swift Ledger."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, ownership, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
