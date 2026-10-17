"""Krungsri's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the first-half 2026 results (20 July 2026), the 1H 2026
analyst briefing (3 August 2026), the 2026 analyst briefing (5 February 2026) and the 2025 One Report. Krungsri
Consumer figures come from Thairath Money (April and August 2026). ``neo`` is the Mastercard lens: [depth, note],
where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

OR25 = "https://www.krungsri.com/getmedia/b18ef64e-3e0e-4127-9afb-c4fd7fdb8c39/one-report-2025-en.PDF"
AB26 = "https://www.krungsri.com/getmedia/8e823c5d-bf3d-45a0-b7cb-c6fd262333f4/2026-Analyst-Briefing-Presentation_Delivered.pdf"
H1AB = "https://www.krungsri.com/getmedia/6bd7315f-d091-4359-a9fc-a5334aa04045/1H2026-Analyst-Briefing_3-Aug_delivered.pdf"
H1R = "https://www.krungsri.com/en/newsandactivities/krungsri-banking-news/krungsri-first-half-2026-financial-performance"
Q1R = "https://www.krungsri.com/en/newsandactivities/krungsri-banking-news/krungsri-1q2026-financial-performance"
AMEX = "https://www.krungsri.com/en/newsandactivities/krungsri-banking-news/krungsri-american-express-card-acceptance-thailand"
TRAUG = "https://en.thairath.co.th/money/personal_finance/finance_banking/2951334"
TRAPR = "https://en.thairath.co.th/money/personal_finance/finance_banking/2925532"
CT1B = "https://centralthe1card.com/product-listing/product-detail-the-black"
CT1L = "https://centralthe1card.com/product-listing/product-detail-luxe"
CT1R = "https://centralthe1card.com/product-listing/product-detail-redz"
KPROD = "https://www.krungsricard.com/en/product"
KPM = "https://www.krungsricard.com/en/product/creditcard/krungsri-platinum-mastercard"
KSIG = "https://www.krungsricard.com/en/product/creditcard/krungsri-signature"
KPB = "https://www.krungsricard.com/en/product/creditcard/krungsri-private-banking"
FC = "https://www.firstchoice.co.th/"
LOTUS = "https://www.lotussmoney.com/credit-card/platinum-beyond"
LMS = "https://www.krungsri.com/en/about-krungsri/about-us/subsidiaries/lotus-money-services"
BOARD = "https://www.krungsri.com/en/personal/card/krungsri-boarding-card"
DEBIT = "https://www.krungsri.com/en/personal/card/krungsri-debit-card"
VISA24 = "https://www.krungsri.com/en/newsandactivities/krungsri-banking-news/krungsri-visa-france-with-boarding-and-debit-card"
DC = "https://www.thailand-business-news.com/banking/312813-krungsri-backs-usd-880m-data-center-push-to-make-thailand-aseans-ai-hub"
ITMX = "https://www.mastercard.com/content/dam/mccom/shared/news-and-trends/insights/2026/real-time-payments-ignite-thailand-as-an-economic-force/MC_RTP_ITMX_Case_Study_final.pdf"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · MUFG · plan", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a 1.94 trillion baht loan book and a 4.6% margin, MUFG's 76.88% stake since 2013, a bank founded in 1945, the Jupiter core and the 2024–26 plan to be a sustainable regional bank.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "16.9bn baht profit in the half.", "div": "bay", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Net profit of 16,912 million baht in the first half of 2026 (up 6.8%), NIM 4.60%, cost-to-income 45.5%, loans of 1.94 trillion baht and deposits of 1.69 trillion baht at 30 June 2026, NPLs 3.08% and bank CET1 15.95%; 31,739 million baht profit in 2025. Fifth-largest Thai bank by assets and a domestic systemically important bank since 2017.",
              s=["con", "corp"], neo=[0, ""], src=[["1H 2026 results, Jul 2026", H1R], ["2025 One Report", OR25]]),
        ]},
        {"id": "1.2", "ic": "building-2", "name": "MUFG & leadership", "blurb": "76.88% owned by MUFG.", "div": "mufg", "rev": "group", "products": [
            P("mufg", "MUFG ownership", "MUFG Bank holds 76.88% after a 2013 tender offer and the January 2015 merger of its Bangkok branch; the Ratanarak group and others hold 23.12%. MUFG brings Japanese corporates, about 120,000 payroll accounts since 2015 and a global network. Rated A3 (Moody's) and BBB+ (S&P, Fitch).",
              s=["corp"], o="A", neo=[0, ""], src=[["2025 One Report", OR25], ["2026 analyst briefing", AB26]]),
            P("leadership", "Board & executives", "Chairman Noriaki Goto, President and CEO Kenichi Yamato (since May 2023), CFO and strategy Duangdao Wongpanitkrit, retail and consumer head Sayam Prasitsirigul, Krungsri Consumer head Atis Rujirawat, CIO Saisunee Hanprathueangsil and transaction banking head Ninlawan Jeeraboon.",
              s=["corp"], neo=[0, ""], src=[["2025 One Report", OR25], ["Thairath: Krungsri Consumer, Aug 2026", TRAUG]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology & AI", "blurb": "Jupiter core, 12bn baht IT.", "div": "bay", "rev": "group", "products": [
            P("tech", "Jupiter, Nimble & AI", "About 12 billion baht of group IT investment, the Jupiter core-banking programme, Krungsri Nimble as the IT hub (23 products), an AI centre of excellence, generative AI in knowledge management, and GitHub Copilot planned for 2026.",
              s=["corp"], st="new", o="B", neo=[0, ""], src=[["2025 One Report", OR25], ["2026 analyst briefing", AB26]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Plan & deals", "blurb": "MTBP 2024–26, ROE 9%.", "div": "bay", "rev": "group", "products": [
            P("mtbp", "Medium-Term Business Plan 2024–26", "'The Leading Sustainable and Regional Bank', with an ROE target of 9%. 2026 targets: loan growth 2–4%, NIM 4.0–4.3%, cost-to-income in the mid-40s and credit cost 200–230 bps; a new 350 billion baht sustainable-finance target for 2030.",
              s=["corp"], neo=[0, ""], src=[["2026 analyst briefing", AB26]]),
            P("deals", "Deals", "SB Finance (2020), SHB Finance (2021), Home Credit Philippines and Indonesia (2023), TIDLOR raised to 46.51% and consolidated (August 2025), and Home Credit Indonesia moved to an associate (June 2026).",
              s=["asean", "driver"], o="A", st="flux", neo=[0, ""], src=[["2025 One Report", OR25], ["1H 2026 analyst briefing", H1AB]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Five ways money moves: Thailand's largest credit-card book, mostly Visa with a Mastercard and JCB line; Central The 1 cards on Mastercard; Visa debit and travel cards; 50,000 card terminals now taking Amex; and PromptPay, QR and MUFG's cross-border rails.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Krungsri credit cards", "blurb": "#1 by cards, 15% share.", "div": "kcc", "rev": "retail", "products": [
            P("kccards", "Krungsri credit cards", "Thailand's number one card issuer by number of cards (15% share, September 2025), with 2.4 million customers and 196.7 billion baht of card spending in the first half of 2026. The Krungsri-branded range is mostly Visa (Signature, Exclusive Signature, Private Banking Visa Infinite, Visa Platinum, Manchester United), with JCB cards alongside.", short="Krungsri cards (mostly Visa)",
              s=["card"], lc="everyday", o="B", at="Visa, JCB", neo=[1, "Mostly Visa; one Mastercard line."],
              mc="Krungsri Consumer plans new credit cards in 2026: a network choice in play.",
              src=[["2026 analyst briefing", AB26], ["Thairath: Krungsri Consumer, Aug 2026", TRAUG], ["Krungsri Card: products", KPROD], ["Krungsri Signature", KSIG], ["Krungsri Private Banking card", KPB]]),
            P("kplatmc", "Krungsri Platinum Mastercard", "The one Krungsri-branded Mastercard in the range: a Platinum card earning up to twice the Krungsri Points.", short="Krungsri Platinum Mastercard",
              s=["card"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Krungsri Platinum Mastercard", KPM]]),
            P("firstchoice", "Krungsri First Choice", "Cash card and credit card for mass-market borrowers; the cash card pays wherever Visa is accepted and online instalments on it grew 242% in early 2026.",
              s=["card"], lc="borrow", st="new", ay="2025", o="B", at="Visa", neo=[0, "Visa."], src=[["Krungsri First Choice", FC], ["Thairath: Krungsri Consumer, Aug 2026", TRAUG]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Co-brand cards", "blurb": "Central The 1 on Mastercard.", "div": "central", "rev": "retail", "products": [
            P("central", "Central The 1 credit cards", "The Black, Black, Luxe and REDZ cards for Central Retail shoppers, issued by Krungsri's General Card Services, all on Mastercard with Priority Pass lounges and Mastercard Travel & Lifestyle Services; about 960,000 cards (5.8% of the market) and T1 Dynamic Points since 2025.", short="Central The 1 (Mastercard)",
              s=["card"], lc="everyday", o="P", at="Central Retail, Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's largest anchor at Krungsri.",
              src=[["Central The 1 The Black", CT1B], ["Central The 1 Luxe", CT1L], ["Thairath: Krungsri Consumer, Aug 2026", TRAUG]]),
            P("lotus", "Lotus's credit cards", "Platinum Beyond and Platinum Reward cards for Lotus's shoppers, from Lotus's Money Services (50% Krungsri, formerly Tesco Lotus), with Lotus's Money Coin rewards added in 2025; the terms name both Mastercard and Visa ⚠.",
              s=["card"], lc="everyday", o="P", at="Lotus's", neo=[None, "Mastercard or Visa ⚠."], src=[["Lotus's Platinum Beyond", LOTUS], ["Krungsri: Lotus's Money Services", LMS], ["2025 One Report", OR25]]),
            P("homepro", "HomePro, AIA & Siam Takashimaya cards", "Co-branded HomePro Visa Platinum, AIA Visa Platinum and Siam Takashimaya Visa and JCB cards.",
              s=["card"], lc="everyday", o="P", at="HomePro, AIA, Siam Takashimaya", neo=[0, "Visa and JCB."], src=[["Krungsri Card: products", KPROD]]),
        ]},
        {"id": "2.3", "ic": "plane", "name": "Debit & travel cards", "blurb": "Visa debit, Boarding Card.", "div": "bay", "rev": "retail", "products": [
            P("debit", "Krungsri debit cards", "Debit cards for account holders, including a Manchester United card; online use is registered through Verified by Visa and Krungsri runs debit campaigns with Visa ⚠ domestic TPN use unconfirmed.",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa ⚠."], src=[["Krungsri debit cards", DEBIT], ["Krungsri and Visa campaign, Mar 2024", VISA24]]),
            P("boarding", "Krungsri Boarding Card", "A Visa top-up travel card holding 16 currencies, with rates set in advance in the krungsri app; issuance fee waived since June 2022 ⚠ launch date.",
              s=["con"], lc="move", o="P", at="Visa", neo=[0, "Visa."],
              mc="Travel FX is a Visa franchise here; currency tools could compete.",
              src=[["Krungsri Boarding Card", BOARD], ["Krungsri and Visa campaign, Mar 2024", VISA24]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acceptance", "blurb": "50,127 terminals; Amex added.", "div": "bay", "rev": "sme", "products": [
            P("edc", "Krungsri EDC & Mung-Mee SHOP", "50,127 card terminals (September 2025), Krungsri EDC Plus with the Mung-Mee SHOP app, tap-to-pay on the phone (2025), e-tax invoices and faster merchant onboarding.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["2026 analyst briefing", AB26], ["2025 One Report", OR25]]),
            P("amexaccept", "American Express acceptance", "From 8 September 2026 Krungsri EDC merchants accept American Express cards under a deal with American Express Limited, signed by Ninlawan Jeeraboon.",
              s=["sme"], lc="move", st="new", ay="Sep 2026", o="P", at="American Express", neo=[0, "Amex."], src=[["Krungsri and American Express, Sep 2026", AMEX]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Real-time & cross-border", "blurb": "PromptPay, QR in 8 markets.", "div": "bay", "rev": "corp", "products": [
            P("promptpay", "PromptPay & Thai QR", "Account-to-account payments and QR in the krungsri app and Business PromptPay, on a national rail that carried 2.38 billion transactions worth 4.70 trillion baht in December 2025; Mastercard's Vocalink supplied its technology ⚠.",
              s=["con", "sme"], lc="move", o="P", at="NITMX", neo=[1, "Vocalink tech under the rail ⚠."],
              mc="PromptPay is the main rival to cards for everyday payments.",
              src=[["Mastercard: Thailand real-time payments case study", ITMX], ["2025 One Report", OR25]]),
            P("qrx", "QR cross-border payments", "Pay by QR abroad in Japan, Indonesia, Malaysia, Singapore, Vietnam, Hong Kong and, from 2025, China and South Korea, with inbound corridors from Korea and China.",
              s=["con"], lc="move", st="new", o="P", neo=[0, ""], src=[["2025 One Report", OR25]]),
            P("txn", "Transaction banking", "Global Payment Hub and Global Pooling through MUFG's network, remittance partnerships with money-transfer operators, ISO 20022 for SWIFT and BAHTNET, and the One Corporate Platform.",
              s=["corp"], lc="move", o="B", at="MUFG", neo=[0, ""], src=[["2025 One Report", OR25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account and card: fraud limits and mule-account checks under the Bank of Thailand's rules, an AI centre and card data, APIs for 1,300 partners, and points programmes with Mastercard's travel and retail offers on Central The 1.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "Risk-based limits, mule checks.", "div": "bay", "rev": "retail", "products": [
            P("fraud", "Fraud controls", "Customer profiling for risk-based transaction limits (new customers from August 2025, existing from January 2026) under the Bank of Thailand's digital-fraud framework, mule-account interception, facial comparison and work with the Central Investigation Bureau.",
              s=["con", "sme"], lc="everyday", st="new", o="B", neo=[0, "Krungsri's own."],
              mc="Fraud rules are tightening; scam and transaction-alert tools have no public user here.",
              src=[["2025 One Report", OR25], ["2026 analyst briefing", AB26]]),
            P("ndid", "Digital identity", "National Digital Identity (NDID) upgrade, centralised web consent and eKYC through the bank's APIs.",
              s=["con"], lc="open", o="P", at="NDID", neo=[0, ""], src=[["2026 analyst briefing", AB26], ["2025 One Report", OR25]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data & AI", "blurb": "Card data shapes benefits.", "div": "kcc", "rev": "retail", "products": [
            P("ai", "AI & card data", "An AI centre of excellence and generative AI in the contact centre's knowledge base; Krungsri Consumer combines Krungsri and Central The 1 data to design benefits and segment offers for parents, couples, pet owners and SMEs.",
              s=["card"], lc="grow", st="new", o="B", neo=[0, ""],
              mc="Merchant enrichment and spending insights could feed this segment work.",
              src=[["Thairath: Krungsri Consumer, Aug 2026", TRAUG], ["2025 One Report", OR25]]),
        ]},
        {"id": "3.3", "ic": "code-xml", "name": "APIs & BaaS", "blurb": "1,300+ partners.", "div": "bay", "rev": "corp", "products": [
            P("baas", "API Factory & Banking-as-a-Service", "Open-banking APIs for lending, payments and eKYC, run by Krungsri Nimble since 2025 and used by more than 1,300 partners across business banking, financial institutions and Japanese corporates.",
              s=["sme", "corp"], lc="move", o="B", neo=[0, ""], src=[["2025 One Report", OR25]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Loyalty & offers", "blurb": "Points and Mastercard perks.", "div": "kcc", "rev": "retail", "products": [
            P("points", "Krungsri Point, T1 & Lotus's Money Coin", "Krungsri Points across the bank's cards, T1 Dynamic Points on Central The 1 (2025) and Lotus's Money Coin (2025), redeemed in the U CHOOSE app.",
              s=["card"], lc="grow", o="B", neo=[1, "Central The 1 is Mastercard."], src=[["2025 One Report", OR25], ["Krungsri Card: products", KPROD]]),
            P("mcperks", "Mastercard benefits on Central The 1", "Mastercard Airport Experiences by Priority Pass and Travel & Lifestyle Services on The Black and Black cards, and Mastercard Friday e-coupons at Central Retail stores (25 September to 31 December 2026).",
              s=["card"], lc="grow", st="new", o="P", at="Mastercard", neo=[3, "Mastercard's own benefits."],
              src=[["Central The 1 The Black", CT1B], ["Central The 1 REDZ", CT1R]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: number one in car finance and personal loans, TIDLOR's title loans, mortgages, SME and corporate banking with MUFG's Japanese clients, wealth and securities, and consumer finance in five ASEAN countries.",
    "tiles": [
        {"id": "4.1", "ic": "target", "name": "Auto finance", "blurb": "#1 in hire purchase, 30%.", "div": "auto", "rev": "retail", "products": [
            P("autohp", "Krungsri Auto", "Thailand's leading auto hire-purchase lender with a 30% share, with car-for-cash and title loans (24% of the group's loans) and an ecosystem of more than 300 partners.",
              s=["driver"], lc="borrow", o="B", neo=[0, ""], src=[["2026 analyst briefing", AB26], ["1H 2026 analyst briefing", H1AB]]),
            P("tidlor", "Ngern Tid Lor (TIDLOR)", "Vehicle title loans and insurance broking for 1.2 million customers through 1,873 branches; loans of 109,585 million baht; 46.51% owned and consolidated since August 2025, with a TIDLOR Card in development.",
              s=["driver"], lc="borrow", st="flux", ay="Aug 2025", o="A", neo=[None, "TIDLOR Card network not stated."], src=[["2025 One Report", OR25]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Personal loans & mortgages", "blurb": "#1 in personal loans.", "div": "kcc", "rev": "retail", "products": [
            P("ploan", "Personal loans & instalments", "Number one in personal loans with a 19% share by accounts; Krungsri Consumer targets 98 billion baht of new loans in 2026, and customers are turning card spending into instalments.",
              s=["card"], lc="borrow", o="B", neo=[0, ""], src=[["2026 analyst briefing", AB26], ["Thairath: Krungsri Consumer, Apr 2026", TRAPR]]),
            P("mortgage", "Mortgages", "216.9 billion baht at 30 June 2026, down 2.6% in the year as the bank stays selective in a weak housing market.",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["1H 2026 analyst briefing", H1AB]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "SME banking", "blurb": "15% of loans.", "div": "bay", "rev": "sme", "products": [
            P("sme", "SME Banking", "Loans to small and mid-sized firms (15% of the book), digital top-up loans in the app, supply-chain finance and debt relief under 'You Fight, We Help' (85,012 accounts, 29,335 million baht); Krungsri Consumer cards reach only about 2,000 of 80,000 SME clients.",
              s=["sme"], lc="borrow", neo=[0, ""],
              mc="Commercial cards for SMEs are a small, open field.",
              src=[["2025 One Report", OR25], ["Thairath: Krungsri Consumer, Aug 2026", TRAUG]]),
        ]},
        {"id": "4.4", "ic": "factory", "name": "Corporate & Japanese clients", "blurb": "Corporate loans +6% in 2026.", "div": "mufg", "rev": "corp", "products": [
            P("corp", "Corporate, Japanese corporate & investment banking", "Thai, multinational and Japanese corporates (37% of loans), growing 6.0% in the half on AI supply chains and electronics; a USD 880 million green loan for a 100MW data centre (May 2026).",
              s=["corp"], lc="borrow", o="B", at="MUFG", neo=[0, ""], src=[["1H 2026 results, Jul 2026", H1R], ["Thailand Business News: data-centre loan, Jun 2026", DC]]),
            P("ssf", "Sustainable finance", "250 billion baht of social and sustainable finance reached five years early, a 15.9% share of ESG bond underwriting and a new 350 billion baht target for 2030.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["2025 One Report", OR25], ["2026 analyst briefing", AB26]]),
        ]},
        {"id": "4.5", "ic": "coins", "name": "Wealth & securities", "blurb": "693bn baht under management.", "div": "bay", "rev": "retail", "products": [
            P("wealth", "Asset management, securities & bancassurance", "Krungsri Asset Management with 693,429 million baht under management (6.95% share), Krungsri Securities (2.19% share, accounts opened in the app since August 2025) and bancassurance.",
              s=["con"], lc="grow", o="B", neo=[0, ""], src=[["2025 One Report", OR25]]),
        ]},
        {"id": "4.6", "ic": "earth", "name": "ASEAN", "blurb": "19 million customers, 5 countries.", "div": "asean", "rev": "asean", "products": [
            P("hattha", "Hattha Bank (Cambodia)", "A commercial bank bought in 2016 with about 24.8 billion baht of loans, deposits, Visa debit cards and mobile banking.",
              s=["asean"], lc="everyday", o="A", at="Visa", neo=[0, "Visa debit."], src=[["2026 analyst briefing", AB26]]),
            P("homecredit", "Home Credit & consumer finance", "Home Credit Philippines (75%, 13 million customers, about 55.1 billion baht of loans, a Puregold card), SB Finance, SHB Finance (cards planned for 2026) and Krungsri Leasing in Laos; Home Credit Indonesia became an associate in June 2026.",
              s=["asean"], lc="borrow", st="flux", o="A", neo=[None, "Card networks not stated."],
              mc="New card launches in the Philippines and Vietnam are open network decisions.",
              src=[["2026 analyst briefing", AB26], ["2025 One Report", OR25], ["1H 2026 analyst briefing", H1AB]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the redesigned krungsri app, the U CHOOSE card app, 555 branches and 5,100 ATMs, Krungsri Biz Online for firms, and retail partners such as Central, Lotus's and HomePro.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "krungsri app", "blurb": "Redesigned in 2025.", "div": "bay", "rev": "retail", "products": [
            P("app", "krungsri app", "Relaunched in 2025 with in-app chat, QR scanning with duplicate-payment alerts, securities account opening and SME top-up loans, plus Krungsri Simple on LINE for alerts; user numbers not disclosed ⚠.",
              s=["con", "sme"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["2025 One Report", OR25]]),
        ]},
        {"id": "5.2", "ic": "wallet", "name": "U CHOOSE", "blurb": "The card app.", "div": "kcc", "rev": "retail", "products": [
            P("uchoose", "U CHOOSE", "Krungsri Consumer's app for card, points and cash-card customers, used for statements, temporary limits, points and offers such as U Japan; a pet-owner community is planned.",
              s=["card"], lc="everyday", o="B", neo=[0, ""], src=[["Krungsri Card: products", KPROD], ["Thairath: Krungsri Consumer, Aug 2026", TRAUG]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & ATMs", "blurb": "555 branches, 5,100 ATMs.", "div": "bay", "rev": "retail", "products": [
            P("branches", "Branches, ATMs & exchange booths", "555 domestic branches, 5,100 ATMs, 37 exchange booths, 46 SME centres and 44 Krungsri Exclusive outlets (September 2025), with cardless withdrawals for LH Bank and TMBThanachart customers.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["2026 analyst briefing", AB26], ["2025 One Report", OR25]]),
        ]},
        {"id": "5.4", "ic": "monitor", "name": "Business platforms", "blurb": "Biz Online, The Living Room.", "div": "bay", "rev": "corp", "products": [
            P("kbol", "Krungsri Biz Online & The Living Room", "Krungsri Biz Online on web and mobile, Krungsri Digital Supply Chain and Banking, the iPro onboarding tool and The Living Room portal for business customers.",
              s=["sme", "corp"], lc="open", o="B", neo=[0, ""], src=[["2025 One Report", OR25]]),
        ]},
        {"id": "5.5", "ic": "users-round", "name": "Retail partners", "blurb": "Central, Lotus's, HomePro.", "div": "kcc", "rev": "retail", "products": [
            P("partners", "Retail and platform partners", "Card and loan partnerships with Central Retail, Lotus's, HomePro, AIA and Siam Takashimaya, SCG on the PromptBuy platform, Phyathai hospitals, and Lazada and TrueMoney for SB Finance.",
              s=["card", "asean"], lc="open", o="P", at="Central Retail, Lotus's, HomePro", neo=[1, "Central The 1 on Mastercard."], src=[["2025 One Report", OR25], ["Krungsri Card: products", KPROD]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Krungsri", "blurb": "Central The 1, in a Visa-led book.", "products": [
        P("mcatkrungsri", "Mastercard at Krungsri", "Krungsri is Thailand's largest card issuer by number of cards. Its own-brand premium cards, debit cards and the Boarding Card are Visa, with JCB alongside. Mastercard carries the Central The 1 programme (about 960,000 cards) and a Krungsri Platinum Mastercard, and may carry Lotus's cards ⚠. No network agreement, tokenisation or services deal has been made public.",
          s=["card"], div="kcc", rev="retail", mc="The relationship this map is drawn for.",
          src=[["Central The 1 The Black", CT1B], ["Krungsri Card: products", KPROD], ["Thairath: Krungsri Consumer, Aug 2026", TRAUG]]),
    ]},
    {"id": "pillar-market", "name": "Thai banking", "blurb": "Weak growth, fraud rules, PromptPay.", "products": [
        P("market", "The Thai market", "GDP growth of about 2% forecast for 2026, household debt near 87% of GDP, Bank of Thailand debt-relief and digital-fraud rules, PromptPay at about 2.4 billion transactions a month, and virtual banks entering the card market.",
          s=["con"], div="bay", rev="group", src=[["2025 One Report", OR25], ["Mastercard: Thailand real-time payments case study", ITMX], ["Thairath: Krungsri Consumer, Aug 2026", TRAUG]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
