"""CRDB Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the 1H 2026 Investors' Briefing (July 2026) and
the 2025 Integrated Report (published May 2026). Amounts are Tanzanian shillings (TZS); about TZS 2,600 = USD 1.
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

IB = "https://crdbbank.co.tz/storage/app/media/For%20Investor/CRDB%20Investor%20Briefing%201H2026.pdf"
IR = "https://crdbbank.co.tz/storage/app/media/Our%20Investors/Annual%20Reports/crdb-ir-2025-8th-may-2026.pdf"
FACT = "https://crdbbank.co.tz/storage/app/media/Our%20Investors/Investor%20Fact%20Sheet.pdf"
SHARE = "https://crdbbank.co.tz/storage/app/media/Shareholding_Structure_Jun_2026.pdf"
ABOUT = "https://crdbbank.co.tz/en/about-us"
CDHOME = "https://crdbbank.cd"
BITEMBO = "https://crdbbank.co.bi/for-you/ways-to-bank/tembo-card"
DRCVISA = "https://bankable.africa/en/digital/1104-2740-crdb-bank-launches-tembocard-visa-to-expand-access-to-global-payment-networks-in-drc"
BPC = "https://africa.com/happening/crdb-bank-embarks-on-digital-transformation-with-bpc-next-generation-smartvista-platform"
TC24 = "https://techcabal.com/zu/2025/09/16/Ukulungiswa-Okukhulu-Kwebhange-LaseTanzania/"
DFI = "https://www.intelligentcio.com/africa/2025/10/27/crdb-bank-signs-three-landmark-partnerships-to-advance-inclusive-finance-and-sustainable-development-across-africa/"
CARDS = "https://crdbbank.co.tz/en/for-you/ways-to-bank/debit-cards"
INFINITE = "https://crdbbank.co.tz/en/for-you/ways-to-bank/debit-cards/tembocard-visa-infinite"
METAL = "https://crdbbank.co.tz/en/for-you/ways-to-bank/debit-cards/metal-debit-card"
YANGA = "https://crdbbank.co.tz/en/for-you/ways-to-bank/debit-cards/yanga-visa-card"
SIMBA = "https://crdbbank.co.tz/en/for-you/ways-to-bank/debit-cards/simba-fan-classic"
GOLDCC = "https://crdbbank.co.tz/en/for-you/ways-to-bank/debit-cards/gold-credit-card"
INFCC = "https://crdbbank.co.tz/en/for-you/ways-to-bank/debit-cards/infinite-credit-card"
PREPAID = "https://crdbbank.co.tz/en/for-you/ways-to-bank/debit-cards/prepaid-cards"
UPIV = "https://crdbbank.co.tz/en/for-you/ways-to-bank/debit-cards/tembo-upi-virtual-card"
UPIAWARD = "https://www.thecitizen.co.tz/tanzania/business/crdb-bank-lands-china-union-pay-award-2675774"
PREMIER = "https://crdbbank.co.tz/en/for-you/premier-banking/premier-banking"
MCCC2018 = "https://www.thecitizen.co.tz/tanzania/news/national/crdb-upgrades-tembocard-to-credit-card-2624328"
VISA2021 = "https://www.thecitizen.co.tz/tanzania/business/crdb-bank-visa-international-unveil-new-campaign-to-promote-cashless-transactions-3638834"
LIPA = "https://crdbbank.co.tz/en/for-business/ways-to-bank/crdb-lipa-hapa"
TANQR = "https://www.bot.go.tz/Publications/Acts,%20Regulations,%20Circulars,%20Guidelines/Circulars/en/2022081908435357.pdf"
SIMB = "https://crdbbank.co.tz/en/for-you/ways-to-bank/mobile-banking"
TIPSAWARD = "https://www.thecitizen.co.tz/tanzania/business/bank-of-tanzania-wins-global-award-for-digital-financial-inclusion-innovations-5196098"
REMIT = "https://crdbbank.co.tz/en/for-you/remittance-service/remittance-service"
FOREXATM = "https://crdbbank.co.tz/en/for-you/ways-to-bank/forex-atm"
TEMBOPTS = "https://crdbbank.co.tz/en/for-you/ways-to-bank/bank-loyalty-program"
WAKALA = "https://crdbbank.co.tz/en/for-you/ways-to-bank/agency-banking"
DUBAI = "https://crdbbank.co.tz/en/crdb-dubai"
TCRA = "https://tanzaniainvest.com/telecoms/telecom-subscriptions-q2-2026"
NMBMC = "https://www.nation.africa/tanzania/business/nmb-mastercard-launch-new-credit-card-for-smes-5511118"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · owners · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: TZS 26.4 trillion of assets and about 29% of Tanzania's banking market, owners led by Denmark's DANIDA fund and Tanzanian pension funds, thirty years of history with banks in Burundi and the DRC, a new T24 core and BPC card switch, and the EVOLVE plan to 2027.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "TZS 417bn profit in 1H 2026.", "div": "crdb", "rev": "corp", "products": [
            P("balance", "Balance sheet & earnings", "1H 2026: profit after tax TZS 417 billion (up 20.3%), total assets TZS 26.4 trillion (up 33.9%), net loans TZS 17.0 trillion, customer deposits TZS 18.5 trillion, ROE 28.0%, gross NPL 2.4%, total capital 16.2%. FY2025: profit TZS 728.6 billion, ROE 29.5%. About 29% of Tanzania's banking assets and deposits and 31% of loans (2025); 7.95 million customers (June 2026).",
              s=["inv"], neo=[0, ""], src=[["1H 2026 Investors' Briefing", IB], ["2025 Integrated Report", IR]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Owners & leadership", "blurb": "DANIDA 21%, Nsekela CEO.", "div": "crdb", "rev": "treasury", "products": [
            P("owners", "Ownership & listing", "Listed on the Dar es Salaam Stock Exchange since June 2009; DANIDA Investment Fund 21.0%, PSSSF Pension Fund 13.3%, NSSF Uganda 7.9%; 101,340 shareholders (June 2026, up 118%). Market value TZS 6,869 billion at 30 June 2026, after a 229% rise in a year; Moody's B1 deposit rating.",
              s=["inv"], neo=[0, ""], src=[["1H 2026 Investors' Briefing", IB], ["Shareholding, June 2026", SHARE], ["2025 Integrated Report", IR]]),
            P("leadership", "Board & management", "Chairperson Prof. Neema Mori; Group CEO and MD Dr Abdulmajid Nsekela; CFO Fredrick Nshekanabo; CCO Boma Raballa; COO Bruce Mwile; Director of Retail Banking Bonaventure Paulo; Director of ICT Edward Mpina. 4,480 staff (June 2026).",
              s=["inv"], neo=[0, ""], src=[["1H 2026 Investors' Briefing", IB]]),
        ]},
        {"id": "1.3", "ic": "earth", "name": "Heritage & region", "blurb": "Tanzania, Burundi, DR Congo.", "div": "crdb", "rev": "corp", "products": [
            P("heritage", "Heritage", "Incorporated as a limited company in 1996; SME banking and microfinance from 2005; first Tanzanian bank agent network (2013); Islamic banking and bancassurance (2022); insurer and foundation (2023); 20% of the Cooperative Bank of Tanzania (2024).",
              s=["con"], o="I", neo=[0, ""], src=[["2025 Integrated Report", IR], ["CRDB: agency banking", WAKALA]]),
            P("burundi", "CRDB Bank Burundi", "Wholly owned since 2012: 2025 profit TZS 43.7 billion, assets TZS 2.3 trillion, seven branches, 13 ATMs and 3,005 agents; 7.3% of group profit in 1H 2026. Its TemboCard is Visa; shilling-franc cards work only on CRDB and Bi-switch ATMs.", short="Burundi",
              s=["con", "sme"], o="B", ay="2012", neo=[0, "Visa debit."], src=[["2025 Integrated Report", IR], ["1H 2026 Investors' Briefing", IB], ["CRDB Burundi: TemboCard", BITEMBO]]),
            P("drc", "CRDB Bank Congo", "55%-owned bank in its third year: branches in Lubumbashi and Kinshasa, 10,000+ clients and about USD 202 million of assets; broke even in Q1 2026. Launched TemboCard Visa (Classic and Gold) in Kinshasa on 10 April 2026 with Visa's DRC country manager.", short="DR Congo",
              s=["con", "corp"], o="B", st="new", ay="2023", neo=[0, "Visa debit."],
              mc="A new market chose Visa for its first card in April 2026.",
              src=[["CRDB Bank Congo", CDHOME], ["Bankable: TemboCard Visa in DRC, Apr 2026", DRCVISA], ["1H 2026 Investors' Briefing", IB]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Core & card platforms", "blurb": "T24 and BPC SmartVista.", "div": "crdb", "rev": "retail", "products": [
            P("t24", "Temenos T24 core", "Moved from Finastra's Fusion Banking Essence ⚠ to Temenos Transact (T24) in 2025, with 99% uptime; ISO 20022 for cross-border payments; 66% of the TZS 168.2 billion 2026 capex goes to ICT.",
              s=["con", "corp"], st="new", ay="2025", o="P", at="Temenos", neo=[0, ""], src=[["2025 Integrated Report", IR], ["TechCabal: core migration, Sep 2025", TC24]]),
            P("smartvista", "BPC SmartVista card switch", "Card switch and card management moved to BPC SmartVista (June 2025), across Tanzania, Burundi and the DRC: issuing of Visa, Mastercard and UnionPay, corporate, virtual and loyalty cards, and acquiring with cardless cash, ATM forex and dynamic currency conversion.", short="SmartVista",
              s=["con", "sme"], st="new", ay="Jun 2025", o="P", at="BPC", neo=[1, "Issues Mastercard with Visa and UnionPay."],
              src=[["Africa.com: BPC SmartVista, Jun 2025", BPC]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & funding", "blurb": "EVOLVE 2023–2027.", "div": "crdb", "rev": "treasury", "products": [
            P("evolve", "EVOLVE 2023–2027", "Ringfence, grow and futureproof the business; 2026 aims are the retail mass market, MSMEs, core-banking optimisation, subsidiary synergies and channel mix. FY2026 guidance: loans up 18–20%, ROE 28–30%, non-funded income 35–40% of income.",
              s=["inv"], neo=[0, ""], src=[["2025 Integrated Report", IR], ["1H 2026 Investors' Briefing", IB]]),
            P("funding", "Green, Sukuk & DFI funding", "Kijani green bond listed in Luxembourg (July 2025); Al Barakah Sukuk raised TZS 125.4 billion and USD 32.3 million; DFC and Citibank USD 320 million for SMEs; FinDev Canada USD 60 million and DEG USD 50 million (October 2025); SMBC partnership (August 2025).",
              s=["corp", "inv"], st="new", neo=[0, ""], src=[["2025 Integrated Report", IR], ["Intelligent CIO: three partnerships, Oct 2025", DFI], ["CRDB: about us", ABOUT]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: TemboCard debit on Visa, credit cards on Mastercard, UnionPay virtual and prepaid cards, Lipa Hapa acquiring for every network plus TanQR, transfers to wallets and banks over TIPS, and remittance and forex.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "TemboCard, Visa.", "div": "crdb", "rev": "retail", "products": [
            P("tembovisa", "TemboCard Visa debit", "Classic, Gold, Platinum, Infinite and metal debit cards on Visa, with Visa Infinite for the Premier Club; part of 8.9 million registered cards (2025, up 22%). Visa named CRDB for activation in 2025.", short="TemboCard (Visa)",
              s=["con", "prem"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="The big card book, 8.9 million cards, is Visa.",
              src=[["CRDB: TemboCard", CARDS], ["CRDB: TemboCard Visa Infinite", INFINITE], ["CRDB: metal debit card", METAL], ["2025 Integrated Report", IR]]),
            P("fancards", "Simba & Yanga fan cards", "Contactless Visa debit cards for fans of Tanzania's two biggest football clubs, with membership fees bundled in.",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["CRDB: Yanga Visa card", YANGA], ["CRDB: Simba fan card", SIMBA]]),
            P("barakahcard", "Al Barakah TemboCard Visa", "Gold, Platinum and Infinite Visa debit cards for Shariah-compliant accounts.",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["CRDB: TemboCard", CARDS]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Mastercard, TZS 3bn book.", "div": "crdb", "rev": "retail", "products": [
            P("mccredit", "Mastercard World Rewards & Gold credit", "MasterCard World Rewards credit card (up to TZS 50 million, 50 days interest-free) for Premier Plus and MasterCard Gold (up to TZS 20 million) for Premier, launched with Mastercard in February 2018. The credit-card book is only TZS 3.1 billion (2025).", short="Credit (Mastercard)",
              s=["prem"], lc="borrow", ay="Feb 2018", o="P", at="Mastercard", neo=[2, "Mastercard credit."],
              mc="Mastercard's main issuing foothold at CRDB, but a very small book.",
              src=[["CRDB: Premier Banking", PREMIER], ["The Citizen: credit cards, Feb 2018", MCCC2018], ["2025 Integrated Report", IR]]),
            P("newcredit", "Gold & Infinite credit cards", "Current product pages list a Gold credit card (up to TZS 50 million) and an Infinite credit card (up to TZS 500 million, lounges) at 3% a month, also secured on fixed deposits; neither page names a network ⚠.", short="Credit (network ⚠)",
              s=["prem", "sme"], lc="borrow", st="unconf", neo=[None, "Network not stated ⚠."],
              src=[["CRDB: Gold credit card", GOLDCC], ["CRDB: Infinite credit card", INFCC]]),
        ]},
        {"id": "2.3", "ic": "plane", "name": "UnionPay & prepaid", "blurb": "Virtual UPI card in-app.", "div": "crdb", "rev": "retail", "products": [
            P("upi", "Tembo UPI Virtual Card", "A UnionPay virtual card issued instantly in SimBanking for online shopping and subscriptions; TemboCard has worked on UnionPay since a 2013 co-brand ⚠, and UnionPay named CRDB a top issuer in Africa ⚠.", short="UnionPay virtual",
              s=["con"], lc="everyday", o="P", at="UnionPay", neo=[0, "UnionPay."], src=[["CRDB: Tembo UPI virtual card", UPIV], ["The Citizen: UnionPay award", UPIAWARD]]),
            P("prepaid", "TemboCard Prepaid", "A reloadable card without a bank account, for travel, online shopping and gifts; network not stated ⚠.",
              s=["con"], lc="everyday", neo=[None, "Network not stated ⚠."], src=[["CRDB: prepaid cards", PREPAID]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Lipa Hapa acquiring", "blurb": "POS, gateway, TanQR.", "div": "crdb", "rev": "retail", "products": [
            P("pos", "Lipa Hapa POS", "Smart and portable POS terminals taking Visa, Mastercard, Maestro, Cirrus, UnionPay and Amex in TZS and USD, with cash-register integration; 7,748 merchant POS (June 2026).", short="POS (all networks)",
              s=["sme"], lc="move", neo=[1, "Accepts Mastercard with Visa, UnionPay and Amex."], src=[["CRDB: Lipa Hapa", LIPA], ["1H 2026 Investors' Briefing", IB]]),
            P("gateway", "Online payment gateway", "E-commerce acquiring for Visa, Mastercard, UnionPay and Amex with 3-D Secure, recurring billing, pay-by-link and a standard API.", short="Gateway (all networks)",
              s=["sme", "corp"], lc="move", neo=[1, "Accepts Mastercard with Visa, UnionPay and Amex."], src=[["CRDB: Lipa Hapa", LIPA]]),
            P("tanqr", "CRDB TanQR & Lipa Namba", "Merchant QR on the Bank of Tanzania's TanQR standard (2022) and a USSD Lipa Namba, paid from any bank or mobile-money wallet; 315,505 QR and Lipa Hapa merchants (June 2026).", short="TanQR",
              s=["sme"], lc="move", o="P", at="Bank of Tanzania", neo=[0, "TanQR."],
              mc="QR merchants outnumber POS merchants about forty to one.",
              src=[["CRDB: Lipa Hapa", LIPA], ["BoT: TANQR circular, Aug 2022", TANQR], ["1H 2026 Investors' Briefing", IB]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Instant & wallet rails", "blurb": "TIPS, mobile money.", "div": "crdb", "rev": "retail", "products": [
            P("tips", "Transfers to banks & wallets (TIPS)", "SimBanking sends to any bank or to M-Pesa, Mixx and Airtel Money wallets; the Bank of Tanzania's TIPS switch carried about 560 million transactions worth about TZS 41 trillion in FY2024/25, and the BoT capped bank-to-wallet charges in 2025. CRDB earned TZS 177 billion from mobile-phone services in 2025.", short="TIPS & wallets",
              s=["con", "sme"], lc="move", o="P", at="Bank of Tanzania", neo=[0, "National rails."],
              mc="Mobile money and TIPS carry most retail value in Tanzania.",
              src=[["CRDB: SimBanking", SIMB], ["The Citizen: BoT award, Sep 2025", TIPSAWARD], ["2025 Integrated Report", IR]]),
            P("farmerpay", "Digital Farmer Payments", "Payments to farmers into wallets, to raise wallet use, volumes and retention (2Q 2026).",
              s=["farm"], lc="move", st="new", neo=[0, ""], src=[["1H 2026 Investors' Briefing", IB]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Remittance & forex", "blurb": "Western Union, Ria, NALA.", "div": "crdb", "rev": "treasury", "products": [
            P("remit", "Remittance service", "Since 2010, with Western Union, Ria, Upesi and NALA: money from 250+ countries into accounts, other banks or wallets, or as cash at branches; send up to USD 7,500 a transaction.",
              s=["xb"], lc="move", ay="2010", o="P", at="Western Union, Ria, Upesi, NALA", neo=[0, ""],
              mc="Diaspora flows ride money-transfer operators, not card rails.",
              src=[["CRDB: remittance", REMIT]]),
            P("forexatm", "Forex ATMs & FX", "ATMs that change USD, EUR and GBP into shillings against a passport or national ID; FX spot and hedging for businesses; FX income TZS 56 billion in 1H 2026.",
              s=["xb", "corp"], lc="move", neo=[0, ""], src=[["CRDB: forex ATM", FOREXATM], ["1H 2026 Investors' Briefing", IB]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: real-time fraud surveillance and card controls, data, automation and faster credit, partnerships with mobile operators and the stock exchange, and Tembo Points and Visa Infinite benefits.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & card controls", "blurb": "Social-engineering fraud.", "div": "crdb", "rev": "retail", "products": [
            P("fraud", "Fraud & cyber defence", "Real-time transaction surveillance, fraud analytics and PCI DSS certification; the most common frauds in 2025 were impersonation at the counter and social-engineering attacks on SimBanking users.",
              s=["con"], lc="everyday", neo=[0, "CRDB's own."],
              mc="SimBanking fraud is the named problem; scam tools could help.",
              src=[["2025 Integrated Report", IR]]),
            P("cardcontrols", "Card alerts & controls", "SMS alerts for TemboCard, Visa and MasterCard use, card block and unblock in SimBanking, and 3-D Secure on the gateway.", short="Card controls",
              s=["con"], lc="everyday", neo=[1, "Alerts cover Mastercard cards."], src=[["CRDB: SimBanking", SIMB], ["CRDB: Lipa Hapa", LIPA]]),
        ]},
        {"id": "3.2", "ic": "brain", "name": "Data, AI & automation", "blurb": "CreditPro, 10-minute loans.", "div": "crdb", "rev": "retail", "products": [
            P("dataai", "Data, analytics & AI", "A group-wide data architecture, analytics and AI in operations, automated service levels and paperless withdrawals; ISO 20022 for cross-border payments.",
              s=["con", "corp"], neo=[0, "CRDB's own."], src=[["2025 Integrated Report", IR]]),
            P("creditpro", "CreditPro & straight-through lending", "Retail loans moved to the CreditPro platform; loans to public servants cut from three days to ten minutes by straight-through processing (2Q 2026); credit scoring for SIDO loan officers.",
              s=["con", "sme"], lc="borrow", st="new", neo=[0, ""], src=[["1H 2026 Investors' Briefing", IB]]),
        ]},
        {"id": "3.3", "ic": "plug", "name": "Partners & ecosystem", "blurb": "MNOs, fintechs, DSE.", "div": "crdb", "rev": "retail", "products": [
            P("mnolending", "MNO & fintech lending", "Loans and overdrafts with mobile operators and fintechs, such as Songesha and Nivushe, and digital agricultural loans.",
              s=["con", "farm"], lc="borrow", o="P", at="Mobile operators", neo=[0, ""], src=[["2025 Integrated Report", IR]]),
            P("mwanahisa", "Mwanahisa mini-app", "Stock-exchange brokerage inside SimBanking with the Dar es Salaam Stock Exchange; 25,000 new retail investors onboarded in 2025.",
              s=["inv"], lc="grow", st="new", o="P", at="DSE", neo=[0, ""], src=[["2025 Integrated Report", IR]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Loyalty & benefits", "blurb": "Tembo Points, Visa perks.", "div": "crdb", "rev": "retail", "products": [
            P("tembopoints", "Tembo Points", "Points for every charged SimBanking transaction and for referrals, redeemable for transfers, fees, cash-back and discounts.",
              s=["con"], lc="grow", neo=[0, "CRDB's own."], src=[["CRDB: Tembo Points", TEMBOPTS]]),
            P("visaperks", "Visa Infinite benefits", "Concierge, airport lounges, airport speed pass, travel insurance and purchase protection for TemboCard Visa Infinite holders.",
              s=["prem"], lc="grow", o="P", at="Visa", neo=[0, "Visa."], src=[["CRDB: TemboCard Visa Infinite", INFINITE]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: accounts, salary loans and mortgages for 7.95 million people and Premier banking for the affluent, MSME and farm credit, corporate, trade and DFI-funded lending, treasury and government securities, and Islamic banking and insurance.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Retail & Premier", "blurb": "53% of loans.", "div": "crdb", "rev": "retail", "products": [
            P("accounts", "Retail accounts & loans", "Accounts for women (Malkia), children, students, pensioners and the diaspora (Tanzanite); salary, personal and Kopa Kimpango Wako loans for civil servants (up to TZS 300 million); Jijenge mortgages up to TZS 1 billion. Retail is 53% of loans; Retail Banking earned TZS 187.2 billion before tax in 2025.",
              s=["con", "xb"], lc="borrow", neo=[0, ""], src=[["1H 2026 Investors' Briefing", IB], ["2025 Integrated Report", IR]]),
            P("premier", "Premier Banking", "Relationship managers and Premier lounges; Premier Plus customers get a Visa Infinite debit card and a MasterCard World Rewards credit card, Premier customers a Visa Platinum and a MasterCard Gold credit card.", short="Premier",
              s=["prem"], lc="everyday", neo=[1, "Mastercard credit beside Visa debit."], src=[["CRDB: Premier Banking", PREMIER]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "MSME & agribusiness", "blurb": "Farm finance, TACATDP.", "div": "crdb", "rev": "retail", "products": [
            P("msme", "MSME banking", "Biashara and Hodari accounts, SME and micro loans, asset finance, purchase-order and invoice discounting, and the Malkia women's proposition, backed by DFI lines such as DFC and Citibank's USD 320 million.",
              s=["sme"], lc="borrow", neo=[0, ""],
              mc="No business card is offered; NMB launched Mastercard SME cards in 2025–26 ⚠.",
              src=[["2025 Integrated Report", IR], ["Nation: NMB and Mastercard SME card", NMBMC]]),
            P("agri", "Agribusiness & TACATDP", "Seasonal and value-chain finance for farmers and cooperatives; agriculture is roughly a quarter of loans (June 2026); the climate-adaptation programme TACATDP has reached 632,000 beneficiaries.",
              s=["farm"], lc="borrow", neo=[0, ""], src=[["1H 2026 Investors' Briefing", IB], ["2025 Integrated Report", IR]]),
        ]},
        {"id": "4.3", "ic": "factory", "name": "Corporate & trade", "blurb": "TZS 507bn pre-tax.", "div": "crdb", "rev": "corp", "products": [
            P("corporate", "Corporate & trade banking", "Working capital, project finance, syndications, trade finance (TZS 36.8 billion of letter-of-credit commission in 2025) and India and China desks; Corporate Banking earned TZS 507.4 billion before tax in 2025.",
              s=["corp"], lc="borrow", neo=[0, ""],
              mc="The most profitable segment has no commercial-card offer in public.",
              src=[["2025 Integrated Report", IR]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Treasury & capital markets", "blurb": "TZS 4.2tn securities.", "div": "crdb", "rev": "treasury", "products": [
            P("treasury", "Treasury & capital markets", "Government securities of TZS 4.2 trillion (June 2026), FX, custody and bond arranging such as the Samia Infrastructure Bond; Treasury earned TZS 335.9 billion before tax in 2025.",
              s=["corp", "inv"], lc="grow", neo=[0, ""], src=[["1H 2026 Investors' Briefing", IB], ["2025 Integrated Report", IR]]),
        ]},
        {"id": "4.5", "ic": "building-2", "name": "Al Barakah & insurance", "blurb": "Islamic banking, CIC.", "div": "barakah", "rev": "ins", "products": [
            P("barakah", "Al Barakah Banking", "Shariah-compliant accounts, financing (TZS 240.3 billion, up 61% in 2025) and Sukuk; assets TZS 338.8 billion.",
              s=["con", "sme"], lc="grow", st="new", ay="2022", neo=[0, ""], src=[["2025 Integrated Report", IR]]),
            P("insurance", "CRDB Insurance & bancassurance", "CRDB Insurance Company (wholly owned) and bancassurance for motor, medical, life and property; Smart Mifugo livestock insurance (2Q 2026); insurer profit TZS 4.5 billion in 1H 2026.",
              s=["con", "farm"], lc="beyond", st="new", neo=[0, ""], src=[["1H 2026 Investors' Briefing", IB], ["2025 Integrated Report", IR]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: SimBanking for 2.9 million registered accounts, 243 branches and 736 ATMs, 38,449 CRDB Wakala agents, internet banking, and a representative office in Dubai.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "SimBanking", "blurb": "99m transactions in 2025.", "div": "crdb", "rev": "retail", "products": [
            P("simbanking", "SimBanking app & USSD", "App and *150*03#: 2.93 million registered accounts and 99.3 million transactions in 2025 (up 43%); transfers, bills, wallets, loans, virtual UnionPay cards and Visa Infinite applications; launched in Burundi and the DRC in 2025; Global Finance's best mobile banking app in Africa.",
              s=["con", "sme"], lc="everyday", neo=[0, "CRDB's own."],
              mc="No tokenised Mastercard in the app; the only in-app virtual card is UnionPay.",
              src=[["CRDB: SimBanking", SIMB], ["2025 Integrated Report", IR]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "243 branches, 736 ATMs.", "div": "crdb", "rev": "retail", "products": [
            P("branches", "Branches, ATMs & mobile branches", "243 branch outlets, 10 mobile branches and 736 ATMs (June 2026), plus cash-deposit machines; ATM transactions fell 9% in 2025 as use moved to mobile and agents.",
              s=["con", "xb"], lc="everyday", neo=[None, "Mastercard acceptance at ATMs not stated."], src=[["1H 2026 Investors' Briefing", IB], ["2025 Integrated Report", IR]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "CRDB Wakala agents", "blurb": "38,449 agents.", "div": "crdb", "rev": "retail", "products": [
            P("wakala", "CRDB Wakala", "The first bank agent network in Tanzania (2013), now 38,449 agents (June 2026), with 99.3 million transactions in 2025: deposits, card and cardless withdrawals, bills, government payments and account opening.",
              s=["con", "farm"], lc="open", neo=[0, ""], src=[["CRDB: agency banking", WAKALA], ["1H 2026 Investors' Briefing", IB], ["2025 Integrated Report", IR]]),
            P("agenttoken", "Agent tokens", "Since October 2025, recipients can withdraw cash at agents with a one-time token, without a bank account.",
              s=["con", "xb"], lc="move", st="new", ay="Oct 2025", neo=[0, "CRDB's own."], src=[["2025 Integrated Report", IR]]),
        ]},
        {"id": "5.4", "ic": "monitor", "name": "Online & Dubai", "blurb": "Internet banking, DIFC.", "div": "dubai", "rev": "corp", "products": [
            P("ib", "Internet banking", "Personal and business internet banking: 98,861 registered customers and 9.8 million transactions in 2025; self-service registration from 2Q 2026; a merchant portal for Lipa Hapa.",
              s=["sme", "corp"], lc="everyday", neo=[0, ""], src=[["2025 Integrated Report", IR], ["1H 2026 Investors' Briefing", IB]]),
            P("dubaioffice", "Dubai representative office", "A DFSA-regulated DIFC office, licensed in 2025 and opened in January 2026, marketing the group's trade, treasury, capital-markets and personal banking along the Gulf–East Africa corridor.", short="Dubai office",
              s=["corp", "xb"], lc="beyond", st="new", ay="Jan 2026", neo=[0, ""],
              mc="Gulf–East Africa trade and diaspora flows run through here.",
              src=[["CRDB: Dubai", DUBAI], ["1H 2026 Investors' Briefing", IB]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at CRDB", "blurb": "Credit cards and acceptance; debit is Visa.", "products": [
        P("mcatcrdb", "Mastercard at CRDB", "CRDB's debit cards in Tanzania, Burundi and the DRC are Visa, with UnionPay second. Mastercard has the World Rewards and Gold credit cards launched in 2018 (a TZS 3.1 billion book), acceptance on Lipa Hapa POS and gateway, and issuing on the BPC SmartVista switch. A TemboCard MasterCard debit dates from 2011 ⚠. Fees from Visa and Mastercard were TZS 13.5 billion in 2025 and commission paid to them TZS 15.2 billion, not split by network.",
          s=["con"], div="crdb", rev="retail", mc="The relationship this map is drawn for.",
          src=[["CRDB: Premier Banking", PREMIER], ["The Citizen: credit cards, Feb 2018", MCCC2018], ["CRDB: Lipa Hapa", LIPA], ["Africa.com: BPC SmartVista, Jun 2025", BPC], ["2025 Integrated Report", IR], ["The Citizen: Visa campaign, Dec 2021", VISA2021]]),
    ]},
    {"id": "pillar-market", "name": "Tanzanian payments", "blurb": "Mobile money, TIPS and TanQR.", "products": [
        P("market", "The Tanzanian market", "87.05 million mobile-money subscriptions at June 2026 (M-Pesa 40.6%, Mixx by Yas 32.0%, Airtel Money 16.4%) and 2.1 billion transactions in the quarter; the Bank of Tanzania's TIPS switch joins banks and wallets, and TanQR (2022) makes one QR work for both; digital fees are capped. CRDB holds about 29% of banking assets; NMB is its main rival and launched Mastercard SME cards ⚠.",
          s=["con"], div="crdb", rev="retail", src=[["TanzaniaInvest: TCRA Q2 2026", TCRA], ["The Citizen: BoT award, Sep 2025", TIPSAWARD], ["BoT: TANQR circular, Aug 2022", TANQR], ["2025 Integrated Report", IR], ["Nation: NMB and Mastercard SME card", NMBMC]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
