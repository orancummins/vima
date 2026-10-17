"""Banca Transilvania's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 results (21 August 2026) and the
preliminary 2025 results (27 February 2026), both filed on the Bucharest Stock Exchange. BT's own website
blocked automated reading, so product facts come from its releases as reprinted in Romanian trade press.
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly
on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://www.bvb.ro/infocont/infocont26/TLV_20260821153439_Financial-results-30-06-2026.pdf"
FS = "https://www.bvb.ro/infocont/infocont26/TLV_20260821153505_FactSheet-30-06-2026.pdf"
FY25 = "https://m.bvb.ro/infocont/infocont26/TLV_20260227073921_Preliminary-Financial-Results-31-12-2025.pdf"
MGMT = "https://www.bvb.ro/infocont/infocont26/TLV_20260707093129_BT-Press-release-terms-of-office.pdf"
BOARD = "https://www.bancatransilvania.ro/en/news/comunicate-de-presa/cine-sunt-membrii-consiliului-de-administratie-bt-2026-2030"
CARDS8M = "https://startupcafe.ro/banca-transilvania-a-ajuns-la-peste-8-milioane-de-carduri-92411"
FORBES8M = "https://www.forbes.ro/?p=481368"
MCLAREN = "https://www.forbes.ro/banca-transilvania-si-mastercard-lanseaza-primele-carduri-din-lume-in-parteneriat-cu-echipa-mclaren-formula-1-457751"
MCLAREN26 = "https://startupcafe.ro/aproape-80-000-de-fani-ai-echipei-mclaren-mastercard-formula-1-in-bt-pay-acum-si-un-card-fizic-in-euro-mclaren-f1-team-mastercard-debit-gold-emis-de-banca-transilvania-95878"
MCLARENEXT = "https://www.capital.ro/parteneriat-extins-banca-transilvania-mclaren-mastercard-in-sezonul-2026-de-formula-1.html"
WU2015 = "https://www.atmmarketplace.com/news/multiparty-deal-to-allow-romanians-to-receive-international-remittances-at-atms"
FLYINGBLUE = "https://www.revistabiz.ro/banca-transilvania-a-emis-35-000-de-carduri-bt-visa-flying-blue/"
EUDI = "https://startupcafe.ro/bt-si-visa-anunta-realizarea-cu-succes-a-primelor-plati-pe-baza-portofelului-ue-pentru-identitatea-digitala-83593"
WEBUILD = "https://www.bancatransilvania.ro/news/en/comunicate-de-presa/visa-si-bt-aduc-la-bucuresti-in-noiembrie-adunarea-generala-a-consortiului-european-we-build"
BTPAY8 = "https://startupcafe.ro/bt-pay-la-8-ani-de-la-lansare-ecosistem-digital-cu-peste-46-milioane-de-utilizatori-93676"
APPS = "https://www.revistabiz.ro/aplicatiile-bt-pay-si-bt-go-vor-inlocui-bt24-si-neobt/"
ROPAY = "https://startupcafe.ro/ropay-si-ropay-alias-in-bt-pay-transferuri-instant-prin-cod-qr-si-numar-de-telefon-87498"
ROPAY26 = "https://www.bancatransilvania.ro/news/en/noutati/noi-functionalitati-ropay-in-aplicatia-bt-pay"
SHARE = "https://www.romania-insider.com/banca-transilvania-largest-market-share-assets-june-2026"
FITCH = "https://www.romania-insider.com/fitch-banca-transilvania-may-2026"
OTP = "https://www.thediplomat.ro/2024/12/18/otp-bank-romania-becomes-banca-transilvania-on-february-28-2025/"
SALTFEES = "https://www.salt.bank/documents/lista-taxelor-si-comisioanelor-aplicate-clientilor-utilizatori-ai-aplicatiei-Salt-Bank-persoane-fizice.pdf"
SALT400 = "https://agerpres.ro/economic/2025/02/24/salt-bank-a-ajuns-la-peste-400-000-de-clienti-in-mai-putin-de-un-an-de-la-lansare--1425067"
SALT100 = "https://businessforum.ro/finance/20240829/salt-bank-100-days-since-launch-of-first-100-romanian-neobank-672"
BTPOS = "https://www.revistabiz.ro/banca-transilvania-lanseaza-btpos-app-care-transforma-telefonul-in-pos/"
ACCEPT22 = "https://startupcafe.ro/bt-certificare-internationala-solutii-de-plata-cu-cardul-htm-17715"
STARFORTE = "https://startupcafe.ro/banca-transilvania-card-cumparaturi-star-forte-online-htm-16975"
NETOPIA = "https://www.revistabiz.ro/banca-transilvania-implementeaza-optiunea-bt-pay-la-procesatorul-de-plati-netopia/"
BLACKFRIDAY = "https://www.revistabiz.ro/record-absolut-pentru-banca-transilvania-de-black-friday-peste-11-milioane-de-tranzactii-intr-o-singura-zi/"
EMPSA = "https://empsa.org/en/news/2025-10-17-transfond-joins-empsa"
PAYPERS = "https://thepaypers.com/payments/expert-views/romania-2025-analysis-of-payments-and-ecommerce-trends"
MERCH = "https://www.romania-insider.com/romanias-digital-payments-growth-outpacing-merchant-infrastructure"
TV = "https://www.tradingview.com/symbols/BVB-TLV"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · ownership · deals", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Romania's largest bank with 22% of system assets, RON 233 billion of group assets and ROE near 22%, a Cluj-Napoca bank from 1993 with no controlling shareholder, and a run of deals ending in OTP Bank Romania.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "RON 233bn, ROE 22%.", "div": "group", "rev": "treasury", "products": [
            P("balance", "Balance sheet & earnings", "Group assets of RON 233.3 billion and bank deposits of RON 172.4 billion at 30 June 2026; group net profit of RON 2.5 billion in the half (+26.8%) and RON 4.66 billion in 2025; ROE 21.98%, capital adequacy 21.96%, NPLs 2.41%.",
              s=["con"], neo=[0, ""], src=[["H1 2026 results", H1], ["H1 2026 fact sheet", FS], ["2025 preliminary results", FY25]]),
            P("market", "Market position", "Number one in Romania with 21.98% of banking assets in 2025, ahead of BCR (13.81%), CEC (11.24%), UniCredit (10.76%), BRD (9.97%) and Raiffeisen (9.26%) ⚠ period from a secondary write-up.",
              s=["con"], neo=[0, ""], src=[["Romania Insider: market share by assets", SHARE]]),
            P("rating", "Ratings & listing", "Fitch raised BT to BBB on 18 May 2026, one notch above Romania's sovereign; listed on the Bucharest Stock Exchange as TLV, worth about RON 30–36 billion ⚠ depending on the snapshot.",
              s=["corp"], neo=[0, ""], src=[["Romania Insider: Fitch upgrade, May 2026", FITCH], ["TradingView: BVB:TLV", TV]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & owners", "blurb": "Tetik to 2030.", "div": "group", "rev": "treasury", "products": [
            P("leadership", "Board & leaders' committee", "Chairman Horia Ciorcilă (re-elected April 2026), CEO Ömer Tetik (renewed to 2030 in July 2026); deputy CEOs George Călinescu (Finance), Oana Ilaș (Retail), Leontin Toderici (Operations), Cosmin Călin (Large Corporate), Cătălin Caragea (Risk), Andrzej Dominiak (Technology) and Tiberiu Moisă (Mid-Corporate & SME).",
              s=["corp"], neo=[0, ""], src=[["BT: terms of office, Jul 2026", MGMT], ["BT: board 2026–2030", BOARD]]),
            P("owners", "Ownership", "No controlling shareholder: NN Group and its pension funds 9.29%, EBRD 5.16%, Romanian companies 44.4%, Romanian individuals 26.40%, foreign companies 13.61% (30 June 2026).",
              s=["corp"], neo=[0, ""], src=[["H1 2026 results", H1]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & deals", "blurb": "OTP Bank Romania absorbed.", "div": "group", "rev": "treasury", "products": [
            P("heritage", "Heritage", "Founded in Cluj-Napoca in 1993 by local entrepreneurs, operating from 1994; 'the bank of entrepreneurial people'. Volksbank Romania (2015) and Bancpost (2018) were absorbed earlier ⚠.",
              s=["con"], o="B", neo=[0, ""], src=[["H1 2026 results", H1], ["2025 preliminary results", FY25]]),
            P("deals", "Deals 2021–2026", "OTP Bank Romania bought for €347.5 million in 2024 and merged into BT on 28 February 2025; BRD Pensii and Microinvest bought and Victoriabank merged with BCR Chișinău in 2025; Idea::Bank Romania in 2021 ⚠.",
              s=["con", "saver"], o="A", neo=[0, ""], src=[["The Diplomat: OTP Bank Romania becomes BT", OTP], ["2025 preliminary results", FY25]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & strategy", "blurb": "Ecosystem, diaspora, digital.", "div": "bt", "rev": "treasury", "products": [
            P("tech", "Technology", "BT Pay built with Endava, with Visa and Mastercard as contributors; the Code Crafters by BT software house folded into the bank in 2026; a 13,565-strong group workforce.",
              s=["corp"], o="P", at="Endava", neo=[0, "Both schemes contributed to BT Pay."], src=[["StartupCafe: BT Pay at eight, Jan 2026", BTPAY8], ["H1 2026 results", H1]]),
            P("strategy", "Strategy", "For H2 2026: join up banking, investments, microfinance and pensions into one ecosystem, keep lending, serve the diaspora through BT Pay and help entrepreneurs expand abroad. No multi-year financial targets were found ⚠.",
              s=["corp"], st="new", neo=[0, ""], src=[["H1 2026 results", H1]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: more than 8 million cards on both Visa and Mastercard, credit on the STAR family and Visa Flying Blue, co-brands split between Mastercard's McLaren and Visa's UNTOLD, Romania's largest acceptance network, BT Pay as a wallet, and instant RoPay payments.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "8 million cards, two schemes.", "div": "bt", "rev": "retail", "products": [
            P("debitmc", "Mastercard debit cards", "Debit lines including Mastercard Mondo, Mastercard Direct and Mastercard Omnipass, part of a portfolio of more than 8 million cards (end-2025), about 70% of them enrolled in BT Pay. BT does not publish its split between Mastercard and Visa.", short="Debit (Mastercard)",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Forbes România: McLaren cards, Jul 2025", MCLAREN], ["2025 preliminary results", FY25]]),
            P("fxcards", "Currency & virtual cards", "More than 650,000 euro and dollar cards and more than 550,000 virtual cards issued straight in BT Pay in 2025.",
              s=["con", "dias"], lc="everyday", neo=[None, "Network split not disclosed."], src=[["Forbes România: 8 million cards, Jan 2026", FORBES8M]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "STAR and Flying Blue.", "div": "bt", "rev": "retail", "products": [
            P("star", "Star Forte", "BT's first credit card (2003): up to 24 interest-free instalments and points at STAR partner merchants; listed among BT's Mastercard products.", short="Star Forte (Mastercard)",
              s=["con"], lc="borrow", ay="2003", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["StartupCafe: Star Forte online, 2021", STARFORTE], ["Forbes România: McLaren cards, Jul 2025", MCLAREN]]),
            P("stargold", "Star Gold & Star Platinum", "Premium STAR credit cards for higher-income customers ⚠ network not confirmed in this research.",
              s=["con", "saver"], lc="borrow", st="unconf", neo=[None, "Network not confirmed."], src=[["StartupCafe: Star Forte online, 2021", STARFORTE]]),
            P("flyingblue", "BT Visa Flying Blue", "Air France-KLM co-brand credit card in Classic and Premium: 35,000 cards at December 2024, with purchases up about 20% a year for three years.", short="Flying Blue (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa, Air France-KLM", neo=[0, "Visa."], src=[["Revista Biz: 35,000 Flying Blue cards, Dec 2024", FLYINGBLUE]]),
            P("bizcards", "Business cards", "Mastercard Business and STAR Business Silver and Gold cards for companies, run in BT Go ⚠ STAR Business network not confirmed.",
              s=["sme"], lc="everyday", o="P", at="Mastercard", neo=[1, "Mastercard Business; STAR Business ⚠."], src=[["Forbes România: McLaren cards, Jul 2025", MCLAREN], ["StartupCafe: Star Forte online, 2021", STARFORTE]]),
        ]},
        {"id": "2.3", "ic": "gem", "name": "Co-brands", "blurb": "McLaren on Mastercard, UNTOLD on Visa.", "div": "bt", "rev": "retail", "products": [
            P("mclaren", "McLaren F1 Team Mastercard Debit & Debit Gold", "The world's first McLaren F1 cards (28 July 2025), digital in BT Pay in lei and euros, with race-weekend cashback, lounges and Priceless; nearly 80,000 activated, a physical euro Debit Gold from 6 March 2026, and the partnership extended for the 2026 season.", short="McLaren (Mastercard)",
              s=["con", "young"], lc="everyday", st="new", ay="Jul 2025", o="P", at="Mastercard, McLaren", neo=[2, "Mastercard co-brand."],
              mc="Mastercard's most visible joint programme with BT.",
              src=[["Forbes România: McLaren cards, Jul 2025", MCLAREN], ["StartupCafe: 80,000 McLaren cards, Mar 2026", MCLAREN26], ["Capital: partnership extended, 2026", MCLARENEXT]]),
            P("untold", "BT Visa UNTOLD", "Music-festival co-brand: Europe's first animated digital card with Visa (2023) and an OLED physical card (July 2025); more than 200,000 cards at end-2025.", short="UNTOLD (Visa)",
              s=["con", "young"], lc="everyday", o="P", at="Visa, UNTOLD", neo=[0, "Visa."],
              mc="The bank's largest named co-brand sits on Visa.",
              src=[["Forbes România: 8 million cards, Jan 2026", FORBES8M], ["StartupCafe: BT Pay at eight, Jan 2026", BTPAY8]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acceptance", "blurb": "177,000 POS.", "div": "bt", "rev": "sme", "products": [
            P("pos", "POS acquiring", "More than 177,000 POS terminals (end-2025), Romania's leading acceptance network; BT cited about 30% acceptance share and 43,000 merchants in 2022 ⚠ old figures.",
              s=["merch"], lc="move", neo=[1, "Accepts every network."], src=[["StartupCafe: 8 million cards, Dec 2025", CARDS8M], ["StartupCafe: card-payment certification, 2022", ACCEPT22]]),
            P("ecomm", "BTeComm", "BT's e-commerce gateway, with about 9,700 online merchants in 2022 ⚠; BT is described as Romania's main payment processor ⚠.",
              s=["merch"], lc="move", neo=[1, "Accepts every network."], src=[["StartupCafe: card-payment certification, 2022", ACCEPT22], ["Romania Insider: merchant infrastructure", MERCH]]),
            P("btpos", "BTPOS app", "Turns a merchant's Android phone into a contactless terminal (January 2022).",
              s=["merch"], lc="move", ay="Jan 2022", neo=[1, "Accepts every network."], src=[["Revista Biz: BTPOS app, Jan 2022", BTPOS]]),
        ]},
        {"id": "2.5", "ic": "wallet", "name": "BT Pay wallet", "blurb": "1 million phone payments a day.", "div": "bt", "rev": "retail", "products": [
            P("wallet", "Phone payments", "Romania's first bank wallet (2018): contactless phone payments, contactless ATM withdrawals (2019), and more than a million phone payments a day; 5.7 million unique cards enrolled in BT Pay and BT Go at end-2025.",
              s=["con"], lc="everyday", ay="2018", o="B", neo=[1, "Holds Visa and Mastercard cards."],
              mc="Tokenised cards at this scale are where Agent Pay would start.",
              src=[["StartupCafe: BT Pay at eight, Jan 2026", BTPAY8], ["2025 preliminary results", FY25]]),
            P("paywithbtpay", "Pay with BT Pay", "Checkout with BT Pay on about 30,000 websites (end-2025), including through the Netopia processor.",
              s=["con", "merch"], lc="move", st="new", ay="2024", o="P", at="Netopia", neo=[1, "Rides on the customer's card ⚠."], src=[["Forbes România: 8 million cards, Jan 2026", FORBES8M], ["Revista Biz: Pay with BT Pay at Netopia", NETOPIA]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Instant & cross-border", "blurb": "RoPay and the diaspora.", "div": "bt", "rev": "retail", "products": [
            P("ropay", "RoPay & instant payments", "Transfond's national instant payments, with RoPay (QR) and RoPay Alias (phone number) in BT Pay from October 2025, free; from January 2026 QR payments at POS and checkout, payment requests and e-commerce by phone number.",
              s=["con", "merch"], lc="move", st="new", ay="Oct 2025", o="P", at="Transfond", neo=[0, "Domestic account-to-account."],
              mc="A domestic rail that can route around cards at the till.",
              src=[["StartupCafe: RoPay in BT Pay, Oct 2025", ROPAY], ["BT: new RoPay features, Jan 2026", ROPAY26], ["EMPSA: Transfond joins, Oct 2025", EMPSA]]),
            P("btpayitalia", "BT Pay Italia", "An Italian IBAN, a digital card and instant transfers for Romanians and Italians in Italy (2025), part of a push to the diaspora.",
              s=["dias"], lc="move", st="new", neo=[None, "Card network not stated."], src=[["StartupCafe: 8 million cards, Dec 2025", CARDS8M], ["H1 2026 results", H1]]),
            P("remit", "Remittances at ATMs", "A 2015 deal with Western Union and Mastercard to pay international remittances to Maestro and Mastercard cards at BT ATMs ⚠ current status unknown.",
              s=["dias"], lc="move", ay="2015", o="P", at="Western Union, Mastercard", neo=[2, "Mastercard and Western Union ⚠."], src=[["ATM Marketplace: remittances at ATMs, 2015", WU2015]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: STAR loyalty at 40,000 merchants and scheme benefits, identity work with Visa on the EU wallet, the bank's own risk models, and the Chat BT assistant on systems that handled 11 million transactions in a day.",
    "tiles": [
        {"id": "3.1", "ic": "gift", "name": "Loyalty & benefits", "blurb": "STAR at 40,000 merchants.", "div": "bt", "rev": "retail", "products": [
            P("starloyalty", "STAR loyalty", "Points and interest-free instalments at about 40,000 partner locations (end-2025), run by BT.",
              s=["con", "merch"], lc="beyond", o="B", neo=[0, "BT's own."],
              mc="Card-linked offers could extend STAR beyond its own merchants.",
              src=[["Forbes România: 8 million cards, Jan 2026", FORBES8M]]),
            P("benefits", "Card benefits", "Priceless experiences, lounges and race-weekend cashback on the McLaren Mastercard cards; Flying Blue miles on the Visa co-brand.",
              s=["con"], lc="beyond", o="P", at="Mastercard, Visa", neo=[1, "Priceless on McLaren; miles on Visa."], src=[["Forbes România: McLaren cards, Jul 2025", MCLAREN], ["Revista Biz: 35,000 Flying Blue cards, Dec 2024", FLYINGBLUE]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Identity & authentication", "blurb": "The EU wallet with Visa.", "div": "bt", "rev": "retail", "products": [
            P("eudi", "EU Digital Identity Wallet", "With Visa, the first live payments using the EU Digital Identity Wallet (July 2025); BT is the only Romanian bank in the WE BUILD consortium, and Visa and BT host its general assembly in Bucharest on 3–4 November 2026.",
              s=["con"], lc="open", st="new", ay="Jul 2025", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa holds BT's identity seat as the EU wallet rolls out from late 2026.",
              src=[["StartupCafe: EU wallet payments, Jul 2025", EUDI], ["BT: WE BUILD in Bucharest, Jul 2026", WEBUILD]]),
            P("btpayauth", "BT Pay authentication", "BT Pay confirms about 300,000 online purchases a day and authenticates customers calling the contact centre (2023) and in branches (2025).",
              s=["con"], lc="everyday", o="B", neo=[0, "BT's own."], src=[["StartupCafe: BT Pay at eight, Jan 2026", BTPAY8]]),
        ]},
        {"id": "3.3", "ic": "shield-check", "name": "Fraud & risk", "blurb": "Cost of risk 0.63%.", "div": "bt", "rev": "treasury", "products": [
            P("fraud", "Fraud & credit risk", "BT's own risk models: NPLs at 2.41% and cost of risk at 0.63% in H1 2026. No scheme fraud or scam tool is publicly named ⚠, while instant RoPay payments grow.",
              s=["con", "sme"], lc="everyday", neo=[None, "No network tool named."],
              mc="Instant payments raise scam risk; no Mastercard fraud tool is on record here.",
              src=[["H1 2026 results", H1]]),
        ]},
        {"id": "3.4", "ic": "bot", "name": "AI, data & APIs", "blurb": "Chat BT; 11m transactions a day.", "div": "bt", "rev": "retail", "products": [
            P("chatbt", "Chat BT", "An AI virtual assistant inside BT Pay (2025), in Romanian first.",
              s=["con"], lc="everyday", st="new", ay="2025", o="B", neo=[0, ""],
              mc="An assistant with 4.6 million users is a natural home for agentic payments.",
              src=[["StartupCafe: BT Pay at eight, Jan 2026", BTPAY8]]),
            P("ops", "Processing", "A record 11 million transactions in one day on Black Friday 2025 across cards, apps, POS and ATMs; transactions up more than 17% in H1 2026.",
              s=["con", "merch"], lc="move", neo=[0, ""], src=[["Revista Biz: Black Friday record, Nov 2025", BLACKFRIDAY], ["H1 2026 results", H1]]),
            P("openbanking", "Open banking", "No public BT open-banking or account-aggregation product was found ⚠.",
              s=["sme"], lc="open", st="unconf", neo=[None, "Nothing public."], src=[["H1 2026 results", H1]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: retail accounts and loans for nearly 5 million active customers, Salt Bank for the mobile-first, banking for 600,000 companies, leasing and consumer finance, investments and pensions, and Victoriabank in Moldova.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Retail banking", "blurb": "Nearly 5m active customers.", "div": "bt", "rev": "retail", "products": [
            P("accounts", "Accounts & deposits", "Nearly 5 million active customers at end-2025 and more than 250,000 new ones in H1 2026; retail deposits of RON 118 billion.",
              s=["con"], lc="open", neo=[1, "Debit on Mastercard and Visa."], src=[["2025 preliminary results", FY25], ["H1 2026 results", H1]]),
            P("lending", "Mortgages & consumer loans", "RON 7 billion of retail loans in H1 2026 (31% housing, 67% consumer); housing loans of RON 24.9 billion at end-2025, up 29%.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["H1 2026 results", H1], ["2025 preliminary results", FY25]]),
            P("kiddo", "BT Pay Kiddo", "Accounts and cards for children and teenagers, launched 2023, with more than 180,000 users.",
              s=["young"], lc="open", ay="2023", o="B", neo=[None, "Network not stated."], src=[["StartupCafe: BT Pay at eight, Jan 2026", BTPAY8]]),
        ]},
        {"id": "4.2", "ic": "rocket", "name": "Salt Bank", "blurb": "A digital bank on Mastercard.", "div": "salt", "rev": "retail", "products": [
            P("saltbank", "Salt Bank", "BT's app-only digital bank, launched about May 2024 ⚠: more than 400,000 clients by February 2025 (about 700,000 reported later ⚠), with Mastercard Standard and Platinum 'Founders' debit cards in 19 currencies.", short="Salt Bank (Mastercard)",
              s=["young"], lc="open", st="new", ay="2024", o="B", at="Mastercard", neo=[2, "Mastercard debit."],
              mc="The group's newest bank issues only Mastercard.",
              src=[["Salt Bank fee schedule, Jan 2026", SALTFEES], ["Agerpres: 400,000 clients, Feb 2025", SALT400], ["Business Forum: 100 days, Aug 2024", SALT100]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "Micro & SME", "blurb": "600,000 companies.", "div": "bt", "rev": "sme", "products": [
            P("smebank", "Micro & SME banking", "About 600,000 company customers; Micro deposits of RON 25.0 billion and SME and Micro gross loans of RON 15.4 billion (30 June 2026); a healthcare division for doctors and clinics.",
              s=["sme"], lc="everyday", neo=[1, "Business cards partly Mastercard."],
              mc="Commercial cards and spend controls for 600,000 firms.",
              src=[["H1 2026 results", H1]]),
        ]},
        {"id": "4.4", "ic": "factory", "name": "Corporate", "blurb": "RON 17.6bn lent in H1.", "div": "bt", "rev": "corp", "products": [
            P("corporate", "Mid & Large Corporate", "RON 17.6 billion of corporate loans in H1 2026, RON 5.1 billion more than a year earlier, led by Large Corporate; lead arranger of syndicated loans in energy, automotive, telecoms and industry.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["H1 2026 results", H1], ["2025 preliminary results", FY25]]),
        ]},
        {"id": "4.5", "ic": "hand-coins", "name": "Leasing & consumer finance", "blurb": "BT Leasing, BT Direct, BT Mic.", "div": "leasing", "rev": "nbfi", "products": [
            P("leasing", "Leasing, consumer finance & microloans", "BT Leasing, BT Direct and BT Microfinanțare, with RON 12.5 billion of gross loans and leases in the segment (30 June 2026); OTP Leasing merged in December 2024.",
              s=["sme", "con"], lc="borrow", neo=[0, ""], src=[["H1 2026 results", H1], ["The Diplomat: OTP Bank Romania becomes BT", OTP]]),
        ]},
        {"id": "4.6", "ic": "trending-up", "name": "Investments & pensions", "blurb": "Funds, brokerage, BT Pensii.", "div": "invest", "rev": "treasury", "products": [
            P("invest", "BT Asset Management & BT Capital Partners", "Investment funds and stock trading, both reachable in BT Pay; asset-management fees of RON 61 million in H1 2026.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["H1 2026 results", H1], ["StartupCafe: BT Pay at eight, Jan 2026", BTPAY8]]),
            P("pensii", "BT Pensii", "Pillar 2 and Pillar 3 private pensions, bought as BRD Pensii in 2025.",
              s=["saver"], lc="grow", st="new", ay="2025", o="A", neo=[0, ""], src=[["2025 preliminary results", FY25]]),
        ]},
        {"id": "4.7", "ic": "flag", "name": "Moldova", "blurb": "Victoriabank, Microinvest.", "div": "victoriabank", "rev": "nbfi", "products": [
            P("victoriabank", "Victoriabank & Microinvest", "Victoriabank (44.63%), merged with BCR Chișinău in 2025, plus BT Leasing MD and Microinvest, Moldova's microfinance leader, bought in 2025.",
              s=["con", "sme"], lc="everyday", o="A", neo=[None, "Not researched ⚠."], src=[["H1 2026 results", H1], ["2025 preliminary results", FY25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach BT: BT Pay for 4.6 million people and BT Go for companies, about 500 branches and agencies with 2,000 ATMs, and partners from Netopia to McLaren.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "BT Pay & BT Go", "blurb": "4.6 million users.", "div": "bt", "rev": "retail", "products": [
            P("btpay", "BT Pay", "More than 4.6 million users (January 2026) and the only app for individuals since 2025: a million phone payments, 400,000 transfers and 300,000 purchase confirmations a day; mobile payments up 24% in H1 2026.",
              s=["con", "dias", "young", "saver"], lc="everyday", o="B", neo=[1, "Holds Visa and Mastercard cards."], src=[["StartupCafe: BT Pay at eight, Jan 2026", BTPAY8], ["H1 2026 results", H1]]),
            P("btgo", "BT Go", "The only app for business customers since 2025, replacing BT24 and NeoBT.",
              s=["sme", "corp"], lc="everyday", o="B", neo=[1, "Business cards partly Mastercard."], src=[["Revista Biz: BT Pay and BT Go replace BT24 and NeoBT", APPS]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "505 units, 2,000 ATMs.", "div": "bt", "rev": "retail", "products": [
            P("branches", "Branches & agencies", "42 branches and 463 agencies, 8 healthcare units, 2 private-banking agencies and a branch in Italy (30 June 2026).",
              s=["con", "sme"], lc="open", neo=[0, ""], src=[["H1 2026 results", H1]]),
            P("atms", "ATMs & self-service", "More than 2,000 ATMs and self-service machines (end-2025).",
              s=["con", "dias"], lc="everyday", neo=[1, "Takes every scheme."], src=[["StartupCafe: 8 million cards, Dec 2025", CARDS8M]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "McLaren, UNTOLD, Netopia.", "div": "bt", "rev": "retail", "products": [
            P("partners", "Partners", "McLaren (with Mastercard), UNTOLD and Air France-KLM Flying Blue (with Visa), Netopia for Pay with BT Pay, and Endava for BT Pay.",
              s=["con", "merch"], lc="beyond", o="P", neo=[1, "McLaren on Mastercard; UNTOLD and Flying Blue on Visa."], src=[["Forbes România: McLaren cards, Jul 2025", MCLAREN], ["Revista Biz: 35,000 Flying Blue cards, Dec 2024", FLYINGBLUE], ["Revista Biz: Pay with BT Pay at Netopia", NETOPIA]]),
        ]},
        {"id": "5.4", "ic": "earth", "name": "Diaspora", "blurb": "Romanians abroad.", "div": "bt", "rev": "retail", "products": [
            P("diaspora", "Onboarding abroad", "Romanians abroad open accounts in BT Pay; the diaspora is named a new source of growth in H1 2026, with a branch in Italy and BT Pay Italia.",
              s=["dias"], lc="open", st="new", neo=[None, ""], src=[["H1 2026 results", H1], ["StartupCafe: 8 million cards, Dec 2025", CARDS8M]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BT", "blurb": "Two schemes, McLaren and Salt.", "products": [
        P("mcatbt", "Mastercard at Banca Transilvania", "BT issues on both Mastercard and Visa and does not publish the split. Mastercard carries Star Forte, debit lines such as Mondo and Direct, Mastercard Business, all of Salt Bank's cards and the McLaren F1 co-brand (about 80,000 cards since July 2025). Visa carries the UNTOLD and Flying Blue co-brands and the EU Digital Identity Wallet pilot. Scheme income ('Visa, Mastercard, WU services') was RON 41.8 million in H1 2026.",
          s=["con"], div="group", rev="treasury", mc="The relationship this map is drawn for.",
          src=[["Forbes România: McLaren cards, Jul 2025", MCLAREN], ["Salt Bank fee schedule, Jan 2026", SALTFEES], ["H1 2026 results", H1]]),
    ]},
    {"id": "pillar-market", "name": "Romanian banking", "blurb": "Leader, RoPay, turnover tax.", "products": [
        P("romania", "The Romanian market", "29 banks and RON 957 billion of assets at end-2025, with BT at 22%; RoPay and instant payments growing, Revolut busy, a bank turnover tax adding about 5 points to BT's cost/income ratio, and Romania's sovereign on negative outlook.",
          s=["con"], div="group", rev="treasury", src=[["Romania Insider: market share by assets", SHARE], ["The Paypers: Romania payments 2025", PAYPERS], ["2025 preliminary results", FY25]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
