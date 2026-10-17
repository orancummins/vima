"""Banco do Brasil's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the 2Q26 results and MD&A (12 August 2026), the
2Q26 institutional presentation (1 September 2026) and the 4Q25 results (February 2026). ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

MDA = "https://api.mziq.com/mzfilemanager/v2/d/5760dff3-15e1-4962-9e81-322a0b3d0bbd/baf82bc7-3aa3-a91d-72c4-fdbde495644c?origin=2"
INST = "https://api.mziq.com/mzfilemanager/v2/d/5760dff3-15e1-4962-9e81-322a0b3d0bbd/5a9610b7-de84-6c13-7010-cd0025aafb0f?origin=2"
Q2 = "https://api.mziq.com/mzfilemanager/v2/d/5760dff3-15e1-4962-9e81-322a0b3d0bbd/3563339f-85c7-176a-07b2-fa1fd0f2917c?origin=2"
BULLETIN = "https://api.mziq.com/mzfilemanager/v2/d/5760dff3-15e1-4962-9e81-322a0b3d0bbd/6ef265fb-094b-3e35-89c0-017d1acea535?origin=2"
FY25 = "https://static.poder360.com.br/2026/02/Banco-do-Brasil-4T25.pdf"
INFO4Q = "https://api.mziq.com/mzfilemanager/v2/d/5760dff3-15e1-4962-9e81-322a0b3d0bbd/292bf43c-1252-8990-aa11-64e56fdb7812?origin=2"
TRADEMAP = "https://trademap.com.br/noticias/news-8201683"
Q2PRESS = "https://mercadoeconsumo.com.br/13/08/2026/mc-capital/banco-do-brasil-tem-lucro-liquido-ajustado-de-r-39-bi-no-2t-alta-de-33/"
Q1 = "https://istoedinheiro.com.br/lucro-do-banco-do-brasil-cai-54-com-avanco-da-crise-no-agro"
RESHUFFLE = "https://www.letsmoney.com.br/noticias/banco-brasil-reorganiza-diretoria-12-executivos/"
BBDAY = "https://www.letsmoney.com.br/noticias/bb-superapp-ia-clientes-digitais-2030/"
VISAAGENT = "https://mercadoeconsumo.com.br/12/03/2026/tecnologia/banco-do-brasil-conclui-primeira-transacao-com-agente-de-ia-no-pais-usando-plataforma-da-visa/"
AGENTPAY = "https://www.bloomberglinea.com.br/negocios/pagamento-com-agentes-de-ia-mastercard-tera-servico-no-brasil-no-comeco-de-2026/"
CLICKTOPAY = "https://finsidersbrasil.com.br/tecnologia-para-fintechs/brasil-e-o-segundo-pais-no-mundo-que-mais-usa-o-click-to-pay-da-mastercard"
UNIVERSO = "https://www.cartoesdecredito.me/?p=80962"
PPV = "https://pontospravoar.com/tag/bb/"
FORUM = "https://www.falandodeviagem.com.br/viewtopic.php?p=449702"
ALTUS = "https://www.falandodeviagem.com.br/viewtopic.php?p=450955"
CARDS2025 = "https://mercadoeconsumo.com.br/15/11/2024/economia/apos-fase-pe-no-chao-banco-do-brasil-voltara-ao-ataque-com-aposta-em-cartao-de-credito-em-2025/"
CIELO = "https://www.suno.com.br/noticias/cielo-ciel3-opa-positiva-bancos-va"
ACADEMIA = "https://tiinside.com.br/en/08/06/2026/banco-do-brasil-engaja-mais-de-36-mil-funcionarios-em-programa-de-capacitacao-para-ia-generativa-e-agentica/"
ITFORUM = "https://itforum.com.br/tag/banco-do-brasil/"
BLACK = "https://cartoeseviagens.com.br/cartao-de-credito/ourocard-mastercard-black"
CAIXA = "https://diariodocomercio.com.br/mix/caixa-anuncia-fim-de-servico-de-cartao-de-credito-e-pega-clientes-de-surpresa/"
DREX = "https://pt.wikipedia.org/wiki/Drex"
PIX = "https://pt.wikipedia.org/wiki/Pix"
WIKI = "https://en.wikipedia.org/wiki/Banco_do_Brasil"
IR = "https://ri.bb.com.br/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · state control · stakes", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: 92 million customers and R$1.31 trillion of loans, profits cut by farm-loan losses, a bank founded in 1808 and half-owned by the federal government, a 2026–2030 strategy, AI at scale, and stakes in Elo, Cielo, Livelo and BB Seguridade.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "RoE 8.3%, NPL 5.6%.", "div": "bb", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Adjusted net income of R$3.9 billion in 2Q26 (RoE 8.3%) and R$20.7 billion in 2025, down 45.4% on farm-credit losses; loans of R$1.313 trillion, assets of R$2.58 trillion, NPL 5.61%, CET1 11.27%. 92 million customers and 83,991 staff. Rated BB/Ba1/BB; market value about R$114 billion at end-June ⚠ (derived).",
              s=["con"], neo=[0, ""], src=[["2Q26 MD&A", MDA], ["4Q25 results", FY25], ["2Q26 institutional presentation", INST], ["TradeMap: 2Q26, Aug 2026", TRADEMAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Control & leadership", "blurb": "The state holds 50%.", "div": "bb", "rev": "group", "products": [
            P("leadership", "Control & leadership", "The federal government holds 50.0000011%; CEO Tarciana Medeiros; CFO Geovanne Tobias; Marisa Reghini runs Digital Business & Technology and Carla Nesi Retail. A March 2026 reshuffle made Bárbara dos Santos Lopes Freitas director of payments and moved Pedro Bramont to digital business. Leadership often changes after elections ⚠ (October 2026).",
              s=["corp"], neo=[0, ""], src=[["2Q26 institutional presentation", INST], ["LetsMoney: reshuffle, Mar 2026", RESHUFFLE]]),
            P("brands", "Heritage", "Founded on 12 October 1808; the first company listed on a Brazilian exchange (1906), the first Brazilian bank with computers (1969), Ourocard from 1987 and internet banking from 1996; headquartered in Brasília and listed as BBAS3.",
              s=["con"], o="I", neo=[0, ""], src=[["2Q26 institutional presentation", INST], ["Wikipedia: Banco do Brasil", WIKI]]),
        ]},
        {"id": "1.3", "ic": "target", "name": "Strategy & guidance", "blurb": "Guidance cut to R$18–22bn.", "div": "bb", "rev": "group", "products": [
            P("strategy", "Strategy 2026–2030 & guidance", "To be 'close and relevant' to customers, on financial resilience, customers, people, technology and new arenas 'beyond banking'. 2026 net-income guidance cut on 13 May from R$22–26 billion to R$18–22 billion, with cost of credit raised to R$65–70 billion. Cards named a 'main focus' after cutting issuance post-pandemic.",
              s=["corp"], st="flux", neo=[0, ""], src=[["2Q26 institutional presentation", INST], ["IstoÉ Dinheiro: 1Q26, May 2026", Q1], ["Mercado & Consumo: cards in 2025, Nov 2024", CARDS2025]]),
            P("sustain", "Sustainable finance & ventures", "A sustainable loan book of R$431.5 billion aiming for R$500 billion by 2030, a US$500 million Nature Bond five times covered, a carbon-credit desk launched at COP30 in Belém, and BB Ventures with seven funds and 50 start-ups.",
              s=["corp", "farm"], st="new", neo=[0, ""], src=[["2Q26 institutional presentation", INST], ["2Q26 MD&A", MDA], ["4Q25 InformAções", INFO4Q]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "R$8.2bn a year on tech.", "div": "bbts", "rev": "group", "products": [
            P("tech", "Cloud, AI & governance", "Hybrid cloud with more than 100 deployments a day, the Plata.IA and GAIA 3.0 AI stack with 2,300 models, R$8.2 billion of technology investment over 12 months, 36,000+ staff in generative and agentic AI training with Microsoft, Google Cloud and IBM, and 12,000+ Copilot agents; Celent Model Bank of the Year 2026.",
              s=["corp"], st="new", o="P", at="Microsoft, Google Cloud, IBM", neo=[0, ""], src=[["2Q26 MD&A", MDA], ["TI Inside: AcademIA BB, Jun 2026", ACADEMIA], ["2Q26 institutional presentation", INST]]),
        ]},
        {"id": "1.5", "ic": "network", "name": "Stakes", "blurb": "Elo, Cielo, Seguridade, BV.", "div": "elo", "rev": "group", "products": [
            P("stakes", "Stakes", "68.26% of BB Seguridade, 50% of Banco Votorantim, 80.39% of Banco Patagonia, 49.99% of UBS BB; and through BB Elo Cartões 49.99% of Elopar, Livelo and Alelo, a third of the Elo network and 49.28% of Cielo, delisted after a joint tender with Bradesco announced in February 2024 ⚠ (completion date not sourced).",
              s=["corp"], o="A", neo=[0, ""], src=[["2Q26 MD&A", MDA], ["Suno: Cielo tender, Feb 2024", CIELO]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "How money moves: R$128 billion of card spending a quarter on Ourocard credit and debit across Visa, Elo and Mastercard, Visa's Altus at the top, Pix, BB Pay and Cielo for acceptance, Elo it co-owns, APIs for 61,000 companies, 84 countries abroad, and an agentic purchase with Visa.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Ourocard credit", "blurb": "R$70bn book, three networks.", "div": "ourocard", "rev": "ind", "products": [
            P("ourocard", "Ourocard credit cards", "A R$69.9 billion book (+15.1%), 11.0 million recurring users (−3%) and R$86.7 billion of spending in 2Q26, on Visa, Elo and Mastercard; no split by network is published. The card business lost R$649 million in 2Q26.", short="Ourocard credit (three networks)",
              s=["con"], lc="borrow", o="B", neo=[1, "Visa, Elo and Mastercard; split not published."],
              mc="A loss-making card business with a growing book is a case for portfolio analytics.",
              src=[["2Q26 MD&A", MDA], ["Mercado & Consumo: cards in 2025, Nov 2024", CARDS2025]]),
        ]},
        {"id": "2.2", "ic": "gem", "name": "Premium & co-brands", "blurb": "Altus on Visa, Black on Mastercard.", "div": "ourocard", "rev": "ind", "products": [
            P("altus", "BB Visa Altus Liv & Altus Visa Infinite", "Visa Infinite since October 2020 and Altus Liv from 4Q25, with 1,700+ lounges and no IOF on foreign spending; BB says Altus Liv spending grows twice as fast as other cards.", short="Altus (Visa)",
              s=["prem"], lc="borrow", st="new", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa holds the premium flagship.",
              src=[["4Q25 InformAções", INFO4Q], ["2Q26 results", Q2], ["Falando de Viagem: Altus, Oct 2020", ALTUS]]),
            P("mcblack", "Ourocard Mastercard Black, Platinum & Gold", "Still offered in 2026; Black at R$1,098 a year by invitation, with Livelo points, IOF cut to 1.1% (March 2024) and a 40,000-point promotion to January 2026. Forum reports in 2020 said BB stopped new Mastercard applications ⚠; BB reportedly denied ending the partnership.", short="Ourocard Mastercard",
              s=["prem", "con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Cartões e Viagens: Ourocard Mastercard Black", BLACK], ["Pontos pra Voar: BB", PPV], ["Falando de Viagem: BB and Mastercard, 2020", FORUM]]),
            P("nanquim", "Ourocard Elo Nanquim", "The top Elo card.", short="Elo Nanquim",
              s=["prem"], lc="borrow", o="P", at="Elo", neo=[0, "Elo."], src=[["Pontos pra Voar: BB", PPV]]),
            P("smiles", "GOL Smiles co-brand", "Co-brand cards with an annual-fee waiver tied to spending (March 2026); network Visa per secondary sources ⚠. The Americanas Ame card contract ended in 2024 for low profitability.", short="Smiles (Visa ⚠)",
              s=["con"], lc="borrow", o="P", at="GOL Smiles", neo=[0, "Visa ⚠."], src=[["Pontos pra Voar: BB", PPV], ["Mercado & Consumo: cards in 2025, Nov 2024", CARDS2025]]),
        ]},
        {"id": "2.3", "ic": "wallet-cards", "name": "Debit", "blurb": "14m users.", "div": "ourocard", "rev": "ind", "products": [
            P("debit", "Ourocard debit", "14.0 million recurring users and R$40.8 billion of spending in 2Q26; network not disclosed, Elo likely the default ⚠ (inference).",
              s=["con"], lc="everyday", neo=[None, "Not disclosed; Elo likely ⚠."], src=[["2Q26 MD&A", MDA]]),
        ]},
        {"id": "2.4", "ic": "zap", "name": "Pix", "blurb": "36.4m keys.", "div": "bb", "rev": "ind", "products": [
            P("pix", "Pix, Bolepix Automático & MED 2.0", "36.4 million active keys (3.7% of the market), Pix by voice and image on WhatsApp, Bolepix Automático and MED 2.0 for recovering Pix fraud (1H26). Sent volume given as 'R$1.3 bilhão' ⚠ (probably a count).",
              s=["con", "sme"], lc="move", o="P", at="Central Bank of Brazil", neo=[0, "Pix."], src=[["2Q26 MD&A", MDA], ["Wikipedia: Pix", PIX]]),
            P("pixabroad", "Pix in Argentina", "A pilot since March 2026 through Banco Patagonia, paying by QR code.",
              s=["con"], lc="move", st="new", ay="Mar 2026", neo=[0, "Pix."],
              mc="Pix abroad competes with card spending on trips.",
              src=[["2Q26 MD&A", MDA]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "BB Pay and Cielo.", "div": "elo", "rev": "comp", "products": [
            P("bbpay", "BB Pay & BB Pay Split", "Payment links, Tap on Phone and e-commerce APIs: R$5.9 billion over 6.0 million transactions in 2Q26 (+40.5%).",
              s=["sme"], lc="move", st="new", o="B", neo=[None, "Networks not stated."], src=[["2Q26 MD&A", MDA]]),
            P("cielo", "Cielo & Cateno", "Acquiring through Cielo (49.28% in total), with retail business customers' processed spend up 12.6%; Cateno (BB 30%, Cielo 70%) manages Ourocard payment accounts.",
              s=["sme"], lc="move", o="P", at="Bradesco", neo=[1, "Acquirer for all networks ⚠."], src=[["2Q26 MD&A", MDA]]),
        ]},
        {"id": "2.6", "ic": "network", "name": "Elo", "blurb": "A third of the network.", "div": "elo", "rev": "group", "products": [
            P("elo", "Elo", "A third of the Elo network through BB Elo Cartões, with Elo income shared with Bradesco under an agreement of 1 November 2017; Elo earnings reach BB through equity accounting.", short="Elo (co-owned)",
              s=["con"], lc="move", o="P", at="Bradesco, Caixa", neo=[0, "Elo."],
              mc="Mastercard's structural rival at BB.",
              src=[["2Q26 MD&A", MDA]]),
        ]},
        {"id": "2.7", "ic": "code-xml", "name": "APIs & open finance", "blurb": "2bn API calls a month.", "div": "bb", "rev": "comp", "products": [
            P("apis", "Cash-management APIs", "More than 61,000 integrated companies, 30+ API products and 2.05 billion calls a month.",
              s=["corp", "sme"], lc="move", neo=[0, ""], src=[["2Q26 MD&A", MDA]]),
            P("itp", "Payment initiation", "BB calls itself 'one of the main' payment initiators under Brazil's open finance.",
              s=["con", "corp"], lc="move", neo=[0, ""], src=[["2Q26 MD&A", MDA]]),
        ]},
        {"id": "2.8", "ic": "earth", "name": "International", "blurb": "84 countries.", "div": "intl", "rev": "comp", "products": [
            P("fx", "FX & international", "Present in 84 countries with 499 correspondent banks; BB Americas (a US$2 billion mortgage book), about 90,000–100,000 customers in Japan and a digital account in Portugal; Banco Patagonia in Argentina.",
              s=["con", "corp"], lc="move", neo=[0, ""],
              mc="Diaspora and cross-border flows are where Mastercard Move could fit.",
              src=[["2Q26 MD&A", MDA], ["2Q26 InformAções", BULLETIN]]),
        ]},
        {"id": "2.9", "ic": "sparkles", "name": "Agentic & digital money", "blurb": "Brazil's first agent purchase.", "div": "bb", "rev": "ind", "products": [
            P("agentic", "Agentic commerce with Visa", "Brazil's first purchase by an AI agent, on Visa Intelligent Commerce in a controlled production environment (11 March 2026), fronted by Pedro Bramont and Visa Brasil's Rodrigo Cury. Mastercard's Agent Pay reached Latin American issuers from February 2026 without naming BB.", short="Agentic (Visa)",
              s=["con"], lc="move", st="new", ay="Mar 2026", o="P", at="Visa", neo=[0, "Visa."],
              mc="An Agent Pay pilot would be BB's second-network first.",
              src=[["Mercado & Consumo: Visa agentic, Mar 2026", VISAAGENT], ["Bloomberg Línea: Agent Pay, Dec 2025", AGENTPAY]]),
            P("drex", "Drex", "The central bank's digital-money project ended its second pilot phase in November 2025 and is being rebuilt; BB's role not verified ⚠.",
              s=["corp"], lc="move", st="flux", neo=[None, "BB's role not verified ⚠."], src=[["Wikipedia: Drex", DREX]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: BB Autenticador, biometrics and risk scoring, Minhas Finanças for 14.8 million and 855 million personalised offers a quarter, and Livelo, Universo Ourocard and the Casa BB lounge.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Security & fraud", "blurb": "Autenticador, biometrics.", "div": "bb", "rev": "ind", "products": [
            P("security", "Security, fraud & privacy", "BB Autenticador, facial biometrics and adaptive real-time risk scoring, a receipt validator (7,000+ checks in three months), Central Minha Privacidade (6 million users) and Caipora for personal-data compliance. Vendors not disclosed.",
              s=["con", "sme"], lc="everyday", neo=[None, "Vendors not disclosed."],
              mc="Pix and card fraud pressure is where Mastercard's identity and risk tools could fit.",
              src=[["2Q26 MD&A", MDA]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data & AI", "blurb": "Minhas Finanças, CRM360.", "div": "bb", "rev": "ind", "products": [
            P("minhasfinancas", "Minhas Finanças", "A multi-bank money manager with generative AI: 14.8 million active users and more than a billion transactions categorised a month.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["2Q26 MD&A", MDA]]),
            P("crm", "CRM360 & Inteligência de Valor", "855 million offers and 361 million contacts in 2Q26 across about 89 million individuals.",
              s=["con"], lc="grow", o="B", neo=[0, ""], src=[["2Q26 MD&A", MDA]]),
            P("analytics", "Risk & collections analytics", "ODIN value-chain analytics, the Atlas corporate default model, AI-led rural-credit inspection, and BBTS collections on WhatsApp built with BRQ and AWS (+306% conversion).",
              s=["farm", "corp"], lc="borrow", neo=[0, ""], src=[["2Q26 MD&A", MDA], ["IT Forum: Banco do Brasil", ITFORUM]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty & benefits", "blurb": "Livelo, Universo, Casa BB.", "div": "ourocard", "rev": "ind", "products": [
            P("livelo", "Livelo", "The points currency on Ourocard, 49.99% owned through Elopar.",
              s=["con", "prem"], lc="grow", o="P", at="Bradesco", neo=[0, ""], src=[["2Q26 MD&A", MDA]]),
            P("universo", "Universo Ourocard", "A gamified spending campaign with Dotz from July 2024 that counted only Visa and Elo spend until March 2026, when Mastercard was added.", short="Universo Ourocard (Mastercard added 2026)",
              s=["con"], lc="grow", st="new", ay="Mar 2026", o="P", at="Dotz", neo=[1, "Mastercard spend counted since March 2026."], src=[["Cartões de Crédito.me: Universo Ourocard, Mar 2026", UNIVERSO]]),
            P("beneficios", "Programa Benefícios BB & Shopping BB", "6.9 million participants and R$45.3 million of points cashback; Shopping BB with 17 million transactions and R$620 million in 1H26.",
              s=["con"], lc="grow", o="B", neo=[0, ""], src=[["2Q26 MD&A", MDA]]),
            P("casabb", "Casa BB lounge", "A 24-hour lounge at Guarulhos Terminal 3 for premium cardholders (opened 1H26), with Mastercard Black holders on the access list.",
              s=["prem"], lc="grow", st="new", neo=[1, "Open to Mastercard Black holders."], src=[["2Q26 MD&A", MDA], ["Cartões e Viagens: Ourocard Mastercard Black", BLACK]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: R$422 billion of farm credit under stress, payroll loans to public servants and retirees, banking for small firms and corporates, public-sector lending, and insurance, asset management and consórcios.",
    "tiles": [
        {"id": "4.1", "ic": "earth", "name": "Agribusiness", "blurb": "R$422bn, NPL above 6%.", "div": "bb", "rev": "agro", "products": [
            P("agro", "Farm credit", "A R$421.6 billion book (+4.1%) for nearly 600,000 clients and more than 200 crops; NPL about 6.27% ⚠ (from a chart) and above 10% on crop financing.",
              s=["farm"], lc="borrow", neo=[0, ""],
              mc="No BB farm-card network is identified ⚠; input-finance cards are untested ground.",
              src=[["2Q26 results", Q2], ["2Q26 MD&A", MDA]]),
            P("regulariza", "BB Regulariza Agro & MP 1.376", "R$39.3 billion renegotiated for 25,600 clients by June 2026 under MP 1.314, and a new MP 1.376/2026 programme reaching up to R$100 billion and 113,000 clients.",
              s=["farm"], lc="borrow", st="new", neo=[0, ""], src=[["2Q26 MD&A", MDA], ["2Q26 results", Q2]]),
        ]},
        {"id": "4.2", "ic": "hand-coins", "name": "Payroll & personal loans", "blurb": "R$154bn payroll book.", "div": "bb", "rev": "ind", "products": [
            P("payroll", "Payroll-deductible loans", "R$153.7 billion: public sector R$113.0 billion, INSS R$28.3 billion and private R$12.4 billion (+128%), including Crédito do Trabalhador for 1.2 million workers; a 19.6% market share.",
              s=["con", "gov"], lc="borrow", neo=[0, ""], src=[["2Q26 MD&A", MDA], ["2Q26 institutional presentation", INST]]),
            P("move", "BB Move Brasil", "Vehicle credit for drivers on Uber, BYD and iFood.",
              s=["con"], lc="borrow", st="new", o="P", at="Uber, BYD, iFood", neo=[0, ""], src=[["2Q26 InformAções", BULLETIN]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "Companies", "blurb": "SMEs to Corporate & IB.", "div": "bb", "rev": "comp", "products": [
            P("sme", "Small businesses", "Government-guaranteed Pronampe and PEAC lines (36% of the SME book guaranteed) and digital business-account openings up 100% in 1H26.",
              s=["sme"], lc="everyday", neo=[0, ""],
              mc="Small-business cards and acceptance are open ground.",
              src=[["2Q26 results", Q2], ["2Q26 MD&A", MDA]]),
            P("cib", "Corporate & investment banking", "Corporate & IB for about 1,200 groups with revenue above R$1.3 billion, Corporate from R$50 million, and UBS BB.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["2Q26 MD&A", MDA]]),
        ]},
        {"id": "4.4", "ic": "landmark", "name": "Government", "blurb": "Municipalities and Fies.", "div": "bb", "rev": "gov", "products": [
            P("gov", "Public sector", "Public-sector lending and Fies student loans, R$79.4 billion disbursed under Eficiência Municipal, and a vice-presidency for government. Government-card networks not verified ⚠.",
              s=["gov"], lc="borrow", neo=[None, "Card network not verified ⚠."],
              mc="Prepaid and benefit disbursement for governments could fit.",
              src=[["2Q26 institutional presentation", INST]]),
        ]},
        {"id": "4.5", "ic": "trending-up", "name": "Insurance, asset & savings", "blurb": "BB Seguridade, BB Asset.", "div": "seguridade", "rev": "group", "products": [
            P("seguridade", "BB Seguridade", "BB Mapfre, Brasilprev and Brasilcap; recurring income of R$2.15 billion in 2Q26 (−3.9%); BB claims first place in rural insurance and pensions.",
              s=["con", "farm"], lc="grow", neo=[0, ""], src=[["Mercado & Consumo: 2Q26, Aug 2026", Q2PRESS], ["2Q26 institutional presentation", INST]]),
            P("asset", "BB Asset, Consórcios & private banking", "About R$1.9 trillion under management ⚠ (from a chart), consórcios of R$156.7 billion (13.7% share), Tesouro Reserva with B3 and the Treasury (R$3.9 billion by 30 June 2026), and what BB calls Brazil's largest private-banking office network.",
              s=["prem", "con"], lc="grow", neo=[0, ""], src=[["2Q26 MD&A", MDA]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the new BB 5.0 app for 35 million digital users, 3,931 branches and 18,221 correspondents in 94% of municipalities, and digital hubs growing to 500.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "App BB", "blurb": "35m digital users.", "div": "bb", "rev": "ind", "products": [
            P("app", "App BB & BB 5.0", "35 million active digital users and 94% of transactions digital; BB 5.0, a personalised app announced on 23 April 2026, reached 29 million users in 90 days; 54 million digital clients targeted by 2030; Pix by voice and image on WhatsApp.",
              s=["con", "prem"], lc="everyday", st="new", neo=[0, ""], src=[["2Q26 MD&A", MDA], ["LetsMoney: BB Day, Apr 2026", BBDAY], ["2Q26 InformAções", BULLETIN]]),
            P("apppj", "App BB PJ & Painel PJ", "About 278,000 business users.",
              s=["sme"], lc="everyday", neo=[0, ""], src=[["2Q26 MD&A", MDA]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & correspondents", "blurb": "94% of municipalities.", "div": "bb", "rev": "ind", "products": [
            P("branches", "Branches, MaisBB & ATMs", "3,931 branches, 6,445 service points and 18,221 MaisBB correspondents in 94% of municipalities, and about 43,000 ATMs ⚠ (undated).",
              s=["con", "farm", "gov"], lc="open", neo=[0, ""], src=[["2Q26 institutional presentation", INST], ["LetsMoney: BB Day, Apr 2026", BBDAY], ["IT Forum: Banco do Brasil", ITFORUM]]),
        ]},
        {"id": "5.3", "ic": "headset", "name": "Digital hubs", "blurb": "100 to 500 by Dec 2026.", "div": "bb", "rev": "ind", "products": [
            P("hubs", "Digital hubs", "About 2.9 million clients served remotely, human service in the app for every customer, and hubs growing from 100 to 500 by December 2026.",
              s=["con", "prem"], lc="everyday", st="new", neo=[0, ""], src=[["2Q26 MD&A", MDA], ["LetsMoney: BB Day, Apr 2026", BBDAY]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Banco do Brasil", "blurb": "Third, behind Elo and Visa.", "products": [
        P("mcatbb", "Mastercard at Banco do Brasil", "BB co-owns Elo and puts Visa on its Altus premium cards and its first agentic purchase. Mastercard keeps the Ourocard Mastercard Black, Platinum and Gold, joined Universo Ourocard in March 2026 and serves Black holders at Casa BB. No BB–Mastercard contract, renewal or joint initiative was found; Caixa reportedly stopped new Mastercard credit cards in 2026 ⚠.",
          s=["con"], div="bb", rev="group", mc="The relationship this map is drawn for.",
          src=[["Cartões de Crédito.me: Universo Ourocard, Mar 2026", UNIVERSO], ["Diário do Comércio: Caixa cards, Jul 2026", CAIXA]]),
    ]},
    {"id": "pillar-market", "name": "Brazilian banking", "blurb": "Farm losses, Pix, agents.", "products": [
        P("market", "The Brazilian market", "BB holds 16.1% of loans and 17.3% of deposits; profits fell on farm credit under new expected-loss rules (CMN 4.966); Pix keeps adding features; Mastercard says Brazil is its second Click to Pay market with 40% of transactions tokenised (February 2025); and general elections in October 2026 may bring leadership change ⚠.",
          s=["con"], div="bb", rev="group", src=[["2Q26 institutional presentation", INST], ["4Q25 results", FY25], ["Finsiders: Click to Pay, Feb 2025", CLICKTOPAY], ["BB investor relations", IR]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
