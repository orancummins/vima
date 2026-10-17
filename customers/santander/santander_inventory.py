"""Banco Santander's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the Q2 2026 financial report (22 July 2026)
and the 2025 Form 20-F (25 February 2026). ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

DOCS = "https://www.santander.com/content/dam/santander-com/en/documentos/"
FR = DOCS + "resultados-trimestrales/2026/q2/rt-q2-2026-banco-santander-financial-report-en.pdf"
EP = DOCS + "resultados-trimestrales/2026/q2/rt-q2-2026-banco-santander-earnings-presentation-en.pdf"
FR25 = DOCS + "resultados-trimestrales/2025/q4/rt-4q-2025-banco-santander-financial-report-en.pdf"
F20 = "https://www.santander.com/content/dam/santander-com/es/documentos/informacion-sobre-resultados-semestrales-y-anuales-suministrada-a-la-sec/2026/sec-2025-annual-20-f-2025-disponible-solo-en-ingles-es.pdf"
WBS = "https://www.businesswire.com/news/home/20260203901062/en/"
CBIA = "https://www.cbia.com/?p=178177"
OBSCF = "https://www.santander.com/en/press-room/press-releases/2025/10/openbank-and-santander-consumer-finance-to-integrate-in-europe-expanding-range-of-products-and-services-to-customers"
UKDEBIT = "https://www.retailbankerinternational.com/news/mastercard-bags-santander-uk-debit-card-deal/"
MXDEBIT = "https://www.paymentmedia.com/news-6355-mxico-santander-sustituye-sus-tarjetas-.html"
AGENTEU = "https://www.santander.com/es/sala-de-comunicacion/notas-de-prensa/2026/03/santander-y-mastercard-completan-el-primer-pago-real-ejecutado-por-un-agente-de-ia-en-europa"
AGENTBR = "https://diariodocomercio.com.br/financas/mastercard-avanca-em-pagamentos-agenticos-com-transacoes-na-america-latina-e-caribe/"
AGENTLAC = "https://www.bloomberglinea.com.br/negocios/pagamento-com-agentes-de-ia-mastercard-tera-servico-no-brasil-no-comeco-de-2026/"
MACHINES = "https://www.letsmoney.com.br/noticias/mastercard-pagamento-entre-agentes-ia/"
VISAAG = "https://www.intelligentcio.com/latam/2026/03/16/santander-and-visa-complete-first-agentic-commerce-pilot-across-latin-america/"
VISADEST = "https://www.cronista.com/economia-politica/un-banco-dara-acceso-vip-al-louvre-y-al-rockefeller-center-a-clientes-con-tarjeta-visa/"
GETNETAG = "https://www.pymnts.com/?p=3828766"
CIO = "https://www.cio.com/article/4038926/santander-se-apalanca-en-la-tecnologia-de-openai-para-convertirse-en-un-banco-nativo-en-ia.html"
BIZUM = "https://s1.aebanca.es/wp-content/uploads/2026/02/las-asociaciones-bancarias-aeb-ceca-y-unacc-celebran-el-inicio-de-la-interconexin-de-bizum-con-13-pases-europeos.pdf"
CRYPTO = "https://www.pymnts.com/cryptocurrency/2025/santander-owned-openbank-debuts-crypto-trading-germany/"
ID26 = "https://thecorner.eu/companies/banco-santander-investor-day-focus-to-be-on-improving-profitability-with-post-at-1-rote-target-20/124362/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · markets · Gravity", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a €1.95 trillion balance sheet and the eurozone's most valuable bank, nine core markets on two continents, the Gravity core and one cloud, an OpenAI partnership, and targets of €20 billion profit and 210 million customers by 2028.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & capital", "blurb": "€1.95 trillion, 182.5 million customers.", "div": "grp", "rev": "grp", "products": [
            P("balance", "Balance sheet", "Total assets of €1,954.5 billion, loans of €1,149.2 billion and deposits of €1,133.8 billion at 30 June 2026; 182.5 million customers, 105.7 million active and 62 million digital.",
              s=["corp"], neo=[0, ""], src=[["Q2 2026 financial report", FR]]),
            P("earnings", "Earnings & capital", "Record attributable profit of €14.1 billion in 2025; €8,973 million in the first half of 2026 (underlying €7.3 billion, RoTE 15.6%), CET1 14.0%, efficiency 42.8%; rated A1 (Moody's), A+ (S&P), A (Fitch); market value €177.5 billion at 30 June 2026, the largest in the eurozone.",
              s=["corp"], neo=[0, ""], src=[["Q2 2026 financial report", FR], ["FY2025 financial report", FR25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Botín and Grisi.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Board & leadership", "Executive chair Ana Botín, CEO Héctor Grisi (2023), CFO José Antonio García Cantera, COO and CTO Juan Olaizola; Matías Sánchez, who led cards and the agentic pilots, became co-head of Retail in June 2026 with Borja Oyarzábal; Nitin Prabhu runs Openbank; Mahesh Aditya runs Santander UK.",
              s=["corp"], neo=[0, ""], src=[["2025 Form 20-F", F20], ["Q2 2026 financial report", FR]]),
        ]},
        {"id": "1.3", "ic": "earth", "name": "Heritage & markets", "blurb": "Since 1857, nine core markets.", "div": "grp", "rev": "grp", "products": [
            P("heritage", "Heritage", "Founded in Santander, Cantabria, in 1857; corporate centre at Boadilla del Monte, Madrid; listed in Spain, New York, London, Mexico and Warsaw.",
              s=["corp"], o="I", neo=[0, ""], src=[["2025 Form 20-F", F20]]),
            P("markets", "Nine core markets", "Spain, the UK, Portugal, the US, Mexico, Brazil, Chile and Argentina plus Openbank in Europe: Brazil is the largest by customers (76 million), Spain by profit (€2.5 billion in the first half).",
              s=["con", "corp"], neo=[0, ""], src=[["Q2 2026 financial report", FR]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Gravity, cloud & AI", "blurb": "One core, OpenAI.", "div": "grp", "rev": "grp", "products": [
            P("gravity", "Gravity & the cloud", "Santander's own cloud core banking, live in Spain, Mexico and Chile and ready for Brazil in 2026; more than 97% of infrastructure in the cloud; a 'build once' model that has saved €542 million since 2022.",
              s=["corp"], o="B", neo=[0, ""], src=[["Q2 2026 earnings presentation", EP], ["2025 Form 20-F", F20]]),
            P("ai", "Data & AI with OpenAI", "An agreement with OpenAI (August 2025) to become an 'AI-native bank': about 30,000 staff on ChatGPT Enterprise, more than 7,000 agents, and €84 million of AI value in the first half of 2026 towards more than €1 billion by 2028.",
              s=["corp"], o="P", at="OpenAI", neo=[0, ""], src=[["CIO: Santander and OpenAI, Aug 2025", CIO], ["Q2 2026 earnings presentation", EP]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "TSB in, Poland out, Webster in.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "ONE Transformation & 2028 targets", "'A digital bank with branches': underlying profit above €20 billion, RoTE above 20%, efficiency about 36% and more than 210 million customers by 2028, set at the February 2026 investor day.",
              s=["corp"], neo=[0, ""], src=[["The Corner: investor day, Feb 2026", ID26], ["Q2 2026 earnings presentation", EP]]),
            P("deals", "TSB, Poland & Webster", "Santander Bank Polska sold to Erste (closed 9 January 2026, about €7 billion); TSB bought for about £2.9 billion (30 April 2026, more than 4 million customers); Webster Financial bought for about $12.2 billion (closed August 2026 ⚠), taking the US business to about $254 billion of assets.",
              s=["con", "corp"], o="A", st="new", neo=[0, ""], src=[["Q2 2026 financial report", FR], ["Webster and Santander, Feb 2026", WBS], ["CBIA: Webster deal completed, Aug 2026", CBIA]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Five ways money moves: €338 billion of card spending, with Mastercard debit in the UK and Mexico; one card processor (Plard) for five countries; Getnet acceptance, €129 billion in half a year; Bizum and a billion account-to-account payments a month; and Ebury for cross-border.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit & credit cards", "blurb": "€338 billion of card spending.", "div": "san", "rev": "retail", "products": [
            P("ukcards", "Santander UK debit & credit (Mastercard)", "An eight-year deal (May 2018) put every Santander UK current-account debit card, more than 9 million, on Mastercard; the credit cards were already Mastercard.", short="UK on Mastercard",
              s=["con"], lc="everyday", o="P", at="Mastercard", ay="May 2018", neo=[2, "Mastercard."],
              mc="The eight-year term runs out around 2026–27, with TSB's cards ⚠ believed Visa to be folded in.",
              src=[["Retail Banker International: Santander UK debit to Mastercard, May 2018", UKDEBIT]]),
            P("mxcards", "Santander México debit & LikeU (Mastercard)", "All debit cards and LikeU credit cards reissued in 2023 as recycled Mastercard Touch Cards; LikeU credit also comes on Visa, and there is an Amex co-brand.", short="Mexico on Mastercard",
              s=["con"], lc="everyday", o="P", at="Mastercard", ay="2023", neo=[2, "Mastercard debit; credit mixed."],
              src=[["Payment Media: Santander México replaces its cards, Feb 2023", MXDEBIT]]),
            P("groupcards", "Cards elsewhere", "€338.5 billion of card spending in 2025 (+6%); Brazil's Unique comes as Mastercard Black and Visa Infinite; Spain, Portugal, Chile and the US network split is not public. Cards moved into Retail in January 2026.", short="Cards: Brazil, Spain & more",
              s=["con", "aff"], lc="everyday", neo=[1, "Both networks; split not public."],
              src=[["2025 Form 20-F", F20], ["Q2 2026 financial report", FR]]),
        ]},
        {"id": "2.2", "ic": "refresh-cw", "name": "Card processing & tokens", "blurb": "Plard: 500 million a month.", "div": "getnet", "rev": "pay", "products": [
            P("plard", "Plard", "Santander's own global card-processing platform: more than 500 million transactions a month across Brazil, Mexico, Chile, Spain and the UK, with Portugal next.",
              s=["con", "corp"], lc="move", o="B", neo=[0, "In-house processing."],
              mc="In-house processing narrows the room for Mastercard's processing services but makes new tokens and products quick to roll out.",
              src=[["Q2 2026 financial report", FR], ["2025 Form 20-F", F20]]),
            P("tokens", "Tokens, wallets & Pay Smarter", "Tokens managed centrally, Apple Pay and Google Pay in every country, and Pay Smarter, which turns a debit purchase into credit after the fact.",
              s=["con"], lc="everyday", neo=[1, "Network tokens on Mastercard cards."], src=[["2025 Form 20-F", F20]]),
        ]},
        {"id": "2.3", "ic": "store", "name": "Getnet acceptance", "blurb": "€129 billion in half a year.", "div": "getnet", "rev": "pay", "products": [
            P("getnet", "Getnet", "Merchant acquiring across Latin America, Spain and Portugal on one API: €237.9 billion and 10.5 billion transactions in 2025, €129 billion in the first half of 2026 (+10%); offices opened in the US and China; Pay-in for foreign merchants in Brazil and dynamic currency conversion in Mexico.",
              s=["merch", "sme"], lc="move", neo=[1, "Accepts every network."],
              src=[["Q2 2026 financial report", FR], ["2025 Form 20-F", F20]]),
            P("getnetagent", "Getnet agentic acceptance", "Acceptance of AI-agent payments (June 2026), compatible with Mastercard Agent Pay with Visa Intelligent Commerce pending; live in Mexico with Mastercard and Neivor, and a launch partner of Mastercard Agent Pay for Machines.",
              s=["merch"], lc="move", st="new", ay="Jun 2026", o="P", at="Mastercard", neo=[3, "Mastercard Agent Pay first."],
              mc="Getnet is the acquiring half of Mastercard's agentic story at Santander, ahead of Visa.",
              src=[["PYMNTS: Getnet agentic payments, Jun 2026", GETNETAG], ["Let's Money: Agent Pay for Machines, Jun 2026", MACHINES]]),
        ]},
        {"id": "2.4", "ic": "zap", "name": "Account-to-account", "blurb": "Bizum, Getnet Platforms.", "div": "san", "rev": "pay", "products": [
            P("bizum", "Bizum & Wero", "Spain's instant mobile payments, where Santander is gaining active users, interconnecting with Italy and Portugal and, under a February 2026 agreement, with EPI's Wero.",
              s=["con", "merch"], lc="move", neo=[0, "Account-to-account."], src=[["AEB: Bizum interconnection, Feb 2026", BIZUM], ["Q2 2026 financial report", FR]]),
            P("gplatforms", "Getnet Platforms", "Account-to-account processing, FX and fraud for platforms: more than a billion payments a month, five times the year before, mostly Brazil.",
              s=["merch", "corp"], lc="move", neo=[0, ""], src=[["Q2 2026 financial report", FR]]),
        ]},
        {"id": "2.5", "ic": "arrow-left-right", "name": "Cross-border & FX", "blurb": "Ebury, 28,000 firms.", "div": "getnet", "rev": "pay", "products": [
            P("ebury", "Ebury & cross-border", "Cross-border payments and FX for small and mid-sized firms (more than 28,000 active, +28%; £550 million raised in 2026), with an instant cross-border solution in development.",
              s=["sme", "corp"], lc="move", neo=[0, ""],
              mc="Mastercard Move could carry Ebury's and Pay-in's payouts; no need has been stated publicly.",
              src=[["Q2 2026 financial report", FR], ["2025 Form 20-F", F20]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account and payment: Europe's first live AI-agent payment with Mastercard and parallel pilots with Visa, AI built with OpenAI, fraud detection, Openbank Pay for checkout lending, and personalisation for affluent customers.",
    "tiles": [
        {"id": "3.1", "ic": "bot", "name": "Agentic commerce", "blurb": "Europe's first, with Mastercard.", "div": "san", "rev": "retail", "products": [
            P("agentpay", "Mastercard Agent Pay", "Europe's first live end-to-end AI-agent payment, in Spain on 2 March 2026 with Mastercard and PayOS, followed by live Agent Pay transactions at Santander Brasil on 24 March with agentic tokens and passkeys.", short="Agent Pay",
              s=["con"], lc="move", st="new", ay="Mar 2026", o="P", at="Mastercard", neo=[3, "Mastercard Agent Pay."],
              mc="Now to scale from pilot to product, before Visa becomes the default.",
              src=[["Santander: first AI-agent payment in Europe, Mar 2026", AGENTEU], ["Diário do Comércio: Agent Pay in Latin America, Mar 2026", AGENTBR]]),
            P("visaagent", "Visa Intelligent Commerce pilot", "An agentic pilot in Argentina, Brazil, Chile, Mexico and Uruguay with Visa (March 2026), weeks after the Mastercard one; Santander is also the first bank on Visa Destinations (June 2026).",
              s=["con", "aff"], lc="move", st="new", ay="Mar 2026", o="P", at="Visa", neo=[0, "Visa."],
              src=[["Intelligent CIO: Santander and Visa agentic pilot, Mar 2026", VISAAG], ["El Cronista: Visa Destinations, Jun 2026", VISADEST]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data & personalisation", "blurb": "Cards Data Lab.", "div": "san", "rev": "retail", "products": [
            P("datalab", "Cards Data Lab & personalisation", "1.6 million pre-approved customers from the Cards Data Lab in nine countries, and a customer-interaction platform live in Brazil, the UK, Argentina, Chile and Mexico.",
              s=["con", "aff"], lc="grow", neo=[0, ""],
              mc="Merchant data and enrichment would feed the same models.",
              src=[["2025 Form 20-F", F20], ["Q2 2026 financial report", FR]]),
        ]},
        {"id": "3.3", "ic": "shield-check", "name": "Fraud & security", "blurb": "Own models, a CERT.", "div": "grp", "rev": "grp", "products": [
            P("fraud", "Fraud detection & cyber", "Fraud detection sold as a Getnet Platforms service, a permanent CERT for cyber incidents, and in-house models on card and account-to-account payments.",
              s=["con", "merch"], lc="everyday", neo=[0, "No Mastercard fraud product announced."],
              mc="Account-to-account fraud grows with Bizum and Wero; evidence of need is thin.",
              src=[["Q2 2026 financial report", FR], ["2025 Form 20-F", F20]]),
        ]},
        {"id": "3.4", "ic": "receipt-text", "name": "Checkout lending", "blurb": "Openbank Pay.", "div": "openbank", "rev": "dcb", "products": [
            P("openbankpay", "Openbank Pay", "Checkout lending and embedded finance, formerly Zinia: more than 2.6 million customers, upgraded journeys on Amazon Spain, and instalments in Openbank Mexico.",
              s=["con", "merch"], lc="borrow", neo=[0, "Santander's own BNPL."],
              mc="Competes with Mastercard Installments; Santander builds BNPL itself.",
              src=[["Q2 2026 financial report", FR], ["2025 Form 20-F", F20]]),
        ]},
        {"id": "3.5", "ic": "gem", "name": "Select & benefits", "blurb": "The affluent proposition.", "div": "san", "rev": "retail", "products": [
            P("select", "Select", "The affluent proposition in Spain and Brazil, driving deposits, fees and card volumes, with premium cards on both networks and Visa Destinations travel benefits.",
              s=["aff"], lc="grow", neo=[1, "Mastercard Black alongside Visa Infinite."], src=[["Q2 2026 financial report", FR], ["El Cronista: Visa Destinations, Jun 2026", VISADEST]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Five global businesses (Retail & Commercial, Openbank, CIB, Wealth & Insurance, Payment Solutions) opened out by market: Spain and Portugal, the UK with TSB, Brazil, Mexico and the rest of South America, the US with Webster, and Openbank's consumer finance across 26 countries.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "Spain & Portugal", "blurb": "€2.2 billion PBT in Spain.", "div": "es", "rev": "retail", "products": [
            P("spain", "Retail Spain & Portugal", "15.4 million customers in Spain, gaining share in payrolls, pensions and cards (profit before tax €2.2 billion in the first half, +33%), and Santander Totta in Portugal; Teens App launched in 2026.",
              s=["con", "home"], lc="everyday", neo=[1, "Cards on both networks."], src=[["Q2 2026 financial report", FR]]),
            P("smegrowth", "Santander Growth & SMEs", "Analytics to find high-growth companies, started in Spain and rolling out to Brazil, Mexico, the UK, Chile and Portugal.",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["Q2 2026 financial report", FR]]),
        ]},
        {"id": "4.2", "ic": "flag", "name": "UK with TSB", "blurb": "Third in current accounts.", "div": "uk", "rev": "retail", "products": [
            P("ukretail", "Santander UK & TSB", "About 27 million customers including TSB's 4 million: third in UK current accounts and fourth in mortgages; TSB's legal merger is expected in 2027.",
              s=["con", "home"], lc="everyday", st="new", neo=[1, "Santander UK cards Mastercard; TSB ⚠ Visa."],
              mc="TSB's cards come into play when its customers move across.",
              src=[["Q2 2026 financial report", FR]]),
        ]},
        {"id": "4.3", "ic": "earth", "name": "Latin America", "blurb": "Brazil, Mexico, Chile, Argentina.", "div": "br", "rev": "retail", "products": [
            P("brazil", "Santander Brasil", "75.6 million retail customers, a focus on affluent Select clients, and Plard managing more than 22 million cards.",
              s=["con", "aff", "sme"], lc="everyday", neo=[1, "Both networks."], src=[["Q2 2026 financial report", FR], ["2025 Form 20-F", F20]]),
            P("mexico", "Santander México", "22.2 million retail customers, 76% of the active ones digital; Mastercard debit and LikeU.",
              s=["con", "sme"], lc="everyday", neo=[2, "Mastercard debit."], src=[["Q2 2026 financial report", FR]]),
            P("southam", "Chile & Argentina", "Profits of €469 million and €194 million in the first half; Gravity is live in Chile.",
              s=["con"], lc="everyday", neo=[None, "Network split not public."], src=[["Q2 2026 financial report", FR]]),
        ]},
        {"id": "4.4", "ic": "building", "name": "United States", "blurb": "With Webster, $254 billion.", "div": "us", "rev": "dcb", "products": [
            P("us", "Santander US & Webster", "Santander Bank and the auto lender (Openbank US), joined by Webster in 2026 for about $254 billion of assets and a 2028 target RoTE of 18%; Openbank US has $11.4 billion of deposits and a Verizon partnership.",
              s=["con", "auto", "corp"], lc="borrow", st="new", neo=[None, "Network not verified."],
              mc="Webster's card portfolio is new territory after the merger.",
              src=[["CBIA: Webster deal completed, Aug 2026", CBIA], ["Q2 2026 earnings presentation", EP]]),
        ]},
        {"id": "4.5", "ic": "plane", "name": "Openbank & consumer finance", "blurb": "27.6 million customers.", "div": "openbank", "rev": "dcb", "products": [
            P("openbankeu", "Openbank Europe & auto finance", "Santander Consumer Finance and Openbank merged into one entity in 26 countries (2026): car loans, leasing, cards with Amazon, Apple and Vodafone, and partners among car makers; UK motor-finance provisions weigh on returns.",
              s=["con", "auto"], lc="borrow", neo=[None, "Network not public."], src=[["Santander: Openbank and SCF to integrate, Oct 2025", OBSCF], ["Q2 2026 financial report", FR]]),
        ]},
        {"id": "4.6", "ic": "building-2", "name": "Corporate & Investment Banking", "blurb": "RoTE 20%.", "div": "san", "rev": "cib", "products": [
            P("cib", "CIB", "Global Transaction Banking, Global Banking and Global Markets: first in Spain for investment-banking fees in the first half of 2026, a $22.8 billion Vantage Data Centers loan, and the first tokenised securities-lending trade on HQLAx.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Q2 2026 financial report", FR]]),
        ]},
        {"id": "4.7", "ic": "chart-candlestick", "name": "Wealth & insurance", "blurb": "€581 billion managed.", "div": "san", "rev": "wealth", "products": [
            P("wealth", "Private Banking, Asset Management & Insurance", "€581 billion under management, about 302,000 private-banking clients, Santander Asset Management and €6.2 billion of insurance premiums.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["Q2 2026 financial report", FR]]),
            P("crypto", "Openbank crypto", "MiCA-regulated crypto trading in Germany (September 2025) and Spain; Santander has explored dollar and euro stablecoins ⚠.",
              s=["aff", "con"], lc="grow", st="new", neo=[0, ""], src=[["PYMNTS: Openbank crypto trading, Sep 2025", CRYPTO]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: One App on the Gravity core, 6,496 branches and Work Cafés, Openbank's digital banks in four countries, and partner channels from Amazon to car makers.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "One App", "blurb": "53% of retail customers.", "div": "san", "rev": "retail", "products": [
            P("oneapp", "One App", "A single app on Gravity, serving 53% of retail customers in the first half of 2026 and more than 80% by 2028; live in Spain, Mexico, Brazil and Chile.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Q2 2026 earnings presentation", EP]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & Work Café", "blurb": "6,496 branches.", "div": "san", "rev": "retail", "products": [
            P("branches", "Branches & Work Café", "6,496 branches, down from 7,322 a year earlier, with an assisted-channel tool in more than half of them and new openings in Brazil, the UK and Portugal.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["Q2 2026 financial report", FR]]),
        ]},
        {"id": "5.3", "ic": "globe", "name": "Openbank digital banks", "blurb": "US, Spain, Mexico, Germany.", "div": "openbank", "rev": "dcb", "products": [
            P("openbankdigital", "Openbank US, Mexico & Germany", "Openbank US (October 2024, 235,000 customers), Openbank Mexico (2025, 1.2 million) and Openbank Germany, with an AI broker in Germany and Spain.",
              s=["con"], lc="open", neo=[None, "Card network not public."], src=[["2025 Form 20-F", F20], ["Q2 2026 financial report", FR]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partner channels", "blurb": "Amazon, Apple, Verizon.", "div": "openbank", "rev": "dcb", "products": [
            P("partners", "Partner channels", "Amazon (instalments in Spain, co-branded cards in Germany and Austria), Apple and Vodafone in Germany, Verizon in the US ($1.3 billion of deposits), and car makers.",
              s=["con", "auto"], lc="open", neo=[0, ""], src=[["2025 Form 20-F", F20], ["Q2 2026 financial report", FR]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Santander", "blurb": "UK and Mexico debit, Agent Pay.", "products": [
        P("mcatsan", "Mastercard at Santander", "Mastercard carries Santander UK's debit (eight-year deal, May 2018) and credit, Mexico's debit, half of Brazil's top cards, and the group's agentic firsts: Europe's first live agent payment, Santander Brasil's Agent Pay, and Getnet in Agent Pay and Agent Pay for Machines. No group-wide network deal has been found; Visa runs parallel agentic pilots.",
          s=["corp"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Retail Banker International, May 2018", UKDEBIT], ["Santander: first AI-agent payment in Europe, Mar 2026", AGENTEU], ["Bloomberg Línea: Agent Pay in LAC, Dec 2025", AGENTLAC]]),
    ]},
    {"id": "pillar-market", "name": "Two continents", "blurb": "Bizum, Pix, agents.", "products": [
        P("market", "Santander's payment markets", "Bizum and Wero in Europe, Pix in Brazil, BNPL from Openbank Pay to Klarna, and both networks racing to make agentic payments their default.",
          s=["con"], div="grp", rev="grp", src=[["AEB: Bizum interconnection, Feb 2026", BIZUM]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
