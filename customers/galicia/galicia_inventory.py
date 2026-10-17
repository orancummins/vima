"""Grupo Financiero Galicia's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the Q2 2026 results (25 August 2026), the Q4 2025
results (5 March 2026) and the 2025 annual report on Form 20-F (16 April 2026), in constant pesos of June 2026
(IAS 29). ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides
wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://www.sec.gov/Archives/edgar/data/1114700/000111470026000073/grupogaliciapressrelease.htm"
Q4 = "https://www.sec.gov/Archives/edgar/data/1114700/000111470026000023/grupogaliciapressrelease.htm"
F20 = "https://www.sec.gov/Archives/edgar/data/1114700/000111470026000038/ggal-20251231.htm"
CLASS = "https://www.sec.gov/Archives/edgar/data/1114700/000111470026000083/a09142026-bgbaclassactionl.htm"
DIVID = "https://www.sec.gov/Archives/edgar/data/1114700/000111470026000077/a09022026-noticeofpaymento.htm"
MCAP = "https://stockanalysis.com/stocks/ggal/market-cap/"
RENEW = "https://www.ambito.com/negocios/inclusion-financiera/naranja-x-renueva-sus-mas-10-millones-tarjetas-y-revela-que-gastan-sus-clientes-n5547677"
GARMIN = "https://infonegocios.info/amp/infotecnologia/pagar-con-el-celu-no-pagar-con-el-reloj-garmin"
MEXICO = "https://www.dedinero.com.mx/consumo/naranja-x-busca-conquistar-mexico-con-su-tarjeta-de-credito-conoce-beneficios-costos-y-requisitos/"
WIKI = "https://en.wikipedia.org/wiki/Naranja_X"
MIGRATE = "https://www.ambito.com/negocios/integracion-banco-galicia-galicia-mas-que-cambia-los-clientes-y-cuando-podran-volver-operar-n6158517"
GWALLET = "https://www.sirchandler.com.ar/2025/02/las-tarjetas-de-naranjax-visa-o-master-llegaron-a-google-wallet/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · families · brands", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: about 16% of Argentina's private-sector loans and deposits, a bank founded in 1905 and still controlled by its founding families, HSBC Argentina absorbed in 2025, and delinquency rising as the economy adjusts.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "ROE 11.3% in Q2 2026.", "div": "gfg", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Net income of Ps.258 billion in Q2 2026 (ROE 11.3%), against Ps.196 billion for all of 2025 (ROE 2.5%); assets of Ps.50.4 trillion, deposits of Ps.29.0 trillion and a capital ratio of 23.7% at 30 June 2026; market value about US$6.2 billion (16 October 2026).",
              s=["corp"], neo=[0, ""], src=[["Q2 2026 results", Q2], ["Q4 2025 results", Q4], ["StockAnalysis: market cap, Oct 2026", MCAP]]),
            P("risk", "Asset quality", "Group NPL ratio of 10.6% at 30 June 2026, against 5.5% a year earlier, with cost of risk at 10.7%; Naranja X's NPL ratio reached 19.7%. Inflation slowed to 6.8% for the quarter.",
              s=["nx", "con"], st="flux", neo=[0, ""],
              mc="Credit and fraud risk tools have an obvious use here.",
              src=[["Q2 2026 results", Q2]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Escasany, Kon, Rivas.", "div": "gfg", "rev": "group", "products": [
            P("leadership", "Board & executives", "Chair Eduardo Escasany, group CEO Fabián Kon, CFO Gonzalo Fernández Covaro; Diego Rivas has run Banco Galicia since September 2025 and Pablo Caputto runs Naranja X. The Escasany, Ayerza and Braun families formed the holding company in 1999.",
              s=["corp"], neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brands", "blurb": "Galicia 1905, Naranja 1985.", "div": "gfg", "rev": "group", "products": [
            P("brands", "Brands", "Banco Galicia (1905), the largest private bank by deposits after state-owned Banco Nación; Naranja (Córdoba, 1985), now Naranja X; Galicia Seguros (1996); Fondos Fima (1958). Listed on BYMA and Nasdaq as GGAL.",
              s=["con"], o="I", neo=[0, ""], src=[["Form 20-F 2025", F20], ["Wikipedia: Naranja X", WIKI]]),
            P("galiciamas", "Galicia Más (ex HSBC Argentina)", "HSBC's Argentine bank, asset manager and insurer, bought on 6 December 2024 (101 branches, 2,843 staff), run as Galicia Más and merged into Banco Galicia on 23 June 2025, when more than 1.5 million cards moved across. Price about US$550 million ⚠.",
              s=["con", "prem"], o="A", ay="Dec 2024", neo=[1, "Its cards appear to have joined Galicia's Mastercard book ⚠."],
              mc="Galicia's Mastercard credit book doubled in 2025 as the HSBC cards came over ⚠.",
              src=[["Form 20-F 2025", F20], ["Q4 2025 results", Q4], ["Ámbito: Galicia Más integration, Jun 2025 ⚠", MIGRATE]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Gen-AI agents, agile tribes.", "div": "galicia", "rev": "bank", "products": [
            P("tech", "Technology, data & AI", "An agile 'tribes' model since 2020, machine-learning models in credit and operations, the first generative-AI agents on help sites, Guru for staff knowledge, Genesys contact centres, and Galicia Seguros' gen-AI assistant Laia.",
              s=["corp"], neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Integrate, cut costs, expand.", "div": "gfg", "rev": "group", "products": [
            P("strategy", "Strategy", "Customer experience and digital transformation, the HSBC integration finished in 2025, and expenses down 15% year on year at the bank in Q2 2026. No numeric medium-term targets published ⚠.",
              s=["corp"], neo=[0, ""], src=[["Q2 2026 results", Q2], ["Q4 2025 results", Q4]]),
            P("deals", "Deals", "HSBC Argentina (2024), the Nera agri joint venture with Santander (completed December 2025), Inviu's Peruvian broker licence (2025), Galicia Ventures Corp (October 2025), and Naranja X's application for a Mexican banking licence (February 2026 ⚠).",
              s=["corp"], o="A", st="new", neo=[0, ""], src=[["Form 20-F 2025", F20], ["DeDinero: Naranja X in Mexico, Jun 2026", MEXICO]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: 15 million credit cards split between Visa, Mastercard, Amex and Naranja's own brand, Visa debit, the Galicia App and MODO, Nave and Naranja X acquiring, and a Mastercard card in Mexico.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Galicia credit cards", "blurb": "6.1m: Visa, Mastercard, Amex.", "div": "galicia", "rev": "bank", "products": [
            P("gcredit", "Galicia credit cards", "6,100,603 cards at end-2025: Visa 3.01 million, Mastercard 2.46 million (up 101% in 2025 as the HSBC cards came over ⚠) and American Express 0.63 million; 622,683 issued in 2025.", short="Galicia credit (Visa, Mastercard, Amex)",
              s=["con", "prem"], lc="borrow", o="P", at="Visa, Mastercard, American Express", neo=[1, "Mastercard 40% of the bank's cards; Visa 49%."],
              mc="Mastercard is close to level with Visa at the bank.",
              src=[["Form 20-F 2025", F20]]),
            P("eminent", "Éminent Black & Platinum", "The premium tier, 17.2% of retail clients, with Mastercard Black (380,427 cards), Visa Signature (876,698) and Amex Platinum and Signature, plus dedicated Éminent officers. Galicia Mastercard cards paid through Garmin watches first in Argentina (February 2020).",
              s=["prem"], lc="everyday", o="P", at="Mastercard, Visa, American Express", neo=[1, "Mastercard Black beside Visa Signature and Amex."],
              src=[["Form 20-F 2025", F20], ["InfoNegocios: Galicia Mastercard on Garmin, Feb 2020", GARMIN]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Naranja X cards", "blurb": "8.9m, a third own-brand.", "div": "naranjax", "rev": "naranja", "products": [
            P("nxcredit", "Naranja X Visa & Mastercard", "Visa 2.97 million and Mastercard 1.13 million cards at end-2025; Mastercard up 253% in 2024 and Amex wound down (68 cards left). The 2022 renewal of more than 10 million cards was done with Mastercard as technology provider.", short="Naranja X Visa & Mastercard",
              s=["nx"], lc="borrow", o="P", at="Visa, Mastercard", neo=[1, "Mastercard about 28% of Naranja X's networked cards."],
              mc="Mastercard is the fast-growing second network at Naranja X.",
              src=[["Form 20-F 2025", F20], ["Ámbito: Naranja X card renewal, Sep 2022", RENEW]]),
            P("naranjabrand", "Naranja own-brand card", "4.80 million cards on Naranja's own closed-loop brand at end-2025, down 11% in the year; Naranja X has 3.97 million active credit customers in all.",
              s=["nx"], lc="borrow", o="I", st="flux", neo=[0, "Own brand, no network."],
              mc="The largest block of cards in the group with no network at all.",
              src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "Debit", "blurb": "Visa at Naranja X.", "div": "gfg", "rev": "bank", "products": [
            P("gdebit", "Galicia debit card", "The Galicia debit card for 11.7 million deposit accounts: dual-currency purchases from peso or dollar accounts, debit payments on any QR code, and Banelco ATMs. Network not confirmed, believed Visa ⚠.",
              s=["con"], lc="everyday", neo=[None, "Network unconfirmed, believed Visa ⚠."], src=[["Form 20-F 2025", F20], ["Q2 2026 results", Q2]]),
            P("nxdebit", "Naranja X Visa debit", "A Visa debit card launched with the 2022 renewal; 6.2 million physical debit cards issued and 8.6 million active account users by 2025, with Visa Click to Pay certified in 2025.",
              s=["nx"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Ámbito: Naranja X card renewal, Sep 2022", RENEW], ["Form 20-F 2025", F20]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Wallets & QR", "blurb": "MODO, QR, contactless.", "div": "galicia", "rev": "bank", "products": [
            P("galiciawallet", "Galicia App wallet", "Send money to phone contacts, pay by QR (interoperable and in instalments without a card), and pay contactless with Apple Pay, Android and watches; NFC transit payments rose 726% in 2025. Naranja X added Google Pay and card-on-file tokenisation in 2025.",
              s=["con", "nx"], lc="move", o="B", neo=[1, "Card tokens ride every network."], src=[["Form 20-F 2025", F20], ["Sir Chandler: Naranja X in Google Wallet, Feb 2025 ⚠", GWALLET]]),
            P("modo", "MODO", "The bank-owned payments app set up by more than 30 Argentine banks through Play Digital (2020); Banco Galicia owns 19.79%.",
              s=["con"], lc="move", o="P", at="Play Digital", neo=[0, "Bank-account rails."], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acquiring", "blurb": "Nave: 61,000 merchants.", "div": "nave", "rev": "bank", "products": [
            P("nave", "Nave", "Banco Galicia's merchant platform since 2022: 61,498 active merchants, 39,761 terminals, Ps.2.6 trillion and 91 million transactions in 2025, card-free instalments, and one view of sales across processors, Mercado Pago and Naranja X.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["Form 20-F 2025", F20]]),
            P("nxaccept", "Naranja X acceptance", "The Toque card reader, TAP tap-to-phone for Visa and Mastercard, payment links and QR, QR PIX for Brazilian tourists, and Naranja X Negocios (2025); small merchants now process through Nave.",
              s=["sme"], lc="move", o="B", st="new", neo=[1, "Visa and Mastercard on TAP."], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "2.6", "ic": "earth", "name": "Cross-border & Mexico", "blurb": "A Mastercard card in Mexico.", "div": "naranjax", "rev": "naranja", "products": [
            P("intl", "International transfers", "24/7 international transfers in the Galicia App since March 2025, at the CCL exchange rate and within an annual limit; foreign-trade services for companies.",
              s=["con", "corp"], lc="move", st="new", ay="Mar 2025", neo=[None, "Provider not public."], src=[["Form 20-F 2025", F20]]),
            P("mexico", "Naranja X Mexico", "A no-fee Naranja X credit card in Mexico on Mastercard, sold through the app, while a banking licence application to the CNBV (February 2026 ⚠) is pending.",
              s=["nx"], lc="borrow", st="new", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="The group's first issuing outside Argentina rides on Mastercard.",
              src=[["DeDinero: Naranja X in Mexico, Jun 2026", MEXICO]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: tokens and biometrics, cards issued without printed data using Mastercard, generative-AI assistants, and Quiero! points and network-branded experiences.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "Token, biometrics, Infoless.", "div": "gfg", "rev": "bank", "products": [
            P("security", "Security & authentication", "Galicia Token, facial biometrics for transfers and loans, tokenised card-on-file payments, and cybersecurity campaigns; no fraud-scoring vendor named ⚠.",
              s=["con", "nx"], lc="everyday", neo=[None, "No vendor public."],
              mc="No public fraud or identity partner, with NPLs of 10–20%.",
              src=[["Form 20-F 2025", F20]]),
            P("infoless", "Infoless cards", "Naranja X launched Infoless with Mastercard in 2025: cards without printed data, delivery cut from 5 days to 1.3, and 11% of virtual cards activated.",
              s=["nx"], lc="open", st="new", ay="2025", o="P", at="Mastercard", neo=[2, "Built with Mastercard."], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "Data & AI", "blurb": "Gen-AI agents, Laia.", "div": "galicia", "rev": "bank", "products": [
            P("ai", "AI assistants", "Generative-AI agents on help channels, the Guru knowledge tool for officers, and Laia, Galicia Seguros' gen-AI assistant for sales, claims and fraud prevention.",
              s=["con"], lc="everyday", st="new", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty & benefits", "blurb": "Quiero! points.", "div": "galicia", "rev": "bank", "products": [
            P("quiero", "Quiero! & benefits", "Quiero! points (licensed to Naranja X since 2019), a benefits platform of discounts and instalments, Naranja X cashback, and the former HSBC Rewards points, now subject to a consumer class action (September 2026).",
              s=["con", "nx"], lc="grow", st="flux", neo=[0, ""],
              mc="Card-linked offers could feed Quiero! and the benefits platform.",
              src=[["Form 20-F 2025", F20], ["Rewards class action, Sep 2026", CLASS]]),
            P("experiences", "Network experiences", "Events by card brand for premium clients: Amex Food & Wine, Visa Signature golf, and padel tournaments and clinics for Mastercard clients (2025).",
              s=["prem"], lc="beyond", o="P", at="Visa, Mastercard, American Express", neo=[1, "One of three networks."], src=[["Form 20-F 2025", F20]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: retail banking for 4.6 million people, Naranja X credit for the underbanked, business, agri and wholesale banking, insurance, and the country's largest fund manager by share.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Retail banking", "blurb": "4.6m individuals.", "div": "galicia", "rev": "bank", "products": [
            P("retail", "Accounts & lending", "4.63 million individual clients across Personas, MOVE, Plus and Éminent; Ps.4.8 trillion of card loans, Ps.2.2 trillion of personal loans and Ps.1.1 trillion of mortgages, with inflation-indexed (UVA) loans up 56% in a year.",
              s=["con", "prem"], lc="everyday", neo=[0, ""], src=[["Form 20-F 2025", F20], ["Q2 2026 results", Q2]]),
        ]},
        {"id": "4.2", "ic": "hand-coins", "name": "Naranja X finance", "blurb": "Loans for the underbanked.", "div": "naranjax", "rev": "naranja", "products": [
            P("nxloans", "Naranja X credit & savings", "6.9 million loans granted in 2025, a 4.8% share of personal loans and 6.3% of savings accounts; ROE of 12.2% in Q2 2026 after a loss in Q1.",
              s=["nx"], lc="borrow", neo=[0, ""], src=[["Form 20-F 2025", F20], ["Q2 2026 results", Q2]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "SME & agri", "blurb": "Nera with Santander.", "div": "galicia", "rev": "bank", "products": [
            P("sme", "Business & SME banking", "Accounts, overdrafts, cheques, a coupon advance on Visa, Mastercard, Cabal and Amex receivables, and a credit line for women-led SMEs (April 2026).",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["Form 20-F 2025", F20], ["Q2 2026 results", Q2]]),
            P("commercial", "Business & corporate cards", "177,797 Visa Business cards at end-2025; corporate-card management unified in 2025, with limits and payments in Office Banking.",
              s=["sme", "corp"], lc="everyday", o="P", at="Visa", neo=[0, "Visa Business; corporate network not stated ⚠."],
              mc="Commercial cards are on Visa.",
              src=[["Form 20-F 2025", F20]]),
            P("nera", "Galicia Rural & Nera", "24,637 agri clients, and Nera, an agri payments and finance ecosystem in Argentina, Paraguay and Uruguay, now a 50/50 joint venture with Banco Santander (December 2025).",
              s=["corp"], lc="borrow", st="new", o="P", at="Banco Santander", neo=[None, ""], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Wholesale & markets", "blurb": "43,000 companies.", "div": "galicia", "rev": "markets", "products": [
            P("wholesale", "Wholesale banking", "42,983 wholesale clients, export pre-financing up 48% in Q2 2026, and dollar lending up 74% in a year.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Form 20-F 2025", F20], ["Q2 2026 results", Q2]]),
            P("securities", "Galicia Securities & markets", "Broker-dealer and markets desk; Galicia ranked first in A3 Mercados futures volume in 2025.",
              s=["corp", "inv"], lc="grow", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "4.5", "ic": "shield-check", "name": "Insurance", "blurb": "2.7m policies.", "div": "seguros", "rev": "insurance", "products": [
            P("seguros", "Galicia Seguros", "2.7 million policies (life, home, accidents, theft, cars) sold through the bank, brokers and digital channels; ROE of 34.8% in Q2 2026.",
              s=["con", "nx"], lc="beyond", neo=[0, ""], src=[["Form 20-F 2025", F20], ["Q2 2026 results", Q2]]),
        ]},
        {"id": "4.6", "ic": "chart-candlestick", "name": "Funds & wealth", "blurb": "Fima: 14.5% share.", "div": "fima", "rev": "markets", "products": [
            P("fima", "Fondos Fima", "Ps.15.5 trillion of assets under management and a 14.5% market share at 30 June 2026; net income of Ps.38 billion in the quarter.",
              s=["inv"], lc="grow", neo=[0, ""], src=[["Q2 2026 results", Q2]]),
            P("inviu", "Inviu", "A digital platform for independent financial advisers in Argentina, Uruguay and, from 2025, Peru.",
              s=["inv"], lc="grow", o="A", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the Galicia App and Office Banking, the Naranja X app that signs up every new customer, 367 branches, and advisers and partners.",
    "tiles": [
        {"id": "5.1", "ic": "monitor", "name": "Galicia digital", "blurb": "93% digital clients.", "div": "galicia", "rev": "bank", "products": [
            P("gapp", "Galicia App & Online Banking", "93% of Galicia clients are digital; Online Banking averages 8.1 million log-ins a month; the app carries payments, loans, investments and insurance.",
              s=["con", "prem"], lc="everyday", neo=[0, ""], src=[["Q2 2026 results", Q2], ["Form 20-F 2025", F20]]),
            P("office", "Office Banking & business app", "Office Banking for companies (7.0 million log-ins a month) and a new Galicia Office App (2025) with biometric log-in.",
              s=["sme", "corp"], lc="everyday", st="new", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "5.2", "ic": "smartphone", "name": "Naranja X app", "blurb": "57,700 joiners a month.", "div": "naranjax", "rev": "naranja", "products": [
            P("nxapp", "Naranja X app", "Every new Naranja X customer, about 57,700 a month, joins through the app and gets a virtual card at once; 75% of clients are digital.",
              s=["nx"], lc="open", neo=[0, ""], src=[["Form 20-F 2025", F20], ["Q2 2026 results", Q2]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & ATMs", "blurb": "367 points.", "div": "gfg", "rev": "bank", "products": [
            P("branches", "Branches & self-service", "277 Galicia and 90 Naranja X branches and points of sale at 30 June 2026, down from 432 group points at end-2025 after the merger; self-service terminals and Banelco ATMs.",
              s=["con", "nx"], lc="everyday", st="flux", neo=[0, ""], src=[["Q2 2026 results", Q2], ["Q4 2025 results", Q4]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Advisers & partners", "blurb": "Conecta, dealers, MODO.", "div": "galicia", "rev": "bank", "products": [
            P("conecta", "Galicia Conecta", "Remote advisers by WhatsApp and email for Éminent and SME clients.",
              s=["prem", "sme"], lc="everyday", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
            P("partners", "Partners & embedded lending", "Loans offered at partners' points of sale and websites and confirmed in the Galicia App, car dealers and auto-parts suppliers, Tienda Nube through Nave, and Inviu's advisers.",
              s=["con", "sme"], lc="borrow", o="P", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Galicia", "blurb": "3.6 million cards, second to Visa.", "products": [
        P("mcatgalicia", "Mastercard at Galicia", "Mastercard carries 3.58 million of the group's 15.0 million credit cards (24%) against Visa's 5.98 million (40%) and Naranja's own 4.80 million (32%). It is close to level with Visa at Banco Galicia after the HSBC cards came over, grows fast at Naranja X, was the technology provider for its 2022 card renewal and Infoless cards, and carries Naranja X in Mexico. Debit is Visa at Naranja X and believed Visa at Galicia ⚠; no network agreement is public.",
          s=["con"], div="gfg", rev="group", mc="The relationship this map is drawn for.",
          src=[["Form 20-F 2025", F20], ["Ámbito: Naranja X card renewal, Sep 2022", RENEW]]),
    ]},
    {"id": "pillar-market", "name": "Argentine banking", "blurb": "Disinflation, arrears, wallets.", "products": [
        P("market", "The Argentine market", "Inflation falling (6.8% in Q2 2026) as delinquency rises, hyperinflation accounting, Banco Nación first by deposits and Galicia second, competition from digital banks and wallets such as Mercado Pago, the banks' MODO and interoperable QR payments, and consumer class actions under the Credit Card Law.",
          s=["con"], div="gfg", rev="group", src=[["Form 20-F 2025", F20], ["Q2 2026 results", Q2]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
