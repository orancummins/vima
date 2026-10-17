"""Banco Santander Chile's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the Q2 2026 management commentary (approved
28 July 2026) and the 4Q 2025 management commentary (January 2026), both filed with the SEC. The parent,
Banco Santander, is a separate customer and appears here only as context. ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://www.sec.gov/Archives/edgar/data/0001027552/000102755226000098/managementcommentary2q20.htm"
Q4 = "https://www.sec.gov/Archives/edgar/data/1027552/000102755226000024/a4q25managementcommentar.htm"
CEO = "https://chocale.cl/2025/01/santander-chile-anuncia-a-andres-trautmann-como-nuevo-gerente-general/"
LATAM = "https://www.df.cl/mercados/banca-fintech/banco-santander-y-latam-pass-renuevan-por-otros-cinco-anos-su-historica"
CARDS25 = "https://chocale.cl/2025/11/adios-a-las-tarjetas-gold-y-life-latam-pass-santander-reestructura-oferta-de-tarjetas-de-credito/"
AMEX = "https://www.meganoticias.cl/nacional/495868-tarjeta-banco-santander-platinium-card-american-express-requisitos-pdp-18-08-2025.html"
WML = "https://banco.santander.cl/personas/tarjetas/viajes/detalles/worldmember-limited-santander-latam-pass"
LIFEDEB = "https://banco.santander.cl/personas/tarjetas/debito/detalles/tarjeta-de-debito-life"
LIFE20 = "https://www.biobiochile.cl/noticias/economia/tu-bolsillo/2020/08/19/todos-pueden-tener-la-nueva-cuenta-corriente-life-de-santander-no-pide-sueldo-ni-antiguedad-laboral.shtml"
PULSERA = "https://www.biobiochile.cl/noticias/economia/actualidad-economica/2020/07/31/las-2-innovaciones-presento-santander-facilitar-metodos-pago-esta-pandemia.shtml"
ECO = "https://chocale.cl/2022/01/santander-renovacion-diseno-tarjetas-credito-debito/"
GETNETCO = "https://abogados.com.ar/guerrero-olivos-asesoro-a-banco-santander-chile-en-la-estructuracion-y-constitucion-de-sociedad-operadora-de-tarjetas-de-pago-santander-getnet-chile-sa/26386"
GETNET25 = "https://www.santander.com/en/press-room/press-releases/2025/02/getnet-launches-new-features-in-chile-to-empower-retailers-through-innovative-business-opportunities"
EMOL = "https://www.emol.com/noticias/Economia/2025/12/01/1184509/actores-desafian-reinado-transbank.html"
KLAP = "https://www.latamfintech.co/articles/llega-a-chile-la-tecnologia-tap-on-phone-gracias-a-la-alianza-entre-klap-y-mastercard"
C2P = "https://chocale.cl/2024/02/click-to-pay-servicio-mastercard-reduce-pasos-compras-online/"
MCAGENT = "https://www.descubre.vc/noticia/mastercard-prueba-en-chile-pagos-aut-nomos-realizados-por-agentes-de-ia-2026-09-04"
MCDIAS = "https://chocale.cl/2026/09/thiago-dias-country-manager-de-mastercard-chile-entrevista/"
VISAAG = "https://www.intelligentcio.com/latam/2026/03/16/santander-and-visa-complete-first-agentic-commerce-pilot-across-latin-america/"
AGENTEU = "https://www.santander.com/es/sala-de-comunicacion/notas-de-prensa/2026/03/santander-y-mastercard-completan-el-primer-pago-real-ejecutado-por-un-agente-de-ia-en-europa"
GFR = "https://www.santander.com/content/dam/santander-com/en/documentos/resultados-trimestrales/2026/q2/rt-q2-2026-banco-santander-financial-report-en.pdf"
G20F = "https://www.santander.com/content/dam/santander-com/es/documentos/informacion-sobre-resultados-semestrales-y-anuales-suministrada-a-la-sec/2026/sec-2025-annual-20-f-2025-disponible-solo-en-ingles-es.pdf"
OPENAI = "https://www.cio.com/article/4038926/santander-se-apalanca-en-la-tecnologia-de-openai-para-convertirse-en-un-banco-nativo-en-ia.html"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · parent · cloud core", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Chile's largest bank by loans, with a 27% return on equity in the first half of 2026, two-thirds owned by Santander Group, a new chief executive since July 2025, the group's Gravity cloud core and a goal of 3.5 million active customers.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Ch$70 trillion, ROAE 27%.", "div": "bsc", "rev": "rc", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of Ch$70.3 trillion (US$76.3 billion), loans of Ch$41.4 trillion and deposits of Ch$32.4 trillion at 30 June 2026; net income of Ch$656 billion in the half (+19.2%), ROAE 27.2% and 31.5% in the second quarter on high inflation; efficiency 31.6%; CET1 11.1%.",
              s=["con"], neo=[0, ""], src=[["Q2 2026 management commentary", Q2]]),
            P("fy25", "2025 results", "Net income of Ch$1,053 billion in 2025 (+22.8%), ROAE 23.5%, NIM 4.0% and efficiency 36.0%; 60% paid out as dividends.",
              s=["con"], neo=[0, ""], src=[["4Q 2025 management commentary", Q4], ["Q2 2026 management commentary", Q2]]),
        ]},
        {"id": "1.2", "ic": "building-2", "name": "Ownership & listing", "blurb": "67% Santander Group.", "div": "group", "rev": "rc", "products": [
            P("ownership", "Ownership, listing & ratings", "Santander Group owns 67% and 33% floats on the Santiago Stock Exchange and as NYSE ADRs (BSAC); market value of US$15.4 billion at 30 June 2026 (+30.8% in a year); rated A2 (Moody's) and A- (S&P), stable. The holding chain was not checked ⚠.",
              s=["corp"], o="I", neo=[0, ""], src=[["Q2 2026 management commentary", Q2]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Leadership", "blurb": "Trautmann and Vergara.", "div": "bsc", "rev": "rc", "products": [
            P("leadership", "Board & management", "Andrés Trautmann, with Santander since 2007, has been chief executive and country head since 1 July 2025, succeeding Román Blanco; Rodrigo Vergara became chair in March 2026 after Claudio Melandri resigned, and the board was re-elected on 28 April 2026.",
              s=["corp"], st="new", ay="Jul 2025", neo=[0, ""], src=[["Chócale: Trautmann named CEO, Jan 2025", CEO], ["Q2 2026 management commentary", Q2]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology", "blurb": "Gravity cloud core, Plard.", "div": "group", "rev": "rc", "products": [
            P("gravity", "Gravity cloud core", "The move from mainframe to the group's Gravity cloud platform was completed in the first quarter of 2025; administrative expenses fell 9.3% in the first half of 2026, largely because of it.",
              s=["corp"], o="P", at="Santander Group", neo=[0, ""], src=[["Q2 2026 management commentary", Q2], ["4Q 2025 management commentary", Q4]]),
            P("plard", "Plard card processing", "The group's own card processor, handling more than 500 million transactions a month across Brazil, Mexico, Chile, Spain and the UK.",
              s=["con"], lc="move", o="P", at="Santander Group", neo=[0, "In-house processing."], src=[["Banco Santander Q2 2026 financial report", GFR]]),
            P("ai", "Data & AI", "No Chile-specific AI programme is disclosed ⚠; the group signed an agreement with OpenAI in August 2025 to become an 'AI-native bank'.",
              s=["corp"], st="unconf", neo=[None, "Nothing public for Chile."], src=[["CIO: Santander and OpenAI, Aug 2025", OPENAI]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & guidance", "blurb": "3.5 million active customers.", "div": "bsc", "rev": "rc", "products": [
            P("strategy", "Strategy & 2026 guidance", "A digital bank with Work/Cafés, aiming for 3.5 million active customers (2.69 million now); 2026 guidance of ROAE above 24%, NIM about 4.1% and efficiency in the low 30s, with ROAE above 20% in the long term.",
              s=["corp"], neo=[0, ""], src=[["Q2 2026 management commentary", Q2]]),
            P("esg", "Sustainability roadmap 2025–2030", "US$1.8 billion of sustainable finance by September 2025, a 2030 decarbonisation goal, DJSI and an MSCI AA rating.",
              s=["corp"], neo=[0, ""], src=[["4Q 2025 management commentary", Q4]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: a quarter of Chile's credit-card purchases on Mastercard, Visa and American Express cards, debit led by the Life account, card security with dynamic codes, Getnet acceptance at 229,000 merchants, dollar accounts and trade, and AI-agent payments being tested by Visa and Mastercard.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "24% of card purchases.", "div": "bsc", "rev": "rc", "products": [
            P("latampass", "Santander LATAM Pass credit cards", "A co-brand with LATAM Airlines for more than three decades, with more than 688,000 clients, renewed for five years in August 2025; Platinum, WorldMember and WorldMember Limited remain. Versions on Mastercard, Visa and American Express ⚠ split by tier not public.", short="LATAM Pass (Mastercard, Visa, Amex)",
              s=["traveller", "con"], lc="borrow", st="active", ay="Aug 2025", o="P", at="LATAM Airlines", neo=[1, "Mastercard, Visa and Amex versions ⚠."],
              mc="The bank's flagship card is shared between three networks.",
              src=[["DF: LATAM Pass renewal, Aug 2025", LATAM], ["Chócale: card range simplified, Nov 2025", CARDS25], ["Santander Chile: WorldMember Limited", WML]]),
            P("lifecredit", "Santander Life credit card", "The mass-market card left after the November 2025 simplification; the Life LATAM Pass card and plan closed to new customers and the Mérito Life programme ended on 31 December 2025. Network not confirmed ⚠.",
              s=["con"], lc="borrow", st="flux", ay="Nov 2025", neo=[None, "Network not confirmed ⚠."], src=[["Chócale: card range simplified, Nov 2025", CARDS25]]),
            P("amexplat", "The Platinum Card American Express", "Launched in 2025 for private-bank clients with net income of at least Ch$15 million a month: Centurion Lounges, Priority Pass and 50,000 LATAM Pass miles on joining.", short="Platinum Card (Amex)",
              s=["wealth", "traveller"], lc="borrow", st="new", ay="Aug 2025", o="P", at="American Express", neo=[0, "American Express."],
              src=[["Meganoticias: Platinum Card, Aug 2025", AMEX]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Debit & accounts", "blurb": "Life on Mastercard debit.", "div": "life", "rev": "rc", "products": [
            P("lifedebit", "Cuenta Life & Life debit", "A current account anyone can open online, with no salary requirement (August 2020), launched with a Mastercard debit card; the bank's Life debit page now shows Mastercard and Visa marks ⚠.", short="Life debit (Mastercard)",
              s=["con"], lc="open", ay="Aug 2020", o="B", neo=[1, "Launched on Mastercard; Visa mark also shown ⚠."],
              mc="Mastercard's clearest foothold in Santander Chile's mass market.",
              src=[["BioBioChile: Cuenta Life, Aug 2020", LIFE20], ["Santander Chile: Life debit card", LIFEDEB]]),
            P("debit", "Debit cards & digital debit", "Debit cards on Visa and Mastercard ⚠ for a 20.8% share of Chile's current accounts, and a digital debit card with its own number for online purchases (July 2020).",
              s=["con", "sme"], lc="everyday", ay="Jul 2020", neo=[1, "Visa and Mastercard ⚠."], src=[["BioBioChile: digital debit, Jul 2020", PULSERA], ["Q2 2026 management commentary", Q2]]),
        ]},
        {"id": "2.3", "ic": "fingerprint", "name": "Card security & wearables", "blurb": "No printed number, dynamic CVV.", "div": "bsc", "rev": "rc", "products": [
            P("ecocards", "Eco cards with dynamic CVV", "Since January 2022, vertical recycled-PVC cards with no printed number, expiry date or CVV; the CVV changes after each purchase or every 24 hours. Brands: Visa, Mastercard, American Express and Magna.",
              s=["con"], lc="everyday", ay="Jan 2022", o="B", neo=[1, "Across all its networks."], src=[["Chócale: eco cards, Jan 2022", ECO]]),
            P("pulsera", "Pulsera Chip", "A contactless wristband linked to a credit card, available only on Mastercard (July 2020) ⚠ current status.", short="Pulsera Chip (Mastercard)",
              s=["con"], lc="everyday", st="unconf", ay="Jul 2020", neo=[2, "Mastercard only."], src=[["BioBioChile: Pulsera Chip, Jul 2020", PULSERA]]),
            P("wallets", "Tokens & mobile wallets", "Group-wide: tokens managed centrally and Apple Pay and Google Pay in every country ⚠ Chile detail not checked.",
              s=["con"], lc="everyday", neo=[1, "Network tokens on each scheme ⚠."], src=[["Banco Santander 2025 Form 20-F", G20F]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Getnet acceptance", "blurb": "229,000 merchants.", "div": "getnet", "rev": "pay", "products": [
            P("getnet", "Getnet acquiring", "Set up in July 2020 to compete with Transbank; more than 287,000 POS terminals and 229,000 merchants in June 2026; second in Chilean acquiring with 18.9% of transactions (its own figure) or 25.4% (2025 survey); fees fell 15.1% in the half on price competition.", short="Getnet (all networks)",
              s=["sme"], lc="move", ay="Jul 2020", o="B", neo=[1, "Accepts every network."],
              mc="Fees under pressure: merchant data, fraud and Tap on Phone tools could help Getnet hold share.",
              src=[["Q2 2026 management commentary", Q2], ["Guerrero Olivos: Getnet Chile, Jul 2020", GETNETCO], ["Emol: acquiring market, Dec 2025", EMOL]]),
            P("smartpos", "Smart POS services", "Bill payments, Bip! transport-card and mobile top-ups on Getnet terminals, and same-day settlement into Santander accounts, weekends included (February 2025).",
              s=["sme"], lc="beyond", st="new", ay="Feb 2025", neo=[0, ""], src=[["Santander: Getnet features in Chile, Feb 2025", GETNET25]]),
            P("ecommerce", "E-commerce & host-to-host", "Online payments and host-to-host integrations that take Getnet from small businesses to larger merchants.",
              s=["sme", "corp"], lc="move", neo=[1, "Accepts every network."], src=[["4Q 2025 management commentary", Q4], ["Q2 2026 management commentary", Q2]]),
        ]},
        {"id": "2.5", "ic": "earth", "name": "Dollars & trade", "blurb": "36% of dollar accounts.", "div": "bsc", "rev": "cib", "products": [
            P("usd", "Dollar current accounts", "507,584 dollar current accounts, a 36.4% market share in May 2026, driven by online opening.",
              s=["con", "traveller"], lc="open", neo=[0, ""], src=[["Q2 2026 management commentary", Q2]]),
            P("trade", "Foreign trade & FX", "About 21% of commercial loans are in foreign currency, mostly dollars; foreign-trade lending drove the recovery in commercial loans in 2026.",
              s=["corp", "sme"], lc="move", neo=[0, ""], src=[["Q2 2026 management commentary", Q2]]),
        ]},
        {"id": "2.6", "ic": "bot", "name": "AI-agent payments", "blurb": "Visa first; Mastercard testing.", "div": "group", "rev": "rc", "products": [
            P("visaagent", "Visa Intelligent Commerce pilot", "AI agents completed a book purchase in Chile in Santander's five-market pilot with Visa (16 March 2026), led by the group's Matías Sánchez.",
              s=["con"], lc="move", st="new", ay="Mar 2026", o="P", at="Visa", neo=[0, "Visa."],
              src=[["Intelligent CIO: Santander and Visa pilot, Mar 2026", VISAAG]]),
            P("agentpay", "Mastercard Agent Pay", "Mastercard ran real agent payments with six unnamed banks in Chile (September 2026) ⚠ Santander not named; the group is already live on Agent Pay in Spain (March 2026).",
              s=["con"], lc="move", st="unconf", ay="Sep 2026", o="P", at="Mastercard", neo=[None, "Santander Chile's role not public ⚠."],
              mc="The group is live with Agent Pay in Spain and Brazil; in Chile Visa went first.",
              src=[["Descubre: Mastercard agent payments in Chile, Sep 2026", MCAGENT], ["Santander: first AI-agent payment in Europe, Mar 2026", AGENTEU]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: card security and fraud controls, Santander Rewards and LATAM Pass miles after Mérito Life ended, readiness for open finance in July 2027 and the new debt registry, and insurance and fund brokerage.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Dynamic CVV, closed accounts.", "div": "bsc", "rev": "rc", "products": [
            P("fraud", "Fraud controls", "Cards without printed numbers and a changing CVV, and unused accounts closed to cut fraud risk (2025); no Mastercard fraud tool is named ⚠.",
              s=["con", "sme"], lc="everyday", neo=[0, "The bank's own."], src=[["Chócale: eco cards, Jan 2022", ECO], ["4Q 2025 management commentary", Q4]]),
        ]},
        {"id": "3.2", "ic": "gift", "name": "Rewards & miles", "blurb": "Santander Rewards, LATAM Pass.", "div": "bsc", "rev": "rc", "products": [
            P("rewards", "Santander Rewards & LATAM Pass miles", "Miles per US dollar spent rise with the customer's Santander Rewards level (0.7, 0.84 or 1.05) ⚠; loyalty campaigns weighed on card fees in the second quarter of 2026, and Mérito Life ended in December 2025.",
              s=["traveller", "con"], lc="grow", st="flux", neo=[0, ""],
              mc="Card-linked offers and Priceless benefits could fill the gap left by Mérito Life.",
              src=[["Santander Chile: WorldMember Limited", WML], ["Q2 2026 management commentary", Q2], ["Chócale: card range simplified, Nov 2025", CARDS25]]),
        ]},
        {"id": "3.3", "ic": "plug", "name": "Open finance & credit data", "blurb": "July 2027; REDEC.", "div": "bsc", "rev": "rc", "products": [
            P("openfinance", "Open Finance System readiness", "Under the 2023 Fintec Law, the CMF's NCG 569 sets the Open Finance System for July 2027, with a pilot period and a CMF sandbox; cost-sharing is still to be defined.",
              s=["con", "sme"], lc="open", st="flux", neo=[None, "Nothing public."],
              mc="An opening for Mastercard's open-finance tools ahead of July 2027.",
              src=[["Q2 2026 management commentary", Q2]]),
            P("redec", "Consolidated Debt Registry (REDEC)", "The CMF's consent-based registry of personal debts, in force since April 2026.",
              s=["con"], lc="borrow", st="new", ay="Apr 2026", neo=[0, ""], src=[["Q2 2026 management commentary", Q2]]),
        ]},
        {"id": "3.4", "ic": "briefcase", "name": "Insurance & funds", "blurb": "Brokerage fees +16%.", "div": "private", "rev": "wmi", "products": [
            P("brokerage", "Insurance & fund brokerage", "Asset-management and insurance fees of Ch$80.6 billion in the first half of 2026 (+16.1%), with insurance brokerage up 26.6% and fund brokerage up 10%.",
              s=["wealth", "con"], lc="grow", neo=[0, ""], src=[["Q2 2026 management commentary", Q2]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: Chile's largest consumer-lending and card business, a fifth of mortgages, banking for 478,000 SMEs, corporate and investment banking, private banking and insurance, and car finance through Santander Consumer.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Mortgages", "blurb": "Ch$17.7 trillion, number two.", "div": "bsc", "rev": "rc", "products": [
            P("mortgages", "Mortgages", "Ch$17.7 trillion, a 19.5% share and second in Chile, helped by the 2025 mortgage-subsidy law.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["Q2 2026 management commentary", Q2]]),
        ]},
        {"id": "4.2", "ic": "hand-coins", "name": "Consumer lending & cards", "blurb": "Number one in consumer.", "div": "bsc", "rev": "rc", "products": [
            P("consumer", "Consumer loans & card balances", "Consumer loans of Ch$6.07 trillion, a 19.0% share and first in Chile, including Ch$2.03 trillion of card balances; first in credit-card purchases with 24.4%; card fees Ch$73.9 billion in the half (−1.6%).",
              s=["con"], lc="borrow", neo=[1, "Cards on Mastercard, Visa and Amex."],
              mc="The largest card-purchase share in Chile, with no public network split.",
              src=[["Q2 2026 management commentary", Q2]]),
        ]},
        {"id": "4.3", "ic": "briefcase-business", "name": "SMEs & business", "blurb": "478,000 SMEs.", "div": "bsc", "rev": "rc", "products": [
            P("sme", "SME banking", "477,788 SME customers (249,365 active) in June 2026; 100% digital current accounts with a debit card and Office Banking; state-guaranteed loans, leasing and factoring; 35.0% of company peso current accounts.",
              s=["sme"], lc="everyday", neo=[0, ""],
              mc="Commercial cards and payment controls are an open field.",
              src=[["Q2 2026 management commentary", Q2]]),
            P("officebanking", "Office Banking", "The transactional platform for SMEs and companies, bundled with digital business accounts.",
              s=["sme", "corp"], lc="everyday", neo=[0, ""], src=[["Q2 2026 management commentary", Q2]]),
        ]},
        {"id": "4.4", "ic": "factory", "name": "Corporate & investment banking", "blurb": "Ch$8.3 trillion of deposits.", "div": "bsc", "rev": "cib", "products": [
            P("cib", "Corporate & Investment Banking", "Loans of Ch$2.18 trillion and deposits of Ch$8.28 trillion; cash management, trade finance, treasury, market-making and M&A advisory; 18% of first-half profit.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Q2 2026 management commentary", Q2]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "Wealth & insurance", "blurb": "Santander Private Bank.", "div": "private", "rev": "wmi", "products": [
            P("wealth", "Wealth Management & Insurance", "Santander Private Bank, international investment accounts and open-architecture funds, and Santander insurance (health, life, travel, car, unemployment); loans of Ch$1.0 trillion.",
              s=["wealth"], lc="grow", neo=[0, ""], src=[["Q2 2026 management commentary", Q2]]),
        ]},
        {"id": "4.6", "ic": "gauge", "name": "Car finance", "blurb": "Santander Consumer.", "div": "consumer", "rev": "dcb", "products": [
            P("autofin", "Santander Consumer Finance", "Car and fleet finance in the Digital Consumer Bank segment: loans of Ch$1.13 trillion (+4.9% in the half) and 3% of profit.",
              s=["driver"], lc="borrow", neo=[0, ""], src=[["Q2 2026 management commentary", Q2]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the app and website for 2.25 million digital customers, 224 branches with 91 Work/Cafés, and Getnet terminals and LATAM Pass as partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "App & website", "blurb": "App NPS 72.", "div": "bsc", "rev": "rc", "products": [
            P("app", "Santander app & website", "2.25 million digital customers using the bank each month (June 2026); app NPS 72, website 70; online opening of current and dollar accounts.",
              s=["con", "sme"], lc="open", neo=[0, ""], src=[["Q2 2026 management commentary", Q2]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & Work/Café", "blurb": "224 branches, 91 Work/Cafés.", "div": "workcafe", "rev": "rc", "products": [
            P("branches", "Branches & Work/Café", "224 branches in June 2026, 91 Work/Cafés opened since 2016 and more than 40% cashless; Work/Café Expresso centres print cards on the spot.",
              s=["con"], lc="open", st="flux", neo=[0, ""], src=[["Q2 2026 management commentary", Q2]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners & service points", "blurb": "LATAM Pass, Getnet shops.", "div": "getnet", "rev": "pay", "products": [
            P("partners", "Partners & service points", "Getnet terminals that take bill payments, deposits and international transfers, account opening in some shops in about three minutes, and LATAM Airlines as the main co-brand partner.",
              s=["con", "sme", "traveller"], lc="open", o="P", at="LATAM Airlines", neo=[0, ""],
              src=[["4Q 2025 management commentary", Q4], ["DF: LATAM Pass renewal, Aug 2025", LATAM]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Santander Chile", "blurb": "One of three networks.", "products": [
        P("mcatsantanderchile", "Mastercard at Santander Chile", "Mastercard is one of three networks on Santander Chile's cards, beside Visa and American Express. It carried the Life debit card at launch (2020) and the Pulsera Chip, shares the LATAM Pass co-brand, and is accepted through Getnet. No Chile network deal is public ⚠; Visa ran the bank's first AI-agent purchase in Chile (March 2026).",
          s=["con"], div="bsc", rev="rc", mc="The relationship this map is drawn for.",
          src=[["BioBioChile: Cuenta Life, Aug 2020", LIFE20], ["Chócale: eco cards, Jan 2022", ECO], ["Intelligent CIO: Santander and Visa pilot, Mar 2026", VISAAG]]),
    ]},
    {"id": "pillar-market", "name": "Chilean payments", "blurb": "Caps, Transbank, open finance.", "products": [
        P("market", "The Chilean market", "Interchange caps since 2023 (debit 0.35%, credit 0.8%) with a further cut suspended; Transbank down to about 61% of acquiring against Getnet, Mercado Pago and Klap; 97 of every 100 in-person payments contactless; Open Finance System due July 2027.",
          s=["con"], div="bsc", rev="rc",
          src=[["Q2 2026 management commentary", Q2], ["Emol: acquiring market, Dec 2025", EMOL], ["Chócale: Mastercard Chile interview, Sep 2026", MCDIAS], ["LatamFintech: Klap and Mastercard Tap on Phone, Apr 2023", KLAP], ["Chócale: Click to Pay in Chile, Feb 2024", C2P]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
