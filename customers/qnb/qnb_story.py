"""QNB Group's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from qnb_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("The Middle East and Africa's largest bank as five discs that stack into one platform, from QR1.46 trillion of "
       "assets and a state-anchored board at the bottom to QNB Mobile, branches and corporate portals at the top. Click "
       "the stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across "
       "the layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("expat", "Expatriate workers", "plane"),
    ("first", "First & Private clients", "gem"),
    ("sme", "Small businesses & merchants", "store"),
    ("corp", "Corporates & government", "building-2"),
    ("intl", "Customers abroad", "globe"),
]
USERS_DESC = ("Six kinds of customer: Qatari households, the expatriate workforce that sends money home, QNB First and "
              "Private clients, small businesses and merchants, corporates and government, and customers of QNB's banks "
              "and branches in more than 28 countries.")

WHO = {"con": "A QNB customer", "expat": "An expatriate worker", "first": "A QNB First client", "sme": "A small business",
       "corp": "A corporate treasurer", "intl": "A customer abroad"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "An account, a debit card, Himyan at home, Fawran for transfers and Apple Pay on the phone.",
     "steps": [("4.1", "retailbank", "Open a salary account"), ("2.4", "mcdebit", "Pay abroad with Mastercard debit"),
               ("2.4", "himyan", "Pay at home on Himyan"), ("2.7", "fawran", "Send money with Fawran"), ("5.1", "wallets", "Tap with Apple Pay")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card and earn points",
     "why": "Life Rewards and co-branded cards, mostly on Visa.",
     "steps": [("2.1", "liferewards", "Take a Life Rewards Visa"), ("2.2", "qrairways", "Earn Avios with Qatar Airways"),
               ("3.3", "rewards", "Redeem Life Rewards points")]},
    {"id": "expat", "who": "expat", "name": "Get paid and send money home",
     "why": "Payroll through WPS, a Himyan or debit card, and transfers to home countries.",
     "steps": [("4.3", "wps", "Get paid through WPS"), ("2.4", "himyan", "Use a Himyan prepaid card"),
               ("2.8", "remit", "Send money home"), ("5.2", "branches", "Deposit cash at an ATM")]},
    {"id": "first", "who": "first", "name": "Bank as a First or Private client",
     "why": "Visa Infinite for First, World Elite Mastercard for Private, Harrods and lifestyle privileges.",
     "steps": [("4.2", "first", "Join QNB First"), ("2.2", "harrods", "Shop with the Harrods Visa"),
               ("2.3", "worldelite", "Carry the World Elite Mastercard"), ("4.2", "wealth", "Invest with QNB Private")]},
    {"id": "merchant", "who": "sme", "name": "Take payments as a small business",
     "why": "myPOS tap on phone, the e-commerce gateway and QNB Simplify.",
     "steps": [("4.4", "smebank", "Open an SME account"), ("2.6", "mypos", "Take cards on a phone"),
               ("2.6", "simplify", "Sell online with QNB Simplify"), ("2.6", "gateway", "Accept online card payments")]},
    {"id": "corp", "who": "corp", "name": "Control company spending",
     "why": "Mastercard corporate and virtual cards with Smart Data reconciliation.",
     "steps": [("4.3", "cib", "Bank with CIB"), ("2.5", "corpcards", "Issue Mastercard corporate cards"),
               ("2.5", "virtualcards", "Pay suppliers with virtual cards"), ("3.4", "smartdata", "Reconcile in Smart Data"), ("5.3", "portals", "Run it in E-Business")]},
    {"id": "abroad", "who": "intl", "name": "Bank with QNB outside Qatar",
     "why": "QNB Türkiye, Enpara, QNB Egypt and the Saudi branches.",
     "steps": [("1.3", "network", "Find QNB in 28+ countries"), ("1.3", "saudi", "Bank in Saudi Arabia"),
               ("4.5", "turkiye", "Bank with QNB Türkiye"), ("4.5", "egypt", "Bank with QNB Egypt")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Corporate and SME cards, Smart Data, Private World Elite, debit, myPOS and Simplify.",
     "steps": [("2.5", "corpcards", "Corporate cards on Mastercard World"), ("3.4", "smartdata", "Smart Data"),
               ("2.3", "worldelite", "Private World Elite"), ("2.4", "mcdebit", "Mastercard debit"),
               ("2.6", "mypos", "myPOS tap on phone"), ("2.6", "simplify", "Simplify Commerce ⚠")]},
    {"id": "mcnext", "who": "mc", "name": "Where Fawran, debit and the footprint could land",
     "why": "Where QNB has needs and Mastercard is not yet in: scam scoring for Fawran, tokenised debit, remittance corridors, payroll cards, card-linked offers and commercial cards across the group.",
     "steps": [("2.7", "fawran", "Fraud and request-to-pay for Fawran"), ("3.1", "security", "Real-time scam scoring"),
               ("2.8", "remit", "Mastercard Move for corridors"), ("4.3", "wps", "Payroll cards for workers"),
               ("3.3", "rewards", "Card-linked offers"), ("1.3", "saudi", "Commercial cards in Saudi Arabia")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across QNB Group's map",
    "title": "Mastercard runs QNB's business cards; Visa has its consumers",
    "lead": "Mastercard signed a long-term deal for QNB's corporate and SME cards in 2023, with Smart Data and virtual cards, launched myPOS tap on phone with it, and issues its Private World Elite cards and, by 2025, its debit cards. Visa holds consumer credit and the Qatar Airways, Harrods and Ooredoo co-brands, and named QNB's the fastest-growing credit portfolio in Qatar. At home, QCB's NAPS switch carries Himyan and Fawran has a quarter of all payments. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (nine-month 2026 results, 8 October 2026) or from QNB, Mastercard, Visa and Qatari press. QNB's site and Mastercard's newsroom were blocked; card networks are read from QNB's 2025 pages, and the networks of QNB Türkiye and QNB Egypt are not confirmed.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Consumer credit", "Visa", "Fastest-growing in Qatar, 2024"],
        ["Co-brands", "Visa", "Qatar Airways 2024; Harrods 2025"],
        ["Corporate & SME", "Mastercard", "Long-term deal, April 2023"],
        ["Private", "World Elite Mastercard", "Invite-only, 2021"],
        ["Debit", "Mastercard ⚠", "Joint campaign, 2025"],
        ["Himyan", "NAPS", "National card, 2023"],
        ["Instant", "Fawran", "3.6m accounts, Dec 2025"],
        ["Acceptance", "myPOS with Mastercard", "March 2023"],
    ],
    "sides": {
        "neo": {"dir": "Corporate and SME cards, virtual cards and Smart Data, Private World Elite, debit, myPOS, Simplify and Airport Pass.",
                "deals": "What it does not do: consumer credit, the big co-brands, Himyan, Fawran or loyalty."},
        "snb": {"dir": "Visa consumer credit and co-brands, QCB's NAPS, Himyan, Fawran and QMP, and QNB's own loyalty and security.",
                "deals": "Where they meet: acquiring, which takes every network, and wallets."},
    },
    "tl": [
        ["May 2017", "First branch in Saudi Arabia"],
        ["Jun 2020", "First international Mastercard transaction in Sudan"],
        ["Jan 2021", "World Elite Exclusive for QNB Private"],
        ["Mar 2023", "Himyan launched; myPOS with Mastercard"],
        ["Apr 2023", "Mastercard commercial-card agreement"],
        ["Feb 2024", "Qatar Airways Visa co-brand"],
        ["Mar 2024", "Fawran instant payments go live"],
        ["Apr 2024", "Visa award for credit growth"],
        ["Apr 2025", "Harrods Visa; Mastercard debit campaign"],
        ["Aug 2025", "Enpara becomes its own bank"],
        ["Oct 2026", "Nine-month profit QR13.3bn"],
    ],
    "l": {
        "U": {"d": 1, "s": "Businesses and Private clients carry Mastercard; consumers mostly Visa.",
              "gap": "Corporate, SME and Private clients and debit holders carry Mastercard; credit cardholders and co-brand members carry Visa; Himyan users ride NAPS.",
              "neo": "Corporates, SMEs, Private clients, debit holders.", "snb": "Credit cardholders, co-brand members, Himyan users."},
        "L5": {"d": 1, "s": "Wallets tokenise both networks.", "gap": "The app, branches and portals are QNB's; Apple Pay and Google Pay carry Visa and Mastercard tokens.",
               "neo": "Tokens on Mastercard cards.", "snb": "App, branches, portals, Visa co-brand partners."},
        "L4": {"d": 1, "s": "Business lines lean on Mastercard; consumers on Visa.", "gap": "Corporate and SME cards are Mastercard; First and retail credit are Visa; Türkiye and Egypt are unconfirmed.",
               "neo": "Corporate, SME and Private cards.", "snb": "Retail credit, QNB First, payroll."},
        "L3": {"d": 1, "s": "Smart Data and Airport Pass are Mastercard's.", "gap": "Corporate reporting and lounges run on Mastercard; security, loyalty and open banking are QNB's own.",
               "neo": "Smart Data, Airport Pass.", "snb": "Security, Life Rewards, open-banking APIs."},
        "L2": {"d": 1, "s": "Mastercard for business cards; Visa, NAPS and Fawran for the rest.", "gap": "Mastercard has corporate cards, Private World Elite, debit, myPOS and Simplify; Visa has consumer credit and co-brands; NAPS has Himyan; Fawran is QCB's.",
               "neo": "Corporate and virtual cards, World Elite, debit, myPOS, Simplify, Sudan.", "snb": "Visa credit and co-brands, Himyan, Fawran, QMP."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, ownership, network, strategy."},
    },
    "t": area_lens(LAYERS),
}
