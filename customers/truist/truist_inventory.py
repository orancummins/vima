"""Truist Financial's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Truist's own unless a source says otherwise: the 3Q26 results (16 October 2026), the 1Q26 and
2Q26 decks, the 4Q25 deck (21 January 2026) and the 2025 Form 10-K. ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

IR = "https://ir.truist.com/download/"
Q3REL = IR + "TFC_3Q26_Earnings_Release.pdf"
Q3DECK = IR + "TFC_3Q26_Earnings_Deck.pdf"
Q2DECK = IR + "TFC_2Q26_Earnings_Deck.pdf"
Q1DECK = IR + "TFC_1Q26_Earnings_Deck.pdf"
Q4DECK = IR + "TFC_4Q25_Earnings_Deck.pdf"
K10 = IR + "TFC_2025_Form_10-K.pdf"
LEAD = "https://ir.truist.com/2026-10-16-Truist-announces-leadership-appointments"
CEO = "https://ir.truist.com/2026-06-15-Truist-announces-Michael-P-Lyons-as-incoming-CEO"
DIVE = "https://bankingdive.com/news/truist-ceo-lyons-rogers-fiserv/822878/"
MCAP = "https://stockanalysis.com/stocks/tfc/market-cap/"
MEDIA = "https://media.truist.com/"
TIH = MEDIA + "2024-05-07-Truist-completes-sale-of-Truist-Insurance-Holdings-and-executes-strategic-balance-sheet-repositioning"
AIDATA = MEDIA + "2025-11-19-Truist-names-Pascal-Belaud-as-chief-AI-data-officer"
BRANCH = MEDIA + "2025-08-20-Truist-announces-significant-multi-year-investment-in-high-growth-markets"
OPENB = MEDIA + "2026-02-12-Truist-launches-secure-open-banking-experience"
INSIGHTS = MEDIA + "2026-09-03-Truist-delivers-2-billion-AI-powered-proactive-insights-helping-clients-move-forward-with-confidence"
DDS = MEDIA + "2025-12-18-Truist-streamlines-digital-account-opening-with-direct-deposit-switching"
VINF = MEDIA + "2025-10-02-Truists-Visa-Infinite-launch-sets-new-super-regional-standard-for-premium-small-business-cards"
ENGAGE = MEDIA + "2025-07-08-Truist-Merchant-Engage-powers-SMB-growth-in-banks-latest-payments-suite-expansion"
RTP = MEDIA + "2025-04-25-Truist-first-bank-to-begin-revolutionizing-bill-pay-with-alias-based-request-for-payment-via-the-RTP-R-network"
PAYVET = MEDIA + "2025-10-14-Truist-taps-payments-veterans-to-accelerate-growth-in-competitive-wholesale-market"
CRYPTO = MEDIA + "2026-02-25-Truist-Wealth-expands-investment-solutions-with-cryptocurrency"
SHEFF = MEDIA + "2026-02-18-Sheffield-Financial,-Mercury-Marine-launch-financing-partnership-for-outboard-engines-and-boat-packages"
BUYBACK = MEDIA + "2025-12-16-Truist-Announces-New-10B-Common-Stock-Repurchase-Program"
CARDS = "https://www.truist.com/credit-cards"
DEBIT = "https://www.truist.com/checking/debit-cards"
DELTA = "https://www.truist.com/content/dam/truist-bank/us/en/documents/truist-delta-sky-miles-faqs.pdf"
SBCC = "https://www.truist.com/small-business/credit-cards"
GIFT = "https://truist.com/prepaid-cards/gift-card"
ONECARD = "https://truist.com/commercial-corporate-institutional/manage-cash-flow/credit-cards/one-card"
EPAY = "https://truist.com/commercial-corporate-institutional/manage-cash-flow/credit-cards/epayables"
MCGUIDE = "https://www.truist.com/content/dam/truist-bank/us/en/documents/guides-benefits/cci/guide-to-benefits-truist-mastercard-commercial.pdf"
TRINITY = "https://discover.trinitydc.edu/business/creditcards"
MERCH = "https://www.truist.com/small-business/merchant-services"
DTENGAGE = "https://www.digitaltransactions.net/truists-merchant-engage-combines-banking-and-payments-in-one/"
POLLMC = "https://www.crowdfundinsider.com/2020/08/165287-mastercard-announces-global-commercial-partnership-with-pollinate/"
NILSON = "https://nilsonreport.com/articles/global-payments-gets-truist-credit-card-processing/"
TSYS = "https://investors.globalpayments.com/news-events/press-releases/detail/53/global-payments-to-provide-credit-card-processing-services"
ZLUSD = "https://eco.com/support/en/articles/15705713-zlusd-bank-partners-the-7-banks-behind-zelle-s-stablecoin"
ZINDIA = "https://apnews.com/article/zelle-india-payments-banking-7b6299bcd9926f6d0a2533da5591d2a8"
ONEVIEW = "https://ffnews.com/newsarticle/truist-debuts-one-view-connect-pilot-enabling-multi-platform-erp-banking-for-wholesale-clients/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · charter · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a $554 billion balance sheet, a new CEO from Fiserv since September 2026, a charter from 1872 and the BB&T–SunTrust merger, AI built into the client experience, and a franchise review that has already sold two lending books.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "$554 billion, ROTCE 14.6% adjusted.", "div": "tfc", "rev": "otc", "products": [
            P("balance", "Balance sheet", "Total assets of $554 billion, loans of $323.9 billion and deposits of $413.2 billion at 30 September 2026; CET1 10.7%.",
              s=["corp"], neo=[0, ""], src=[["3Q26 earnings release", Q3REL]]),
            P("earnings", "Earnings", "2025: net income to common of $4.97 billion, EPS $3.82, revenue $20.5 billion, ROTCE 12.7%. 3Q26: EPS $0.56 reported and $1.16 adjusted, after a $1.4 billion securities loss and the RAC loan sale; adjusted ROTCE 14.6%.",
              s=["corp"], neo=[0, ""], src=[["3Q26 earnings deck", Q3DECK], ["4Q25 earnings deck", Q4DECK]]),
            P("ratings", "Ratings & market value", "Truist Financial rated Baa1, A- and A by Moody's, S&P and Fitch; Truist Bank A3, A and A; all stable at end-2025. Market value about $56 billion at 16 October 2026 ⚠.",
              s=["corp"], neo=[0, ""], src=[["2025 Form 10-K", K10], ["StockAnalysis: market cap", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Lyons in, Rogers to chair.", "div": "tfc", "rev": "otc", "products": [
            P("leadership", "CEO & executive team", "Mike Lyons, ex-Fiserv CEO and ex-PNC president, became CEO on 1 September 2026; Bill Rogers is executive chair until April 2027. CFO Mike Maguire, wholesale chief Kristin Lesher. In October 2026 Dontá Wilson left, and Shimna Sameer (consumer), Jeff Warner (small business) and Steve Boland (vice chair) were named.",
              s=["corp"], st="flux", ay="Sep 2026", neo=[0, ""], src=[["Truist: Lyons named CEO, Jun 2026", CEO], ["Truist: leadership appointments, Oct 2026", LEAD]]),
            P("board", "Board", "Thomas Skains is lead independent director; the board's succession process chose an outside CEO for the first time since the 2019 merger.",
              s=["corp"], neo=[0, ""], src=[["Banking Dive: Lyons to Truist, Jun 2026", DIVE]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & footprint", "blurb": "BB&T and SunTrust, 1872.", "div": "bank", "rev": "csbb", "products": [
            P("heritage", "BB&T and SunTrust", "Formed in late 2019 by merging BB&T of Winston-Salem and SunTrust of Atlanta; Truist Bank was chartered in 1872 and is the oldest bank headquartered in North Carolina.",
              s=["con"], o="I", neo=[0, ""], src=[["2025 Form 10-K", K10], ["Banking Dive: Lyons to Truist, Jun 2026", DIVE]]),
            P("footprint", "Southeast & Mid-Atlantic footprint", "Number one by deposits in Georgia, number two in North Carolina, third in Virginia, Maryland and South Carolina, fourth in Florida (22% of deposits); 38,711 teammates at end-2025.",
              s=["con"], neo=[0, ""], src=[["2025 Form 10-K", K10]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "A chief AI officer from Microsoft.", "div": "tfc", "rev": "otc", "products": [
            P("tech", "Technology & processing", "CIO Steve Hagerman; Pascal Belaud, ex-Microsoft, chief AI & data officer since November 2025; credit cards processed by TSYS on TS2 under a 2020 agreement.",
              s=["corp"], ay="Nov 2025", o="P", at="TSYS", neo=[0, "TSYS processing."], src=[["Truist: chief AI & data officer", AIDATA], ["Global Payments: TSYS for Truist, May 2020", TSYS]]),
            P("aiprog", "AI in numbers", "Truist Assist handled 12.5 million requests since 2023, 9 million end to end by AI; GenAI wrote 3.4 million care-centre call summaries in 1Q26.",
              s=["con"], st="new", neo=[0, ""], src=[["1Q26 earnings deck", Q1DECK]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & portfolio review", "blurb": "15% ROTCE in 2027.", "div": "tfc", "rev": "otc", "products": [
            P("strategy", "Strategy & targets", "Become 'the most important financial partner' to clients: 15% ROTCE in 2027 and 16–18% long term, a franchise review to move capital to the best businesses, a flatter organisation and a $10 billion buyback.",
              s=["corp"], st="new", neo=[0, ""], src=[["3Q26 earnings deck", Q3DECK], ["1Q26 earnings deck", Q1DECK], ["Truist: $10bn buyback", BUYBACK]]),
            P("portfolio", "Deals & disposals", "Sold Truist Insurance Holdings (May 2024, about $10.1 billion after tax) and Sterling Capital (July 2024); sold the $5.5 billion RAC auto book (3Q26) and agreed to sell $7.7 billion of LightStream loans to Carlyle (14 October 2026).",
              s=["corp"], st="flux", ay="Oct 2026", neo=[0, ""], src=[["Truist: TIH sale completed", TIH], ["3Q26 earnings deck", Q3DECK]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Visa debit and the Delta debit card ending this month, Visa credit and a Visa Business Infinite card, commercial cards on Visa and Mastercard, Merchant Engage on Pollinate, Zelle and RTP, treasury, and a share in a Zelle stablecoin.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit & prepaid", "blurb": "Visa debit.", "div": "bank", "rev": "csbb", "products": [
            P("debit", "Truist debit cards", "'Visa bank debit cards' with contactless, phone wallets, spending controls, lock and unlock in Truist Mobile and custom images; debit and credit spend of $32 billion in 3Q26.", short="Debit (Visa)",
              s=["con", "sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Truist: debit cards", DEBIT], ["3Q26 earnings deck", Q3DECK]]),
            P("delta", "Truist Delta SkyMiles debit card", "No new cards since 10 November 2025; the programme ends on 31 October 2026 and cards are replaced by standard Truist debit cards.",
              s=["con"], lc="everyday", st="retired", ay="Oct 2026", o="P", at="Delta", neo=[None, "Network not stated ⚠."], src=[["Truist: Delta SkyMiles debit FAQs", DELTA]]),
            P("prepaid", "Truist Visa gift cards", "Prepaid gift cards usable wherever Visa is accepted in the US.",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Truist: gift cards", GIFT]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "All Visa.", "div": "bank", "rev": "csbb", "products": [
            P("enjoy", "Truist Enjoy, Future & Secured cards", "Enjoy Cash (3-2-1% or 1.5%), Enjoy Beyond ($95, 3x travel), Enjoy Travel, Future (low rate) and Enjoy Cash Secured, sold to existing clients only; card loans about $4.9 billion.", short="Consumer credit (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              mc="Before conversion the credit book was Visa and Mastercard; today's range is all Visa ⚠.",
              src=[["Truist: credit cards", CARDS], ["2025 Form 10-K", K10], ["Nilson Report: TSYS for Truist, May 2020", NILSON]]),
            P("bizcards", "Business Cash Rewards & Business Premium Visa Infinite", "Small business cards on Visa; the Business Premium Visa Infinite (October 2025, $299, 2% cash back plus a 10% bonus, lines of $15,000–$100,000) made Truist the first super-regional bank with Visa Business Infinite.", short="Small business credit (Visa)",
              s=["sme"], lc="borrow", st="new", ay="Oct 2025", o="P", at="Visa", neo=[0, "Visa."], src=[["Truist: Visa Infinite launch, Oct 2025", VINF], ["Truist: small business cards", SBCC]]),
        ]},
        {"id": "2.3", "ic": "briefcase-business", "name": "Commercial cards", "blurb": "Visa and Mastercard.", "div": "payments", "rev": "wb", "products": [
            P("commcards", "Truist One Card, Corporate & Purchasing cards", "Travel, entertainment and purchasing cards with spending limits, merchant blocks, receipts online and pooled rewards; the pages carry both a Visa and a Truist Mastercard commercial benefits guide, and one university's Truist cards carry Mastercard ⚠.", short="Commercial cards (Visa & Mastercard)",
              s=["corp", "sme"], lc="move", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard; split not published ⚠."],
              mc="Mastercard's main card foothold at Truist.",
              src=[["Truist: One Card", ONECARD], ["Truist: Mastercard commercial benefits guide", MCGUIDE], ["Trinity Washington University: cards", TRINITY]]),
            P("epayables", "Truist ePayables", "Virtual-card supplier payments for commercial clients, with the same Visa and Mastercard benefit guides ⚠.",
              s=["corp"], lc="move", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard ⚠."], src=[["Truist: ePayables", EPAY]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acceptance", "blurb": "Merchant Engage on Pollinate.", "div": "payments", "rev": "wb", "products": [
            P("merchant", "Truist merchant services", "In-store, online and mobile acceptance, next-day funding into Truist checking and Truist Merchant Connection reporting; the processor is not named ⚠.",
              s=["sme"], lc="move", neo=[1, "Accepts every network."], src=[["Truist: merchant services", MERCH]]),
            P("engage", "Truist Merchant Engage", "One platform for business banking and merchant services, powered by Pollinate (its first US bank), rolled out from June 2025 to early 2026 and free to merchant clients. Mastercard invested in Pollinate in 2019 and partnered with it in 2020.",
              s=["sme"], lc="move", st="new", ay="Jul 2025", o="P", at="Pollinate", neo=[1, "Pollinate is Mastercard-backed ⚠."],
              mc="A Mastercard-backed engine under Truist's SMB acquiring.",
              src=[["Truist: Merchant Engage, Jul 2025", ENGAGE], ["Digital Transactions: Merchant Engage", DTENGAGE], ["Crowdfund Insider: Mastercard and Pollinate, Aug 2020", POLLMC]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Real-time & P2P", "blurb": "Zelle owner, RTP first.", "div": "bank", "rev": "csbb", "products": [
            P("zelle", "Zelle", "Truist is one of seven bank owners of Early Warning Services, which runs Zelle and the Paze wallet; Zelle transactions grew 12% year on year in 1Q26.",
              s=["con", "sme"], lc="move", o="P", at="Early Warning Services", neo=[0, "Zelle."], src=[["1Q26 earnings deck", Q1DECK], ["eco: the seven banks behind Zelle", ZLUSD]]),
            P("rtp", "RTP Request for Payment", "In April 2025 Truist became the first institution to send and receive alias-based Requests for Payment and settle them over The Clearing House's RTP network, piloted on its own credit card bills.",
              s=["corp", "con"], lc="move", st="new", ay="Apr 2025", o="P", at="The Clearing House", neo=[0, "RTP."], src=[["Truist: RTP Request for Payment, Apr 2025", RTP]]),
        ]},
        {"id": "2.6", "ic": "arrow-left-right", "name": "Treasury & Enterprise Payments", "blurb": "Fees up 14%.", "div": "payments", "rev": "wb", "products": [
            P("treasury", "Treasury management", "Enterprise Payments under Chris Ward: treasury management fees up 14% a year to June 2025, payments sales teams up more than 20%, and wholesale payments fees of about $468 million in 2025 ⚠.",
              s=["corp"], lc="move", neo=[0, ""], src=[["Truist: payments hires, Oct 2025", PAYVET], ["4Q25 earnings deck", Q4DECK]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Digital money", "blurb": "ZelleUSD, bitcoin ETFs.", "div": "tfc", "rev": "otc", "products": [
            P("zelleusd", "ZelleUSD stablecoin", "Early Warning, which Truist co-owns, unveiled a dollar stablecoin on 11 June 2026, with Zelle going to India first ⚠.",
              s=["con"], lc="move", st="new", ay="Jun 2026", o="P", at="Early Warning Services", neo=[0, "EWS stablecoin ⚠."], src=[["eco: ZelleUSD banks", ZLUSD], ["AP: Zelle to India, Jun 2026", ZINDIA]]),
            P("crypto", "Spot bitcoin ETFs", "Since February 2026 Truist Wealth advisers and Truist Trade offer Fidelity and BlackRock spot bitcoin ETFs.",
              s=["prem"], lc="grow", st="new", ay="Feb 2026", o="P", at="Fidelity, BlackRock", neo=[0, ""], src=[["Truist: bitcoin ETFs, Feb 2026", CRYPTO]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: open banking on Mastercard's platform, 2 billion AI insights and an assistant answering 2 million chats a quarter, fraud and identity checks, and Truist Deals cashback.",
    "tiles": [
        {"id": "3.1", "ic": "plug", "name": "Open banking & switching", "blurb": "Mastercard first.", "div": "bank", "rev": "csbb", "products": [
            P("openbanking", "Open banking on Mastercard", "Launched 12 February 2026: consumer and small business clients connect fintech apps through Mastercard's open finance platform, Truist's first direct API integration, with tokenised access and control over what each app sees.", short="Open banking (Mastercard)",
              s=["con", "sme"], lc="open", st="new", ay="Feb 2026", o="P", at="Mastercard", neo=[3, "Mastercard open finance."],
              mc="Mastercard's newest and clearest role at Truist.",
              src=[["Truist: open banking launch, Feb 2026", OPENB]]),
            P("dds", "Direct deposit switching", "Built with Atomic into digital account opening from August 2025; 19% of applicants who used it moved their pay.",
              s=["con"], lc="open", st="new", ay="Aug 2025", o="P", at="Atomic", neo=[0, "Atomic."], src=[["Truist: direct deposit switching, Dec 2025", DDS]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI insights & assistant", "blurb": "2 billion insights.", "div": "bank", "rev": "csbb", "products": [
            P("insights", "Truist Insights", "More than 2 billion personalised insights since 2023 on cash flow, subscriptions, duplicate charges and balances, now inside account pages, Truist Assist and push alerts; rated 4.5 by clients.",
              s=["con", "sme", "prem"], lc="everyday", st="new", neo=[0, ""], src=[["Truist: 2 billion insights, Sep 2026", INSIGHTS]]),
            P("assist", "Truist Assist", "An AI assistant with hand-off to staff: about 440,000 conversations a month in late 2025 and 2.0 million chats in 3Q26, up 54%.",
              s=["con"], lc="everyday", neo=[0, ""], mc="Agent Pay and tokens are open ground for an assistant at this scale.",
              src=[["Truist: direct deposit switching, Dec 2025", DDS], ["3Q26 earnings deck", Q3DECK]]),
            P("pulse", "Truist Client Pulse", "A patent-pending AI tool, in pilot, that reads client feedback across millions of conversations for trends.",
              s=["con"], lc="everyday", st="new", neo=[0, ""], src=[["Truist: direct deposit switching, Dec 2025", DDS]]),
        ]},
        {"id": "3.3", "ic": "shield-check", "name": "Fraud & identity", "blurb": "AI models, ID checks.", "div": "bank", "rev": "csbb", "products": [
            P("fraud", "Fraud prevention & ID verification", "A digital and in-branch ID verification tool and AI models that watch account opening and payments for anomalies and malware; vendors not named ⚠.",
              s=["con", "sme"], lc="open", neo=[None, "Vendors not named."], mc="Zelle and RTP growth raise the stakes for scam scoring.",
              src=[["Truist: growth investment, Aug 2025", BRANCH]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Offers & rewards", "blurb": "Truist Deals.", "div": "bank", "rev": "csbb", "products": [
            P("offers", "Truist Deals", "Cashback offers for personal credit cards and personal and business debit cards, with no fee; the provider is not named ⚠.",
              s=["con", "sme"], lc="everyday", neo=[None, "Provider not named ⚠."], src=[["Truist: debit cards", DEBIT]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What clients buy: Truist One and Premier banking, small business banking, mortgages and specialty consumer lending (with two books just sold), commercial, corporate and investment banking, and Truist Wealth with $348 billion of client assets.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "Everyday & Premier banking", "blurb": "$216 billion of deposits.", "div": "bank", "rev": "csbb", "products": [
            P("checking", "Truist One checking & savings", "Consumer deposits of about $216 billion in 3Q26; 72,000 net new checking accounts in 2025.",
              s=["con"], lc="everyday", neo=[0, "Visa debit."], src=[["3Q26 earnings deck", Q3DECK], ["4Q25 earnings deck", Q4DECK]]),
            P("premier", "Premier Banking", "The mass-affluent focus: Premier new deposit production up 20% a year to 2Q26, with more Premier advisers and financial planning.",
              s=["prem"], lc="grow", neo=[0, ""], src=[["2Q26 earnings deck", Q2DECK]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "Small business", "blurb": "A new chief from PNC.", "div": "bank", "rev": "csbb", "products": [
            P("smallbiz", "Small business banking", "Deposits, loans, Visa cards and merchant services for small firms; Jeff Warner joins from PNC to run it.",
              s=["sme"], lc="everyday", st="flux", neo=[0, "Visa cards."], src=[["Truist: leadership appointments, Oct 2026", LEAD], ["2025 Form 10-K", K10]]),
        ]},
        {"id": "4.3", "ic": "house", "name": "Home & consumer lending", "blurb": "Two books sold.", "div": "lending", "rev": "csbb", "products": [
            P("mortgage", "Mortgages & home equity", "Residential mortgages and home-equity lines in the footprint; mortgage banking income of $113 million in 3Q26.",
              s=["borrow"], lc="borrow", neo=[0, ""], src=[["3Q26 earnings release", Q3REL], ["2025 Form 10-K", K10]]),
            P("sheffield", "Sheffield Financial", "Powersports, outdoor-equipment and marine finance through manufacturers such as Polaris, BRP, Kawasaki, Triumph and Mercury Marine (February 2026).",
              s=["borrow", "dealer"], lc="borrow", o="P", neo=[0, ""], src=[["Truist: Sheffield and Mercury Marine, Feb 2026", SHEFF], ["2025 Form 10-K", K10]]),
            P("servicefinance", "Service Finance", "Point-of-sale loans for home improvements and other purchases, made through contractors and dealers.",
              s=["borrow", "dealer"], lc="borrow", o="A", neo=[0, ""], src=[["2025 Form 10-K", K10]]),
            P("lightstream", "LightStream", "National online unsecured lending; $7.7 billion of loans to be sold to Carlyle, closing in 4Q26.",
              s=["borrow"], lc="borrow", st="flux", ay="Oct 2026", neo=[0, ""], src=[["3Q26 earnings release", Q3REL]]),
            P("rac", "Regional Acceptance", "Non-prime auto lending; the $5.5 billion book was sold for $5.2 billion in 3Q26.",
              s=["borrow"], lc="borrow", st="retired", ay="Sep 2026", neo=[0, ""], src=[["3Q26 earnings deck", Q3DECK]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Commercial, corporate & IB", "blurb": "$194 billion of loans.", "div": "securities", "rev": "wb", "products": [
            P("commercial", "Commercial & corporate banking", "Middle-market and industry teams (energy, technology, hospitals, higher education, government, sponsors and family offices); Wholesale loans of about $194 billion in 3Q26.",
              s=["corp"], lc="borrow", neo=[1, "Commercial cards partly Mastercard."], src=[["3Q26 earnings deck", Q3DECK], ["2025 Form 10-K", K10]]),
            P("cre", "Commercial real estate", "CRE lending inside Wholesale Banking.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["2025 Form 10-K", K10]]),
            P("securities", "Truist Securities", "Investment banking and capital markets: $324 million of income in 3Q26.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["3Q26 earnings release", Q3REL]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "Truist Wealth", "blurb": "$348 billion of client assets.", "div": "wealth", "rev": "wb", "products": [
            P("wealth", "Truist Wealth", "Private wealth, brokerage and trust: record income of $407 million in 3Q26 and $348 billion of client assets; Jeff Dunn and Bryan Cram lead it for now.",
              s=["prem"], lc="grow", st="flux", neo=[0, ""], src=[["3Q26 earnings release", Q3REL], ["Truist: leadership appointments, Oct 2026", LEAD]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How clients reach Truist: Truist Mobile for 5.4 million active users, 1,912 branches with 100 more coming, One View for companies, and dealers and contractors for consumer loans.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Truist Mobile & online", "blurb": "71% of transactions.", "div": "bank", "rev": "csbb", "products": [
            P("app", "Truist Mobile & online banking", "5.4 million active mobile users in 2Q26; digital transactions were 71% of the total in 3Q26 and 349 million in 2025.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["2Q26 earnings deck", Q2DECK], ["3Q26 earnings deck", Q3DECK], ["4Q25 earnings deck", Q4DECK]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & advisers", "blurb": "1,912 branches.", "div": "bank", "rev": "csbb", "products": [
            P("branches", "Branches & ATMs", "1,912 branches and 2,790 ATMs at 30 September 2026; 100 new branches and 300+ renovations over five years in Atlanta, Austin, Charlotte, Dallas, Miami, Orlando, Philadelphia and Washington.",
              s=["con", "prem"], lc="everyday", st="new", neo=[0, ""], src=[["3Q26 earnings deck", Q3DECK], ["Truist: growth investment, Aug 2025", BRANCH]]),
            P("advisors", "Premier advisers & care centres", "More Premier advisers, a virtual sales centre turned to mass-affluent clients, and care centres using GenAI call summaries.",
              s=["prem"], lc="grow", neo=[0, ""], src=[["Truist: growth investment, Aug 2025", BRANCH], ["1Q26 earnings deck", Q1DECK]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "Truist One View", "blurb": "Banking inside the ERP.", "div": "payments", "rev": "wb", "products": [
            P("oneview", "Truist One View & One View Connect", "The wholesale portal; One View Connect (pilot from October 2025) puts treasury inside NetSuite, Sage Intacct, Workday and Dynamics 365 ⚠.",
              s=["corp"], lc="move", st="new", ay="Oct 2025", neo=[0, ""], src=[["FF News: One View Connect, Oct 2025", ONEVIEW]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Dealers & partners", "blurb": "Point-of-sale lending.", "div": "lending", "rev": "csbb", "products": [
            P("dealers", "Dealers, manufacturers & contractors", "Sheffield's manufacturer programmes and Service Finance's contractors and dealers bring Truist loans to the point of sale.",
              s=["dealer", "borrow"], lc="borrow", neo=[0, ""], src=[["Truist: Sheffield and Mercury Marine, Feb 2026", SHEFF], ["2025 Form 10-K", K10]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Truist", "blurb": "Open banking, commercial cards.", "products": [
        P("mcattruist", "Mastercard at Truist", "Truist's consumer debit, consumer credit, small business cards and gift cards are Visa. Mastercard carries part of the commercial card book, is Truist's first open banking partner (February 2026), and backs Pollinate, which runs Truist Merchant Engage ⚠.",
          s=["corp"], div="tfc", rev="otc", mc="The relationship this map is drawn for.",
          src=[["Truist: open banking launch, Feb 2026", OPENB], ["Truist: Mastercard commercial benefits guide", MCGUIDE], ["Truist: Visa Infinite launch, Oct 2025", VINF]]),
    ]},
    {"id": "pillar-market", "name": "US banking", "blurb": "Interchange caps, stablecoins.", "products": [
        P("market", "The US market", "A top-10 US commercial bank against JPMorgan, Bank of America, Wells Fargo and PNC; a 2023 Fed proposal to cut the debit interchange cap, Illinois' interchange law from July 2026, and stablecoins and tokenisation named as threats.",
          s=["corp"], div="tfc", rev="otc", src=[["2025 Form 10-K", K10]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
