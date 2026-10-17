"""Banco Angolano de Investimentos (BAI): layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are BAI's own unless a source says otherwise: the Q2 2026 results release (23 July 2026), the H1 2026
report and the 2025 annual report, all in Portuguese. Kz = kwanza; USD 1 was about Kz 980 in October 2026.
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

AR25 = "https://www.bancobai.ao/media/2bsbbx4o/relatorio-e-contas-individual-e-consolidado-2025.pdf"
H126 = "https://www.bancobai.ao/media/smzbakdz/relatorio-e-contas-individual-e-consolidado-do-i-semestre-2026.pdf"
Q226 = "https://www.bancobai.ao/media/wirkfdjj/comunicado-resultados-do-ii-trimestre-2026.pdf"
IR = "https://www.bancobai.ao/pt/relacoes-com-investidores"
ABOUT = "https://www.bancobai.ao/pt/institucional/quem-somos/sobre-o-bai"
GROUP = "https://www.bancobai.ao/pt/institucional/quem-somos/grupo-bai"
BOARD = "https://www.bancobai.ao/pt/institucional/mandato-2026-2029/orgaos-sociais-2026-2029"
IPO = "https://www.bancobai.ao/media/3804/nota-de-imprensa-bai-informa-a-publicac-a-o-do-prospecto-da-oferta-pu-blica-de-venda-opv-aprovado-pela-comissa-o-de-mercado-de-capitais-cmc-_final.pdf"
FITCH22 = "https://www.bancobai.ao/media/4150/nota-de-imprensa_fitch-melhora-rating-do-bai-para-positivo_17-08-2022.pdf"
CORE = "https://www.bancobai.ao/media/cq1jinmq/nota-de-imprensa-bai-inicia-programa-de-transformacao-do-core-bancario.pdf"
BOND = "https://www.bancobai.ao/media/tfepbvwg/o-bai-banco-angolano-de-investimentos-sa-sociedade-aberta-informa-sobre-a-admissa-o-a-negociac-a-o-das-obrigac-o-es-sustenta-veis-bai-na-bodiva.pdf"
EUROPA = "https://www.bancobai.ao/media/1lxhw0zu/bai-europa-comunicado-de-imprensa.pdf"
EUROPA2 = "https://www.bancobaieuropa.pt/pt/institucional/noticias/todas/comunicado/"
EM26 = "https://www.bancobai.ao/media/oq1npsao/nota-de-imprensa-bai-distinguido-como-melhor-banco-para-pequenas-e-m%C3%A9dias-empresas-em-angola-e-melhor-banco-de-angola-pela-euromoney.pdf"
DEBIT = "https://www.bancobai.ao/pt/particulares/produtos/cartoes/cartao-debito-multicaixa"
CONTACTLESS = "https://www.bancobai.ao/pt/institucional/imprensa/noticias/pagamentos-via-contactless-com-o-cartao-de-debito-multicaixa"
CHIP = "https://www.bancobai.ao/media/4738/nota-de-imprensa-bai-conclui-mudanc-a-de-carto-es-de-banda-magne-tica-para-carto-es-com-chip.pdf"
MULTI = "https://www.bancobai.ao/media/sd2cgmug/bai-reforc-a-financiamento-ao-agronego-cio-e-apresenta-carta-o-de-de-bito-multimarca-na-expo-hui-la-2026.pdf"
FORBESMM = "https://forbesafricalusofona.com/bai-lanca-cartao-multimarca-que-une-rede-multicaixa-e-mastercard/"
EMISMC = "https://www.verangola.net/va/en/082023/BankingInsurance/36636/Partnership-between-EMIS-and-Mastercard-allows-issuing-of-cards-that-can-be-used-abroad.htm"
KAMBA = "https://www.bancobai.ao/pt/particulares/produtos/cartoes/cartao-kamba"
LIMITS = "https://expansao.co.ao/empresas/interior/bai-reduz-limites-de-carregamento-mensal-de-cartoes-de-pagamento-internacionais-117806.html"
RENTAL = "https://www.bancobai.ao/media/vu0fax5l/nota-de-impresa_bai-investiga-aluguer-de-cartoes-e-anuncia-medidas-restritivas_51.pdf"
CLASSIC = "https://www.bancobai.ao/pt/particulares/produtos/cartoes/cartao-credito-bai-classic"
BUSINESS = "https://www.bancobai.ao/pt/empresas/produtos/cartoes/cartao-credito-bai-business"
VISA26 = "https://www.bancobai.ao/media/cw4bsbir/nota-de-imprensa-bai-e-visa-assinam-acordo-estrate-gico-para-reforc-ar-a-inovac-a-o-nos-pagamentos.pdf"
MCXCREDIT = "https://www.bancobai.ao/pt/particulares/produtos/cartoes/cartao-credito-multicaixa"
TAAG = "https://www.bancobai.ao/pt/particulares/produtos/cartoes/cartao-de-credito-multicaixa-taag"
MCCORP = "https://www.bancobai.ao/pt/empresas/produtos/cartoes/cartao-mastercard-corporativo"
FLEX = "https://www.bancobai.ao/pt/particulares/produtos/cartoes/cartao-flex"
TPA = "https://www.bancobai.ao/pt/empresas/servicos/tpa-terminal-de-pagamento-automatico"
TPAPLUS = "https://www.bancobai.ao/pt/empresas/produtos/contas/conta-tpaplus"
EBAI = "https://www.bancobai.ao/pt/empresas/servicos/e-bai"
KWIK = "https://www.bancobai.ao/pt/particulares/servicos/servico-kwik"
KWIK23 = "https://www.bancobai.ao/media/fq0khqnh/bai-apresenta-na-filda-modelo-de-atendimento-bai-plus-perto-e-lanc-a-transfere-ncias-instanta-neas-kwik.pdf"
BAIPAGA = "https://www.bancobai.ao/pt/particulares/servicos/bai-paga"
BOC = "https://www.bancobai.ao/media/efph0xbg/o-bai-e-bank-of-china-assinam-memorando-de-entendimento-para-cooperac-a-o-no-a-mbito-do-cips-e-dos-servic-os-de-compensac-a-o-em-renminbi.pdf"
SIBOS = "https://www.bancobai.ao/media/rmun3ocf/bai-conclui-participac-a-o-na-sibos-2026-com-mais-de-50-reunio-es-estrate-gicas-e-reforc-a-presenc-a-internacional.pdf"
SECURITY = "https://www.bancobai.ao/pt/particulares/seguranca-e-fraude"
INFOTUR = "https://forbesafricalusofona.com/turismo-em-angola-ganha-novas-solucoes-de-financiamento-com-acordo-entre-infotur-e-bai"
PREMIUM = "https://www.bancobai.ao/pt/premium"
AGENT = "https://www.bancobai.ao/pt/agente-bancario"
MCX25 = "https://www.verangola.net/va/en/012026/BankingInsurance/47451/More-than-40-billion-kwanzas-were-transacted-on-the-Multicaixa-network-in-2025.htm"
ATLVISA = "https://www.verangola.net/va/en/072026/BankingInsurance/49602/The-first-debit-card-in-kwanzas-that-allows-international-payments-has-been-launched.htm"
DELOITTE = "https://www.verangola.net/va/en/062026/BankingInsurance/49166/Angolan-banking-sector's-net-profits-grow-23-percent-with-a-record-milestone-of-one-billion-kwanzas-in-2025.htm"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · listing · core", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Angola's largest bank by assets and its most profitable in 2025, listed on BODIVA since 2022 with no controlling shareholder, a new Finastra core being built, and banks in Portugal and Cabo Verde.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Kz 5.3trn assets, record 2025.", "div": "bai", "rev": "commercial", "products": [
            P("balance", "Balance sheet & earnings", "Assets of Kz 5,334 billion (about USD 5.4 billion), loans of Kz 1,366 billion and customer funds of Kz 4,105 billion at 30 June 2026; H1 profit Kz 117 billion (down 34% as trading gains fell), ROAE 25.2%, capital ratio 25.7%. 2025 profit was a record Kz 296 billion, the sector's largest.",
              s=["corp"], neo=[0, ""], src=[["BAI: Q2 2026 results, Jul 2026", Q226], ["BAI: 2025 annual report", AR25], ["Ver Angola: Deloitte banking study, Jun 2026", DELOITTE]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "Listed, dispersed, Lélis.", "div": "group", "rev": "commercial", "products": [
            P("listing", "Listing, owners & ratings", "First company on BODIVA (10% sold in June 2022); 2,329 shareholders, six with 5% or more (32.5% together), none qualifying under banking law; market value about Kz 1.9 trillion; rated B- by Fitch and B3 by Moody's, both stable.",
              s=["corp"], neo=[0, ""], src=[["BAI: IPO prospectus note, Apr 2022", IPO], ["BAI: 2025 annual report", AR25], ["BAI: investor relations", IR], ["BAI: Fitch outlook note, Aug 2022", FITCH22]]),
            P("leadership", "Board & executive committee", "Chair Mário Alberto Barber; CEO Luís Filipe Rodrigues Lélis, also the largest shareholder (6.33%); nine executive directors for 2026–29, including Irisolange Verdades (international); auditor Deloitte. Portfolios for cards and digital are not published ⚠.",
              s=["corp"], neo=[0, ""], src=[["BAI: governing bodies 2026–2029", BOARD], ["BAI: SIBOS note, Oct 2026", SIBOS]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Core & technology", "blurb": "Finastra Essence.", "div": "bai", "rev": "commercial", "products": [
            P("core", "Core banking renewal", "Execution of a new information-systems programme began on 1 August 2025: Finastra Essence core banking (first in Angola and southern Africa), OPICS treasury, trade finance and corporate channels, integrated by local partner Innovation Makers.",
              s=["corp"], st="new", ay="Aug 2025", o="P", at="Finastra, Innovation Makers", neo=[0, ""],
              mc="A core migration is the moment card processing and tokenisation get re-plumbed.",
              src=[["BAI: core transformation note, Aug 2025", CORE]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Geração BAI", "blurb": "Plan 2022–27, 58% done.", "div": "group", "rev": "commercial", "products": [
            P("strategy", "Geração BAI 2022–2027", "Five axes, 21 initiatives and 71 action plans: customer experience, profitability, a high-performance culture, digital transformation including payment methods and a 'bank in your pocket', and group risk and sustainability; 58% executed at end-2025. No acquisitions planned.",
              s=["corp"], neo=[0, ""], src=[["BAI: 2025 annual report", AR25], ["BAI: Euromoney note, Jul 2026", EM26]]),
            P("funding", "Bonds & sustainability", "BAI 2026–2031 bonds listed in January 2026 and a Kz 57.5 billion sustainability bond at 17% (2026–29) listed on 22 September 2026, 130% subscribed; first sustainability report in 2025.",
              s=["corp", "prem"], st="new", ay="Sep 2026", neo=[0, ""], src=[["BAI: sustainability bond listing, Sep 2026", BOND]]),
        ]},
        {"id": "1.5", "ic": "earth", "name": "Group abroad", "blurb": "Portugal, Cabo Verde, São Tomé.", "div": "europa", "rev": "markets", "products": [
            P("europa", "BAI Europa", "Lisbon-based subsidiary (99.99%) with an office in Porto, focused on trade finance for Angola; searched by Portugal's Polícia Judiciária on 14 October 2026 in an investigation it has not described ⚠.",
              s=["corp"], o="B", st="flux", neo=[0, ""], src=[["BAI: BAI Europa statement, Oct 2026", EUROPA], ["BAI Europa: communiqué, Oct 2026", EUROPA2]]),
            P("capeverde", "BAI Cabo Verde & BISTP", "BAI Cabo Verde (81.63%): 71,671 customers, 36 ATMs, 2,561 POS terminals and 7,950 active cards, including the country's first platinum business card; a 25% stake in Banco Internacional de São Tomé e Príncipe.",
              s=["con", "corp"], o="B", neo=[None, "Card networks not published."], div="cv", src=[["BAI: H1 2026 report", H126], ["BAI: 2025 annual report", AR25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: 2.1 million Multicaixa debit cards, a new debit card that is Multicaixa at home and Mastercard abroad, Visa for prepaid travel cards and credit, domestic credit cards, a small Mastercard corporate card, 34,000 POS terminals, KWiK and the é-Kwanza wallet, and correspondent banking now adding China's CIPS.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Multicaixa debit", "blurb": "2.08 million cards.", "div": "bai", "rev": "retail", "products": [
            P("mcxdebit", "Cartão de Débito Multicaixa", "The everyday card on EMIS's domestic Multicaixa network: 2,084,773 active at June 2026, the largest base in Angola; all on EMV chip since February 2023; contactless up to Kz 20,000 without a PIN.",
              s=["con", "unb"], lc="everyday", o="P", at="EMIS", neo=[0, "Multicaixa (EMIS)."],
              src=[["BAI: Multicaixa debit card", DEBIT], ["BAI: H1 2026 report", H126], ["BAI: chip migration, Feb 2023", CHIP], ["BAI: contactless", CONTACTLESS]]),
            P("mcxprepaid", "Multicaixa prepaid", "109,019 active prepaid Multicaixa cards at June 2026, many issued in 2025 for the Ministry of Education's MED programme.",
              s=["unb"], lc="everyday", o="P", at="EMIS", neo=[0, "Multicaixa."], src=[["BAI: H1 2026 report", H126], ["BAI: 2025 annual report", AR25]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Multi-brand debit", "blurb": "Multicaixa + Mastercard.", "div": "bai", "rev": "retail", "products": [
            P("multibrand", "Multi-brand debit card", "Launched on 20 August 2026 for individuals: one card on the kwanza current account that works on Multicaixa in Angola and on Mastercard abroad, so customers no longer need a credit card to spend overseas. Built on the EMIS–Mastercard framework of August 2023. Cards issued and fees not disclosed ⚠.", short="Multi-brand debit (Mastercard abroad)",
              s=["con", "trav", "prem"], lc="move", st="new", ay="Aug 2026", o="P", at="EMIS, Mastercard", neo=[1, "Multicaixa at home, Mastercard abroad."],
              mc="Mastercard's first route into BAI's mass market; Visa launched a rival co-badge with another bank a month earlier.",
              src=[["BAI: multi-brand card note, Aug 2026", MULTI], ["Forbes África Lusófona, Aug 2026", FORBESMM], ["Ver Angola: EMIS and Mastercard, Aug 2023", EMISMC]]),
        ]},
        {"id": "2.3", "ic": "plane", "name": "Visa cards", "blurb": "Kamba and credit on Visa.", "div": "bai", "rev": "retail", "products": [
            P("kamba", "Cartão Kamba (Visa prepaid)", "A personalised Visa prepaid card for travel and for family abroad, loaded in BAI Directo: 169,755 active at June 2026, down 15% in six months; monthly loading cut from USD 1,000 to USD 500 in April 2024 as dollars ran short; card-rental abuse investigated in 2024.", short="Kamba (Visa)",
              s=["trav", "con"], lc="move", o="P", at="Visa", neo=[0, "Visa."],
              src=[["BAI: Cartão Kamba", KAMBA], ["BAI: H1 2026 report", H126], ["Expansão: card limits cut, Apr 2024", LIMITS], ["BAI: card rental note, Feb 2024", RENTAL]]),
            P("visacredit", "Visa credit: BAI Classic & BAI Business", "Credit cards for spending online and abroad with OTP and Verified by Visa: 6,142 active at June 2026, down 6%; limits cut by 25% in April 2024. A BAI Platinum card has a contract online but is not on current product pages ⚠.", short="Visa credit",
              s=["prem", "sme"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              src=[["BAI: BAI Classic", CLASSIC], ["BAI: BAI Business", BUSINESS], ["BAI: H1 2026 report", H126], ["Expansão: card limits cut, Apr 2024", LIMITS]]),
            P("visadeal", "Visa partnership", "A strategic agreement signed on 23 September 2026 'reinforcing a long-standing partnership': e-payment adoption, digital transformation, payment security and cross-border payments; BAI also holds collateral from local banks under Visa representation protocols, suggesting it sponsors them into Visa ⚠.",
              s=["con", "corp"], lc="move", st="new", ay="Sep 2026", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa renewed its hold a month after the Mastercard card launched.",
              src=[["BAI: Visa agreement, Sep 2026", VISA26], ["BAI: 2025 annual report", AR25]]),
        ]},
        {"id": "2.4", "ic": "hand-coins", "name": "Multicaixa credit", "blurb": "Domestic credit, TAAG.", "div": "bai", "rev": "retail", "products": [
            P("mcxcredit", "Multicaixa credit cards", "Domestic credit cards for individuals and companies, with cash advance at any Angolan ATM: 5,207 active at June 2026, up 8%.",
              s=["con", "sme"], lc="borrow", o="P", at="EMIS", neo=[0, "Multicaixa."], src=[["BAI: Multicaixa credit card", MCXCREDIT], ["BAI: H1 2026 report", H126]]),
            P("taag", "Multicaixa TAAG credit card", "A co-branded card with the national airline TAAG (2025) for tickets and payments: up to 55 days interest-free, limits from Kz 100,000 to Kz 8 million, for Classic, Affluent and Premium customers.",
              s=["trav", "prem"], lc="borrow", st="new", ay="2025", o="P", at="TAAG, EMIS", neo=[0, "Multicaixa."],
              mc="A domestic co-brand with no international network on it.",
              src=[["BAI: TAAG card", TAAG], ["BAI: 2025 annual report", AR25]]),
        ]},
        {"id": "2.5", "ic": "briefcase-business", "name": "Corporate & fleet cards", "blurb": "796 Mastercard cards.", "div": "bai", "rev": "commercial", "products": [
            P("mccorp", "Cartão Mastercard Corporativo", "A personalised Mastercard prepaid card for resident companies, for payments and withdrawals in Angola and abroad without interest: only 796 active at June 2026 (127 in 2023); loading of up to USD 5,000 per company on the product page, USD 1,500 a month after the 2024 cuts ⚠.", short="Mastercard corporate prepaid",
              s=["corp", "sme"], lc="move", o="P", at="Mastercard", neo=[2, "Mastercard prepaid."],
              mc="BAI's only Mastercard programme before 2026, and a small one.",
              src=[["BAI: Mastercard corporate card", MCCORP], ["BAI: H1 2026 report", H126], ["Expansão: card limits cut, Apr 2024", LIMITS]]),
            P("flex", "Cartão FLEX", "An EMIS prepaid fuel card for Sonangol and TotalEnergies stations, loaded singly or in bulk through BAI Directo, for company fleets.",
              s=["corp", "sme"], lc="move", o="P", at="EMIS, Sonangol", neo=[0, "Multicaixa (EMIS)."], src=[["BAI: Cartão FLEX", FLEX]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acceptance", "blurb": "34,000 POS, e-BAI.", "div": "bai", "rev": "commercial", "products": [
            P("tpa", "TPA terminals & Conta TPA+", "39,152 POS terminals registered and 34,143 active at June 2026, about a fifth of Angola's active terminals ⚠; merchants earn 1% on cash withdrawals at the till; free terminals at fuel stations; Conta TPA+ pays interest to merchants with over Kz 750 million a month.", short="TPA acquiring",
              s=["sme", "corp"], lc="move", o="P", at="EMIS", neo=[None, "Multicaixa; international card acceptance not stated."],
              src=[["BAI: TPA", TPA], ["BAI: Conta TPA+", TPAPLUS], ["BAI: H1 2026 report", H126]]),
            P("ebai", "e-BAI", "An e-commerce gateway that lets merchants take payment from Visa cardholders in Angola and abroad.",
              s=["sme"], lc="move", o="P", at="Visa", neo=[0, "Visa."],
              mc="Online acceptance names Visa only.",
              src=[["BAI: e-BAI", EBAI]]),
        ]},
        {"id": "2.7", "ic": "zap", "name": "Instant, QR & wallet", "blurb": "KWiK, BAI Paga, é-Kwanza.", "div": "pay4all", "rev": "retail", "products": [
            P("kwik", "KWiK", "The central bank's instant-payment scheme run by EMIS, joined by BAI at launch in July 2023: transfers by phone number, e-mail, nickname or IBAN, now mandatory for banks; about 35 million KWiK transfers nationally in 2025.",
              s=["con", "unb"], lc="move", ay="Jul 2023", o="P", at="EMIS, BNA", neo=[0, "EMIS instant payments."],
              src=[["BAI: KWiK", KWIK], ["BAI: KWiK launch, Jul 2023", KWIK23], ["Ver Angola: Multicaixa 2025", MCX25]]),
            P("baipaga", "BAI Paga", "QR-code and reference payments inside BAI Directo, in shops and online, with instant notification.",
              s=["con", "sme"], lc="move", o="B", neo=[0, ""], src=[["BAI: BAI Paga", BAIPAGA]]),
            P("ekwanza", "é-Kwanza (Pay4all)", "The e-money wallet of Pay4all, a group payments company founded in 2023: 1,137,976 é-Kwanza clients and 1,373 distribution points at June 2026; first profit in 2025 (Kz 1.2 billion).",
              s=["unb"], lc="open", ay="2023", o="B", neo=[0, "Wallet; no card network."], div="pay4all",
              mc="A million wallet users with no card credential.",
              src=[["BAI: H1 2026 report", H126], ["BAI: 2025 annual report", AR25]]),
        ]},
        {"id": "2.8", "ic": "globe", "name": "Cross-border", "blurb": "Correspondents, now CIPS.", "div": "group", "rev": "markets", "products": [
            P("correspondent", "Correspondent banking & trade", "Foreign-currency payments, vostro accounts and FX for clients, with BAI Europa in trade finance; first SIBOS stand in 2026 with over 50 meetings with correspondents and technology partners.",
              s=["corp"], lc="move", o="B", neo=[0, ""], src=[["BAI: 2025 annual report", AR25], ["BAI: SIBOS note, Oct 2026", SIBOS]]),
            P("cips", "RMB clearing & CIPS", "A memorandum with Bank of China (8 September 2026) to open a renminbi clearing account and give BAI indirect access to China's CIPS cross-border system.",
              s=["corp"], lc="move", st="new", ay="Sep 2026", o="P", at="Bank of China", neo=[0, "Bank of China / CIPS."],
              src=[["BAI: Bank of China memorandum, Sep 2026", BOC]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: BAI's own security against 3.9 million cyber-attack attempts a year, the LUENA AI assistant, and partner benefits for Premium clients and tourism.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "3.9m attacks, Kz 10.8bn lost.", "div": "bai", "rev": "retail", "products": [
            P("security", "Fraud & cyber defence", "In 2025 BAI logged 12,358 operational-risk events, 3.87 million attempted cyber-attacks and Kz 10.8 billion of losses, mostly internal and external fraud; defences include chip cards, OTP, biometric log-in (2026), QR-validated receipts and anti-phishing campaigns.",
              s=["con", "corp"], lc="everyday", o="B", neo=[0, "BAI's own."],
              mc="No Mastercard fraud or token tools in use; losses show the need.",
              src=[["BAI: 2025 annual report", AR25], ["BAI: H1 2026 report", H126], ["BAI: security and fraud", SECURITY]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI", "blurb": "LUENA assistant.", "div": "bai", "rev": "retail", "products": [
            P("luena", "LUENA & AI", "LUENA, an AI assistant answering customers around the clock (version 2.0 piloted in 2025), plus automated high-volume processes, AI tools for staff and AI-assisted software development.",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["BAI: H1 2026 report", H126], ["BAI: 2025 annual report", AR25]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Benefits & partners", "blurb": "Prestige, tourism card.", "div": "bai", "rev": "private", "products": [
            P("prestige", "BAI Prestige & protocols", "Partner offers for Premium clients through their manager, and a protocol programme with employers and institutions: 7,912 product take-ups and 14 new protocols in 2025. No points scheme found ⚠.",
              s=["prem", "corp"], lc="grow", o="P", neo=[0, ""], src=[["BAI: 2025 annual report", AR25]]),
            P("tourism", "Tourism card & Visit Angola", "An agreement with the tourism institute INFOTUR (2 June 2026) for tourism finance, digital payments and a planned national credit card with benefits at certified operators on the Visit Angola platform.",
              s=["trav", "sme"], lc="beyond", st="new", ay="Jun 2026", o="P", at="INFOTUR", neo=[None, "Network not announced."],
              mc="A card still without a network.",
              src=[["Forbes África Lusófona: INFOTUR and BAI, Jun 2026", INFOTUR]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: accounts for 3.1 million active customers, a fast-growing digital personal loan, housing credit, corporate and agribusiness lending for 3,251 companies, Premium private banking, and insurance and markets through NOSSA and ÁUREA.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Accounts & savings", "blurb": "3.1 million customers.", "div": "bai", "rev": "retail", "products": [
            P("accounts", "Current accounts", "Current, salary, pensioner and simplified BNA accounts, opened in branches, through agents or online: 3,088,238 active customers at June 2026, up 8% in six months.",
              s=["con", "unb"], lc="open", neo=[0, "Multicaixa debit."], src=[["BAI: Q2 2026 results, Jul 2026", Q226], ["BAI: 2025 annual report", AR25]]),
            P("savings", "Deposits & savings", "Term deposits (Super BAI, NET7 and Directo online), rising-rate deposits and Conta Jovem; retail deposits of Kz 1,427 billion at end-2025, up 48%.",
              s=["con", "prem"], lc="grow", neo=[0, ""], src=[["BAI: 2025 annual report", AR25]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Personal lending", "blurb": "Online loans, housing.", "div": "bai", "rev": "retail", "products": [
            P("cpo", "Crédito Pessoal Online", "A fully digital personal loan in BAI Directo with funds at once (2025): 69,647 take-ups in 2025; sold with NOSSA's Vida Digital life cover; pensioner credit added in 2026. Retail loans were Kz 661 billion at end-2025.",
              s=["con"], lc="borrow", st="new", ay="2025", o="B", neo=[0, ""], src=[["BAI: 2025 annual report", AR25], ["BAI: Q2 2026 results, Jul 2026", Q226]]),
            P("housing", "Housing credit", "Mortgages to buy or build, including subsidised housing credit, alongside the BAI Imobiliário property service.",
              s=["con", "prem"], lc="borrow", neo=[0, ""], src=[["BAI: 2025 annual report", AR25]]),
        ]},
        {"id": "4.3", "ic": "factory", "name": "Corporate & agribusiness", "blurb": "3,251 companies.", "div": "bai", "rev": "commercial", "products": [
            P("corporate", "Corporate & institutional banking", "Large and medium companies and the state through seven corporate centres and sector portfolios (oil, gas and minerals; institutions; trade; services; agribusiness; group banks): 3,251 clients at June 2026; corporate loans of Kz 678 billion at end-2025, up 154%.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["BAI: 2025 annual report", AR25], ["BAI: H1 2026 report", H126]]),
            P("agri", "Agribusiness & SME credit", "PAC Express and real-economy credit under BNA rules, Crédito Crescer Mulher for women-led firms, Crédito ECO Futuro green loans and car leasing (2026); 8,172 agribusiness clients.",
              s=["sme"], lc="borrow", o="P", neo=[0, ""], src=[["BAI: 2025 annual report", AR25], ["BAI: multi-brand card note, Aug 2026", MULTI]]),
            P("collections", "Payments & collections for companies", "Mass salary and supplier payments, tax (RUPE) payments, reference payments, collections and cash pick-up and delivery.",
              s=["corp", "sme"], lc="move", neo=[0, ""], src=[["BAI: 2025 annual report", AR25]]),
        ]},
        {"id": "4.4", "ic": "gem", "name": "Premium", "blurb": "1,151 private clients.", "div": "bai", "rev": "private", "products": [
            P("premium", "BAI Premium", "Private banking with a personal manager, concierge and two Premium centres: 1,151 clients and Kz 691 billion of business volume in 2025.",
              s=["prem"], lc="grow", neo=[0, ""], src=[["BAI: Premium", PREMIUM], ["BAI: 2025 annual report", AR25]]),
        ]},
        {"id": "4.5", "ic": "chart-candlestick", "name": "Insurance & markets", "blurb": "NOSSA, ÁUREA.", "div": "nossa", "rev": "insurance", "products": [
            P("nossa", "NOSSA Seguros", "The group insurer (72.24%): 276,168 customers, life and non-life cover, pension funds, and 63,127 Vida Digital policies sold with online loans in 2025.",
              s=["con", "corp"], lc="grow", o="A", neo=[0, ""], src=[["BAI: H1 2026 report", H126], ["BAI: 2025 annual report", AR25]]),
            P("markets", "Markets & ÁUREA", "Treasury and BODIVA settlement for 13 brokers (33,293 trades in 2025) and the broker ÁUREA, which arranged BAI's own bond issues.",
              s=["prem", "corp"], lc="grow", o="B", neo=[0, ""], div="aurea", src=[["BAI: 2025 annual report", AR25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach BAI: the BAI Directo app for a million users, 155 branches and 775 ATMs, and 889 banking-agent posts in shops across the provinces.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "BAI Directo", "blurb": "1.02 million users.", "div": "bai", "rev": "retail", "products": [
            P("app", "BAI Directo app & internet banking", "1,024,978 users at June 2026 and more than 100 functions: biometric log-in, online account opening, personal loans, card loading, KWiK and BAI Paga, and a business app since 2024.",
              s=["con", "sme", "prem"], lc="everyday", o="B", neo=[0, ""], src=[["BAI: Q2 2026 results, Jul 2026", Q226], ["BAI: 2025 annual report", AR25]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "155 branches, 775 ATMs.", "div": "bai", "rev": "retail", "products": [
            P("branches", "Branches & corporate centres", "155 branches and dependencies, seven corporate centres and two Premium centres across 20 provinces.",
              s=["con", "corp"], lc="everyday", neo=[0, ""], src=[["BAI: Q2 2026 results, Jul 2026", Q226], ["BAI: about BAI", ABOUT]]),
            P("atm", "ATMs, deposit machines & ATM Centers", "The largest ATM fleet in Angola: 775 active ATMs, 191 deposit machines and 88 round-the-clock ATM Centers at June 2026; PINs set at the ATM since 2025.",
              s=["con", "unb"], lc="everyday", neo=[0, "Multicaixa network."], src=[["BAI: H1 2026 report", H126], ["BAI: 2025 annual report", AR25]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Banking agents", "blurb": "889 agent posts.", "div": "bai", "rev": "retail", "products": [
            P("agents", "Agente Bancário BAI", "Shops and businesses acting for the bank, ten years old in 2024: 889 agent posts at June 2026 (95 added in the half), for account opening, deposits, withdrawals, transfers and card requests.",
              s=["unb", "sme"], lc="open", o="P", neo=[0, ""], src=[["BAI: banking agents", AGENT], ["BAI: Q2 2026 results, Jul 2026", Q226]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BAI", "blurb": "A corporate card and a new debit card.", "products": [
        P("mcatbai", "Mastercard at BAI", "Of about 2.38 million active cards at June 2026, 92% are domestic Multicaixa, about 176,000 are Visa (Kamba prepaid and credit) and 796 are Mastercard corporate prepaid. In August 2026 BAI launched a Multicaixa debit card that runs on Mastercard abroad; a month later it signed a strategic agreement with Visa.",
          s=["con"], div="group", rev="retail", mc="The relationship this map is drawn for.",
          src=[["BAI: H1 2026 report", H126], ["BAI: multi-brand card note, Aug 2026", MULTI], ["BAI: Visa agreement, Sep 2026", VISA26]]),
    ]},
    {"id": "pillar-market", "name": "Angolan banking", "blurb": "Multicaixa, KWiK, scarce dollars.", "products": [
        P("market", "The Angolan market", "21 banks with about Kz 26 trillion of assets; EMIS runs Multicaixa (3.4 billion operations in 2025, 62% of them in the Multicaixa Express app) and KWiK; dollar scarcity caps international cards; Visa launched a kwanza co-badge debit card with Banco Millennium Atlântico in July 2026.",
          s=["con"], div="group", rev="retail",
          src=[["Ver Angola: Multicaixa 2025", MCX25], ["Ver Angola: Deloitte banking study, Jun 2026", DELOITTE], ["Ver Angola: Visa co-badge with Atlântico, Jul 2026", ATLVISA]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
