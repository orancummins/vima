"""Kapital Bank's (Birbank's) kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from kapitalbankaz_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Azerbaijan's second-largest bank, now selling everything as Birbank, as five discs that stack into one platform, "
       "from AZN 13.9 billion of assets at the bottom to the Birbank app, branches and partners at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("edu", "Students & teachers", "graduation-cap"),
    ("prem", "Private clients", "gem"),
    ("eco", "Ecosystem shoppers", "store"),
    ("micro", "Micro & small businesses", "briefcase"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer: more than 5 million individuals, students and teachers on public-sector cards, "
              "private clients, shoppers on Birmarket, m10 and Trendyol, about 123,000 micro and small businesses, and "
              "22,000-plus legal entities.")

WHO = {"con": "A Birbank customer", "edu": "A student or teacher", "prem": "A private client", "eco": "A shopper",
       "micro": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: a free Birbank debit card ordered in the app, QR and card payments, alerts and Bir Bonus.",
     "steps": [("3.2", "onboarding", "Sign up with Bir ID"), ("2.2", "debit", "Get a Birbank Debit card"), ("5.1", "app", "Run it in the Birbank app"),
               ("2.6", "qr", "Pay by QR"), ("3.3", "notify", "See every payment"), ("3.1", "birbonus", "Earn Bir Bonus")]},
    {"id": "credit", "who": "con", "name": "Buy now, pay in instalments",
     "why": "The Taksit card that holds 60% of the country's instalment cards, Star, Ninja and Trendyol.",
     "steps": [("2.1", "taksit", "Take a Taksit card"), ("4.1", "bnpl", "Split a purchase at a partner"), ("2.1", "star", "Or use a Star credit line"),
               ("3.1", "vat", "Collect the VAT refund")]},
    {"id": "travel", "who": "con", "name": "Travel on miles",
     "why": "Birbank Miles, with Mastercard lounges on the Taksit version.",
     "steps": [("2.2", "miles", "Earn miles on Birbank Miles"), ("2.7", "wallets", "Pay with Apple Pay abroad"), ("2.6", "transfers", "Send money home")]},
    {"id": "edu", "who": "edu", "name": "Study or teach on a public card",
     "why": "TələbəPlus on Visa for students and TəhsilPlus on Mastercard for teachers.",
     "steps": [("2.3", "telebe", "Get TələbəPlus as a student"), ("2.3", "tehsil", "Get TəhsilPlus as a teacher"), ("2.7", "transit", "Ride the metro"),
               ("5.1", "app", "Manage it in Birbank")]},
    {"id": "private", "who": "prem", "name": "Bank privately and invest",
     "why": "Birbank Private's Visa Infinite and World Elite cards, deposits and Birbank Invest.",
     "steps": [("2.3", "private", "Choose a premium card"), ("4.3", "deposits", "Place a deposit"), ("4.3", "invest", "Invest with Birbank Invest")]},
    {"id": "shop", "who": "eco", "name": "Shop across the ecosystem",
     "why": "Birmarket, the m10 wallet, MilliÖn terminals and Bir Bonus.",
     "steps": [("4.5", "birmarket", "Shop on Birmarket"), ("2.7", "m10", "Pay with m10"), ("2.7", "million", "Top up at a MilliÖn terminal"),
               ("3.1", "birbonus", "Spend Bir Bonus")]},
    {"id": "sme", "who": "micro", "name": "Run a small business",
     "why": "Birbank Biznes, Visa business cards, POS and Mobile POS, and micro loans.",
     "steps": [("5.2", "bizapp", "Open a Birbank Biznes account"), ("2.4", "bizcards", "Get a business card"), ("2.5", "mpos", "Take cards on a phone"),
               ("4.4", "sme", "Borrow for the business")]},
    {"id": "corp", "who": "corp", "name": "Run a company's money",
     "why": "Corporate accounts, trade finance, payroll and POS acceptance.",
     "steps": [("4.4", "corp", "Bank with Kapital Bank"), ("2.4", "bizcards", "Pay expenses on company cards"), ("2.5", "pos", "Accept cards in-store")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Miles Taksit and World Elite, TəhsilPlus, acceptance at the bank's terminals and the PashaPay MoU.",
     "steps": [("2.2", "miles", "Miles Taksit on Mastercard World"), ("2.3", "tehsil", "TəhsilPlus with Priceless Specials"),
               ("2.3", "private", "World Elite Miles"), ("2.5", "pos", "Mastercard accepted at POS"), ("3.2", "mcmou", "PashaPay MoU")]},
    {"id": "mcnext", "who": "mc", "name": "Where sends, security and offers could land",
     "why": "Where Kapital Bank has needs and Mastercard is not yet in: outbound transfers, fraud and identity after the 2026 incident, Click to Pay on Birmarket, offers for Bir Bonus, subscription controls and business cards.",
     "steps": [("2.6", "transfers", "Mastercard Move for Birbank sends"), ("3.2", "fraud", "Fraud and identity tools"),
               ("4.5", "birmarket", "Click to Pay at checkout"), ("3.1", "birbonus", "Card-linked offers"),
               ("3.3", "notify", "Subscription and merchant clarity"), ("2.4", "bizcards", "Commercial cards for SMEs")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Kapital Bank's map",
    "title": "A Visa-first bank where Mastercard holds the niches",
    "lead": "Kapital Bank issues on both networks, but the card most customers carry, the Birbank Taksit, and the Star credit card, all business cards and the student card are Visa. Mastercard has Miles Taksit, World Elite for private clients and, since March 2026, TəhsilPlus for about 450,000 education staff. Its subsidiary PashaPay signed an MoU with Mastercard in 2025. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (statutory indicators to 30 September 2026; 2025 IFRS statements) or from Birbank, Trend, PashaPay and Report.az. Networks for several cards are read from card artwork on birbank.az; the bank does not publish issuance by network.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Taksit & Star", "Visa", "Core Birbank cards ⚠ artwork"],
        ["Miles Taksit", "Mastercard World", "LoungeKey, Airport Experiences"],
        ["Private", "Visa Infinite + World Elite", "Two Visa, one Mastercard"],
        ["Teachers", "TəhsilPlus, Mastercard", "About 450,000 staff, Mar 2026"],
        ["Students", "TələbəPlus, Visa", "2024"],
        ["Business cards", "Visa", "Biznes, Gold, Digital, Sahibkar"],
        ["PashaPay", "Mastercard MoU", "June 2025; live use ⚠"],
        ["Instant payments", "CBAR IPS", "About 1 million a day"],
    ],
    "sides": {
        "neo": {"dir": "Miles Taksit, World Elite Miles, TəhsilPlus with Priceless Specials, acceptance at the bank's terminals and the PashaPay MoU on sends, identity and fraud.",
                "deals": "What it does not do: the core Taksit and Star cards, business cards, students, transit, QR or loyalty."},
        "snb": {"dir": "Visa on Taksit, Star, Platinum, Visa Infinite, TələbəPlus and business cards and in transit; the bank's own QR, m10, MilliÖn and Bir Bonus; the central bank's instant payments.",
                "deals": "Where they meet: Apple Pay and Google Pay, POS acceptance and the Miles range, split across both."},
    },
    "tl": [
        ["2016", "BirKart instalment card launched"],
        ["Nov 2021", "Apple Pay with Kapital Bank among launch banks"],
        ["Mar 2022", "PashaPay brought into the group"],
        ["2024", "TələbəPlus with Visa; QR brought in-house"],
        ["2025", "Kapital Bank becomes Birbank; Visa transit with BakıKart"],
        ["Jun 2025", "PashaPay–Mastercard MoU"],
        ["Nov 2025", "Birbank and Visa Disneyland campaign"],
        ["Mar 2026", "TəhsilPlus with Mastercard"],
        ["Jul 2026", "Visa: 10 local issuers on Click to Pay"],
        ["Oct 2026", "IPS at a million transactions a day"],
    ],
    "l": {
        "U": {"d": 1, "s": "Teachers, Miles Taksit and World Elite holders carry Mastercard.",
              "gap": "Most Taksit, Star, student and business cardholders carry Visa; TəhsilPlus brings up to 450,000 staff onto Mastercard.",
              "neo": "Teachers, Miles Taksit and World Elite holders.", "snb": "Taksit and Star holders, students, businesses, wallet and QR users."},
        "L5": {"d": 0, "s": "The front doors are the bank's.", "gap": "App, Birbank Biznes, branches, ATMs and partners are Kapital Bank's own.", "neo": "None.", "snb": "Birbank apps, branches, MilliÖn, Wolt."},
        "L4": {"d": 0, "s": "The business lines carry no network role.", "gap": "Loans, deposits, Birbank Invest and Birmarket are the bank's; SME cards are Visa.",
               "neo": "None.", "snb": "Lending, BNPL, deposits, Birmarket, Visa SME cards."},
        "L3": {"d": 1, "s": "A Mastercard MoU at PashaPay; the rest is the bank's.", "gap": "Fraud, AI, alerts and Bir Bonus are built in-house; the PashaPay MoU on identity and fraud is unconfirmed in use.",
               "neo": "PashaPay MoU ⚠.", "snb": "Own fraud controls, AI, Bir Bonus, VAT refunds."},
        "L2": {"d": 1, "s": "Visa leads the cards; Mastercard has Miles, World Elite and TəhsilPlus.", "gap": "Visa carries Taksit, Star, Platinum, students and business; Mastercard holds the niches and accepts at POS.",
               "neo": "Miles Taksit, World Elite, TəhsilPlus, POS acceptance, wallets.", "snb": "Visa cards and transit, own QR, m10, MilliÖn, IPS."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, PASHA ownership, brand, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
