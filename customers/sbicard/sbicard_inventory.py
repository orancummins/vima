"""SBI Card's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the company's own unless a source says otherwise: the Q1 FY27 investor presentation (24 July 2026),
the Integrated Annual Report 2025-26 and the Q4 FY26 earnings call (27 April 2026). SBI Card's card pages
could not be read, so most networks come from launch coverage. ``neo`` is the Mastercard lens: [depth, note],
where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

IPQ1 = "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/who-we-are/notices/Investor-Presentation-Q1-FY-26-27.pdf"
IPOCT = "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/who-we-are/notices/investor-presentation-oct25.pdf"
AR26 = "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/who-we-are/notices/Integrated-annual-report-fy-2025-26.pdf"
Q4CALL = "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/who-we-are/notices/SBICards-Earnings-Apr27-2026.pdf"
Q3CALL = "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/who-we-are/notices/SBICards-Earnings-Jan28-2026.pdf"
Q1IW = "https://www.investywise.com/sbi-card-q1-fy27-earnings-call-transcript-and-disclosure/"
ETERNAL = "https://www.theweek.in/news/biz-tech/2026/10/15/sbi-card-zomato-partnership-eternal-features.amp.html"
GPAY = "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/who-we-are/news/2026/Moneycontrol-20260520.pdf"
ADVANTAGE = "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/who-we-are/news/2026/Economic-Times.pdf"
FLIPKART = "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/who-we-are/news/2025/CNBC-TV18-020250826.pdf"
PHONEPE = "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/who-we-are/news/2025/CNBC-TV18-20250722.pdf"
TATANEU = "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/who-we-are/news/2025/CNBC-TV18-20250417.pdf"
APOLLO = "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/who-we-are/news/2025/CNBC-TV18-20250515.pdf"
MINT = "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/who-we-are/news/2026/MintMoney20260302.pdf"
CEO25 = "https://www.sbicard.com/sbi-card-en/assets/docs/pdf/who-we-are/news/2025/CNBC-TV18-new-MDCEO-20250401.pdf"
INDIGO = "https://cardinsider.com/blog/sbi-indigo-launch-new-co-branded-credit-cards/"
INDIGOPTI = "https://www.theweek.in/wire-updates/business/2025/09/25/dcm66-biz-indigo-sbicard.html"
KRIS = "https://www.aviation-defence-universe.com/sbi-card-partners-with-singapore-airlines-launches-exclusive-krisflyer-sbi-card-a-super-premium-co-brand-credit-card"
ELITE16 = "https://indiablooms.com/phoenix/server.php/finance/sbi-card-launches-credit-card-elite/details"
MCAPP = "https://thepaypers.com/payments/news/mastercard-and-sbi-card-enable-contactless-payments-on-the-sbi-card-app"
RUPAY19 = "https://www.businesstoday.in/sectors/banks/sbi-card-to-soon-issue-rupay-credit-cards-says-ceo-hardayal-prasad/story/376614.html"
PROFILE = "https://www.arihantcapital.com/company-information/about-company/20149"
CHOICE = "https://www.businesstoday.in/amp/personal-finance/news/story/credit-cards-from-sept-6-you-can-choose-your-card-network-from-visa-mastercard-rupay-444649-2024-09-05"
MCBAN = "https://www.business-standard.com/article/finance/rbi-lifts-restrictions-related-to-on-boarding-new-customers-on-mastercard-122061600884_1.html"
CARDSHARE = "https://www.businesstoday.in/personal-finance/banking/story/who-dominates-indias-credit-card-market-hdfc-bank-leads-cards-sbi-card-tops-spending-539505-2026-06-27"
CARDADD = "https://www.kotakneo.com/news/personal-finance/india-credit-card-additions-june-2026-hdfc-bank-sbi-cards-icici/"
AGENTPAY = "https://www.paymentsjournal.com/mastercard-advances-agentic-ai-commerce-in-india/"
MCAP = "https://www.indiainfoline.com/company/sbi-cards-payment-services-ltd-share-price/20149"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · parent · technology", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: 2.26 crore cards and ₹58,269 crore of receivables, ROAE of 16.5%, State Bank of India as 68.58% owner, 28 years of issuing, and in-house AI and digital onboarding.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "2.26 crore cards, PAT ₹664 crore.", "div": "sbicard", "rev": "central", "products": [
            P("balance", "Balance sheet & earnings", "Q1 FY27: 2.26 crore cards in force (+7%), record spends of ₹1,18,475 crore (+27%), receivables ₹58,269 crore, PAT ₹664 crore (+20%), ROAA 3.9%, ROAE 16.5%, GNPA 2.04%, CAR 25.6%. FY26: total income ₹20,708 crore, PAT ₹2,167 crore. Rated AAA/Stable by CRISIL and ICRA; market cap about ₹54,000 crore ⚠ (13 October 2026).",
              s=["con"], neo=[0, ""], src=[["Investor presentation Q1 FY27", IPQ1], ["Annual Report 2025-26", AR26], ["India Infoline: share price ⚠", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Setty and Pande.", "div": "sbicard", "rev": "central", "products": [
            P("leadership", "Board & management", "Chairman Challa Sreenivasulu Setty, also Chairman of SBI; MD & CEO Salila Pande since 1 April 2025; COO Saurav Ghosh, CFO Rashmi Mohanty, CRO Krishna Kant Bishnoi, sales and marketing head Girish Budhiraja, CIO and digital head Pradeep Khurana. 4,218 employees at March 2026.",
              s=["con"], neo=[0, ""], src=[["Annual Report 2025-26", AR26], ["CNBC-TV18: Salila Pande MD & CEO, Apr 2025", CEO25]]),
        ]},
        {"id": "1.3", "ic": "building-2", "name": "SBI & heritage", "blurb": "68.58% owned by SBI.", "div": "sbi", "rev": "retail", "products": [
            P("parent", "State Bank of India", "SBI owns 68.58% (30 June 2026). Its branches ('Banca') sourced 47% of new accounts in Q1 FY27, and SBI's YONO 2.0 app is the planned engine for digital acquisition.",
              s=["con", "tier2"], o="I", neo=[0, ""], src=[["Investor presentation Q1 FY27", IPQ1], ["Annual Report 2025-26", AR26]]),
            P("heritage", "Heritage & licence", "Incorporated in 1998 ⚠ as an NBFC that only issues credit cards; 10 lakh cards in 2002, 1 crore in 2019; listed on NSE and BSE in 2020 as India's first pure-play card issuer to list.",
              s=["con"], o="I", neo=[0, ""], src=[["Annual Report 2025-26", AR26], ["Arihant Capital: company profile ⚠", PROFILE]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "AI in risk and service.", "div": "sbicard", "rev": "central", "products": [
            P("tech", "Technology & AI", "About ₹112 crore of technology investment in FY26, PCI-DSS 4.0, 200+ digital projects; AI and machine learning in underwriting, early warning, collections and fraud, speech analytics and conversational AI; Oracle tools for personalisation.",
              s=["con"], neo=[0, "SBI Card's own."], src=[["Annual Report 2025-26", AR26], ["Investor presentation Oct 2025", IPOCT]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & co-brands", "blurb": "Premium, co-brands, YONO.", "div": "sbicard", "rev": "central", "products": [
            P("strategy", "Strategy", "Credit-cost discipline and efficiency now; premium and co-brand growth, digital onboarding through SPRINT and YONO 2.0, and wider RuPay-on-UPI use over the medium term. No numeric targets are published ⚠.",
              s=["con"], neo=[0, ""], src=[["Annual Report 2025-26", AR26], ["Q4 FY26 earnings call", Q4CALL]]),
            P("deals", "Co-brand deals 2024–26", "22 co-brand partners: KrisFlyer (September 2024), Tata Neu (April 2025), Apollo (May 2025), PhonePe (July 2025), Flipkart (August 2025), IndiGo (September 2025), Google Pay (July 2026) and Eternal, Zomato's parent (October 2026). No acquisitions.",
              s=["partner"], o="P", st="new", neo=[1, "Mastercard on five of the eight ⚠."],
              mc="Each new co-brand picks its international network; Mastercard and Visa split them.",
              src=[["Annual Report 2025-26", AR26], ["The Week: Eternal SBI Card, Oct 2026", ETERNAL]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: a core and premium range on Visa, Mastercard and RuPay, digital-platform co-brands, travel and fuel co-brands, RuPay credit on UPI, corporate cards, tokens, and the RBI's network choice at every issue and renewal.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Core & premium cards", "blurb": "Visa, Mastercard, RuPay.", "div": "sbicard", "rev": "retail", "products": [
            P("core", "Core range", "SimplySAVE, SimplyCLICK, PRIME, PULSE, CASHBACK and MILES: SBI Card's own cards, issued on Visa, Mastercard and RuPay, with no split published ⚠.", short="Core cards (Visa, Mastercard, RuPay ⚠)",
              s=["con", "tier2"], lc="everyday", o="B", neo=[1, "Shared with Visa and RuPay ⚠."],
              mc="The largest block of cards, and its network is chosen card by card.",
              src=[["Investor presentation Q1 FY27", IPQ1], ["Arihant Capital: company profile ⚠", PROFILE]]),
            P("elite", "SBI Card ELITE", "Launched on 7 July 2016 as SBI Card's first card on Mastercard World, with Vijay Jasuja (CEO, SBI Card) and Vikas Varma (Mastercard South Asia); today's network mix is not published ⚠.", short="ELITE (Mastercard World at launch)",
              s=["prem"], lc="everyday", ay="Jul 2016", o="P", at="Mastercard", neo=[1, "Mastercard World at launch; current mix ⚠."],
              src=[["India Blooms: SBI Card ELITE, Jul 2016", ELITE16]]),
            P("aurum", "AURUM", "The invite-led super-premium card, launched in 2021; listed on Visa Infinite and Mastercard World ⚠.", short="AURUM (Visa, Mastercard ⚠)",
              s=["prem"], lc="everyday", ay="2021", o="B", neo=[1, "Visa and Mastercard ⚠."], src=[["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "2.2", "ic": "smartphone", "name": "Platform co-brands", "blurb": "Flipkart, PhonePe, Eternal.", "div": "platform", "rev": "retail", "products": [
            P("eternal", "Eternal SBI Card", "Announced on 15 October 2026 with Zomato's parent Eternal, rolling out from 22 October: 10% off Zomato, District and Bistro and some Blinkit categories, ₹499 a year, applied for inside Zomato, Blinkit and District.", short="Eternal (Mastercard, RuPay)",
              s=["digi"], lc="everyday", st="new", ay="Oct 2026", o="P", at="Eternal", neo=[1, "Mastercard and RuPay."],
              mc="The newest co-brand, on Mastercard, inside India's largest food-delivery app.",
              src=[["The Week: Eternal SBI Card, Oct 2026", ETERNAL]]),
            P("flipkart", "Flipkart SBI Card", "Launched on 26 August 2025: 7.5% back on Myntra and 5% on Flipkart, Shopsy and Cleartrip, applied for in the Flipkart app.", short="Flipkart (Mastercard, Visa)",
              s=["digi"], lc="everyday", st="new", ay="Aug 2025", o="P", at="Flipkart", neo=[1, "Mastercard and Visa."],
              src=[["CNBC-TV18: Flipkart SBI Card, Aug 2025", FLIPKART]]),
            P("phonepe", "PhonePe SBI Card", "SELECT BLACK and PURPLE, launched on 22 July 2025: up to 10% back on PhonePe spends; the RuPay version links to UPI and the Visa version is tokenised for online use.", short="PhonePe (RuPay, Visa)",
              s=["digi"], lc="everyday", st="new", ay="Jul 2025", o="P", at="PhonePe", neo=[0, "Visa and RuPay."], src=[["CNBC-TV18: PhonePe SBI Card, Jul 2025", PHONEPE]]),
            P("tataneu", "Tata Neu SBI Card", "Infinity and Plus, launched on 17 April 2025: up to 10% in NeuCoins on Tata brands and up to 1.5% on UPI through the RuPay variant.", short="Tata Neu (RuPay, Visa)",
              s=["digi"], lc="everyday", st="new", ay="Apr 2025", o="P", at="Tata Digital", neo=[0, "Visa and RuPay."], src=[["CNBC-TV18: Tata Neu SBI Card, Apr 2025", TATANEU]]),
            P("gpay", "Google Pay Flex SBI Card", "Launched on 29 July 2026 and run inside the Google Pay app: Stars on spending, EMI on the bill, tokenised tap-to-pay, and UPI payments through the RuPay variant.", short="Google Pay Flex (RuPay, Visa)",
              s=["digi"], lc="everyday", st="new", ay="Jul 2026", o="P", at="Google", neo=[0, "Visa and RuPay."], src=[["Moneycontrol: Google Pay Flex SBI Card, Jul 2026", GPAY]]),
        ]},
        {"id": "2.3", "ic": "plane", "name": "Travel & fuel co-brands", "blurb": "KrisFlyer, IndiGo, BPCL.", "div": "travel", "rev": "retail", "products": [
            P("krisflyer", "KrisFlyer SBI Card & Apex", "With Singapore Airlines, launched on 30 September 2024: KrisFlyer miles on every spend, ₹2,999 and ₹9,999 fees ⚠; which variant is on which network is not stated.", short="KrisFlyer (Amex, Mastercard)",
              s=["prem"], lc="everyday", ay="Sep 2024", o="P", at="Singapore Airlines", neo=[1, "American Express and Mastercard."], src=[["Aviation & Defence Universe: KrisFlyer SBI Card, Sep 2024", KRIS]]),
            P("indigo", "IndiGo SBI Card & ELITE", "With IndiGo, launched on 25 September 2025: BluChips on spending, fees of ₹1,499 and ₹4,999.", short="IndiGo (Mastercard, RuPay ⚠)",
              s=["prem"], lc="everyday", st="new", ay="Sep 2025", o="P", at="IndiGo", neo=[1, "Mastercard and RuPay ⚠."], src=[["The Week (PTI): IndiGo SBI Card, Sep 2025", INDIGOPTI], ["CardInsider: networks ⚠", INDIGO]]),
            P("bpcl", "BPCL SBI Card & OCTANE", "A fuel co-brand with Bharat Petroleum since 2017 that passed 5 million cards in 2026, one of India's largest fuel co-brands; network not confirmed ⚠.", short="BPCL (network ⚠)",
              s=["con", "tier2"], lc="everyday", ay="2017", o="P", at="BPCL", neo=[None, "Network not confirmed."], src=[["Investor presentation Q1 FY27", IPQ1]]),
            P("irctc", "IRCTC SBI Card", "The Indian Railways co-brand, first launched in 2006; an IRCTC card on RuPay since FY21 ⚠.", short="IRCTC (RuPay ⚠)",
              s=["con", "tier2"], lc="everyday", o="P", at="IRCTC", neo=[0, "RuPay ⚠."], src=[["Annual Report 2025-26", AR26], ["Arihant Capital: company profile ⚠", PROFILE]]),
        ]},
        {"id": "2.4", "ic": "zap", "name": "RuPay credit on UPI", "blurb": "UPI spend +126% in FY26.", "div": "sbicard", "rev": "retail", "products": [
            P("upicc", "RuPay credit cards on UPI", "RuPay since 2019; linked to UPI since 2023. More than 60% of the RuPay base is UPI-linked; UPI spends grew 126% in FY26 and 13% in Q1 FY27, 80% of them from Tier 2+ towns. App partners share the issuer's fee under NPCI rules.", short="UPI credit (RuPay)",
              s=["tier2", "digi"], lc="move", o="P", at="NPCI", neo=[0, "RuPay."],
              mc="RuPay on UPI is in every new co-brand; Mastercard can only be the international variant.",
              src=[["Annual Report 2025-26", AR26], ["Investor presentation Q1 FY27", IPQ1], ["Q3 FY26 earnings call", Q3CALL], ["Business Today: RuPay cards, Sep 2019", RUPAY19]]),
        ]},
        {"id": "2.5", "ic": "briefcase-business", "name": "Corporate cards", "blurb": "Spends tripled in FY26.", "div": "corp", "rev": "corporate", "products": [
            P("corpcards", "Corporate cards", "Corporate spends of ₹76,595 crore in FY26 (+210%) and ₹24,442 crore in Q1 FY27 (+125%), about a fifth of all spends, on thin margins because of 'passback' to corporates; network not disclosed ⚠.", short="Corporate cards (network ⚠)",
              s=["corp"], lc="move", st="flux", o="B", neo=[None, "Network not disclosed."],
              mc="A fast-growing commercial book that needs controls and better margins.",
              src=[["Annual Report 2025-26", AR26], ["Q4 FY26 earnings call", Q4CALL], ["Investor presentation Q1 FY27", IPQ1]]),
        ]},
        {"id": "2.6", "ic": "key-round", "name": "Tokens & contactless", "blurb": "MDES since 2020.", "div": "sbicard", "rev": "retail", "products": [
            P("mdes", "Phone payments & tokens", "Tap-to-pay from the SBI Card app on Mastercard's Digital Enablement Service tokens (November 2020) ⚠ current use; Visa and Google Pay tokens on newer co-brands.", short="App tokens (Mastercard MDES ⚠)",
              s=["con", "digi"], lc="everyday", ay="Nov 2020", o="P", at="Mastercard", neo=[3, "Mastercard's own (MDES) ⚠."], src=[["The Paypers: Mastercard and SBI Card contactless, Nov 2020", MCAPP], ["Moneycontrol: Google Pay Flex SBI Card, Jul 2026", GPAY]]),
        ]},
        {"id": "2.7", "ic": "refresh-cw", "name": "Network choice", "blurb": "Chosen at issue and renewal.", "div": "sbicard", "rev": "retail", "products": [
            P("netselect", "Network selection at renewal", "Under the RBI's rule in force since 6 September 2024, issuers with more than 10 lakh cards must offer a choice of network and cannot sign exclusive deals; SBI Card was building 'Network Selection In Card Renewal' at March 2026.", short="Network choice (RBI rule)",
              s=["con"], lc="open", st="new", ay="Sep 2024", o="B", neo=[1, "Visa, Mastercard or RuPay by choice."],
              mc="Every new card and renewal is now open to all three networks.",
              src=[["Business Today: network choice, Sep 2024", CHOICE], ["Annual Report 2025-26", AR26]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card: in-house AI fraud and credit models, SPRINT digital onboarding, Oracle-based personalisation and the Ask ILA assistant, 1,800 merchant offers, and EMIs that make up a third of receivables.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & credit risk", "blurb": "Credit cost down to 6.5%.", "div": "sbicard", "rev": "central", "products": [
            P("fraud", "Fraud detection", "AI-led monitoring, real-time fraud detection, dynamic limits and conversational-AI alerts, with an upgraded fraud-monitoring tool; first-party fraud, onboarding fraud, phishing and account takeover named as risks.",
              s=["con"], lc="everyday", o="B", neo=[0, "SBI Card's own."],
              mc="No Mastercard fraud or identity product is named.",
              src=[["Annual Report 2025-26", AR26]]),
            P("risk", "Underwriting & collections", "Early-warning models, an ECL refresh and account-aggregator data in collections cut gross credit cost from 9.5% to 6.5% in a year and GNPA to 2.04%.",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["Investor presentation Q1 FY27", IPQ1], ["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Digital onboarding", "blurb": "SPRINT and eKYC.", "div": "sbicard", "rev": "retail", "products": [
            P("sprint", "SBI Card SPRINT", "End-to-end digital acquisition since 2022: 10 lakh+ instant cards, DigiLocker KYC and the K-Locker eKYC platform (40 lakh+ eKYCs), linked to YONO and to PhonePe, Tata Neu and Flipkart.",
              s=["digi", "tier2"], lc="open", o="B", neo=[0, ""], src=[["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "AI & personalisation", "blurb": "Ask ILA, 400 campaigns.", "div": "sbicard", "rev": "retail", "products": [
            P("hyper", "Hyper-personalisation", "More than 400 campaigns moved to Oracle behaviour analytics and Responsys for push and in-app offers.",
              s=["con"], lc="everyday", o="P", at="Oracle", neo=[0, ""], src=[["Annual Report 2025-26", AR26], ["Investor presentation Oct 2025", IPOCT]]),
            P("ila", "Ask ILA", "A virtual assistant since 2018: 1.72 crore logins answering 5.51 crore queries in FY26, with WhatsApp and live chat.",
              s=["con"], lc="everyday", ay="2018", o="B", neo=[0, ""], src=[["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Offers & rewards", "blurb": "1,800+ merchant offers.", "div": "sbicard", "rev": "retail", "products": [
            P("offers", "Merchant offers", "More than 1,800 offers in FY26, 1,250 of them national and regional festive offers, and a long-running Apple instant discount of up to ₹7,000.",
              s=["con", "partner"], lc="grow", o="P", neo=[None, "Not stated."],
              mc="Card-linked offers could scale the merchant programme across networks.",
              src=[["Annual Report 2025-26", AR26], ["Investor presentation Q1 FY27", IPQ1]]),
        ]},
        {"id": "3.5", "ic": "coins", "name": "EMI & instalments", "blurb": "A third of receivables.", "div": "sbicard", "rev": "retail", "products": [
            P("emi", "Flexipay, Encash & EMIs", "EMIs on purchases and bills, cash and balance transfers: EMI is 33% of receivables, and management wants more of it.",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["Investor presentation Q1 FY27", IPQ1], ["Q4 FY26 earnings call", Q4CALL]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What it sells: card credit to 2.26 crore cardholders, health and lifestyle co-brands, cards for partner banks, and secured cards against SBI fixed deposits.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Card credit", "blurb": "₹58,269 crore lent.", "div": "sbicard", "rev": "retail", "products": [
            P("retail", "Retail card lending", "Receivables of ₹58,269 crore (June 2026): transactors 45%, revolvers 22%, EMI 33%; retail spends of ₹94,033 crore a quarter (+14%), 63% of them online; 19.5% of India's card spend.",
              s=["con"], lc="borrow", neo=[1, "Card spend on all networks."], src=[["Investor presentation Q1 FY27", IPQ1]]),
        ]},
        {"id": "4.2", "ic": "gem", "name": "Health & lifestyle co-brands", "blurb": "Apollo, Reliance, Titan.", "div": "platform", "rev": "retail", "products": [
            P("apollo", "Apollo SBI Card SELECT", "With Apollo HealthCo, launched on 15 May 2025: up to 25% back on Apollo 24|7 and pharmacy spends.", short="Apollo (RuPay, Mastercard)",
              s=["con"], lc="everyday", st="new", ay="May 2025", o="P", at="Apollo HealthCo", neo=[1, "RuPay and Mastercard."], src=[["CNBC-TV18: Apollo SBI Card SELECT, May 2025", APOLLO]]),
            P("lifestyle", "Reliance, Titan & Landmark cards", "Reliance SBI Card (2023), Titan SBI Card (2024) and Landmark Rewards; networks not confirmed ⚠.", short="Retail co-brands (network ⚠)",
              s=["con"], lc="everyday", o="P", neo=[None, "Networks not confirmed."], src=[["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "4.3", "ic": "landmark", "name": "Partner-bank cards", "blurb": "Cards for other banks.", "div": "banks", "rev": "retail", "products": [
            P("bankcards", "Partner-bank cards", "Cards issued for Bank of Maharashtra (launched 2025), UCO Bank, Punjab & Sind Bank and Karnataka Bank customers; networks not disclosed ⚠.",
              s=["con", "tier2"], lc="everyday", o="P", neo=[None, "Not disclosed."], src=[["Investor presentation Q1 FY27", IPQ1], ["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "4.4", "ic": "wallet", "name": "Secured cards", "blurb": "Against an SBI deposit.", "div": "sbi", "rev": "retail", "products": [
            P("advantage", "Advantage SBI Card", "Launched on 24 September 2026: ELITE, PRIME, SimplyCLICK and SimplySAVE secured against an SBI fixed deposit, applied for paperless in YONO.",
              s=["tier2"], lc="open", st="new", ay="Sep 2026", o="P", at="SBI", neo=[None, "Network not stated."], src=[["Economic Times: Advantage SBI Card, Sep 2026", ADVANTAGE]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How cardholders reach SBI Card: the app with 1.5 crore active installs, SBI's branches and YONO, a sales force in 206 cities, and partner apps from PhonePe to Zomato.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "SBI Card app", "blurb": "81.8 crore logins.", "div": "sbicard", "rev": "retail", "products": [
            P("app", "SBI Card app", "1.5 crore active installs and 81.8 crore logins in FY26, with 100+ self-service features, card controls and alerts.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["Annual Report 2025-26", AR26]]),
            P("travelbook", "Travel bookings in the app", "Flights, hotels and buses booked inside the app with ixigo, Yatra and AbhiBus (2026).",
              s=["con", "prem"], lc="beyond", st="new", o="P", at="ixigo, Yatra, AbhiBus", neo=[0, ""], src=[["Investor presentation Q1 FY27", IPQ1]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "SBI branches & YONO", "blurb": "47% of new accounts.", "div": "sbi", "rev": "retail", "products": [
            P("banca", "SBI branches & YONO", "SBI branches sourced 47% of new accounts in Q1 FY27; YONO 2.0 is the focus for digital acquisition.",
              s=["con", "tier2"], lc="open", o="P", at="SBI", neo=[0, ""], src=[["Investor presentation Q1 FY27", IPQ1], ["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "5.3", "ic": "store", "name": "Open market", "blurb": "206 cities.", "div": "sbicard", "rev": "retail", "products": [
            P("openmkt", "Sales force & kiosks", "Open-market sourcing (53% of Q1 FY27 accounts) from 200+ locations in 206 cities, plus kiosks such as those in Croma stores for Tata Neu.",
              s=["con", "tier2"], lc="open", o="B", neo=[0, ""], src=[["Annual Report 2025-26", AR26], ["CNBC-TV18: Tata Neu SBI Card, Apr 2025", TATANEU]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partner apps", "blurb": "PhonePe to Zomato.", "div": "platform", "rev": "retail", "products": [
            P("partnerapps", "Partner apps", "Applications and servicing inside PhonePe, Flipkart, Tata Neu, Google Pay, Apollo 24|7, IndiGo and, from October 2026, Zomato, Blinkit and District.",
              s=["digi", "partner"], lc="open", st="new", o="P", neo=[0, ""], src=[["Annual Report 2025-26", AR26], ["The Week: Eternal SBI Card, Oct 2026", ETERNAL]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at SBI Card", "blurb": "One of four networks.", "products": [
        P("mcatsbicard", "Mastercard at SBI Card", "SBI Card issues on Visa, Mastercard, RuPay and American Express and publishes no split ⚠. Mastercard carried the first premium card (ELITE, 2016) and app tokens (2020), and since 2024 is the international network on KrisFlyer, Apollo, Flipkart, IndiGo ⚠ and Eternal. Visa has Tata Neu, PhonePe and Google Pay; RuPay is on almost every new card for UPI.",
          s=["con"], div="sbicard", rev="central", mc="The relationship this map is drawn for.",
          src=[["India Blooms: SBI Card ELITE, Jul 2016", ELITE16], ["The Week: Eternal SBI Card, Oct 2026", ETERNAL], ["CNBC-TV18: Flipkart SBI Card, Aug 2025", FLIPKART]]),
    ]},
    {"id": "pillar-market", "name": "Indian cards", "blurb": "Choice, UPI, RuPay.", "products": [
        P("market", "The Indian market", "About 12.1 crore cards (May 2026): HDFC Bank 22.0% of cards, SBI Card 18.6%, ICICI 16.1%, Axis 13.4%. Network choice at issue and renewal since September 2024; RuPay credit on UPI; Mastercard barred from new cardholders from July 2021 to June 2022; Mastercard ran India's first agentic payment in February 2026.",
          s=["con"], div="sbicard", rev="central",
          src=[["Business Today: issuer shares, Jun 2026", CARDSHARE], ["Kotak Neo: card additions, Jun 2026", CARDADD], ["Business Today: network choice, Sep 2024", CHOICE], ["Business Standard: Mastercard curbs lifted, Jun 2022", MCBAN], ["Payments Journal: agentic payment, Feb 2026", AGENTPAY]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
