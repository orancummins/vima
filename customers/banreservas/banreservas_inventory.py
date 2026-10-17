"""Banreservas' layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the Memoria Institucional 2025 (the bilingual annual
report with the 2025 accounts) and the live card catalogue on banreservas.com. No 2026 half-year report was found;
2026 figures come from the Dominican press. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's
own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

MEM = "https://memoriahistorica.senadord.gob.do/bitstreams/db79673f-3199-4075-8cbe-0ea91b58ab0c/download"
HOME = "https://www.banreservas.com/"
CARDS = "https://www.banreservas.com/personal/tarjetas/"
DEBIT = "https://www.banreservas.com/personal/tarjetas/mastercard-debito-standard/"
BLACK = "https://www.banreservas.com/personal/tarjetas/mastercard-black-banreservas/"
INFINITE = "https://www.banreservas.com/personal/tarjetas/visa-infinite/"
UNIVERSE = "https://www.banreservas.com/personal/tarjetas/visa-platinum-universe/"
SER = "https://www.banreservas.com/personal/tarjetas/tarjeta-de-credito-visa-ser-banreservas/"
PRESERVA = "https://www.banreservas.com/personal/tarjetas/tarjeta-de-credito-preserva/"
CREDIMAS = "https://www.banreservas.com/personal/tarjetas/credimas-banreservas/"
MCCOM = "https://www.banreservas.com/pyme/tarjetas/mastercard-comercial-banreservas/"
MCCOMNEWS = "https://revistamercado.do/money-invest/daily-news/banreservas-lanza-junto-a-mastercard-nueva-tarjeta-comercial-para-el-sector-empresarial/"
MIO22 = "https://eldinero.com.do/213276/banreservas-y-mio-lanzan-primera-cuenta-de-pago-electronico-bancaria-en-republica-dominicana/"
MIOMC = "https://diariolibre.com/actualidad/contenido-patrocinado/2025/09/10/mio-banreservas-lanza-una-pieza-clave-su-credencial-mastercard/3231868"
CARDNET = "https://eldinero.com.do/15645/pagos-con-tarjetas-de-credito-y-debito-en-republica-dominicana/"
SGPI = "https://eldinero.com.do/378530/el-2027-marcara-el-inicio-del-fin-de-los-pagos-en-efectivo-en-republica-dominicana/"
APPOINT = "https://eldinero.com.do/333876/abinader-designa-a-leonardo-aguilera-como-presidente-ejecutivo-del-banreservas/"
D100 = "https://eldinero.com.do/344820/leonardo-aguilera-destaca-impulso-a-sectores-productivos-en-sus-primeros-100-dias-en-banreservas/"
FITUR26 = "https://eldinero.com.do/351380/banreservas-lidera-en-fitur-2026-con-acuerdos-de-inversion-superiores-a-us6500-millones/"
SEP26 = "https://eldinero.com.do/?p=379793"
SBTYPES = "https://eldinero.com.do/380711/cuantos-tipos-de-tarjetas-de-credito-ofrece-la-banca-dominicana/"
SBCARDS = "https://eldinero.com.do/339909/cual-es-el-banco-que-mas-tarjetas-de-credito-emite-en-republica-dominicana/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "state bank · balance sheet · systems", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: the Dominican Republic's largest bank, wholly owned by the state since 1941, with RD$1.28 trillion of assets, a third of the system's loans, a new executive president and a technology base that carries 400 million transactions a year.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "35% of bank assets, ROE 21%.", "div": "br", "rev": "central", "products": [
            P("balance", "Balance sheet & earnings", "Assets of RD$1,281.9 billion at the end of 2025 (35.2% of multiple-bank assets, the only Dominican bank above a trillion pesos), gross loans of RD$628.1 billion (31% share), deposits of RD$1,045.9 billion and net profit of RD$25.45 billion, down 7.7%; ROE 20.8%, solvency 19.85%, NPLs 1.29%. Assets were RD$1,352.8 billion at September 2025; no 2026 half-year report was found ⚠.",
              s=["con"], neo=[0, ""], src=[["Memoria Institucional 2025", MEM], ["elDinero: first 100 days, Nov 2025", D100]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "State-owned; Aguilera since 2025.", "div": "br", "rev": "central", "products": [
            P("governance", "State ownership & governance", "Wholly owned by the Dominican state under Organic Law 13-24 (April 2024). The board is chaired ex officio by the Minister of Finance and Economy, Magín Díaz, with Jean Antonio Haché as independent vice-chair; Moody's raised deposits to Ba2 in 2025 and local agencies rate it AAA ⚠.",
              s=["corp"], o="I", neo=[0, ""], src=[["Memoria Institucional 2025", MEM]]),
            P("leadership", "Executive President & team", "Leonardo Aguilera Batista, named by decree on 17 August 2025 in place of Samuel Pereyra, formerly head of the state refiner Refidomsa; senior executive vice-presidents Alieska Díaz (administration), Ysidro García (business) and Ana Elizabeth Pou (people, technology and operations).",
              s=["corp"], st="new", ay="Aug 2025", neo=[0, ""], src=[["elDinero: Aguilera appointed, Aug 2025", APPOINT], ["Memoria Institucional 2025", MEM]]),
            P("heritage", "Heritage & standing", "Founded in 1941, more than 84 years of service; 686th in The Banker's Top 1000, first in the Superintendency of Banks' 2025 financial-inclusion ranking (89.4), and named best bank in the country by Global Finance.",
              s=["con"], o="I", neo=[0, ""], src=[["Memoria Institucional 2025", MEM]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology", "blurb": "400m transactions, 88% digital.", "div": "br", "rev": "central", "products": [
            P("tech", "Core systems & operations", "About 400 million transactions a year for 8 million customers, an 88.3% digital share, 1,774 servers and more than 300 critical applications; new cloud HR and accounting cores, biometrics in branches and an incident repair time cut from 4.5 to 2.8 hours in 2025.",
              s=["corp"], neo=[0, ""], src=[["Memoria Institucional 2025", MEM]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy", "blurb": "Productive credit and inclusion.", "div": "br", "rev": "central", "products": [
            P("strategy", "Strategy", "No numeric multi-year targets are published ⚠. The 2025 report names productive credit (tourism, construction, SMEs, housing, rice), financial inclusion, digital transformation and governance; the next digital priorities are AI and big data for personalised offers, open banking, cybersecurity and mobile banking. More than RD$44 billion went to business clients by September 2026.",
              s=["corp", "sme"], neo=[0, ""], src=[["Memoria Institucional 2025", MEM], ["elDinero: RD$7bn for productive sectors, Sep 2026", SEP26]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Mastercard debit for 3.8 million cards, credit on both Visa and Mastercard, commercial cards led by Visa with a new Mastercard card, the MIO e-wallet and Apple and Google Pay, CardNet acceptance, the central bank's instant payments, and US$1.6 billion of remittances and government grants.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "3.8m Mastercard debit cards.", "div": "br", "rev": "personal", "products": [
            P("debit", "Mastercard debit: Standard, Platinum & dollars", "3,846,212 active debit cards at December 2025, 47.3% of the Dominican market, all on Mastercard in the live catalogue; 128.8 million debit purchases at the point of sale in 2025 (up 27%), with Puntos Banreservas and Mastercard Global Service. A Visa Electron licence remains in the accounts ⚠.", short="Debit (Mastercard)",
              s=["con", "incl"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard debit."],
              mc="Mastercard's anchor at the bank: almost half the country's debit cards.",
              src=[["Banreservas: Mastercard Débito Standard", DEBIT], ["Memoria Institucional 2025", MEM]]),
            P("debitbiz", "Mastercard Débito Negocios", "A Mastercard debit card for business accounts, sold to SMEs alongside the personal range.",
              s=["sme"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard debit."], src=[["Banreservas: home page card catalogue", HOME]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Consumer credit cards", "blurb": "1.47m cards on Visa and Mastercard.", "div": "br", "rev": "personal", "products": [
            P("credit", "Visa & Mastercard credit: Classic/Standard, Gold, Platinum", "1.467 million active credit cards (33.4% of the market) and a RD$42.9 billion book at December 2025, with 363,069 issued in the year; most tiers come in both Visa and Mastercard and the split by network is not published ⚠. Banreservas has the most cards in the system but a lower average balance than Banco Popular.", short="Credit (Visa & Mastercard)",
              s=["con"], lc="borrow", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard tiers."],
              mc="A dual-brand book: each card issued is a choice between networks.",
              src=[["Banreservas: personal cards", CARDS], ["Memoria Institucional 2025", MEM], ["elDinero: cards by bank, Oct 2025", SBCARDS]]),
            P("premium", "Visa Infinite, Visa Platinum Universe & Mastercard Black", "The top tier: Visa Infinite (launched about 2014 ⚠) and Platinum Universe with Priority Pass, and Mastercard Black with LoungeKey and Before Boarding lounges at Las Américas and Cibao; the Black ámbar version is among the costliest cards in the market.",
              s=["pref"], lc="borrow", o="P", at="Visa, Mastercard", neo=[1, "Visa Infinite; Mastercard Black."],
              src=[["Banreservas: Mastercard Black", BLACK], ["Banreservas: Visa Infinite", INFINITE], ["Banreservas: Visa Platinum Universe", UNIVERSE], ["elDinero: card products, Sep 2026", SBTYPES]]),
            P("ser", "Visa SER", "A lower-rate credit card for lower-income customers (35% for public payroll clients, 40% private payroll, 45% savers), with cashback on basic-needs categories and Apple Pay and Google Pay.",
              s=["incl"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Banreservas: Visa SER", SER]]),
            P("preserva", "Preserva", "A credit-rebuilding card for people with damaged credit scores: limits up to RD$15,000, no cash withdrawals, and a compulsory workshop; 1,513 people trained in 42 workshops in 2025.",
              s=["incl"], lc="borrow", neo=[None, "Network not stated."], src=[["Banreservas: Preserva", PRESERVA], ["Memoria Institucional 2025", MEM]]),
            P("credimas", "Credimás instalments", "An automatic extra credit line on Banreservas credit cards for purchases or cash in fixed instalments of 2 to 48 months, without using the card limit.",
              s=["con"], lc="borrow", neo=[1, "Rides on the client's Visa or Mastercard."], src=[["Banreservas: Credimás", CREDIMAS]]),
        ]},
        {"id": "2.3", "ic": "briefcase-business", "name": "Commercial cards", "blurb": "Visa-led; Mastercard Comercial new.", "div": "br", "rev": "corporate", "products": [
            P("mccomercial", "Mastercard Comercial Banreservas", "A commercial credit card launched on 5 October 2026 in Santiago by Leonardo Aguilera and Mastercard's country manager Tomás Alonso, for SMEs and corporates: Credimás, Easy Savings rebates, Entrepreneur's Odyssey, a free year of My Cyber Risk, LinkedIn Premium rebates and a tactile notch.", short="Mastercard Comercial",
              s=["sme", "corp"], lc="borrow", st="new", ay="Oct 2026", o="P", at="Mastercard", neo=[2, "Mastercard, with Mastercard's own SME services."],
              mc="Mastercard's first commercial card at the bank, against a Visa-held corporate book.",
              src=[["Revista Mercado: Mastercard Comercial, Oct 2026", MCCOMNEWS], ["Banreservas: Mastercard Comercial", MCCOM]]),
            P("visabiz", "Visa Corporativa, Empresarial & Negocios", "Visa credit cards for corporates, companies and small businesses; SME 'Business/Corporate Visa' balances were RD$5,994 million at November 2025.",
              s=["sme", "corp"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Memoria Institucional 2025", MEM], ["Banreservas: home page card catalogue", HOME]]),
            P("fleet", "Visa Flotilla", "Fleet cards for businesses, government bodies and individuals, on Visa.",
              s=["corp"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              mc="Fleet is uncontested ground for Mastercard here.",
              src=[["Banreservas: home page card catalogue", HOME]]),
        ]},
        {"id": "2.4", "ic": "wallet", "name": "MIO & digital wallets", "blurb": "30m MIO transactions.", "div": "mio", "rev": "personal", "products": [
            P("mio", "MIO Banreservas Billetera", "An electronic payment account with the fintech MIO (November 2022): biometric sign-up, a free card and 30.1 million wallet transactions in 2025 (up 160%). Launched on Visa; new clients have been offered a Mastercard credential since mid-2025.", short="MIO (Visa & Mastercard)",
              s=["incl", "con"], lc="open", st="flux", ay="Nov 2022", o="P", at="MIO", neo=[1, "Visa from 2022; Mastercard for new clients from 2025."],
              mc="Mastercard won the e-wallet's new issuance in 2025.",
              src=[["elDinero: MIO launch, Nov 2022", MIO22], ["Diario Libre: MIO Mastercard credential, Sep 2025", MIOMC], ["Memoria Institucional 2025", MEM]]),
            P("wallets", "Banreservas Wallet, Apple Pay & Google Pay", "The in-app wallet reached Android in February 2025; more than 700,000 cards were added to Apple Pay and Google Pay in the year, 540,000 of them in Google Pay.",
              s=["con"], lc="everyday", st="new", ay="Feb 2025", o="P", at="Apple, Google", neo=[1, "Tokens on both networks ⚠."], src=[["Memoria Institucional 2025", MEM]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "Merchants via CardNet.", "div": "br", "rev": "personal", "products": [
            P("cardnet", "CardNet merchant acquiring", "Merchants are signed through CardNet, the country's largest payments processor, which also runs the ATH ATM network and the national ACH; banks including Banreservas are its main shareholders ⚠ stake not confirmed. The bank has its own CardNet and merchant-onboarding teams.",
              s=["sme"], lc="move", o="P", at="CardNet", neo=[1, "Accepts every network."], src=[["elDinero: card payments in the DR", CARDNET], ["Memoria Institucional 2025", MEM]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Transfers & instant payments", "blurb": "New central-bank rails in 2027.", "div": "br", "rev": "personal", "products": [
            P("instant", "Transfers & instant payments", "Transfers in TuBanco and the app over the central bank's Pagos al Instante (on its RTGS since 2014). The central bank's new instant-payments system, built by CMA Small Systems, is due in the first half of 2027 with aliases, 24/7 settlement and QR merchant payments in a second phase; Banreservas backed it.",
              s=["con", "sme"], lc="move", st="flux", o="P", at="Banco Central", neo=[0, "Central-bank rails."],
              mc="QR instant payments from 2027 will compete with debit at the till.",
              src=[["elDinero: instant payments in 2027, Sep 2026", SGPI]]),
        ]},
        {"id": "2.7", "ic": "send", "name": "Remittances & grants", "blurb": "US$1.6bn in; RD$21.8bn out.", "div": "br", "rev": "gov", "products": [
            P("remit", "Remittances", "6.1 million transfers worth US$1,646.95 million received in 2025 (up 49%), 94% paid straight into savings accounts; home delivery and loans for remittance families launched in the year.",
              s=["dias", "incl"], lc="move", o="P", neo=[0, ""],
              mc="A large inbound flow paid into accounts, not cards.",
              src=[["Memoria Institucional 2025", MEM]]),
            P("remesasapp", "Remesas Reservas app", "More than 33,000 transfers in 2025 (up 50%), 79% from the United States and 21% from Europe.",
              s=["dias"], lc="move", neo=[0, ""], src=[["Memoria Institucional 2025", MEM]]),
            P("govpay", "Government grants", "Seventeen monthly social subsidies for Supérate and ADESS worth RD$21.8 billion in 2025, Bono Navidad for 2.2 million people and a Mother's Bonus for a million mothers.",
              s=["incl"], lc="move", o="P", at="Supérate, ADESS", neo=[None, "Card network for subsidies not stated."], src=[["Memoria Institucional 2025", MEM]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: in-house cybersecurity and digital tokens, the Alma assistant and 15 bots, award-winning APIs and cash management, and Puntos Banreservas with network-funded promotions.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security & fraud", "blurb": "Own SOC, digital token.", "div": "br", "rev": "central", "products": [
            P("cyber", "Cybersecurity", "A Vice Presidency of Cybersecurity with a security operations centre covering the bank and its subsidiaries; named the country's safest bank by Global Finance in 2025. No fraud vendor is named ⚠.",
              s=["con", "corp"], lc="everyday", neo=[0, "Banreservas' own."],
              mc="Fast growth in tokens and app payments with no named fraud partner.",
              src=[["Memoria Institucional 2025", MEM]]),
            P("token", "Digital token & card authentication", "A digital token for the app, now also in the phone banking line (2025), and online card authentication on Banreservas cards.",
              s=["con"], lc="everyday", st="new", neo=[0, ""], src=[["Memoria Institucional 2025", MEM], ["Banreservas: Credimás", CREDIMAS]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & automation", "blurb": "Alma and 15 bots.", "div": "br", "rev": "central", "products": [
            P("alma", "Alma virtual assistant", "Takes claims, pre-qualifies fair applicants and tracks card and loan applications; AI routing added in 2025, users up 112%, 11,300 inquiries and 70% handled automatically.",
              s=["con"], lc="everyday", st="new", neo=[0, ""],
              mc="An AI front door with no agentic payments yet.",
              src=[["Memoria Institucional 2025", MEM]]),
            P("automation", "AI & bots in operations", "AI contract analysis (67% faster), 15 bots saving RD$38 million and the work of 85 people, and statement processing cut from four days to 40 minutes.",
              s=["corp"], lc="beyond", neo=[0, ""], src=[["Memoria Institucional 2025", MEM]]),
        ]},
        {"id": "3.3", "ic": "code-xml", "name": "APIs & cash management", "blurb": "Best open-banking APIs award.", "div": "br", "rev": "corporate", "products": [
            P("apis", "Open-banking APIs", "Named best open-banking APIs in the Dominican Republic in 2025; no public developer portal or product details were found ⚠.",
              s=["corp", "sme"], lc="open", neo=[0, ""], src=[["Memoria Institucional 2025", MEM]]),
            P("cashmgmt", "Cash management", "Referenced collections for 71 billers (17.9 million payments, RD$291 billion), 205 automated deposit vaults, cash in transit, escrow accounts and Swift gpi tracking in the business app.",
              s=["corp", "sme"], lc="move", neo=[0, ""], src=[["Memoria Institucional 2025", MEM]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Loyalty & offers", "blurb": "Puntos Banreservas.", "div": "br", "rev": "personal", "products": [
            P("puntos", "Puntos Banreservas & benefits guide", "One point worth RD$1 for every RD$200 on credit cards and RD$300 on debit, up to 25,000 points a transaction, plus merchant discounts in the Guía de Beneficios.",
              s=["con", "pref"], lc="grow", neo=[1, "Earned on Visa and Mastercard cards."],
              mc="A points scheme with no card-linked offers engine behind it.",
              src=[["Banreservas: Mastercard Débito Standard", DEBIT], ["Banreservas: Visa Platinum Universe", UNIVERSE]]),
            P("promos", "Network promotions", "Campaigns funded with the networks: Mastercard cashback, travel and Christmas promotions across debit, credit and Credimás, and Visa draws such as VIP winter-baseball tickets (2024).",
              s=["con"], lc="grow", o="P", at="Visa, Mastercard", neo=[1, "Both networks fund campaigns."], src=[["Banreservas: personal cards", CARDS]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: personal and SME loans, corporate, government and rice finance, 44% of the country's tourism lending, inclusion accounts that banked a million people, and insurance, pensions and funds through its subsidiaries.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Personal lending", "blurb": "RD$124bn lent to people.", "div": "br", "rev": "personal", "products": [
            P("personal", "Consumer loans & mortgages", "190,068 personal loans for RD$123.8 billion from January to November 2025; mortgages of RD$85.8 billion; 21,092 fully digital consumer loans averaging RD$309,000.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Memoria Institucional 2025", MEM]]),
            P("fairs", "Expo Hogar & Expo Móvil", "Housing and car fairs with pre-qualification through Alma: 1,495 home applications worth RD$8.4 billion and 3,781 car applications worth RD$8.5 billion in 2025.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Memoria Institucional 2025", MEM]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "SME banking", "blurb": "RD$48bn to small firms.", "div": "br", "rev": "personal", "products": [
            P("sme", "SME banking", "23,766 loans for RD$48.4 billion in 2025, Expo Fomenta Pymes (8,439 loans) and about 88,000 SME clients by identity card and 81,000 by tax number; LatinFinance's bank of the year for SMEs in Latin America and the Caribbean.",
              s=["sme"], lc="borrow", neo=[1, "Mastercard debit; Visa and Mastercard credit."], src=[["Memoria Institucional 2025", MEM]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Corporate, public & agri", "blurb": "Corporates, the state and rice.", "div": "br", "rev": "corporate", "products": [
            P("corporate", "Corporate & investment banking", "Corporate disbursements above RD$63.2 billion and a RD$110.4 billion book in 2025, deposits above RD$50.4 billion, and trade and supply-chain finance awards.",
              s=["corp"], lc="borrow", neo=[1, "Visa corporate cards; Mastercard Comercial from Oct 2026."], src=[["Memoria Institucional 2025", MEM]]),
            P("government", "Government business", "Public-sector deposits of RD$161.4 billion, a RD$40 billion budget credit line and road financing; the bank pays the state's grants and education bonuses.",
              s=["corp"], lc="borrow", rev="gov", neo=[0, ""], src=[["Memoria Institucional 2025", MEM]]),
            P("agro", "Rice pledge finance", "RD$11.7 billion lent to rice growers and millers in 2025 and RD$12 billion approved for 2025–26 at 7%; RD$8.6 billion disbursed in 2026 by September.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Memoria Institucional 2025", MEM], ["elDinero: RD$7bn for productive sectors, Sep 2026", SEP26]]),
        ]},
        {"id": "4.4", "ic": "plane", "name": "Tourism", "blurb": "44% of tourism lending.", "div": "br", "rev": "tourism", "products": [
            P("tourism", "Tourism finance", "A tourism book above RD$61 billion, about 44% of the system's tourism lending; at FITUR 2026 the bank identified more than US$6.5 billion of opportunities and US$4.2 billion of expected financing for about 11,000 hotel rooms.",
              s=["corp"], lc="borrow", neo=[0, ""],
              mc="Hotels and cruise ports are where visitors' cards are accepted.",
              src=[["Memoria Institucional 2025", MEM], ["elDinero: FITUR 2026, Jan 2026", FITUR26]]),
        ]},
        {"id": "4.5", "ic": "users-round", "name": "Financial inclusion", "blurb": "A million newly banked.", "div": "br", "rev": "personal", "products": [
            P("bancarizar", "Bancarizar es Patria", "The inclusion programme that has banked more than a million Dominicans since 2021 with more than 100 partners, Mastercard among them; over 60% of new account holders in 2025 were women aged 19 to 35.",
              s=["incl"], lc="open", o="P", at="Mastercard, Supérate", neo=[1, "Mastercard a named partner."], src=[["Memoria Institucional 2025", MEM]]),
            P("digitalacct", "Digital & basic accounts", "Inclusive basic account and the digital account (228,000 openings, RD$6.5 billion of balances); 575,913 accounts opened in 2025, 59.7% of savings accounts digitally.",
              s=["incl", "con"], lc="open", neo=[1, "Accounts come with Mastercard debit ⚠."], src=[["Memoria Institucional 2025", MEM]]),
        ]},
        {"id": "4.6", "ic": "coins", "name": "Insurance, pensions & funds", "blurb": "Ten subsidiaries.", "div": "seguros", "rev": "central", "products": [
            P("subs", "Subsidiaries", "Seguros Reservas, ARS Reservas (health), AFP Reservas (pensions), AFI Reservas (funds), Inversiones & Reservas (brokerage), Fiduciaria Reservas, Inmobiliaria Reservas and the Fundación Reservas del País microfinance foundation; RD$306.8 million of policies sold through the bank in 2025.",
              s=["con", "corp"], lc="grow", neo=[0, ""], src=[["Memoria Institucional 2025", MEM]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: an app with 13.7 million downloads that uses no mobile data, 458 locations with a branch in New York and digital sign-up in Spain, and 971 ATMs and 1,300 sub-agents in every municipality.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "App & TuBanco", "blurb": "200m app transactions.", "div": "br", "rev": "personal", "products": [
            P("app", "Banreservas app & TuBanco", "13.7 million downloads, more than 200 million transactions in 2025 (up 48%) and 1.9 million transacting users, with mobile data paid by the bank; 580,000 users moved to the new TuBanco Personas.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["Memoria Institucional 2025", MEM]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & diaspora", "blurb": "458 locations; NY and Spain.", "div": "br", "rev": "personal", "products": [
            P("branches", "Branches", "458 locations across all 32 provinces; 95,000 customers referred from branches to the app in 2025.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Memoria Institucional 2025", MEM]]),
            P("diaspora", "Diaspora banking", "Digital savings accounts for Dominicans in Spain, real-estate fairs in New York and Madrid (RD$8.7 billion placed in 2026), and a New York presence ⚠.",
              s=["dias"], lc="open", st="new", neo=[0, ""], src=[["Memoria Institucional 2025", MEM], ["elDinero: RD$7bn for productive sectors, Sep 2026", SEP26]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "ATMs & sub-agents", "blurb": "971 ATMs, 1,300 agents.", "div": "br", "rev": "personal", "products": [
            P("atms", "ATMs", "971 ATMs and more than 2,000 surcharge-free through UNARED; contactless withdrawals for MIO and other banks' cards added in 2025.",
              s=["con", "incl"], lc="everyday", neo=[0, ""], src=[["Memoria Institucional 2025", MEM]]),
            P("subagents", "Banking sub-agents", "More than 1,300 shops acting as agents in every municipality, 17.7 million transactions in 2025 (up 20%); current-account withdrawals added.",
              s=["incl"], lc="everyday", neo=[0, ""], src=[["Memoria Institucional 2025", MEM]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Banreservas", "blurb": "Debit, half of credit, a new commercial card.", "products": [
        P("mcatbr", "Mastercard at Banreservas", "Mastercard carries all 3.8 million Banreservas debit cards in the live catalogue, half the consumer credit tiers including the Black card, the MIO e-wallet for new clients since 2025 and, from 5 October 2026, Mastercard Comercial. Visa holds Infinite, SER, most commercial and fleet cards and launched MIO; both licences are non-exclusive.",
          s=["con"], div="br", rev="central", mc="The relationship this map is drawn for.",
          src=[["Memoria Institucional 2025", MEM], ["Revista Mercado: Mastercard Comercial, Oct 2026", MCCOMNEWS]]),
    ]},
    {"id": "pillar-market", "name": "Dominican banking", "blurb": "Cash, cards and instant payments.", "products": [
        P("market", "The Dominican market", "Bank assets of RD$3.6 trillion (2025) led by Banreservas, Banco Popular and BHD; Visa has 53% of the market's credit-card products and Mastercard 24%; 65% of adults banked; and the central bank's instant-payments system with QR is due in 2027.",
          s=["con"], div="br", rev="central", src=[["elDinero: card products, Sep 2026", SBTYPES], ["elDinero: instant payments in 2027, Sep 2026", SGPI]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
