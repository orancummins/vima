"""Slovenská sporiteľňa's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the H1 2026 results and half-year report
(30 July 2026), the Q1 2026 investor presentation and the 2025 audited accounts. ``neo`` is the Mastercard
lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1REL = "https://www.slsp.sk/en/news/2026/7/30/slovenska-sporitelna-reports-net-profit-of-eur-176-8-million-in-the-first-half-of-the-year"
H1PDF = "https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/en/aktuality/obchodne-vysledky-slovenskej-sporitelne-30062026-en.pdf"
HYR = "https://cdn.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/documents/financne-ukazovatele/polrocna-sprava-slovenskej-sporitelne-30062026.pdf"
INFO = "https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/en/aktuality/slsp-infografika-2q-2026-en.pdf"
PRES = "https://cdn.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/documents/dlhopisy/investor-presentation.pdf"
FACT = "https://cdn.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/documents/footer-pdfs/factsheet-sk.pdf"
PROFILE = "https://www.slsp.sk/en/information-about-bank/about-bank/bank-profile"
MGMT = "https://www.slsp.sk/en/information-about-bank/about-bank/management-of-the-bank"
CEO = "https://www.slsp.sk/en/news/2026/3/2/michaela-bauer-has-taken-over-as-chief-executive-officer-of-slovenska-sporitelna"
VISA21 = "https://sita.sk/slovenska-sporitelna-a-visa-posilnuju-svoje-partnerstvo-uvedenim-udrzatelnych-kariet-na-slovensku/"
VISA16 = "https://www.slsp.sk/en/news/2016/2/12/uz-1-milion-kariet-visa-od-slovenskej-sporitelne"
APPLEPAY = "https://www.mynewsdesk.com/sk/visa/pressreleases/sluzba-apple-pay-je-od-dnes-dostupna-pre-drzitelov-kariet-visa-na-slovensku-a-v-dalsich-12-europskych-krajinach-2958685"
DEBIT = "https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/documents/zverejnenia/zverejnenie-debetne-karty-01022025.pdf"
BIZDEBIT = "https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/documents/zverejnenia/zverejnenie-debetne-karty-podnikatel-01012026.pdf"
CREDIT = "https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/documents/zverejnenia/zverejnenie-kreditne-karty.pdf"
CARDS = "https://www.slsp.sk/sk/ludia/karty"
FEES26 = "https://sita.sk/vofinanciach/velka-zmena-poplatkov-v-slovenskej-sporitelni-prichadzaju-lacnejsie-prevody-aj-drahsie-plastove-karty/"
MW19 = "https://www.teraz.sk/ekonomika/slovenska-sporitelna-vylepsuje-verno/396872-clanok.html"
ACQ = "https://slsp.sk/en/business/receiving-payments"
GPJV = "https://www.retailbankerinternational.com/news/caixabank-global-payments-erste-group-form-jv-in-central-and-eastern-europe-020616-4911785/"
PAYME = "https://www.teraz.sk/ekonomika/slovenska-sporitelna-spusta-digit/523447-clanok.html"
INST25 = "https://touchit.sk/slovenske-banky-okamzite-platby-2025/654228/"
QR = "https://www.epravo.sk/top/clanky/slovensko-startuje-eru-qr-platieb-financna-sprava-aj-banky-su-pripravene-6676.html"
GAI = "https://www.startitup.sk/?p=1236180"
MB = "https://cdn0.erstegroup.com/content/dam/sk/slsp/www_slsp_sk/documents/zverejnenia/zverejnenie-k-vernostnemu-programu-moneyback-01072025.pdf"
MBL = "https://touchit.sk/slovenska-sporitelna-spusta-pre-takmer-milion-ludi-digitalnu-inovaciu-moneyback/339350/"
TATRA = "https://WWW.tatrabanka.sk/files/archiv/obchodne-podmienky/obchodne-podmienky-pravnicke-osoby/medzinarodne-platobne-karty/DodatokkObchodnympodmienkamprefiremnedebetnekarty.pdf"
VUB = "https://www.podnikajte.sk/financny-manazment/vub-meni-podmienky-firemnych-debetnych-kreditnych-kariet-od-1-7-2026"
WERO = "https://www.trendingtopics.eu/oesterreichische-banken-steigen-bei-europaeischer-zahlungsloesung-wero-ein/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · Erste · 200 years", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Slovakia's largest bank with €27.6 billion of assets and ROE above 15%, two hundred years of savings banking, Erste Group as sole owner, a new chief executive from March 2026, and George as the group platform.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "€176.8m in the half, ROE 15.3%.", "div": "slsp", "rev": "alm", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of €27.6 billion, loans of €20.7 billion and deposits of €19.8 billion at 30 June 2026; net profit of €176.8 million in the half (+18.9%) and €310.3 million in 2025; ROE 15.3%, cost/income 38.9%, capital adequacy 20.4%; Moody's A1 deposits, A3 issuer, Aaa covered bonds.",
              s=["con"], neo=[0, ""], src=[["H1 2026 results", H1PDF], ["Investor presentation, Q1 2026", PRES]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Bauer took over in March 2026.", "div": "slsp", "rev": "alm", "products": [
            P("leadership", "Board of directors", "Michaela Bauer, chief executive since 1 March 2026 (from ČSOB and KBC), succeeding Peter Krutil; Pavel Cetkovský (risk), Milan Hain (IT, payments and operations), Juraj Barta (retail), Marek Sásik (corporate and markets) and Slavomír Seemann (CFO from April 2026). Alexandra Habeler-Drabek of Erste chairs the supervisory board.",
              s=["corp"], st="new", ay="Mar 2026", neo=[0, ""], src=[["SLSP: management", MGMT], ["SLSP: Bauer takes over, Mar 2026", CEO], ["Factsheet, Apr 2026", FACT]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & Erste", "blurb": "Since 1825; Erste's since 2001.", "div": "erste", "rev": "alm", "products": [
            P("heritage", "Two hundred years", "Savings banks opened in Bratislava, Trnava, Banská Bystrica and Levoča in 1825; the first ATM in Czechoslovakia in 1989; the first Slovak bank licensed for all types of Visa card; bicentenary in 2025.",
              s=["con"], o="I", neo=[0, ""], src=[["SLSP: bank profile", PROFILE], ["Infographic, H1 2026", INFO]]),
            P("erste", "Erste Group", "Sole owner since 2001: Erste has 23.1 million customers in eight markets and bought 49% of Santander Bank Polska in January 2026. Its Austrian bank issues Debit Mastercard and joined Wero in June 2026, so the group is not one-network.",
              s=["corp"], o="A", neo=[0, "Group context."], src=[["Investor presentation, Q1 2026", PRES], ["Trending Topics: Austrian banks join Wero, Jun 2026", WERO]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "George and OpenAI.", "div": "george", "rev": "retail", "products": [
            P("tech", "George platform & AI", "George, Erste's group-built banking platform, in Slovakia since January 2018; George AI on an OpenAI model hosted in EU data centres, with client data not used for training; spending on modernisation and digitalisation named as a cost driver in 2026.",
              s=["corp"], o="B", neo=[0, ""], src=[["Startitup: George AI, Sep 2026", GAI], ["H1 2026 results", H1REL]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & holdings", "blurb": "Largest digital bank.", "div": "slsp", "rev": "alm", "products": [
            P("strategy", "Strategy", "\"The best financial partner\", \"exceptional digital solutions\" and \"different from other banks\": the new chief executive aims to stay Slovakia's largest digital bank and widen investing. No public numeric targets of its own ⚠; Erste's group targets apply.",
              s=["corp"], neo=[0, ""], src=[["Factsheet, Apr 2026", FACT], ["SLSP: Bauer takes over, Mar 2026", CEO]]),
            P("holdings", "Subsidiaries & stakes", "LANED (property), SLSP Social Finance (60.4%), SLSP Seed Starter, a 9.98% stake with 35% of votes in the building society Prvá stavebná sporiteľňa, a third of the Slovak Banking Credit Bureau, 28% of the cash-processing venture Monilogi, and 19.28% of Holding Card Service in Prague, linked to the card-acquiring venture ⚠.",
              s=["corp"], neo=[0, ""], src=[["Half-year report 2026", HYR]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: 1.94 million cards, all Visa since an exclusive deal in 2021; credit cards; virtual cards and phone wallets on Visa tokens; business debit; card acceptance through the Global Payments joint venture, the one place Mastercard runs; and SEPA Instant, Payme links and the new national QR payments.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "1.94m cards, all Visa.", "div": "slsp", "rev": "retail", "products": [
            P("debit", "Visa debit cards", "Visa Electron, Visa Standard and Visa Platinum on personal accounts, contactless and five-year validity; 1.94 million cards issued in all at 30 June 2026. Since April 2026 a physical card on a SPACE account costs €10, and only phone, watch or credit-card payments count towards fee waivers. Visa-exclusive since July 2021.", short="Debit (Visa)",
              s=["con"], lc="everyday", st="flux", o="P", at="Visa", neo=[0, "Visa."],
              mc="The largest card base in Slovakia, locked to Visa since 2021.",
              src=[["Debit card disclosure, Feb 2025", DEBIT], ["H1 2026 results", H1PDF], ["SITA: SLSP and Visa, Jul 2021", VISA21], ["SITA: fee changes, Nov 2025", FEES26]]),
            P("junior", "Visa Junior", "A card for children aged 6 to 14 on a SPACE account, with monthly limits of €100 cash and €200 in shops, PIN shown in the George kids' app.",
              s=["young"], lc="open", o="P", at="Visa", neo=[0, "Visa."], src=[["Debit card disclosure, Feb 2025", DEBIT], ["SLSP: cards", CARDS]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Visa Classic and Gold.", "div": "slsp", "rev": "retail", "products": [
            P("credit", "Visa credit cards", "Visa Classic and Visa Gold; the Štedrá karta was withdrawn from sale on 1 July 2025. Credit cards earned only €1.2 million of fees in the first half of 2026, against €28 million from debit card payments.", short="Credit (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Credit card disclosure, Jul 2025", CREDIT], ["Half-year report 2026", HYR]]),
            P("mcworld", "Mastercard World (retired)", "As late as May 2019 the Exclusive account came with half-price Mastercard World, offering lounge access, Mastercard Elite travel perks and ClaimAir; Mastercard Mass and Maestro were also sold. By June 2021 the card disclosures list only Visa ⚠ exact end date not found.",
              s=["con"], lc="everyday", st="retired", ay="2019", o="P", at="Mastercard", neo=[0, "Mastercard until about 2020 ⚠; retired."],
              mc="The last Mastercard issuing at the bank.",
              src=[["TASR: Exclusive account, May 2019", MW19]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "Virtual cards & wallets", "blurb": "Free virtual Visa, Apple Pay.", "div": "slsp", "rev": "retail", "products": [
            P("virtual", "Virtual cards", "Up to three free virtual Visa cards per account, open to 15-year-olds with a SPACE account from 9 January 2026, as physical cards start to carry a fee.",
              s=["con", "young"], lc="everyday", st="new", ay="Jan 2026", o="P", at="Visa", neo=[0, "Visa."], src=[["SITA: fee changes, Nov 2025", FEES26], ["Debit card disclosure, Feb 2025", DEBIT]]),
            P("dobra", "Dobrá karta", "A virtual card for which the bank's foundation gives 0.2% of every payment to a non-profit the client chooses, up to €15,000 a quarter.",
              s=["con"], lc="beyond", st="new", o="B", neo=[0, "Visa ⚠."], src=[["Infographic, H1 2026", INFO]]),
            P("wallets", "Phone & watch wallets", "Apple Pay (June 2019), Google Pay, Garmin Pay, SwatchPAY! and Xiaomi Pay on debit cards, all on Visa's tokens.",
              s=["con"], lc="everyday", o="P", at="Visa, Apple, Google", neo=[0, "Visa tokens."], src=[["Visa: Apple Pay in Slovakia, Jun 2019", APPLEPAY], ["SLSP: cards", CARDS]]),
        ]},
        {"id": "2.4", "ic": "briefcase", "name": "Business cards", "blurb": "Visa Business debit.", "div": "slsp", "rev": "corporates", "products": [
            P("bizdebit", "Business debit cards", "Visa Business Electron, Visa Business and Visa Business Platinum, with daily limits up to €60,000, and a deposit-only business card. No corporate credit or virtual commercial card is advertised ⚠.",
              s=["sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="No commercial credit or virtual card programme in public: an open field.",
              src=[["Business debit card disclosure, Jan 2026", BIZDEBIT]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "Global Payments JV.", "div": "gp", "rev": "corporates", "products": [
            P("accept", "POS terminals", "Card terminals for merchants, processed by Global Payments s.r.o., a joint venture of Global Payments, CaixaBank and Erste formed in 2016 from Erste's acquiring in the Czech Republic, Slovakia and Romania.", short="Acceptance (all networks)",
              s=["sme"], lc="move", ay="2016", o="P", at="Global Payments", neo=[1, "Accepts Mastercard and Visa."],
              mc="Where Mastercard volume meets the bank.",
              src=[["SLSP: receiving payments", ACQ], ["Retail Banker International: Erste JV, Jun 2016", GPJV]]),
            P("webpay", "GP webpay & Sporopay", "Online card payments through GP webpay (Visa, Mastercard and Diners Club) and Sporopay, the bank's own e-shop payment button.",
              s=["sme"], lc="move", o="P", at="Global Payments", neo=[1, "Accepts Mastercard and Visa."], src=[["SLSP: receiving payments", ACQ]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Instant & account payments", "blurb": "SEPA Instant, Payme, QR.", "div": "slsp", "rev": "retail", "products": [
            P("instant", "SEPA & instant payments", "SEPA Instant, which Slovak banks must send and receive since 9 October 2025; urgent transfers in George cost €0.22 from January 2026, and cross-border transfers in George €5.",
              s=["con", "sme"], lc="move", st="new", neo=[0, "Account rails."], src=[["Touchit: instant payments 2025", INST25], ["SITA: fee changes, Nov 2025", FEES26]]),
            P("payme", "Payme", "Payment links shared over chat, SMS or e-mail that fill in a transfer in any bank's app, built by members of the Slovak Banking Association; launched at the bank on 28 January 2021.",
              s=["con"], lc="move", ay="Jan 2021", o="P", at="Slovak Banking Association", neo=[0, "Account rails."], src=[["TASR: Payme launch, Jan 2021", PAYME]]),
            P("qr", "National QR payments", "From 1 May 2026, QR payments on the Payme standard with the Financial Administration, with the bank one of five offering full support including instant-payment notification; merchants need no terminal.",
              s=["sme", "con"], lc="move", st="new", ay="May 2026", o="P", at="Financial Administration, banks", neo=[0, "Account rails, no card."],
              mc="A terminal-free rival to card acceptance at Slovak merchants.",
              src=[["epravo.sk: QR payments, May 2026", QR]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: card security and limits, George AI on an OpenAI model, George Moneyback cashback with Dateio and fee rewards that favour mobile payments, and shared utilities for credit data and cash.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security", "blurb": "Limits, 3-D Secure, alerts.", "div": "slsp", "rev": "retail", "products": [
            P("security", "Card security & limits", "Default online limits of €300 a day on personal debit cards, card blocking and PIN in George, and planned AI alerts on unusual card payments with one-tap blocking. Visa Secure for online checks presumed ⚠.",
              s=["con"], lc="everyday", neo=[0, "Bank's own; Visa ⚠."], src=[["Debit card disclosure, Feb 2025", DEBIT], ["Startitup: George AI, Sep 2026", GAI]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "George AI", "blurb": "Ask about your money.", "div": "george", "rev": "retail", "products": [
            P("georgeai", "George AI", "A conversational assistant on an OpenAI model, for the first several thousand clients by September 2026: where the money goes, how investments perform and how products work; next come mortgage affordability, budgets, financial health checks, card-fraud alerts and voice.",
              s=["con", "inv"], lc="everyday", st="new", ay="2026", o="P", at="OpenAI", neo=[0, ""],
              mc="Spending insight and merchant data could sit behind its answers on any network.",
              src=[["Startitup: George AI, Sep 2026", GAI]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards", "blurb": "Moneyback with Dateio.", "div": "george", "rev": "retail", "products": [
            P("moneyback", "George Moneyback", "Card-linked cashback activated in George: clients pick merchant offers and get money back the next month. Launched for nearly a million clients in 2021 with Dateio of Prague; terms of July 2025 cover debit and Visa credit cards.",
              s=["con"], lc="grow", ay="2021", o="P", at="Dateio", neo=[0, "Visa cards; Dateio."],
              mc="Card-linked offers run by a local fintech, not a network.",
              src=[["Moneyback terms, Jul 2025", MB], ["Touchit: Moneyback launch", MBL]]),
            P("odmena", "Moja odmena fee rewards", "From January 2026 accounts are free for under-26s; others earn a zero fee by paying at least €450 a month by phone, watch or credit card and three regular payments, or by holding €15,000.",
              s=["con"], lc="everyday", st="new", ay="Jan 2026", neo=[0, ""], src=[["SITA: fee changes, Nov 2025", FEES26]]),
        ]},
        {"id": "3.4", "ic": "chart-column", "name": "Data & operations", "blurb": "Credit bureau, cash venture.", "div": "slsp", "rev": "alm", "products": [
            P("bureau", "Slovak Banking Credit Bureau", "A one-third stake in the register of retail credit shared by Slovak banks.",
              s=["con"], lc="borrow", o="P", neo=[0, ""], src=[["Half-year report 2026", HYR]]),
            P("monilogi", "Monilogi cash processing", "A 28% joint venture for cash processing, behind 733 ATMs including 296 deposit machines.",
              s=["con"], lc="everyday", o="P", at="Monilogi", neo=[0, ""], src=[["Half-year report 2026", HYR], ["H1 2026 results", H1PDF]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: €12.3 billion of housing loans and a quarter of Slovak retail lending, SPACE accounts and consumer loans, George investing and insurance, €7.4 billion of corporate lending with leasing and factoring, and social finance and start-up money.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Housing loans", "blurb": "€12.3bn, market leader.", "div": "slsp", "rev": "retail", "products": [
            P("mortgages", "Housing loans", "€12.3 billion (+6.0%), the core of a 24.2% share of Slovak retail lending in May 2026; refixing offers shown in George; banks run the state mortgage subsidy from 2026.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["Half-year report 2026", HYR], ["Factsheet, Apr 2026", FACT], ["Investor presentation, Q1 2026", PRES]]),
            P("pss", "Prvá stavebná sporiteľňa", "Building savings through an associate in which the bank holds 9.98% and 35% of the votes; €1.3 million dividend in May 2026.",
              s=["home"], lc="grow", o="P", neo=[0, ""], src=[["Half-year report 2026", HYR]]),
        ]},
        {"id": "4.2", "ic": "wallet", "name": "Accounts & consumer loans", "blurb": "SPACE, 28% of deposits.", "div": "slsp", "rev": "retail", "products": [
            P("accounts", "SPACE current accounts", "SPACE and SPACE Mini accounts, free for under-26s; nearly 28% of Slovak retail deposits; account fees of €35.3 million in the first half.",
              s=["con", "young"], lc="open", neo=[0, "Visa debit."], src=[["SITA: fee changes, Nov 2025", FEES26], ["Investor presentation, Q1 2026", PRES], ["Half-year report 2026", HYR]]),
            P("consumer", "Consumer loans", "Retail loans of €14.2 billion in all; consumer lending grew only 0.9% a year to March 2026, the slowest in two years.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Investor presentation, Q1 2026", PRES], ["H1 2026 results", H1REL]]),
        ]},
        {"id": "4.3", "ic": "trending-up", "name": "Investing & insurance", "blurb": "From €20 in George.", "div": "george", "rev": "retail", "products": [
            P("invest", "George investing", "From €20, more than 1,000 shares and ETFs and funds in George (Q2 2026), named best banking app for investing; fund fees of €19.1 million in the half.",
              s=["inv"], lc="grow", st="new", ay="Q2 2026", o="B", neo=[0, ""], src=[["Infographic, H1 2026", INFO], ["Half-year report 2026", HYR]]),
            P("bonds", "Government retail bonds", "More than 40% of sales of Slovak government retail bonds.",
              s=["inv"], lc="grow", neo=[0, ""], src=[["Investor presentation, Q1 2026", PRES]]),
            P("insurance", "Insurance (as agent)", "Insurance sold as an agent earned €32.0 million of commissions in the first half of 2026; insurer partner not confirmed ⚠.",
              s=["con", "home"], lc="beyond", o="P", neo=[0, ""], src=[["Half-year report 2026", HYR]]),
        ]},
        {"id": "4.4", "ic": "building", "name": "Corporates & SMEs", "blurb": "€7.4bn, leasing, factoring.", "div": "slsp", "rev": "corporates", "products": [
            P("corporate", "Corporate & SME banking", "Corporate loans with leasing and factoring of €7.4 billion (+4.0%), about 22.5% of lending to Slovak companies, four regional corporate centres; the Corporates segment earned €34.5 million in the half.",
              s=["sme", "corp"], lc="borrow", neo=[0, "Visa business debit."], src=[["Half-year report 2026", HYR], ["Investor presentation, Q1 2026", PRES], ["Factsheet, Apr 2026", FACT]]),
            P("markets", "Group Markets", "The markets segment serving clients' trading and treasury needs ⚠ scope not detailed; €11.7 million net profit in the first half of 2026.",
              s=["corp"], lc="move", neo=[0, ""], src=[["Half-year report 2026", HYR]]),
        ]},
        {"id": "4.5", "ic": "hand-coins", "name": "Social finance & start-ups", "blurb": "Housing, Seed Starter.", "div": "social", "rev": "alm", "products": [
            P("social", "SLSP Social Finance", "A 60.4% subsidiary financing social enterprises, with stakes in the affordable-housing companies Dostupný Domov and Dostupný Nájom.",
              s=["corp"], lc="beyond", o="B", neo=[0, ""], src=[["Half-year report 2026", HYR]]),
            P("seed", "SLSP Seed Starter", "The bank's start-up fund, which put €400,000 into the video platform Webout.",
              s=["corp"], lc="beyond", st="new", o="B", neo=[0, ""], src=[["Infographic, H1 2026", INFO], ["Half-year report 2026", HYR]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: George for 1.4 million people, 128 branches and four corporate centres, and Slovakia's largest ATM network.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "George", "blurb": "1.4 million users.", "div": "george", "rev": "retail", "products": [
            P("george", "George app & web", "1.4 million users, 1.16 million on the mobile app, rated 4.8 from more than 200,000 reviews; best Slovak banking app (Smart Banka 2025), Euromoney best digital bank 2026.",
              s=["con", "inv", "young"], lc="everyday", o="B", neo=[0, ""], src=[["Infographic, H1 2026", INFO], ["H1 2026 results", H1REL]]),
        ]},
        {"id": "5.2", "ic": "building-2", "name": "Branches & ATMs", "blurb": "128 branches, 733 ATMs.", "div": "slsp", "rev": "retail", "products": [
            P("branches", "Branches & corporate centres", "128 branches at 30 June 2026, down from 140 at the end of 2025, and four regional corporate centres.",
              s=["con", "home", "sme"], lc="open", st="flux", neo=[0, ""], src=[["H1 2026 results", H1PDF], ["Factsheet, Apr 2026", FACT]]),
            P("atms", "ATMs", "733 ATMs including 296 deposit machines, the largest network in Slovakia.",
              s=["con"], lc="everyday", neo=[None, "Card acceptance not stated."], src=[["H1 2026 results", H1PDF], ["Infographic, H1 2026", INFO]]),
        ]},
        {"id": "5.3", "ic": "headset", "name": "Client centre", "blurb": "0850 111 888.", "div": "slsp", "rev": "retail", "products": [
            P("contact", "Client centre", "Phone and e-mail support for retail and business clients, and the route for merchants to ask about terminals.",
              s=["con", "sme"], lc="open", neo=[0, ""], src=[["Debit card disclosure, Feb 2025", DEBIT], ["SLSP: receiving payments", ACQ]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Slovenská sporiteľňa", "blurb": "Acceptance only; issuing is Visa.", "products": [
        P("mcatslsp", "Mastercard at Slovenská sporiteľňa", "Visa has worked with the bank since 1994 and, under an exclusive agreement of July 2021, every new card carries the Visa logo; Apple Pay, virtual cards and credit cards ride on Visa. Mastercard World and Mass cards were sold until about 2019–20 ⚠. Mastercard reaches the bank's merchants only through the Global Payments joint venture, which accepts every network.",
          s=["con"], div="slsp", rev="retail", mc="The relationship this map is drawn for.",
          src=[["SITA: SLSP and Visa, Jul 2021", VISA21], ["SLSP: 1 million Visa cards, Feb 2016", VISA16], ["SLSP: receiving payments", ACQ]]),
    ]},
    {"id": "pillar-market", "name": "Slovak banking", "blurb": "Three big banks, instant rails.", "products": [
        P("market", "The Slovak market", "Slovenská sporiteľňa, VÚB and Tatra banka lead; Tatra banka moved business debit from Mastercard to Visa in 2023 while VÚB issues both. Instant payments are mandatory since October 2025, QR payments started in May 2026, and the government is consolidating the budget with a bank levy.",
          s=["con"], div="slsp", rev="alm", src=[["Investor presentation, Q1 2026", PRES], ["Tatra banka: business debit terms, 2023", TATRA], ["Podnikajte.sk: VÚB business cards, 2026", VUB], ["epravo.sk: QR payments, May 2026", QR]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
