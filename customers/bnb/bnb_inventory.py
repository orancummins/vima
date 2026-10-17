"""Banco Nacional de Bolivia's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the 2025 annual report (212th Memoria, February 2026),
the 30 June 2026 financial statements and the tariff in force from 16 October 2026. 2025 figures in US dollars use
the old fixed rate of Bs6.86; Bolivia floated the boliviano on 29 June 2026, so 2026 figures are in bolivianos.
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

MEM = "https://www.bnb.com.bo/PortalBNB/Documentos/Memorias/Memoria%20Institucional%202025.pdf"
H1 = "https://www.bnb.com.bo/PortalBNB/Documentos/EEFF_BANCO_2026.pdf"
TARIFF = "https://www.bnb.com.bo/PortalBNB/Documentos/Tarifario/TarifarioNormaSCLIE.pdf"
CARDS = "https://www.bnb.com.bo/PortalBNB/TarjetasCredito/Index/6"
SIG = "https://www.bnb.com.bo/PortalBNB/Documentos/GuiasTarjetas/Guia-Signature.pdf"
CRIPTO = "https://www.bnb.com.bo/PortalBNB/Documentos/Cuenta_Cripto.pdf"
OPENB = "https://www.bnb.com.bo/PortalBNB/Api/OpenBanking"
HOME = "https://www.bnb.com.bo/PortalBNB/Principal/BancaPersonas"
PRESTO = "https://www.latamfintech.co/articles/paytech-presto-lanza-la-primera-tarjeta-bnpl-de-bolivia-con-soporte-visa"
WIKI = "https://en.wikipedia.org/wiki/Banco_Nacional_de_Bolivia"
CT = "https://cointelegraph.com/news/bolivia-weighs-usdt-payment-currency-amid-dollar-shortage"
LT = "https://www.lostiempos.com/actualidad/economia/20260209/utilidades-banca-continuan-ascenso-logra-cifra-record-2025"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · licence · group", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Bolivia's third-largest bank with USD5.4 billion of assets and profit up half in 2025, a licence dating from 1872, a family-chaired board, a new core and award-winning AI, and a group of leasing, funds and brokerage companies.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Third largest, ROE 14.6%.", "div": "bnb", "rev": "fin", "products": [
            P("balance", "Balance sheet & earnings 2025", "Total assets USD5,388 million, gross loans USD3,421 million (11.4% of the system, third) and deposits USD3,903 million (12.4%, third) at end-2025; net profit USD50 million, up 51.5%, ROE 14.6%; NPLs 3.4% with 158.5% cover.",
              s=["con", "corp"], neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
            P("h1", "First half 2026", "Net profit Bs216.5 million, up 52% on H1 2025; assets Bs37.7 billion, deposits Bs28.5 billion and equity Bs2.7 billion at 30 June 2026, the day after Bolivia floated the boliviano at Bs9.73 to the dollar.",
              s=["corp"], st="new", neo=[0, ""], src=[["BNB financial statements, 30 Jun 2026", H1]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Bedoya and Abastoflor.", "div": "bnb", "rev": "fin", "products": [
            P("board", "Board", "Chair Pablo Bedoya Sáenz, with Gonzalo Argandoña Fernández de Córdova and Mario Solares Sánchez as vice-chairs; Valeria Bedoya Alipaz is an alternate director. Who controls the bank's shares is not public ⚠.",
              s=["corp"], neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
            P("exec", "Executive team", "Executive Vice-President Gonzalo Abastoflor Sauma; Erick Grundner (Finance & International, from September 2025), Ramiro Argandoña (Corporate & Business), Rolando Achá (Mass Banking), Carlos Mojica (Innovation & Digital Transformation); Freddy Ramírez runs electronic payment instruments (from January 2025).",
              s=["corp"], neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & licence", "blurb": "Since 1872, rated AAA locally.", "div": "bnb", "rev": "fin", "products": [
            P("heritage", "Heritage & licence", "Incorporated on 4 March 1872 (decree of 1871), legal seat in Sucre, a multiple bank supervised by ASFI and listed on the Bolivian stock exchange; 1,972 staff at end-2025 and 2,013 in March 2026.",
              s=["con"], o="I", neo=[0, ""], src=[["BNB annual report 2025", MEM], ["Wikipedia: Banco Nacional de Bolivia", WIKI], ["BNB financial statements, 30 Jun 2026", H1]]),
            P("ratings", "Ratings", "AAA as issuer on the Bolivian scale from Moody's Local and AESA Ratings at end-2025; bonds AAA, subordinated bonds AA; top CSR grade R1+. No international-scale rating found ⚠.",
              s=["inv"], neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Core & AI", "blurb": "New core, AI award.", "div": "bnb", "rev": "fin", "products": [
            P("core", "New core banking", "First stage of a new core live in 2025, with real-time data and 24/7 availability, run by dedicated New Core design and transition managers since March 2025; data centres modernised.",
              s=["corp"], st="new", o="B", neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
            P("ai", "AI & automation", "Predictive models, AI document review and compliance checks, bots for credit checks and file validation, 41 automation projects in 2025; first place for AI innovation in FELABAN's CLAB 2025 awards.",
              s=["corp"], st="new", o="B", neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Group & strategy", "blurb": "Mobile First, Grupo BNB.", "div": "group", "rev": "fin", "products": [
            P("group", "Grupo Financiero BNB", "BNB Corporación S.A. controls BNB SAFI, BNB Valores, BNB Leasing and BNB Valores Perú; the bank holds a quarter of the card processor ATC and of a cash-in-transit firm.",
              s=["corp", "inv"], neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
            P("strategy", "Strategy", "Mobile First, a new core, AI and a growing digital-asset offer for trade; capital raised to Bs1,926 million in February 2025 and the chair warning shareholders they may need to add more. No public numeric targets ⚠.",
              s=["corp"], neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: debit cards, Visa consumer credit cards, a new Mastercard corporate range, QR Simple, transfers abroad, and USDT and the Bille wallet.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Free card, 428 ATMs.", "div": "bnb", "rev": "mass", "products": [
            P("debit", "Debit cards", "A free basic debit card with every account; free withdrawals at BNB's 428 ATMs and Bs10 at the Enlace, Redbank and UNIRED networks; Cashback on debit purchases. Network not stated; BNB ran a 'Paga con Visa y gana' campaign for debit and credit cards in 2025 ⚠.", short="Debit (Visa ⚠)",
              s=["con"], lc="everyday", at="Visa ⚠", neo=[0, "Visa ⚠ inferred from a 2025 campaign."], src=[["BNB tariff, 16 Oct 2026", TARIFF], ["BNB annual report 2025", MEM]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Consumer credit cards", "blurb": "Classic to Excellence, on Visa.", "div": "bnb", "rev": "mass", "products": [
            P("visacredit", "Visa credit cards", "Visa Classic International (limit to Bs21,000), Platinum (Bs35,000), Signature (Bs140,000, Priority Pass) and Excellence (from Bs140,000); Extra Cash advances at 14.9%; QR payments charged to the card line. Card receivables about Bs246 million at end-2025, about 1% of loans.", short="Credit cards (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              mc="The consumer book is small and wholly Visa.",
              src=[["BNB credit cards", CARDS], ["BNB Visa Signature guide", SIG], ["BNB tariff, 16 Oct 2026", TARIFF]]),
            P("bnbcash", "BNB Cash, Banca Joven Plus & SOBOCE cards", "Three more credit cards in the tariff: BNB Cash, Banca Joven Plus for young customers, and a SOBOCE-branded card with 1% QR cash advances. Network not stated ⚠.",
              s=["con"], lc="borrow", st="unconf", neo=[None, "Network not stated."], src=[["BNB tariff, 16 Oct 2026", TARIFF]]),
            P("presto", "Presto BNPL card", "Fintech Presto's buy-now-pay-later card: three interest-free or up to 12 instalments on a Bs1,400 starting line, no fee; BNB issues the cards and checks credit (May 2023).", short="Presto BNPL (Visa)",
              s=["con"], lc="borrow", ay="May 2023", o="P", at="Presto, Visa", neo=[0, "Visa."], src=[["LatamFintech: Presto BNPL card, May 2023", PRESTO], ["BNB tariff, 16 Oct 2026", TARIFF]]),
        ]},
        {"id": "2.3", "ic": "briefcase-business", "name": "Corporate cards", "blurb": "Mastercard since September 2025.", "div": "bnb", "rev": "corp", "products": [
            P("mccorp", "BNB Corporate & Corporate Black", "Mastercard corporate cards launched in September 2025, billed as the most complete corporate range in Bolivia: Corporate Black (Bs2,400 a year, USD800 a week outside hotels, food and transport) and Corporate (Bs1,800, USD200 a week), plus T&E and B2B variants.", short="Corporate cards (Mastercard)",
              s=["corp", "sme"], lc="move", st="new", ay="Sep 2025", o="P", at="Mastercard", neo=[2, "Issued on Mastercard."],
              mc="Mastercard's first visible issuing programme at BNB.",
              src=[["BNB annual report 2025", MEM], ["BNB tariff, 16 Oct 2026", TARIFF]]),
            P("cta", "BNB CTA", "A Mastercard central travel account for company travel, restricted to travel merchants, Bs1,800 a year (September 2025).", short="CTA (Mastercard)",
              s=["corp"], lc="move", st="new", ay="Sep 2025", o="P", at="Mastercard", neo=[2, "Issued on Mastercard."], src=[["BNB annual report 2025", MEM], ["BNB tariff, 16 Oct 2026", TARIFF]]),
            P("visabiz", "Visa Empresarial", "The older business credit card, Bs1,200 a year, for hotels, food and transport, with USD100 a week elsewhere and no cash advances.",
              s=["sme"], lc="move", o="P", at="Visa", neo=[0, "Visa."], src=[["BNB tariff, 16 Oct 2026", TARIFF]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "QR & acceptance", "blurb": "QR Simple, the domestic rail.", "div": "bnb", "rev": "mass", "products": [
            P("qr", "QR Simple payments", "Bolivia's interoperable QR, which BNB calls a leading means of payment: immediate QR payments since 2023, QR codes for merchants signed up by an external sales force, dynamic QR by API, and paying a credit card from the app by QR.",
              s=["con", "micro", "sme"], lc="move", o="P", at="Banco Central de Bolivia", neo=[0, "Domestic QR, no card network."],
              mc="QR takes everyday spend that cards could carry.",
              src=[["BNB annual report 2025", MEM], ["BNB personal banking", HOME]]),
        ]},
        {"id": "2.5", "ic": "earth", "name": "Cross-border & FX", "blurb": "SWIFT, remittances, a floating boliviano.", "div": "bnb", "rev": "fin", "products": [
            P("intl", "Transfers abroad, remittances & FX", "SWIFT transfers, remittance-company partners, letters of credit and currency exchange, in a year when the boliviano moved from Bs6.96 to a floating rate (Bs9.73 on 29 June 2026, Bs11.69 official on 17 October 2026).",
              s=["con", "corp"], lc="move", st="flux", o="P", at="Correspondent banks, remittance firms", neo=[0, ""],
              mc="Dollar scarcity makes cross-border payouts and FX a live need.",
              src=[["BNB financial statements, 30 Jun 2026", H1], ["BNB tariff, 16 Oct 2026", TARIFF], ["BNB personal banking", HOME]]),
        ]},
        {"id": "2.6", "ic": "coins", "name": "USDT & wallet", "blurb": "Cuenta Cripto, Bille.", "div": "bille", "rev": "mass", "products": [
            P("cripto", "Cuenta Cripto BNB", "Buy, hold and sell USDT against bolivianos in the app (50 to 10,000 USDT a day) and use USDT as a bridge for transfers abroad in US dollars, Bs50–150 per transfer (by May 2026).",
              s=["con", "corp"], lc="move", st="new", ay="2026", o="B", at="Tether (USDT)", neo=[0, "Stablecoin rail."],
              mc="A stablecoin bridge abroad where card and Move rails could compete.",
              src=[["BNB: Cuenta Cripto leaflet, May 2026", CRIPTO], ["BNB tariff, 16 Oct 2026", TARIFF]]),
            P("bille", "Bille wallet", "A mobile wallet with free transfers, cash-in and cash-out, refocused on business in 2025 with CBN and Yango and a 'Mi Negocio' QR-collection module.",
              s=["con", "micro"], lc="everyday", st="flux", o="B", at="CBN, Yango", neo=[0, ""], src=[["BNB annual report 2025", MEM], ["BNB tariff, 16 Oct 2026", TARIFF]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: app security and card controls, data analytics and an AI contact centre, open-banking APIs, Cashback and BNB Puntos, and a quarter-share in the card processor ATC.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security & card controls", "blurb": "BNB Pass, BNB Token.", "div": "bnb", "rev": "mass", "products": [
            P("security", "Security & card controls", "BNB Pass app authentication, BNB Token keys for business users, card limits for travel and online use, and blocking of unusual transactions under ASFI's electronic-payment security rules. Fraud tools are not described ⚠.",
              s=["con", "corp"], lc="everyday", neo=[None, "Nothing public."], src=[["BNB tariff, 16 Oct 2026", TARIFF]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data & AI service", "blurb": "Analytics, Carlitos.", "div": "bnb", "rev": "mass", "products": [
            P("analytics", "Data analytics", "A Data Analytics management unit using customer behaviour, income and needs to drive offers and risk.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
            P("contact", "AI contact centre & Carlitos", "AI for frequent queries in the contact centre (2025) and the Carlitos chatbot on the website and Messenger.",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, ""],
              mc="An assistant without payments yet; agentic payments are open ground.",
              src=[["BNB annual report 2025", MEM], ["BNB personal banking", HOME]]),
        ]},
        {"id": "3.3", "ic": "code-xml", "name": "Open banking & APIs", "blurb": "QR, direct debit, balances.", "div": "bnb", "rev": "corp", "products": [
            P("apis", "Open Banking APIs", "APIs for QR Simple, third-party QR, account statements and real-time balances, with documentation and a sandbox.",
              s=["sme", "corp"], lc="open", o="B", neo=[0, ""], src=[["BNB Open Banking", OPENB]]),
            P("domicil", "Direct-debit APIs", "A domiciliation platform and APIs that let billers collect by direct debit.",
              s=["corp"], lc="move", o="B", neo=[0, ""], src=[["BNB Open Banking", OPENB], ["BNB tariff, 16 Oct 2026", TARIFF]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Loyalty", "blurb": "Cashback, BNB Puntos.", "div": "bnb", "rev": "mass", "products": [
            P("cashback", "Cashback BNB", "Cash back on debit and QR purchases at more than 100 merchants for more than 84,000 customers at end-2025, with maps, proximity alerts and push notifications in the app; BNB says no other Bolivian bank pays cash back.",
              s=["con", "sme"], lc="grow", o="B", neo=[0, "Debit and QR."],
              mc="Merchant-funded offers that card-linked tools could scale.",
              src=[["BNB annual report 2025", MEM]]),
            P("puntos", "BNB Puntos & Pago Inteligente", "Points per dollar on BNB credit cards, redeemable for bills, card payments, cash and goods; Pago Inteligente discounts on annual fees at schools, universities, insurers and clubs.",
              s=["con"], lc="grow", o="B", neo=[0, "Visa cards."], src=[["BNB credit cards", CARDS], ["BNB annual report 2025", MEM]]),
        ]},
        {"id": "3.5", "ic": "network", "name": "Card processing", "blurb": "25% of ATC.", "div": "group", "rev": "fin", "products": [
            P("atc", "ATC stake", "24.998% of Administradora de Tarjetas de Crédito (ATC), the bank-owned card processor whose helpline BNB gives cardholders; ATC earned Bs40.8 million in 2025. ATC serving both Visa and Mastercard is not confirmed here ⚠.",
              s=["corp"], lc="move", o="P", at="ATC", neo=[1, "Processor for both networks ⚠."], src=[["BNB annual report 2025", MEM], ["BNB personal banking", HOME]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: mortgages (38% of loans), consumer and car loans, corporate lending (the fastest growing), SME and microcredit, deposits (12.4% of Bolivia's), and leasing, funds and brokerage from the group.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Homes & consumer loans", "blurb": "USD1.3bn of mortgages.", "div": "bnb", "rev": "mass", "products": [
            P("mortgage", "Mortgages", "USD1,315 million, 38.4% of loans; social-housing loans up to 30 years with 20% down.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
            P("consumer", "Consumer & car loans", "Consumer loans of USD281 million, with 'Súper Consumo' prize campaigns (February and October 2025) and 48-hour disbursement for payroll clients; car finance through exclusive dealer deals and more than 350 activations.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Corporate & business", "blurb": "USD1.1bn, growing fastest.", "div": "bnb", "rev": "corp", "products": [
            P("corporate", "Corporate & business lending", "Corporate loans of USD1,094 million, 32% of the book and up USD168 million in 2025, the fastest-growing line; named best corporate bank by Bolivian Business (December 2025).",
              s=["corp"], lc="borrow", neo=[0, ""],
              mc="The customers the new Mastercard corporate cards are for.",
              src=[["BNB annual report 2025", MEM]]),
            P("trade", "Guarantees & trade finance", "Bank guarantees issued digitally, letters of credit, documentary collections and standby letters for importers and exporters.",
              s=["corp"], lc="beyond", neo=[0, ""], src=[["BNB annual report 2025", MEM], ["BNB tariff, 16 Oct 2026", TARIFF]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "SME & microcredit", "blurb": "USD730m to small firms.", "div": "bnb", "rev": "micro", "products": [
            P("sme", "SME & microcredit", "SME loans of USD494 million and microcredit of USD236 million, with supply-chain finance for distributors and suppliers and the FOCREMI microenterprise fund; productive and social-housing loans are 60.2% of the book.",
              s=["sme", "micro"], lc="borrow", neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
        ]},
        {"id": "4.4", "ic": "wallet", "name": "Deposits & savings", "blurb": "12.4% of Bolivia's deposits.", "div": "bnb", "rev": "mass", "products": [
            P("deposits", "Deposits & term deposits", "USD3,903 million of deposits at end-2025, 89.8% in bolivianos and 44% in term deposits, a 12.4% share (third); term deposits can be opened fully online in the app.",
              s=["inv", "con"], lc="grow", neo=[0, ""], src=[["BNB annual report 2025", MEM], ["BNB personal banking", HOME]]),
            P("savings", "Savings accounts", "Accounts for young people (Banca Joven), seniors (Banca Senior), Banca Activa and a digital savings account.",
              s=["con"], lc="open", neo=[0, ""], src=[["BNB tariff, 16 Oct 2026", TARIFF]]),
        ]},
        {"id": "4.5", "ic": "chart-candlestick", "name": "Leasing, funds & brokerage", "blurb": "The group companies.", "div": "group", "rev": "fin", "products": [
            P("leasing", "BNB Leasing", "Leasing and leaseback for farm machinery, construction and medical equipment, offices and vehicles (founded 2009).",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["Wikipedia: Banco Nacional de Bolivia", WIKI], ["BNB annual report 2025", MEM]]),
            P("safi", "BNB SAFI funds", "Investment funds, bought from the app with 'QR SAFI' since 2025.",
              s=["inv"], lc="grow", st="new", neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
            P("valores", "BNB Valores (Bolivia & Peru)", "Stockbroking in Bolivia (BNB Valores) and Peru (BNB Valores Perú), which also placed BNB Leasing bonds.",
              s=["inv", "corp"], lc="grow", neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
            P("insurance", "Bancassurance", "Credit-life, unemployment, car and multi-risk policies sold through the bank, with the 2026–2029 credit-life tender awarded in 2026.",
              s=["home", "con"], lc="beyond", neo=[0, ""], src=[["BNB personal banking", HOME]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach BNB: the BNB Móvil app for 83% of transactions, online banking for companies, and 663 service points with partners from Presto to Yango.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "BNB Móvil", "blurb": "83% of transactions.", "div": "bnb", "rev": "mass", "products": [
            P("app", "BNB Móvil", "More than 155 million digital transactions in 2025 and 97% of operations outside branches, 83% of them in the app, rebuilt in 2025.",
              s=["con", "micro"], lc="everyday", o="B", neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Online banking for firms", "blurb": "BNB Net+, Móvil Empresas.", "div": "bnb", "rev": "corp", "products": [
            P("net", "BNB Net+ & BNB Móvil Empresas", "Online and mobile banking for companies, with salary payment, supplier payments, MT940 statements and Video Banca.",
              s=["sme", "corp"], lc="everyday", o="B", neo=[0, ""], src=[["BNB annual report 2025", MEM], ["BNB tariff, 16 Oct 2026", TARIFF]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & partners", "blurb": "663 points, 428 ATMs.", "div": "bnb", "rev": "mass", "products": [
            P("branches", "Branches, ATMs & agents", "663 service points in all nine departments at end-2025: 10 branches, 57 agencies, 13 BNB Express, 428 ATMs and 135 non-bank agents; agencies being refitted.",
              s=["con", "micro"], lc="everyday", neo=[0, ""], src=[["BNB annual report 2025", MEM]]),
            P("partners", "Partners & education", "Presto, CBN and Yango, car dealers, Cashback merchants and remittance firms; 'Aprendiendo con el BNB' financial education in schools, a bus and SME workshops.",
              s=["con", "sme"], lc="open", o="P", at="Presto, CBN, Yango", neo=[0, ""], src=[["BNB annual report 2025", MEM], ["LatamFintech: Presto BNPL card, May 2023", PRESTO]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BNB", "blurb": "Company cards; Visa elsewhere.", "products": [
        P("mcatbnb", "Mastercard at BNB", "BNB's consumer credit cards, Visa Empresarial and the Presto card are Visa, and debit probably is too ⚠. Mastercard came in through the company door: Corporate Black, Corporate, T&E, B2B and CTA cards launched in September 2025 and still in the October 2026 tariff. QR Simple, Bille and USDT move money without any network.",
          s=["corp"], div="bnb", rev="corp", mc="The relationship this map is drawn for.",
          src=[["BNB annual report 2025", MEM], ["BNB tariff, 16 Oct 2026", TARIFF]]),
    ]},
    {"id": "pillar-market", "name": "Bolivian banking", "blurb": "Float, QR, stablecoins.", "products": [
        P("market", "The Bolivian market", "Record bank profits of Bs3,827 million in 2025; a new government; the boliviano floated in June 2026; credit quotas and rate caps under Law 393; fintech rules (May 2025); the crypto ban lifted in 2024, USDT under study as a currency and Bolivia on the FATF grey list.",
          s=["corp"], div="bnb", rev="fin", src=[["Los Tiempos: bank profits 2025, Feb 2026", LT], ["Cointelegraph: Bolivia weighs USDT, Jul 2026", CT], ["BNB financial statements, 30 Jun 2026", H1]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
