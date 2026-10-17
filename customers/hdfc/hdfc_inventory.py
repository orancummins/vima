"""HDFC Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the Q2 FY27 results and presentation (17 October 2026),
the Q4 FY26 analyst call (18 April 2026) and the Integrated Annual Report 2025-26. HDFC's card pages rarely state
the network, so several card networks are inferred and marked. ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

Q2PR = "https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/pdf/about-us/financial-results/2026-2027/quarter-2/press-release-sep-2026.pdf"
Q2PPT = "https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/pdf/about-us/financial-results/2026-2027/quarter-2/q2fy27-earnings-presentation.pdf"
Q4PR = "https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/pdf/about-us/financial-results/2025-2026/quarter-4/press-release-march-2026.pdf"
Q4CALL = "https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/pdf/about-us/financial-results/2025-2026/quarter-4/HDFCBank-Analyst-Apr18-2026-vF.pdf"
AR26 = "https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/pdf/annual-reports/2025-26/reports/HDFC_Bank_IR26.pdf"
CHAIR = "https://www.outlookbusiness.com/amp/story/corporate/rbi-approves-ex-chief-election-commissioner-rajiv-kumar-as-hdfc-bank-chairman"
REVIEW = "https://www.outlookbusiness.com/corporate/hdfc-bank-likely-to-reappoint-sashidhar-jagdishan-after-legal-review-clears-ex-chairmans-concerns"
CEO = "https://www.kotakneo.com/news/stocks/hdfc-bank-names-anup-bagchi-as-md-ceo-from-27-october/"
CARDSHARE = "https://www.businesstoday.in/personal-finance/banking/story/who-dominates-indias-credit-card-market-hdfc-bank-leads-cards-sbi-card-tops-spending-539505-2026-06-27"
CARDADD = "https://www.kotakneo.com/news/personal-finance/india-credit-card-additions-june-2026-hdfc-bank-sbi-cards-icici/"
SWIGGY26 = "https://oga-prod.angelone.in/news/stocks/swiggy-hdfc-bank-launch-blck-and-ornge-co-branded-credit-cards-with-up-to-48-000-annual-savings"
SWIGGYBLCK = "https://www.hdfc.bank.in/credit-cards/swiggy-blck-hdfc-bank-credit-card"
PIXEL = "https://www.hdfc.bank.in/credit-cards/pixel-play-credit-card"
FIFA = "https://www.deccanchronicle.com/business/in-other-news/visa-and-hdfc-bank-bring-indian-fans-closer-to-the-fifa-world-cup-2026-1950225"
TATANEU = "https://www.hdfc.bank.in/credit-cards/tata-neu-infinity-hdfc-bank-credit-card"
IOCL = "https://www.hdfc.bank.in/credit-cards/indianoil-hdfc-bank-credit-card"
MARRIOTT = "https://www.hdfc.bank.in/credit-cards/marriott-bonvoy-credit-card"
DINERSBLK = "https://www.hdfc.bank.in/credit-cards/diners-club-black-metal-edition-credit-card"
INFINIA = "https://www.hdfc.bank.in/credit-cards/infinia-credit-card"
PINELABS = "https://www.hdfc.bank.in/credit-cards/pine-labs-pro-credit-card"
PHONEPE = "https://www.hdfc.bank.in/credit-cards/phonepe-hdfc-bank-ultimo-credit-card"
UPIRUPAY = "https://www.hdfc.bank.in/credit-cards/hdfc-bank-upi-rupay-credit-card"
BHARAT = "https://www.hdfc.bank.in/credit-cards/bharat-credit-card"
CCLIST = "https://www.hdfc.bank.in/credit-cards"
MILLENNIA19 = "https://www.electronicpaymentsinternational.com/news/hdfc-bank-launches-card-range-for-millennials"
DINERS11 = "https://www.retailbankerinternational.com/news/hdfc-to-issue-diners-club-credit-cards-in-india/"
PAYTMVISA = "https://www.retailbankerinternational.com/news/hdfc-bank-paytm-partner-visa-powered-credit-cards/"
DFC = "https://www.mastercard.com/news/ap/en-in/newsroom/press-releases/en-in/2021/october/hdfc-bank-mastercard-usaid-and-dfc-launch-100-million-credit-facility-for-micro-small-and-medium-enterprises-msmes-in-india/"
RECUR = "https://www.mastercard.com/news/ap/en-in/newsroom/press-releases/en-in/2021/october/mastercard-enables-recurring-payments-to-offer-a-hassle-free-experience-for-bank-s-cardholders/"
GPAY = "https://www.mastercard.com/news/ap/en-in/newsroom/press-releases/en-in/2021/december/mastercard-and-google-pay-come-together-to-facilitate-tokenization-for-card-based-payments-across-india/"
SAMSUNG = "https://newsroom.mastercard.com/asia-pacific/press-releases/mastercard-moves-india-one-step-closer-to-cashless-society-with-samsung-pay/"
MCBAN = "https://www.business-standard.com/article/finance/rbi-lifts-restrictions-related-to-on-boarding-new-customers-on-mastercard-122061600884_1.html"
HDFCBAN = "https://www.business-standard.com/article/markets/lifting-of-credit-card-ban-may-spark-up-to-32-rally-in-hdfc-bank-analysts-121081800347_1.html"
CHOICE = "https://www.businesstoday.in/amp/personal-finance/news/story/credit-cards-from-sept-6-you-can-choose-your-card-network-from-visa-mastercard-rupay-444649-2024-09-05"
UPIMDR = "https://www.hdfc.bank.in/blogs/upi/new-upi-rules-2026"
UPISEP = "https://startuptalky.com/india-upi-transactions-september-2026/"
UPIFEAT = "https://www.hdfc.bank.in/content/dam/hdfcbankpws/in/en/pdf/press-release/2024/q3-jul-sep/august/hdfc-bank-launches-new-upi-features.pdf"
VYAPAR = "https://www.hdfc.bank.in/press-release/2022/q4/hdfc-bank-launches-smarthub-vyapar-for-merchants"
AGENTPAY = "https://www.paymentsjournal.com/mastercard-advances-agentic-ai-commerce-in-india/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · governance · scale", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a ₹45.8 trillion balance sheet and 103.6 million customers, a new chairman and a new CEO in 2026, the 2023 merger with HDFC Ltd, the Neev AI platform, and leading shares in cards and acquiring.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "103.6m customers, RoA 1.78%.", "div": "bank", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Balance sheet of ₹45.8 trillion, deposits of ₹33.3 trillion (+18.8%) and gross advances of ₹32.2 trillion (+16.3%) at 30 September 2026; Q2 FY27 profit after tax ₹195.1 billion (RoA 1.78%, RoE 13.5%); FY26 profit ₹746.7 billion; CET1 17.1%; GNPA 1.11%; 103.6 million customers and 210,109 staff.",
              s=["con"], neo=[0, ""], src=[["Q2 FY27 results release, 17 Oct 2026", Q2PR], ["Q2 FY27 presentation", Q2PPT], ["FY26 results release, 18 Apr 2026", Q4PR]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Kumar chairs; Bagchi takes over.", "div": "bank", "rev": "other", "products": [
            P("leadership", "Board & management", "Chairman Rajiv Kumar (RBI approval 15 July 2026) after Atanu Chakraborty resigned on 18 March 2026; MD & CEO Sashidhar Jagdishan until 26 October 2026, then Anup Bagchi, approved by the RBI on 1 October 2026 for three years; Deputy MD Kaizad Bharucha, CFO Srinivasan Vaidyanathan.",
              s=["corp"], st="flux", ay="Oct 2026", neo=[0, ""], src=[["Outlook Business: chairman approved, Jul 2026", CHAIR], ["Kotak Neo: Bagchi named CEO, Oct 2026", CEO], ["Outlook Business: legal review, Jun 2026", REVIEW]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & merger", "blurb": "One with HDFC Ltd since 2023.", "div": "bank", "rev": "retail", "products": [
            P("merger", "HDFC Ltd merger & brand", "Set up in 1994 by Housing Development Finance Corporation, which merged into the bank on 1 July 2023; listed on NSE, BSE and NYSE (HDB); 15.39 billion shares after the FY26 bonus issue, about ₹11 lakh crore of market value at ₹721 (1 October 2026) ⚠; brand valued at US$47.5 billion by Kantar BrandZ 2026.",
              s=["con"], o="I", ay="Jul 2023", neo=[0, ""], src=[["Annual Report 2025-26", AR26], ["Q2 FY27 presentation", Q2PPT], ["Kotak Neo: share price, Oct 2026", CEO]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Neev, an in-house AI platform.", "div": "bank", "rev": "other", "products": [
            P("neev", "Neev AI platform", "An in-house enterprise AI platform with Model Context Protocol, an Agentic Studio and an Agentic Mesh, used for card processing, trade operations, risk monitoring and frontline agentic bots; new NetBanking and in-house mobile platforms rolled out in FY26.",
              s=["corp"], st="new", o="B", neo=[0, ""],
              mc="HDFC is building agents; Agent Pay gives them a card rail to pay on.",
              src=[["Annual Report 2025-26", AR26], ["Q4 FY26 analyst call, Apr 2026", Q4CALL]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & position", "blurb": "A third of India's acquiring.", "div": "bank", "rev": "other", "products": [
            P("strategy", "Strategy & market position", "Grow faster than the system once the post-merger loan-to-deposit ratio is rebuilt; 11.5% of deposits and 14.0% of advances; about 35–36% of merchant acquiring, 21–22% of credit-card issuance and 26–28% of card spend (CEO, April 2026).",
              s=["corp"], neo=[0, ""], src=[["Q4 FY26 analyst call, Apr 2026", Q4CALL], ["Q2 FY27 presentation", Q2PPT]]),
            P("deals", "Group deals", "HDFC Ltd merger (July 2023), HDB Financial Services listed on 2 July 2025, the bank's first 1:1 bonus issue in FY26, and new co-brands with Swiggy and PhonePe.",
              s=["corp"], o="A", neo=[0, ""], src=[["Annual Report 2025-26", AR26]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: India's largest credit-card book on four networks, co-brands from Swiggy on Mastercard to Tata Neu on Visa and RuPay, Diners Club at the top end, debit and prepaid, UPI and RuPay credit on UPI, a third of the country's card acquiring, and cross-border and e-rupee rails.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "22% of India's cards.", "div": "cards", "rev": "retail", "products": [
            P("cards", "Credit-card franchise", "More than 2 crore (20 million) credit-card customers, 22% of India's cards in force and 29.2% of spend (May 2026); more than 50 lakh new cards a year; FY26 cards issued +11% and spend +18%; on Visa, Mastercard, RuPay and Diners Club.", short="Credit cards (four networks)",
              s=["card"], lc="borrow", o="B", neo=[1, "Shared across four networks."],
              mc="India's biggest card book, and under the RBI's choice rule every new card is contested.",
              src=[["Annual Report 2025-26", AR26], ["Business Today: card market, Jun 2026", CARDSHARE], ["Kotak Neo: June 2026 additions", CARDADD]]),
            P("premium", "Infinia & Regalia Gold", "The super-premium Infinia (metal) and Regalia Gold travel cards; the bank's pages do not name the network ⚠, and Visa and Mastercard variants are both reported.", short="Infinia & Regalia (Visa, Mastercard ⚠)",
              s=["card"], lc="borrow", o="B", neo=[1, "Visa and Mastercard variants ⚠."], src=[["HDFC Bank: Infinia", INFINIA], ["HDFC Bank: credit cards", CCLIST]]),
            P("millennia", "Millennia & MoneyBack+", "Cashback cards for younger customers; the Millennia range (credit, debit, prepaid and EMI) launched with Mastercard in August 2019, aiming for 2 million cards in five years; now issued on more than one network ⚠.", short="Millennia (Mastercard at launch)",
              s=["card", "con"], lc="borrow", ay="Aug 2019", o="P", at="Mastercard", neo=[1, "Mastercard at launch; more networks now ⚠."], src=[["EPI: Millennia on Mastercard, Aug 2019", MILLENNIA19]]),
        ]},
        {"id": "2.2", "ic": "gift", "name": "Co-brand cards", "blurb": "Swiggy on Mastercard.", "div": "cards", "rev": "retail", "products": [
            P("swiggy", "Swiggy BLCK & Swiggy ORNGE", "Two Swiggy co-brands that replaced the original Swiggy HDFC card on 9 March 2026: 10% cashback on Swiggy for BLCK, 5% for ORNGE, with Mastercard World golf benefits.", short="Swiggy (Mastercard)",
              s=["card"], lc="everyday", st="new", ay="Mar 2026", o="P", at="Swiggy, Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's clearest HDFC programme, and Swiggy took part in Agent Pay's first India payments.",
              src=[["Angel One: Swiggy BLCK and ORNGE, Mar 2026", SWIGGY26], ["HDFC Bank: Swiggy BLCK", SWIGGYBLCK]]),
            P("tataneu", "Tata Neu Infinity & Plus", "NeuCoins on Tata's apps; issued on Visa and on RuPay, which works on UPI.", short="Tata Neu (Visa, RuPay)",
              s=["card"], lc="everyday", o="P", at="Tata Digital", neo=[0, "Visa and RuPay."], src=[["HDFC Bank: Tata Neu Infinity", TATANEU]]),
            P("pixel", "Pixel Play & Pixel Go", "A born-digital card run from the app; a FIFA World Cup 2026 Pixel Play Visa card launched with Visa in April 2026; the RuPay variant pays on UPI.", short="Pixel (Visa, RuPay)",
              s=["card"], lc="everyday", st="new", ay="Apr 2026", o="P", at="Visa", neo=[0, "Visa and RuPay."], src=[["HDFC Bank: Pixel Play", PIXEL], ["Deccan Chronicle: Visa FIFA card, Apr 2026", FIFA]]),
            P("iocl", "IndianOil HDFC Bank", "A fuel co-brand with IndianOil; fuel points are earned on Visa and RuPay merchant codes.", short="IndianOil (Visa, RuPay)",
              s=["card"], lc="everyday", o="P", at="IndianOil", neo=[0, "Visa and RuPay."], src=[["HDFC Bank: IndianOil card", IOCL]]),
            P("phonepe", "PhonePe HDFC Bank Ultimo & Uno", "Co-brand with PhonePe, India's largest UPI app, launched in FY26; network not stated ⚠.",
              s=["card"], lc="everyday", st="new", o="P", at="PhonePe", neo=[None, "Network not stated ⚠."], src=[["HDFC Bank: PhonePe Ultimo", PHONEPE], ["Annual Report 2025-26", AR26]]),
            P("bizcobrand", "Pine Labs, Paytm & Flipkart Wholesale cards", "Business co-brands for merchants and traders; the Paytm cards launched on Visa in 2021 and Pine Labs Pro carries Visa lounge access ⚠.", short="Business co-brands (Visa ⚠)",
              s=["sme"], lc="borrow", o="P", at="Pine Labs, Paytm, Flipkart", neo=[0, "Visa ⚠."], src=[["HDFC Bank: Pine Labs Pro", PINELABS], ["Retail Banker International: Paytm Visa cards, 2021", PAYTMVISA]]),
        ]},
        {"id": "2.3", "ic": "gem", "name": "Diners Club", "blurb": "The top-end badge.", "div": "cards", "rev": "retail", "products": [
            P("diners", "Diners Club Black Metal & Marriott Bonvoy", "HDFC has issued and acquired Diners Club cards in India since a 2011 deal with Discover; Diners Black Metal (₹10,000 fee) and the Marriott Bonvoy HDFC card run on Diners.", short="Diners Club",
              s=["card"], lc="borrow", ay="Oct 2011", o="P", at="Diners Club (Discover)", neo=[0, "Diners Club."],
              src=[["Retail Banker International: Diners deal, Oct 2011", DINERS11], ["HDFC Bank: Diners Black Metal", DINERSBLK], ["HDFC Bank: Marriott Bonvoy", MARRIOTT]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Debit & prepaid", "blurb": "9 crore cards issued in FY26.", "div": "bank", "rev": "retail", "products": [
            P("debit", "Debit & prepaid cards", "More than 9 crore credit, debit and prepaid cards issued in FY26; debit on RuPay (including NRO accounts), Visa and Mastercard, with the split not published ⚠.", short="Debit (RuPay, Visa, Mastercard ⚠)",
              s=["con"], lc="everyday", o="B", neo=[1, "Split across networks ⚠."], src=[["Annual Report 2025-26", AR26], ["HDFC Bank: cards", CCLIST]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "UPI & RuPay credit", "blurb": "Credit on UPI.", "div": "bank", "rev": "retail", "products": [
            P("upicc", "UPI RuPay credit cards", "The UPI RuPay credit card, the Bharat card and UPI RuPay Biz put a credit line on UPI QR codes; RuPay variants of Tata Neu, Pixel and IndianOil do the same.", short="UPI RuPay credit (RuPay)",
              s=["con", "sme"], lc="borrow", o="P", at="NPCI", neo=[0, "RuPay."],
              mc="RuPay on UPI is the domestic route around the international networks.",
              src=[["HDFC Bank: UPI RuPay credit card", UPIRUPAY], ["HDFC Bank: Bharat card", BHARAT]]),
            P("upi", "UPI", "Issuer, app provider and acquirer on UPI, with UPI Circle delegate payments (August 2024); UPI handled 24.07 billion payments in September 2026, and from 15 October 2026 merchants pay 0.4% on eligible payments above ₹2,000.",
              s=["con", "mer"], lc="move", o="P", at="NPCI", neo=[0, "UPI."], src=[["HDFC Bank: UPI features, Aug 2024", UPIFEAT], ["StartupTalky: UPI Sep 2026", UPISEP], ["HDFC Bank: new UPI rules 2026", UPIMDR]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Merchant acquiring", "blurb": "35–36% of acquiring.", "div": "vyapar", "rev": "retail", "products": [
            P("vyapar", "SmartHub Vyapar", "The offline merchant platform launched in October 2022: 20.4 lakh merchants and ₹4.73 lakh crore processed by March 2026, with QR codes, soundboxes and POS; the bank has 59 lakh acceptance points and about 35–36% of acquiring.", short="SmartHub Vyapar (all networks)",
              s=["mer"], lc="move", ay="Oct 2022", o="P", at="Mintoak", neo=[1, "Accepts every network."],
              mc="A third of India's card acquiring runs through HDFC terminals.",
              src=[["Annual Report 2025-26", AR26], ["HDFC Bank: SmartHub Vyapar, Oct 2022", VYAPAR], ["Q4 FY26 analyst call, Apr 2026", Q4CALL]]),
            P("gateway", "SmartGATEWAY", "The online payment gateway launched in February 2024, with more than 150 payment methods: cards, UPI, net banking and wallets.",
              s=["mer"], lc="move", ay="Feb 2024", o="B", neo=[1, "Accepts every network."], src=[["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "2.7", "ic": "earth", "name": "Cross-border & e-rupee", "blurb": "Its own cross-border rails.", "div": "bank", "rev": "wholesale", "products": [
            P("xborder", "Cross-border payments", "APIs that provide AD-1 banking to cross-border fintechs, and plans to launch the bank's own cross-border rails under new RBI rules; a GIFT City branch; 13–15% of India's trade flows.",
              s=["nri", "corp"], lc="move", st="new", o="B", neo=[0, ""],
              mc="Cross-border is being built now; Mastercard Move is not in it.",
              src=[["Annual Report 2025-26", AR26], ["Q4 FY26 analyst call, Apr 2026", Q4CALL]]),
            P("cbdc", "e-rupee (CBDC)", "e-rupee is accepted alongside cards, UPI and wallets across HDFC's acceptance network.",
              s=["con", "mer"], lc="move", o="P", at="RBI", neo=[0, ""], src=[["Annual Report 2025-26", AR26]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account and card: fraud awareness and agentic security tools, tokens and recurring mandates, AI agents for staff and customers, and rewards and EMI.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Vigil Aunty, OTP-less login.", "div": "bank", "rev": "retail", "products": [
            P("fraud", "Fraud & cyber defence", "In-house agentic tools for threat detection, OTP-less authentication and an app lock, and the 'Vigil Aunty' awareness campaign since 2021; no Mastercard fraud product is named in public sources ⚠.",
              s=["con"], lc="everyday", o="B", neo=[0, "HDFC's own."], src=[["Annual Report 2025-26", AR26], ["Q4 FY26 analyst call, Apr 2026", Q4CALL]]),
        ]},
        {"id": "3.2", "ic": "key-round", "name": "Tokens & mandates", "blurb": "Tokens since 2021.", "div": "cards", "rev": "retail", "products": [
            P("tokens", "Tokenisation & wallets", "HDFC Mastercards were in Samsung Pay's India launch (March 2017) and live on Google Pay tokens (December 2021); MyCards, the card-servicing platform, has 4.5 crore registered customers.",
              s=["card"], lc="everyday", ay="Dec 2021", o="P", at="Mastercard, Google", neo=[1, "Mastercard tokens for Mastercards."],
              src=[["Mastercard: Google Pay tokens, Dec 2021", GPAY], ["Mastercard: Samsung Pay, Mar 2017", SAMSUNG], ["Annual Report 2025-26", AR26]]),
            P("recurring", "Recurring mandates", "Card e-mandates under RBI rules: HDFC debit and credit Mastercards supported recurring payments from Mastercard's launch in October 2021.",
              s=["card"], lc="everyday", ay="Oct 2021", o="P", at="Mastercard", neo=[1, "On Mastercard for Mastercards."], src=[["Mastercard: recurring payments, Oct 2021", RECUR]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "AI agents", "blurb": "Agentic bots at the front line.", "div": "bank", "rev": "retail", "products": [
            P("bots", "Agentic bots & conversational AI", "Agentic bots for frontline staff, AI for card and transaction queries, ChatBanking on WhatsApp and voice bots on PhoneBanking, all on Neev.",
              s=["con", "card"], lc="everyday", st="new", o="B", neo=[0, ""],
              mc="Mastercard's first India Agent Pay payments (February 2026) used other banks' cards.",
              src=[["Annual Report 2025-26", AR26], ["PaymentsJournal: Agent Pay in India, Feb 2026", AGENTPAY]]),
        ]},
        {"id": "3.4", "ic": "coins", "name": "Rewards & EMI", "blurb": "SmartBuy and EasyEMI.", "div": "cards", "rev": "retail", "products": [
            P("rewards", "SmartBuy & card rewards", "SmartBuy, the bank's rewards and travel portal, with reward points, cashback and NeuCoins across the card range ⚠.",
              s=["card"], lc="grow", o="B", neo=[0, ""],
              mc="Card-linked offers could feed SmartBuy across networks.",
              src=[["HDFC Bank: credit cards", CCLIST]]),
            P("easyemi", "EasyEMI", "Instalments at the point of sale and on cards, aimed at semi-urban and rural customers.",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["Annual Report 2025-26", AR26]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: ₹17.4 trillion of retail loans with ₹9.2 trillion of mortgages, Business Banking growing 28%, wholesale and trade, and a group of insurers, an asset manager, an NBFC and a broker.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Mortgages & retail loans", "blurb": "₹17.4trn of retail loans.", "div": "bank", "rev": "retail", "products": [
            P("mortgages", "Mortgages", "₹9.2 trillion at September 2026 (+7.5%), inherited from HDFC Ltd; a top-two mortgage lender.",
              s=["home"], lc="borrow", o="I", neo=[0, ""], src=[["Q2 FY27 presentation", Q2PPT], ["Q4 FY26 analyst call, Apr 2026", Q4CALL]]),
            P("loans", "Personal, auto & retail loans", "Retail assets of ₹8.2 trillion (+16.9%), with 99% of personal loans originated digitally and the top 'wheels' book.",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["Q2 FY27 presentation", Q2PPT], ["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "MSME & Business Banking", "blurb": "Up 28% a year.", "div": "bank", "rev": "wholesale", "products": [
            P("bizbank", "Business Banking", "Small and mid-market loans of ₹7.1 trillion (+23.5%), Business Banking ₹5.3 trillion (+28.1%); a top-two MSME bank.",
              s=["sme"], lc="borrow", o="B", neo=[0, ""], src=[["Q2 FY27 presentation", Q2PPT], ["Q4 FY26 analyst call, Apr 2026", Q4CALL]]),
            P("bizcards", "Business cards", "A suite of Business Cards for the self-employed and MSMEs, plus Corporate Visa Signature cards; the network split is not public ⚠.",
              s=["sme", "corp"], lc="everyday", o="B", neo=[None, "Split not public ⚠."],
              mc="Commercial and virtual cards for a top-two MSME bank are open ground.",
              src=[["Annual Report 2025-26", AR26], ["HDFC Bank: credit cards", CCLIST]]),
            P("msmefund", "MSME credit facility", "A US$100 million credit facility for small businesses with Mastercard, USAID and DFC (October 2021), with at least half for women entrepreneurs ⚠ current status.",
              s=["sme"], lc="borrow", ay="Oct 2021", o="P", at="Mastercard, DFC, USAID", neo=[1, "Mastercard partnership ⚠ status."], src=[["Mastercard: MSME facility, Oct 2021", DFC]]),
        ]},
        {"id": "4.3", "ic": "factory", "name": "Wholesale & trade", "blurb": "13–15% of India's trade.", "div": "bank", "rev": "wholesale", "products": [
            P("wholesale", "Corporate & wholesale banking", "Corporate and other wholesale loans of ₹8.6 trillion (+16.4%), transaction banking and 13–15% of India's trade flows.",
              s=["corp"], lc="borrow", o="B", neo=[0, ""], src=[["Q2 FY27 presentation", Q2PPT], ["Q4 FY26 analyst call, Apr 2026", Q4CALL]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Group & wealth", "blurb": "Insurance, AMC, NBFC.", "div": "life", "rev": "other", "products": [
            P("hdb", "HDB Financial Services", "A non-deposit NBFC, 74.1% owned and listed in July 2025: loans of ₹1,245 billion, Q2 FY27 profit ₹7.8 billion.",
              s=["con"], lc="borrow", o="B", div="hdb", neo=[0, ""], src=[["Q2 FY27 results release, 17 Oct 2026", Q2PR]]),
            P("insurance", "HDFC Life & HDFC ERGO", "HDFC Life (50.5%, 16.2% of individual premium) and HDFC ERGO (50.2%).",
              s=["con"], lc="grow", o="I", neo=[0, ""], src=[["Q2 FY27 results release, 17 Oct 2026", Q2PR], ["Q2 FY27 presentation", Q2PPT]]),
            P("amc", "HDFC AMC, HDFC Securities & wealth", "HDFC AMC (52.3%, about ₹9.7 trillion of assets, 11.1% share), HDFC Securities (93.9%) and a wealth team serving about 86,500 households.",
              s=["nri", "con"], lc="grow", o="I", div="amc", neo=[0, ""], src=[["Q2 FY27 results release, 17 Oct 2026", Q2PR], ["Annual Report 2025-26", AR26]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the new mobile app and NetBanking, PayZapp, 9,706 branches with half outside the cities, and co-brand partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Mobile app & NetBanking", "blurb": "60 million registered.", "div": "bank", "rev": "retail", "products": [
            P("app", "Mobile banking & NetBanking", "New in-house mobile banking and NetBanking platforms (FY26), with 60 million registered app users and 97% of payment and service transactions digital.",
              s=["con", "card", "nri"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["Q4 FY26 analyst call, Apr 2026", Q4CALL], ["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "5.2", "ic": "wallet", "name": "PayZapp", "blurb": "2 crore registrations.", "div": "payzapp", "rev": "retail", "products": [
            P("payzapp", "PayZapp & Zapp account", "PayZapp 2.0 (March 2023): about 2.1 crore registrations and 50–52 lakh monthly users, with cards, wallet and UPI; opened in January 2026 to NRIs in the US, UK, Canada and the Gulf; the Zapp account, a UPI wallet, has about 5 lakh monthly users.", short="PayZapp (all networks)",
              s=["con", "nri"], lc="move", ay="Mar 2023", o="B", neo=[1, "Cards of every network."], src=[["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & correspondents", "blurb": "9,706 branches.", "div": "bank", "rev": "retail", "products": [
            P("branches", "Branches, ATMs & correspondents", "9,706 branches, 20,881 ATMs and 14,365 business correspondents across 4,177 cities and towns at September 2026, half of the branches semi-urban or rural.",
              s=["con", "sme"], lc="open", o="B", neo=[0, ""], src=[["Q2 FY27 results release, 17 Oct 2026", Q2PR]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partners", "blurb": "Swiggy, Tata Neu, PhonePe.", "div": "cards", "rev": "retail", "products": [
            P("partners", "Co-brand & platform partners", "Swiggy, Tata Neu, PhonePe, Marriott, IndianOil, Pine Labs, Flipkart Wholesale and Paytm sell HDFC cards in their apps; Common Service Centres run its correspondents.",
              s=["card", "sme"], lc="open", o="P", at="Swiggy, Tata Digital, PhonePe and others", neo=[1, "Swiggy on Mastercard; others not."], src=[["HDFC Bank: credit cards", CCLIST], ["Q2 FY27 results release, 17 Oct 2026", Q2PR]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at HDFC Bank", "blurb": "One network of four.", "products": [
        P("mcathdfc", "Mastercard at HDFC Bank", "HDFC runs Visa, Mastercard, RuPay and Diners Club side by side. Mastercard carries the Swiggy co-brands (March 2026), launched the Millennia range in 2019, tokenised HDFC cards on Google Pay (2021) and backed a US$100 million MSME facility (2021); Visa has Pixel and the FIFA 2026 card, and RuPay takes the UPI credit cards. No network split is published ⚠.",
          s=["card"], div="cards", rev="retail", mc="The relationship this map is drawn for.",
          src=[["Annual Report 2025-26", AR26], ["Angel One: Swiggy BLCK and ORNGE, Mar 2026", SWIGGY26], ["Mastercard: MSME facility, Oct 2021", DFC]]),
    ]},
    {"id": "pillar-market", "name": "Indian payments", "blurb": "Network choice, UPI, RuPay.", "products": [
        P("market", "The Indian market", "Since 6 September 2024, issuers with more than 10 lakh cards must offer a choice of network and cannot sign exclusive deals; the RBI barred Mastercard from new cardholders from July 2021 to June 2022 and HDFC from new cards from December 2020 to August 2021; UPI runs at 802 million payments a day and charges merchants 0.4% above ₹2,000 from 15 October 2026.",
          s=["con"], div="bank", rev="other",
          src=[["Business Today: network choice, Sep 2024", CHOICE], ["Business Standard: Mastercard curbs lifted, Jun 2022", MCBAN], ["Business Standard: HDFC card curbs lifted, Aug 2021", HDFCBAN], ["HDFC Bank: new UPI rules 2026", UPIMDR], ["StartupTalky: UPI Sep 2026", UPISEP]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
