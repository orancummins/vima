"""Banco Itaú Paraguay's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the 2025 sustainability report, the 2025
Memoria y Balance and governance report, FIX SCR's ratings (April 2026), and the quarterly balance
sheets to 30 September 2026. Amounts in guaraníes (Gs); USD at the BCP's end-2025 rate. ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

DYN = "https://www.itau.com.py/Content/archivos/Dinamicos/"
REL25 = DYN + "Relatorio_de_Sustentabilidad-8584191232728122178.pdf"
FIXA = DYN + "Calificacion_de_riesgo_anual-8584251580257413430.pdf"
FIXQ = DYN + "Calificacion_de_riesgo_trimestral-8584411426184226044.pdf"
BAL26 = DYN + "Balance_Trimestral-8584096257764096739.pdf"
MEM25 = DYN + "Composicion_Accionaria-8584158265584611339.pdf"
GC25 = "https://www.itau.com.py/Content/archivos/Gobierno_Corporativo_2026.pdf"
PROFILE = "https://www.itau.com.py/Paginas/sobreitau_itauparaguay"
CARDS = "https://www.itau.com.py/Tarjetas/TarjetasdeCredito"
TARJ = "https://www.itau.com.py/Paginas/paravos_tarjetas"
DEBIT = "https://www.itau.com.py/Paginas/paravos_tarjetas_debito"
PREPAID = "https://www.itau.com.py/Paginas/paravos_tarjetas_prepagas"
CORPCARD = "https://www.itau.com.py/Paginas/paraempresas_tarjetas_empresarial"
PROCAMPO = "https://www.itau.com.py/Paginas/paraempresas_tarjetas_ganadera"
C2P = "https://www.itau.com.py/clicktopay"
APPLE = "https://www.itau.com.py/applepay"
GPAY = "https://www.itau.com.py/googlepay"
QRPIX = "https://www.itau.com.py/qrpix"
HOME = "https://www.itau.com.py/"
PIK = "https://www.pik.com.py/"
BANCARD = "https://www.bancard.com.py/"
MCAP = "https://www.mastercard.com/pe/es/news-and-trends/press/2024/november/mastercard-trae-apple-pay-a-los-consumidores-en-paraguay.html"
LPO = "https://www.lapoliticaonline.com/paraguay/economia-py/continental-cerro-el-2025-como-el-banco-con-mas-ganancia-en-medio-de-un-cierre-historico-para-el-sistema-317/"
INFON = "https://infonegocios.com.py/default/itau-tarjetas-innovando-en-la-banca-digital"
MDA = "https://www.sec.gov/Archives/edgar/data/1132597/000113259726000223/managementdiscussionanal.htm"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · parent · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Gs 40.7 trillion of assets, an AAApy rating, a 99.99% owner in Itaú Unibanco, a bank dating from Interbanco in 1978, and a strategy built on digital service and payments.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Gs 40.7 trillion; ROE about 20%.", "div": "bipy", "rev": "central", "products": [
            P("balance", "2025 results", "Assets of Gs 39.8 trillion (about USD 6.1 billion) and loans of Gs 27.1 trillion at end-2025, gross loans up 17.3%; net profit Gs 1,258.6 billion (about USD 191 million), ROAE 20.3%, NPLs 1.57%, capital ratio 19.3%. First by equity (20%), second by deposits (14.5%), third by assets and loans.",
              s=["con", "corp"], neo=[0, ""], src=[["FIX SCR annual rating, Apr 2026", FIXA], ["Sustainability report 2025", REL25]]),
            P("q3", "Third quarter 2026", "At 30 September 2026: assets Gs 40.7 trillion, non-financial deposits Gs 28.8 trillion, performing loans Gs 25.4 trillion; nine-month profit Gs 1,014.4 billion, about 9% above the same period of 2025; ROE 19.3% for the nine months. AAApy, stable, from FIX SCR (updated 6 October 2026).",
              s=["con", "corp"], st="new", neo=[0, ""], src=[["Quarterly balance sheets 2026", BAL26], ["FIX SCR update, Oct 2025", FIXQ]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Owner, board & heritage", "blurb": "Itaú Unibanco owns 99.99%.", "div": "parent", "rev": "central", "products": [
            P("owner", "Ownership & heritage", "ITB Holding Brasil Participações (Itaú Unibanco) owns 99.99688% of 2 billion shares; not listed. Incorporated 1976, operating as Interbanco from 1978, part of Unibanco from 1995 and renamed Banco Itaú Paraguay in July 2010. Parent reports it as Paraguay's largest private bank, ROE 21.5% ⚠ the parent's label.",
              s=["corp"], o="I", neo=[0, ""], src=[["Governance report 2025", GC25], ["Itaú Unibanco 2Q26 MD&A", MDA], ["Itaú Paraguay: profile", PROFILE]]),
            P("leadership", "Board & executive team", "Chair César Blaquier; general manager José Brítez; María Fernanda Carrón (risk), Antonio Vasconsellos (personal banking), Federico Arana (business banking), Raúl Luraghi (markets), Patricia Torrents (technology, operations and data), Norma Prantte (people), Bruno Geraci (finance). As at December 2025 ⚠.",
              s=["corp"], neo=[0, ""], src=[["Governance report 2025", GC25], ["Sustainability report 2025", REL25]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology & data", "blurb": "Digital first; AI inside.", "div": "bipy", "rev": "central", "products": [
            P("tech", "Technology, data & AI", "Digital transformation is the group's stated pillar: a data and analytics engine, iToken in the app, AI being put into internal processes, and Global Finance's 2025 awards for best digital bank, mobile app and open-banking APIs in Paraguay. No customer-facing AI assistant found ⚠.",
              s=["con", "corp"], neo=[0, ""], src=[["Sustainability report 2025", REL25], ["FIX SCR annual rating, Apr 2026", FIXA]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & stakes", "blurb": "Payments ecosystem for companies.", "div": "bipy", "rev": "central", "products": [
            P("strategy", "Strategy", "Four aims (customer experience, employee experience, sustainable profitability, growth); FIX reads it as growing high-income retail and SMEs, improving the app, and becoming a collections and payments ecosystem for companies. Capital increases approved in January and October 2025. No numeric targets published ⚠.",
              s=["sme", "corp"], neo=[0, ""], src=[["FIX SCR annual rating, Apr 2026", FIXA], ["Governance report 2025", GC25]]),
            P("stakes", "Bancard & other stakes", "A 9.09% stake in Bancard, the bank-owned processor behind most Paraguayan cards (100,000+ POS, 4.5 million cards processed), minority Visa shares, and a share of Caja de Valores.",
              s=["merch"], o="P", at="Bancard", neo=[0, "Bancard and Visa stakes; none in Mastercard."],
              mc="Itaú part-owns the processor that runs its cards and Visa shares; Mastercard has no such tie.",
              src=[["Memoria y Balance 2025", MEM25], ["Bancard", BANCARD]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Mastercard debit on every account, Paraguay's largest credit-card book on Visa, Mastercard and American Express, co-brands and prepaid, phone wallets and Visa-only Click to Pay, SIPAP transfers and QR Pix into Brazil, Pik acceptance, and FX and cross-border transfers.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Mastercard Debit for all.", "div": "bipy", "rev": "personal", "products": [
            P("debit", "Itaú Mastercard Debit", "The debit card for about 476,000 current and savings accounts: chip and contactless, on Infonet, Cirrus, Maestro and Mastercard ATMs and POS, with purchase protection and Mastercard Global Service.", short="Debit (Mastercard)",
              s=["con", "pb", "sme"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard Debit, Maestro and Cirrus."],
              mc="Mastercard's anchor at Itaú Paraguay: every account's card.",
              src=[["Itaú Paraguay: debit card", DEBIT], ["Sustainability report 2025", REL25]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Leader by balances, 35.6%.", "div": "bipy", "rev": "personal", "products": [
            P("credit", "Itaú credit cards", "496,360 active cards in 2025 (+6%) and Gs 9.3 trillion (about USD 1.4 billion) of spend; first by balances (35.6%) and third by number (16.2%); 21 card types on Visa, Mastercard and American Express. Card fees are 40.2% of service income. No split by network published ⚠.", short="Credit (Visa, Mastercard, Amex)",
              s=["con", "pb"], lc="borrow", o="P", at="Visa, Mastercard, Amex", neo=[1, "Split across Visa, Mastercard and Amex."],
              mc="Paraguay's largest card book by balances, with no public network split.",
              src=[["Sustainability report 2025", REL25], ["FIX SCR annual rating, Apr 2026", FIXA], ["Itaú Paraguay: credit cards", CARDS]]),
            P("premium", "Premium cards", "Visa Infinite, Mastercard Black and American Express Platinum at the top, with lounge access, travel cover and personal assistance.",
              s=["pb"], lc="beyond", o="P", at="Visa, Mastercard, Amex", neo=[1, "Mastercard Black beside Visa Infinite and Amex Platinum."],
              mc="No World Elite or World Legend tier against Visa Infinite.",
              src=[["Itaú Paraguay: credit cards", CARDS]]),
            P("amex", "American Express", "Itaú is the only American Express issuer in Paraguay: Platinum, Green and Práctica cards with Membership Rewards; FIX and the bank credit Amex exclusivity and Interventajas for its card leadership.", short="American Express (sole issuer)",
              s=["con", "pb"], lc="borrow", o="P", at="American Express", neo=[0, "American Express."],
              src=[["Sustainability report 2025", REL25], ["Itaú Paraguay: credit cards", CARDS]]),
        ]},
        {"id": "2.3", "ic": "plane", "name": "Co-brands & prepaid", "blurb": "Miles, clubs, Tigo, teens.", "div": "bipy", "rev": "personal", "products": [
            P("cobrands", "Co-brand cards", "AAdvantage (Visa or Mastercard, the customer's choice) and Centenario club cards (Visa or Mastercard); LATAM Pass, Touring (TACPY) and 24 HS IN on Visa; Tigo Itaú with Tigo points, network not stated ⚠.",
              s=["con", "pb"], lc="borrow", o="P", at="American Airlines, LATAM, Club Centenario, TACPY, Tigo", neo=[1, "AAdvantage and Centenario on either network; LATAM and Touring Visa."],
              src=[["Itaú Paraguay: credit cards", CARDS]]),
            P("prepaid", "Tarjeta Joven", "A Visa international prepaid card for 12–17-year-olds, not tied to an account.",
              s=["con"], lc="open", o="P", at="Visa", neo=[0, "Visa."], src=[["Itaú Paraguay: prepaid cards", PREPAID]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Wallets & Click to Pay", "blurb": "Apple Pay, Google Pay, Visa C2P.", "div": "bipy", "rev": "personal", "products": [
            P("wallets", "Apple Pay & Google Pay", "Cards added from the Itaú app or the wallet. The 2025 report says Visa credit and Mastercard debit cards; the bank's FAQ pages say Visa credit and debit only ⚠. Mastercard announced Apple Pay for Itaú's Mastercard cardholders on 5 November 2024 ⚠.",
              s=["con", "pb"], lc="everyday", st="new", ay="Nov 2024", o="P", at="Apple, Google", neo=[1, "Mastercard debit per the 2025 report ⚠; FAQ says Visa."],
              src=[["Sustainability report 2025", REL25], ["Itaú Paraguay: Apple Pay", APPLE], ["Itaú Paraguay: Google Pay", GPAY], ["Mastercard: Apple Pay in Paraguay, Nov 2024", MCAP]]),
            P("c2p", "Click to Pay", "Visa credit, debit and prepaid cards enrolled automatically; the bank says it is 'for now exclusively' for Visa. Launch date not stated ⚠.", short="Click to Pay (Visa only)",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="Mastercard's debit book is not in Click to Pay.",
              src=[["Itaú Paraguay: Click to Pay", C2P]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Transfers & QR", "blurb": "105 million transfers; Pix in Brazil.", "div": "bipy", "rev": "personal", "products": [
            P("transfers", "Transfers & QR payments", "Free transfers to any bank, cooperative or finance company by alias, through the BCP's SIPAP: 105 million in 2025 by more than 400,000 customers (Gs 510 trillion); digital transfers up 49% and QR payments up 19%.",
              s=["con", "sme"], lc="move", neo=[0, ""], src=[["Sustainability report 2025", REL25]]),
            P("qrpix", "QR Pix", "Pay Brazilian Pix merchants by scanning their QR in the Itaú PY app, from a guaraní account: 2% + VAT, up to R$1,000 a transaction and R$5,000 a day, invoiced through Bancard.",
              s=["con"], lc="move", o="P", at="Bancard", neo=[0, "Pix, via Bancard."], src=[["Itaú Paraguay: QR Pix", QRPIX], ["Bancard", BANCARD]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acceptance", "blurb": "Pik QR and SmartPOS.", "div": "pont", "rev": "personal", "products": [
            P("pik", "Pik", "Itaú's acceptance for shops and entrepreneurs, run by Pont S.A.: free QR or a SmartPOS (Gs 99,000 a month) taking cards, QR and wallets, at 2% + VAT on debit and 3% + VAT on credit, with daily settlement; launched about April 2023 and more than 1.2 million transactions in 2025 ⚠.",
              s=["merch", "sme"], lc="move", st="new", ay="Apr 2023", o="B", neo=[1, "Accepts every network."],
              mc="Itaú's acquiring push: room for Mastercard acceptance and risk tools.",
              src=[["Pik", PIK], ["Sustainability report 2025", REL25]]),
        ]},
        {"id": "2.7", "ic": "earth", "name": "FX & cross-border", "blurb": "47% of FX forwards.", "div": "bipy", "rev": "markets", "products": [
            P("fx", "FX & international transfers", "59,500 outward transfers by 3,500 customers in 2025 (Gs 27 trillion), plus 24% of the spot FX market and 47% of forwards, and correspondent banking from the institutional treasury.",
              s=["sme", "corp", "agro"], lc="move", neo=[0, ""], src=[["Sustainability report 2025", REL25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud monitoring and 3D Secure, Open Banking APIs for companies from June 2025, and rewards and offers, from Interventajas to the Tienda Naranja marketplace.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Monitoring, 3D Secure, iToken.", "div": "bipy", "rev": "central", "products": [
            P("fraud", "Fraud prevention", "Rules-based transaction monitoring on habits, merchant types and risky countries, blocking tools, restricted lists of phone numbers used for extortion, and a fraud-prevention committee; 450 people trained in 2025.",
              s=["con", "sme"], lc="everyday", neo=[0, "Itaú's own."],
              mc="Transfers grew 49% in 2025 with rules-based checks: scope for network fraud and scam scoring.",
              src=[["Sustainability report 2025", REL25]]),
            P("threeds", "3D Secure & iToken", "3D Secure on Visa and Mastercard credit cards and Mastercard debit cards for online purchases; iToken in the app authorises transfers.",
              s=["con"], lc="everyday", neo=[1, "3D Secure on Visa and Mastercard ⚠ provider not named."], src=[["Sustainability report 2025", REL25]]),
        ]},
        {"id": "3.2", "ic": "code-xml", "name": "Open Banking APIs", "blurb": "ISO 20022, from June 2025.", "div": "ibba", "rev": "business", "products": [
            P("openapi", "Open Banking Itaú", "APIs that let companies pull balances and statements and send supplier payments, payroll and local and international transfers from their own systems, on ISO 20022, from June 2025; Global Finance's best open-banking APIs in Paraguay.",
              s=["sme", "corp"], lc="move", st="new", ay="Jun 2025", o="B", neo=[0, ""], src=[["Sustainability report 2025", REL25]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & offers", "blurb": "Interventajas, Tienda Naranja.", "div": "pont", "rev": "personal", "products": [
            P("interventajas", "Interventajas & points", "Itaú's own points (5 USD = 1 point on business cards), alongside Membership Rewards on Amex, AAdvantage miles, LATAM Pass and Tigo points.",
              s=["con", "pb"], lc="grow", neo=[0, "Itaú's own programme."], src=[["Itaú Paraguay: credit cards", CARDS], ["Itaú Paraguay: Tarjeta Empresarial", CORPCARD]]),
            P("offers", "Discounts & promotions", "Monthly merchant discounts, travel benefits and a standing 2x1 cinema offer for Itaú cards, including Mastercard debit.",
              s=["con"], lc="grow", neo=[0, "Itaú's own."], mc="Card-linked offers could fund these promotions.", src=[["Itaú Paraguay", HOME], ["Itaú Paraguay: debit card", DEBIT]]),
            P("tiendanaranja", "Tienda Naranja", "Itaú's marketplace, run by Pont S.A., with interest-free instalments, discounts and points: more than 400 merchants, 172,000 users and 32,000 transactions in 2025, and a claimed 65% share ⚠; also a travel platform.",
              s=["con", "merch"], lc="beyond", o="B", neo=[0, ""], src=[["Sustainability report 2025", REL25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: pre-approved and car loans, 27% of housing credit, accounts and Personal Bank, SME banking and cash management, Itaú Campo for farmers and ranchers, Itaú BBA for corporates, and investments and insurance from sister companies.",
    "tiles": [
        {"id": "4.1", "ic": "hand-coins", "name": "Consumer lending", "blurb": "141,000 pre-approved loans.", "div": "bipy", "rev": "personal", "products": [
            P("preapproved", "Pre-approved loans", "141,364 pre-approved loans in 2025 (Gs 11.3 trillion), up to Gs 250 million fully digitally, through ATMs, the app, the web and branches; second in consumer credit with 21.1%.",
              s=["con", "pb"], lc="borrow", neo=[0, ""], src=[["Sustainability report 2025", REL25], ["FIX SCR annual rating, Apr 2026", FIXA]]),
            P("auto", "Mi Auto", "2,355 car loans in 2025 (Gs 343 billion) with 25 dealer agreements, and the first electric and hybrid car loans with the AFD's electromobility fund (253 loans).",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Sustainability report 2025", REL25]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Mortgages", "blurb": "27% of housing credit.", "div": "bipy", "rev": "personal", "products": [
            P("mortgage", "Mi Casa & Primera Vivienda", "3,762 home loans in 2025 (Gs 907 billion) from own funds and the AFD, including Che Róga Porã; leader in housing credit with 27.1%.",
              s=["con", "pb"], lc="borrow", o="P", at="AFD", neo=[0, ""], src=[["Sustainability report 2025", REL25], ["FIX SCR annual rating, Apr 2026", FIXA]]),
        ]},
        {"id": "4.3", "ic": "gem", "name": "Accounts & Personal Bank", "blurb": "476,000 accounts.", "div": "pbank", "rev": "personal", "products": [
            P("accounts", "Accounts & savings", "123,970 current accounts and 352,480 savings accounts at end-2025, each with a Mastercard debit card; 63,670 programmed-savings plans and 14,925 savings certificates (Gs 6.5 trillion).",
              s=["con"], lc="everyday", neo=[1, "Every account carries Mastercard debit."], src=[["Sustainability report 2025", REL25]]),
            P("pbank", "Personal Bank & Private Banking", "For income of Gs 20 million a month or USD 100,000 with the bank: seven Personal Bank agencies and a digital agency, premium cards, and private banking through the financial advisory desk.",
              s=["pb"], lc="grow", neo=[1, "Mastercard Black among the premium cards."], src=[["Sustainability report 2025", REL25]]),
        ]},
        {"id": "4.4", "ic": "briefcase-business", "name": "SMEs & cash management", "blurb": "Payroll for 214,000 people.", "div": "bipy", "rev": "personal", "products": [
            P("sme", "Empresas", "Businesses with turnover up to USD 3 million, served by executives in every branch: working-capital loans, overdrafts and cheque discounting; strategy targets SME growth.",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["Sustainability report 2025", REL25]]),
            P("cashmgmt", "Cash management", "Payroll for 4,390 companies and 214,400 employees a month, 399,000 supplier payments (USD 1.9 billion), 14.2 million direct debits, customs payments and cheque custody in 2025.",
              s=["sme", "corp"], lc="move", neo=[0, ""], src=[["Sustainability report 2025", REL25]]),
            P("corpcard", "Tarjeta Empresarial", "Cards for executives with individual limits adding up to the company line, consolidated expense reports and Interventajas points; network not stated ⚠.",
              s=["sme", "corp"], lc="move", neo=[None, "Network not stated."],
              mc="Business payment controls and virtual cards are untested ground.",
              src=[["Itaú Paraguay: Tarjeta Empresarial", CORPCARD]]),
        ]},
        {"id": "4.5", "ic": "flag", "name": "Itaú Campo", "blurb": "Soy, maize and cattle.", "div": "campo", "rev": "business", "products": [
            P("campo", "Agribusiness banking", "Farmers with 150+ hectares, ranchers with 1,000+ head and agribusinesses with USD 2 million+ turnover, in two regions and centres in the Chaco: crop and cattle cycles, machinery, land and infrastructure.",
              s=["agro"], lc="borrow", neo=[0, ""], src=[["Sustainability report 2025", REL25]]),
            P("procampo", "Tarjeta Pro Campo", "A spend-control card for agribusiness companies with individual limits and consolidated statements by category and country; its travel and car-hire insurance is Visa's, so Visa ⚠ inferred.",
              s=["agro"], lc="move", o="P", at="Visa", neo=[0, "Visa ⚠ inferred."], src=[["Itaú Paraguay: Tarjeta Pro Campo", PROCAMPO]]),
        ]},
        {"id": "4.6", "ic": "building-2", "name": "Itaú BBA", "blurb": "Corporates and the state.", "div": "ibba", "rev": "business", "products": [
            P("ibba", "Corporate & institutional banking", "Companies above USD 3 million and multinationals, plus state companies: syndicated loans, project finance, derivatives, local and international debt, trade finance, factoring (USD 67 million) and forfaiting (USD 65 million) in 2025.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Sustainability report 2025", REL25]]),
        ]},
        {"id": "4.7", "ic": "trending-up", "name": "Invest & insure", "blurb": "Sister companies since 2021.", "div": "sisters", "rev": "markets", "products": [
            P("invest", "Itaú Invest, Asset Management & Seguros", "Itaú Unibanco companies in Paraguay since 2021: a broker-dealer, a fund manager running mutual and real-estate funds, and a life insurer; the bank also sells cover from Mapfre, Sancor and others.",
              s=["pb", "corp"], lc="grow", o="A", neo=[0, ""], src=[["Sustainability report 2025", REL25], ["FIX SCR annual rating, Apr 2026", FIXA]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the Itaú PY, Personal Bank, Itaú Pagos and Itaú Negocios apps used by 429,000 individuals, 25 branches and 268 ATMs, and digital agencies on the phone and WhatsApp.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "429,000 digital individuals.", "div": "bipy", "rev": "personal", "products": [
            P("app", "Itaú PY & Personal Bank apps", "Accounts, cards, loans, transfers by alias, QR payments, bill payments, wallet enrolment and chat; more than 429,000 individual customers and 79% of business customers on digital channels in 2025. Itaú Negocios Py for companies.",
              s=["con", "pb", "sme"], lc="everyday", neo=[0, ""], src=[["Sustainability report 2025", REL25]]),
            P("itaupagos", "Itaú Pagos", "A P2P app for sending money to phone contacts without account numbers and requesting payments.",
              s=["con"], lc="move", neo=[0, ""], src=[["Sustainability report 2025", REL25]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "25 branches, 268 ATMs.", "div": "bipy", "rev": "personal", "products": [
            P("branches", "Branches, ATMs & Itaú Express", "25 full-service branches, 7 Personal Bank agencies, 6 service centres and 71 Itaú Express correspondents in 31 localities, with 268 ATMs.",
              s=["con", "agro"], lc="open", neo=[0, ""], src=[["Sustainability report 2025", REL25], ["FIX SCR annual rating, Apr 2026", FIXA]]),
        ]},
        {"id": "5.3", "ic": "headset", "name": "Remote channels", "blurb": "Digital agencies, web.", "div": "bipy", "rev": "personal", "products": [
            P("remote", "Digital agencies & online banking", "Digital agencies serving 33,000 customers by phone, email and WhatsApp; home banking and 24 horas Negocios for companies; SMS alerts.",
              s=["con", "sme", "corp"], lc="open", neo=[0, ""], src=[["Sustainability report 2025", REL25]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Itaú Paraguay", "blurb": "Debit yes; the digital edge Visa's.", "products": [
        P("mcatitaupy", "Mastercard at Itaú Paraguay", "Every debit card is Mastercard, Mastercard Black sits at the top beside Visa Infinite and Amex Platinum, AAdvantage and Centenario come on either network, and Mastercard announced Apple Pay for Itaú cardholders in November 2024 ⚠. Visa has most credit programmes, prepaid and the only Click to Pay; Amex is exclusive to Itaú. No network agreement for Paraguay is public.",
          s=["con"], div="bipy", rev="central", mc="The relationship this map is drawn for.",
          src=[["Itaú Paraguay: debit card", DEBIT], ["Itaú Paraguay: credit cards", CARDS], ["Itaú Paraguay: Click to Pay", C2P]]),
    ]},
    {"id": "pillar-market", "name": "Paraguayan banking", "blurb": "Continental, Bancard, SIPAP.", "products": [
        P("market", "The Paraguayan market", "System profit about USD 900 million in 2025, with Continental (about USD 200 million) passing Itaú (about USD 191 million) for the first time; Continental leads loans (21.2%) and deposits (17.6%). Bancard processes most cards and accepts Pix; SIPAP carries transfers.",
          s=["con"], div="bipy", rev="central", src=[["La Política Online, Feb 2026", LPO], ["FIX SCR annual rating, Apr 2026", FIXA], ["Bancard", BANCARD]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
