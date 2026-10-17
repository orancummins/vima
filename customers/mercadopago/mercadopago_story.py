"""Mercado Pago's kinds of user, journeys and Mastercard lens, as at 17 October 2026 (see page_data.py)."""
# ruff: noqa: E501

from mercadopago_inventory import LAYERS

from customers.lens_tiles import area_lens

SUB = ("Latin America's largest fintech as five discs that stack into one, from $12.6 billion of revenue, payment and "
       "credit licences and two pending bank licences at the bottom to one app in 18 countries at the top. Click the "
       "stack to open it. Choose who you are and what you want to do, and the areas that deliver it light up across the "
       "layers, joined in the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

USERS = [  # key, label, icon (a key of the template's ICONS)
    ("cons", "Consumers", "user-round"),
    ("sme", "Small merchants", "store"),
    ("seller", "Mercado Libre sellers", "briefcase"),
    ("unb", "Unbanked & benefit recipients", "hand-coins"),
    ("invest", "Savers", "trending-up"),
    ("ent", "Online businesses & developers", "code-xml"),
]
USERS_DESC = ("Six kinds of user: 88 million monthly active consumers, the small merchants who take payments on Point "
              "machines and phones, sellers on Mercado Libre, people without a bank account or receiving social benefits, "
              "savers and investors, and the online businesses and developers who use its checkout.")

WHO = {"cons": "A consumer", "sme": "A small merchant", "seller": "A Mercado Libre seller", "unb": "Someone without a bank",
       "invest": "A saver", "ent": "An online business"}

# Steps are (area, product, label).
OUTCOMES = [
    {"id": "card", "who": "cons", "name": "Get a credit card in the app",
     "why": "The engine of engagement: 2.6 million cards issued a quarter, on Visa in Brazil and Mexico and on Mastercard in Argentina.",
     "steps": [("5.1", "app", "Apply in the app"), ("3.1", "credit", "Get a limit from in-house underwriting"),
               ("2.3", "brcc", "Visa in Brazil"), ("2.3", "arcc", "Or Mastercard in Argentina"), ("3.5", "meliplus", "Earn cashback with Meli+")]},
    {"id": "pay", "who": "cons", "name": "Pay every day from the account",
     "why": "Debit cards, Pix, QR and transfers from one free account.",
     "steps": [("4.1", "account", "Open a free account"), ("2.4", "mxdebit", "Pay with a Debit Mastercard in Mexico"),
               ("2.5", "pix", "Pay by Pix in Brazil"), ("2.5", "qr", "Scan a QR code in Argentina")]},
    {"id": "accept", "who": "sme", "name": "Take payments in a shop",
     "why": "Point machines and phones, every card network, Pix and QR, and credit on the takings.",
     "steps": [("2.1", "point", "Take cards on a Point machine"), ("2.1", "taptopay", "Or tap on a phone"),
               ("2.1", "acquiring", "Settled by Mercado Pago's acquiring"), ("4.2", "merchants", "Borrow against sales")]},
    {"id": "sell", "who": "seller", "name": "Sell on Mercado Libre and get paid",
     "why": "Mercado Pago is the marketplace's checkout, with instalments on its own card.",
     "steps": [("4.3", "marketplace", "Sell on Mercado Libre"), ("2.2", "checkout", "Get paid through the checkout"),
               ("3.1", "bnpl", "Buyers pay in instalments without a card"), ("3.6", "savings", "Keep the money earning")]},
    {"id": "save", "who": "invest", "name": "Make money earn",
     "why": "$23 billion under management: pots, money-market funds and crypto.",
     "steps": [("5.1", "app", "Open the app"), ("3.6", "savings", "Put money in savings pots or funds"),
               ("5.3", "partners", "Invested by GBM, BICE or Mercado Fondo"), ("2.6", "crypto", "Or buy Meli Dólar")]},
    {"id": "bank", "who": "unb", "name": "Get banked",
     "why": "Benefit payments, a prepaid card and first-time credit for people outside the banks.",
     "steps": [("4.4", "benefits", "Receive benefits into Mercado Pago"), ("2.4", "arprepaid", "Spend on a prepaid Mastercard"),
               ("2.4", "clprepaid", "Or a prepaid Mastercard in Chile"), ("3.1", "bnpl", "Get first-time credit")]},
    {"id": "salary", "who": "cons", "name": "Move my salary to Mercado Pago",
     "why": "Payroll is the next step, and the reason for the bank licences in Mexico and Argentina.",
     "steps": [("4.4", "payroll", "Bring my salary"), ("1.2", "mxlic", "Into a bank account in Mexico"),
               ("1.2", "arlic", "Or in Argentina"), ("2.4", "mxdebit", "Spend on the debit card")]},
    {"id": "online", "who": "ent", "name": "Sell online",
     "why": "Checkout, links and subscriptions for online businesses.",
     "steps": [("5.3", "developers", "Integrate the APIs"), ("2.2", "checkout", "Take payments online"),
               ("3.3", "security", "Screened by Mercado Pago's own models")]},
    {"id": "mcnow", "who": "mc", "name": "Where Mastercard already is",
     "why": "The Mexican debit card, the Argentine credit and prepaid cards, the Chilean prepaid card, acceptance everywhere, and a history going back to 2016.",
     "steps": [("2.4", "mxdebit", "Debit Mastercard in Mexico"), ("2.3", "arcc", "Mastercard credit card in Argentina"),
               ("2.4", "clprepaid", "Prepaid Mastercard in Chile"), ("2.1", "acquiring", "Acceptance on every Point"),
               ("2.1", "payfac", "Payment facilitator since 2016")]},
    {"id": "mcnext", "who": "mc", "name": "Where bank licences, tokens and Brazil could land",
     "why": "Where Mercado Pago has needs and Mastercard is not yet in: the new bank programmes in Mexico and Argentina, the Chilean credit card, tokens and Click to Pay on the checkout, acquirer risk, fraud and identity, and the Brazilian card.",
     "steps": [("1.2", "mxlic", "Debit for the new Mexican bank"), ("2.3", "clcc", "The Chilean credit card"),
               ("3.2", "tokens", "Tokens and Click to Pay"), ("3.3", "security", "Fraud and identity"),
               ("2.3", "brcc", "The Brazilian card, now Visa")]},
]

# The Mastercard lens: the template's VS object. d: 3 Mastercard-run, 2 on Mastercard, 1 partly, 0 not, None can't tell.
LENS = {
    "asof": "17 October 2026",
    "kicker": "Mastercard, across Mercado Pago's map",
    "title": "Mastercard in the Spanish-speaking wallets; Visa holds Brazil and the cards that are growing",
    "lead": "Mastercard runs Mercado Pago's debit card in Mexico, its credit and prepaid cards in Argentina and its prepaid card in Chile, and the relationship goes back to a 2016 payment-facilitator deal and the 2018 prepaid launch. Visa holds the debit and credit cards in Brazil, Mercado Pago's largest market, and the credit card in Mexico, so most of a $7.7 billion card book growing at 91% sits with Visa. Pix, SPEI and QR take more payments off the cards altogether. Each of the areas below is marked by how deep Mastercard goes in it.",
    "qnote": "Figures are MercadoLibre's own releases and Mercado Pago's country sites, with press where marked. Mercado Pago does not publish its network split or a card book by country.",
    "how": "A mark records how much of an area runs on Mastercard, in public sources as at 17 October 2026: Mastercard's own product running it, the whole capability riding on Mastercard, part of it, or none. It is this map's judgement and says nothing about volumes.",
    "q": [
        ["Brazil cards", "Visa", "Credit since 2021; debit too"],
        ["Mexico credit", "Visa", "Launched 2023"],
        ["Mexico debit", "Mastercard", "Debit Mastercard"],
        ["Argentina", "Mastercard", "Credit and prepaid"],
        ["Chile", "Mastercard prepaid", "9m+ cards; credit planned"],
        ["Acquiring", "$64bn a quarter", "Every network"],
        ["Off-card", "Pix, SPEI, QR", "And card-free instalments"],
        ["Bank licences", "Mexico, Argentina", "Pending in 2026"],
    ],
    "sides": {
        "neo": {"dir": "Debit in Mexico, credit and prepaid in Argentina, prepaid in Chile, acceptance on every Point machine and checkout, and a payment-facilitator deal from 2016.",
                "deals": "What it does not do: the Brazilian cards, the Mexican credit card, tokens, Click to Pay, Agent Pay or fraud services in public."},
        "snb": {"dir": "Visa on the Brazilian debit and credit cards and the Mexican credit card, with Visa tokens and Vai de Visa; Pix, SPEI and QR; Mercado Pago's own credit, fraud models and AI.",
                "deals": "Where they meet: every card payment, the coming bank programmes and the Chilean credit card."},
    },
    "tl": [
        ["Sep 2016", "Mastercard payment facilitator in Argentina"],
        ["Feb 2018", "Mastercard prepaid cards in three countries"],
        ["Mar 2021", "Brazil credit card on Visa"],
        ["Nov 2022", "Chile prepaid on Mastercard"],
        ["2023", "Mexico credit card on Visa"],
        ["Nov 2024", "Modo dispute over Visa tokens on QR"],
        ["May 2025", "Argentina bank licence requested"],
        ["Feb 2026", "Visa agrees to buy Prisma and Newpay"],
        ["Aug 2026", "$101bn quarterly volume; card book $7.7bn"],
        ["Sep 2026", "Mexico licence halfway; Argentina expected by year-end"],
    ],
    "l": {
        "U": {"d": 1, "s": "Consumers in Mexico, Argentina and Chile carry Mastercard; Brazilians carry Visa.",
              "gap": "Mastercard is in the wallet for Spanish-speaking consumers and accepted by every merchant; Brazilian cardholders and Mexican credit-card holders are on Visa.",
              "neo": "Mexican debit, Argentine and Chilean cardholders, every merchant.", "snb": "Brazilian cardholders, Mexican credit cards, Pix and QR users."},
        "L5": {"d": 0, "s": "The front doors are Mercado Pago's.", "gap": "App, resellers and partners are its own.",
               "neo": "None.", "snb": "App, resellers, developers, partners."},
        "L4": {"d": 1, "s": "Mastercard in every line through acceptance and some cards.", "gap": "Accounts, merchants and the marketplace accept Mastercard; benefits and payroll do not involve it.",
               "neo": "Acceptance; cards in Mexico and Argentina.", "snb": "Brazilian accounts on Visa; benefits and payroll."},
        "L3": {"d": 1, "s": "The engine room is Mercado Pago's own.",
               "gap": "Credit runs partly on Mastercard cards; tokens are Visa's in public; fraud, AI, loyalty and savings are its own.",
               "neo": "Card loans in Argentina; tokens from 2019 ⚠.", "snb": "Visa tokens, Vai de Visa, own models, Meli+."},
        "L2": {"d": 1, "s": "Split by country: Visa in Brazil, Mastercard in the Spanish-speaking markets.",
               "gap": "Mastercard has debit in Mexico, cards in Argentina and prepaid in Chile; Visa has Brazil and Mexican credit; Pix, QR, SPEI and crypto are off the cards.",
               "neo": "Acquiring, Argentine and Mexican cards, Chilean prepaid.", "snb": "Brazilian cards, Mexican credit, Pix, QR, SPEI."},
        "L1": {"d": 0, "s": "Mercado Pago's own scale and licences.", "gap": "Nothing in the foundation is Mastercard's.",
               "neo": "None.", "snb": "Licences, parent, platform, strategy."},
    },
    "t": area_lens(LAYERS),
}
