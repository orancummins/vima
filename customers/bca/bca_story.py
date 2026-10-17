"""Bank Central Asia's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bca_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Indonesia's most valuable bank as five discs that stack into one platform, from Rp1,661 trillion of assets and "
       "85% CASA funding at the bottom to myBCA, blu and 1,272 branches at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Young digital customers", "smartphone"),
    ("trav", "Travellers & online shoppers", "plane"),
    ("aff", "Prioritas & Solitaire clients", "gem"),
    ("mer", "Merchants", "store"),
    ("sme", "SMEs & commercial clients", "briefcase"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Seven kinds of customer, about 33–34 million in all: everyday account holders, the young customers of myBCA "
              "and blu, travellers and online shoppers, Prioritas and Solitaire clients, the merchants on EDC BCA and "
              "QRIS, SMEs and commercial clients, and the corporates that drive loan growth.")

WHO = {"con": "A BCA customer", "young": "A young customer", "trav": "A traveller", "aff": "A Prioritas client",
       "mer": "A merchant", "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a Tahapan account with a GPN Paspor card, myBCA, QRIS and Flazz, watched by BCA's fraud models.",
     "steps": [("2.1", "paspor", "Open Tahapan with a Paspor GPN card"), ("5.1", "mybca", "Run it in myBCA"),
               ("2.4", "qris", "Pay by QRIS or QRIS Tap"), ("2.4", "flazz", "Ride the MRT with Flazz"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "cards", "who": "con", "name": "Shop and borrow on a card",
     "why": "Credit on five networks plus BCA Card, the new Blibli Tiket co-brand, rewards and instalments.",
     "steps": [("2.2", "mccc", "Take a BCA credit card"), ("2.3", "bbt", "Shop on Blibli and tiket.com"),
               ("3.3", "rewards", "Earn Reward BCA and points"), ("3.3", "cicilan", "Spread it with Cicilan BCA")]},
    {"id": "travel", "who": "trav", "name": "Spend abroad",
     "why": "Mastercard debit and credit, foreign-currency pockets and QR links in six countries.",
     "steps": [("2.6", "fx", "Hold currency in an FX pocket"), ("2.1", "paspormc", "Pay with the Paspor Mastercard"),
               ("2.6", "xbqr", "Scan a QR code in Japan or Thailand"), ("2.3", "krisflyer", "Earn KrisFlyer miles")]},
    {"id": "young", "who": "young", "name": "Bank the digital way",
     "why": "blu for the young, with Mastercard debit and virtual cards, and domestic credit by QR in myBCA.",
     "steps": [("5.2", "blu", "Open a blu account"), ("3.1", "kyc", "Verify by face"), ("5.2", "bludebit", "Pay online with bluVirtual"),
               ("2.5", "paylater", "Pay later by QRIS")]},
    {"id": "merchant", "who": "mer", "name": "Take payments",
     "why": "EDC BCA terminals and QRIS, watched in the Merchant BCA app, with APIs for larger sellers.",
     "steps": [("2.7", "edc", "Accept cards on EDC BCA"), ("2.7", "qrism", "Display a QRIS code"), ("3.2", "api", "Connect by API BCA")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "SME loans, KlikBCA Bisnis and a GPN business debit card.",
     "steps": [("4.2", "smelend", "Borrow for working capital"), ("2.8", "cashmgmt", "Pay suppliers in KlikBCA Bisnis"),
               ("2.8", "bdc", "Give staff a Business Debit Card"), ("2.4", "bifast", "Send money by BI-FAST")]},
    {"id": "corp", "who": "corp", "name": "Run a corporate treasury",
     "why": "Investment loans, cash management, virtual accounts and host-to-host links across a supply chain.",
     "steps": [("4.1", "corplend", "Borrow for investment"), ("2.8", "cashmgmt", "Collect through virtual accounts"), ("3.2", "api", "Link the ERP by API")]},
    {"id": "wealth", "who": "aff", "name": "Grow and protect wealth",
     "why": "Prioritas and Solitaire, mutual funds and bonds, insurance, and a Mastercard World card free for Solitaire clients.",
     "steps": [("4.4", "wealth", "Invest through Prioritas"), ("4.4", "insure", "Insure in myBCA"), ("2.2", "mccc", "Carry a Mastercard World card")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Paspor debit abroad and online, four Mastercard credit cards including the Blibli Tiket co-brand, every blu card, and acceptance on EDC BCA.",
     "steps": [("2.1", "paspormc", "Paspor BCA Mastercard"), ("2.2", "mccc", "Mastercard Black, World and Globe"),
               ("2.3", "bbt", "Blibli Tiket Mastercard"), ("5.2", "bludebit", "blu debit and virtual cards"), ("2.7", "edc", "Acceptance on EDC BCA")]},
    {"id": "mcnext", "who": "mc", "name": "Where travel, tokens and commercial cards could land",
     "why": "Where BCA has needs and Mastercard is not yet in: travel spending now going to bilateral QR, tokenised cards in myBCA, commercial cards for the corporate book, fraud scoring, card-linked offers and agentic payments.",
     "steps": [("2.6", "xbqr", "Mastercard travel against bilateral QR"), ("5.1", "mybca", "Tokenised Mastercard credentials in myBCA"),
               ("4.1", "corplend", "Commercial and virtual cards"), ("3.1", "fraud", "Fraud and identity scoring"),
               ("3.3", "rewards", "Card-linked offers"), ("1.4", "ai", "Agent Pay for BCA's AI")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Bank Central Asia's map",
    "title": "Domestic rails at home, Mastercard for abroad and online",
    "lead": "BCA's everyday payments run on Indonesia's own rails: GPN debit, its own BCA Card and Debit BCA, QRIS, BI-FAST, Flazz and now the KKI. Mastercard is where customers leave those rails: the Paspor debit card abroad and online since 2017, four Mastercard credit cards including the Blibli Tiket co-brand launched in September 2026, and every blu card. Visa holds the Singapore Airlines and premium lines. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are BCA's own (1H26 results, 28 July 2026) or from BCA's product pages, Bank Indonesia and press. BCA does not publish card numbers by network; the 4.9 million cards figure is from June 2025.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "GPN or Mastercard", "Paspor BCA; Mastercard variant since 2017"],
        ["Credit", "Five networks plus BCA Card", "About 4.9m cards (June 2025) ⚠"],
        ["Mastercard credit", "Black, World, Globe, Blibli Tiket", "Blibli Tiket co-brand, Sep 2026"],
        ["Visa credit", "KrisFlyer, Black, Batman", "FIFA and BTS campaigns, 2026"],
        ["QR & instant", "QRIS, QRIS Tap, BI-FAST", "65.8m QRIS users nationally"],
        ["Domestic credit", "KKI, Paylater", "KKI for individuals, Aug 2026"],
        ["Digital bank", "blu", "Debit and virtual cards on Mastercard"],
        ["Acceptance", "EDC BCA, QRIS", "All networks"],
    ],
    "sides": {
        "neo": {"dir": "Paspor debit abroad and online, Mastercard Black, World, Globe and Blibli Tiket credit cards, every blu card, and acceptance at BCA's merchants.",
                "deals": "What it does not do: domestic debit, QRIS, BI-FAST, Flazz, the KKI, business cards, fraud models or AI."},
        "snb": {"dir": "GPN debit and business cards, BCA Card and Debit BCA, QRIS and QRIS Tap, BI-FAST, Flazz, the KKI and Paylater; Visa, JCB, UnionPay and Amex credit cards; BCA's own fraud models and AI.",
                "deals": "Where they meet: co-brand cards, travel spending and acceptance on EDC BCA."},
    },
    "tl": [
        ["Nov 2017", "Paspor BCA Mastercard debit launched"],
        ["Oct 2021", "BCA tiket.com Mastercard"],
        ["Apr 2025", "US names QRIS and GPN as trade barriers"],
        ["Jun 2025", "Hendra Lembong becomes President Director"],
        ["Aug 2025", "Cross-border QRIS in Japan"],
        ["Feb 2026", "US–Indonesia trade deal finalised"],
        ["Mar 2026", "Visa FIFA top-spender campaign"],
        ["Aug 2026", "KKI for individuals; Affin Bank deal"],
        ["Sep 2026", "BCA Blibli Tiket Mastercard"],
    ],
    "l": {
        "U": {"d": 1, "s": "Travellers, online shoppers and blu users carry Mastercard.",
              "gap": "Most account holders carry GPN debit and pay by QRIS; Mastercard reaches those who choose it for travel, online spending or blu.",
              "neo": "Paspor Mastercard holders, Mastercard credit cardholders, blu users.", "snb": "GPN debit holders, QRIS users, Visa and other cardholders, merchants on QRIS."},
        "L5": {"d": 1, "s": "blu's cards are Mastercard; the rest is BCA's.", "gap": "myBCA, branches and Halo BCA are BCA's own; blu issues only Mastercard cards.",
               "neo": "bluDebit and bluVirtual.", "snb": "myBCA, BCA mobile, branches, Halo BCA, partners."},
        "L4": {"d": 0, "s": "The business lines have no network role.", "gap": "Loans, wealth, insurance and sharia banking sit off the card rails.",
               "neo": "None.", "snb": "Corporate, SME, mortgages, BCA Finance, wealth, BCA Syariah."},
        "L3": {"d": 1, "s": "Rewards and instalments ride on every card; fraud and AI are BCA's.", "gap": "BCA builds fraud detection and AI in-house; no Mastercard service is public.",
               "neo": "Rewards and instalments on Mastercard cards.", "snb": "Fraud models, biometric KYC, API BCA."},
        "L2": {"d": 1, "s": "Mastercard for abroad and online; domestic rails at home.", "gap": "GPN, QRIS, BI-FAST, Flazz and the KKI carry everyday payments; Mastercard has a debit variant, four credit cards and a co-brand.",
               "neo": "Paspor Mastercard, Mastercard credit, Blibli Tiket, acceptance.", "snb": "GPN, BCA Card, QRIS, BI-FAST, Flazz, KKI, Visa, JCB, UnionPay, Amex."},
        "L1": {"d": 0, "s": "BCA's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, owners, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
