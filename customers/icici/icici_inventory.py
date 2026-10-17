"""ICICI Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the Q1 FY27 investor presentation (18 July 2026) and
the Annual Report 2025-26 (18 July 2026), both filed on BSE, and the card pages on ``icici.bank.in``. Q2 FY27 is
not yet reported. ICICI issues many cards on two networks at once (Mastercard with Amex, or Visa with RuPay);
no split by network is published. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own
product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q1PPT = "https://www.bseindia.com/xml-data/corpfiling/AttachHis/881c8fc3-a4c2-40ff-bacf-d68efc0e3d7a.pdf"
AR26 = "https://www.bseindia.com/xml-data/corpfiling/AttachHis/d0771b18-4b9c-4297-abba-6acbf99ae4a9.pdf"
CALL = "https://www.marketbeat.com/earnings/reports/2026-7-19-icici-bank-limited-stock/"
BOARD = "https://www.icici.bank.in/about-us/board-of-directors"
RATING = "https://www.icici.bank.in/about-us/credit-rating"
MCAP = "https://www.5paisa.com/index.php/blog/icici-bank-stock-update-1-oct-26"
CCLIST = "https://www.icici.bank.in/personal-banking/cards/credit-card"
AMAZON = "https://www.icici.bank.in/personal-banking/cards/credit-card/amazon-pay-credit-card"
AMZ1M = "https://www.icici.bank.in/about-us/news-room/2020/news-amazon-pay-icici-bank-credit-card-is-fastest-to-cross-1-million-milestone"
AMZ2M = "https://www.icici.bank.in/about-us/news-room/2021/news-amazon-pay-icici-bank-credit-card-onboards-over-two-million-customers"
RUPAYUPI = "https://www.icici.bank.in/about-us/article/press-release-icici-bank-introduces-upi-payments-via-rupay-credit-cards"
RUPAYCC = "https://www.icici.bank.in/personal-banking/cards/credit-card/rupay-credit-card"
CORALRUPAY = "https://www.icici.bank.in/personal-banking/cards/credit-card/coral-rupay-card"
CORAL = "https://www.icici.bank.in/personal-banking/cards/credit-card/coral-credit-card"
RUBYX = "https://www.icici.bank.in/personal-banking/cards/credit-card/rubyx-credit-card"
SAPPHIRO = "https://www.icici.bank.in/personal-banking/cards/credit-card/sapphiro-card"
EMERALDE = "https://www.icici.bank.in/personal-banking/cards/credit-card/emeralde-credit-card"
EPM = "https://www.icici.bank.in/personal-banking/cards/credit-card/emeralde-private-metal-credit-card"
TIMESBLACK = "https://www.icici.bank.in/personal-banking/cards/credit-card/times-black-icici-credit-card"
R1838 = "https://www.icici.bank.in/personal-banking/cards/credit-card/1838-reserve-icici-credit-card"
R1838NEWS = "https://cardinsider.com/blog/1838-reserve-icici-bank-credit-card-launched/"
MMT = "https://www.icici.bank.in/personal-banking/cards/credit-card/makemytrip/makemytrip-icici-credit-card"
ADANI = "https://www.icici.bank.in/personal-banking/cards/credit-card/adani-icici-credit-card/signature-credit-card"
HPCL = "https://www.icici.bank.in/personal-banking/cards/credit-card/hpcl-super-saver"
EMIRATES = "https://www.icici.bank.in/personal-banking/cards/credit-card/emirates-emeralde-credit-card"
DIAMANT = "https://www.icici.bank.in/about-us/news-room/2012/Diamant_card_release"
DEBIT = "https://www.icici.bank.in/personal-banking/cards/debit-card"
BIZCC = "https://www.icici.bank.in/business-banking/cards/business-credit-card"
CORPCARD = "https://www.icici.bank.in/business-banking/cards/corporate-card"
MCCASE = "https://www.mastercard.com/us/en/news-and-trends/Insights/2025/how-icici-bank-used-marketing-services-to-drive-9-75-million-in-incremental-spend.html"
APPLEPAY = "https://www.kotakneo.com/news/sectors/apple-pay-india-axis-bank-hdfc-icici-sbi-card/"
CARDSHARE = "https://www.businesstoday.in/personal-finance/banking/story/who-dominates-indias-credit-card-market-hdfc-bank-leads-cards-sbi-card-tops-spending-539505-2026-06-27"
CHOICE = "https://www.businesstoday.in/amp/personal-finance/news/story/credit-cards-from-sept-6-you-can-choose-your-card-network-from-visa-mastercard-rupay-444649-2024-09-05"
MCBAN = "https://www.business-standard.com/article/finance/rbi-lifts-restrictions-related-to-on-boarding-new-customers-on-mastercard-122061600884_1.html"
UPISEP = "https://startuptalky.com/india-upi-transactions-september-2026/"
UPIMDR = "https://www.hdfc.bank.in/blogs/upi/new-upi-rules-2026"
AGENTPAY = "https://www.paymentsjournal.com/mastercard-advances-agentic-ai-commerce-in-india/"
VISAGFF = "https://stellagent.ai/insights/visa-agentic-commerce-showcase-gff-india"
POS = "https://deccanchronicle.com/business/micro-merchant-adoption-sees-upi-qr-terminals-double-in-five-months-1913708"
FISERV = "https://www.sec.gov/Archives/edgar/data/798354/000079835426000009/fi-20251231.htm"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · governance · scale", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a ₹24 trillion balance sheet earning a 2.5% return on assets, a CEO reappointed to 2028, a group of listed insurers and an asset manager, 124,324 staff, and a 'Bank to BankTech' technology build.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "PAT ₹148bn in Q1 FY27.", "div": "bank", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Q1 FY27 profit after tax ₹148.05 billion (+15.9%), consolidated ₹154.40 billion; NII ₹243.84 billion, NIM 4.36%; deposits ₹18.34 trillion (+14.0%) and advances ₹16.31 trillion (+19.6%) at 30 June 2026; ROA 2.49%, CET1 16.19%, net NPA 0.35%. FY2026 profit ₹501.47 billion.",
              s=["con"], neo=[0, ""], src=[["Q1 FY27 investor presentation, 18 Jul 2026", Q1PPT], ["Q1 FY27 earnings call, 19 Jul 2026", CALL]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Bakhshi reappointed to 2028.", "div": "bank", "rev": "other", "products": [
            P("leadership", "Board & management", "Part-time chairman Pradeep Kumar Sinha; MD & CEO Sandeep Bakhshi since October 2018, reappointed by the board on 17 January 2026 for 4 October 2026 to 3 October 2028 and approved by the RBI on 22 May 2026; executive directors Sandeep Batra, Rakesh Jha and Ajay Kumar Gupta; group CFO Anindya Banerjee.",
              s=["corp"], ay="Oct 2026", neo=[0, ""], src=[["ICICI Bank: board of directors", BOARD], ["Annual Report 2025-26 (AGM notice)", AR26], ["Q1 FY27 earnings call, 19 Jul 2026", CALL]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & listing", "blurb": "NSE, BSE and NYSE.", "div": "bank", "rev": "other", "products": [
            P("listing", "Listing, value & ratings", "Listed on NSE and BSE with ADRs on the NYSE (IBN); ₹1,326 a share and about ₹9.5 lakh crore of market value on 1 October 2026 ⚠; Moody's Baa3 and S&P BBB, domestic AAA; successor to ICICI Limited, which merged into the bank in 2002 ⚠ date.",
              s=["corp"], o="I", neo=[0, ""], src=[["5paisa: share price, 1 Oct 2026", MCAP], ["ICICI Bank: credit ratings", RATING], ["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "'Bank to BankTech'.", "div": "bank", "rev": "other", "products": [
            P("tech", "Technology platforms & AI", "iLens for retail lending (cards added in FY2025, auto loans in FY2026), iCRM, DigiEase onboarding and a move to the bank.in domain; AI and generative AI for fraud detection, onboarding, document extraction and servicing under a board-approved model-risk framework; technology about 11.4% of operating costs.",
              s=["corp"], st="new", o="B", neo=[0, ""],
              mc="An AI build with no agentic-payments partner named yet.",
              src=[["Annual Report 2025-26", AR26], ["Q1 FY27 earnings call, 19 Jul 2026", CALL]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "One Bank, One Team.", "div": "bank", "rev": "other", "products": [
            P("strategy", "Strategy & market position", "'One Bank, One Team', Customer-360° and 'Fair to Customer, Fair to Bank'; growth by micromarkets and ecosystems (MNCs, global capability centres, NRIs, senior citizens); third in Indian credit cards with 16.1% of cards and 16.2% of spend (May 2026).",
              s=["corp"], neo=[0, ""], src=[["Annual Report 2025-26", AR26], ["Business Today: card market, Jun 2026", CARDSHARE]]),
            P("deals", "Group deals 2025-26", "ICICI Securities wholly owned (March 2025); remaining stake in ICICI Merchant Services sold to Fiserv (April 2025); ICICI Prudential AMC listed (19 December 2025) with the bank at 53%; ICICI Pension Fund bought from ICICI Life (January 2026).",
              s=["corp"], o="A", neo=[0, ""], src=[["Annual Report 2025-26", AR26], ["Fiserv 10-K, Feb 2026", FISERV]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: a card book on four networks with most cards issued in pairs, gemstone cards on Mastercard and Amex, co-brands from Amazon Pay on Visa to MakeMyTrip on Mastercard, a Visa super-premium top end, RuPay credit on UPI, debit and commercial cards, and acquiring, FASTag and cross-border rails.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "16.1% of India's cards.", "div": "cards", "rev": "retail", "products": [
            P("cards", "Credit-card franchise", "16.1% of India's credit cards in force and 16.2% of spend (May 2026), third behind HDFC Bank and SBI Card, about 1.9–2.0 crore cards ⚠ own calculation; card loans ₹532 billion at June 2026 (−1.9% y/y); issued on Visa, Mastercard, American Express and RuPay, often two networks per customer.", short="Credit cards (four networks)",
              s=["card"], lc="borrow", o="B", neo=[1, "Shared across four networks."],
              mc="A shrinking card book in a fast-growing bank, and every new card is a choice of network.",
              src=[["Business Today: card market, Jun 2026", CARDSHARE], ["Q1 FY27 investor presentation, 18 Jul 2026", Q1PPT], ["ICICI Bank: credit cards", CCLIST]]),
            P("gemstone", "Coral, Rubyx & Sapphiro", "The Gemstone collection, issued as Mastercard and American Express pairs (dual-network variants with lounge visits per variant); RuPay variants of Coral and Rubyx run on UPI.", short="Gemstone (Mastercard + Amex)",
              s=["card"], lc="borrow", o="B", at="Mastercard, American Express", neo=[1, "Mastercard leg of each pair."],
              mc="Mastercard is the global network on ICICI's core range.",
              src=[["ICICI Bank: Sapphiro", SAPPHIRO], ["ICICI Bank: Coral", CORAL], ["ICICI Bank: Rubyx", RUBYX]]),
            P("emeralde", "Emeralde & Emeralde Private Metal", "Emeralde comes in American Express and Mastercard variants; the invite-only Emeralde Private Metal (₹12,499 fee) carries Mastercard Moments, Mastercard's programme for its cardholders.", short="Emeralde (Mastercard)",
              s=["card"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard; Emeralde also on Amex."],
              src=[["ICICI Bank: Emeralde Private Metal", EPM], ["ICICI Bank: Emeralde", EMERALDE]]),
        ]},
        {"id": "2.2", "ic": "gem", "name": "Super-premium", "blurb": "Times Black and 1838 on Visa.", "div": "cards", "rev": "retail", "products": [
            P("timesblack", "Times Black & 1838 Reserve", "Times Black (₹20,000 fee) and the invite-only 1838 Reserve (₹1,75,000 fee), both issued with Times Internet and Visa; 1838 Reserve was reported launched by 12 October 2026 on Visa Infinite Privilege ⚠.", short="Times Black & 1838 (Visa)",
              s=["card"], lc="borrow", st="new", ay="Oct 2026", o="P", at="Times Internet, Visa", neo=[0, "Visa."],
              mc="ICICI took its newest top-end cards to Visa.",
              src=[["ICICI Bank: 1838 Reserve", R1838], ["ICICI Bank: Times Black", TIMESBLACK], ["CardInsider: 1838 Reserve launched, Oct 2026", R1838NEWS]]),
            P("diamant", "Diamant", "Launched in November 2012 for private-banking clients on the 'MasterCard World platform', part of the Gemstone collection; still offered by invitation ⚠.", short="Diamant (Mastercard)",
              s=["card"], lc="borrow", ay="Nov 2012", o="P", at="Mastercard", neo=[2, "Mastercard World."], src=[["ICICI Bank: Diamant launch, Nov 2012", DIAMANT], ["ICICI Bank: Emeralde Private Metal (card list)", EPM]]),
        ]},
        {"id": "2.3", "ic": "gift", "name": "Co-brand cards", "blurb": "Amazon Pay on Visa.", "div": "cards", "rev": "retail", "products": [
            P("amazonpay", "Amazon Pay ICICI Bank card", "No-fee card launched 'powered by Visa' in October 2018, with up to 5% back on Amazon for Prime members credited to Amazon Pay balance; the fastest co-brand to 1 million (about 1.4 million by October 2020) and 2 million (July 2021); ICICI's page still shows Visa branding.", short="Amazon Pay (Visa)",
              s=["card", "con"], lc="everyday", ay="Oct 2018", o="P", at="Amazon Pay, Visa", neo=[0, "Visa."],
              mc="The biggest digital co-brand, and under the 2024 rule its renewals are a choice of network.",
              src=[["ICICI Bank: Amazon Pay card", AMAZON], ["ICICI Bank: 1 million, Oct 2020", AMZ1M], ["ICICI Bank: 2 million, Jul 2021", AMZ2M]]),
            P("makemytrip", "MakeMyTrip ICICI Bank card", "A travel co-brand offering 'two networks – MasterCard and RuPay', with up to 6% myCash on MakeMyTrip and a 0.99% forex mark-up.", short="MakeMyTrip (Mastercard + RuPay)",
              s=["card"], lc="everyday", o="P", at="MakeMyTrip, Mastercard", neo=[1, "Mastercard with RuPay."],
              mc="Mastercard's clearest ICICI co-brand.",
              src=[["ICICI Bank: MakeMyTrip card", MMT]]),
            P("cobrands", "Adani One, HPCL, Emirates Skywards & CSK", "Airport, fuel, airline and cricket co-brands, mostly in dual-network variants (the site lists pairs as 'Mastercard & Amex | Visa & RuPay'); the network of each pair is not stated ⚠.", short="Other co-brands (pairs ⚠)",
              s=["card"], lc="everyday", o="P", at="Adani One, HPCL, Emirates, Chennai Super Kings", neo=[None, "Pairs not stated ⚠."],
              src=[["ICICI Bank: Adani One card", ADANI], ["ICICI Bank: HPCL Super Saver", HPCL], ["ICICI Bank: Emirates Emeralde", EMIRATES]]),
        ]},
        {"id": "2.4", "ic": "zap", "name": "UPI & RuPay credit", "blurb": "Credit on UPI since 2023.", "div": "bank", "rev": "retail", "products": [
            P("rupayupi", "RuPay credit cards on UPI", "Coral, HPCL Super Saver and Rubyx RuPay credit cards went live on UPI on 1 December 2023 with NPCI, for merchant payments by QR; the MakeMyTrip RuPay card was added later; a Coral RuPay Braille card serves visually impaired customers.", short="UPI credit (RuPay)",
              s=["con", "card"], lc="borrow", ay="Dec 2023", o="P", at="NPCI", neo=[0, "RuPay."],
              mc="RuPay on UPI is the domestic route around the international networks.",
              src=[["ICICI Bank: RuPay on UPI, Dec 2023", RUPAYUPI], ["ICICI Bank: RuPay credit cards", RUPAYCC], ["ICICI Bank: Coral RuPay", CORALRUPAY]]),
            P("upi", "UPI & UPI Lite", "UPI in iMobile with UPI Lite (PIN-free up to ₹1,000) and biometric approval; India ran about 24 billion UPI payments in September 2026, and a 0.4% merchant fee on eligible payments above ₹2,000 applies from 15 October 2026 ⚠.",
              s=["con", "mer"], lc="move", o="P", at="NPCI", neo=[0, "UPI."], src=[["Annual Report 2025-26", AR26], ["StartupTalky: UPI Sep 2026", UPISEP], ["HDFC Bank: new UPI rules 2026", UPIMDR]]),
        ]},
        {"id": "2.5", "ic": "wallet-cards", "name": "Debit & commercial cards", "blurb": "Every network, split unknown.", "div": "biz", "rev": "retail", "products": [
            P("debit", "Debit cards", "Coral and Sapphiro gemstone debit cards, Expressions (175+ designs), RuPay contactless NCMC debit, the Visa Wealth Select Infinite card and a Mastercard World Chip NRI debit card; the split by network is not published ⚠.", short="Debit (RuPay, Visa, Mastercard ⚠)",
              s=["con", "nri"], lc="everyday", o="B", div="bank", neo=[1, "Mastercard on the NRI card and others ⚠."],
              src=[["ICICI Bank: debit cards", DEBIT]]),
            P("bizcards", "Business & corporate cards", "Amex Business Ascent and Essential, Visa Business Advantage Blue, Platinum and Gold business cards, Corporate Platinum and Gold, a Purchase Card for vendor payments and a Central Travel Account card; networks of the corporate range are not stated ⚠.", short="Business & corporate cards (Amex, Visa ⚠)",
              s=["sme", "corp"], lc="everyday", o="B", neo=[None, "Corporate networks not stated ⚠."],
              mc="Purchase and travel cards for a bank chasing MNCs and GCCs are open ground.",
              src=[["ICICI Bank: business credit cards", BIZCC], ["ICICI Bank: corporate cards", CORPCARD]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acquiring & FASTag", "blurb": "Top-ten POS deployer.", "div": "biz", "rev": "wholesale", "products": [
            P("acquiring", "Merchant acquiring & Merchant STACK", "One of the ten banks that deployed 97% of India's POS terminals (December 2024), with Merchant STACK and merchant tools in InstaBIZ; the bank sold the last of its stake in ICICI Merchant Services to Fiserv in April 2025; share of acquiring not published ⚠.", short="Acquiring (all networks)",
              s=["mer"], lc="move", o="B", neo=[1, "Accepts every network."],
              mc="Acquirer risk and merchant data tools fit a top-ten acquirer.",
              src=[["Deccan Chronicle: POS deployers, 2025", POS], ["Q1 FY27 investor presentation, 18 Jul 2026", Q1PPT], ["Annual Report 2025-26", AR26]]),
            P("fastag", "FASTag & embedded payments", "The bank claims a 'leadership position in FASTag' and is extending embedded payments to wider mobility and transit uses.",
              s=["con"], lc="move", o="P", at="NPCI", neo=[0, ""], src=[["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "2.7", "ic": "earth", "name": "Cross-border & NRI", "blurb": "Money2India, GIFT City.", "div": "intl", "rev": "wholesale", "products": [
            P("xborder", "Remittances & trade", "Money2India and Money2World remittances, an IFSC Banking Unit at GIFT City with LRS onboarding, Trade Online and the Trade API suite, six overseas business centres and subsidiaries in the UK and Canada; overseas loans 3.1% of the book.",
              s=["nri", "corp"], lc="move", o="B", neo=[0, ""],
              mc="NRI remittances are a fit for Mastercard Move.",
              src=[["Annual Report 2025-26", AR26], ["Q1 FY27 investor presentation, 18 Jul 2026", Q1PPT]]),
            P("forex", "Forex & travel cards", "Prepaid forex travel cards, now in InstaBIZ, and a Corporate Sapphiro Forex Card; network not stated ⚠.",
              s=["nri", "sme"], lc="move", o="B", neo=[None, "Network not stated ⚠."], src=[["Annual Report 2025-26", AR26], ["ICICI Bank: business credit cards", BIZCC]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account and card: in-house fraud and security controls, wallets and tokens (ICICI is not yet on Apple Pay), generative AI for staff and customers, rewards and EMI, and Mastercard marketing services on debit activation.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Smart Lock, biometric UPI.", "div": "bank", "rev": "retail", "products": [
            P("fraud", "Fraud & cyber defence", "Smart Lock to switch off unused channels, QR login for internet banking, biometric UPI approval and AI fraud detection; the RBI fined the bank ₹97.8 lakh in April 2025, partly over card issuance and conduct rules; no Mastercard fraud product is named in public sources ⚠.",
              s=["con"], lc="everyday", o="B", neo=[0, "ICICI's own."], src=[["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "3.2", "ic": "key-round", "name": "Tokens & wallets", "blurb": "Not on Apple Pay.", "div": "cards", "rev": "retail", "products": [
            P("wallets", "Tokens & phone wallets", "Apple Pay went live in India on 30 September 2026 with Axis Bank only; ICICI, HDFC Bank and SBI Card were not live, with fee terms reported as the obstacle; ICICI's token programmes by network are not public ⚠.",
              s=["card"], lc="everyday", st="flux", ay="Sep 2026", o="P", neo=[None, "Not public ⚠."],
              mc="Mastercard tokens could carry ICICI's Mastercards into Apple Pay.",
              src=[["Kotak Neo: Apple Pay in India, Oct 2026", APPLEPAY]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "AI & servicing", "blurb": "GenAI with a human in the loop.", "div": "bank", "rev": "retail", "products": [
            P("genai", "Generative AI & iPal", "An in-house generative AI tool with a human in the loop, AI call summaries for relationship managers, chatbots and the iPal assistant; ICICI was not named in Mastercard's (February 2026) or Visa's (Global Fintech Fest 2026) India agentic-payment pilots.",
              s=["con", "card"], lc="everyday", st="new", o="B", neo=[0, ""],
              mc="Agent Pay is open ground at ICICI.",
              src=[["Annual Report 2025-26", AR26], ["PaymentsJournal: Agent Pay in India, Feb 2026", AGENTPAY], ["Stellagent: Visa at GFF 2026", VISAGFF]]),
        ]},
        {"id": "3.4", "ic": "coins", "name": "Rewards, EMI & insights", "blurb": "Brands, UPI and EMI.", "div": "cards", "rev": "retail", "products": [
            P("rewards", "Rewards & EMI", "Reward points, Amazon Pay balance and myCash, Culinary Treats and EMI campaigns; the bank says card spend grows through brand partnerships, UPI on credit cards and EMI, with about 70% of the card book with existing customers.",
              s=["card"], lc="grow", o="B", neo=[0, ""], src=[["Q1 FY27 investor presentation, 18 Jul 2026", Q1PPT], ["ICICI Bank: credit cards", CCLIST]]),
            P("mcmarketing", "Mastercard debit-activation campaign", "A Mastercard marketing-services case study (2025): ICICI and Mastercard reworked the early-month-on-book strategy for new debit cards, with about US$9.75 million of incremental spend during and after the campaign ⚠ (read from a search summary; the page blocked fetching).",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[3, "Mastercard Data & Services ⚠."],
              mc="Proof that Mastercard services already work inside ICICI.",
              src=[["Mastercard: ICICI case study, 2025", MCCASE]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: ₹8.1 trillion of retail loans led by ₹5.1 trillion of mortgages, business banking growing 28%, rural and corporate lending, and a group of insurers, an asset manager and a broker.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Mortgages & retail loans", "blurb": "₹8.1trn of retail loans.", "div": "bank", "rev": "retail", "products": [
            P("mortgages", "Mortgages", "₹5.13 trillion at June 2026 (+14.6%), 63.6% of retail loans; about 90% of borrowers already bank with ICICI.",
              s=["home"], lc="borrow", o="B", neo=[0, ""], src=[["Q1 FY27 investor presentation, 18 Jul 2026", Q1PPT]]),
            P("loans", "Personal & vehicle loans", "Personal loans ₹1.36 trillion (+12.9%) and vehicle loans ₹1.02 trillion; originated on the iLens platform.",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["Q1 FY27 investor presentation, 18 Jul 2026", Q1PPT], ["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "Business banking", "blurb": "Up 28% a year.", "div": "biz", "rev": "wholesale", "products": [
            P("bizbank", "Business banking & InstaBIZ", "Loans of ₹3.50 trillion to firms with turnover up to ₹7.5 billion (+28.2%), sourced through branches, InstaBIZ, Merchant STACK, Trade Online and DigiEase.",
              s=["sme"], lc="borrow", o="B", neo=[0, ""],
              mc="Fast-growing small firms are the users of commercial cards.",
              src=[["Q1 FY27 investor presentation, 18 Jul 2026", Q1PPT], ["Annual Report 2025-26", AR26]]),
            P("rural", "Rural & gold loans", "Rural loans ₹1.04 trillion (+35.4%), including Kisan Credit Cards and gold loans; 46,624 rural locations served through business correspondents.",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["Q1 FY27 investor presentation, 18 Jul 2026", Q1PPT], ["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "4.3", "ic": "factory", "name": "Corporate & government", "blurb": "₹3.3trn of corporate loans.", "div": "bank", "rev": "wholesale", "products": [
            P("corporate", "Corporate, MNC & government banking", "Domestic corporate loans ₹3.27 trillion (+18.5%), cash management, Digi Escrow, and coverage of MNCs, global capability centres and government departments.",
              s=["corp"], lc="borrow", o="B", neo=[0, ""], src=[["Q1 FY27 investor presentation, 18 Jul 2026", Q1PPT], ["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Group & wealth", "blurb": "Insurers, AMC, broker.", "div": "life", "rev": "other", "products": [
            P("insurance", "ICICI Prudential Life & ICICI Lombard", "ICICI Life (Q1 FY27 profit ₹3.86 billion, VNB margin 26.7%) and ICICI Lombard (premium ₹83.18 billion, profit ₹4.03 billion).",
              s=["con"], lc="grow", o="B", neo=[0, ""], src=[["Q1 FY27 investor presentation, 18 Jul 2026", Q1PPT]]),
            P("amc", "ICICI Prudential AMC & ICICI Securities", "ICICI Pru AMC (53%, listed 19 December 2025; ₹11.17 trillion of fund assets; profit ₹9.65 billion) and ICICI Securities (wholly owned since March 2025; the 3-in-1 account) for private banking and wealth.",
              s=["con", "nri"], lc="grow", o="B", div="amc", neo=[0, ""], src=[["Q1 FY27 investor presentation, 18 Jul 2026", Q1PPT], ["Annual Report 2025-26", AR26]]),
            P("homefin", "ICICI Home Finance", "A housing-finance subsidiary with ₹335 billion of loans and Q1 FY27 profit of ₹2.00 billion.",
              s=["home"], lc="borrow", o="B", div="hfc", neo=[0, ""], src=[["Q1 FY27 investor presentation, 18 Jul 2026", Q1PPT]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: iMobile and internet banking, InstaBIZ for firms, 7,608 branches with half outside the big cities, NRI channels abroad, and co-brand partners from Amazon to MakeMyTrip.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "iMobile & internet banking", "blurb": "One app strategy.", "div": "bank", "rev": "retail", "products": [
            P("imobile", "iMobile & internet banking", "A reworked iMobile under a 'one app' strategy, with UPI Lite, Smart Lock, digital account servicing and card management; 12 public websites worldwide.",
              s=["con", "card", "nri"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "5.2", "ic": "briefcase-business", "name": "InstaBIZ", "blurb": "Business app since 2019.", "div": "biz", "rev": "wholesale", "products": [
            P("instabiz", "InstaBIZ", "The business-banking app launched in 2019, refreshed in FY2026 with forex travel-card services, SWIFT statements and merchant solutions.",
              s=["sme", "mer"], lc="everyday", ay="2019", o="B", neo=[0, ""], src=[["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & correspondents", "blurb": "7,608 branches.", "div": "bank", "rev": "retail", "products": [
            P("branches", "Branches, ATMs & correspondents", "7,608 branches and 12,190 ATMs and cash recyclers at June 2026 (528 branches added in FY2026), 48.5% semi-urban or rural, plus business correspondents in 46,624 rural locations.",
              s=["con", "sme"], lc="open", o="B", neo=[0, ""], src=[["Q1 FY27 investor presentation, 18 Jul 2026", Q1PPT], ["Annual Report 2025-26", AR26]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partners", "blurb": "Amazon, MakeMyTrip, Adani.", "div": "cards", "rev": "retail", "products": [
            P("partners", "Co-brand & platform partners", "Amazon (sells the card on amazon.in to non-customers), MakeMyTrip, Adani One, HPCL, Emirates, Times Internet and Chennai Super Kings.",
              s=["card"], lc="open", o="P", at="Amazon, MakeMyTrip, Adani One, Times Internet and others", neo=[1, "MakeMyTrip on Mastercard; Amazon and Times on Visa."],
              src=[["ICICI Bank: credit cards", CCLIST], ["ICICI Bank: 2 million, Jul 2021", AMZ2M]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at ICICI Bank", "blurb": "The global leg of the gemstone pairs.", "products": [
        P("mcaticici", "Mastercard at ICICI Bank", "ICICI runs Visa, Mastercard, American Express and RuPay side by side, often two to a customer. Mastercard carries the Mastercard leg of the Coral, Rubyx, Sapphiro and Emeralde pairs (with Amex), Emeralde Private Metal, Diamant (2012), the MakeMyTrip co-brand (with RuPay) and the NRI World debit card, and its marketing services worked on debit activation ⚠. Visa carries Amazon Pay and the Times Black and 1838 Reserve cards; RuPay carries credit on UPI. No split by network is published ⚠.",
          s=["card"], div="cards", rev="retail", mc="The relationship this map is drawn for.",
          src=[["ICICI Bank: Sapphiro", SAPPHIRO], ["ICICI Bank: MakeMyTrip card", MMT], ["ICICI Bank: Amazon Pay card", AMAZON], ["Mastercard: ICICI case study, 2025", MCCASE]]),
    ]},
    {"id": "pillar-market", "name": "Indian payments", "blurb": "Network choice, UPI, RuPay.", "products": [
        P("market", "The Indian market", "Since 6 September 2024, issuers with more than 10 lakh cards must offer a choice of network at issue and renewal and cannot sign exclusive deals; the RBI barred Mastercard from new cardholders from July 2021 to June 2022; India has nearly 12.1 crore credit cards (HDFC 22%, SBI Card 18.6%, ICICI 16.1%); UPI ran about 24 billion payments in September 2026.",
          s=["con"], div="bank", rev="other",
          src=[["Business Today: network choice, Sep 2024", CHOICE], ["Business Standard: Mastercard curbs lifted, Jun 2022", MCBAN], ["Business Today: card market, Jun 2026", CARDSHARE], ["StartupTalky: UPI Sep 2026", UPISEP]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
