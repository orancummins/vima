"""BRAC Bank's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from brac_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Bangladesh's leading SME bank as five discs that stack into one platform, from BDT 1.45 trillion of assets and "
       "BRAC's 46% stake at the bottom to the Astha app, branches, agents and bKash at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in "
       "the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("women", "Women (TARA)", "users-round"),
    ("sme", "Small businesses", "briefcase"),
    ("probashi", "Bangladeshis abroad", "plane"),
    ("wallet", "bKash users", "smartphone"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer: 2.3 million bank customers, among them 465,000 TARA women and more than 2 million "
              "SMEs served since 2001, Bangladeshis abroad sending money home, bKash's 84 million wallet users, and "
              "the corporates wholesale banking serves.")

WHO = {"con": "A BRAC Bank customer", "women": "A TARA customer", "sme": "A small business", "probashi": "A Bangladeshi abroad",
       "wallet": "A bKash user", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "The everyday loop: an account, a Visa debit card, the Astha app, Bangla QR and fraud checks.",
     "steps": [("4.3", "retail", "Open an account"), ("2.2", "visadebit", "Pay with Visa debit"), ("5.1", "astha", "Run it in Astha"),
               ("2.5", "banglaqr", "Pay by Bangla QR"), ("3.1", "fraud", "Protected from fraud")]},
    {"id": "credit", "who": "con", "name": "Borrow on a card",
     "why": "A digital application, then a Visa, Mastercard or Diners card, rewards and Google Pay on Visa.",
     "steps": [("3.2", "digitalcard", "Apply digitally"), ("2.1", "mccredit", "Take a Mastercard World"), ("2.1", "visacredit", "Or a Visa Signature or Infinite"),
               ("3.4", "rewards", "Earn rewards"), ("2.3", "gpay", "Tap with Google Pay (Visa)")]},
    {"id": "abroad", "who": "con", "name": "Spend and pay abroad",
     "why": "Multicurrency debit on both networks, medical quota cards and Visa Direct for fees abroad.",
     "steps": [("2.2", "mcdebit", "Carry a Mastercard multicurrency debit"), ("2.2", "visadebit", "Or a Visa medical quota card"),
               ("2.6", "visadirect", "Pay fees abroad with Visa Direct")]},
    {"id": "tara", "who": "women", "name": "Bank as a woman",
     "why": "TARA, with Mastercard TARA World and TARA debit and double points.",
     "steps": [("4.2", "tara", "Join TARA"), ("2.1", "mccredit", "Take a Mastercard TARA World"), ("2.2", "mcdebit", "Use TARA debit"),
               ("3.4", "rewards", "Earn double points"), ("5.1", "astha", "Bank in Astha")]},
    {"id": "sme", "who": "sme", "name": "Run a small business",
     "why": "An SME loan from a unit office, Visa business cards, card and QR acceptance and NPSB collections.",
     "steps": [("5.3", "branches", "Visit an SME unit office"), ("4.1", "sme", "Take a collateral-free loan"), ("4.1", "smecards", "Use a Visa business card"),
               ("2.4", "acquiring", "Take cards and QR"), ("2.5", "npsb", "Collect over NPSB")]},
    {"id": "remit", "who": "probashi", "name": "Send money home",
     "why": "Exchange houses into BRAC Bank accounts, or Mastercard Move into bKash wallets.",
     "steps": [("4.4", "probashi", "Open a Probashi account"), ("3.2", "ekyc", "Verify by eKYC"), ("2.6", "remitin", "Send through an exchange house"),
               ("2.7", "bkmove", "Or straight to bKash on Mastercard Move"), ("5.1", "astha", "Family sees it in Astha")]},
    {"id": "wallet", "who": "wallet", "name": "Live on bKash",
     "why": "bKash's wallet, agents and QR, and a digital bank on the way.",
     "steps": [("5.4", "bkagents", "Cash in at a bKash agent"), ("2.7", "bkash", "Pay and send with bKash"), ("2.5", "banglaqr", "Pay by QR"),
               ("2.7", "bkdigital", "Bank with bKash Digital Bank")]},
    {"id": "corp", "who": "corp", "name": "Move money as a corporate",
     "why": "Wholesale banking through CORPnet, with bKash cash management for distributors.",
     "steps": [("4.5", "wholesale", "Bank with wholesale"), ("5.2", "corpnet", "Pay through CORPnet"), ("2.7", "bkcash", "Sweep bKash e-money into deposits")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Mastercard credit, the first Mastercard debit cards, TARA, the MPGS gateway and bKash remittances on Move.",
     "steps": [("2.1", "mccredit", "World, TARA World and Millennial credit"), ("2.2", "mcdebit", "Platinum Multicurrency debit"),
               ("4.2", "tara", "TARA cards"), ("2.4", "gateways", "MPGS gateway"), ("2.7", "bkmove", "bKash remittances on Mastercard Move")]},
    {"id": "mcnext", "who": "mc", "name": "Where tokens, remittances and bKash could land",
     "why": "Where BRAC Bank has needs and Mastercard is not yet in: tokens and wallets, the bank's own remittances, SME cards, acquirer risk and bKash Digital Bank.",
     "steps": [("2.3", "gpay", "Mastercard tokens for phone payments"), ("2.6", "remitin", "Mastercard Move for the bank's remittances"),
               ("4.1", "smecards", "Commercial cards for SMEs"), ("2.4", "acquiring", "Acquirer risk tools for QR and cards"),
               ("2.7", "bkdigital", "Cards for bKash Digital Bank"), ("3.1", "fraud", "Fraud and scam scoring")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across BRAC Bank's map",
    "title": "A Visa-led bank whose Mastercard business is growing, mainly through bKash",
    "lead": "BRAC Bank uses several networks, but Visa has its top credit cards, most debit, Google Pay, tokens, outbound remittance and the January 2026 SME cards. Mastercard has World, TARA World and Millennial credit, the dual-network mass cards, its first debit cards (November 2025) and the MPGS gateway. Through bKash it also carries remittances on Mastercard Move. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are the bank's own (H1 2026 earnings disclosure, 13 August 2026; 2025 annual report) or from Bangladeshi press. The bank does not publish card numbers or volumes by network; market shares are Bangladesh Bank data for March 2025.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Credit", "Visa and Mastercard", "Visa Infinite/Signature on top; Mastercard World, TARA World"],
        ["Debit", "Mostly Visa", "Mastercard multicurrency since Nov 2025; TakaPay"],
        ["Wallets", "Google Pay on Visa", "February 2026; Mastercard token status unknown ⚠"],
        ["Acquiring", "MPGS and CyberSource", "11,000+ merchants"],
        ["Remittance out", "Visa Direct", "June 2025"],
        ["bKash remittance", "Mastercard Move", "June 2026"],
        ["Market", "Visa 71.8%", "Mastercard 17.5% of credit spending, March 2025"],
    ],
    "sides": {
        "neo": {"dir": "Mastercard credit (World, TARA World, Millennial), dual-network mass cards, Platinum Multicurrency debit, the MPGS gateway, and Move into bKash.",
                "deals": "What it does not do: most debit, phone payments, outbound remittance, SME cards or fraud tooling."},
        "snb": {"dir": "Visa premium credit, most debit, Google Pay and CyberSource tokens, Visa Direct and SME cards; Diners, TakaPay, NPSB and Bangla QR for the rest.",
                "deals": "Where they meet: dual-network credit, multicurrency debit and acquiring."},
    },
    "tl": [
        ["Apr 2016", "Mastercard Send into bKash with Western Union and BRAC Bank"],
        ["Jul 2019", "Visa Infinite and three other Visa cards"],
        ["Sep 2021", "Mastercard TARA World for women"],
        ["Oct 2021", "Mastercard Millennial Titanium"],
        ["Jun 2023", "Mastercard World (health and wellness)"],
        ["Nov 2023", "TakaPay domestic card launched"],
        ["Jun 2025", "Visa Direct for outward remittance"],
        ["Nov 2025", "First Mastercard debit cards"],
        ["Jan 2026", "Visa SME multicurrency cards"],
        ["Feb 2026", "Google Pay for Visa credit"],
        ["Jun 2026", "bKash on Mastercard Move"],
        ["Sep 2026", "bKash Digital Bank approved in principle"],
    ],
    "l": {
        "U": {"d": 1, "s": "Mastercard credit and new debit holders, TARA women, and bKash remittance receivers.",
              "gap": "Most debit holders and premium customers carry Visa; Mastercard reaches TARA, World and Millennial holders and bKash's remittance users.",
              "neo": "Mastercard cardholders, TARA, bKash remittance users.", "snb": "Visa debit and premium holders, TakaPay holders, SMEs."},
        "L5": {"d": 0, "s": "The front doors are the bank's and bKash's.", "gap": "Astha, CORPnet, branches and agents carry no network.", "neo": "None.", "snb": "Astha, CORPnet, branches, agents, bKash."},
        "L4": {"d": 1, "s": "TARA and retail partly on Mastercard.", "gap": "TARA's top cards are Mastercard; SME cards and premium banking are Visa; loans and wholesale have no network role.",
               "neo": "TARA, retail cards.", "snb": "SME cards, premium, wholesale, Probashi."},
        "L3": {"d": 1, "s": "Rewards and onboarding span both networks.", "gap": "No Mastercard fraud, identity or data product is named.",
               "neo": "Rewards and digital onboarding for Mastercard cards.", "snb": "Fraud, eKYC, scoring."},
        "L2": {"d": 1, "s": "Mastercard credit, new debit, MPGS and Move; Visa leads.", "gap": "Visa has most debit, tokens, Google Pay, Visa Direct and SME cards; Mastercard has credit, new debit, MPGS and bKash's Move.",
               "neo": "Mastercard credit and debit, MPGS, Move.", "snb": "Visa cards and tokens, Diners, TakaPay, NPSB, Bangla QR."},
        "L1": {"d": 0, "s": "The bank's own foundation.", "gap": "Nothing in the foundation is Mastercard's.", "neo": "None.", "snb": "Capital, BRAC, technology, strategy."},
    },
    "t": area_lens(LAYERS),
}
