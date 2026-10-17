"""Banco Pichincha's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the audited 2025 annual financial report (February
2026) and BankWatch's rating extract with data to 31 March 2026 (May 2026). The bank is unlisted and publishes no
quarterly results deck or segment results. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's
own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

IFA = "https://www.pichincha.com/sites/default/files/documents/2026-02/informe-financiero-anual-bp-2025.pdf"
BWR = "https://www.pichincha.com/sites/default/files/documents/2026-07/extracto-de-calificacion-papel-comercial-banco-pichincha.pdf"
FITCH = "https://www.expreso.ec/economia-y-negocios/fitch-eleva-calificacion-banco-pichincha-abre-paso-financiamiento-mejores-condiciones-284339.html"
GG = "https://www.expreso.ec/actualidad/economia/alejandro-ribadeneira-asume-como-nuevo-gerente-general-de-banco-pichincha-272091.html"
DIG = "https://www.primicias.ec/economia/banco-pichincha-concentra-transacciones-canales-digitales-134017/"
VDIR = "https://www.primicias.ec/economia/banco-pichincha-transferencias-internacionales-app-aplicativo-movil-ecuador-133335/"
CARDS = "https://www.pichincha.com/detalle-catalogo/personas-tarjetas-credito"
BIZ = "https://www.pichincha.com/detalle-catalogo/creditos-tarjetas-empresariales"
DDIG = "https://www.pichincha.com/detalle-producto/personas-tarjeta-debito-digital"
QUANTUM = "https://www.pichincha.com/detalle-producto/personas-tarjeta-quantum"
MILES = "https://www.pichincha.com/detalle-producto/personas-producto-tarjeta-credito-servicios-plan-de-lealtad"
METRO = "https://www.pichincha.com/detalle-producto/personas-tarjeta-ciudad-metro-quito"
VECINO = "https://www.pichincha.com/mi-vecino"
DEUNA = "https://www.pichincha.com/deuna"
DEUNAPYME = "https://www.pichincha.com/detalle-producto/pymes-servicios-deuna"
DEUNA24 = "https://primicias.ec/economia/billeteras-digitales-ecuador-google-apple-pay-deuna-85103"
APP = "https://www.pichincha.com/banca-movil"
INTL = "https://www.pichincha.com/transferencias-internacionales"
ABOUT = "https://www.pichincha.com/lo-que-ofrecemos"
SAG = "https://www.pichincha.com/sites/default/files/documents/2026-07/MastercardSaG2.pdf"
PAPA = "https://www.pichincha.com/sites/default/files/documents/2026-05/Papa_Mastercard.pdf"
BONOS = "https://www.pichincha.com/sites/default/files/documents/2026-09/TarjetaBonos-Tyc2.pdf"
PANINI = "https://www.pichincha.com/sites/default/files/documents/2026-05/Visa_ActivacionTC_Panini.pdf"
SIP = "https://primicias.ec/economia/transferencias-bancarias-ecuador-resolucion-junta-monetaria-banco-central-87660"
SIP26 = "https://asobanca.org.ec/wp-content/uploads/2026/03/RO-Res.-BCE-GG-007-2026-Estandar-mensajeria-transferencias-electronicas-pago-tiempo-real.pdf"
BOARD = "https://primicias.ec/noticias/economia/banco-pichincha-utilidades-reserva-capitalizacion"
EGAS = "https://www.expreso.ec/actualidad/economia/fidel-egas-propietario-banco-pichincha-compro-intercredit-bank-medios-miami-87573.html"
RANK = "https://www.expreso.ec/actualidad/economia/pichincha-pacifico-y-guayaquil-los-de-mayor-utilidad-en-2025-268744.html"
COL = "https://www.valoraanalitik.com/pichincha-renuncio-productos-rentable-2027/"
KASP = "https://www.kaspersky.com/small-business-security/resources/customers/banco-pichincha-takes-the-lead-in-fight-against-banking-fraud"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · ratings · family group", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: about 28% of Ecuador's banking assets, a $240 million profit in 2025, a local AAA and a Fitch upgrade, a family-controlled group founded in 1906, and a new general manager since February 2026.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "$22bn of assets, number one.", "div": "bp", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Bank assets of $21.5 billion, deposits of $17.7 billion and net profit of $240.5 million in 2025 (up 60%); $22.3 billion of assets at March 2026, about 28% of Ecuador's banking system, with a first-quarter profit of $62.4 million. The consolidated group holds $27.0 billion.",
              s=["con"], neo=[0, ""], src=[["Annual financial report 2025", IFA], ["BankWatch rating extract, May 2026", BWR]]),
        ]},
        {"id": "1.2", "ic": "badge-check", "name": "Ratings & funding", "blurb": "AAA locally, B from Fitch.", "div": "bp", "rev": "group", "products": [
            P("ratings", "Ratings & capital markets", "Local AAA (PCR) and AAA- (BankWatch); AAA for a $235 million commercial-paper programme (May 2026); Fitch raised it from CCC+ to B in June 2026, a notch above Ecuador. Solvency 16.5% at December 2025.",
              s=["corp"], st="new", ay="Jun 2026", neo=[0, ""], src=[["Expreso: Fitch upgrade, Jun 2026", FITCH], ["BankWatch rating extract, May 2026", BWR], ["Expreso: new general manager, Jan 2026", GG]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Ownership & leadership", "blurb": "Ribadeneira runs it from 2026.", "div": "bp", "rev": "group", "products": [
            P("leadership", "Owners, board & management", "Unlisted and controlled by the family of Fidel Egas Grijalva ⚠. Antonio Acosta Espinosa chairs the board ⚠ (re-elected 2022). Alejandro Ribadeneira Jaramillo became general manager on 27 February 2026, succeeding Santiago Bayas, who joined the board.",
              s=["corp"], st="flux", ay="Feb 2026", neo=[0, ""], src=[["Expreso: new general manager, Jan 2026", GG], ["Primicias: board, Mar 2022", BOARD], ["Expreso: Fidel Egas, 2020", EGAS]]),
        ]},
        {"id": "1.4", "ic": "building-2", "name": "Group & subsidiaries", "blurb": "Since 1906; Deuna to Teuno.", "div": "subs", "rev": "group", "products": [
            P("group", "Grupo Pichincha", "Founded in Quito in 1906 and a universal bank since 2017. Ecuador subsidiaries: Deuna (payments), Pague Ya (collections), Vaserum (cash and ATM logistics), Almesa (warehousing) and Teuno (data and telecoms); association agreements with Diners Club, Banco General Rumiñahui and Banco de Loja; Credife merged in 2024.",
              s=["corp"], o="I", neo=[0, ""], src=[["Annual financial report 2025", IFA], ["BankWatch rating extract, May 2026", BWR]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & technology", "blurb": "Inclusion, digital, long funding.", "div": "bp", "rev": "group", "products": [
            P("strategy", "Strategy", "No published multi-year targets. Stated aims: financial inclusion and digitalisation (8 in 10 customers digital), sustainability, the agricultural book, and longer international funding after the Fitch upgrade for energy and infrastructure.",
              s=["corp"], neo=[0, ""], src=[["Annual financial report 2025", IFA], ["Expreso: Fitch upgrade, Jun 2026", FITCH]]),
            P("tech", "Technology & AI", "Over 5,000 staff; Teuno runs data and telecoms in-house. No public AI or cloud programme for the Ecuador bank was found ⚠.",
              s=["corp"], st="unconf", neo=[None, "Nothing public."], mc="An open question: no named AI, cloud or data partner.",
              src=[["Banco Pichincha: about us", ABOUT], ["Annual financial report 2025", IFA]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Visa debit for every account, credit cards on Visa and Mastercard, corporate and micro-business cards on both, merchant acquiring where Visa earns three times Mastercard's fees, the bank's own Deuna QR, instant transfers under a new central-bank mandate, and Visa Direct for money sent abroad.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "All Visa.", "div": "bp", "rev": "personas", "products": [
            P("debit", "Tarjeta de Débito Visa Internacional", "The standard debit card for savings and current accounts, for use in Ecuador and abroad, requested in the app; all of the bank's debit cards are Visa.",
              s=["con", "micro"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Banco Pichincha: cards", CARDS]]),
            P("debitdigital", "Tarjeta de Débito Digital", "A virtual Visa debit card, one per account, with limits up to $2,000 a day, biometric validation and Apple Pay and Google Pay provisioning.", short="Digital debit (Visa)",
              s=["con"], lc="everyday", st="new", o="P", at="Visa, Apple, Google", neo=[0, "Visa."],
              mc="Digital debit is where a second network would most easily enter.", src=[["Banco Pichincha: digital debit card", DDIG]]),
            P("affinity", "Affinity debit cards", "Visa Débito Liga (LDU Quito), Barcelona Sporting Club and Universidad Católica cards.",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Banco Pichincha: cards", CARDS]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Visa and Mastercard, Miles on both.", "div": "miles", "rev": "personas", "products": [
            P("visacredit", "Visa credit cards", "Six Visa tiers on Pichincha Miles: Infinite, Signature, Platinum, Gold, Premium and Joven; Visa new-card placement backed by a World Cup 2026 sticker album.", short="Credit (Visa)",
              s=["con", "aff"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Banco Pichincha: cards", CARDS], ["Visa World Cup card placement, May 2026", PANINI]]),
            P("mccredit", "Mastercard credit cards", "Five Mastercard tiers on Pichincha Miles: Black, Platinum, Gold, Premium and Joven; the bank holds the licence as issuer, processor and administrator; Spend And Get Mastercard ran from 31 July to 6 October 2026.", short="Credit (Mastercard)",
              s=["con", "aff"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's main footprint at Ecuador's largest bank.",
              src=[["Banco Pichincha: cards", CARDS], ["Spend And Get Mastercard 2026 terms", SAG], ["Annual financial report 2025", IFA]]),
            P("quantum", "Tarjeta Quantum", "The bank's most exclusive card, by invitation to preferred clients, issued on Visa or Mastercard; lounge access through Visa Airport Companion or Priority Pass, or Mastercard Airport Experiences.",
              s=["aff"], lc="borrow", o="P", at="Visa, Mastercard", neo=[1, "Visa or Mastercard."], src=[["Banco Pichincha: Quantum", QUANTUM]]),
        ]},
        {"id": "2.3", "ic": "briefcase-business", "name": "Business cards", "blurb": "Black Corporate on Mastercard.", "div": "bp", "rev": "empresas", "products": [
            P("visabiz", "Visa business cards", "Visa Empresarial (two versions), Visa Corporativa (two), Visa CTA Miles for corporate travel and a Visa prepaid card for operating expenses.",
              s=["sme", "corp"], lc="move", o="P", at="Visa", neo=[0, "Visa."], src=[["Banco Pichincha: business cards", BIZ]]),
            P("mcbiz", "Mastercard business cards", "Mastercard Corporativa Pichincha Miles, Black Corporate, Business Black and Black Corporativa, for travel, representation and supplier spend.", short="Business (Mastercard)",
              s=["sme", "corp"], lc="move", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard owns the top corporate tier here.", src=[["Banco Pichincha: business cards", BIZ]]),
            P("microcards", "Microfinance cards", "Visa and Mastercard Premium Microfinanzas cards, with or without Pichincha Miles, for micro-entrepreneurs.",
              s=["micro"], lc="borrow", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard."], src=[["Banco Pichincha: business cards", BIZ]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acquiring", "blurb": "Visa fees three times Mastercard's.", "div": "bp", "rev": "empresas", "products": [
            P("acquiring", "Merchant acquiring", "Merchant commissions of $40.8 million from Visa establishments and $12.6 million from Mastercard in 2025 (about 76% and 24%), and $26,000 from Discover; processor not published ⚠.",
              s=["sme", "corp"], lc="move", neo=[1, "Accepts every network; Mastercard about a quarter of fees."],
              mc="Acceptance and merchant data at the country's largest acquiring bank ⚠.", src=[["Annual financial report 2025", IFA]]),
            P("paylink", "Link de Pagos", "Payment links for card sales online, for small businesses without a web shop ⚠ networks not stated.",
              s=["sme", "micro"], lc="move", neo=[1, "Card-agnostic ⚠."], src=[["Banco Pichincha: cards", CARDS]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Deuna QR", "blurb": "The bank's own wallet.", "div": "deuna", "rev": "personas", "products": [
            P("deuna", "Deuna wallet", "A QR and phone-number wallet launched in 2019 from the bank's innovation lab, run by App Deuna S.A., a licensed payments-system operator (99.98% owned); about 5 million customers and 420,000 merchants (December 2024 ⚠); QR payments now inside Banca Móvil. 2025 revenue $7.6 million, loss $4.9 million.", short="Deuna (account-to-account)",
              s=["con", "micro"], lc="move", st="active", ay="2019", o="B", neo=[0, "Account-to-account."],
              mc="The bank's own rail competes with cards for small payments.",
              src=[["Primicias: digital wallets, Dec 2024", DEUNA24], ["Banco Pichincha: Deuna", DEUNA], ["Annual financial report 2025", IFA]]),
            P("deunamerchant", "Cobra con Deuna", "Merchants download a unique QR and collect straight into their account, up to $250,000, managed in Banca Móvil or the Deuna app.",
              s=["micro", "sme"], lc="move", o="B", neo=[0, "Account-to-account."], src=[["Banco Pichincha: Deuna for businesses", DEUNAPYME]]),
        ]},
        {"id": "2.6", "ic": "arrow-left-right", "name": "Transfers & instant payments", "blurb": "Instant by law from 2026.", "div": "bp", "rev": "personas", "products": [
            P("transfers", "Transfers", "Three in four banking operations are phone transfers; transfers within Pichincha and allied banks are instant, others take up to 72 hours; interbank transfers rose 11% in 2025.",
              s=["con", "sme"], lc="move", neo=[0, ""], src=[["Primicias: digital channels, Oct 2026", DIG], ["Banco Pichincha: Banca Móvil", APP]]),
            P("sip", "Instant payments mandate", "Resolution JPRM-2024-029-M (December 2024) makes interbank transfers real-time through private networks or the central bank's Sistema Integrador de Pagos, with payment keys and a standard QR; the messaging standard is compulsory by 30 November 2026.",
              s=["con", "sme"], lc="move", st="flux", ay="Nov 2026", neo=[0, "Central-bank rails."],
              mc="Standard QR and instant payments arrive in late 2026.", src=[["Primicias: instant transfers, Jan 2025", SIP], ["BCE resolution GG-007-2026", SIP26]]),
        ]},
        {"id": "2.7", "ic": "send", "name": "Cross-border", "blurb": "Visa Direct, September 2026.", "div": "bp", "rev": "intl", "products": [
            P("visadirect", "International transfers with Visa Direct", "In the app since 24 September 2026: up to $15,000 a transfer (about $680 on average), with cost and exchange-rate simulation, for remittances, tuition and supplier payments.", short="Remittances (Visa Direct)",
              s=["con", "migr", "sme"], lc="move", st="new", ay="Sep 2026", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa won the app's outbound remittance rail.", src=[["Primicias: Visa Direct, Sep 2026", VDIR]]),
            P("swift", "Transfers abroad & money from the US and Spain", "Bank transfers abroad of up to $15,000 a day, money received from the United States and Spain, and the Ecuadorian-migrant corridor served by Banco Pichincha España.",
              s=["migr"], lc="move", neo=[0, ""], src=[["Banco Pichincha: international transfers", INTL], ["Annual financial report 2025", IFA]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud and cyber defence for a bank where 83% of transactions are digital, Pichincha Miles with Priceless and World Cup campaigns on top, and partnerships with cooperatives, Diners Club and smaller banks.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "83% of transactions digital.", "div": "bp", "rev": "personas", "products": [
            P("fraud", "Fraud & cyber defence", "A cyber-defence team, biometric validation on digital cards, temporary and permanent card blocking in the app; an anti-fraud drive with Kaspersky from 2013 ⚠. No card-network risk tool is publicly named.",
              s=["con", "sme"], lc="everyday", neo=[None, "No network tool named."],
              mc="High digital volumes with no named network risk scoring.", src=[["Primicias: digital channels, Oct 2026", DIG], ["Banco Pichincha: digital debit card", DDIG], ["Kaspersky case study ⚠", KASP]]),
            P("fraudins", "Robbery & fraud insurance", "Insurance against card robbery and fraud sold alongside accounts and cards.",
              s=["con"], lc="everyday", o="P", neo=[0, ""], src=[["Banco Pichincha: cards", CARDS]]),
        ]},
        {"id": "3.2", "ic": "gift", "name": "Loyalty & campaigns", "blurb": "Pichincha Miles, Priceless.", "div": "miles", "rev": "personas", "products": [
            P("miles", "Pichincha Miles", "Miles earned on Visa and Mastercard credit cards and redeemed from a catalogue at pichinchamiles.com; reward-plan income of $15.9 million in 2025.",
              s=["con", "aff", "sme"], lc="grow", o="B", neo=[1, "Earned on Visa and Mastercard."],
              mc="Card-linked offers could feed the catalogue.", src=[["Banco Pichincha: Pichincha Miles", MILES], ["Annual financial report 2025", IFA]]),
            P("mccampaigns", "Mastercard campaigns & Priceless", "Father's Day 2026 drew two Priceless experiences and a Madrid–Barcelona trip for Mastercard cardholders; Spend And Get Mastercard 2026 (31 July to 6 October); new-card bonuses on Visa or Mastercard (1 September to 30 October 2026).",
              s=["con", "aff"], lc="grow", st="new", ay="May 2026", o="P", at="Mastercard", neo=[3, "Mastercard's Priceless."],
              src=[["Father's Day 2026 terms", PAPA], ["Spend And Get Mastercard 2026 terms", SAG], ["New credit card bonuses terms", BONOS]]),
            P("visacampaigns", "Visa World Cup 2026", "First-time Visa credit cardholders receive a World Cup 2026 sticker album and 350 stickers.",
              s=["con"], lc="grow", st="new", ay="May 2026", o="P", at="Visa", neo=[0, "Visa."], src=[["Visa World Cup card placement, May 2026", PANINI]]),
        ]},
        {"id": "3.3", "ic": "plug", "name": "Partners & open finance", "blurb": "Cooperatives, Diners, BGR.", "div": "deuna", "rev": "group", "products": [
            P("coops", "Deuna with cooperatives & banks", "Deuna links savings cooperatives (Tulcán, Cotocollao, Alianza del Valle) and Banco General Rumiñahui; association agreements with BGR and Banco de Loja (2022). No open-banking mandate in Ecuador found ⚠.",
              s=["con", "micro"], lc="open", o="P", neo=[0, ""], src=[["Primicias: digital wallets, Dec 2024", DEUNA24], ["Annual financial report 2025", IFA]]),
            P("diners", "Diners Club association", "An association agreement with Banco Diners Club del Ecuador, renewed in 2019 and extended in July 2024 for five years.",
              s=["aff"], lc="borrow", o="P", at="Diners Club", neo=[0, "Diners Club."], src=[["Annual financial report 2025", IFA]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: accounts, consumer loans and mortgages for more than a third of Ecuadorians, cash management and trade finance for companies, microfinance from the old Credife, a $2.5 billion farm book, and banks in Spain, Colombia and Miami.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Personal banking", "blurb": "6.5 million customers.", "div": "bp", "rev": "personas", "products": [
            P("accounts", "Accounts & deposits", "Savings and current accounts for about 6.5 million customers, more than 36% of Ecuador's population; public deposits of $17.7 billion at December 2025; term deposits from $500.",
              s=["con", "aff"], lc="everyday", neo=[0, "Visa debit."], src=[["Annual financial report 2025", IFA], ["Expreso: new general manager, Jan 2026", GG]]),
            P("loans", "Consumer loans & mortgages", "Multipurpose and revolving credit, mortgages from 7.5% financing up to 83%, car and education loans; gross loans of $13.9 billion across segments.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Banco Pichincha: cards", CARDS], ["BankWatch rating extract, May 2026", BWR]]),
            P("insurance", "Insurance & assistance", "Health, life, funeral, fraud and travel cover sold through the bank.",
              s=["con"], lc="beyond", o="P", neo=[0, ""], src=[["Banco Pichincha: cards", CARDS]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Corporate & SME", "blurb": "Cash management, trade.", "div": "bp", "rev": "empresas", "products": [
            P("cashmgmt", "Banca Empresas & cash management", "Payroll (Nómina Confianza), supplier and third-party payments, collections for companies ($81.5 million of fees in 2025) and cash management ($11.1 million).",
              s=["sme", "corp"], lc="everyday", neo=[0, ""], src=[["Annual financial report 2025", IFA], ["Banco Pichincha: business cards", BIZ]]),
            P("trade", "Trade & long-term finance", "Working capital and fixed-asset loans, letters of credit, and trade lines guaranteed by the IFC (since 2013) and the IDB (since 2016).",
              s=["corp"], lc="borrow", o="P", at="IFC, IDB", neo=[0, ""], src=[["Annual financial report 2025", IFA]]),
        ]},
        {"id": "4.3", "ic": "hand-coins", "name": "Microfinance", "blurb": "Credife folded in.", "div": "bp", "rev": "micro", "products": [
            P("microfinance", "Microfinance", "Micro-enterprise lending, now inside the bank after Credife Desarrollo Microempresarial merged in 2024, with microfinance cards and Mi Vecino agents.",
              s=["micro"], lc="borrow", st="flux", o="I", neo=[0, ""], src=[["BankWatch rating extract, May 2026", BWR]]),
        ]},
        {"id": "4.4", "ic": "earth", "name": "Agribusiness", "blurb": "$2.5bn, Rabobank to 2028.", "div": "bp", "rev": "empresas", "products": [
            P("agro", "Agricultural finance", "A $2.5 billion agricultural book and an alliance with Rabobank renewed to 2028, reaching more than 100,000 producers with finance and technical help.",
              s=["micro", "corp"], lc="borrow", o="P", at="Rabobank", neo=[0, ""], src=[["Annual financial report 2025", IFA]]),
        ]},
        {"id": "4.5", "ic": "globe", "name": "International", "blurb": "Spain, Colombia, Miami.", "div": "espana", "rev": "intl", "products": [
            P("spain", "Banco Pichincha España", "78.9% owned, based in Madrid, serving Ecuadorian, Peruvian and Colombian migrants and businesses: deposits of €3.1 billion and loans of €2.45 billion at end-2025.",
              s=["migr"], lc="everyday", neo=[None, "Card networks not checked."], src=[["Annual financial report 2025", IFA]]),
            P("colombia", "Banco Pichincha Colombia & Pibank", "91.1% owned and loss-making; plans to cut the loss about 20% in 2026 with about $39 million of new capital; Pibank, its digital brand, holds about a third of customers ⚠.",
              s=["con"], lc="everyday", st="flux", neo=[None, "Not researched."], src=[["Annual financial report 2025", IFA], ["Valora Analitik: Pichincha Colombia ⚠", COL]]),
            P("miami", "Agencia Miami", "A Florida-licensed agency since 1986, supervised by the Federal Reserve Bank of Atlanta.",
              s=["corp"], lc="everyday", neo=[0, ""], src=[["Annual financial report 2025", IFA]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: Banca Móvil and web for 5.5 million active digital users, branches in every canton and the country's largest ATM network, more than 8,500 Mi Vecino agents, and WhatsApp and phone banking.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Banca Móvil", "blurb": "5.5m active digital users.", "div": "bp", "rev": "personas", "products": [
            P("app", "Banca Móvil & Banca Web", "5.5 million active digital users and 83% of monetary transactions digital; 164 million mobile transactions worth nearly $15 billion in a month; card instalments from $50 over up to 12 months and cardless ATM withdrawals.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["Primicias: digital channels, Oct 2026", DIG], ["Banco Pichincha: Banca Móvil", APP]]),
            P("bills", "Bills, tax & Metro de Quito", "Utility, tax and fine payments, phone top-ups, and activation and top-up of the Metro de Quito Tarjeta Ciudad; fares can also be paid with Deuna.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Banco Pichincha: Metro de Quito", METRO]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "Every canton.", "div": "bp", "rev": "personas", "products": [
            P("branches", "Branches & ATMs", "Branches in every canton of Ecuador and, by the bank's account, the largest ATM network in the country; deposit ATMs take cash, cheques and repayments of the bank's Visa and Mastercard cards.",
              s=["con", "micro"], lc="everyday", neo=[0, ""], src=[["Expreso: new general manager, Jan 2026", GG], ["Banco Pichincha: business cards", BIZ]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Mi Vecino", "blurb": "8,500+ agents.", "div": "vecino", "rev": "micro", "products": [
            P("mivecino", "Mi Vecino agents", "More than 8,500 corner shops acting as banking agents for deposits, withdrawals and payments of $1 to $500 a day, open from 6am to 10pm.",
              s=["con", "micro"], lc="everyday", neo=[0, ""], src=[["Banco Pichincha: Mi Vecino", VECINO]]),
        ]},
        {"id": "5.4", "ic": "headset", "name": "WhatsApp & phone", "blurb": "Help on any channel.", "div": "bp", "rev": "personas", "products": [
            P("contact", "WhatsApp & telephone banking", "Account, card and loan queries on WhatsApp and telephone banking, which also handles card limits and Quantum's fast-track airport service.",
              s=["con", "aff"], lc="everyday", neo=[0, ""], src=[["Banco Pichincha: Quantum", QUANTUM]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Pichincha", "blurb": "Second card, first in Black.", "products": [
        P("mcatpichincha", "Mastercard at Pichincha", "Visa carries every debit card, six credit tiers, the September 2026 remittance launch and about three-quarters of merchant commissions. Mastercard has five consumer credit tiers up to Black, Quantum on either network, four corporate products and 2026 campaigns with Priceless.",
          s=["con"], div="bp", rev="group", mc="The relationship this map is drawn for.",
          src=[["Banco Pichincha: cards", CARDS], ["Annual financial report 2025", IFA], ["Primicias: Visa Direct, Sep 2026", VDIR]]),
    ]},
    {"id": "pillar-market", "name": "Ecuadorian banking", "blurb": "Dollarised, cash-heavy, going instant.", "products": [
        P("market", "The Ecuadorian market", "About 23 banks ⚠ in a dollarised economy rated B-; Pichincha leads Banco Guayaquil, Banco del Pacífico and Produbanco by assets and profit; 2025 profits recovered after a weak 2024; instant payments and a standard QR become compulsory in late 2026.",
          s=["con"], div="bp", rev="group", src=[["Expreso: 2025 bank profits", RANK], ["Expreso: Fitch upgrade, Jun 2026", FITCH], ["BCE resolution GG-007-2026", SIP26]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
