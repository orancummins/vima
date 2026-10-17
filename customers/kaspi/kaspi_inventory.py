"""Kaspi.kz's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Kaspi.kz's own unless a source says otherwise: the Q2 2026 results and presentation
(10 August 2026), the 4Q and FY 2025 results (2 March 2026) and the Form 20-F for 2025 (16 March 2026).
Kaspi reports Kazakhstan without Türkiye unless stated. ``neo`` is the Mastercard lens: [depth, note],
where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not
Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://ir.kaspi.kz/media/2Q_2026_Results_.pdf"
Q2P = "https://ir.kaspi.kz/media/2Q_2026_Presentation.pdf"
Q1 = "https://ir.kaspi.kz/media/1Q_2026_Results_.pdf"
FY25 = "https://ir.kaspi.kz/media/4Q__FY_2025_Financial_Results_.pdf"
F20 = "https://ir.kaspi.kz/media/Form_20-F_2025.pdf"
HBANK = "https://finviz.com/news/368329/kaspikz-completes-acquisition-of-rabobank-a-in-turkiye"
BDDK = "https://finviz.com/news/363610/kaspikz-receives-regulatory-approval-to-acquire-rabobank-a-in-turkiye"
RABO = "https://ir.kaspi.kz/media/Kaspi.kz_to_acquire_Rabobank_Groups_Turkish_subsidiary_Rabobank_A.%C5%9E..pdf"
HEPSI = "https://ir.kaspi.kz/media/Kaspi.kz_Completes_Acquisition_of_Controlling_Interest_in_Hepsiburada.pdf"
TENCENT = "https://ir.kaspi.kz/media/Tencent_Invests_in_Kaspi.kz_Alongside_Co-Founder__CEO_Mikheil_Lomtadze_.pdf"
ALIPAY = "https://ir.kaspi.kz/media/Kaspi_.kz_Partnership_with_Alipay.pdf"
HUMO = "https://ir.kaspi.kz/media/Update_on_the_privatisation_of_Humo_payments_system_in_Uzbekistan.pdf"
FITCH = "https://ir.kaspi.kz/media/Fitch_Ratings_Assignment.pdf"
MOODYS = "https://ir.kaspi.kz/media/Moodys_Ratings_Assignment.pdf"
NBK = "https://nationalbank.kz/en/news/elektronnye-bankovskie-uslugi/20351"
GOLD = "https://kaspi.kz/gold"
GOLDVISA = "https://moneypanda.kz/kz/news/kakaya-platezhnaya-sistema-u-kart-kaspi-visa-ili-mastercard-819"
VISATOPUP = "https://guide.kaspi.kz/client/ru/gold/recharge/visa"
INTL = "https://guide.kaspi.kz/client/ru/transfers/services/international/q12971"
UNIONPAY = "https://kapital.kz/finance/150417/v-kaspikz-poyavilis-perevody-na-karty-unionpay.html"
INTERBANK = "https://kapital.kz/finance/150588/kaspikz-podklyuchilsya-k-mezhbankovskoj-sisteme-mobilnyh-platezhej.html"
QRFEES = "https://digitalbusiness.kz/2026-07-20/kaspi-kz-skazal-prodavtsam-chto-nuzhno-sdelat-so-starimi-kaspi-qr-chtobi-prodolzhit-torgovlyu/"
MAGAZIN = "https://finratings.kz/news/7214-v-kaspi-magazine-teper-oplachivat-pokupki-mozhno-kartami-liubykh-bankov/"
UQR = "https://paymentexpert.com/2025/11/13/kazakhstan-launches-qr-retail-payments/"
MCKZ = "https://en.qazmonitor.com/news/2137/mastercard-and-kazakhstan-launch-digital-country-partnership?amp=1"
MKT = "https://stockanalysis.com/stocks/KSPI"
HEPSIPAY = "https://ibsintelligence.com/ibsi-news/hepsipay-hits-new-milestone-with-10-million-users/"
WIKI = "https://en.wikipedia.org/wiki/Kaspi.kz"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · licences · owners", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $8 billion of revenue in 2025, Kaspi Bank's licence as a systemically important bank, founders who own 43%, an in-house technology stack, and a plan to be a 100-million-user company with Türkiye.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & returns", "blurb": "$8.0bn revenue, $2.1bn profit.", "div": "grp", "rev": "grp", "products": [
            P("scale", "Revenue & profit", "Consolidated revenue of KZT4,046 billion ($8.0 billion) in 2025, up 60% with Hepsiburada, and net income of KZT1,068 billion ($2.1 billion). In the second quarter of 2026 revenue was KZT1.1 trillion ($2.3 billion, +15%) and net income KZT259 billion ($539 million), stable; 2026 guidance is about 5% growth in adjusted EBITDA.",
              s=["cons", "merch"], neo=[0, ""], src=[["Kaspi.kz: Q2 2026 results, Aug 2026", Q2], ["Kaspi.kz: FY 2025 results, Mar 2026", FY25], ["Form 20-F 2025", F20]]),
            P("users", "Consumers & merchants", "15.7 million average monthly users of the Kaspi.kz Super App in 2025, 68% of them daily, with 77 transactions a month per active consumer; 764,000 active merchants on Kaspi Pay. Including Türkiye, 26.6 million active consumers in the first half of 2026.",
              s=["cons", "merch"], neo=[0, ""], src=[["Form 20-F 2025", F20], ["Kaspi.kz: Q2 2026 presentation", Q2P]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Licences & ratings", "blurb": "A systemic bank; BBB-/Baa3.", "div": "bank", "rev": "fin", "products": [
            P("licences", "Kaspi Bank & regulators", "Kaspi Bank JSC is regulated by the National Bank of Kazakhstan and the ARDFM as a systemically important bank, with a Tier 1 ratio of 19.6% at the end of 2025. The holding is rated BBB- by Fitch (2024) and Baa3 by Moody's ⚠ date; Hepsi Bank holds a full Turkish banking licence from July 2026.",
              s=["borrow"], neo=[0, ""], src=[["Form 20-F 2025", F20], ["Kaspi.kz: Fitch rating", FITCH], ["Kaspi.kz: Moody's rating", MOODYS], ["Kaspi.kz: Hepsi Bank completed, Jul 2026", HBANK]]),
        ]},
        {"id": "1.3", "ic": "users-round", "name": "Owners & leaders", "blurb": "Kim, Lomtadze, Tencent.", "div": "grp", "rev": "grp", "products": [
            P("owner", "Ownership & listing", "Nasdaq-listed since January 2024, with a market value of about $17.7 billion on 16 October 2026. Co-founders Mikheil Lomtadze (22.6%) and Vyacheslav Kim (20.8%) are the largest holders (January 2026); Tencent bought into the Baring funds' stake in about April 2026 ⚠ date.",
              s=["cons"], neo=[0, ""], src=[["Form 20-F 2025", F20], ["Kaspi.kz: Tencent invests", TENCENT], ["Stock Analysis, Oct 2026", MKT]]),
            P("leaders", "Board & management", "Chairman Vyacheslav Kim; CEO and co-founder Mikheil Lomtadze; CFO Tengiz Mosidze; Yuri Didenko for capital markets and Pavel Mironov as COO. 14,008 full-time staff at the end of 2025, 3,611 of them in Türkiye.",
              s=["cons"], neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & data", "blurb": "Own stack, four data centres.", "div": "grp", "rev": "grp", "products": [
            P("tech", "In-house technology", "Mobile-only, built in-house: four data centres at 99.99% availability, Kaspi Data Factory for data science and AI, and 4,455 technology staff. Kaspi says integrated payments 'reduce transaction costs by eliminating the need to rely on third parties'.",
              s=["cons", "merch"], o="B", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "100 million users.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "A 100-million-user company", "e-Commerce in Kazakhstan and Türkiye as the main growth driver, Hepsiburada run at about adjusted-EBITDA breakeven, fintech in Türkiye from 2027 and AI through Kasper. Headwinds: bank tax rose to 25% in 2026 and reserve requirements went up.",
              s=["cons", "merch"], st="new", neo=[0, ""], src=[["Kaspi.kz: FY 2025 results, Mar 2026", FY25], ["Kaspi.kz: Q2 2026 results, Aug 2026", Q2]]),
            P("deals", "Deals", "Hepsiburada (control from January 2025, now 86.7%), Rabobank A.Ş. (agreed March 2025, completed July 2026 as Hepsi Bank), Portmone in Ukraine (2021, sale agreed 2025) and a $600 million Eurobond (April 2026). A bid for Uzbekistan's Humo processing centre was dropped ⚠ date.",
              s=["cons"], o="A", neo=[0, ""], src=[["Kaspi.kz: Hepsiburada completed, Jan 2025", HEPSI], ["Kaspi.kz: Rabobank A.Ş., Mar 2025", RABO], ["Kaspi.kz: Humo update", HUMO], ["Form 20-F 2025", F20]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: the Kaspi Gold account and its Visa card, Kaspi's own QR and pay-by-palm network, Kaspi Red instalments, acceptance of other banks' cards, interbank and cross-border transfers, and B2B and bill payments. KZT44 trillion of payments in 2025.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Kaspi Gold", "blurb": "The account; card on Visa.", "div": "bank", "rev": "pay", "products": [
            P("gold", "Kaspi Gold (Visa)", "A digital account opened in the app, with a debit card that Kaspi says is a Visa card (January 2026); it works with Apple Pay and Google Pay and is printed in about 60 seconds at a Kaspi Kartomat. Payments active consumers: 14.6 million in 2025.", short="Kaspi Gold (Visa)",
              s=["cons"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="The country's most-used payment account carries Visa.",
              src=[["Kaspi.kz: Kaspi Gold", GOLD], ["MoneyPanda, Jan 2026", GOLDVISA], ["Form 20-F 2025", F20]]),
            P("visatopup", "Top-ups through Visa", "Kaspi Gold can be topped up by phone number from another bank's card 'through the Visa service'.",
              s=["cons"], lc="move", o="P", at="Visa", neo=[0, "Visa."], src=[["Kaspi Guide: top-ups via Visa", VISATOPUP]]),
            P("goldkids", "Kaspi Gold for children", "A Kaspi Gold account and card for children, run from a parent's app. Network not stated ⚠.",
              s=["cons"], lc="open", neo=[None, "Probably Visa ⚠."], src=[["Kaspi.kz: Kaspi Gold", GOLD]]),
        ]},
        {"id": "2.2", "ic": "zap", "name": "Kaspi QR & Alaqan", "blurb": "Kaspi's own closed loop.", "div": "pay", "rev": "pay", "products": [
            P("kaspiqr", "Kaspi QR", "Kaspi's own payments network between the two super-apps, in shops and online; Kaspi QR and card payments were 69% of KZT44.2 trillion of TPV in 2025. Merchants pay 0.95% on Kaspi Gold payments by QR (July 2026).", short="Kaspi QR (own network)",
              s=["cons", "merch"], lc="move", o="B", ay="2019", neo=[0, "Kaspi's own network."],
              mc="Most of Kaspi's volume never touches a card scheme.",
              src=[["Form 20-F 2025", F20], ["Kaspi.kz: FY 2025 results, Mar 2026", FY25], ["Digital Business, Jul 2026", QRFEES]]),
            P("alaqan", "Kaspi Alaqan pay-by-palm", "Pay by palm without a card or phone, launched in Almaty in December 2025: 511,000 people registered and 9.2% of Kaspi payments at enabled stores within three months; national roll-out during 2026.",
              s=["cons", "merch"], lc="move", st="new", ay="Dec 2025", o="B", neo=[0, "Kaspi's own network."],
              src=[["Kaspi.kz: FY 2025 results, Mar 2026", FY25], ["Kaspi.kz: Q2 2026 results, Aug 2026", Q2]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Kaspi Red", "blurb": "Shopping-club instalments.", "div": "bank", "rev": "fin", "products": [
            P("red", "Kaspi Red", "A shopping-club card with instalments at Kaspi merchants, with credit lines that grow with active users. The National Bank counts 28.4 million cards on local systems and names Kaspi.kz's local system, so Kaspi Red is probably on Kaspi's own scheme ⚠.",
              s=["cons"], lc="borrow", o="B", neo=[None, "Network not public; probably Kaspi's own ⚠."],
              src=[["Form 20-F 2025", F20], ["National Bank of Kazakhstan, Sep 2026", NBK]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acceptance", "blurb": "Other banks' Visa and Mastercard.", "div": "pay", "rev": "pay", "products": [
            P("pos", "Kaspi POS & Smart POS", "Kaspi POS, Smart POS and mobile POS for 764,000 active merchants. They take other banks' cards at 1.3–1.35% (July 2026), but those volumes are 'significantly lower' than Kaspi QR and Kaspi Gold.", short="Kaspi POS (every network)",
              s=["merch"], lc="move", o="B", neo=[1, "Accepts Visa and Mastercard from other banks."],
              mc="Where Mastercard cards meet Kaspi's merchants.",
              src=[["Form 20-F 2025", F20], ["Digital Business, Jul 2026", QRFEES]]),
            P("magazincards", "Other banks' cards on Kaspi Magazin", "Since September 2025 shoppers can pay on Kaspi's marketplace with a Visa or Mastercard card from any Kazakh bank, one card at a time.",
              s=["cons", "seller"], lc="move", st="new", ay="Sep 2025", neo=[1, "Visa and Mastercard from other banks."],
              src=[["Finratings, Sep 2025", MAGAZIN]]),
        ]},
        {"id": "2.5", "ic": "arrow-left-right", "name": "Transfers & cross-border", "blurb": "Interbank QR, transfers, Alipay+.", "div": "pay", "rev": "pay", "products": [
            P("interbank", "Interbank QR & phone transfers", "Kaspi joined the National Bank's interbank mobile-payment system on 17 July 2026: other banks' apps can pay at more than 700,000 Kaspi QR points, and transfers by phone number work across banks. The unified QR went live in November 2025.",
              s=["cons", "merch"], lc="move", st="new", ay="Jul 2026", o="P", at="National Bank of Kazakhstan", neo=[0, "National rails."],
              src=[["Kapital.kz, Jul 2026", INTERBANK], ["Payment Expert, Nov 2025", UQR], ["Digital Business, Jul 2026", QRFEES]]),
            P("p2p", "P2P transfers", "Free instant transfers between Kaspi customers in the app; P2P was 8% of 2025 TPV.",
              s=["cons"], lc="move", o="B", neo=[0, "Kaspi's own network."], src=[["Form 20-F 2025", F20]]),
            P("intl", "Transfers abroad", "From Kaspi Gold to Visa and Mastercard cards worldwide except Russia, and to Elkart, Uzcard and Humo cards; UnionPay added on 14 July 2026. The rails behind card transfers are not stated ⚠.",
              s=["cons", "trav"], lc="move", neo=[1, "Sends to Mastercard cards; rails not public ⚠."],
              mc="Remittances to Central Asia and Türkiye are where Mastercard Move could fit.",
              src=[["Kaspi Guide: transfers abroad", INTL], ["Kapital.kz, Jul 2026", UNIONPAY]]),
            P("alipay", "Kaspi QR in China (Alipay+)", "Since April 2024 Kaspi customers can pay by QR at more than 80 million points in China through Alipay+.",
              s=["trav"], lc="move", ay="Apr 2024", o="P", at="Alipay+", neo=[0, "Alipay+."],
              src=[["Kaspi.kz: Alipay+ partnership, Apr 2024", ALIPAY]]),
        ]},
        {"id": "2.6", "ic": "receipt-text", "name": "B2B & bills", "blurb": "KZT2.8tn of B2B.", "div": "pay", "rev": "pay", "products": [
            P("b2b", "Kaspi B2B Payments", "Merchants and suppliers issue and settle invoices instantly: KZT2.8 trillion of TPV in 2025 (+45%) and 79.7 million transactions.",
              s=["merch", "seller"], lc="move", o="B", neo=[0, "Kaspi's own network."],
              mc="B2B is growing fastest and runs off the card schemes.",
              src=[["Form 20-F 2025", F20]]),
            P("bills", "Household bill payments", "Commission-free bill payments in the app for more than 10,000 services; 16% of 2025 TPV.",
              s=["cons"], lc="everyday", o="B", neo=[0, "Kaspi's own network."], src=[["Form 20-F 2025", F20], ["Kaspi.kz: Kaspi Gold", GOLD]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every payment: biometric identity and in-house credit models, the Kasper AI assistant, bonuses, cashback and advertising, government services in the app, and Kaspi's own delivery network.",
    "tiles": [
        {"id": "3.1", "ic": "fingerprint", "name": "Identity & risk", "blurb": "Biometrics; loans in 6 seconds.", "div": "bank", "rev": "fin", "products": [
            P("kaspiid", "Kaspi ID biometrics", "Face recognition to open accounts and confirm transactions, which Kaspi says prevents fraud.",
              s=["cons"], lc="open", o="B", neo=[0, "Kaspi's own."],
              mc="Identity and fraud tools would sit next to Kaspi's own.",
              src=[["Form 20-F 2025", F20]]),
            P("risk", "Credit models", "Models built on 231 million loans and 44.5 billion transactions; 99.9% of loans decided in under six seconds; cost of risk 2.2% in 2025 and NPLs of 7.0% at mid-2026.",
              s=["borrow"], lc="borrow", o="B", neo=[0, "Kaspi's own."], src=[["Form 20-F 2025", F20], ["Kaspi.kz: Q2 2026 results, Aug 2026", Q2]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI", "blurb": "Kasper shops for you.", "div": "grp", "rev": "mkt", "products": [
            P("kasper", "Kasper AI assistant", "A personal AI assistant, launched in July 2026 for shopping in Kazakh or Russian; about 20% of eligible consumers used it within a month, and about 80% of conversations produce a recommendation.",
              s=["cons"], lc="grow", st="new", ay="Jul 2026", o="B", neo=[0, ""],
              mc="An agent that shops is where Agent Pay and tokens could fit.",
              src=[["Kaspi.kz: Q2 2026 results, Aug 2026", Q2]]),
            P("aisupport", "AI customer service", "The in-house virtual assistant handled 14.2 million chats (64% of all) and 6.2 million calls (38%) in 2025.",
              s=["cons"], lc="everyday", o="B", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
            P("aimerchant", "Kaspi AI for partners", "AI-written listings, photos and descriptions for marketplace merchants.",
              s=["seller"], lc="grow", o="B", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty & advertising", "blurb": "Bonuses, cashback, ads.", "div": "grp", "rev": "mkt", "products": [
            P("bonus", "Kaspi Bonus", "Bonuses on Kaspi Gold spending and purchases with merchants, spent on later purchases; booked as a deduction from fee revenue.",
              s=["cons"], lc="everyday", o="B", neo=[0, ""], src=[["Form 20-F 2025", F20], ["Kaspi.kz: Kaspi Gold", GOLD]]),
            P("cashback", "Merchant Cashback", "Merchants choose products, cashback amounts and customer segments, and pay for the cashback themselves.",
              s=["seller", "merch"], lc="grow", o="B", neo=[0, ""],
              mc="Merchant-funded offers are what card-linked offers do for issuers.",
              src=[["Form 20-F 2025", F20]]),
            P("ads", "Kaspi Advertising", "Ads in the app and on Instagram, Facebook, TikTok and Google; advertising revenue grew 64% in 2025.",
              s=["seller"], lc="grow", o="B", neo=[0, ""], src=[["Kaspi.kz: FY 2025 results, Mar 2026", FY25], ["Form 20-F 2025", F20]]),
        ]},
        {"id": "3.4", "ic": "building-2", "name": "Government & tax", "blurb": "Passports to tax returns.", "div": "grp", "rev": "pay", "products": [
            P("gov", "Government services", "Digital documents, driving-licence renewal, car registration, business registration, taxes and birth certificates in the Kaspi.kz app.",
              s=["cons", "merch"], lc="beyond", o="P", at="Government of Kazakhstan", neo=[0, ""], src=[["Form 20-F 2025", F20], ["Wikipedia: Kaspi.kz", WIKI]]),
            P("register", "POS Register & tax tools", "Cash-register software in Kaspi Pay that issues fiscal receipts, used by 40% of merchants since 2023, with tax reports and payments.",
              s=["merch"], lc="everyday", o="B", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "3.5", "ic": "rocket", "name": "Delivery & logistics", "blurb": "10,441 Postomats.", "div": "grp", "rev": "mkt", "products": [
            P("delivery", "Kaspi Delivery & Postomats", "182 million orders delivered in 2025 (+84%), 58% of them to 10,441 Kaspi Postomats, 84% free to the buyer; 10 dark stores for e-Grocery.",
              s=["cons", "seller"], lc="everyday", o="B", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What it sells: consumer credit and BNPL, finance for merchants, deposits, e-commerce, travel and classifieds in Kazakhstan, and Hepsiburada and Hepsi Bank in Türkiye.",
    "tiles": [
        {"id": "4.1", "ic": "hand-coins", "name": "Consumer finance", "blurb": "BNPL is 41% of lending.", "div": "bank", "rev": "fin", "products": [
            P("bnpl", "BNPL & Kaspi Kredit", "Buy now, pay later at Kaspi merchants was 41% of KZT11.7 trillion of lending in 2025; general-purpose loans too. The average net loan book was KZT7.3 trillion ($15.2 billion) in Q2 2026 (+18%).",
              s=["cons", "borrow"], lc="borrow", o="B", neo=[0, "Off the card schemes."],
              mc="Instalments without a card take the place of credit cards.",
              src=[["Kaspi.kz: FY 2025 results, Mar 2026", FY25], ["Kaspi.kz: Q2 2026 results, Aug 2026", Q2]]),
            P("carloan", "Car finance", "Car loans, including for cars bought on Kolesa.kz; a growing share of the book.",
              s=["borrow"], lc="borrow", o="B", neo=[0, ""], src=[["Kaspi.kz: Q2 2026 results, Aug 2026", Q2], ["Form 20-F 2025", F20]]),
        ]},
        {"id": "4.2", "ic": "briefcase-business", "name": "Merchant finance", "blurb": "18% of lending.", "div": "bank", "rev": "fin", "products": [
            P("merchfin", "Merchant & micro-business finance", "Working capital and buy-inventory-now-pay-later for merchants; the fastest-growing loan product and 18% of lending in 2025.",
              s=["merch", "seller"], lc="borrow", o="B", neo=[0, ""],
              mc="Commercial and virtual cards for supplier payments could sit beside it.",
              src=[["Kaspi.kz: FY 2025 results, Mar 2026", FY25], ["Form 20-F 2025", F20]]),
        ]},
        {"id": "4.3", "ic": "coins", "name": "Deposits", "blurb": "KZT7.5tn in customer accounts.", "div": "bank", "rev": "fin", "products": [
            P("deposits", "Kaspi Deposit", "Savings and three-month term deposits: KZT7.5 trillion of customer accounts at the end of 2025, with funding costs of 14.5% in Q2 2026; the three-month rate was cut by 1 point in August 2026.",
              s=["cons", "borrow"], lc="grow", o="B", neo=[0, ""], src=[["Kaspi.kz: FY 2025 results, Mar 2026", FY25], ["Kaspi.kz: Q2 2026 results, Aug 2026", Q2]]),
            P("bizdeposit", "Business Deposit", "A savings account for merchants from August 2024: 138,000 accounts and KZT229 billion by the end of 2025.",
              s=["merch"], lc="grow", st="new", ay="Aug 2024", o="B", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "4.4", "ic": "chart-column", "name": "Marketplace & travel", "blurb": "KZT6.7tn GMV.", "div": "grp", "rev": "mkt", "products": [
            P("ecom", "e-Commerce & e-Grocery", "e-Commerce GMV of KZT3.2 trillion in 2025 and 184.7 million orders (+83%); e-Grocery GMV KZT206 billion (+53%). Group e-Commerce GMV, with Türkiye, was KZT1.3 trillion in Q2 2026 (+28%).",
              s=["cons", "seller"], lc="grow", o="B", neo=[0, ""], src=[["Kaspi.kz: FY 2025 results, Mar 2026", FY25], ["Kaspi.kz: Q2 2026 results, Aug 2026", Q2]]),
            P("mcom", "m-Commerce", "Buying in a shop with Kaspi financing and payment: KZT2.9 trillion of GMV in 2025, as shoppers move online.",
              s=["cons", "merch"], lc="grow", o="B", neo=[0, ""], src=[["Kaspi.kz: FY 2025 results, Mar 2026", FY25]]),
            P("travel", "Kaspi Travel", "Flights, rail tickets and holidays: KZT538 billion of GMV in 2025 (+14%), used by 19% of monthly users.",
              s=["trav"], lc="beyond", o="A", ay="Aug 2020", neo=[0, ""], src=[["Kaspi.kz: FY 2025 results, Mar 2026", FY25], ["Form 20-F 2025", F20]]),
            P("classifieds", "Classifieds", "Kolesa.kz (cars) and Krisha.kz (property) lead their categories; Turbo.az, Tap.az and Bina.az in Azerbaijan have more than 2.5 million monthly users.",
              s=["cons", "seller"], lc="beyond", o="A", neo=[0, ""], div="kolesa", src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "4.5", "ic": "flag", "name": "Türkiye", "blurb": "Hepsiburada and Hepsi Bank.", "div": "hepsi", "rev": "mkt", "products": [
            P("hepsiburada", "Hepsiburada", "One of Türkiye's leading e-commerce platforms, 86.7% owned since January 2025: GMV of TRY212.7 billion and 11.8 million consumers in 2025, run at about adjusted-EBITDA breakeven.",
              s=["tr"], lc="grow", o="A", ay="Jan 2025", neo=[0, ""], src=[["Kaspi.kz: Hepsiburada completed, Jan 2025", HEPSI], ["Kaspi.kz: FY 2025 results, Mar 2026", FY25]]),
            P("hepsibank", "Hepsi Bank & Hepsicredit", "Rabobank A.Ş., bought on 15 July 2026 and renamed Hepsi Bank, to be capitalised with about $300 million; a Hepsicredit shopping loan is in pilot (0.4% of GMV in June), with lending and deposits a priority from 2027.",
              s=["tr"], lc="borrow", st="new", ay="Jul 2026", o="A", div="hbank", neo=[None, "No cards yet."],
              mc="A new bank with no card network chosen.",
              src=[["Kaspi.kz: Hepsi Bank completed, Jul 2026", HBANK], ["Kaspi.kz: BDDK approval, Jun 2026", BDDK], ["Kaspi.kz: Q2 2026 results, Aug 2026", Q2]]),
            P("hepsipay", "Hepsipay", "Hepsiburada's wallet, BNPL and loans; about 10 million users in April 2024 ⚠.",
              s=["tr"], lc="move", o="A", neo=[None, "Networks not public."], src=[["IBS Intelligence, Apr 2024", HEPSIPAY]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How people reach Kaspi: the consumer and merchant super-apps, a network of kiosks, ATMs and card machines, and partners from Glovo to the other Kazakh banks.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Kaspi.kz Super App", "blurb": "15.7m monthly users.", "div": "grp", "rev": "grp", "products": [
            P("app", "Kaspi.kz Super App", "Payments, shopping, travel, loans, deposits and government services in one app: 15.7 million average monthly users and 10.7 million daily in 2025.",
              s=["cons"], lc="open", o="B", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Kaspi Pay Super App", "blurb": "764,000 merchants.", "div": "pay", "rev": "pay", "products": [
            P("payapp", "Kaspi Pay Super App", "The merchant app: accept payments, sell on the marketplace, arrange delivery, borrow, keep a business account and file taxes.",
              s=["merch", "seller"], lc="open", o="B", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Physical network", "blurb": "Kiosks, ATMs, Kartomats.", "div": "bank", "rev": "fin", "products": [
            P("kiosks", "Kiosks, ATMs & Kartomats", "3,708 payment kiosks, 3,261 ATMs and 140 Kartomats that print a Kaspi Gold card in about 60 seconds (end of 2025).",
              s=["cons"], lc="open", o="B", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
            P("partners", "Partners", "Glovo inside the super-app, Alipay+ in China, Kaspi QR open to every Kazakh bank through the National Bank's system, and Visa for Kaspi Gold.",
              s=["cons", "merch"], lc="open", o="P", at="Glovo, Alipay+, Visa", neo=[0, ""],
              src=[["Form 20-F 2025", F20], ["Kapital.kz, Jul 2026", INTERBANK], ["Kaspi.kz: Alipay+ partnership, Apr 2024", ALIPAY]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Kaspi.kz", "blurb": "At the edges: acceptance and transfers.", "products": [
        P("mcatkaspi", "Mastercard at Kaspi.kz", "No Mastercard card programme or joint initiative with Kaspi is public. Mastercard cards from other banks are accepted on Kaspi POS and on Kaspi Magazin, and Kaspi Gold sends money to Mastercard cards abroad. Kaspi Gold itself is Visa. Mastercard signed a Digital Country Partnership with Kazakhstan's government in September 2023.",
          s=["cons"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["MoneyPanda, Jan 2026", GOLDVISA], ["Finratings, Sep 2025", MAGAZIN], ["Qazmonitor, Sep 2023", MCKZ]]),
    ]},
    {"id": "pillar-market", "name": "Kazakhstan's payments market", "blurb": "Visa 49%, local 34%, Mastercard 17%.", "products": [
        P("market", "The market", "84.3 million cards at 1 September 2026: Visa 41.0 million, local systems 28.4 million, Mastercard 14.1 million and UnionPay 0.75 million. 2.7 billion QR payments worth KZT13.7 trillion in January–August 2026. The National Bank's unified QR and phone transfers link every bank.",
          s=["cons"], div="grp", rev="grp", src=[["National Bank of Kazakhstan, Sep 2026", NBK], ["Payment Expert, Nov 2025", UQR]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
