"""Millennium bcp's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 fact sheet and institutional presentation
(July–September 2026), the 2025 earnings release (25 February 2026) and the 2025-28 Strategic Plan (October 2024).
Card networks come from the bank's card pages and its card price list in force from 7 September 2026. ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

FY25 = "https://live.euronext.com/sites/default/files/company_press_releases/attachments/2026/02/25/cpr01_notified_Earnings%20Millennium%20BCP%20FY25_f.pdf"
Q126 = "https://ind.millenniumbcp.pt/pt/Institucional/investidores/Documents/ApresentacaoResultados/2026/Resultados_Millennium_bcp_1Q2026_f_06052026.pdf"
FS1S26 = "https://ind.millenniumbcp.pt/pt/Institucional/investidores/Documents/ApresentacaoResultados/2026/Fact_Sheet_1S_2026_PT.pdf"
INST = "https://ind.millenniumbcp.pt/pt/Institucional/investidores/Documents/Apresent_Institucional.pdf"
SP = "https://ind.millenniumbcp.pt//en/Institucional/investidores/Documents/2025-28-Strategic-Plan.pdf"
DN24 = "https://www.dn.pt/economia/bcp-sobe-dividendos-e-recompra-acoes-para-se-proteger-de-opa-hostil"
AGM = "https://dinheirovivo.dn.pt/empresas/miguel-maya-reconduzido-como-presidente-executivo-do-bcp"
EXCO = "https://live.euronext.com/sites/default/files/company_press_releases/attachments/2026/05/27/cpr01_notified_2026%2005%2027%20CE%20e%20Comiss%C3%B5es%20CA%20PT.pdf"
DBRS26 = "https://ind.millenniumbcp.pt/pt/Institucional/investidores/Documents/comunicados/2026/20260921_Upgrade_da_DBRS_PT.pdf"
FITCH26 = "https://ind.millenniumbcp.pt//en/Institucional/investidores/Documents/Comunicados/2026/Upgrade_Fitch_EN_13052026.pdf"
MOODYS25 = "https://ind.millenniumbcp.pt/pt/Institucional/investidores/Documents/comunicados/2025/20250521_Moodys_PT.pdf"
PRICE = "https://ind.millenniumbcp.pt/pt/Articles/Documents/precario/SECCAO_03.pdf"
DEBIT = "https://www.millenniumbcp.pt/cartoes/cartao-debito"
CREDIT = "https://www.millenniumbcp.pt/cartoes/cartao-credito"
PRESTIGEDEB = "https://www.millenniumbcp.pt/cartoes/cartao-debito/prestige-debito"
BIZCARDS = "https://www.millenniumbcp.pt/empresas/tesouraria/cartoes"
MCDEB = "https://www.millenniumbcp.pt/empresas/tesouraria/cartoes/mastercard-debito-empresas"
GOLDEMP = "https://www.millenniumbcp.pt/empresas/tesouraria/cartoes/gold-empresas"
TAPBIZ = "https://www.millenniumbcp.pt/empresas/tesouraria/cartoes/tap-business"
BIZPREPAID = "https://www.millenniumbcp.pt/empresas/tesouraria/cartoes/pre-pago-business"
MBWAY = "https://www.millenniumbcp.pt/cartoes/mb-way"
PAYME = "https://www.millenniumbcp.pt/empresas/tesouraria/pagamentos-recebimentos/pay-me"
MOOVE = "https://www.millenniumbcp.pt/empresas/tesouraria/pagamentos-recebimentos/tpa-smart-moove"
TPAAN = "https://www.millenniumbcp.pt/empresas/tesouraria/pagamentos-recebimentos/tpa-analytics"
CASHONTIME = "https://ind.millenniumbcp.pt/pt/Institucional/imprensa/Documents/2026/2026_09_28_Millennium_bcp_lanca_Solucao_Digital.pdf"
GO22 = "https://ind.millenniumbcp.pt/pt/Institucional/imprensa/Documents/2022/GO_Changer_25012022.pdf"
UP17 = "https://ind.millenniumbcp.pt/pt/Institucional/imprensa/Documents/2017/Millenniumbcp-UnionPay-Int-PT-17112017.PDF"
UP19 = "https://ind.millenniumbcp.pt/pt/Institucional/imprensa/Documents/2019/MILLENNIUM_BCP_INICIA_EMISSAO_CARTOES_UNIONPAY_25012019.pdf"
AIACAD = "https://ind.millenniumbcp.pt/pt/Institucional/imprensa/Documents/2025/20251112_Millenniumbcp_Nova_SBE_AIAcademy_PT.pdf"
QORUS = "https://www.qorusglobal.com/innovations/28567-digital-money-management-with-ai"
AWARDS = "https://ind.millenniumbcp.pt/pt/Institucional/imprensa/Documents/2026/Premios_Cinco_Estrelas_Escolha_Consumidor_PT_12012026.pdf"
PLPRES = "https://www.bankmillennium.pl/documents/d/guest/millennium-1h26_en_pres"
PLCARDS = "https://www.bankmillennium.pl/klienci-indywidualni/karty-platnicze"
PLIMPRESJA = "https://www.bankmillennium.pl/klienci-indywidualni/karty-platnicze/karty-kredytowe/millennium-impresja"
PLPREPAID = "https://www.bankmillennium.pl/klienci-indywidualni/karty-platnicze/karty-przedplacone"
PLC2P = "https://www.gsmmaniak.pl/1690863/millennium-bank-nowosc-metoda-platnosci/amp/"
BIMVISA = "https://millenniumbim.co.mz/media/moapgntz/condicoes-gerais-de-utilizacao-dos-cartoes-visa.pdf"
BIMIZI = "https://millenniumbim.co.mz/media/icxk0v2k/comunicado-mbim-lanca-novas-funcionalidades-smart-izi.pdf"
EUROPA = "https://observador.pt/2026/04/16/sibs-dona-do-multibanco-e-mbway-entra-em-parceria-europeia-para-destronar-americanas-visa-e-mastercard-e-antecipar-se-ao-euro-digital/"
SIBSRC = "https://www.corporate.sibs.com/wp-content/uploads/2026/06/RC_Grupo-SIBS_2025_Final.pdf"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owners · plan", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Portugal's second-largest bank with 7.4 million active customers across three countries, €566 million of profit in the half, Fosun and Sonangol as anchor shareholders, a cloud and GenAI programme, and the 2025-28 plan to deliver more value.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & ratings", "blurb": "€566m in H1, CET1 15.1%.", "div": "group", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Net income of €565.8 million in H1 2026 (+12.7%) and €1,018.6 million in 2025 (+12.4%); ROE 14.6%; loans of €65.2 billion and customer funds of €116.7 billion at 30 June 2026; CET1 15.1%; 7.4 million active customers and 15,747 staff at end-2025.",
              s=["con"], neo=[0, ""], src=[["Fact sheet H1 2026", FS1S26], ["2025 earnings release", FY25]]),
            P("ratings", "Credit ratings", "Morningstar DBRS raised senior debt to A on 21 September 2026; Fitch raised deposits to A in May 2026; Moody's deposits A2 since May 2025. S&P not checked ⚠.",
              s=["corp"], st="new", neo=[0, ""], src=[["DBRS upgrade, Sep 2026", DBRS26], ["Fitch upgrade, May 2026", FITCH26], ["Moody's upgrade, May 2025", MOODYS25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & owners", "blurb": "Maya and Amado to 2029.", "div": "group", "rev": "other", "products": [
            P("leadership", "Board & executive committee", "Chair Nuno Amado and CEO Miguel Maya reappointed for 2026–2029 on 7 May 2026; Miguel Bragança and João Nuno Palma are vice-chairs of the executive committee. Who owns payments is not published ⚠.",
              s=["corp"], neo=[0, ""], src=[["Dinheiro Vivo: Maya reappointed, May 2026", AGM], ["BCP: executive committee, May 2026", EXCO]]),
            P("owners", "Shareholders", "Fosun 20.5% and Sonangol 19.9%, the rest spread across about 112,000 holders; listed on Euronext Lisbon, about €14 billion market value in May 2026 ⚠ derived from the buyback size.",
              s=["corp"], neo=[0, ""], src=[["Institutional presentation", INST], ["Fact sheet H1 2026", FS1S26]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology & AI", "blurb": "GenAI and a data platform.", "div": "group", "rev": "other", "products": [
            P("tech", "Cloud, data & GenAI", "A modular, event-based stack with a cloud Enterprise Data Platform; targets of more than 70% of core data migrated, more than 75% of documents processed with GenAI and more than 70% of retail servicing journeys digital by 2028; an in-house 'Agent Lab' and 'Sourcery' code-migration tool.",
              s=["corp"], o="B", neo=[0, ""], src=[["2025-28 Strategic Plan", SP]]),
            P("aiacademy", "AI Academy", "With Nova SBE, training more than 6,500 staff in AI, focused on generative AI, until 2027 (November 2025).",
              s=["corp"], st="new", ay="Nov 2025", o="P", at="Nova SBE", neo=[0, ""], src=[["BCP: AI Academy, Nov 2025", AIACAD]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Deliver more value 2028", "blurb": ">8m customers, ROE >13.5%.", "div": "group", "rev": "other", "products": [
            P("strategy", "2025-28 Strategic Plan", "More than 8 million active customers and over 80% mobile by 2028, cost-to-income below 40%, cost of risk below 50 bp, ROE and CET1 above 13.5%; in Portugal, lead in companies and the affluent, with ActivoBank leading digital acquisition.",
              s=["corp"], neo=[0, ""], src=[["2025-28 Strategic Plan", SP], ["Institutional presentation", INST]]),
            P("payout", "Shareholder distributions", "Payout raised to up to 90% of 2025 profit (50% dividend, 40% buyback) at the May 2026 AGM; a €407.5 million buyback began on 4 June 2026. DN linked the higher payout in 2024 to deterring a hostile bid ⚠.",
              s=["corp"], st="new", ay="May 2026", neo=[0, ""], src=[["Fact sheet H1 2026", FS1S26], ["DN: payout and hostile bid, Oct 2024", DN24]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Visa debit co-badged with Multibanco, Visa credit and the TAP co-brand, Europe's first UnionPay cards, business cards with one Mastercard debit card, MB WAY and phone wallets, terminals and an online gateway, and dual-network cards with Click to Pay at Bank Millennium in Poland.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Visa and Multibanco.", "div": "bcp", "rev": "retail", "products": [
            P("debit", "Débito, Prestige & Gold debit", "Every adult debit card now sold in Portugal is Visa co-badged with Multibanco, at €23.50 a year, issued instantly as a digital card in the app.", short="Debit (Visa + MB)",
              s=["con", "affluent"], lc="everyday", o="P", at="Visa, SIBS", neo=[0, "Visa."], src=[["Price list, Sep 2026", PRICE], ["Millennium bcp: debit cards", DEBIT]]),
            P("juniordebit", "Jovem 12/17 debit", "A debit card for 12 to 17-year-olds listed under Mastercard, Visa and Multibanco ⚠ which network the card carries is unclear.",
              s=["con"], lc="everyday", neo=[1, "Mastercard and Visa listed ⚠."], src=[["Price list, Sep 2026", PRICE]]),
            P("mclegacy", "Mastercard Débito, GO! Débito & Maestro", "Mastercard and Maestro debit cards, now listed as no longer sold; cards in circulation still carry Mastercard ⚠ number and switch date unpublished.", short="Legacy Mastercard debit",
              s=["con"], lc="everyday", st="retired", o="I", neo=[2, "Mastercard, no longer sold."],
              mc="The trace of a Mastercard debit book that has moved to Visa.",
              src=[["Price list, Sep 2026", PRICE]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Visa, with TAP miles.", "div": "bcp", "rev": "retail", "products": [
            P("credit", "GO!, Classic, Platinum & Gold Prestige", "Credit cards from no fee (GO!) to Platinum, on Visa and Multibanco, with Millennium Rewards on the upper tiers; GO! Changer (2022) was a biodegradable Visa card.", short="Credit (Visa)",
              s=["con", "affluent", "digital"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Price list, Sep 2026", PRICE], ["Millennium bcp: credit cards", CREDIT], ["GO! Changer, Jan 2022", GO22]]),
            P("tapcard", "TAP Miles&Go cards", "TAP Classic, Gold and Platinum earn 1 to 2 miles per euro, on Visa.",
              s=["affluent"], lc="beyond", o="P", at="TAP Air Portugal, Visa", neo=[0, "Visa."], src=[["Price list, Sep 2026", PRICE], ["Millennium bcp: credit cards", CREDIT]]),
            P("legacycredit", "Legacy Mastercard & American Express cards", "Classic, FIX, Gold and Prestige Mastercard credit cards and all American Express cards are listed as no longer sold ⚠ switch dates unpublished.", short="Legacy Mastercard credit",
              s=["con"], lc="borrow", st="retired", o="I", neo=[1, "Mastercard or Visa; no longer sold."],
              mc="Mastercard credit has been replaced by Visa in Portugal.",
              src=[["Price list, Sep 2026", PRICE]]),
        ]},
        {"id": "2.3", "ic": "earth", "name": "UnionPay", "blurb": "Europe's first issuer.", "div": "bcp", "rev": "retail", "products": [
            P("unionpay", "UnionPay debit & Travel Mate", "Europe's first UnionPay issuer (agreement November 2017, cards from January 2019, with a goal of 200,000 cards in five years); today UnionPay debit and Travel Mate Platinum and Business cards for trade with Asia.",
              s=["affluent", "sme"], lc="move", ay="Jan 2019", o="P", at="UnionPay International", neo=[0, "UnionPay."],
              src=[["UnionPay agreement, Nov 2017", UP17], ["UnionPay issuing, Jan 2019", UP19], ["Price list, Sep 2026", PRICE]]),
        ]},
        {"id": "2.4", "ic": "briefcase-business", "name": "Business cards", "blurb": "Visa, one Mastercard debit.", "div": "empresas", "rev": "companies", "products": [
            P("bizcredit", "Gold, Silver & TAP Business", "Company credit cards for staff expenses with insurance and digital statements; Gold and Silver on Visa, TAP Business on Visa Commercial.",
              s=["sme", "corp"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Millennium bcp: business cards", BIZCARDS], ["Gold Empresas", GOLDEMP], ["TAP Business", TAPBIZ]]),
            P("mcbiz", "Mastercard Débito Empresas", "A business debit card for company spending, contactless, sold only in branches: the one Mastercard card still on sale in Portugal.", short="Business debit (Mastercard)",
              s=["sme"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's only live issuing foothold at the Portuguese bank.",
              src=[["Mastercard Débito Empresas", MCDEB]]),
            P("bizprepaid", "Pré-pago Business & MRefeição", "A Visa prepaid card for staff expenses at home and abroad, and the MRefeição meal card.",
              s=["sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Pré-pago Business", BIZPREPAID], ["Millennium bcp: business cards", BIZCARDS]]),
        ]},
        {"id": "2.5", "ic": "smartphone", "name": "MB WAY & wallets", "blurb": "MB WAY inside the app.", "div": "bcp", "rev": "retail", "products": [
            P("mbway", "MB WAY & MB NET", "SIBS's MB WAY built into the Millennium app for P2P, QR and online payments and cardless withdrawals (59% of customers prefer it there), and free MB NET virtual cards.",
              s=["con", "digital"], lc="move", o="P", at="SIBS", neo=[0, "SIBS domestic rail."], src=[["Millennium bcp: MB WAY", MBWAY]]),
            P("wallets", "Apple Pay, Google Pay & Samsung Wallet", "Cards added to Apple Pay, Google Pay, Samsung Wallet and Garmin Pay at issue; the cards are Visa.",
              s=["con", "digital"], lc="move", o="P", at="Apple, Google, Samsung", neo=[0, "Visa cards."], src=[["Millennium bcp: debit cards", DEBIT]]),
            P("europa", "EuroPA interoperability", "SIBS, owner of MB WAY, with Bizum, Bancomat, Vipps MobilePay and EPI: P2P across 13 countries by end-2026 and shop payments at common terminals by end-2027, aimed at displacing Visa and Mastercard.",
              s=["con"], lc="move", st="new", o="P", at="SIBS", neo=[0, "A rival rail."],
              mc="A European account-to-account rail aimed squarely at the card schemes.",
              src=[["Observador: SIBS and EuroPA, Apr 2026", EUROPA], ["SIBS annual report 2025", SIBSRC]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acceptance", "blurb": "Terminals and P@y.me.", "div": "empresas", "rev": "companies", "products": [
            P("tpa", "TPA & Smart Moove terminals", "Card terminals in three formats, including an Android terminal taking chip, contactless and MB WAY QR payments, with no fixed monthly fee and a Moove back office. Acquiring licence and processor not published ⚠.",
              s=["merchant", "sme"], lc="move", neo=[1, "Accepts every network."], src=[["TPA Smart Moove", MOOVE]]),
            P("payme", "P@y.me gateway", "An online payment gateway taking MB WAY, Multibanco references and Visa and Mastercard cards, with e-commerce plug-ins, for €6 a month plus about 1.2% a payment.",
              s=["merchant"], lc="move", o="B", neo=[1, "Accepts Visa and Mastercard."], src=[["P@y.me", PAYME]]),
        ]},
        {"id": "2.7", "ic": "flag", "name": "Bank Millennium cards", "blurb": "Dual network, Click to Pay.", "div": "poland", "rev": "intl", "products": [
            P("plcredit", "Impresja, Gold, WWF & Global credit", "Credit cards on Visa or Mastercard: Impresja (Mastercard promoted to 15 November 2026 with a Moneyback programme to June 2027), Visa/Mastercard Gold, WWF Millennium Mastercard and Visa Global; about 553,000 credit cards in June 2026.", short="Poland credit (Visa & Mastercard)",
              s=["abroad"], lc="borrow", o="P", at="Visa, Mastercard", neo=[1, "Visa or Mastercard."], src=[["Bank Millennium: Impresja", PLIMPRESJA], ["Bank Millennium: payment cards", PLCARDS], ["Bank Millennium 1H26 presentation", PLPRES]]),
            P("pldebit", "Debit, Voyager, Visa Raz & prepaid", "About 4.2 million debit cards on Visa and Mastercard ⚠ split unknown, the euro Mastercard Voyager, Millennium Mastercard Prepaid, and the Millennium Visa Raz one-time virtual card (from 23 June 2026).",
              s=["abroad"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard ⚠ split."], src=[["Bank Millennium: payment cards", PLCARDS], ["Bank Millennium: prepaid", PLPREPAID], ["Bank Millennium 1H26 presentation", PLPRES]]),
            P("c2p", "Click to Pay", "Mastercard cards issued by Bank Millennium can be added to Click to Pay in the app for tokenised online checkout (September 2026).", short="Click to Pay (Mastercard)",
              s=["abroad"], lc="move", st="new", ay="Sep 2026", o="P", at="Mastercard", neo=[3, "Mastercard's own product."],
              mc="Proof inside the group that Mastercard's digital services land.",
              src=[["gsmManiaK: Click to Pay, Sep 2026", PLC2P]]),
            P("blik", "BLIK", "Poland's mobile payment scheme, used by 2.45 million Bank Millennium customers in H1 2026 (+21% y/y).",
              s=["abroad"], lc="move", o="P", at="BLIK", neo=[0, "Domestic scheme."], src=[["Bank Millennium 1H26 presentation", PLPRES]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud controls and digital identity, AI money management and in-house models, Millennium Rewards and TAP miles, and merchant analytics and APIs.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "Real-time monitoring planned.", "div": "group", "rev": "other", "products": [
            P("fraud", "Fraud, AML & card controls", "A plan to invest heavily in real-time fraud, AML and KYC monitoring; customers switch contactless, online and foreign use on and off in the app; fraudulent-use insurance on cards. Vendors not public.",
              s=["con", "sme"], lc="everyday", neo=[None, "Vendors not public."],
              mc="The plan's fraud push is open to network-agnostic tools.",
              src=[["2025-28 Strategic Plan", SP], ["Millennium bcp: debit cards", DEBIT]]),
            P("identity", "Chave Móvel Digital & Millennium ID", "Log-in and onboarding with Portugal's state digital key, including for non-clients; in Poland, Millennium ID with a QR code for public e-services.",
              s=["con", "corp", "abroad"], lc="open", o="P", at="AMA (Portuguese state)", neo=[0, ""], src=[["Cash-on-Time, Sep 2026", CASHONTIME], ["Bank Millennium 1H26 presentation", PLPRES]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data & AI", "blurb": "AI money management.", "div": "bcp", "rev": "retail", "products": [
            P("dmm", "AI money management", "AI in the app to uncover hidden spending and give real-time insights (Qorus–Infosys awards entry, June 2024) ⚠ features not detailed.",
              s=["con"], lc="everyday", ay="Jun 2024", o="B", neo=[None, "Nothing public."],
              mc="Merchant and spend data would sharpen these insights.",
              src=[["Qorus: digital money management with AI", QORUS]]),
            P("datamodels", "Enterprise data & AI models", "Customer engagement, mass personalisation and loyalty listed as priority data products; an in-house behavioural model is reported ⚠ not confirmed by the bank.",
              s=["corp"], st="unconf", o="B", neo=[0, ""], src=[["2025-28 Strategic Plan", SP]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty", "blurb": "Rewards, miles, hotels.", "div": "prestige", "rev": "retail", "products": [
            P("rewards", "Millennium Rewards & travel benefits", "Points turned into offers on Platinum and Gold Prestige, TAP Miles&Go co-brands, and Visa Luxury Hotel Collection on the Prestige debit card.",
              s=["affluent", "con"], lc="beyond", o="P", at="Visa, TAP", neo=[0, "Visa benefits."],
              mc="Card-linked offers could sit alongside Millennium Rewards.",
              src=[["Millennium bcp: credit cards", CREDIT], ["Prestige Débito", PRESTIGEDEB]]),
        ]},
        {"id": "3.4", "ic": "chart-column", "name": "Merchant data & APIs", "blurb": "TPA Analytics, API onboarding.", "div": "empresas", "rev": "companies", "products": [
            P("tpaanalytics", "TPA Analytics", "Free analytics for card-accepting merchants: monthly sales, number of customers, peak days and hours, and customer age and gender.",
              s=["merchant"], lc="grow", o="B", neo=[0, "Bank's own."],
              mc="Merchant insight is where Mastercard data services compete.",
              src=[["TPA Analytics", TPAAN]]),
            P("apis", "APIs & open banking", "API-based onboarding of non-client suppliers for Cash-on-Time; no consumer open-banking product found ⚠.",
              s=["corp", "sme"], lc="open", st="new", o="B", neo=[None, "Nothing public."], src=[["Cash-on-Time, Sep 2026", CASHONTIME]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: retail and Prestige banking for 2.9 million customers in Portugal, ActivoBank for digital natives, lending and supply-chain finance for companies, bancassurance with Ageas, Bank Millennium in Poland and Millennium bim in Mozambique.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Retail & Prestige", "blurb": "16.5% of loans, 18.5% of deposits.", "div": "bcp", "rev": "retail", "products": [
            P("accounts", "Accounts & deposits", "About 2.9 million customers in Portugal, 67% mobile; 18.5% of deposits (July 2026); Portugal's second-largest bank by business volume.",
              s=["con"], lc="everyday", neo=[0, "Visa debit."], src=[["Institutional presentation", INST]]),
            P("mortgages", "Mortgages & personal loans", "16.5% of loans in Portugal (July 2026); Portuguese loans up 8.6% y/y in June 2026.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Institutional presentation", INST], ["Fact sheet H1 2026", FS1S26]]),
            P("prestige", "Prestige & Private Banking", "Advisory for the affluent with tiered relationship managers, and Private Banking with its own Visa cards.",
              s=["affluent"], lc="grow", neo=[0, "Visa cards."], src=[["2025-28 Strategic Plan", SP], ["Price list, Sep 2026", PRICE]]),
        ]},
        {"id": "4.2", "ic": "rocket", "name": "ActivoBank", "blurb": "400k, aiming for 700k.", "div": "activo", "rev": "retail", "products": [
            P("activobank", "ActivoBank", "A digital-first bank with about 400,000 active customers in 2024, aiming for more than 700,000 by 2028, adding lending, mortgages and GenAI service. Card network not checked ⚠.",
              s=["digital"], lc="open", o="B", neo=[None, "Network not checked."], src=[["2025-28 Strategic Plan", SP]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Companies & corporate", "blurb": "Supply-chain finance.", "div": "empresas", "rev": "companies", "products": [
            P("companies", "Companies, corporate & investment banking", "About 18% of lending to Portuguese companies (2024), aiming for about 20% by 2028, small-business credit to double, factoring and trade, and over €2 billion of energy-transition lending planned; Euromoney's best digital bank for SMEs in Portugal.",
              s=["sme", "corp"], lc="borrow", neo=[1, "Visa cards; one Mastercard debit card."], src=[["2025-28 Strategic Plan", SP], ["Cash-on-Time, Sep 2026", CASHONTIME]]),
            P("cashontime", "Cash-on-Time & Confirming", "Suppliers, now including non-clients, discount invoices approved by their buyers online, through APIs and the state digital key (September 2026).",
              s=["sme", "corp"], lc="borrow", st="new", ay="Sep 2026", o="B", neo=[0, ""], src=[["Cash-on-Time, Sep 2026", CASHONTIME]]),
        ]},
        {"id": "4.4", "ic": "coins", "name": "Insurance & savings", "blurb": "Ageas, asset management.", "div": "ageas", "rev": "retail", "products": [
            P("ageas", "Bancassurance & asset management", "Millenniumbcp Ageas life and non-life insurance (bancassurance commissions €141 million in 2025) and asset management and distribution (€95 million).",
              s=["con", "affluent"], lc="grow", o="P", at="Ageas", neo=[0, ""], src=[["2025 earnings release", FY25]]),
        ]},
        {"id": "4.5", "ic": "flag", "name": "Bank Millennium", "blurb": "3.35m clients, PLN 708m.", "div": "poland", "rev": "intl", "products": [
            P("bankmillennium", "Bank Millennium (Poland)", "50.01% owned: 3.35 million active retail clients, net profit of PLN 708 million in H1 2026 (+39%), ROE 14.5%, corporate loans +41% y/y; Swiss-franc mortgage costs falling.",
              s=["abroad"], lc="everyday", o="A", neo=[1, "Dual Visa and Mastercard."], src=[["Bank Millennium 1H26 presentation", PLPRES], ["Fact sheet H1 2026", FS1S26]]),
        ]},
        {"id": "4.6", "ic": "globe", "name": "Mozambique & Macau", "blurb": "bim, 21.7% of deposits.", "div": "bim", "rev": "intl", "products": [
            P("bim", "Millennium bim", "66.67% owned: 18.2% of Mozambique's loans and 21.7% of deposits, 191 branches; cards on Visa ⚠; profit hit by sovereign-debt impairments in 2025.",
              s=["abroad"], lc="everyday", o="A", at="Visa", neo=[0, "Visa ⚠."], src=[["Institutional presentation", INST], ["Millennium bim: Visa card conditions", BIMVISA], ["2025 earnings release", FY25]]),
            P("macau", "Macau branch & Angola stake", "An on-shore branch in Macau serving China–Portuguese-speaking trade, and an equity stake in Banco Millennium Atlântico in Angola.",
              s=["corp"], lc="move", neo=[0, ""], src=[["Institutional presentation", INST], ["2025 earnings release", FY25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the Millennium app, used by three in four customers, 385 branches in Portugal, the Empresas website, and the Bank Millennium and Smart IZI apps abroad.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "75% of customers mobile.", "div": "group", "rev": "retail", "products": [
            P("app", "App Millennium", "75% of the group's 7.4 million customers are mobile (June 2026); the app won a Cinco Estrelas award in January 2026.",
              s=["con", "digital", "affluent"], lc="everyday", o="B", neo=[0, ""], src=[["Fact sheet H1 2026", FS1S26], ["BCP: awards, Jan 2026", AWARDS]]),
            P("plapp", "Bank Millennium & Smart IZI apps", "Bank Millennium: 2.99 million active mobile users, 2.52 million mobile-only; Millennium bim's Smart IZI app with Western Union transfers.",
              s=["abroad"], lc="everyday", o="B", neo=[0, ""], src=[["Bank Millennium 1H26 presentation", PLPRES], ["Millennium bim: Smart IZI", BIMIZI]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "385 in Portugal.", "div": "bcp", "rev": "retail", "products": [
            P("branches", "Branches", "385 branches in Portugal (12% of the system's), 585 in Poland and 191 in Mozambique (June 2026).",
              s=["con", "affluent", "sme"], lc="open", neo=[0, ""], src=[["Institutional presentation", INST]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "Empresas website", "blurb": "Product of the Year 2026.", "div": "empresas", "rev": "companies", "products": [
            P("empresasweb", "Empresas website", "The companies' website, named Product of the Year 2026 for companies (Escolha do Consumidor) and now open to non-clients for Cash-on-Time.",
              s=["sme", "corp", "merchant"], lc="open", o="B", neo=[0, ""], src=[["Cash-on-Time, Sep 2026", CASHONTIME]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Millennium bcp", "blurb": "Visa in Portugal, dual in Poland.", "products": [
        P("mcatbcp", "Mastercard at Millennium bcp", "In Portugal every new consumer card is Visa with Multibanco, plus UnionPay; Mastercard and Maestro debit and Mastercard credit cards are listed as no longer sold, leaving a branch-only Mastercard business debit card and acceptance on terminals and P@y.me. In Poland, Bank Millennium issues both networks, pushes Mastercard credit and added Mastercard Click to Pay in September 2026. No public Mastercard services deal was found ⚠.",
          s=["con"], div="group", rev="other", mc="The relationship this map is drawn for.",
          src=[["Price list, Sep 2026", PRICE], ["Mastercard Débito Empresas", MCDEB], ["gsmManiaK: Click to Pay, Sep 2026", PLC2P]]),
    ]},
    {"id": "pillar-market", "name": "Portuguese banking", "blurb": "Five banks, SIBS, EuroPA.", "products": [
        P("market", "The Portuguese market", "The top five banks hold about 80% of the market and BCP is second with about 17%; SIBS runs Multibanco and MB WAY and, through EuroPA, plans pan-European P2P by end-2026 and shop payments by end-2027; the digital euro is not expected before 2029.",
          s=["con"], div="group", rev="other", src=[["Institutional presentation", INST], ["Observador: SIBS and EuroPA, Apr 2026", EUROPA]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
