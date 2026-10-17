"""BAC's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from bac_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Central America's largest bank as five discs that stack into one platform, from US$46.9 billion of assets in six "
       "countries at the bottom to the BAC app, branches and card partners at the top. Click the stack to open it. Choose who "
       "you are and what you want to do, and the areas that deliver it light up across the layers, joined in the order "
       "they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("con", "Everyday customers", "user-round"),
    ("prem", "Travellers & premium cardholders", "plane"),
    ("remit", "Remittance families", "send"),
    ("home", "Homebuyers", "house"),
    ("sme", "Small businesses & merchants", "store"),
    ("corp", "Corporates", "factory"),
]
USERS_DESC = ("Six kinds of customer, more than 6 million in all across Costa Rica, Panama, Guatemala, Honduras, El Salvador "
              "and Nicaragua: everyday customers, travellers and premium cardholders, families receiving remittances, "
              "homebuyers, more than 300,000 businesses and the corporates behind the region's supplier payments.")

WHO = {"con": "A BAC customer", "prem": "A premium cardholder", "remit": "A family receiving remittances", "home": "A homebuyer",
       "sme": "A small business", "corp": "A corporate treasurer"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "everyday", "who": "con", "name": "Bank day to day",
     "why": "An account opened in the app, La Roja debit on Visa or Mastercard, a phone wallet and SINPE Móvil.",
     "steps": [("4.1", "accounts", "Open an account in the app"), ("2.3", "debit", "Pay with La Roja debit"), ("2.7", "wallets", "Tap with Apple or Google Pay"),
               ("2.8", "sinpe", "Send by SINPE Móvil"), ("5.1", "app", "Run it in the app")]},
    {"id": "card", "who": "con", "name": "Borrow on a card",
     "why": "A BAC credit card on Visa, Mastercard or Amex, paid off in Tasa Cero instalments and earning points.",
     "steps": [("2.1", "credit", "Take a BAC credit card"), ("2.4", "tasacero", "Split a purchase with Tasa Cero"), ("3.3", "loyalty", "Earn points or cashback")]},
    {"id": "travel", "who": "prem", "name": "Travel on a premium card",
     "why": "Mastercard Black and Unlimited, Visa Infinite or Amex Platinum, with airline miles.",
     "steps": [("2.2", "premium", "Carry a premium card"), ("2.2", "cobrand", "Earn AAdvantage, LifeMiles or ConnectMiles"), ("3.3", "loyalty", "Redeem through Mi Viaje")]},
    {"id": "remit", "who": "remit", "name": "Receive money from family abroad",
     "why": "Remittances into Guatemala, Honduras, El Salvador and Nicaragua, spent on debit.",
     "steps": [("2.9", "remesa", "Receive with Mi Remesa BAC"), ("5.2", "rapibac", "Collect at Rapibac or a branch"), ("2.3", "debit", "Spend on debit")]},
    {"id": "home", "who": "home", "name": "Buy a home",
     "why": "A BAC mortgage through a branch.",
     "steps": [("5.2", "branches", "Visit a branch"), ("4.2", "mortgages", "Take a mortgage")]},
    {"id": "sme", "who": "sme", "name": "Get paid as a small business",
     "why": "A 54% acquirer: terminals, softPOS, payment links and instalments for customers.",
     "steps": [("4.3", "sme", "Open a business account"), ("2.5", "hit", "Take cards on a phone with HIT"), ("2.6", "compraclick", "Sell online with Compra Click"),
               ("2.4", "tasacero", "Offer Tasa Cero"), ("2.5", "acquiring", "Settle through BAC acquiring")]},
    {"id": "corp", "who": "corp", "name": "Run treasury across the region",
     "why": "Payroll, supplier payments and statements across six countries through APIs and host-to-host links.",
     "steps": [("4.3", "corporate", "Bank with BAC corporate"), ("3.4", "treasury", "Connect by API or host-to-host"), ("2.9", "ameritransfer", "Pay across borders")]},
    {"id": "panama", "who": "con", "name": "Move from Multibank to BAC",
     "why": "About 100,000 Multibank clients joining BAC Panamá in 2026.",
     "steps": [("1.4", "multibank", "Become a BAC Panamá client"), ("1.2", "mkt_pa", "Bank with BAC Panamá"), ("2.1", "credit", "Get a BAC card")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "Part of BAC's credit and debit in every market, premium Black and Unlimited cards, Digital First, wallets and acceptance at BAC's merchants.",
     "steps": [("2.1", "credit", "Mastercard credit cards"), ("2.3", "debit", "Mastercard debit, most in Nicaragua"), ("2.3", "digitalfirst", "Digital First certification"),
               ("2.2", "premium", "Mastercard Black and Unlimited"), ("2.5", "acquiring", "Acceptance at BAC merchants")]},
    {"id": "mcnext", "who": "mc", "name": "Where acquiring, remittances and Multibank could land",
     "why": "Where BAC has needs and Mastercard is not yet in: checkout at the region's largest acquirer, remittance payouts, the Multibank reissue, supplier-payment cards, data and an AI assistant.",
     "steps": [("2.6", "compraclick", "Click to Pay on Compra Click"), ("2.9", "remesa", "Mastercard Move for remittances"), ("1.4", "multibank", "Multibank cards reissued on Mastercard"),
               ("4.3", "corporate", "Commercial cards for supplier payments"), ("3.2", "icbac", "Spending insights"), ("5.1", "app", "Agent Pay for a future assistant")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across BAC's map",
    "title": "One of three networks at the region's card leader",
    "lead": "BAC issues about 41% of Central America's credit-card volume and acquires about 54%, under long-term agreements with Visa, Mastercard and American Express. Mastercard carries part of its credit and debit in all six markets, most in Nicaragua, plus Black and Unlimited cards and the 2021 Digital First certification. Amex leads the Costa Rica catalogue and the premium tier, Visa holds Infinite travel cards, and BAC runs its own acquiring, instalments and transfers. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are BAC's own (IIQ 2026 presentation, September 2026) or from BAC's country websites and press. Network split is read from BAC's card catalogues, which count products, not volumes; agreement terms and dates are not public.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Issuing", "Visa, Mastercard, Amex", "About 41% of regional credit volume"],
        ["Acquiring", "BAC, all brands", "About 54% share"],
        ["Costa Rica credit", "Amex 27, Visa 20, Mastercard 16", "Products in the catalogue"],
        ["Nicaragua", "Mostly Mastercard", "Credit and debit ⚠"],
        ["Digital First", "Mastercard", "First in the region, Dec 2021"],
        ["Apple Pay checkout", "Visa and Amex", "Compra Click, Jul 2024"],
        ["Instant payments", "SINPE Móvil, ACH", "Not card rails"],
    ],
    "sides": {
        "neo": {"dir": "Part of credit and debit in every market, Black and Unlimited cards, Walmart in Guatemala and El Salvador, Digital First, wallets and acceptance at BAC's merchants.",
                "deals": "What it does not do: Amex's premium lead, BAC's own instalments, transfers, loyalty and data."},
        "snb": {"dir": "Visa and Amex cards, BAC's in-house acquiring and Tasa Cero, SINPE Móvil and ACH, remittances and treasury.",
                "deals": "Where they meet: every card product family is offered on more than one network."},
    },
    "tl": [
        ["Feb 2006", "Discover acceptance through Credomatic"],
        ["Dec 2021", "Mastercard Digital First certification"],
        ["2022", "Spun off from Grupo Aval; S&P investment grade"],
        ["Nov 2022", "Unlimited Mastercard in Panama"],
        ["Jun 2024", "Google Wallet for Visa and Mastercard"],
        ["Jul 2024", "Apple Pay on Compra Click for Visa and Amex"],
        ["Mar 2026", "Multi Financial Group bought"],
        ["Jun 2026", "Multibank merged into BAC Panamá"],
        ["Sep 2026", "Fitch upgrades BAC to investment grade"],
    ],
    "l": {
        "U": {"d": 1, "s": "Many BAC customers carry Mastercard, alongside Visa and Amex.",
              "gap": "Everyday and premium cardholders are split three ways; remittance families and treasurers use BAC's own rails.",
              "neo": "Mastercard cardholders in six markets, most in Nicaragua.", "snb": "Visa and Amex cardholders, SINPE and ACH users, remittance families."},
        "L5": {"d": 0, "s": "The front doors are BAC's.", "gap": "App, branches and Rapibac are BAC's; co-brand partners are split across networks.",
               "neo": "Co-brands such as Walmart in Guatemala and La Colonia.", "snb": "App, branches, Rapibac."},
        "L4": {"d": 0, "s": "The business lines carry cards from all three networks.", "gap": "Accounts come with Visa or Mastercard debit; loans, mortgages and pensions have no network role.",
               "neo": "Debit on accounts.", "snb": "Loans, mortgages, corporate banking, pensions."},
        "L3": {"d": 0, "s": "BAC's own services.", "gap": "Loyalty, data and treasury APIs are BAC's; fraud vendors are not public.",
               "neo": "None public.", "snb": "Points and miles, Índice de Consumo, treasury APIs."},
        "L2": {"d": 1, "s": "Mastercard is one of three card networks.", "gap": "Cards and acceptance run on all brands; instalments, instant payments and remittances are BAC's or local rails.",
               "neo": "Credit, debit, premium, Digital First, wallets, acceptance.", "snb": "Visa and Amex, Tasa Cero, SINPE Móvil, ACH, Mi Remesa."},
        "L1": {"d": 0, "s": "BAC's own foundation.", "gap": "Capital, owners and strategy are BAC's; each market issues Mastercard among others.",
               "neo": "A share of each market's cards.", "snb": "Capital, owners, Multibank, strategy."},
    },
    "t": area_lens(LAYERS),
}
