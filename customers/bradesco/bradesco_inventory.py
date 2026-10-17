"""Banco Bradesco's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the 2Q26 results (6 August 2026), the 4Q25 results
(6 February 2026) and the 2025 Form 20-F (25 March 2026). ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

F20 = "https://www.sec.gov/Archives/edgar/data/1160330/000129281426001753/bbdform20f_2025.htm"
Q2 = "https://www.sec.gov/Archives/edgar/data/1160330/000129281426004099/bbdpr2q26_6k.htm"
FY25 = "https://www.sec.gov/Archives/edgar/data/1160330/000129281426000261/bbdpr4q25_6k.htm"
CALL = "https://allmind.ai/earnings/event/2944321"
GUID = "https://www.sec.gov/Archives/edgar/data/1160330/000129281426000245/0001292814-26-000245-index.htm"
CAPITAL = "https://www.sec.gov/Archives/edgar/data/1160330/000129281426003966/0001292814-26-003966-index.htm"
CAPOCT = "https://www.sec.gov/Archives/edgar/data/1160330/000129281426004874/bbd20261008_6k.htm"
BLACKROCK = "https://www.sec.gov/Archives/edgar/data/1160330/000129281426004912/bbd20261013_6k.htm"
ELOINC = "https://www.sec.gov/Archives/edgar/data/1160330/000129281425001403/0001292814-25-001403-index.htm"
ELOEQ = "https://www.sec.gov/Archives/edgar/data/1160330/000129281425002043/0001292814-25-002043-index.htm"
ALELO = "https://www.sec.gov/Archives/edgar/data/1160330/000129281425002733/0001292814-25-002733-index.htm"
CIELO = "https://www.sec.gov/Archives/edgar/data/1160330/000129281426000080/0001292814-26-000080-index.htm"
AGRI = "https://www.sec.gov/Archives/edgar/data/1160330/000129281426000389/0001292814-26-000389-index.htm"
BRB = "https://www.sec.gov/Archives/edgar/data/1160330/000129281426002332/0001292814-26-002332-index.htm"
BRADSAUDE = "https://www.sec.gov/Archives/edgar/data/1160330/000129281426002726/0001292814-26-002726-index.htm"
QUOTE = "https://hgbrasil.com/finance/tickers/B3:BBDC4"
ELOIPO = "https://www.moneytimes.com.br/ipo-a-vista-elo-contrata-bancos-para-abertura-de-capital-nos-eua-dizem-fontes-igdl/"
DIGIO = "https://www.suno.com.br/noticias/?p=192564"
NEXT = "https://istoedinheiro.com.br/bradesco-reincorporacao-next-na-virada-do-ano"
FINS = "https://finsidersbrasil.com.br/noticias-sobre-fintechs/pagamentos-agenticos-avancam-no-brasil-e-atraem-bancos-bandeiras-e-fintechs/"
AGENTPAY = "https://tiinside.com.br/10/12/2025/mastercard-anuncia-implementacao-do-agent-pay-na-america-latina-para-acelerar-adocao-de-pagamentos-por-ia/"
PIXAUTO = "https://www.portalin.com.br/negocios/bradesco-lanca-pix-automatico-para-pagamentos-recorrentes-de-pessoas-fisicas-e-juridicas/"
CARDS = "https://banco.bradesco/html/classic/produtos-servicos/cartoes/index.shtm"
DEBIT = "https://banco.bradesco/html/classic/produtos-servicos/cartoes/debito.shtm"
DISNEY = "https://banco.bradesco/cartaodisney"
BLACK = "https://passageirodeprimeira.com/?p=335760"
AMAZON = "https://fstech.co.uk/fst/Amazon_Banco_Bradesco_Credit_Card.php"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · control · stakes", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: 74 million clients and R$1.14 trillion of loans, ten straight quarters of rising profit, a bank founded in 1943 near São Paulo, a R$10 billion capital raise, and stakes in Elo, Cielo, Livelo and Alelo shared with Banco do Brasil.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "R$7.05bn in 2Q26, ROAE 16.2%.", "div": "bradesco", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Recurring net income of R$7.05 billion in 2Q26 (ROAE 16.2%, the tenth straight quarter of growth) and R$24.7 billion in 2025; an expanded loan book of R$1,136.6 billion; CET1 11.3%; card income R$4.49 billion, 43% of fees. 74.3 million clients and 82,095 staff at the end of 2025. Bradesco's own ratings were not retrieved ⚠; the market value is not reliably known ⚠.",
              s=["con"], neo=[0, ""], src=[["2Q26 results", Q2], ["4Q25 results", FY25], ["Form 20-F 2025", F20], ["HG Brasil: BBDC4", QUOTE]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & capital", "blurb": "Noronha, and R$10bn new capital.", "div": "bradesco", "rev": "group", "products": [
            P("leadership", "Board & executives", "Chair Luiz Carlos Trabuco Cappi; CEO Marcelo Noronha (since November 2023, who once ran Bradesco Cartões); CFO Cassiano Scarpelli; José Ramos Rocha Neto sits on the Cielo, Elo and Livelo boards; Fernando Freiberger runs Bradesco Payments and banking-as-a-service. The head of cards is not identified ⚠.",
              s=["corp"], neo=[0, ""], src=[["Form 20-F 2025", F20]]),
            P("capital", "R$10 billion capital increase", "Announced 29 July 2026 for technology, commercial efficiency and growth, fully subscribed and approved by the central bank on 8 October 2026; the controlling shareholders committed up to R$8 billion. BlackRock holds 10.06% of the preferred shares.",
              s=["corp"], st="new", neo=[0, ""], src=[["Capital increase, Jul 2026", CAPITAL], ["Central-bank approval, Oct 2026", CAPOCT], ["BlackRock holding, Oct 2026", BLACKROCK]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & reach", "blurb": "Founded 1943 in Osasco.", "div": "bradesco", "rev": "group", "products": [
            P("brands", "Heritage & reach", "Founded in 1943 as Banco Brasileiro de Descontos, Brazil's largest private bank by the late 1960s and renamed in 1988; headquartered at Cidade de Deus, Osasco, with branches or units in New York, Cayman, Luxembourg, Miami, Mexico, Hong Kong and London.",
              s=["con"], o="I", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy", "blurb": "Ten priorities, ROAE above cost.", "div": "bradesco", "rev": "group", "products": [
            P("strategy", "Transformation & 2026 guidance", "Ten priorities: a physical bank at 'adequate cost' for high-return clients and an 'efficient digital bank with humanized experience and AI'. Fewer management layers and outside hires; 2026 guidance of 8.5–10.5% loan growth and 3–5% fee growth, unchanged at 2Q26. 4Q25 was the first quarter with returns above the cost of capital.",
              s=["corp"], st="new", neo=[0, ""], src=[["Form 20-F 2025", F20], ["2026 guidance", GUID], ["4Q25 results", FY25]]),
        ]},
        {"id": "1.5", "ic": "network", "name": "Stakes & deals", "blurb": "Elo, Cielo, Digio, Bradsaúde.", "div": "elopar", "rev": "group", "products": [
            P("stakes", "Stakes & deals", "50.01% of Elopar (with Banco do Brasil), which holds Elo, Livelo and Alelo; joint control of Cielo, delisted in September 2024; all of Digio (BB's half bought for R$625 million, 2021); 50% of Banco John Deere (February 2025); 91.35% of Bradsaúde (May 2026); hospitals with Rede D'Or; BRB loan portfolios bought with Itaú (April 2026). iFood was reported in July 2025 to be negotiating for Alelo; Bradesco said it had no formal proposal.",
              s=["corp"], o="A", neo=[0, ""], src=[["Form 20-F 2025", F20], ["Suno: Digio buyout, Oct 2021", DIGIO], ["Bradsaúde closing, May 2026", BRADSAUDE], ["BRB portfolios, Apr 2026", BRB], ["Alelo clarification, Jul 2025", ALELO]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "How money moves: R$360 billion of credit-card spending across Elo, Visa, Mastercard and Amex, premium tiers led by Visa and Amex with a Mastercard Black, the Amazon co-brand on Mastercard and Disney on Visa, Pix and Pix Automático, Elo and Cielo co-owned with Banco do Brasil, and trade and FX.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "R$360bn on four networks.", "div": "cartoes", "rev": "ind", "products": [
            P("credit", "Bradesco credit cards", "R$360.4 billion of spending on 2.714 billion transactions in 2025 and card income of R$18.2 billion; high-income clients bring about 52% of card revenue, up 29% in 2Q26. The 20-F lists Elo, American Express, Visa and Mastercard; no split is published.", short="Credit cards (four networks)",
              s=["con", "hnw"], lc="borrow", o="B", neo=[1, "Elo, Visa, Mastercard and Amex; split not published."], src=[["Form 20-F 2025", F20], ["2Q26 results", Q2]]),
            P("elocards", "Elo cards", "Elo Nanquim (top tier, VIP lounges), Elo Diners, Elo Grafite and Elo Mais.", short="Elo cards",
              s=["con", "hnw"], lc="borrow", o="P", at="Elo", neo=[0, "Elo."], src=[["Bradesco: cards", CARDS], ["Form 20-F 2025", F20]]),
            P("visacards", "Visa cards", "Visa Aeternum and Infinite for high net worth, and Visa Signature, Platinum and the no-fee Neo Visa Platinum for the mass affluent.", short="Visa cards",
              s=["con", "hnw"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Bradesco: cards", CARDS], ["Form 20-F 2025", F20]]),
        ]},
        {"id": "2.2", "ic": "gem", "name": "Premium & Amex", "blurb": "Black, Centurion, Principal.", "div": "cartoes", "rev": "ind", "products": [
            P("mcblack", "Mastercard Black", "A high-net-worth card, relaunched in February 2024 with a lifetime-free version and one earning Livelo points; Mastercard Black lounge at Guarulhos T2, LoungeKey and Priceless.", short="Mastercard Black",
              s=["hnw"], lc="borrow", ay="Feb 2024", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's clearest premium foothold at Bradesco.",
              src=[["Passageiro de Primeira: Mastercard Black, Feb 2024", BLACK], ["Form 20-F 2025", F20]]),
            P("amex", "American Express cards", "Bradesco issues Amex in Brazil, including The Centurion Card, The Platinum Card, Gold and Green, and once ran the Amex network.", short="Amex (Bradesco-issued)",
              s=["hnw"], lc="borrow", o="P", at="American Express", neo=[0, "American Express."], src=[["Form 20-F 2025", F20], ["Bradesco: cards", CARDS]]),
            P("principalcard", "Bradesco Principal card", "A card for Principal clients with VIP rooms; network not disclosed.",
              s=["hnw"], lc="borrow", st="new", neo=[None, "Network not disclosed."],
              mc="An open premium contest as Principal grows to 70+ cities.",
              src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "2.3", "ic": "store", "name": "Co-brands & private label", "blurb": "Amazon, Disney, Bradescard.", "div": "cartoes", "rev": "ind", "products": [
            P("amazon", "Amazon co-brand credit card", "Launched in August 2023 with Bradesco carrying the credit risk; on Mastercard. Current status and tier not verified ⚠.", short="Amazon card (Mastercard)",
              s=["con"], lc="borrow", ay="Aug 2023", o="P", at="Amazon, Mastercard", neo=[2, "Mastercard ⚠ status."], src=[["FStech: Amazon card, Aug 2023", AMAZON]]),
            P("disney", "Disney Visa Infinite & Signature", "A co-brand with Disney+ included, 1–3% loyalty earn and a travel platform; fee of 12 × R$119.", short="Disney card (Visa)",
              s=["con"], lc="borrow", o="P", at="Disney, Visa", neo=[0, "Visa."], src=[["Bradesco: Disney card", DISNEY]]),
            P("bradescard", "Bradescard & Bradescard México", "Hybrid and private-label cards with retail partners, some closed-loop, and an exclusive card operation with Mexican retail chains; partners and networks not retrieved ⚠.",
              s=["con"], lc="borrow", o="B", neo=[None, "Networks not disclosed."], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Debit & wallets", "blurb": "Visa and Elo promoted.", "div": "bradesco", "rev": "ind", "products": [
            P("debit", "Debit & multiple cards", "Contactless debit and combined credit-debit cards with an on/off switch in the app; the debit page promotes 'Vai de Visa' and 'Programa Use Elo' and does not mention Mastercard. Split not disclosed ⚠.",
              s=["con", "mei"], lc="everyday", o="P", at="Visa, Elo", neo=[0, "Visa and Elo promoted ⚠."], src=[["Bradesco: debit", DEBIT], ["Form 20-F 2025", F20]]),
            P("wallets", "Wallets & virtual cards", "Apple Pay, Google Pay and Samsung Pay (cards added in the app after unlocking at an ATM) and virtual card numbers for online shopping. No Mastercard-specific token or Click to Pay announcement found.",
              s=["con"], lc="everyday", o="P", at="Apple, Google, Samsung", neo=[1, "Tokens on whichever network the card carries."], src=[["Bradesco: debit", DEBIT], ["Bradesco: cards", CARDS]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Pix", "blurb": "Pix Automático from April 2025.", "div": "bradesco", "rev": "ind", "products": [
            P("pix", "Pix", "Brazil's instant payments in every app, including text and voice Pix through the BIA assistant. The central bank suspended Pix Parcelado, instalments on Pix, at the end of 2025.",
              s=["con", "mei"], lc="move", o="P", at="Central Bank of Brazil", neo=[0, "Pix."], src=[["Form 20-F 2025", F20], ["2Q26 call", CALL]]),
            P("pixauto", "Pix Automático", "Recurring Pix, launched by Bradesco on 3 April 2025 for its own corporate billers and nationally from 16 June 2025.",
              s=["mei", "corp"], lc="move", st="new", ay="Apr 2025", neo=[0, "Pix."],
              mc="Pix Automático competes with card-on-file subscriptions.",
              src=[["Portal IN: Pix Automático, Apr 2025", PIXAUTO]]),
        ]},
        {"id": "2.6", "ic": "network", "name": "Elo & Alelo", "blurb": "A network it co-owns.", "div": "elopar", "rev": "ind", "products": [
            P("elo", "Elo", "The domestic network launched in 2011 by Bradesco, Banco do Brasil and Caixa: 34 million active cards, 37 issuers and R$310.9 billion of spending in 2025. An incentive deal of 2 April 2025 pays Bradesco to issue Elo cards until 31 December 2034; holdings are being equalised to a third each ⚠ (completion not confirmed); advisers hired for a possible US listing (May 2026).", short="Elo (co-owned)",
              s=["con"], lc="move", ay="Apr 2025", o="P", at="Banco do Brasil, Caixa", neo=[0, "Elo."],
              mc="Mastercard's structural rival at Bradesco, with incentives locked in to 2034.",
              src=[["Elo incentive programme, Apr 2025", ELOINC], ["Elo equalisation, May 2025", ELOEQ], ["Money Times: Elo IPO, May 2026", ELOIPO]]),
            P("alelo", "Alelo", "Meal and benefit cards through Elopar; network not checked ⚠.",
              s=["mei", "corp"], lc="everyday", o="P", neo=[None, "Network not checked ⚠."], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "2.7", "ic": "store", "name": "Acceptance (Cielo)", "blurb": "Jointly controlled acquirer.", "div": "cielo", "rev": "msme", "products": [
            P("cielo", "Cielo", "Brazil's acquirer, jointly controlled with Banco do Brasil and delisted in September 2024; Bradesco is paid to refer and keep merchants under an agreement renewed in January 2026 that renews every 12 months.",
              s=["mei", "merch"], lc="move", o="P", at="Banco do Brasil", neo=[1, "Multi-network acceptance."], src=[["Cielo agreement, Jan 2026", CIELO], ["Form 20-F 2025", F20]]),
            P("netempresa", "Net Empresa acceptance", "Instant QR codes, TEF, POS, e-commerce, Cielo machines and payment links, all contracted online.",
              s=["mei", "merch"], lc="move", neo=[1, "Multi-network acceptance."], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "2.8", "ic": "earth", "name": "Trade, FX & international", "blurb": "832 correspondent banks.", "div": "bbi", "rev": "large", "products": [
            P("fx", "Global Trade & Finance", "832 correspondent banks; 11.0% of Brazil's export market and 9.1% of imports.",
              s=["corp"], lc="move", neo=[0, ""],
              mc="Cross-border flows are untested ground for Mastercard Move.",
              src=[["Form 20-F 2025", F20]]),
            P("intlaccount", "International Account", "A full US checking account for Principal clients, with debit and credit cards; network not disclosed.",
              s=["hnw"], lc="move", st="new", neo=[None, "Network not disclosed."], src=[["Form 20-F 2025", F20]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: BIA, a generative-AI assistant open to all clients, the inovabra innovation hub and open finance, round-the-clock fraud monitoring, and Livelo points, Viva Prime offers and Mastercard Surpreenda.",
    "tiles": [
        {"id": "3.1", "ic": "bot", "name": "AI & innovation", "blurb": "BIA for every client.", "div": "bradesco", "rev": "ind", "products": [
            P("bia", "BIA", "An assistant since 2016, on Bradesco's own generative-AI platform since 2025, in the app, WhatsApp, the corporate portal and by phone; it makes Pix by text or voice, pays bills, activates cards and sends fraud alerts. Open to all clients, with 74 million interactions ⚠ (period not given).",
              s=["con", "mei"], lc="everyday", o="B", neo=[0, ""],
              mc="Bradesco is in Visa's agentic programme but not Mastercard's first Agent Pay wave.",
              src=[["Form 20-F 2025", F20], ["2Q26 call", CALL]]),
            P("inovabra", "inovabra & open finance", "An innovation hub with 346 resident start-ups and a sandbox that simulates the core system; an open-finance participant, with no Bradesco metrics found ⚠.",
              s=["corp"], lc="open", o="B", neo=[None, "No provider disclosed."], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud & security", "blurb": "24/7 monitoring.", "div": "bradesco", "rev": "ind", "products": [
            P("fraud", "Fraud prevention", "Real-time monitoring around the clock across the app, internet banking, Net Empresa, phone, BIA on WhatsApp, cards and account opening; screen masking and warnings about fake call centres. Vendor not disclosed.",
              s=["con", "mei"], lc="everyday", neo=[None, "Vendor not disclosed."],
              mc="Scam and card-fraud intelligence across cards and Pix is a stated need.",
              src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty & offers", "blurb": "Livelo, Viva Prime, Surpreenda.", "div": "elopar", "rev": "ind", "products": [
            P("livelo", "Livelo", "The coalition loyalty programme owned through Elopar with Banco do Brasil; points on Bradesco cards.",
              s=["con", "hnw"], lc="grow", o="P", at="Banco do Brasil", neo=[0, ""], src=[["Form 20-F 2025", F20], ["Bradesco: cards", CARDS]]),
            P("viva", "Viva Prime, Menu & Cinemark", "Offers and discounts, including up to 15% off restaurants with Menu, Cinemark and Teatro Bradesco.",
              s=["con"], lc="grow", o="B", neo=[0, ""], src=[["Bradesco: cards", CARDS]]),
            P("surpreenda", "Mastercard Surpreenda", "Mastercard's promotions programme, the only Mastercard item on Bradesco's cards page.", short="Surpreenda (Mastercard)",
              s=["con"], lc="grow", o="P", at="Mastercard", neo=[3, "Mastercard's own."], src=[["Bradesco: cards", CARDS]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: payroll, home and vehicle loans, banking for small firms and MEIs, corporate, investment and agribusiness banking, Principal and Private for the wealthy, what Bradesco calls Latin America's largest insurance group, and Digio.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Lending to individuals", "blurb": "R$480bn book.", "div": "bradesco", "rev": "ind", "products": [
            P("payroll", "Payroll-deductible loans", "A 14.1% market share and 25.7% of INSS retiree benefit payments; private-sector payroll lending growing. Individuals' loans R$479.7 billion (+8.4%).",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Form 20-F 2025", F20], ["2Q26 results", Q2]]),
            P("homeauto", "Homes, vehicles & consortia", "381,000 mortgage contracts (10.2% of the loan book), vehicle loans to individuals up 26.8% in 2Q26, and a 21.8% share in auto consortia.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Form 20-F 2025", F20], ["2Q26 results", Q2]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "Small firms & MEIs", "blurb": "Loans up 16%.", "div": "bradesco", "rev": "msme", "products": [
            P("smes", "Empresas e Negócios", "Banking for firms with up to R$50 million of revenue: 150 new SME branches and 10 middle-market platforms in 1Q25, a free MEI app used by 50,000 by August 2025, and loans of R$267.5 billion, up 16.1%.",
              s=["mei"], lc="everyday", st="new", neo=[0, ""],
              mc="Small-business cards and acceptance are open ground.",
              src=[["Form 20-F 2025", F20], ["2Q26 results", Q2]]),
        ]},
        {"id": "4.3", "ic": "factory", "name": "Corporate & agribusiness", "blurb": "BBI, Ultra, R$120bn agri.", "div": "bbi", "rev": "large", "products": [
            P("corporate", "Bradesco BBI & Corporate", "Corporate, Large, Ultra and Global coverage for firms with revenue from R$50 million to more than R$5 billion; large-corporate loans R$389.4 billion (+12.7%); a global platform for all wholesale clients and 38% of leasing.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Form 20-F 2025", F20], ["2Q26 results", Q2]]),
            P("agri", "Agribusiness & Banco John Deere", "A direct agribusiness book of about R$120 billion expected to grow 15–20% in 2026, and equipment finance through 50% of Banco John Deere.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Agribusiness clarification, Feb 2026", AGRI], ["Form 20-F 2025", F20]]),
        ]},
        {"id": "4.4", "ic": "gem", "name": "Wealth", "blurb": "Principal, Prime, Private, Ágora.", "div": "principal", "rev": "ind", "products": [
            P("principal", "Principal, Prime & Private", "Bradesco Principal for high-net-worth clients (November 2024; more than 320,000 clients, 62 offices in 36 cities, 70+ cities targeted by end-2026), Prime for the affluent, and Global Private Bank with 13 offices plus Miami and Luxembourg.",
              s=["hnw"], lc="grow", st="new", ay="Nov 2024", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
            P("invest", "Ágora & Bradesco Asset", "Ágora brokerage with 1.4 million clients and R$128 billion in custody; Bradesco Asset with a 16.1% share and R$984 million of fees in 2Q26.",
              s=["hnw", "con"], lc="grow", neo=[0, ""], src=[["Form 20-F 2025", F20], ["2Q26 results", Q2]]),
        ]},
        {"id": "4.5", "ic": "shield-check", "name": "Insurance & health", "blurb": "22.8% of premiums.", "div": "seguros", "rev": "ins", "products": [
            P("seguros", "Bradesco Seguros", "Auto, property, life, pensions and capitalisation; R$118.5 billion of revenue and R$10.1 billion of net income in 2025, R$2.94 billion in 2Q26 (ROAE 22.8%), and a 22.8% share of premiums.",
              s=["ins"], lc="grow", neo=[0, ""], src=[["Form 20-F 2025", F20], ["2Q26 results", Q2]]),
            P("health", "Bradsaúde & hospitals", "Bradsaúde, formerly Odontoprev, holds all the health businesses (91.35%, May 2026); hospitals through Atlântica D'Or with Rede D'Or.",
              s=["ins"], lc="beyond", st="new", ay="May 2026", o="A", neo=[0, ""], src=[["Bradsaúde closing, May 2026", BRADSAUDE], ["Form 20-F 2025", F20]]),
        ]},
        {"id": "4.6", "ic": "smartphone", "name": "Digio & digital retail", "blurb": "10m Digio clients.", "div": "digio", "rev": "ind", "products": [
            P("digio", "Digio", "A digital bank with 10.0 million clients, a R$20.5 billion portfolio and R$4.2 billion of revenue; payroll loans, cards and a white-label platform. Its 2026 goal is to 'monetize the base of cards'. Card network not disclosed.",
              s=["con"], lc="everyday", o="A", neo=[None, "Network not disclosed."],
              mc="Issuer processing and banking-as-a-service for Digio's white label could fit.",
              src=[["Form 20-F 2025", F20], ["Suno: Digio buyout, Oct 2021", DIGIO]]),
            P("next", "Digital Retail & next", "The entry segment, physical and digital; next was folded back into Bradesco at the turn of 2024 and the Bitz wallet closed in 2023.",
              s=["con"], lc="open", st="retired", neo=[0, ""], src=[["IstoÉ Dinheiro: next, Dec 2023", NEXT]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: 1,844 branches and 39,000 ATMs, 39,000 Bradesco Expresso correspondents, and an app used by 28.5 million people, with 99% of transactions digital.",
    "tiles": [
        {"id": "5.1", "ic": "building", "name": "Branches & ATMs", "blurb": "1,844 branches.", "div": "bradesco", "rev": "ind", "products": [
            P("branches", "Branches & ATMs", "1,844 branches in June 2026 (1,509 retail and Prime, 150 for small firms, 90 corporate, 95 platforms) and 39,245 ATMs, 26,705 of them Banco24Horas.",
              s=["con", "mei"], lc="open", st="flux", neo=[0, ""], src=[["2Q26 results", Q2], ["Form 20-F 2025", F20]]),
        ]},
        {"id": "5.2", "ic": "users-round", "name": "Bradesco Expresso", "blurb": "39,335 correspondents.", "div": "bradesco", "rev": "ind", "products": [
            P("expresso", "Bradesco Expresso", "39,335 correspondent points in shops, with 25.5 million transactions a month (December 2025).",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Form 20-F 2025", F20]]),
        ]},
        {"id": "5.3", "ic": "smartphone", "name": "Apps & channels", "blurb": "28.5m app users.", "div": "bradesco", "rev": "ind", "products": [
            P("app", "Bradesco app", "28.5 million active individual app users at the end of 2025, and 99% of transactions on digital channels; 'more than 30 million' fully digital clients ⚠ (the CFO said 36 million).",
              s=["con", "hnw"], lc="everyday", neo=[0, ""], src=[["Form 20-F 2025", F20], ["2Q26 results", Q2], ["2Q26 call", CALL]]),
            P("channels", "Business apps & assisted channels", "Net Empresa, the MEI app, Bradesco Cartões and Ágora apps, BIA on WhatsApp and by phone, and Fone Fácil.",
              s=["mei", "corp"], lc="open", neo=[0, ""], src=[["Form 20-F 2025", F20], ["Bradesco: cards", CARDS]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Bradesco", "blurb": "Black, Amazon and Surpreenda.", "products": [
        P("mcatbradesco", "Mastercard at Bradesco", "Bradesco co-owns Elo and is paid to issue Elo cards until 2034; Visa carries its top premium tiers and the Disney co-brand, and Bradesco issues Amex. Mastercard is visible in Mastercard Black (relaunched 2024), the Amazon co-brand (2023) and Surpreenda promotions. No Mastercard master agreement or switch was found, and Bradesco was not among Mastercard's first Agent Pay partners in Latin America.",
          s=["con"], div="bradesco", rev="group", mc="The relationship this map is drawn for.",
          src=[["Elo incentive programme, Apr 2025", ELOINC], ["Passageiro de Primeira: Mastercard Black, Feb 2024", BLACK], ["TI Inside: Agent Pay in Latin America, Dec 2025", AGENTPAY]]),
    ]},
    {"id": "pillar-market", "name": "Brazilian banking", "blurb": "Pix, Elo, agentic payments.", "products": [
        P("market", "The Brazilian market", "Itaú, Caixa, Banco do Brasil and Santander compete for deposits; Pix Automático is live and Pix Parcelado suspended; the Selic is about 14%; and Visa named Bradesco in its Agentic Ready programme (August 2026), while Mastercard's first Agent Pay partners (December 2025) did not include it.",
          s=["con"], div="bradesco", rev="group", src=[["Form 20-F 2025", F20], ["Finsiders: agentic payments, Aug 2026", FINS], ["TI Inside: Agent Pay in Latin America, Dec 2025", AGENTPAY]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
