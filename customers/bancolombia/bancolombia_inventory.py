"""Bancolombia's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Bancolombia S.A. is the Colombian bank; Grupo Cibest S.A. (formerly Grupo Bancolombia, renamed May 2025) is the
listed holding company and is used as context. Figures are the group's own as reported in the Colombian financial
press: the Q2 2026 results (10 August 2026) and the 2025 results (23 February 2026). ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q226 = "https://www.valoraanalitik.com/utilidad-grupo-cibest-2t-2026/"
FY25 = "https://www.valoraanalitik.com/?p=556642"
FY25B = "https://www.larepublica.co/finanzas/grupo-cibest-reporto-utilidad-anual-de-3-8-billones-en-2025-con-una-caida-de-38-4334220"
PLAN = "https://www.valoraanalitik.com/?p=568376"
CIBEST = "https://www.grupocibest.com/"
GOV = "https://www.grupocibest.com/corporativo/gobierno-corporativo/junta-directiva-alta-gerencia"
F20 = "https://www.barchart.com/story/news/1208044/grupo-cibest-s-a-announces-filing-of-the-2025-annual-report-on-form-20-f"
BANISTMO = "https://www.bloomberglinea.com/latinoamerica/colombia/grupo-cibest-vendera-banistmo-en-panama-a-inversiones-cuscatlan-por-us1418-millones/"
BANISTMO2 = "https://lexlatin.com/noticias/grupo-cibest-vende-banitsmo-grupo-bsc-usd-1418-millones"
DIVIDEND = "https://www.portafolio.co/negocios/empresas/cibest-matriz-de-bancolombia-repartira-1-2-billones-entre-sus-accionistas-tras-la-venta-de-banistmo-501208"
CARDS = "https://www.larepublica.co/finanzas/bancolombia-falabella-y-davivienda-son-los-reyes-de-las-tarjetas-de-credito-activas-4437271"
CCPAGE = "https://www.bancolombia.com/personas/tarjetas-de-credito"
DCPAGE = "https://www.bancolombia.com/personas/tarjetas-debito"
MAESTRO = "https://www.bancolombia.com/centro-de-ayuda/preguntas-frecuentes/pedir-tarjeta-debito-nueva"
LEGEND = "https://www.larepublica.co/finanzas/bancolombia-sera-el-primer-banco-en-ofrecer-la-world-legend-dentro-de-su-portafolio-4400003"
LEGEND2 = "https://www.valoraanalitik.com/mastercard-colombia-tarjeta-alto-valor/"
VISATAP = "https://www.larepublica.co/finanzas/bancolombia-y-visa-lanzan-convenio-para-agregar-tarjetas-a-los-dispositivos-mas-facil-4047209"
LIFEMILES = "https://www.publimetro.co/comercial/2025/09/12/bancolombia-lifemiles-y-visa-lanzan-nueva-tarjeta-con-beneficios-exclusivos-para-viajeros/"
NEQUIVISA = "https://www.pulzo.com/economia/nequi-beneficio-usuarios-con-nueva-tarjeta-visa-para-pagar-contacto-PP4001052"
NEQUIDIG = "https://www.portafolio.co/economia/finanzas/nequi-lanza-una-tarjeta-digital-para-compras-en-linea-522643"
NEQUISV = "https://diario.elmundo.sv/economia/nequi-una-de-las-aplicaciones-populares-de-colombia-llega-a-el-salvador"
NEQUICF = "https://www.portafolio.co/economia/finanzas/nequi-superfinanciera-la-autorizo-a-ser-compania-de-financiamiento-568967"
NEQUICEO = "https://www.larepublica.co/finanzas/entrevista-con-andres-vasquez-ceo-de-nequi-quien-hablo-del-enfoque-en-credito-de-la-compania-4469641"
BREB = "https://www.elpais.com.co/economia/en-su-primer-ano-bre-b-mueve-262-billones-y-alcanza-116-millones-de-llaves-en-colombia-0604.html"
QRBREB = "https://www.elpais.com.co/economia/bancolombia-integro-sus-codigos-qr-a-bre-b-para-pagos-inmediatos-entre-bancos-asi-funciona-la-medida-0730.html"
WOMPI = "https://www.portafolio.co/tecnologia/wompi-crea-aplicacion-que-permite-usar-celulares-como-datafonos-596812"
WOMPIQR = "https://cambiocolombia.com/peso-a-peso-paso-a-paso/articulo/2026/9/wompi-amplia-los-pagos-sin-contacto-y-baja-al-uno-por-ciento-la-tarifa-de-los-pagos-con-qr"
WENIA = "https://cointelegraph.com/news/bancolombia-group-wenia-crypto-exchange-copw-stablecoin"
WENIAPOR = "https://criptonoticias.com/finanzas/stablecoin-peso-colombiano-chainlink-bancolombia-reservas"
TECH = "https://impactotic.co/innovacion/transformacion-digital/alvaro-carmona-trabajar-en-bancolombia-es-como-trabajar-en-50-startups-simultaneamente/"
TECHREV = "https://www.technologyreview.com/2026/05/01/1138032/innovation-talk-with-bancolombia/"
MCAGENT = "https://forbes.co/2026/02/24/negocios/mastercard-se-prepara-para-abordar-los-pagos-agenticos-hechos-por-la-ia"
GUAJIRA = "https://www.larepublica.co/responsabilidad-social/alianza-de-bancolombia-y-mastercard-en-la-guajira-supero-su-meta-inicial-2565603"
STAFF = "https://stockanalysis.com/stocks/cib"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · holding · technology", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: COP 363 trillion of assets and a Q2 2026 ROE of 28.7%, a new holding company, Grupo Cibest, that sold Banistmo and spun Nequi into its own licence, and a cloud and AI programme with COP 1.6 trillion behind it.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "COP 363trn of assets, ROE 28.7%.", "div": "cibest", "rev": "colombia", "products": [
            P("balance", "Balance sheet & earnings", "Grupo Cibest had assets of COP 363 trillion, gross loans of COP 262 trillion and equity of COP 38 trillion at 30 June 2026; Q2 2026 net income was COP 2.7 trillion (annualised ROE 28.73%) and H1 COP 4.2 trillion. In 2025 profit fell to COP 3.8 trillion after a COP 3.4 trillion Banistmo impairment. Deposits, capital ratios and ratings were not captured ⚠.",
              s=["con"], neo=[0, ""], src=[["Valora Analitik: Q2 2026 results, Aug 2026", Q226], ["Valora Analitik: 2025 results, Feb 2026", FY25], ["La República: 2025 results", FY25B]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Mora and Restrepo.", "div": "cibest", "rev": "colombia", "products": [
            P("leadership", "Board & senior management", "Juan Carlos Mora Uribe is President of Grupo Cibest; Mauricio Rosillo runs business, Mauricio Botero strategy and finance, Rodrigo Prieto risk; Luis Fernando Restrepo chairs the board, which includes a cyber-security expert. No separate CEO of Bancolombia S.A. was found ⚠.",
              s=["corp"], neo=[0, ""], src=[["Grupo Cibest: board and senior management", GOV]]),
        ]},
        {"id": "1.3", "ic": "building-2", "name": "Group structure", "blurb": "Cibest, Banistmo sold.", "div": "cibest", "rev": "camerica", "products": [
            P("structure", "Grupo Cibest", "A holding company created in May 2025 as Bancolombia's sole shareholder, listed in Bogotá and on the NYSE (CIB); it also owns Banco Agrícola, BAM, Nequi, Wompi, Wenia, Sufi and Renting Colombia, and about 34,000 staff ⚠.",
              s=["corp"], st="new", ay="May 2025", neo=[0, ""], src=[["Valora Analitik: Cibest plans to 2027", PLAN], ["Grupo Cibest", CIBEST], ["Grupo Cibest 2025 Form 20-F", F20], ["Stock Analysis: CIB", STAFF]]),
            P("deals", "Banistmo sale & Nequi licence", "Banistmo (Panama) sold to Inversiones Cuscatlán for US$1,418 million, agreed 18 December 2025 and closed 30 June 2026, with an extraordinary COP 1.2 trillion dividend; Nequi became a separately licensed finance company on 1 September 2026.",
              s=["corp", "ca"], st="flux", ay="Jun 2026", o="A", neo=[0, ""], src=[["Bloomberg Línea: Banistmo sale, Dec 2025", BANISTMO], ["LexLatin: Banistmo sale", BANISTMO2], ["Portafolio: extraordinary dividend", DIVIDEND], ["Portafolio: Nequi licence", NEQUICF]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "75% of apps in the cloud.", "div": "bancolombia", "rev": "colombia", "products": [
            P("tech", "Cloud, data & AI", "Three-quarters of the bank's applications moved to the cloud, nine in ten interactions digital, an 'AI para todos' programme, and large language models used in credit approval and offer design (December 2025).",
              s=["corp"], o="B", neo=[0, ""], src=[["ImpactoTIC: Álvaro Carmona, Dec 2025", TECH], ["MIT Technology Review: Bancolombia, May 2026", TECHREV]]),
            P("continuity", "Service continuity", "About COP 1.6 trillion of 2026 investment in technology and in serving clients during a contingency, one of the group's four priorities for the year.",
              s=["con", "sme"], st="new", neo=[None, "No vendor named."],
              mc="Resilience spending is where processing and stand-in services could fit ⚠.",
              src=[["Valora Analitik: Cibest plans to 2027", PLAN]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & capital", "blurb": "Latin America after 2026.", "div": "cibest", "rev": "colombia", "products": [
            P("strategy", "Plans to 2027", "In 2026: sell Banistmo, separate Nequi, build the Central American banks and invest in technology; from 2027, look for investments across Latin America, including taking Nequi, Wenia and Wompi abroad ⚠.",
              s=["corp"], st="new", neo=[0, ""], src=[["Valora Analitik: Cibest plans to 2027", PLAN], ["La República: Nequi CEO, Aug 2026", NEQUICEO]]),
            P("capital", "Dividends & buybacks", "A 2025 dividend of COP 4,512 a share paid in four quarterly instalments through 29 December 2026, and a buyback (COP 1.3 trillion in phase one, a three-year phase two).",
              s=["corp"], neo=[0, ""], src=[["Valora Analitik: 2025 results, Feb 2026", FY25], ["Valora Analitik: Cibest plans to 2027", PLAN]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: debit cards that are all Mastercard, Colombia's largest credit-card book across Mastercard, Visa and Amex, wallets and tokens, Nequi's cards, the Bancolombia QR on the new Bre-B instant rail, Wompi acceptance, and Wenia's peso stablecoin.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "All Mastercard.", "div": "bancolombia", "rev": "colombia", "products": [
            P("debit", "Bancolombia debit cards", "Six debit cards (Clásica, Preferencial, Black, Banconautas for under-13s, Virtual and Transporte) are all Mastercard; Maestro cards are swapped to Mastercard debit free the first time; contactless without a PIN up to COP 250,000.", short="Debit (Mastercard)",
              s=["con", "prem"], lc="everyday", o="P", at="Mastercard", neo=[2, "All Mastercard."],
              mc="The whole debit book is Mastercard's, and Bre-B is now competing with it at the till.",
              src=[["Bancolombia: debit cards", DCPAGE], ["Bancolombia: Maestro to Mastercard", MAESTRO]]),
            P("transit", "Mastercard Transporte", "A debit card that pays public transport in Barranquilla, Bogotá, Cali, Medellín and Pereira, with or without a prior top-up.",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Bancolombia: debit cards", DCPAGE]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "2.76m active, number one.", "div": "bancolombia", "rev": "colombia", "products": [
            P("credit", "Bancolombia credit cards", "Colombia's largest book: 2,760,578 active cards at 30 April 2026, 17.5% of the market; about 1.2 million Mastercard, 887,952 Visa and 572,931 American Express. 24 cards on sale: 11 Mastercard, 6 Visa, 7 Amex.", short="Credit (Mastercard, Visa, Amex)",
              s=["con", "prem"], lc="borrow", o="P", at="Mastercard, Visa, American Express", neo=[1, "About 45% Mastercard."],
              mc="Mastercard leads the book but holds well under half of it.",
              src=[["La República: active credit cards, Jul 2026", CARDS], ["Bancolombia: credit cards", CCPAGE]]),
            P("legend", "World Legend Mastercard", "Mastercard's top tier, above Black, launched in Colombia on 25 May 2026 with Bancolombia as the first issuer; roll-out June–July 2026, with a Taste by Priceless lounge planned at El Dorado.", short="World Legend (Mastercard)",
              s=["prem"], lc="borrow", st="new", ay="May 2026", o="P", at="Mastercard", neo=[2, "Mastercard's top tier."],
              mc="The newest joint product, aimed at the clients who drive consumer profit.",
              src=[["La República: World Legend, May 2026", LEGEND], ["Valora Analitik: World Legend in Colombia", LEGEND2]]),
            P("visaco", "Visa co-brands: LifeMiles & Selección", "Visa Avianca LifeMiles, a travel card launched in September 2025, and Visa Selección, tied to the national football team; with Visa Infinite at the top of the Visa range.",
              s=["con", "prem"], lc="borrow", ay="Sep 2025", o="P", at="Visa, Avianca LifeMiles", neo=[0, "Visa."], src=[["Publimetro: LifeMiles Visa, Sep 2025", LIFEMILES], ["Bancolombia: credit cards", CCPAGE]]),
            P("amex", "American Express cards", "Seven Amex cards issued by Bancolombia, from Libre (no fee) to a metal Platinum Card; 572,931 active in April 2026.",
              s=["prem"], lc="borrow", o="P", at="American Express", neo=[0, "American Express."], src=[["Bancolombia: credit cards", CCPAGE], ["La República: active credit cards, Jul 2026", CARDS]]),
        ]},
        {"id": "2.3", "ic": "smartphone", "name": "Wallets & tokens", "blurb": "Visa's Tap to Add first.", "div": "bancolombia", "rev": "colombia", "products": [
            P("wallets", "Apple Pay, Google Pay & Click to Pay", "Visa and Bancolombia launched Tap to Add Card for Apple Pay in January 2025, the first in the region; Bancolombia's Visa cards made more than 4 million wallet payments in 2024. The virtual Mastercard debit card goes into Apple, Google, Garmin and Fitbit wallets and Click to Pay.",
              s=["con"], lc="everyday", ay="Jan 2025", o="P", at="Visa, Mastercard, Apple, Google", neo=[1, "Both networks."],
              mc="Visa got the wallet headline; Mastercard's tokens sit under the debit book.",
              src=[["La República: Visa Tap to Add, Jan 2025", VISATAP], ["Bancolombia: debit cards", DCPAGE]]),
        ]},
        {"id": "2.4", "ic": "wallet", "name": "Nequi cards", "blurb": "Visa at home, Mastercard abroad.", "div": "nequi", "rev": "digital", "products": [
            P("nequicard", "Nequi Visa card (Colombia)", "A contactless debit card, physical and digital, for Nequi's 29 million clients (2024); an earlier Nequi digital card for online shopping was Mastercard ⚠.", short="Nequi card (Visa)",
              s=["nequi"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="Colombia's biggest wallet carries Visa.",
              src=[["Pulzo: Nequi Visa card, Oct 2024", NEQUIVISA], ["Portafolio: Nequi digital card", NEQUIDIG]]),
            P("nequisv", "Nequi El Salvador", "Launched in July 2024 through Banco Agrícola's Accelera unit, with remittances, QR payments and a digital Mastercard debit card.", short="Nequi El Salvador (Mastercard)",
              s=["ca"], lc="move", ay="Jul 2024", o="P", at="Mastercard", neo=[2, "Mastercard debit."],
              src=[["El Mundo: Nequi in El Salvador, Jul 2024", NEQUISV]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "QR & instant payments", "blurb": "Bancolombia QR on Bre-B.", "div": "bancolombia", "rev": "colombia", "products": [
            P("qr", "Bancolombia QR", "Open to payments from other banks since July 2023, when more than 3 million people a month paid with it; moved onto Bre-B keys in May 2026. Nequi and Bancolombia handled 88% of Bre-B merchant sales revenue in April 2026 (Bold data).",
              s=["con", "sme"], lc="move", st="new", ay="May 2026", o="B", neo=[0, "Account to account."],
              mc="The QR is the bank's own alternative to card acceptance.",
              src=[["El País: Bancolombia QR on Bre-B, May 2026", QRBREB]]),
            P("breb", "Bre-B transfers", "Banco de la República's instant system, about a year old: 116 million keys, 36 million clients and COP 262 trillion moved in its first year to 4 October 2026. Bancolombia's own volumes are not published ⚠.",
              s=["con", "nequi", "sme"], lc="move", st="new", o="P", at="Banco de la República", neo=[0, "Account to account."],
              mc="Bre-B is the main threat to debit at merchants, and a place for scam scoring.",
              src=[["El País: Bre-B's first year, Oct 2026", BREB]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acceptance", "blurb": "Wompi, 83,000 businesses.", "div": "wompi", "rev": "digital", "products": [
            P("wompi", "Wompi", "Payment gateway, in-person payments and payouts for more than 83,000 businesses (2026); a Tap to Phone app since January 2024 accepting cards, Nequi and the Bancolombia QR; the QR fee cut to 1% in September 2026 ⚠.",
              s=["sme"], lc="move", o="B", at="Redeban", neo=[1, "Accepts every network."],
              src=[["Valora Analitik: Q2 2026 results, Aug 2026", Q226], ["Portafolio: Wompi Tap to Phone, Jan 2024", WOMPI], ["Cambio: Wompi QR fee, Sep 2026", WOMPIQR]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Digital assets", "blurb": "Wenia and COPW.", "div": "wenia", "rev": "digital", "products": [
            P("wenia", "Wenia & COPW", "A Bermuda-licensed crypto platform with COPW, a peso stablecoin on Polygon with Chainlink proof of reserve, funded through Nequi; more than 73,000 users in 2026.",
              s=["con"], lc="grow", st="new", o="B", at="Polygon, Chainlink", neo=[0, "The group's own."],
              mc="A bank-issued peso stablecoin that could settle on card or crypto rails.",
              src=[["Cointelegraph: Wenia and COPW", WENIA], ["CriptoNoticias: COPW reserves", WENIAPOR], ["Valora Analitik: Q2 2026 results, Aug 2026", Q226]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: the bank's own fraud models, AI that approves credit and plans to shop for customers, and Puntos Colombia and premium benefits on the cards.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "AI in fraud.", "div": "bancolombia", "rev": "colombia", "products": [
            P("fraud", "Fraud & cyber-security", "AI used in fraud management, and a board member chosen for cyber-security expertise. No fraud vendor is named in public sources ⚠.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, "Bancolombia's own."],
              mc="Bre-B's growth makes transfer scam scoring a live need.",
              src=[["ImpactoTIC: Álvaro Carmona, Dec 2025", TECH], ["Grupo Cibest: board and senior management", GOV]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & agents", "blurb": "LLMs approve credit.", "div": "bancolombia", "rev": "colombia", "products": [
            P("ai", "AI in credit & personalisation", "Large language models in credit approval and offer design, and offers tailored to each customer's life stage; Microsoft's CEO called Bancolombia the region's most advanced user of AI in software development (December 2025).",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["ImpactoTIC: Álvaro Carmona, Dec 2025", TECH]]),
            P("agents", "Automated purchasing agents", "Planned agents that buy on a customer's behalf, using AI with tokenised deposits and stablecoins; no launch date ⚠.",
              s=["con"], lc="everyday", st="unconf", o="B", neo=[None, "Network not named."],
              mc="Mastercard is pushing agentic payments in Colombia; Agent Pay fits this plan.",
              src=[["ImpactoTIC: Álvaro Carmona, Dec 2025", TECH], ["Forbes Colombia: Mastercard agentic payments, Feb 2026", MCAGENT]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & benefits", "blurb": "Puntos Colombia.", "div": "bancolombia", "rev": "colombia", "products": [
            P("points", "Puntos Colombia & card benefits", "Puntos Colombia is earned across the card range, with LifeMiles on the Visa co-brand and lounge access on premium cards; ownership of Puntos Colombia was not checked ⚠.",
              s=["con", "prem"], lc="grow", o="P", at="Puntos Colombia", neo=[1, "Earned on all three networks."],
              mc="Card-linked offers and Priceless could add to points.",
              src=[["Bancolombia: credit cards", CCPAGE]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: personal and premium banking with COP 217 trillion of loans in Colombia, business and corporate banking, Nequi's credit for people new to it, Sufi and Renting Colombia for vehicles, and banks in El Salvador and Guatemala.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Personal & premium", "blurb": "16m+ clients.", "div": "bancolombia", "rev": "colombia", "products": [
            P("personal", "Personal banking & loans", "More than 16 million people and businesses served in Colombia, with Bancolombia's loans at COP 217 trillion (up 9.4% year on year, June 2026).",
              s=["con"], lc="everyday", neo=[1, "Mastercard debit; credit split."], src=[["Valora Analitik: Q2 2026 results, Aug 2026", Q226]]),
            P("premium", "Premium & private banking", "World Legend Mastercard, Mastercard Black, Visa Infinite and the metal Amex Platinum for wealthier clients, who reportedly bring more than half of consumer-banking profit ⚠.",
              s=["prem"], lc="grow", st="new", neo=[1, "Mastercard's top tiers alongside Visa and Amex."],
              src=[["La República: World Legend, May 2026", LEGEND], ["Bancolombia: credit cards", CCPAGE]]),
        ]},
        {"id": "4.2", "ic": "building", "name": "Business & corporate", "blurb": "Commercial loans flat.", "div": "bancolombia", "rev": "colombia", "products": [
            P("business", "Business & corporate banking", "Lending, accounts, the Bancolombia Negocios app and Wompi for companies; commercial loans fell slightly in Q2 2026. Business card networks were not captured ⚠.",
              s=["sme", "corp"], lc="borrow", neo=[None, "Business card networks not found."],
              mc="Commercial and virtual cards are untested ground.",
              src=[["Valora Analitik: Q2 2026 results, Aug 2026", Q226]]),
        ]},
        {"id": "4.3", "ic": "hand-coins", "name": "Nequi lending", "blurb": "29m clients, COP 2.3trn.", "div": "nequi", "rev": "digital", "products": [
            P("nequicredit", "Nequi credit & inclusion", "About 29 million clients and 22 million monthly users; loans of about COP 2.3 trillion; break-even since September 2025; more than 7 million use it as their only account; credit offered at Redeban terminals and on Temu.",
              s=["nequi"], lc="borrow", st="new", o="B", at="Redeban, Temu", neo=[0, ""],
              mc="Point-of-sale credit could run on card-on-file and tokens.",
              src=[["La República: Nequi CEO, Aug 2026", NEQUICEO]]),
        ]},
        {"id": "4.4", "ic": "target", "name": "Vehicles", "blurb": "Sufi and Renting Colombia.", "div": "sufi", "rev": "nonbank", "products": [
            P("sufi", "Sufi", "Consumer and vehicle finance; a Sufi co-branded Mastercard halves the card fee for Sufi vehicle-loan holders but is no longer on sale.",
              s=["con"], lc="borrow", neo=[1, "Sufi Mastercard, closed to new clients."], src=[["Bancolombia: credit cards", CCPAGE], ["Grupo Cibest", CIBEST]]),
            P("renting", "Renting Colombia", "Vehicle leasing and fleets, led by Héctor Mauricio Serna.",
              s=["sme", "corp"], lc="borrow", neo=[0, ""],
              mc="Fleet and fuel cards are untested ground.",
              src=[["Grupo Cibest: board and senior management", GOV]]),
        ]},
        {"id": "4.5", "ic": "earth", "name": "Central America", "blurb": "El Salvador and Guatemala.", "div": "agricola", "rev": "camerica", "products": [
            P("agricola", "Banco Agrícola (El Salvador)", "1.8 million clients and loans of US$4.9 billion (June 2026); runs Nequi El Salvador. Card networks not captured ⚠.",
              s=["ca"], lc="everyday", neo=[None, "Card networks not found."], src=[["Valora Analitik: Q2 2026 results, Aug 2026", Q226]]),
            P("bam", "BAM (Guatemala)", "More than 700,000 people and businesses, in its centenary year. Card networks not captured ⚠.",
              s=["ca"], lc="everyday", div="bam", neo=[None, "Card networks not found."], src=[["Valora Analitik: Q2 2026 results, Aug 2026", Q226]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the Mi Bancolombia and Negocios apps, the Nequi app, branches, ATMs and agents shared with Nequi, and partners from Redeban to Avianca.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Bancolombia apps", "blurb": "9.5m active digital clients.", "div": "bancolombia", "rev": "colombia", "products": [
            P("app", "Mi Bancolombia", "9.5 million active digital clients over 30 days (June 2026); virtual debit cards are created in the app in under a minute.",
              s=["con", "prem"], lc="everyday", neo=[0, ""], src=[["Valora Analitik: Q2 2026 results, Aug 2026", Q226], ["Bancolombia: debit cards", DCPAGE]]),
            P("negocios", "Bancolombia Negocios", "The business app, where merchants manage Bre-B keys and QR codes.",
              s=["sme"], lc="move", neo=[0, ""], src=[["El País: Bancolombia QR on Bre-B, May 2026", QRBREB]]),
        ]},
        {"id": "5.2", "ic": "wallet", "name": "Nequi app", "blurb": "22m monthly users.", "div": "nequi", "rev": "digital", "products": [
            P("nequiapp", "Nequi app", "Its own finance company since 1 September 2026, with fees, ATM access and agents unchanged.",
              s=["nequi"], lc="open", st="flux", ay="Sep 2026", neo=[0, ""], src=[["La República: Nequi CEO, Aug 2026", NEQUICEO]]),
        ]},
        {"id": "5.3", "ic": "building-2", "name": "Branches & agents", "blurb": "Shared with Nequi.", "div": "bancolombia", "rev": "colombia", "products": [
            P("network", "Branches, ATMs & correspondents", "Branches, ATMs and banking agents used by both Bancolombia and Nequi customers; counts not captured ⚠.",
              s=["con", "nequi"], lc="everyday", neo=[0, ""], src=[["La República: Nequi CEO, Aug 2026", NEQUICEO]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partners", "blurb": "Redeban, Temu, Avianca.", "div": "cibest", "rev": "colombia", "products": [
            P("partners", "Partners", "Redeban terminals and Temu for Nequi credit, Avianca LifeMiles for travel cards, and the national football team.",
              s=["con", "nequi"], lc="beyond", o="P", at="Redeban, Temu, Avianca LifeMiles", neo=[0, ""],
              src=[["La República: Nequi CEO, Aug 2026", NEQUICEO], ["Publimetro: LifeMiles Visa, Sep 2025", LIFEMILES]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Bancolombia", "blurb": "All of debit, most of credit.", "products": [
        P("mcatbancolombia", "Mastercard at Bancolombia", "Every Bancolombia debit card is Mastercard, and Mastercard is the largest of three credit networks, with about 1.2 million of 2.76 million active cards (April 2026). Bancolombia was the first issuer of World Legend (May 2026), and Nequi's El Salvador card is Mastercard. Visa holds Nequi's Colombian card, the travel and football co-brands and the first Tap to Add Card; Amex has seven cards.",
          s=["con"], div="bancolombia", rev="colombia", mc="The relationship this map is drawn for.",
          src=[["Bancolombia: debit cards", DCPAGE], ["La República: active credit cards, Jul 2026", CARDS], ["La República: World Legend, May 2026", LEGEND]]),
    ]},
    {"id": "pillar-market", "name": "Colombian payments", "blurb": "Bre-B, wallets, three networks.", "products": [
        P("market", "The Colombian market", "17.8 million credit cards (15.7 million active) in April 2026, led by Bancolombia, Falabella, Davivienda and Nu; Bre-B instant payments with 116 million keys in its first year; Mastercard pushing tokens, Click to Pay and agentic payments (February 2026).",
          s=["con"], div="cibest", rev="colombia",
          src=[["La República: active credit cards, Jul 2026", CARDS], ["El País: Bre-B's first year, Oct 2026", BREB], ["Forbes Colombia: Mastercard agentic payments, Feb 2026", MCAGENT]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
