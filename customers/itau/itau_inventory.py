"""Itaú's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Itaú's own unless a source says otherwise: the 2Q26 MD&A and results (4–7 August 2026)
and the FY2025 20-F (29 April 2026). Amounts in reais (R$). ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product or network runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

SEC = "https://www.sec.gov/Archives/edgar/data/1132597/"
MDA = SEC + "000113259726000223/managementdiscussionanal.htm"
F20 = SEC + "000113259726000132/itub-20251231.htm"
MDA1Q = SEC + "000113259726000164/managementdiscussionanal.htm"
MZ = "https://api.mziq.com/mzfilemanager/v2/d/42787847-4cf6-4461-94a5-40ed237dca33/"
PR2Q = MZ + "a886b521-389e-da70-dbb1-0be7758c8d91?origin=2"
DECK2Q = MZ + "d5fdc4fc-90be-85fb-51e7-7fd7f3770930?origin=2"
PR4Q = "https://filemanager-cdn.mziq.com/published/42787847-4cf6-4461-94a5-40ed237dca33/8b83aad9-1ed2-47a5-ac9b-d0807a8ee955_itau_unibanco_holding_s.a..pdf"
MC2015 = "https://investor.mastercard.com/investor-news/investor-news-details/2015/Ita-and-MasterCard-Sign-Agreement-That-Expands-Relationship/default.aspx"
CADE = "https://www.gov.br/cade/en/matters/news/cade-approves-with-restrictions-joint-venture-between-itau-unibanco-and-mastercard"
HIPER = "https://www.cerc.com/wp-content/uploads/2025/07/Instituicao-de-pagamento-__-Arranjo-de-pagamento-Encerramento-do-Arranjo-Hipercard-e-Migracao-para-Mastercard-1.pdf"
LEGEND = "https://www.bloomberglinea.com.br/negocios/itau-e-c6-apostam-em-novo-cartao-premium-da-mastercard-para-atender-milionarios/"
AGENTPAY = "https://www.mobiletime.com.br/noticias/24/03/2026/mastercard-agentes-ia/"
LETS = "https://www.letsmoney.com.br/noticias/"
FINSIDERS_CARDS = "https://finsidersbrasil.com.br/pagamentos/cartoes/nubank-cresce-o-dobro-do-mercado-de-cartoes-e-os-bancoes-assistem-a-festa-pela-janela/"
IR = "https://www.itau.com.br/relacoes-com-investidores/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · control · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a R$3.2 trillion balance sheet earning a 24% return, two founding families who still control it, a century of mergers from Unibanco and Itaú to CorpBanca, a bank 70% in the cloud, and an 'AI First' strategy.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & capital", "blurb": "R$3.2 trillion, ROE 24%.", "div": "iuh", "rev": "corp", "products": [
            P("balance", "Balance sheet", "Total assets of R$3.23 trillion, a credit portfolio of R$1.52 trillion (up 9.6%) and deposits of R$1.13 trillion at June 2026; 90,429 employees.",
              s=["inv"], neo=[0, ""], src=[["2Q26 MD&A", MDA]]),
            P("earnings", "Earnings", "A record recurring managerial result of R$46.8 billion in 2025 (ROE 23.4%) and R$12.4 billion in 2Q26 (ROE 24.3%, 25.7% in Brazil), with an efficiency ratio of 37.4%; Brazil is about 95% of the result.",
              s=["inv"], neo=[0, ""], src=[["2Q26 MD&A", MDA], ["4Q25 results", PR4Q]]),
            P("capital", "Capital, ratings & payouts", "CET1 of 12.3%; rated Ba2 (Moody's) and BB+ (Fitch) for the holding, at or above Brazil's sovereign. R$33.7 billion paid out for 2025 (a 72% payout), plus R$23.4 billion brought forward in November 2025 ahead of the dividend-tax change; market value about US$96 billion (July 2026).",
              s=["inv"], neo=[0, ""], src=[["2Q26 MD&A", MDA], ["Itaú IR: ratings", IR + "en/itau-unibanco/ratings-and-fixed-income/"]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Control & leadership", "blurb": "Two families, one CEO.", "div": "iuh", "rev": "corp", "products": [
            P("control", "IUPAR, Itaúsa & the Moreira Salles", "IUPAR holds 51.7% of the voting shares, jointly controlled by Itaúsa (the Setubal and Villela families) and the Moreira Salles family; co-chairs Pedro Moreira Salles and Roberto Setubal. Listed on B3 and the NYSE.",
              s=["inv"], neo=[0, ""], src=[["FY2025 20-F", F20]]),
            P("leadership", "Leadership", "CEO Milton Maluhy Filho since 2021 (also Febraban chair from April 2026); CFO Gabriel Amado de Moura; André Rodrigues runs retail for individuals, Carlos Vanzo SMEs and Rede, Flávio Souza Itaú BBA, Ricardo Guerra technology and operations.",
              s=["inv"], neo=[0, ""], src=[["FY2025 20-F", F20]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage", "blurb": "Unibanco 1924, Itaú 1945.", "div": "iuh", "rev": "corp", "products": [
            P("heritage", "A century of mergers", "Unibanco began as Casa Moreira Salles in 1924; Itaú as Banco Central de Crédito, first branch 1945, Banco Itaú from 1973. Itaú BBA formed in 2002; the Itaú–Unibanco merger (2008) was then Brazil's largest; Itaú CorpBanca (Chile, 2016) became Banco Itaú Chile; Argentina was sold to Banco Macro in 2023.",
              s=["inv", "latam"], o="I", neo=[0, ""], src=[["FY2025 20-F", F20]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI core", "blurb": "70% in the cloud.", "div": "iuh", "rev": "corp", "products": [
            P("cloud", "Cloud & engineering", "A ten-year AWS deal (November 2020) has moved about 70% of services to public cloud, aiming for all by 2028; technology spending was R$11.7 billion in 2025 (up 18%); Cognition's Devin is used by about three-quarters of technology teams, and more than 750 generative-AI initiatives are running.",
              s=["inv"], o="P", at="AWS, Cognition", neo=[0, ""],
              src=[["AWS: Itaú selects AWS, Nov 2020", "https://press.aboutamazon.com/2020/11/itau-unibanco-selects-aws-as-its-long-term-strategic-cloud-provider-to-accelerate-digital-transformation"], ["Baguete: Itaú and Cognition's agent, Jan 2026", "https://www.baguete.com.br/noticias/itau-usa-agente-de-ia-da-cognition"]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy", "blurb": "One Itaú, AI First.", "div": "iuh", "rev": "corp", "products": [
            P("strategy", "One Itaú & AI First", "One app, a conversational rather than transactional bank, fewer branches (2,210 from 2,738 a year earlier) and a 2026 credit-growth guide of 5.5–9.5%; fee and insurance growth guidance was cut to 2–5% in August 2026.",
              s=["con", "aff", "inv"], st="new", neo=[0, ""], src=[["2Q26 results", PR2Q], ["2Q26 MD&A", MDA]]),
            P("esg", "Sustainable finance", "R$605 billion of sustainable finance since 2020 against R$1 trillion by 2030, net zero by 2050, a CDP 'A' and a lead role in the government's Eco Invest programme.",
              s=["corp", "inv"], neo=[0, ""], src=[["2Q26 results presentation", DECK2Q]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Five ways money moves: Brazil's largest credit-card book on Mastercard and Visa, Pix (now by tap, automatic and on WhatsApp), Rede, the largest acquirer by volume, cash management across Latin America, and dollar accounts for Brazilians abroad.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Cards & networks", "blurb": "Mastercard and Visa; Hipercard to Mastercard.", "div": "cards", "rev": "retail", "products": [
            P("mcdeal", "Itaú–Mastercard network agreement", "In March 2015 Itaú and Mastercard signed a 20-year agreement to build a new Brazilian payments network on which Itaú would issue; CADE approved it in 2016 only for seven years and barred the new brand from using either name. The brand never visibly launched.", short="2015 network agreement",
              s=["con", "aff"], lc="move", o="P", at="Mastercard", ay="Mar 2015", st="unconf", neo=[3, "Mastercard's own agreement."],
              mc="The deepest formal tie on record: whatever became of the joint network, it set up the Hipercard migration a decade later.",
              src=[["Mastercard: Itaú and Mastercard expand relationship, Mar 2015", MC2015], ["CADE: joint venture approved with restrictions, May 2016", CADE]]),
            P("hipercard", "Hipercard to Mastercard", "Itaú closed its own Hipercard network in 2025: the bank was merged into Itaú in January 2025 and about 15 million Hipercard cards moved to Hipercard Mastercard Platinum by 30 June 2025.", short="Hipercard → Mastercard",
              s=["con"], lc="move", st="new", ay="Jun 2025", o="P", at="Mastercard", neo=[2, "Now Mastercard."],
              src=[["CERC: Hipercard arrangement closes and migrates to Mastercard, Jul 2025", HIPER], ["Seu Crédito Digital: Hipercard ends after 57 years, Jul 2025", "https://seucreditodigital.com.br/hipercard-deixa-de-existir-apos-57-anos/"]]),
            P("wallets", "Wallets & tokens", "Cards in Apple Pay, Google Wallet and Samsung Pay; Itaú was not in the first wave of Brazil's standardised Click to Pay in 2024.",
              s=["con", "aff"], lc="move", o="P", at="Apple, Google, Samsung", neo=[1, "Mastercard and Visa tokens."],
              mc="Click to Pay and payment passkeys at Brazil's largest card issuer, where Mastercard aims to end passwords and manual card entry by 2030.",
              src=[["Central do Varejo: Click to Pay in Brazil, Feb 2024", "https://centraldovarejo.com.br/?p=11349"]]),
        ]},
        {"id": "2.2", "ic": "zap", "name": "Pix", "blurb": "By tap, automatic, on WhatsApp.", "div": "retail", "rev": "retail", "products": [
            P("pixnfc", "Pix by tap", "Contactless Pix through Google Wallet from November 2024, accepted on every Rede terminal, and straight from the Itaú app on Android from January 2026; iPhones are still excluded by Apple's NFC rules.",
              s=["con", "merch"], lc="move", st="new", neo=[0, "Pix, not cards."],
              mc="Pix by tap competes with contactless cards at the counter; debit card volume at Itaú was flat in 2025.",
              src=[["Itaú: Pix by tap in the app, Jan 2026", IR + "noticias/itau-unibanco-lanca-pix-por-aproximacao-direto-no-aplicativo/"]]),
            P("pixmore", "Pix Automático & Pix on WhatsApp", "Recurring Pix for business clients from January 2025, ahead of the national launch; balance and Pix through WhatsApp; voice Pix inside the ia.i assistant.",
              s=["con", "sme"], lc="move", st="new", neo=[0, ""],
              src=[["Let's Money: ia.i and Pix on WhatsApp, Jun 2026", LETS + "itau-ia-i-saldo-pix-whatsapp/"]]),
        ]},
        {"id": "2.3", "ic": "store", "name": "Acquiring", "blurb": "Rede, number one by volume.", "div": "rede", "rev": "retail", "products": [
            P("rede", "Rede", "Itaú's acquirer: R$1.03 trillion of volume in 2025 and R$298.7 billion in 2Q26 (up 23.5%), the largest by volume (22.7% share); more than 50 card brands accepted and receivables paid out the next day, bundled with Itaú business accounts and credit.",
              s=["merch", "sme"], lc="move", neo=[1, "Accepts Mastercard among 50-plus brands."],
              mc="The largest Brazilian acquirer by volume sees Mastercard transactions from both sides: merchant data, acceptance and agentic tokens fit.",
              src=[["2Q26 MD&A", MDA], ["Let's Money: Rede leads acquirers by volume, Mar 2026", LETS + "rede-itau-lidera-volume-adquirentes/"]]),
            P("laranjinha", "Laranjinha+", "Rede's card terminal with generative AI and voice-command sales (May 2026), extended to all clients by software update in June.",
              s=["merch"], lc="move", st="new", ay="May 2026", neo=[1, "Accepts Mastercard."],
              src=[["2Q26 MD&A", MDA]]),
        ]},
        {"id": "2.4", "ic": "arrow-left-right", "name": "Cash management", "blurb": "Multi-bank, multi-country.", "div": "bba", "rev": "wholesale", "products": [
            P("cashmgmt", "Connect Cash, Scope & collections", "Connect Cash, a multi-bank, multi-country cash-management platform for Latin America through Itaú BBA, and Scope, connecting retailers' tills to every bank and acquirer (1Q26); payments and collections earned R$2.0 billion in 2Q26.", short="Connect Cash & collections",
              s=["corp", "sme"], lc="everyday", st="new", neo=[0, ""],
              src=[["1Q26 MD&A", MDA1Q], ["2Q26 MD&A", MDA]]),
        ]},
        {"id": "2.5", "ic": "globe", "name": "Global accounts", "blurb": "Dollars for Brazilians.", "div": "retail", "rev": "retail", "products": [
            P("contaglobal", "Conta Global Personnalité", "A dollar and euro account inside the app with an international debit card usable in 180 countries (4Q25).",
              s=["aff", "pvt"], lc="move", st="new", neo=[None, "Card network not stated."],
              mc="Brazilian travellers abroad are a cross-border card story: FX, benefits and Move for transfers.",
              src=[["4Q25 MD&A", "https://filemanager-cdn.mziq.com/published/42787847-4cf6-4461-94a5-40ed237dca33/a03fd48e-6ec1-4b6f-b198-cdfb0409b7d3_itau_unibanco_holding_s.a..pdf"]]),
            P("avenue", "Avenue", "US brokerage and dollar accounts for Brazilians: Itaú bought 35% in 2023 and control (50.1%) on 30 January 2026 for about R$735 million.",
              s=["aff", "inv"], lc="grow", o="A", ay="Jan 2026", neo=[0, ""], src=[["FY2025 20-F", F20]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account and payment: an AI assistant that can move money by voice, fraud defences against Brazil's Pix scams, open finance, the loyalty programmes behind the cards, and AI agents that shop with Itaú cards.",
    "tiles": [
        {"id": "3.1", "ic": "brain", "name": "AI assistants", "blurb": "ia.i, by voice.", "div": "retail", "rev": "retail", "products": [
            P("iai", "ia.i", "A generative-AI assistant in the app that understands voice, text and images and can carry out transactions, including Pix by voice with confirmation; launched to 300,000 clients on 27 July 2026, with all clients by the end of 2026.",
              s=["con", "aff"], lc="everyday", st="new", ay="Jul 2026", neo=[0, ""],
              src=[["Let's Money: ia.i assistant, Jul 2026", LETS + "itau-ia-i-assistente-app/"]]),
            P("inteligencia", "Inteligência Itaú on WhatsApp", "The conversational platform behind WhatsApp banking, now opening SME accounts with generative AI (2Q26).",
              s=["sme", "con"], lc="open", st="new", neo=[0, ""], src=[["2Q26 MD&A", MDA]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud & identity", "blurb": "Against the Pix scams.", "div": "retail", "rev": "retail", "products": [
            P("fraud", "Fraud prevention", "New fraud engines (2025), facial biometrics and e-signature in vehicle finance, Itaú's own 'Alerta Pix' (April 2026), and the central bank's new rules: suspicious accounts rejected, mule accounts closed, and from September 2026 an 80-day window and layered tracing for Pix refunds.",
              s=["con", "sme"], lc="everyday", neo=[0, "No Mastercard fraud product public."],
              mc="About 28 million Brazilians fell for Pix scams in 2025: scam and mule-account intelligence on instant payments is the opening, with nothing Mastercard-branded at Itaú yet.",
              src=[["FY2025 20-F", F20], ["Tribuna PR: central bank changes Pix rules, Aug 2026", "https://www.tribunapr.com.br/noticias/economia/banco-central-muda-regras-do-pix-para-combater-fraudes-em-agosto/"]]),
        ]},
        {"id": "3.3", "ic": "webhook", "name": "Open finance", "blurb": "Brazil's open-finance rails.", "div": "retail", "rev": "retail", "products": [
            P("openfinance", "Open finance", "Consents of up to 12 months through the app and internet banking; in 2023 Itaú received about a quarter of shared data, second to Nubank. Payroll-loan portability now runs over open-finance rails.",
              s=["con", "sme"], lc="beyond", neo=[0, ""],
              src=[["Itaú: open finance", "https://www.itau.com.br/open-finance"], ["FY2025 20-F", F20]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Loyalty", "blurb": "Points that never expire.", "div": "cards", "rev": "retail", "products": [
            P("loyalty", "Minhas Vantagens, Mais Vantagens & card points", "Tiered fee waivers for individuals (Minhas Vantagens) and SMEs (Mais Vantagens, 4Q25), non-expiring points on Personnalité and Private cards, LATAM Pass and Azul points on co-brands, Itaú Shop and Itaú Live presales; rising rewards costs are squeezing card fees.",
              s=["con", "aff", "sme"], lc="grow", neo=[1, "Mastercard and Visa benefits on the premium cards."],
              mc="Merchant-funded offers and Priceless experiences would ease rewards costs that Itaú says are compressing card fees.",
              src=[["FY2025 20-F", F20], ["2Q26 MD&A", MDA]]),
        ]},
        {"id": "3.5", "ic": "bot", "name": "Agentic commerce", "blurb": "AI agents paying with Itaú cards.", "div": "cards", "rev": "retail", "products": [
            P("agentpay", "Mastercard Agent Pay", "Itaú was among 17 issuers and processors running live, controlled agentic transactions with Mastercard across Latin America (March 2026), about ten days after Visa's first in Brazil with BB and Santander; Itaú said it moved 'from discussion to execution'.",
              s=["con", "aff"], lc="move", st="new", ay="Mar 2026", o="P", at="Mastercard", neo=[3, "Mastercard's own."],
              src=[["Mobile Time: Mastercard AI agents, Mar 2026", AGENTPAY], ["IstoÉ Dinheiro: AI agents shop in Brazil, Apr 2026", "https://istoedinheiro.com.br/agentes-de-ia-ja-fazem-compras-no-brasil-e-aceleram-corrida-tecnologica-das-bandeiras"]]),
            P("redeagent", "Rede agentic gateway", "Rede's own multiprotocol gateway (30 September 2026) that translates AI agents' protocols into Rede's APIs, credit cards only at launch, with unnamed tokenisation partners.",
              s=["merch"], lc="move", st="new", ay="Sep 2026", neo=[None, "Protocols and token partners not named."],
              mc="Agent Pay acceptance inside Rede's gateway would close the loop: Itaú issuing, Rede acquiring, Mastercard's agentic tokens in between.",
              src=[["Let's Money: Rede's agentic commerce, Sep 2026", LETS + "itau-rede-comercio-agentico-agentes-ia/"]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Retail and Wholesale, opened out into what clients buy: Brazil's largest card book, co-brands from LATAM to Pão de Açúcar, payroll, car and personal credit, mortgages, SME lending, Itaú BBA, and the largest private-bank wealth franchise.",
    "tiles": [
        {"id": "4.1", "ic": "credit-card", "name": "Credit cards", "blurb": "Number one, 24% of volume.", "div": "cards", "rev": "retail", "products": [
            P("cards", "Itaú credit cards", "Brazil's largest credit-card issuer: 24% of purchase volume (R$206 billion in 2Q26, ahead of Nubank's R$128.5 billion), R$150.4 billion of balances and R$3.3 billion of card fees a quarter. Itaú, Uniclass, Personnalité and Private cards on Mastercard and Visa (Mastercard Black and Visa Infinite at the top), plus cards backed by investments.",
              s=["con", "aff"], lc="borrow", neo=[1, "Mastercard and Visa; no public split."],
              mc="At the largest issuer in Latin America's largest card market, the share of new cards each network wins is the whole game; Nubank, growing twice as fast, issues Mastercard.",
              src=[["2Q26 MD&A", MDA], ["Finsiders: Nubank grows twice the card market, Oct 2026", FINSIDERS_CARDS]]),
            P("legend", "World Legend & The One", "Mastercard World Legend by invitation for Private and then Personnalité clients from 2026 (Itaú a launch issuer), The One Mastercard Black, and Visa Infinite Privilege at R$15,000 a year.", short="World Legend",
              s=["pvt", "aff"], lc="borrow", st="new", ay="2026", o="P", at="Mastercard, Visa", neo=[1, "World Legend is Mastercard; Infinite Privilege is Visa."],
              src=[["Bloomberg Línea: Itaú and C6 bet on World Legend, Oct 2025", LEGEND]]),
        ]},
        {"id": "4.2", "ic": "plane", "name": "Co-brands", "blurb": "LATAM, Azul, Pão de Açúcar, Magalu.", "div": "cards", "rev": "retail", "products": [
            P("airline", "LATAM Pass & Azul Itaú", "Airline co-brands on both networks, from Gold to Black and Infinite (Azul's top card is Mastercard); purchase volume up 25% in 2025.",
              s=["con", "aff"], lc="borrow", o="P", at="LATAM, Azul", neo=[1, "Both networks."],
              src=[["FY2025 20-F", F20]]),
            P("retailcob", "Retail co-brands & Luizacred", "Pão de Açúcar (Mastercard Black and Platinum), Passaí (Visa), Instituto Ayrton Senna (Mastercard), and Luizacred, the 50% venture with Magazine Luiza (R$20.2 billion of card balances, 5.7 million cards). Itaú agreed to buy out GPA's and Assaí's stakes in Financeira Itaú CBD (December 2025).",
              s=["con"], lc="borrow", o="P", at="GPA, Assaí, Magazine Luiza", neo=[1, "Both networks."],
              src=[["FY2025 20-F", F20], ["Magalu: 2Q26 results", "https://static.poder360.com.br/uploads/2026/08/Magalu-balanco-2T2026.pdf"]]),
        ]},
        {"id": "4.3", "ic": "hand-coins", "name": "Consumer credit", "blurb": "Payroll, cars, personal.", "div": "retail", "rev": "retail", "products": [
            P("consignado", "Payroll loans", "R$81.3 billion of payroll-deducted loans (up 11.7%): pensioners, public servants and, since March 2025, private-sector workers through the government's Crédito do Trabalhador, up 90% in a year; the Minas Gerais state payroll won for five years from December 2026.",
              s=["con"], lc="borrow", neo=[0, ""],
              src=[["2Q26 MD&A", MDA], ["Itaú: Minas Gerais payroll, Jul 2026", SEC + "000113259726000189/comunicadoaomercado-reno.htm"]]),
            P("autos", "Vehicle finance", "R$35.1 billion of car loans to individuals (fourth, 9.1% share), decided digitally at dealers through Credline in under a minute three times in four.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["FY2025 20-F", F20]]),
            P("personal", "Personal credit & microcredit", "R$68.1 billion of personal loans and overdrafts (10.4% share), R$1.5 billion of microcredit to 324,000 clients (64% women), and debt renegotiation under Desenrola.",
              s=["con", "sme"], lc="borrow", neo=[0, ""], src=[["FY2025 20-F", F20], ["2Q26 results presentation", DECK2Q]]),
        ]},
        {"id": "4.4", "ic": "house", "name": "Mortgages", "blurb": "Second only to Caixa.", "div": "retail", "rev": "retail", "products": [
            P("mortgage", "Crédito imobiliário", "R$152.2 billion of mortgages (up 13%), origination up 64% in 2Q26, 26% of new loans in 2025, second only to Caixa, with Loft and QuintoAndar as partners.",
              s=["con", "aff"], lc="borrow", neo=[0, ""], src=[["2Q26 MD&A", MDA], ["FY2025 20-F", F20]]),
        ]},
        {"id": "4.5", "ic": "briefcase-business", "name": "SMEs", "blurb": "1.6 million businesses.", "div": "sme", "rev": "retail", "products": [
            P("sme", "Itaú Empresas & Itaú Emps", "More than 1.6 million small and medium businesses, R$307.4 billion of SME credit (up 11.6%) with government-backed lines up sharply, and Itaú Emps, the fully digital offer.",
              s=["sme"], lc="borrow", neo=[0, "SME card networks not stated."],
              mc="Commercial and business cards for 1.6 million SMEs, many already on Rede, is the B2B opening; Mastercard sees boleto spend moving to cards.",
              src=[["2Q26 MD&A", MDA], ["FY2025 20-F", F20]]),
        ]},
        {"id": "4.6", "ic": "building-2", "name": "Itaú BBA", "blurb": "Number one in DCM and M&A.", "div": "bba", "rev": "wholesale", "products": [
            P("bba", "Corporate & investment banking", "R$474.9 billion of corporate credit (up 10%), first in debt capital markets (26% share) and in M&A by number of deals, a leader in BNDES on-lending, FX and supply-chain finance, with a new infrastructure and energy segment.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["2Q26 MD&A", MDA], ["FY2025 20-F", F20]]),
        ]},
        {"id": "4.7", "ic": "gem", "name": "Wealth & insurance", "blurb": "R$3.8 trillion managed.", "div": "wms", "rev": "wholesale", "products": [
            P("private", "Itaú Private & Personnalité", "31.1% of Brazilian private banking, offices in Miami, Zurich, Portugal and the Bahamas, and a planned US national bank (OCC preliminary approval August 2026); Personnalité for clients earning more than R$15,000 a month.",
              s=["pvt", "aff"], lc="grow", neo=[0, ""],
              src=[["FY2025 20-F", F20], ["Itaú: Itaú Bank, N.A., Aug 2026", SEC + "000113259726000226/announcementtothemarket-.htm"]]),
            P("asset", "Asset management & brokerage", "R$3.82 trillion under management across the group; Itaú Asset (R$1.24 trillion, the largest private-bank manager) and Kinea; Íon and Itaú Corretora for investors; Solana Capital bought in 2Q26.",
              s=["inv", "aff"], lc="grow", neo=[0, ""], src=[["2Q26 MD&A", MDA], ["FY2025 20-F", F20]]),
            P("insurance", "Insurance, pensions & consórcio", "Itaú Seguros with a 30.7% stake in Porto Seguro (fourth in insurance), third in private pensions (19.9%), and consórcio sales of R$37 billion in 2025.",
              s=["con", "inv"], lc="grow", neo=[0, ""], src=[["FY2025 20-F", F20]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How clients reach Itaú: one SuperApp in place of six, 2,210 branches and falling, 12,000 ATMs plus Banco24Horas, WhatsApp and digital managers, and Bankline and the Itaú Empresas app for business.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "SuperApp", "blurb": "Six apps into one.", "div": "retail", "rev": "retail", "products": [
            P("superapp", "One Itaú SuperApp", "About 15 million clients moved from six apps (Itaú Cartões, iti, Credicard, Credicard On, Hipercard and the old Personnalité app) into one, finished around January 2026; 4.6 million accounts were opened digitally in 2025, 68% of new accounts. iti, the digital bank, is gone as a separate app.",
              s=["con", "aff"], lc="everyday", st="new", neo=[0, ""],
              src=[["Let's Money: migration to the SuperApp complete, Jan 2026", LETS + "itau-conclui-migracao-clientes-superapp/"], ["FY2025 20-F", F20]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "2,210 and closing.", "div": "retail", "rev": "retail", "products": [
            P("branches", "Branches & ATMs", "2,210 branches and service branches at June 2026, down from 2,738 a year earlier (162 closed in 1Q26 alone); 11,822 own ATMs plus 14,196 Banco24Horas machines through TecBan.",
              s=["con", "aff", "sme"], lc="everyday", neo=[0, ""], src=[["2Q26 MD&A", MDA], ["FY2025 20-F", F20]]),
        ]},
        {"id": "5.3", "ic": "headset", "name": "WhatsApp & remote", "blurb": "Click to human.", "div": "retail", "rev": "retail", "products": [
            P("remote", "WhatsApp & digital managers", "Pix and balances on WhatsApp, Uniclass and Personnalité managers by phone, chat and WhatsApp, and 'click to human' when the AI is not enough.",
              s=["con", "aff"], lc="everyday", neo=[0, ""], src=[["2Q26 MD&A", MDA]]),
        ]},
        {"id": "5.4", "ic": "monitor", "name": "Business channels", "blurb": "All digital.", "div": "sme", "rev": "retail", "products": [
            P("bizchannels", "Itaú Empresas app & Bankline", "Every corporate transaction is digital: the Itaú Empresas and Itaú Emps apps for SMEs, Bankline internet banking, and Itaú BBA platforms for corporates.",
              s=["sme", "corp"], lc="everyday", neo=[0, ""], src=[["2Q26 results presentation", DECK2Q]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-latam", "name": "Latin America", "blurb": "Chile, Paraguay, Uruguay, Colombia.", "products": [
        P("latam", "Itaú in Latin America", "A R$253 billion loan book outside Brazil: Banco Itaú Chile (67.4%; 11.5% loan share), Paraguay (largest private bank, ROE 21.5%), Uruguay (largest private bank, ROE 34.1%, with OCA, the largest card issuer), and Colombia, corporate-only since retail moved to Banco de Bogotá in July 2026. About 5% of the result.",
          s=["latam"], div="latam", rev="wholesale", neo=[None, "Not researched by country."],
          src=[["2Q26 MD&A", MDA], ["Itaú: Colombia retail transfer, Jul 2026", SEC + "000113259726000203/announcementtothemarket_.htm"]]),
    ]},
    {"id": "pillar-mastercard", "name": "Mastercard at Itaú", "blurb": "A 2015 deal, a 2025 migration.", "products": [
        P("mcatitau", "Mastercard at Itaú", "A 2015 network agreement, about 15 million Hipercard cards moved to Mastercard (2025), World Legend at the top (2026), Agent Pay (2026), and Rede accepting Mastercard; Visa keeps Uniclass Signature, Visa Infinite, airline and retail co-brands. Mastercard Brasil is led by Marcelo Tangioni; Itaú's cards director is Rodrigo Carneiro. A former Itaú CEO, Candido Bracher, joined Mastercard's board in 2021.",
          s=["inv"], div="iuh", rev="corp", mc="The relationship this map is drawn for.",
          src=[["Mastercard: Itaú agreement, Mar 2015", MC2015], ["CERC: Hipercard migrates to Mastercard, Jul 2025", HIPER], ["Mobile Time: Mastercard AI agents, Mar 2026", AGENTPAY]]),
    ]},
    {"id": "pillar-market", "name": "Brazilian payments", "blurb": "Cards, Pix and the regulator.", "products": [
        P("brmarket", "Cards and Pix in Brazil", "R$4.5 trillion of card spending in 2025 (credit R$3.1 trillion, up 14.5%; debit flat) against R$35.4 trillion through Pix (up 34%); Nubank growing twice as fast as the card market; debit interchange capped and a consultation on capping credit interchange announced in May 2025; Elo pushing into premium cards.",
          s=["con", "merch"], div="iuh", rev="corp",
          src=[["Mercado & Consumo: card sector R$4.5 trillion in 2025, Feb 2026", "https://mercadoeconsumo.com.br/11/02/2026/meios-de-pagamento/setor-de-cartoes-movimenta-r-45-trilhoes-em-2025-alta-de-101-ante-2024/"], ["Metrópoles: Pix record in 2025, Feb 2026", "https://metropoles.com/brasil/pix-bate-recorde-em-2025-e-movimenta-r-354-trilhoes"], ["Finsiders: central bank to consult on interchange, May 2025", "https://finsidersbrasil.com.br/congresso-abipag-2025/bc-vai-lancar-consulta-publica-para-limitar-tarifas-de-intercambio-de-cartoes/"]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
