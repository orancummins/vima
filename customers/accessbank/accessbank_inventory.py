"""Access Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Access Bank Plc's own unless a source says otherwise: the 2025 annual report (June 2026) and the
unaudited Q1 2026 results (27 April 2026), with Access Holdings Plc as the listed parent. H1 2026 audited results
had not been found by 17 October 2026. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own
product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

PROFILE = "https://www.accessbankplc.com/about-us/corporate-profile"
BOARD = "https://www.accessbankplc.com/about-us/board-management-team"
BUSINESSES = "https://www.accessbankplc.com/about-us/our-businesses"
AR25 = "https://www.accessbankplc.com/access/media/Financial-Report/Annual%20Reports/2025-Annual-Report.pdf?ext=.pdf"
Q1FS = "https://www.accessbankplc.com/access/media/documents/Abridged-FS-Q1-2026.pdf"
HQ1 = "https://nairametrics.com/2026/05/02/access-holding-reports-n272-billion-profit-in-q1-2026-up-22/"
H1DELAY = "https://nairametrics.com/2026/08/18/access-holdings-delays-h1-audited-results-to-september-30-over-cbn-approval/"
GEO = "https://www.ecofinagency.com/news/0505-55272-access-holdings-africa-pivot-eclipses-nigeria-as-dr-congo-profit-doubles-in-2026"
LEAD = "https://nairametrics.com/2026/06/25/access-holdings-announces-retirement-of-executive-directorbolaji-agbede/"
RIGHTS = "https://www.accessbankplc.com/media/news/access-holdings-plc-secures-full-regulatory-approvals-of-its-recently-closed-rights-issue-of-ordina"
BIDVEST = "https://www.accessbankplc.com/media/news/access-bank-plc-signs-agreement-to-acquire-100-equity-stake-in-south-african-based-bidvest-bank-dc20967416c8c0b0ba5f5a4de56ccc4f"
SCB = "https://www.accessbankplc.com/media/news/access-bank-plc-(access)-enters-into-acquisition-agreements-with-standard-chartered-bank"
NBK = "https://www.accessbankplc.com/media/news/proposed-acquisition-of-national-bank-of-kenya-limited-by-access-bank-plc"
HK = "https://www.accessbankplc.com/media/news/access-bank-uk-expands-footprint-with-new-hong-kong-branch"
MALTA = "https://www.accessbankplc.com/media/news/the-access-bank-uk-limited-expands-international-presence-with-launch-of-the-access-bank-malta-limit"
EUROMONEY = "https://www.accessbankplc.com/media/news/access-bank-earns-16-euromoney-honours-as-strategy,-innovation-and-impact-deliver-global-recognition"
CARDS = "https://www.accessbankplc.com/ways-to-bank/cards"
AMEX = "https://www.accessbankplc.com/amex"
AMEXREW = "https://www.accessbankplc.com/ways-to-bank/amex-rewards"
AMEXLAUNCH = "https://www.accessbankplc.com/media/news/access-bank-launches-the-first-american-express%C2%AE-cards-to-be-issued-in-nigeria"
BLACK = "https://www.accessbankplc.com/private/black-card"
SIGNATURE = "https://www.accessbankplc.com/ways-to-bank/cards/visa-signature-card"
VIRTUAL = "https://www.accessbankplc.com/ways-to-bank/cards/virtual-card"
CARDXPRESS = "https://www.accessbankplc.com/ways-to-bank/cards/cardxpress"
DTS = "https://www.accessbankplc.com/ways-to-bank/cards/access-bank-dual-transaction-service-(dts)"
VISACORP = "https://msmeafricaonline.com/?p=61470"
VISASME = "https://brandspurng.com/2020/12/11/visa-partners-access-bank-to-launch-business-debit-card-for-smes/"
MOVE = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2024/may/access-bank-group-and-mastercard-join-forces-to-expand-opportunities-for-cross-border-payments-for-african-businesses-and-consumers/"
MOVEFT = "https://fintech.global/2024/05/10/access-bank-group-and-mastercard-unite-to-revolutionise-cross-border-payments-in-africaaccess-bank-group-and-mastercard-unite-to-revolutionise-cross-border-payments-in-africa/"
GHANA = "https://www.ghana.accessbankplc.com/media/news/mastercard-and-access-bank-introduce-innovative-card-to-empower-ghanaians"
AFRIGO = "https://nibss-plc.com.ng/access-bank-partners-with-afrigopay-to-boost-payment-ecosystem/"
AFRIGO3 = "https://nibss-plc.com.ng/insight-three-years-later-how-is-cbns-afrigo-doing/"
NIBSS = "https://nibss-plc.com.ng/nigerias-digital-payments-surge-to-n1-07-quadrillion-as-nibss-defines-future/"
NIPQ1 = "https://www.thisdaylive.com/2025/07/29/e-payment-transactions-rise-17-7-to-n284-99-trillion-in-q1-2025/"
VERVE70 = "https://interswitchgroup.com/news/verve-hits-70-million-payment-cards-in-nigeria-consolidates-market"
VERVE100 = "https://techcabal.com/2025/12/01/verve-hits-100-million-card-issuance/"
HYDROGEN = "https://thecable.ng/access-holdings-gets-cbns-nod-for-its-payment-business"
HYDROGEN25 = "https://techcabal.com/2025/10/28/accesss-hydrogen-grows-profit-305-as-transactions-hit-%E2%82%A641-1-trillion/"
FITCH = "https://dmarketforces.com/fitch-affirms-access-bank-at-b-with-stable-outlook/"
ZENITH = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2025-1/november/mastercard-and-zenith-bank-launch-essential-debit-card-to-expand-access-to-affordable-digital-payments-in-nigeria/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · capital · group", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Nigeria's largest bank by assets, N51 trillion at the end of 2025, recapitalised first under the CBN's new rules, led by Roosevelt Ogbonna under Access Holdings, and moving 'from scale to value'.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & capital", "blurb": "N51.3trn assets, PBT N954bn.", "div": "abg", "rev": "retail", "products": [
            P("balance", "Balance sheet & earnings (2025)", "Total assets N51.27 trillion (+25.5%), customer deposits N34.56 trillion (+53.4%), gross loans N16.23 trillion and profit before tax N954.2 billion (+6.8%) in 2025; net fee income up 41.5% to N537.9 billion. Businesses outside Nigeria made 52% of group profit.",
              s=["corp"], neo=[0, ""], src=[["Access Bank 2025 annual report", AR25], ["Ecofin: 2025 results by geography", GEO]]),
            P("q1", "Q1 2026 results", "Banking-group profit before tax of N253.6 billion in Q1 2026 (N227.2 billion a year earlier) on assets of N53.1 trillion; Access Holdings made N272.2 billion. H1 2026 audited results were delayed pending CBN approval ⚠ not found by 17 October 2026.",
              s=["corp"], st="new", neo=[0, ""], src=[["Access Bank Q1 2026 results", Q1FS], ["Nairametrics: Access Holdings Q1 2026", HQ1], ["Nairametrics: H1 results delayed, Aug 2026", H1DELAY]]),
            P("capital", "Capital & ratings", "A fully digital N351 billion rights issue (December 2024 ⚠) lifted share capital to N600 billion, first to meet the CBN's N500 billion minimum for international banks; Fitch rates the bank 'B', Stable (May 2026). Access Holdings is worth about N1.46 trillion (August 2026).",
              s=["corp"], ay="Dec 2024", neo=[0, ""], src=[["Access: rights issue approvals", RIGHTS], ["MarketForces: Fitch affirms Access, May 2026", FITCH], ["Nairametrics: H1 results delayed, Aug 2026", H1DELAY]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Ogbonna; Ike at the holding company.", "div": "holdings", "rev": "retail", "products": [
            P("leadership", "Board & executives", "Access Bank: chair Ifeyinwa Osime, MD/CEO Roosevelt Ogbonna (since May 2022), executive directors Hadiza Ambursa, Seyi Kumapayi, Iyabo Soji-Okusanya and Ifedayo Orimoloye. Access Holdings: chairman Aigboje Aig-Imoukhuede and Group CEO Innocent Ike (from 29 August 2025), after Herbert Wigwe's death in February 2024.",
              s=["corp"], neo=[0, ""], src=[["Access: board and management", BOARD], ["Nairametrics: Access Holdings leadership, Jun 2026", LEAD]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology & innovation", "blurb": "Project Everest core.", "div": "abg", "rev": "retail", "products": [
            P("tech", "Project Everest", "A core upgrade to FLEXCUBE v14.7 with zero-trust security and active/active Tier 3 data centres, alongside digital onboarding and automation across retail.",
              s=["con"], st="new", neo=[0, ""], src=[["Access Bank 2025 annual report", AR25]]),
            P("foundry", "Africa Fintech Foundry", "The bank's fintech and innovation arm: accelerators for 131 sustainability start-ups, a space-tech programme with NIGCOMSAT, and incubated products such as the DASH car-pooling app (2025).",
              s=["sme"], o="B", neo=[0, ""], src=[["Access Bank 2025 annual report", AR25]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & deals", "blurb": "From scale to value.", "div": "holdings", "rev": "intl", "products": [
            P("strategy", "From scale to value", "Five priorities for the next phase: earnings quality, capital efficiency, a technology-led bank, 'scaling trade and payments leadership' and governance. Retail targets 5 million new customers in 2026.",
              s=["corp"], st="new", neo=[0, ""], src=[["Access Bank 2025 annual report", AR25], ["Access: 16 Euromoney awards, Jul 2026", EUROMONEY]]),
            P("deals", "Acquisitions", "Standard Chartered's banks in Angola, Sierra Leone, The Gambia, Cameroon and Tanzania consumer (agreed July 2023), National Bank of Kenya (2024), 76% of AfrAsia Bank, Mauritius (July 2025); the Bidvest Bank deal lapsed in January 2026.",
              s=["corp"], o="A", st="flux", neo=[0, ""], src=[["Access: Standard Chartered deal, Jul 2023", SCB], ["Access: National Bank of Kenya", NBK], ["Access: Bidvest long-stop expired", BIDVEST], ["Access Bank 2025 annual report", AR25]]),
            P("groupcos", "Access Holdings companies", "Beside the bank: Hydrogen Payment Services, Access ARM Pensions, Access Insurance Brokers and Oxygen X Finance, with more than 31,000 staff across the group.",
              s=["con"], neo=[0, ""], src=[["Access Bank 2025 annual report", AR25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: debit on Visa, Mastercard and Verve, the domestic AfriGO card, credit on Visa and Amex, prepaid and virtual cards, POS and Hydrogen processing, NIBSS instant transfers, and Access Africa cross-border payments on Mastercard Move.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "Visa first, Mastercard too.", "div": "access", "rev": "retail", "products": [
            P("visadebit", "Visa debit cards", "Naira debit in Classic, Privilege, Platinum and Signature tiers, plus a Visa Business Debit card for SMEs (December 2020); Visa Signature adds lounge access and concierge.", short="Debit (Visa)",
              s=["con", "sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Access: cards", CARDS], ["Access: Visa Signature", SIGNATURE], ["BrandSpur: Visa business debit, Dec 2020", VISASME]]),
            P("mcdebit", "Mastercard debit cards", "A naira Mastercard Debit card sits alongside Visa and Verve, with the same N2 million daily POS limit; the bank won a Mastercard Franchise Award (EDGE 2025). Share of the base not disclosed ⚠.", short="Debit (Mastercard)",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's main card foothold in the Nigerian bank.",
              src=[["Access: cards", CARDS], ["Access Bank 2025 annual report", AR25]]),
        ]},
        {"id": "2.2", "ic": "flag", "name": "Domestic schemes", "blurb": "Verve and AfriGO.", "div": "access", "rev": "retail", "products": [
            P("verve", "Verve cards", "Debit and prepaid cards on Interswitch's Verve, usable only in Nigeria; Verve passed 70 million cards in Nigeria in October 2024 and 100 million across Africa in December 2025.", short="Verve",
              s=["con"], lc="everyday", o="P", at="Interswitch", neo=[0, "Verve."],
              mc="The domestic scheme that competes for every low-cost debit card.",
              src=[["Access: cards", CARDS], ["Interswitch: Verve 70 million", VERVE70], ["TechCabal: Verve 100 million, Dec 2025", VERVE100]]),
            P("afrigo", "AfriGO", "Access issued the first live card on the CBN and NIBSS national scheme, with POS and ATM purchases from 14 March 2023; AfriGO had more than a million cards and N70 billion of transactions by September 2025.", short="AfriGO",
              s=["con"], lc="everyday", ay="Mar 2023", o="P", at="AfriGO (NIBSS)", neo=[0, "AfriGO."],
              src=[["NIBSS: Access and AfriGO, Mar 2023", AFRIGO], ["NIBSS: AfriGO three years on", AFRIGO3], ["Access: CardXpress", CARDXPRESS]]),
        ]},
        {"id": "2.3", "ic": "credit-card", "name": "Credit cards", "blurb": "Visa and Amex.", "div": "access", "rev": "retail", "products": [
            P("visacredit", "Visa credit cards", "All credit cards are Visa: naira and USD dual-currency cards from Classic to Infinite, with up to 40 days interest-free and limits up to $50,000.", short="Credit (Visa)",
              s=["con", "hnw"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Access: cards", CARDS]]),
            P("amex", "American Express Gold & Platinum", "The first Amex cards issued in Nigeria and West Africa (June 2023): Gold ($75 a year) and metal Platinum ($250), dual currency, with Membership Rewards and local partners; Access has acquired Amex since 2019.", short="Amex",
              s=["hnw"], lc="borrow", ay="Jun 2023", o="P", at="American Express", neo=[0, "American Express."],
              src=[["Access: first Amex cards, 2023", AMEXLAUNCH], ["Access: Amex cards", AMEX], ["Access: Amex Rewards", AMEXREW]]),
            P("visacorp", "Access Visa Corporate Credit Card", "Launched January 2026 for medium and large companies: up to 45 days interest-free and Visa Spend Clarity reporting by employee, branch and department.", short="Corporate card (Visa)",
              s=["corp"], lc="borrow", st="new", ay="Jan 2026", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa took the newest commercial card programme.",
              src=[["MSME Africa: Access Visa Corporate card, Jan 2026", VISACORP]]),
            P("dts", "Dual Transaction Service", "A virtual naira credit line on an existing debit card for pre-approved customers, switched on by USSD *901*14# or AccessMore and used by choosing 'Credit' at ATM or POS.",
              s=["con"], lc="borrow", neo=[None, "Follows the debit card's network ⚠."], src=[["Access: DTS", DTS]]),
        ]},
        {"id": "2.4", "ic": "wallet", "name": "Prepaid & virtual", "blurb": "Three schemes, four currencies.", "div": "more", "rev": "retail", "products": [
            P("prepaid", "Prepaid cards", "Reloadable cards for payroll, allowances and student IDs: Visa in naira, pounds, dollars and euros, Mastercard in naira (usable abroad) and Verve for Nigeria, with co-branding on all three.",
              s=["con", "corp"], lc="everyday", o="P", at="Visa, Mastercard, Verve", neo=[1, "Visa, Mastercard and Verve."], src=[["Access: cards", CARDS]]),
            P("virtual", "Virtual cards", "Prepaid virtual cards created in AccessMore in under a minute, in naira (domestic only) and dollars, pounds and euros (abroad only), with up to five gift cards per customer. Network not stated ⚠.",
              s=["con", "diaspora"], lc="everyday", neo=[None, "Network not stated."],
              mc="Multi-currency virtual cards are a natural fit for tokenised Mastercard credentials.",
              src=[["Access: virtual card", VIRTUAL]]),
            P("cobrand", "Co-branded merchant credit card", "A fully digital co-branded credit card platform for retailers, first rolled out at Fouani's stores in 2025, built for other merchants and West Africa. Network not stated ⚠.",
              s=["con"], lc="borrow", st="new", ay="2025", o="P", at="Fouani", neo=[None, "Network not stated."], src=[["Access Bank 2025 annual report", AR25]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance & processing", "blurb": "POS and Hydrogen.", "div": "holdings", "rev": "commercial", "products": [
            P("pos", "POS & merchant acquiring", "POS terminals for SMEs, Amex acceptance since 2019, cardholder discounts at Access POS merchants, and AccessPing alerts for merchants.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["Access Bank 2025 annual report", AR25], ["Access: cards", CARDS], ["Access: first Amex cards, 2023", AMEXLAUNCH]]),
            P("hydrogen", "Hydrogen Payment Services", "Access Holdings' switching and processing company (CBN approval 2022): POS, the HydrogenPay gateway and third-party card processing; transaction value of N41.1 trillion in H1 2025 ⚠ secondary.", short="Hydrogen",
              s=["sme", "corp"], lc="move", o="B", neo=[None, "Scheme mix not disclosed."], src=[["The Cable: Hydrogen approval", HYDROGEN], ["TechCabal: Hydrogen H1 2025", HYDROGEN25]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Instant transfers", "blurb": "NIBSS NIP.", "div": "access", "rev": "retail", "products": [
            P("nip", "Transfers on NIBSS Instant Payments", "App, USSD, internet-banking and agent transfers settle on NIBSS NIP ⚠ inferred; NIP carried 11.2 billion transfers a year and about N285 trillion in Q1 2025 alone.", short="NIP transfers",
              s=["con", "sme"], lc="move", o="P", at="NIBSS", neo=[0, "NIBSS rails."],
              mc="Account-to-account transfers, not cards, carry most Nigerian payments.",
              src=[["NIBSS: digital payments, Jul 2026", NIBSS], ["ThisDay: e-payments Q1 2025", NIPQ1]]),
        ]},
        {"id": "2.7", "ic": "earth", "name": "Cross-border", "blurb": "Access Africa on Mastercard Move.", "div": "subs", "rev": "africa", "products": [
            P("accessafrica", "Access Africa with Mastercard Move", "Since May 2024 customers in Access Bank Group's African markets send and receive money to and from more than 150 countries through accounts, wallets, cards and cash, on Mastercard Move, integrated by Fable Fintech.", short="Access Africa (Move)",
              s=["corp", "diaspora", "sme"], lc="move", ay="May 2024", o="P", at="Mastercard", neo=[3, "Mastercard Move."],
              mc="Mastercard's deepest product in the group; cross-border is a 2026 priority.",
              src=[["Mastercard: Access Bank Group and Mastercard, May 2024", MOVE], ["FinTech Global: Access and Mastercard, May 2024", MOVEFT], ["Access Bank 2025 annual report", AR25]]),
            P("diaspora", "Diaspora banking", "Remote account opening for Nigerians abroad (NRBVN), a diaspora community hub and diaspora mortgages for customers in the US, UK and Canada (2025).",
              s=["diaspora"], lc="open", st="new", neo=[0, ""], src=[["Access Bank 2025 annual report", AR25]]),
            P("stablecoin", "Stablecoin trials", "Blockchain experiments focused on stablecoins with partners, under the regulatory framework, for domestic and cross-border payments, SME transactions and clearing (planned 2026).",
              s=["corp"], lc="move", st="unconf", neo=[None, "Partners not named."], src=[["Access Bank 2025 annual report", AR25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud controls against USSD and transfer fraud and digital KYC, AI merchant alerts, wallet and escrow APIs for fintechs, and rewards led by Amex and Visa benefits.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "N1.24bn lost in 2025.", "div": "access", "rev": "retail", "products": [
            P("fraud", "Fraud controls", "Fraud losses of N1.24 billion in 2025 (N1.69 billion in 2024), with 5,931 successful electronic and USSD frauds the largest category; Verified by Visa protects card payments online.",
              s=["con"], lc="everyday", o="B", neo=[0, "Access's own; Visa on cards."],
              mc="High electronic-fraud counts on transfer channels point to scam and identity tools.",
              src=[["Access Bank 2025 annual report", AR25], ["Access: cards", CARDS]]),
            P("kyc", "Digital onboarding & KYC", "Fully digital account opening in AccessMore with digital KYC and facial authentication (2025), with digital address checks next.",
              s=["con", "diaspora"], lc="open", st="new", o="B", neo=[0, ""], src=[["Access Bank 2025 annual report", AR25]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & data", "blurb": "AccessPing.", "div": "access", "rev": "retail", "products": [
            P("accessping", "AccessPing", "An AI-powered service that sends merchants instant, verified payment alerts on WhatsApp, cutting disputes and driving virtual-account use.",
              s=["sme"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["Access Bank 2025 annual report", AR25]]),
            P("aidata", "AI in credit & service", "AI in credit management, customer experience and operations, with a suite of AI tools for retail, SME and merchant banking to come, and data models for segmentation.",
              s=["con"], lc="everyday", st="new", neo=[0, ""], src=[["Access Bank 2025 annual report", AR25]]),
        ]},
        {"id": "3.3", "ic": "code-xml", "name": "APIs & embedded finance", "blurb": "Wallets, escrow, funds.", "div": "access", "rev": "commercial", "products": [
            P("waas", "Wallet-as-a-Service, escrow & Bank-to-Fund", "API wallets backed by core accounts for fintechs and marketplaces (in design), an escrow platform piloted in 2025, and an API link selling Coronation Asset Management funds through Access channels.",
              s=["sme", "corp"], lc="beyond", st="new", o="B", neo=[0, ""], src=[["Access Bank 2025 annual report", AR25]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards", "blurb": "Amex and Visa benefits.", "div": "access", "rev": "retail", "products": [
            P("rewards", "Rewards & card benefits", "Amex Membership Rewards and local partners (private jets, visas, luxury goods), Visa Signature lounge and hotel benefits, discounts at Access POS merchants, and AccessRewards+ in delivery.",
              s=["con", "hnw"], lc="grow", neo=[0, "Visa and Amex; no Mastercard programme found."],
              mc="AccessRewards+ is being built; card-linked offers could feed it.",
              src=[["Access: Amex Rewards", AMEXREW], ["Access: Visa Signature", SIGNATURE], ["Access Bank 2025 annual report", AR25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: QuickBucks loans and the W women's proposition, 7.5 million small businesses, corporate and transaction banking, a private bank, and banks in the UK, Mauritius and across Africa.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Retail & lending", "blurb": "QuickBucks, W, mortgages.", "div": "access", "rev": "retail", "products": [
            P("quickbucks", "QuickBucks & consumer loans", "Digital nano, micro, salary and payday loans, with QuickBucks 3.0 and a new loan engine planned for 2026; auto and personal loans alongside.",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["Access Bank 2025 annual report", AR25]]),
            P("women", "W women's banking", "695,000 women customers added and 347,255 women and women-led SMEs lent more than N78.3 billion; over 1.2 million cards issued in 2025 ⚠ network not stated.",
              s=["women"], lc="everyday", neo=[None, "Cards issued; network not stated."], src=[["Access Bank 2025 annual report", AR25]]),
            P("mortgages", "Mortgages", "A N52 billion mortgage book using the MREIF scheme's single-digit, long-tenor loans, plus equity release and diaspora mortgages.",
              s=["con", "diaspora"], lc="borrow", neo=[0, ""], src=[["Access Bank 2025 annual report", AR25]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "SME banking", "blurb": "7.5 million MSMEs.", "div": "access", "rev": "retail", "products": [
            P("sme", "SME banking", "More than 7.5 million MSME customers with POS, AccessMore and PrimusPlus tools, pre-approved loans from September 2025 (more than N35 billion in four months) and a Visa business debit card.",
              s=["sme", "women"], lc="borrow", neo=[1, "Visa business debit; POS takes all cards."],
              mc="SME cards beyond Visa debit are open ground.",
              src=[["Access Bank 2025 annual report", AR25], ["BrandSpur: Visa business debit, Dec 2020", VISASME]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Corporate & commercial", "blurb": "Trade, treasury, transactions.", "div": "access", "rev": "cib", "products": [
            P("cib", "Corporate & Investment Banking", "Treasury, financial markets, global transaction services, project finance and sector groups for large corporates and institutions, with the Access Africa platform for intra-African trade.",
              s=["corp"], lc="move", neo=[0, ""], src=[["Access Bank 2025 annual report", AR25]]),
            P("commercial", "Commercial Banking", "Companies with turnover above N1 billion, and federal, state and local government.",
              s=["corp"], lc="everyday", neo=[0, ""], src=[["Access: our businesses", BUSINESSES]]),
        ]},
        {"id": "4.4", "ic": "gem", "name": "Private banking", "blurb": "Black Card on Visa Infinite.", "div": "private", "rev": "retail", "products": [
            P("private", "Access Private Bank", "Private bankers, investment management and the invitation-only Black Card on Visa Infinite, alongside the Amex Platinum card.",
              s=["hnw"], lc="grow", neo=[0, "Visa Infinite and Amex."], src=[["Access: Black Card", BLACK], ["Access: Amex cards", AMEX]]),
        ]},
        {"id": "4.5", "ic": "globe", "name": "International", "blurb": "UK, Mauritius, Malta, Hong Kong.", "div": "uk", "rev": "intl", "products": [
            P("ukbank", "The Access Bank UK", "Trade finance and commercial banking from London, with branches in Dubai and Paris, a Hong Kong branch (November 2024) and The Access Bank Malta; international made 26% of group profit in 2025.",
              s=["corp"], lc="move", neo=[0, ""], src=[["Access: Hong Kong branch, Nov 2024", HK], ["Access: Access Bank Malta", MALTA], ["Access Bank 2025 annual report", AR25]]),
            P("afrasia", "AfrAsia Bank, Mauritius", "76% bought by The Access Bank UK on 22 July 2025, adding an international financial centre bank. Card networks not researched ⚠.",
              s=["corp", "hnw"], lc="grow", st="new", ay="Jul 2025", o="A", neo=[None, "Not researched."], src=[["Access Bank 2025 annual report", AR25]]),
        ]},
        {"id": "4.6", "ic": "earth", "name": "African subsidiaries", "blurb": "Banks in 16 more countries.", "div": "subs", "rev": "africa", "products": [
            P("subsidiaries", "Banks across Africa", "Banks in Ghana, Kenya (with National Bank of Kenya), Zambia, DR Congo, Angola, South Africa, Botswana, Mozambique, Rwanda, Tanzania, Sierra Leone, The Gambia, Cameroon and Guinea; the rest of Africa made 26% of group profit in 2025.",
              s=["con", "corp"], lc="everyday", o="A", neo=[1, "Mastercard in Ghana; other markets not researched ⚠."], src=[["Access Bank 2025 annual report", AR25], ["Ecofin: 2025 results by geography", GEO]]),
            P("accessu", "AccessU youth cards (Ghana)", "Age-staged Mastercard cards for Ghanaians aged 13 to 40 (July 2025): prepaid for teens with parental controls, debit plus entry credit and buy-now-pay-later for young professionals, and premium and SME cards; a women's version planned.", short="AccessU (Mastercard)",
              s=["con", "women"], lc="everyday", st="new", ay="Jul 2025", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="A Mastercard proposition that could travel to Nigeria and the other subsidiaries.",
              src=[["Access Bank Ghana: AccessU with Mastercard, Jul 2025", GHANA]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: AccessMore for 8.4 million users, USSD and business banking channels, about 680 Nigerian branches, and 750,000 Access Closa agents.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "AccessMore", "blurb": "8.4 million users.", "div": "more", "rev": "retail", "products": [
            P("app", "AccessMore app", "8.4 million users (1.3 million added in 2025) and 1.18 billion transactions worth more than N168 trillion in 2025; live in The Gambia, Mozambique, Namibia and Tanzania; cross-border payments planned.",
              s=["con", "sme", "diaspora"], lc="everyday", neo=[0, ""], src=[["Access Bank 2025 annual report", AR25]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "USSD & business channels", "blurb": "*901#, PrimusPlus.", "div": "access", "rev": "commercial", "products": [
            P("ussd", "USSD, internet banking & PrimusPlus", "USSD *901# for feature phones, internet banking, AccessPay and PrimusPlus for corporates.",
              s=["con", "corp"], lc="everyday", neo=[0, ""], src=[["Access Bank 2025 annual report", AR25]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches", "blurb": "About 680 in Nigeria.", "div": "access", "rev": "retail", "products": [
            P("branches", "Branches", "About 678 branches in Nigeria ⚠ read from the report's location table, and more than 900 branches and outlets across 24 countries.",
              s=["con"], lc="open", neo=[0, ""], src=[["Access Bank 2025 annual report", AR25], ["Access: corporate profile", PROFILE]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Agents", "blurb": "750,000 Closa agents.", "div": "closa", "rev": "retail", "products": [
            P("closa", "Access Closa agents", "More than 750,000 agents at the end of 2025, growing in the North Central, South-East and North-East, and a Gates Foundation project to fund 50,000 female agents.",
              s=["con", "women"], lc="open", neo=[0, "Cash and transfers."], src=[["Access Bank 2025 annual report", AR25]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Access", "blurb": "Move and a second debit card.", "products": [
        P("mcataccess", "Mastercard at Access", "Visa carries every Access credit card, the premium debit tiers, the January 2026 corporate card and the Black Card; Verve and AfriGO carry domestic cards and Amex the top travel cards. Mastercard has a naira debit and prepaid card, Access Africa's cross-border payments on Mastercard Move (May 2024), AccessU youth cards in Ghana (July 2025) and a 2025 franchise award.",
          s=["con"], div="abg", rev="retail", mc="The relationship this map is drawn for.",
          src=[["Access: cards", CARDS], ["Mastercard: Access Bank Group and Mastercard, May 2024", MOVE], ["Access Bank Ghana: AccessU with Mastercard, Jul 2025", GHANA]]),
    ]},
    {"id": "pillar-market", "name": "Nigerian payments", "blurb": "NIP, Verve, AfriGO, recapitalisation.", "products": [
        P("market", "The Nigerian market", "NIBSS Instant Payments carries most money (11.2 billion transfers a year); Verve and the CBN's AfriGO compete for domestic cards; the CBN's recapitalisation ran to March 2026; Mastercard is pushing low-cost debit with Zenith (November 2025).",
          s=["con"], div="abg", rev="retail", src=[["NIBSS: digital payments, Jul 2026", NIBSS], ["NIBSS: AfriGO three years on", AFRIGO3], ["Mastercard: Zenith Essential Debit, Nov 2025", ZENITH]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
