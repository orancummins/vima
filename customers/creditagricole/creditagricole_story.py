"""Crédit Agricole's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from creditagricole_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("France's largest retail banking group as five discs that stack into one platform, from a cooperative owned by 12.3 million "
       "mutual shareholders at the bottom to the Ma Banque app, LCL and 8,065 branches at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in "
       "the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("young", "Young customers", "graduation-cap"),
    ("borrower", "Borrowers & drivers", "hand-coins"),
    ("saver", "Savers & investors", "coins"),
    ("farm", "Farmers", "factory"),
    ("sme", "Professionals & small businesses", "briefcase"),
    ("corp", "Corporates & institutions", "building-2"),
]
USERS_DESC = ("Seven kinds of customer, 55 million in all: everyday customers of the Regional Banks, LCL and CA Italia, the young "
              "people ACT 2028 targets, borrowers and drivers at Sofinco, Agos and Leasys, savers and investors with Amundi and "
              "the insurer, farmers, professionals and small businesses, and the corporates CACIB and CACEIS serve.")

WHO = {"con": "A Crédit Agricole customer", "young": "A young customer", "borrower": "A borrower", "saver": "A saver",
       "farm": "A farmer", "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop at a Regional Bank: an account, a CB and Mastercard card, the Ma Banque app, Wero and transaction security.",
     "steps": [("4.1", "regional", "Open an account at a Regional Bank"), ("2.1", "racards", "Pay with a CB and Mastercard card"),
               ("5.1", "apps", "Run it in Ma Banque"), ("2.5", "wero", "Pay friends with Wero"), ("3.2", "fraud", "Protected by CAPS")]},
    {"id": "phone", "who": "con", "name": "Pay with a phone",
     "why": "The group's own wallet on Android and, since June 2026, on iPhone, beside Apple Pay.",
     "steps": [("2.5", "paiementmobile", "Pay with Paiement Mobile"), ("2.5", "wallets", "Or use Apple Pay"), ("2.1", "racards", "Choose CB, Mastercard or Visa")]},
    {"id": "young", "who": "young", "name": "Get a first card",
     "why": "Mozaïc Mastercard for 10–17s, Mouv by LCL, and Wero.",
     "steps": [("5.2", "branches", "Open an account in branch"), ("2.1", "racards", "Get a Mozaïc Mastercard"), ("2.2", "lclcards", "Or Mouv by LCL"), ("2.5", "wero", "Get paid back with Wero")]},
    {"id": "premium", "who": "con", "name": "Travel with a premium card",
     "why": "Gold and World Elite Mastercard, with fingerprint versions, or Visa Premier and Infinite.",
     "steps": [("3.3", "premium", "Choose a premium card"), ("2.1", "biometric", "Pay by fingerprint"), ("2.2", "lclcards", "Or Visa Infinite at LCL")]},
    {"id": "borrow", "who": "borrower", "name": "Borrow and drive",
     "why": "Cartwin's revolving credit, Sofinco and Agos, CA Auto Bank and Leasys.",
     "steps": [("2.1", "cartwin", "Carry a Cartwin card"), ("4.3", "capfm", "Borrow from Sofinco or lease with Leasys"), ("4.5", "assurances", "Insure the car")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "A professional account, Mastercard business cards, CAWL or Up2pay to take payments, and Amex acceptance.",
     "steps": [("4.1", "lclbank", "Bank with LCL or a Regional Bank"), ("2.3", "procards", "Spend with a Mastercard Business card"),
               ("2.6", "cawl", "Take payments with CAWL"), ("2.6", "up2pay", "Or Up2pay mobile"), ("2.6", "amexaccept", "Accept American Express")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "CACIB, CACEIS, leasing and tokenised finance.",
     "steps": [("4.4", "cacib", "Bank with CACIB"), ("4.3", "leasing", "Lease equipment"), ("4.4", "caceis", "Hold assets at CACEIS"), ("2.7", "stablecoin", "Settle in a euro stablecoin")]},
    {"id": "save", "who": "saver", "name": "Save and invest",
     "why": "Amundi, the insurer, Indosuez and the new German savings platform.",
     "steps": [("4.5", "amundi", "Invest with Amundi"), ("4.5", "assurances", "Save in life insurance"), ("1.5", "germany", "Save with CA Savings in Germany")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The Regional Banks' Mastercard-led cards, biometric and business cards, part of LCL, Poland with Priceless, CAPS processing and the first agentic payment in France.",
     "steps": [("2.1", "racards", "Regional Bank cards"), ("2.1", "biometric", "Biometric Mastercard"), ("2.3", "procards", "Business cards"),
               ("2.2", "lclcards", "Part of LCL"), ("3.3", "priceless", "Priceless in Poland"), ("3.1", "agentpay", "Agent Pay")]},
    {"id": "mcnext", "who": "mc", "name": "Where agents, the wallet and CAWL could land",
     "why": "Where Crédit Agricole has needs and Mastercard is not yet in: agents at scale, tokens for its own wallet, acquirer tools at a wholly owned CAWL, fraud scoring for Wero, commercial cards for mid-caps and the new German bank.",
     "steps": [("3.1", "agents", "Agent Pay for customer-facing agents"), ("2.5", "paiementmobile", "Tokens for Paiement Mobile"),
               ("2.6", "cawl", "Acquirer risk and Click to Pay at CAWL"), ("3.2", "fraud", "Scam scores for Wero and instant payments"),
               ("4.4", "cacib", "Commercial cards for mid-caps and IKB"), ("1.5", "germany", "Cards for Crédit Agricole Deutschland")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Crédit Agricole's map",
    "title": "Mastercard leads the cards, but CB, Wero and the group's own wallet carry the payments",
    "lead": "The Regional Banks' cards are co-badged with Cartes Bancaires and lean to Mastercard, with Mastercard-only tiers, fingerprint cards and business cards, and Visa offered alongside. LCL is mixed, CA Italia debit is Visa and Poland is split. Most domestic payments still route over CB. The group co-owns Wero, launched its own iPhone wallet in June 2026 and now owns CAWL outright. In June 2026 it ran France's first agentic payment on Mastercard Agent Pay. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the group's own (Q2 2026 results, 31 July 2026) or from Regional Bank, LCL, CA Italia and CA Polska card pages, Worldline and press. No group-wide split of cards by network is published; the group's press site refused connections, and Nexi credit, LCL Mouv and wallet token services were not verified.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Regional Banks", "Mastercard-led, CB co-badged", "Visa alongside at Classic, Premier, Infinite"],
        ["Business cards", "Mastercard", "Professionnel, Business, Business World"],
        ["LCL", "Visa and Mastercard", "Visa Premier and Infinite; Platinum+"],
        ["Italy", "Visa debit", "Bancomat, Nexi credit, Amex"],
        ["Poland", "Visa and Mastercard", "Priceless on Mastercard Maxima"],
        ["Agentic", "Agent Pay", "First in France, June 2026"],
        ["Wallets", "Wero and Paiement Mobile", "About 5m Wero users a month"],
        ["Acquiring", "CAWL", "Wholly owned since June 2026"],
    ],
    "sides": {
        "neo": {"dir": "Regional Bank and business cards, biometric cards, part of LCL, Poland with Priceless, CAPS processing of Mastercard, and Agent Pay.",
                "deals": "What it does not do: domestic routing over CB, Wero, the group's own wallet, CA Italia debit, AI or the stablecoin."},
        "snb": {"dir": "Cartes Bancaires on every French card, Visa at LCL and in Italy and Egypt, Wero, Paiement Mobile, Amex acceptance, and the group's own AI and KYC.",
                "deals": "Where they meet: CAPS and CAWL, which process and accept every scheme."},
    },
    "tl": [
        ["Jun 2019", "Biometric Mastercard trial with CAPS"],
        ["Jan 2020", "Apple Pay, CB first"],
        ["Jul 2021", "CA Italia's Visa Debit partnership"],
        ["2023", "CAWL with Worldline"],
        ["Oct 2023", "American Express acceptance"],
        ["Oct 2024", "Wero for all customers"],
        ["Nov 2025", "ACT 2028 plan"],
        ["Jun 2026", "Paiement Mobile on iPhone"],
        ["Jun 2026", "First agentic payment in France on Agent Pay"],
        ["Jun 2026", "Crédit Agricole sole owner of CAWL"],
        ["Oct 2026", "Crédit Agricole Deutschland; IKB deal"],
    ],
    "l": {
        "U": {"d": 1, "s": "Most French cardholders carry Mastercard beside CB.",
              "gap": "Regional Bank and business cardholders mostly carry Mastercard; LCL is mixed; CA Italia and Egypt customers carry Visa.",
              "neo": "Regional Bank, business and many LCL cardholders; Polish Mastercard holders.", "snb": "Visa holders at LCL and in Italy, Wero users, savers, corporates."},
        "L5": {"d": 0, "s": "The front doors are the group's.", "gap": "Apps, branches and partners are Crédit Agricole's; Mastercard is not a named strategic partner.", "neo": "None in public view.", "snb": "Ma Banque, LCL app, branches, partners."},
        "L4": {"d": 1, "s": "Mastercard inside French retail banking.", "gap": "Regional Banks and LCL issue Mastercard; CA Italia is Visa; consumer finance, CIB and savings have no network role in view.",
               "neo": "Regional Banks, LCL in part, Poland.", "snb": "CA Italia, CAPFM, CACIB, Amundi, insurance."},
        "L3": {"d": 1, "s": "Agent Pay and Priceless; the rest is the group's.", "gap": "The first agentic payment ran on Agent Pay and Poland uses Priceless; fraud, KYC and AI agents are the group's own.",
               "neo": "Agent Pay, Priceless, premium cards.", "snb": "CAPS security, Digital Trust, AI agents."},
        "L2": {"d": 1, "s": "Mastercard on most cards; CB, Wero and the wallet beside it.", "gap": "Mastercard leads Regional Bank and business cards; CB routes domestic payments, Visa holds Italy and part of LCL, and Wero, Paiement Mobile and CAWL are the group's own.",
               "neo": "Regional Bank, biometric and business cards, part of LCL, Poland, CAPS.", "snb": "CB, Visa, Wero, Paiement Mobile, CAWL, Amex, stablecoin."},
        "L1": {"d": 0, "s": "The group's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, heritage, AI, strategy."},
    },
    "t": area_lens(LAYERS),
}
