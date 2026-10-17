"""Banamex's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the GFBanamex 2Q26 report (July 2026) and the 2025
Integrated Annual Report; networks were read from Banamex's own card pages on 17 October 2026. Amounts in pesos (Ps).
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://www.banamex.com/inversionistas/assets/pdf/eng/financial/GFBanamex2Q26.pdf"
AR25 = "https://www.banamex.com/inversionistas/assets/pdf/eng/sustainability/BanamexIntegratedAnnualReport2025.pdf"
IR = "https://www.banamex.com/investors/"
BOARD = "https://www.banamex.com/inversionistas/assets/pdf/eng/governance/BoardofDirectors.pdf"
DESCH = "https://www.banamex.com/inversionistas/assets/pdf/eng/events/July292026.pdf"
HRPR = "https://www.banamex.com/inversionistas/assets/pdf/eng/events/July302026.pdf"
CITI24 = "https://www.citigroup.com/global/news/press-release/2026/citi-announces-agreements-with-investors-for-commitments-to-purchase-an-aggregate-24-equity-stake-in-banamex"
CITI226 = "https://www.citigroup.com/global/news/press-release/2026/citi-announces-completion-22-6-percent-sale-equity-stake-banamex"
IPO = "https://finance.yahoo.com/markets/stocks/articles/citigroup-c-lines-3-billion-202731590.html"
C10Q = "https://www.sec.gov/Archives/edgar/data/0000831001/000083100126000045/c-20260630.htm"
CARDS = "https://www.banamex.com/es/personas/tarjetas-credito/"
PLATINUM = CARDS + "tarjeta-platinum.html"
DESCUBRE = CARDS + "tarjeta-de-credito-recompensas-descubre.html"
EXPLORA = CARDS + "tarjeta-de-credito-viajes-explora.html"
CONQUISTA = CARDS + "tarjeta-de-credito-experiencias-conquista.html"
JOY = CARDS + "tarjeta-de-credito-sin-anualidad-joy.html"
ORO = CARDS + "tarjeta-oro.html"
CLASICA = CARDS + "tarjeta-clasica.html"
HOMEDEPOT = CARDS + "tarjeta-homedepot.html"
TELETON = CARDS + "tarjeta-teleton.html"
LACOMERP = CARDS + "tarjeta-lacomer.html"
BEYOND = CARDS + "tarjeta-beyond.html"
COSTCO = CARDS + "tarjeta-costco.html"
LINEUP = CARDS + "tarjeta-credito-lineup.html"
AFFINITY = CARDS + "tarjeta-affinity.html"
PRIORITY = "https://www.banamex.com/es/personas/cuentas/cuentapriority.html"
DEBIT = "https://www.banamex.com/es/personas/cuentas/mi-cuenta-debito.html"
SWITCH = "https://www.banamex.com/personas/cuentas/cuenta-digital-switch/index.html"
LOUNGE = "https://www.banamex.com/loungekey/index.html"
LACOMER = "https://www.justretail.news/latam/noticias/banamex-y-la-comer-lanzan-tarjeta-de-credito-con-beneficios-exclusivos/"
FORTUNA = "https://revistafortuna.com.mx/2025/09/01/cierra-banamex-alianza-para-atraer-nuevos-clientes-y-extender-beneficios-de-monedero-naranja-de-la-comer/"
GPREN = "https://thepaypers.com/payments/news/global-payments-and-banamex-renew-partnership-in-mexico"
PAGOSHOPS = "https://www.mastercard.com/ar/es/news-and-trends/press/2025/july/global-payments-con-el-respaldo-de-banamex-y-mastercard-lanza-pago-shops-la-solucion-ideal-para-el-crecimiento-digital-de-las-pymes-en-mexico.html"
DPL = "https://dplnews.com/?p=283382"
SIMPL = "https://www.mastercard.com/news/latin-america/es/sala-de-prensa/comunicados-de-prensa/pr-es/2021/junio/lanzan-citibanamex-y-mastercard-la-tarjeta-de-credito-simplicity-la-primera-sin-anualidad-y-con-medidas-de-seguridad-unicas/"
WALLET16 = "https://www.eluniversal.com.mx/articulo/techbit/2016/02/16/banamex-y-mastercard-presentan-banamex-wallet/"
ABM = "https://www.abm.org.mx/sala-de-prensa/sintesis/historial/sintesis_2026_08_07.pdf"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owners · brand", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Ps 1.4 trillion of assets and Ps 541 billion of loans, a bank founded in 1884, Citi selling down to about 51% with Fernando Chico Pardo as anchor owner, a new CEO in June 2026 and an IPO targeted for January 2027 ⚠.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Ps 1.4tn assets, 49% efficiency.", "div": "gfb", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "At 30 June 2026: total assets Ps 1.40 trillion, loans Ps 541.5 billion (+12% a year), deposits Ps 805 billion, assets under management Ps 2.45 trillion. Net income Ps 6.7 billion in 2Q26 and Ps 22.2 billion in 2025; efficiency ratio 49.0%; NPL 3.2%.",
              s=["con", "corp"], neo=[0, ""], src=[["GFBanamex 2Q26 report", Q2], ["Integrated Annual Report 2025", AR25]]),
            P("capital", "Capital & funding", "Bank CET1 18.8% and total capital 24.5% after US$1.3 billion (Ps 22.5 billion) of Tier 2 notes in May 2026; LCR 238%; 42% of deposits pay no interest; a Ps 8 billion dividend paid in 2Q26.",
              s=["corp"], st="new", ay="May 2026", neo=[0, ""], src=[["GFBanamex 2Q26 report", Q2]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & IPO", "blurb": "Citi about 51%, IPO next.", "div": "gfb", "rev": "group", "products": [
            P("ownership", "Shareholders", "Fernando Chico Pardo bought 25% (closed 15 December 2025) and chairs the group; investors including General Atlantic, Afore SURA, BTG Pactual, Chubb, Blackstone funds, Liberty Strategic Capital and QIA agreed to buy 24% for about MXN 43 billion (US$2.5 billion, about 0.85x book), 22.6% closing on 29 April 2026. Citi keeps about 51% ⚠ once the last 1.4% closes.",
              short="Owners: Citi, Chico Pardo, investors", s=["corp"], st="flux", o="I", neo=[0, ""],
              src=[["Citi: 24% stake agreements, Feb 2026", CITI24], ["Citi: 22.6% sale completed, Apr 2026", CITI226], ["Integrated Annual Report 2025", AR25]]),
            P("ipo", "Initial public offering", "Citi's preferred exit. Bloomberg reported in September 2026 a January target raising more than US$3 billion, led by Citi with Bank of America, Goldman Sachs and JPMorgan ⚠ plans could change. Citi deconsolidates Banamex below 50% and books the translation loss, about US$9 billion at March 2026 ⚠.",
              s=["corp"], st="unconf", neo=[0, ""],
              mc="New public owners will review every big contract, network deals included.",
              src=[["Yahoo Finance: IPO for January, Sep 2026", IPO], ["Citigroup 10-Q, Q2 2026", C10Q]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brand", "blurb": "Since 1884; Citi 2001–24.", "div": "bank", "rev": "group", "products": [
            P("heritage", "Heritage & separation from Citi", "Founded on 2 June 1884; nationalised 1982 and reprivatised 1991; owned by Citigroup from 2001 and renamed Citibanamex in 2016. Citi announced its exit in January 2022 and the split from Citi México was completed on 1 December 2024.",
              s=["con"], o="I", neo=[0, ""], src=[["Integrated Annual Report 2025", AR25]]),
            P("brand", "Banamex brand", "Relaunched in March 2025, lighter and simpler, as the second most recognised bank brand in Mexico; the group also holds the country's leading institutional collection of Mexican art (4,000+ pieces).",
              s=["con"], st="new", ay="Mar 2025", neo=[0, ""], src=[["Integrated Annual Report 2025", AR25], ["Banamex press release, Jul 2026", DESCH]]),
        ]},
        {"id": "1.4", "ic": "users-round", "name": "Leadership", "blurb": "Chico Pardo and del Rincón.", "div": "gfb", "rev": "group", "products": [
            P("leadership", "Board & management", "Chairman Fernando Chico Pardo (of the bank too since 29 July 2026); CEO Edgardo del Rincón from 1 June 2026 after Manuel Romo; CFO Patricio Diez de Bonilla; René Pimentel runs corporate and investment banking; Citi's Ernesto Torres Cantú sits on the board.",
              s=["corp"], st="new", ay="Jun 2026", neo=[0, ""], src=[["GFBanamex 2Q26 report", Q2], ["Banamex: boards of directors", BOARD], ["Banamex press release, Jul 2026", DESCH], ["Banamex press release, 30 Jul 2026", HRPR]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & modernisation", "blurb": "A Modernization Office.", "div": "gfb", "rev": "group", "products": [
            P("strategy", "Modernization programme", "A three-year ambition to be the undisputed leader of Mexico's financial system, run through a Modernization Office (2025) that simplifies and automates; priorities are digital, younger customers, the regions and entrepreneurs. Technology separation from Citi is not detailed publicly ⚠.",
              s=["corp"], st="new", neo=[0, ""], src=[["Integrated Annual Report 2025", AR25]]),
            P("deals", "Deals", "Sold its stake in TransUnion de México (about Ps 3 billion of income in 1Q26), merged Tarjetas Banamex into the bank, and started annuities through Pensiones Banamex in late 2025.",
              s=["corp"], o="A", neo=[0, ""], src=[["GFBanamex 2Q26 report", Q2], ["Integrated Annual Report 2025", AR25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Mexico's second-largest card book (24%) with ten of fourteen credit cards on Mastercard and four on Visa, Mastercard debit ⚠, phone wallets, card acceptance through Global Payments, SPEI and CoDi, and corporate cards and cash management.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Own-brand credit cards", "blurb": "Clásica to Platinum, on Mastercard.", "div": "cards", "rev": "consumer", "products": [
            P("credit", "Banamex credit cards", "Ps 173.5 billion of card loans at June 2026 (+14% a year), a 24% share and second in Mexico. Clásica and Oro carry Mastercard insurance; the 2025 rebrand added Descubre (rewards), Explora (travel) and Conquista (experiences), all Mastercard.",
              short="Credit cards (Mastercard)", s=["con"], lc="borrow", o="B", at="Mastercard", neo=[2, "Mastercard on every own-brand card."],
              mc="Mastercard's biggest lever at Banamex: the core of a 24% share of Mexico's card balances.",
              src=[["GFBanamex 2Q26 report", Q2], ["Banamex: Descubre", DESCUBRE], ["Banamex: Explora", EXPLORA], ["Banamex: Conquista", CONQUISTA], ["Banamex: Oro", ORO], ["Banamex: Clásica", CLASICA]]),
            P("platinum", "Platinum", "Ten Salones Beyond visits and four Mastercard Airport Experiences (LoungeKey) visits a year, Elite Valet, Mastercard Concierge and travel insurance to US$1 million.",
              s=["aff"], lc="borrow", at="Mastercard", neo=[2, "Mastercard."], src=[["Banamex: Platinum", PLATINUM], ["Banamex: LoungeKey", LOUNGE]]),
            P("joy", "Joy", "A no-annual-fee card with entertainment presales ⚠ and Mastercard purchase and travel cover.",
              s=["young"], lc="borrow", at="Mastercard", neo=[2, "Mastercard."], src=[["Banamex: Joy", JOY]]),
            P("simplicity", "Simplicity (retired)", "Citibanamex Simplicity Mastercard, June 2021: no annual fee and a dynamic CVC generated in the app ⚠ no longer on sale.",
              s=["con"], lc="borrow", st="retired", ay="Jun 2021", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Mastercard: Simplicity, Jun 2021", SIMPL]]),
        ]},
        {"id": "2.2", "ic": "store", "name": "Co-brand cards", "blurb": "Costco on Visa, La Comer on Mastercard.", "div": "cards", "rev": "consumer", "products": [
            P("costco", "Costco Banamex", "Costco co-brand with an annual rebate, 'backed by Visa' with Visa insurance.",
              s=["con"], lc="borrow", o="P", at="Costco, Visa", neo=[0, "Visa."],
              mc="Likely one of the largest single programmes ⚠; a contestable prize at renewal.",
              src=[["Banamex: Costco", COSTCO]]),
            P("lacomer", "La Comer Card", "Co-brand with Grupo La Comer linked to the Monedero Naranja programme, launched with Mastercard; 5,000+ cards approved in the first month.",
              s=["con"], lc="borrow", st="new", ay="Sep 2025", o="P", at="Grupo La Comer, Mastercard", neo=[2, "Mastercard ⚠ launch date."],
              src=[["Banamex: La Comer", LACOMERP], ["Revista Fortuna, Sep 2025", FORTUNA], ["Just Retail Latam", LACOMER], ["Integrated Annual Report 2025", AR25]]),
            P("lineup", "LineUp", "Entertainment co-brand with presales, launched in 2025 to make Banamex 'the presale bank'; 8,000+ applications in the first month; Visa.",
              s=["young"], lc="borrow", st="new", ay="2025", o="P", at="LineUp, Visa", neo=[0, "Visa."], src=[["Banamex: LineUp", LINEUP], ["Integrated Annual Report 2025", AR25]]),
            P("retailcards", "Home Depot, Teletón & Affinity", "Home Depot and Teletón cards on Mastercard; the Affinity Card on Visa.",
              s=["con"], lc="borrow", o="P", at="The Home Depot, Teletón", neo=[1, "Two Mastercard, one Visa."], src=[["Banamex: Home Depot", HOMEDEPOT], ["Banamex: Teletón", TELETON], ["Banamex: Affinity", AFFINITY]]),
        ]},
        {"id": "2.3", "ic": "gem", "name": "Premium cards", "blurb": "Beyond on Visa, Priority on Mastercard.", "div": "wealth", "rev": "consumer", "products": [
            P("beyond", "Beyond", "The top card: Visa Luxury Hotel Collection, Visa Médico Online, Priority Pass, Grand Lounge and Salones Beyond, and the lowest card rate (TIIE + 17.5 points).",
              s=["aff"], lc="borrow", at="Visa", neo=[0, "Visa."], src=[["Banamex: Beyond", BEYOND]]),
            P("priority", "Banamex Priority", "Affluent account with Mastercard EveryDay Value offers, Concierge, Elite Lounge and Elite Valet Mastercard.",
              s=["aff"], lc="everyday", at="Mastercard", neo=[2, "Mastercard."], src=[["Banamex: Priority", PRIORITY]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Debit & digital accounts", "blurb": "Switch: 300,000 accounts.", "div": "bank", "rev": "consumer", "products": [
            P("debit", "Debit & payroll accounts", "Current, payroll and dollar accounts with debit cards carrying Mastercard offers (Cinépolis 2x1) ⚠ network inferred from benefits; Ps 569 billion of demand deposits.",
              s=["con"], lc="everyday", neo=[2, "Mastercard ⚠ inferred."], src=[["Banamex: debit account", DEBIT], ["GFBanamex 2Q26 report", Q2]]),
            P("switch", "Switch", "A fully digital account opened remotely, with an optional physical card; about 300,000 accounts in 2025, aimed at younger customers.",
              s=["young"], lc="open", st="new", ay="2025", neo=[2, "Mastercard benefits ⚠."], src=[["Banamex: Switch", SWITCH], ["Integrated Annual Report 2025", AR25]]),
        ]},
        {"id": "2.5", "ic": "smartphone", "name": "Wallets & tokens", "blurb": "600,000 Google Pay tokens.", "div": "bank", "rev": "consumer", "products": [
            P("wallets", "Google Pay, Apple Pay & PayPal", "Google Pay in the Android app with about 600,000 active tokens by end-2025; digital credit cards can be added to Apple Pay, Google Pay and PayPal.",
              s=["con", "young"], lc="move", st="new", ay="2025", o="P", at="Google, Apple, PayPal", neo=[1, "Tokens on both networks."],
              mc="Token growth on a mostly Mastercard card base: room for token services and Click to Pay.",
              src=[["Integrated Annual Report 2025", AR25]]),
            P("wallet16", "Banamex Wallet (retired)", "Launched February 2016 with Mastercard as Latin America's first bank wallet using host card emulation ⚠ since replaced.",
              s=["con"], lc="move", st="retired", ay="Feb 2016", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["El Universal, Feb 2016", WALLET16]]),
        ]},
        {"id": "2.6", "ic": "receipt-text", "name": "Card acceptance", "blurb": "Global Payments' EVO.", "div": "bank", "rev": "commercial", "products": [
            P("acquiring", "Acquiring with Global Payments", "Merchant acquiring through Global Payments' EVO Payments, about 900 million transactions on 250,000 terminals in Mexico; renewed for several years in July 2025.",
              s=["sme"], lc="move", ay="Jul 2025", o="P", at="Global Payments (EVO)", neo=[1, "Accepts every network."], src=[["The Paypers, Jul 2025", GPREN]]),
            P("pagoshops", "Pago Shops", "Online store builder for SMEs with a Banamex account, from Global Payments 'backed by Banamex and Mastercard' with tokenised processing; live from 1 August 2025.",
              s=["sme"], lc="move", st="new", ay="Aug 2025", o="P", at="Global Payments, Mastercard", neo=[1, "Mastercard tokenised processing ⚠."],
              src=[["Mastercard: Pago Shops, Jul 2025", PAGOSHOPS], ["DPL News, Jul 2025", DPL]]),
        ]},
        {"id": "2.7", "ic": "zap", "name": "Transfers & instant payments", "blurb": "SPEI and CoDi.", "div": "bank", "rev": "consumer", "products": [
            P("spei", "SPEI transfers & CoDi", "Real-time transfers on Banxico's SPEI, debit-card transfers now in real time, and CoDi QR and push payments; transfers are the most-saved app shortcut (about 10 million favourites).",
              s=["con", "sme"], lc="move", neo=[0, "Banxico rails."], src=[["Integrated Annual Report 2025", AR25]]),
        ]},
        {"id": "2.8", "ic": "briefcase-business", "name": "Corporate cards & cash", "blurb": "Purchasing cards, BancaNet.", "div": "bank", "rev": "commercial", "products": [
            P("commcards", "Commercial & prepaid cards", "Banamex Purchasing Card, Distribution Card, Executive Card and TU Banamex pre-funded universal card ⚠ network not stated.",
              s=["corp", "sme"], lc="move", neo=[None, "Network not stated."],
              mc="Untested ground: no public commercial-card network or Mastercard deal.",
              src=[["Integrated Annual Report 2025", AR25]]),
            P("cashmgmt", "Cash management & trade", "Peso and dollar accounts, payments and collections, BancaNet Empresarial, CitiDirect Online Banking ⚠ and Digitem, cash centres, trusts, custody, letters of credit and supply-chain finance.",
              s=["corp"], lc="move", neo=[0, ""], src=[["Integrated Annual Report 2025", AR25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: Secure Call and NetKey against fraud, AI-led fraud and credit models with Belvo income data and clear merchant names, and Momentos points and Mastercard benefits on the cards.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "8 million on Secure Call.", "div": "bank", "rev": "consumer", "products": [
            P("securecall", "Banamex Secure Call", "The app warns customers before the fraud team calls about unusual activity, against phone fraud; more than 8 million enrolled.",
              s=["con"], lc="everyday", st="new", neo=[0, "Banamex's own."],
              mc="Scam scoring on SPEI transfers is a gap Mastercard tools could fill.",
              src=[["Integrated Annual Report 2025", AR25]]),
            P("controls", "NetKey, Quick Lock & limits", "NetKey Mobile token (portable to a new phone in three steps), on-off for debit and credit cards in the app, and CNBV transaction limits (MTU) set in three clicks.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Integrated Annual Report 2025", AR25]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data & AI", "blurb": "AI awards for fraud and credit.", "div": "bank", "rev": "consumer", "products": [
            P("ai", "AI for fraud & credit", "Global Finance AI in Finance awards for fraud detection and credit assessment in 2025 ⚠ no named AI programme published.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Integrated Annual Report 2025", AR25]]),
            P("clarity", "Instant Clarity", "Merchant names and logos on every debit and credit card transaction in the app ⚠ data provider not named.",
              s=["con"], lc="everyday", st="new", neo=[None, "Provider unknown."],
              mc="Mastercard merchant data could power it.",
              src=[["Integrated Annual Report 2025", AR25]]),
            P("belvo", "Belvo income checks", "An API to IMSS through Belvo that verifies income for customers with no credit history, raising approval rates for mortgages and cards.",
              s=["con", "home"], lc="borrow", st="new", o="P", at="Belvo", neo=[0, ""], src=[["Integrated Annual Report 2025", AR25]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & benefits", "blurb": "Momentos, LoungeKey, Concierge.", "div": "cards", "rev": "consumer", "products": [
            P("momentos", "Momentos Banamex", "Card points (one per US$1 on Descubre), 2x1 flight promotions and cashback on co-brands; card rewards are now booked against fee income (from 2Q26).",
              s=["con", "aff"], lc="grow", neo=[0, "Banamex's own."], src=[["Banamex: Descubre", DESCUBRE], ["GFBanamex 2Q26 report", Q2]]),
            P("mcbenefits", "Mastercard benefits", "Mastercard Airport Experiences by LoungeKey on Platinum, Explora and Conquista; Elite Lounge Mastercard at Mexico City airport T1; Elite Valet, Concierge and MasterSeguro travel insurance.",
              s=["aff"], lc="grow", o="P", at="Mastercard", neo=[3, "Mastercard's own benefits."], src=[["Banamex: LoungeKey", LOUNGE], ["Banamex: Platinum", PLATINUM]]),
            P("lounges", "Salones Beyond", "Banamex's own airport lounges for Beyond, Platinum and Priority clients.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["Banamex: Platinum", PLATINUM], ["Banamex: Priority", PRIORITY]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: payroll and personal loans, Ps 82 billion of mortgages, SME and commercial banking, wealth and private banking with BlackRock, the second-largest life insurer and the fourth-largest Afore.",
    "tiles": [
        {"id": "4.1", "ic": "hand-coins", "name": "Loans & mortgages", "blurb": "Payroll, personal, homes.", "div": "bank", "rev": "consumer", "products": [
            P("payroll", "Payroll loans", "Ps 73.7 billion at June 2026 (+12% a year), revolving loans for people paid through Banamex, taken in the app, BancaNet, ATMs or branches.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["GFBanamex 2Q26 report", Q2], ["Integrated Annual Report 2025", AR25]]),
            P("personal", "Personal loans", "Ps 25.8 billion; up to Ps 750,000 at a fixed rate over 24–60 months, reusable in the app from 2026; Disponible Banamex beat its 2025 target by 50%.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["GFBanamex 2Q26 report", Q2], ["Integrated Annual Report 2025", AR25]]),
            P("mortgage", "Mortgages", "Ps 81.9 billion (Ps 70.1 billion residential), up 15% in 2025, with instant branch approval for payroll customers and a channel for housing developers.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["GFBanamex 2Q26 report", Q2], ["Integrated Annual Report 2025", AR25]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "SMEs", "blurb": "8.1% share, fifth.", "div": "bank", "rev": "commercial", "products": [
            P("sme", "SME banking", "Ps 43.6 billion of SME loans (8.1% share, fifth), no-fee accounts, working-capital loans, payment terminals and BancaNet Empresarial; agreements with states including Yucatán and Guanajuato.",
              s=["sme"], lc="everyday", neo=[0, ""], src=[["GFBanamex 2Q26 report", Q2], ["Integrated Annual Report 2025", AR25]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Commercial & institutional", "blurb": "Ps 187bn of loans.", "div": "bank", "rev": "commercial", "products": [
            P("commercial", "Commercial, Government & Institutional Banking", "Ps 186.6 billion of commercial loans (companies Ps 150.9 billion, government Ps 33.4 billion); market shares of 3.15% in loans, 4.1% in deposits and 15.3% in funds.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["GFBanamex 2Q26 report", Q2], ["Integrated Annual Report 2025", AR25]]),
            P("cib", "Corporate & Investment Banking", "Financing, capital markets and advisory under René Pimentel (appointed 2026), plus treasury, FX and derivatives.",
              s=["corp"], lc="borrow", st="new", ay="2026", neo=[0, ""], src=[["GFBanamex 2Q26 report", Q2], ["Integrated Annual Report 2025", AR25]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Wealth & private banking", "blurb": "Ps 2.45tn under management.", "div": "wealth", "rev": "consumer", "products": [
            P("wealth", "Wealth Management & Private Banking", "Advice and portfolios for wealthy clients with a BlackRock partnership; Ps 698 billion in funds sold through the bank (2025) and 24/7 scheduled fund trades.",
              s=["aff"], lc="grow", o="P", at="BlackRock", neo=[0, ""], src=[["Integrated Annual Report 2025", AR25], ["GFBanamex 2Q26 report", Q2]]),
        ]},
        {"id": "4.5", "ic": "shield-check", "name": "Insurance & pensions", "blurb": "Second in life insurance.", "div": "seguros", "rev": "insurance", "products": [
            P("seguros", "Seguros Banamex", "Mexico's second-largest life insurer: Plan Patrimonial reserves of Ps 205 billion, life and accident cover sold in the app, and Chubb travel insurance.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["Integrated Annual Report 2025", AR25]]),
            P("pensiones", "Pensiones Banamex", "Annuities from IMSS social-security pensions, started in the second half of 2025.",
              s=["saver"], lc="grow", st="new", ay="2025", neo=[0, ""], src=[["Integrated Annual Report 2025", AR25]]),
        ]},
        {"id": "4.6", "ic": "coins", "name": "Afore Banamex", "blurb": "Ps 1.3tn, fourth.", "div": "afore", "rev": "afore", "products": [
            P("afore", "Afore Banamex", "Fourth-largest retirement fund manager, Ps 1.29 trillion (+22% in 2025) for more than 8 million customers, with the Afore Móvil app; Marcelo Santos became CEO in 2026.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["Integrated Annual Report 2025", AR25], ["GFBanamex 2Q26 report", Q2]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Banamex: the app and BancaNet for 9.4 million digital customers, 1,261 branches, 9,112 ATMs and 13,152 correspondents, WhatsApp and phone, and partners from Costco to state governments.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "App, BancaNet & chat", "blurb": "9.4 million digital customers.", "div": "bank", "rev": "consumer", "products": [
            P("app", "Banamex app & BancaNet", "9.4 million digital customers at December 2025, more than 210 million app log-ins a month, and over 63.8% of sales made digitally.",
              s=["con", "young"], lc="everyday", neo=[0, ""], src=[["Integrated Annual Report 2025", AR25]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "1,261 branches, 9,112 ATMs.", "div": "bank", "rev": "consumer", "products": [
            P("branches", "Branches, ATMs & correspondents", "1,261 branches, 9,112 ATMs and 13,152 correspondents (1Q26), the country's widest network by Banamex's account.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["Banamex press release, Jul 2026", DESCH], ["Integrated Annual Report 2025", AR25]]),
            P("whatsapp", "Banamex WhatsApp & Audiomático", "A WhatsApp channel launched in 2025, web chat, and Audiomático phone banking around the clock.",
              s=["con"], lc="everyday", st="new", neo=[0, ""], src=[["Integrated Annual Report 2025", AR25]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners & payroll", "blurb": "Employers, retailers, states.", "div": "gfb", "rev": "commercial", "products": [
            P("partners", "Payroll, retail & state partners", "Payroll agreements that bring employees into accounts, retail partners (Costco, The Home Depot, La Comer, LineUp) and SME agreements with states and municipalities.",
              s=["sme", "corp"], lc="open", o="P", neo=[1, "Card partners split across networks."], src=[["Integrated Annual Report 2025", AR25]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Banamex", "blurb": "Ten of fourteen credit cards.", "products": [
        P("mcatbanamex", "Mastercard at Banamex", "Mastercard carries ten of the fourteen credit cards on sale, including the whole own-brand range and the 2025 La Comer launch, plus Priority and, by the evidence of its offers, everyday debit ⚠; it backed Pago Shops for Banamex SMEs in 2025. Visa holds the top Beyond card and the Costco, LineUp and Affinity co-brands. No network agreement has been published ⚠.",
          s=["con"], div="gfb", rev="group", mc="The relationship this map is drawn for.",
          src=[["Banamex: credit cards", PLATINUM], ["Banamex: Costco", COSTCO], ["Mastercard: Pago Shops, Jul 2025", PAGOSHOPS]]),
    ]},
    {"id": "pillar-market", "name": "Mexican banking", "blurb": "IPO, SPEI, slower profits.", "products": [
        P("market", "The Mexican market", "Banamex is fourth by assets, second in cards (24%) and fifth in SME lending. Bank profits fell 5.4% in real terms in H1 2026 ⚠; SPEI and CoDi carry instant payments; Mexico has about 5 million card terminals, 70% mobile.",
          s=["con"], div="gfb", rev="group", src=[["Integrated Annual Report 2025", AR25], ["ABM digest, Aug 2026", ABM], ["The Paypers, Jul 2025", GPREN]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
