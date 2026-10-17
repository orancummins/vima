"""Bank Muscat's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bankmuscat_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Oman's largest bank as five discs that stack into one platform, from about a third of the country's banking assets "
       "at the bottom to the app, 200 branches and co-brand partners at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("prem", "Premier & private clients", "gem"),
    ("expat", "Expatriate workers", "plane"),
    ("isl", "Islamic banking customers", "landmark"),
    ("sme", "Small businesses & merchants", "store"),
    ("corp", "Corporates & government", "factory"),
]
USERS_DESC = ("Six kinds of customer, about 4 million in all: everyday Omani customers, premier and private clients, "
              "expatriate workers, Meethaq's Islamic banking customers, small businesses and merchants, and the "
              "corporates and government bodies whose deposits make up about 30% of the book.")

WHO = {"con": "A Bank Muscat customer", "prem": "A premier client", "expat": "An expatriate worker", "isl": "A Meethaq customer",
       "sme": "A merchant", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "An account, a Visa debit card, the free Maal card for local spending, the app and card controls.",
     "steps": [("4.1", "personal", "Open an account"), ("2.1", "debit", "Pay with Visa debit"), ("2.2", "maal", "Use Maal at home"),
               ("5.1", "app", "Run it in the app"), ("3.1", "security", "Lock or unlock the card")]},
    {"id": "credit", "who": "con", "name": "Get a credit card in minutes",
     "why": "Apply in the app, get a digital card at once, pay by phone, earn points and spread big purchases.",
     "steps": [("2.4", "instantcard", "Get an instant digital card"), ("2.3", "visacredit", "Choose a Visa credit card"),
               ("2.4", "wallets", "Add it to Apple Pay"), ("3.2", "rewards", "Earn Bank Muscat Rewards"), ("3.2", "epp", "Pay in 0% instalments")]},
    {"id": "cobrand", "who": "con", "name": "Earn where I shop",
     "why": "The LuLu Mastercard and the Shukran Visa prepaid card.",
     "steps": [("5.3", "partners", "Join through a retailer"), ("2.3", "lulu", "Earn 2% at LuLu"), ("2.1", "prepaid", "Earn Shukran points")]},
    {"id": "expat", "who": "expat", "name": "Get paid and send money home",
     "why": "Hisaby centres for wages and basic banking, and transfers abroad.",
     "steps": [("5.2", "hisaby", "Open an account at Hisaby"), ("2.1", "debit", "Take a Visa debit card"),
               ("2.6", "remit", "Send money home"), ("2.6", "mpcss", "Pay friends instantly")]},
    {"id": "premier", "who": "prem", "name": "Bank as a premier client",
     "why": "Al Jawhar, Asalah and Private Banking with Visa Signature and Infinite cards and Oman Air miles.",
     "steps": [("4.2", "premier", "Join Asalah or Private Banking"), ("2.3", "visacredit", "Carry a Visa Signature or Infinite"),
               ("2.3", "omanair", "Earn Oman Air miles")]},
    {"id": "islamic", "who": "isl", "name": "Bank the Islamic way",
     "why": "Meethaq's 32 branches and its Visa cards.",
     "steps": [("5.2", "branches", "Visit a Meethaq branch"), ("4.5", "meethaq", "Open a Sharia-compliant account"),
               ("4.5", "meethaqcards", "Use a Meethaq Visa card")]},
    {"id": "merchant", "who": "sme", "name": "Take payments as a merchant",
     "why": "Oman's largest acquirer, a phone that takes cards, and QR over the instant rails.",
     "steps": [("4.3", "sme", "Open a business account"), ("2.5", "acquiring", "Take cards and online payments"),
               ("2.5", "tapngo", "Accept on a phone with Tap'N'Go"), ("2.6", "mpcss", "Take QR payments")]},
    {"id": "corp", "who": "corp", "name": "Run a company's money",
     "why": "Corporate banking, Visa virtual cards for suppliers, treasury and the Saudi branch.",
     "steps": [("4.3", "corporate", "Bank with Corporate Banking"), ("2.7", "corpcard", "Pay suppliers by virtual card"),
               ("4.4", "wholesale", "Hedge with Treasury"), ("4.6", "intl", "Trade through the Saudi branch")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The LuLu co-brand, its tokens in phone wallets, and acceptance across Oman's largest acquiring book.",
     "steps": [("2.3", "lulu", "LuLu Titanium Mastercard"), ("2.4", "wallets", "LuLu card in Apple Pay"),
               ("2.5", "acquiring", "Mastercard accepted at 46% of volume"), ("2.5", "tapngo", "Mastercard taps on Tap'N'Go")]},
    {"id": "mcnext", "who": "mc", "name": "Where acquiring, transfers and fraud tools could land",
     "why": "Where Bank Muscat has needs and Mastercard is not yet in: risk and tokenised checkout for the biggest acquirer, remittances for expatriates, scam scoring as instant payments grow, tokens for instant cards, offers for rewards, and premium credit if the Visa deal is re-tendered.",
     "steps": [("2.5", "acquiring", "Acquirer risk and Click to Pay"), ("2.6", "remit", "Mastercard Move for remittances"),
               ("3.1", "security", "Scam and identity scoring"), ("2.4", "instantcard", "Tokens for instant cards"),
               ("3.2", "rewards", "Card-linked offers"), ("2.3", "visacredit", "Premium credit at the next Visa renewal")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Bank Muscat's map",
    "title": "A Visa bank whose merchants Mastercard needs",
    "lead": "Visa carries Bank Muscat's debit, prepaid, credit, Islamic and corporate cards, under a partnership renewed in November 2021. Mastercard has one card, the LuLu Titanium co-brand from 2015. Mastercard's bigger stake is acceptance: the bank handles more than 46% of Oman's acquiring volume. Meanwhile the central bank's Maal card and MPCSS instant payments are taking domestic volume. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (audited 2025 statements; investor presentation, March 2026; H1 2026 results) or from Visa, Mastercard and Omani press. Card counts by network are not published; the Visa contract term is unknown.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Debit", "Visa", "Every tier, youth and Islamic"],
        ["Credit", "Visa, one Mastercard", "LuLu Titanium co-brand since 2015"],
        ["Corporate", "Visa", "Visa Commercial Pay virtual cards"],
        ["Domestic", "Maal", "Central bank card on OmanNet, 2025"],
        ["Acquiring", "All networks", "More than 46% of Oman's volume"],
        ["Instant", "MPCSS", "RO 8.2bn in H1 2026, up 72%"],
        ["Visa deal", "Renewed", "November 2021; term not disclosed ⚠"],
    ],
    "sides": {
        "neo": {"dir": "The LuLu co-brand and its wallet tokens, and acceptance across Bank Muscat's merchants and soft POS.",
                "deals": "What it does not do: debit, prepaid, premium and corporate cards, Meethaq, remittances or fraud tools."},
        "snb": {"dir": "Visa for almost every card; the central bank's Maal, OmanNet and MPCSS for domestic payments; the bank's own rewards and controls.",
                "deals": "Where they meet: the acquiring book, which takes every network."},
    },
    "tl": [
        ["Mar 2015", "LuLu Titanium Mastercard launched"],
        ["Nov 2021", "Visa partnership renewed"],
        ["Nov 2023", "Shukran Visa prepaid with Landmark"],
        ["Jan 2024", "Mastercard names LuLu card Oman's largest co-brand"],
        ["Sep 2025", "Central bank announces Maal"],
        ["Mar 2026", "46% of acquiring volume"],
        ["Jul 2026", "Free local transfers; QR fee cap cut"],
        ["Sep 2026", "Instant credit cards in the app"],
    ],
    "l": {
        "U": {"d": 1, "s": "LuLu cardholders carry Mastercard; everyone else carries Visa.",
              "gap": "About 4 million customers hold Visa debit; the LuLu co-brand is the one Mastercard card.",
              "neo": "LuLu cardholders; merchants accepting Mastercard.", "snb": "Debit, premium, Islamic and corporate cardholders."},
        "L5": {"d": 1, "s": "The front doors are the bank's; one partner brings Mastercard.", "gap": "App and branches are the bank's; LuLu is the Mastercard co-brand partner.",
               "neo": "LuLu co-brand.", "snb": "App, branches, Hisaby, Oman Air and Landmark."},
        "L4": {"d": 0, "s": "The business lines carry Visa cards.", "gap": "Personal, premier, Meethaq and corporate cards are Visa; loans and treasury have no network role.",
               "neo": "None.", "snb": "Personal, premier, corporate, wholesale, Meethaq, international."},
        "L3": {"d": 0, "s": "Services are the bank's own.", "gap": "Rewards, instalments and controls are built in-house; no fraud or open-banking vendor is named.",
               "neo": "Instalments on the LuLu card only.", "snb": "Rewards, controls, AI."},
        "L2": {"d": 1, "s": "One co-brand and acceptance on Mastercard; the rest Visa or domestic.", "gap": "Visa has debit, credit and corporate; Maal and MPCSS take domestic volume; Mastercard has LuLu and acquiring.",
               "neo": "LuLu card, wallet tokens, acceptance.", "snb": "Visa cards, Maal, MPCSS, remittances."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, ownership, licences, strategy."},
    },
    "t": area_lens(LAYERS),
}
