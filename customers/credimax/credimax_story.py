"""CrediMax's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from credimax_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Bahrain's first card issuer and its main acquirer as five discs that stack into one platform, from BBK's "
       "ownership and a 1991 heritage at the bottom to the CrediMax Digital app and BBK's branches at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Cardholders", "user-round"),
    ("prem", "Premium cardholders", "gem"),
    ("young", "Families & students", "graduation-cap"),
    ("corp", "Businesses", "briefcase"),
    ("merch", "Merchants", "store"),
    ("partner", "Co-brand partners", "users-round"),
]
USERS_DESC = ("Six kinds of user: everyday cardholders, premium cardholders, parents, children and students, businesses "
              "with corporate cards, Bahrain's merchants, and the co-brand partners that put their names on the cards. "
              "CrediMax publishes no customer count.")

WHO = {"con": "A cardholder", "prem": "A premium cardholder", "young": "A parent or student", "corp": "A business",
       "merch": "A merchant", "partner": "A co-brand partner"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Pay and borrow on a card",
     "why": "The everyday loop: instant onboarding, a Mastercard or Visa credit card, Apple Pay, the app and Thameen points.",
     "steps": [("3.2", "onboarding", "Get approved instantly"), ("2.1", "mccredit", "Take a Mastercard"), ("2.8", "applepay", "Add it to Apple Pay"),
               ("5.1", "app", "Manage it in the app"), ("3.3", "thameen", "Earn Thameen points")]},
    {"id": "premium", "who": "prem", "name": "Travel on a premium card",
     "why": "World Elite or Infinite, lounges and airline miles.",
     "steps": [("2.1", "mccredit", "Carry World Elite Mastercard"), ("2.2", "visacredit", "Or Infinite Visa"), ("3.3", "thameen", "Convert points to miles"),
               ("3.3", "offers", "Use travel offers")]},
    {"id": "cobrand", "who": "con", "name": "Earn with a co-brand",
     "why": "talabat and LuLu cards, both on Mastercard.",
     "steps": [("2.1", "talabat", "Get the talabat card"), ("2.1", "danat", "Or the LuLu Danat card"), ("3.3", "offers", "Collect cashback and offers")]},
    {"id": "islamic", "who": "con", "name": "Pay the Islamic way",
     "why": "Tayseer charge cards, paid in full each month.",
     "steps": [("2.3", "tayseer", "Take a Tayseer card"), ("5.3", "qpay", "Pay it off with Quick Pay")]},
    {"id": "family", "who": "young", "name": "Give a child or student a card",
     "why": "iLead for children with a parent dashboard, Cardy prepaid and the Student Card.",
     "steps": [("2.4", "ilead", "Give a child iLead"), ("5.1", "app", "Watch it in the parent dashboard"), ("2.4", "student", "Get a Student Card at university")]},
    {"id": "corp", "who": "corp", "name": "Run company spending",
     "why": "Corporate cards on both networks and Visa's virtual cards.",
     "steps": [("2.5", "mccorp", "Issue Mastercard corporate cards"), ("2.5", "vcp", "Pay suppliers with virtual cards"), ("4.2", "business", "Set limits and report")]},
    {"id": "merch", "who": "merch", "name": "Take payments as a merchant",
     "why": "Terminals, the gateway, Click to Pay and instalments.",
     "steps": [("2.6", "pos", "Install a CrediMax terminal"), ("2.6", "gateway", "Sell online through the gateway"), ("2.6", "c2p", "Offer Click to Pay"),
               ("2.7", "instal", "Offer instalments"), ("2.7", "bnpl", "Add BNPL with ONE App"), ("5.2", "mportal", "Reconcile in the Merchant Portal")]},
    {"id": "partner", "who": "partner", "name": "Launch a co-brand",
     "why": "talabat in 2026, Batelco's loyalty tie-up in 2025.",
     "steps": [("4.4", "partners", "Sign a partnership"), ("2.1", "talabat", "Issue a co-branded Mastercard"), ("3.4", "batelco", "Align loyalty with Batelco")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Half the credit range including World Elite, the talabat and LuLu co-brands, youth and prepaid cards, corporate cards, Click to Pay and the gateway.",
     "steps": [("2.1", "mccredit", "World Elite and World Mastercard"), ("2.1", "talabat", "The talabat co-brand"), ("2.4", "ilead", "iLead and Cardy"),
               ("2.5", "mccorp", "Corporate and World Business"), ("2.6", "c2p", "Click to Pay"), ("2.6", "gateway", "Mastercard Gateway ⚠")]},
    {"id": "mcnext", "who": "mc", "name": "Where instalments, fraud tools and the HSBC book could land",
     "why": "Where CrediMax has needs and Mastercard is not yet in: instalments and BNPL at the till, fraud scoring in an A2A-heavy market, the reissued HSBC book, virtual commercial cards and card-linked offers.",
     "steps": [("2.7", "instal", "Mastercard Installments at the POS"), ("3.1", "mccyber", "Fraud and identity scoring"), ("1.4", "hsbc", "Premium Mastercard for the HSBC book"),
               ("2.5", "vcp", "Virtual commercial cards against Visa"), ("3.3", "offers", "Card-linked offers for SAVUR"), ("1.4", "merger", "A merged BBK–NBB card book")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across CrediMax's map",
    "title": "A two-network issuer where Mastercard holds the top and the checkout",
    "lead": "CrediMax splits its fourteen credit cards almost evenly: seven on Mastercard, six on Visa and one on JCB. Mastercard has World Elite, the newest co-brand (talabat, May 2026), LuLu's Danat card, iLead, Cardy prepaid, corporate cards and Bahrain's first Click to Pay, renewed as a strategic partner in July 2023. Visa has the Tayseer Islamic cards, the student card, the multi-currency prepaid card and Visa Commercial Pay. Around both sits BENEFIT, part-owned by BBK, whose Fawri+ and BenefitPay rails carry most of Bahrain's everyday payments. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "CrediMax publishes no accounts, card counts, merchant counts or network volumes; the split is by product on its website. The gateway being Mastercard Gateway is inferred from its integration modes and the 2024 Click to Pay release.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit range", "7 Mastercard, 6 Visa, 1 JCB", "CrediMax website, Oct 2026"],
        ["Top tier", "World Elite Mastercard; Infinite Visa", "Premium-spend award from Mastercard, May 2024"],
        ["Co-brands", "talabat, LuLu Danat", "Both Mastercard; talabat May 2026"],
        ["Islamic & student", "Tayseer, Student Card", "Visa"],
        ["Commercial", "Corporate cards on both", "Visa Commercial Pay virtual cards, 2025 ⚠"],
        ["E-commerce", "Click to Pay, gateway", "Mastercard Gateway, 2024 ⚠"],
        ["Partnership", "Mastercard strategic deal", "Renewed 13 July 2023"],
        ["Domestic rails", "BENEFIT, Fawri+", "246m BenefitPay transfers in H1 2026"],
    ],
    "sides": {
        "neo": {"dir": "World Elite and half the credit range, the talabat and LuLu co-brands, iLead and Cardy, corporate cards, Click to Pay and the gateway.",
                "deals": "What it does not do: Islamic, student and multi-currency cards, virtual commercial cards, BNPL, fraud scoring or the domestic rails."},
        "snb": {"dir": "Visa's half of the credit range, Tayseer, Cardy EX and Visa Commercial Pay; JCB; BENEFIT, Fawri+ and BenefitPay; ONE App's BNPL.",
                "deals": "Where they meet: the HSBC reissue, a merged BBK–NBB book and instalments at CrediMax's terminals."},
    },
    "tl": [
        ["Jul 1991", "BBK issues Bahrain's first credit card"],
        ["Apr 1999", "CrediMax becomes a BBK subsidiary"],
        ["Jul 2023", "Mastercard strategic partnership renewed"],
        ["May 2024", "First Click to Pay in Bahrain; premium-spend award"],
        ["May 2024", "Mastercard MoU with BENEFIT"],
        ["2025", "Visa Commercial Pay ⚠"],
        ["Jul 2025", "BBK, CrediMax and Batelco MoU"],
        ["Nov 2025", "HSBC cards move to CrediMax; NBB merger MoU"],
        ["May 2026", "talabat co-brand on Mastercard"],
        ["Oct 2026", "BNPL with ONE App on CrediMax terminals"],
    ],
    "l": {
        "U": {"d": 1, "s": "About half of cardholders carry Mastercard.",
              "gap": "Premium, co-brand, youth and prepaid holders lean Mastercard; Islamic, student and multi-currency holders carry Visa.",
              "neo": "World Elite, talabat, Danat, iLead and Cardy holders; Mastercard corporate users.", "snb": "Visa, Tayseer and JCB holders; BenefitPay users."},
        "L5": {"d": 0, "s": "The front doors are CrediMax's and BBK's.", "gap": "App, portals and branches are their own.", "neo": "None.", "snb": "App, Merchant Portal, Quick Pay, BBK branches."},
        "L4": {"d": 1, "s": "Every line sells both networks.", "gap": "Co-brands are Mastercard; corporate virtual cards are Visa; acquiring takes everything.",
               "neo": "Co-brands, premium top tier.", "snb": "Islamic and student lines, virtual commercial cards."},
        "L3": {"d": 1, "s": "Mastercard cyber work is exploratory ⚠.", "gap": "Fraud, scoring and Thameen are CrediMax's own; a Mastercard cyber workshop ran in May 2025.",
               "neo": "Cyber intelligence explored ⚠; World card benefits.", "snb": "Own fraud, scoring, Thameen, Batelco, Fawateer."},
        "L2": {"d": 1, "s": "Half the cards and the checkout on Mastercard.", "gap": "Mastercard has seven credit cards, co-brands and Click to Pay; Visa has six, Tayseer and Commercial Pay; BNPL is ONE App's.",
               "neo": "Mastercard credit, co-brands, iLead, Cardy, corporate, Click to Pay, gateway ⚠.", "snb": "Visa credit, Tayseer, Cardy EX, Visa Commercial Pay, JCB, BNPL."},
        "L1": {"d": 0, "s": "BBK's foundation.", "gap": "Nothing in the foundation is Mastercard's; the processor is not named.", "neo": "None.", "snb": "BBK ownership, licence, processing arm, merger talks."},
    },
    "t": area_lens(LAYERS),
}
