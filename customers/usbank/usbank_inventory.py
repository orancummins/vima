"""U.S. Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are U.S. Bancorp's own unless a source says otherwise: the Q3 2026 results (15 October 2026), the
Q4 2025 results (20 January 2026) and the company's press releases. ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q3 = "https://ir.usbank.com/news-events/news/news-details/2026/U-S--Bancorp-Reports-Third-Quarter-2026-Results/default.aspx"
Q3PRES = "https://www.sec.gov/Archives/edgar/data/0000036104/000003610426000054/a3q26earningspresentatio.htm"
FY25 = "https://ir.usbank.com/news-events/news/news-details/2026/U-S--Bancorp-Reports-Fourth-Quarter-2025-Results/default.aspx"
ABOUT = "https://www.usbank.com/about-us-bank.html"
MCAP = "https://stockanalysis.com/stocks/usb/market-cap/"
CHAIR = "https://ir.usbank.com/news-events/news/news-details/2026/U-S--Bancorp-Appoints-Gunjan-Kedia-Chairman-of-the-Board-of-Directors-Effective-in-April-2026/default.aspx"
PAYORG = "https://ir.usbank.com/news-events/news/news-details/2024/U.S.-Bancorp-announces-planned-leadership-structural-changes-for-payments-business/default.aspx"
PMI = "https://ir.usbank.com/news-events/news/news-details/2026/U-S--Bank-Adds-Industry-Veterans-to-Its-Payments-Merchant-and-Institutional-Leadership-Team/default.aspx"
UNION = "https://ir.usbank.com/news-events/news/news-details/2022/U.S.-Bancorp-Completes-Acquisition-of-Union-Bank-12-01-2022/default.aspx"
BTIG = "https://ir.usbank.com/news-events/news/news-details/2026/U-S--Bancorp-Completes-Acquisition-of-BTIG/default.aspx"
BTIGDEAL = "https://ir.usbank.com/news-events/news/news-details/2026/U-S--Bancorp-to-Acquire-BTIG/default.aspx"
DESIGN = "https://www.usbank.com/about-us-bank/news-and-stories/article-library/us-bank-launches-design-assistant-an-ai-solution-to-empower-designers-at-scale.html"
STAT = "https://www.usbank.com/about-us-bank/news-and-stories/article-library/ai-powered-statement-analyzer-simplifies-payment-services-for-small-businesses.html"
DEBIT = "https://www.usbank.com/about-us-bank/news-and-stories/article-library/the-us-bank-visa-debit-card-gets-a-new-look.html"
CREDIT = "https://www.usbank.com/credit-cards.html"
SMARTLY = "https://ir.usbank.com/news-events/news/news-details/2024/U.S.-Bank-unveils-industry-leading-card-savings-combination/default.aspx"
SPLIT = "https://ir.usbank.com/news-events/news/news-details/2025/U-S--Bank-Launches-Split-World-Mastercard/default.aspx"
AMZN = "https://ir.usbank.com/news-events/news/news-details/2026/Amazons-New-Prime-Business-and-Amazon-Business-Credit-Cards-Powered-by-U-S--Bank-and-Mastercard-Are-Now-Available-with-Enhanced-Rewards-and-Flexible-Financing/default.aspx"
AMZNMC = "https://www.usbank.com/about-us-bank/news-and-stories/article-library/amazon-us-bank-and-mastercard-partner-on-new-cards-for-small-businesses.html"
AMZNTX = "https://www.usbank.com/splash/amazon-business/card-transition.html"
AMZNPD = "https://finance.yahoo.com/markets/stocks/articles/u-bank-mastercard-amazons-small-124500210.html"
BMW = "https://ir.usbank.com/news-events/news/news-details/2026/U-S--Bank-and-BMW-Financial-Services-North-America-Launch-Expanded-Benefits-Simplified-Rewards-for-BMW-MINI-and-BMW-Motorrad-Card-Holders-in-the-U-S-/default.aspx"
EJ = "https://ir.usbank.com/news-events/news/news-details/2025/U-S--Bank-Launches-Edward-Jones-Co-Branded-Products-Expanding-Reach-to-Millions-of-New-Customers/default.aspx"
EJAWARD = "https://www.usbank.com/about-us-bank/news-and-stories/article-library/us-bank-receives-2026-innovation-of-the-year-award-for-edward-jones-collaboration.html"
KROGER = "https://www.usbank.com/about-us-bank/news-and-stories/article-library/us-bank-announces-transition-of-kroger-co-brand-card-program.html"
COBRAND = "https://www.usbank.com/credit-cards/co-branded-credit-cards.html"
AAA = "https://ir.usbank.com/news-events/news/news-details/2025/U-S--Bank-AAA---The-Auto-Club-Group-Drive-Credit-Card-Partnership-Into-New-Chapter/default.aspx"
STATEFARM = "https://www.usbank.com/about-us-bank/company-blog/article-library/state-farm-and-us-bank-unveil-new-consumer-and-business-credit-cards.html"
BIZCARDS = "https://www.usbank.com/business-banking/business-credit-cards.html"
ESSENTIALS = "https://ir.usbank.com/news-events/news/news-details/2026/U-S--Bank-Launches-New-Credit-Cards-for-Small-Business-Owners-with-Jessica-Alba-as-Spokesperson/default.aspx"
ALTITUDE23 = "https://ir.usbank.com/news-events/news/news-details/2023/U.S.-Bank-Launches-Business-Altitude-Connect-World-Elite-Mastercard-02-16-2023/default.aspx"
ELAN = "https://www.elanfinancialservices.com/"
FISERV = "https://ir.usbank.com/news-events/news/news-details/2025/U-S--Bank-and-Fiserv-Create-Market-Leading-Integrated-Agent-Card-Issuance/default.aspx"
MCTRAVEL = "https://ir.usbank.com/news-events/news/news-details/2018/U.S.-Bank-Mobile-Payment-Expands-to-Mastercard-Business-Travel-Cards-04-11-2018/default.aspx"
TRAVELBANK = "https://ir.usbank.com/news-events/news/news-details/2023/U.S.-Bank-Unveils-TravelBank-powered-Commercial-Rewards-Card-06-27-2023/default.aspx"
GSA = "https://ir.usbank.com/news-events/news/news-details/2017/U.S.-Bank-Selected-for-U.S.-Government-GSA-SmartPay-3-Payment-Program-09-07-2017/default.aspx"
VOYAGER = "https://ir.usbank.com/news-events/news/news-details/2021/U.S.-Bank-Partners-With-Mastercard-to-Launch-the-U.S.-Bank-Voyager-Mastercard-for-the-Fleet-Industry-08-24-2021/default.aspx"
ELAVON = "https://www.elavon.com/about-elavon.html"
NILSON = "https://ir.usbank.com/news-events/news/news-details/2025/U-S--Banks-Elavon-Jumps-Two-Spots-in-2025-Nilson-Report-Ratings/default.aspx"
MLYN = "https://ir.usbank.com/news-events/news/news-details/2026/Wally-Mlynarski-Named-Elavon-CEO/default.aspx"
ELAVONEU = "https://www.elavon.ie/about-elavon.html"
ELAVONSMB = "https://ir.usbank.com/news-events/news/news-details/2026/Elavon-Launches-New-Industry-Tailored-People-Powered-Payments-Solution-to-Support-Small-Businesses-at-Every-Stage-of-Growth/default.aspx"
ALLINONE = "https://ir.usbank.com/news-events/news/news-details/2026/Elavon-expands-All-In-One-payments-platform-across-North-America-to-power-integrated-commerce/default.aspx"
PAZE = "https://ir.usbank.com/news-events/news/news-details/2024/U.S.-Bank-offers-Paze-for-cardholders-and-merchants/default.aspx"
ZELLE = "https://www.usbank.com/about-us-bank/news-and-stories/article-library/customizing-the-zelle-experience-for-small-business-owners.html"
ENHANCED = "https://ir.usbank.com/news-events/news/news-details/2026/U-S--Bank-Launches-Enhanced-Payments-to-Help-Small-Businesses-Move-Money-Quickly-and-More-Affordably/default.aspx"
USBDC = "https://ir.usbank.com/news-events/news/news-details/2026/U-S--Bank-Launches-USBDC-Stablecoin/default.aspx"
DIGASSETS = "https://ir.usbank.com/news-events/news/news-details/2025/U-S--Bank-establishes-new-Digital-Assets-and-Money-Movement-organization/default.aspx"
ANCHORAGE = "https://ir.usbank.com/news-events/news/news-details/2025/U-S--Bank-selected-to-provide-custody-services-for-reserves-backing-payment-stablecoins-from-Anchorage-Digital-Bank/default.aspx"
PROTECT = "https://ir.usbank.com/news-events/news/news-details/2026/U-S--Bank-expands-consumer-protection-tools-with-new-identity-privacy-and-credit-monitoring-service/default.aspx"
SUBS = "https://ir.usbank.com/news-events/news/news-details/2025/U-S--Bank-Expands-Subscription-Management-for-Credit-Cardholders/default.aspx"
SHIELD = "https://ir.usbank.com/news-events/news/news-details/2026/U-S--Bank-Business-Shield-Visa-Card-Offers-Intro-0-APR-for-up-to-18-Billing-Cycles/default.aspx"
TRAVEL = "https://ir.usbank.com/news-events/news/news-details/2024/U.S.-Bank-Launches-New-Travel-Center-With-Booking.com-for-Credit-Cardholders/default.aspx"
AVVANCE = "https://ir.usbank.com/news-events/news/news-details/2026/U-S--Bank-Avvance-Introduces-New-Longer-Term-Financing-Options/default.aspx"
SINGLEPOINT = "https://ir.usbank.com/news-events/news/news-details/2025/U-S--Bank-rolls-out-new-SinglePoint-experience-to-businesses/default.aspx"
KYRIBA = "https://ir.usbank.com/news-events/news/news-details/2025/U-S--Bank-launches-AI-driven-cash-forecasting-tool/default.aspx"
UPDATION = "https://ir.usbank.com/news-events/news/news-details/2026/Updation-Integrates-With-U-S--Bank-to-Help-Dealerships-Modernize-Payments-and-Financial-Operations/default.aspx"
LEVINE = "https://ir.usbank.com/news-events/news/news-details/2026/U-S--Bank-Names-Eric-Levine-to-Lead-Healthcare-Payments/default.aspx"
BRANCHES = "https://www.usbank.com/about-us-bank/news-and-stories/article-library/us-bank-revamping-branch-network-for-the-digital-age.html"
EJ24 = "https://ir.usbank.com/news-events/news/news-details/2024/U.S.-Bank-Expands-Alliance-Strategy-Announces-Edward-Jones-Partnership/default.aspx"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · charter · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $703 billion of assets and record revenue, a charter from 1863, Gunjan Kedia as chair and CEO, a payments business split in two, and BTIG, USBDC and in-house AI.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "$703bn assets, ROTCE 18.5%.", "div": "usb", "rev": "tcs", "products": [
            P("balance", "Balance sheet & earnings", "The fifth-largest US commercial bank: total assets $703.0 billion at 30 September 2026; record Q3 2026 revenue of $7.97 billion (+8.7%), net income $2.20 billion, ROTCE 18.5%, CET1 10.8%; 2025 net income $7.57 billion on revenue of $28.7 billion; market value about $91.5 billion (16 October 2026); 15 million clients and nearly 70,000 staff.",
              s=["con"], neo=[0, ""], src=[["Q3 2026 results", Q3], ["Q4 2025 results", FY25], ["StockAnalysis: market cap", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Kedia, Runkel and Kelso.", "div": "usb", "rev": "tcs", "products": [
            P("leadership", "Board & managing committee", "Gunjan Kedia, CEO since April 2025 and chair since April 2026; Stephen Philipson runs Wealth, Corporate, Commercial and Institutional Banking; Mark Runkel runs Payments: Merchant and Institutional; Courtney Kelso, ex-American Express, runs Payments: Consumer and Small Business; John Stern is CFO ⚠.",
              s=["corp"], st="flux", neo=[0, ""], src=[["Kedia named chair, Jan 2026", CHAIR], ["Payments split in two, Oct 2024", PAYORG], ["PMI leadership, Feb 2026", PMI]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & deals", "blurb": "Charter 24, Union Bank, BTIG.", "div": "usb", "rev": "wccib", "products": [
            P("heritage", "Charter & acquisitions", "National bank charter No. 24 (1863), headquartered in Minneapolis; MUFG Union Bank's regional franchise added in December 2022; TravelBank, Bento and Salucro bought for payments; BTIG agreed in January 2026 (target price $725 million) and completed on 1 June 2026.",
              s=["corp"], o="A", neo=[0, ""], src=[["U.S. Bank: about us", ABOUT], ["Union Bank completed, Dec 2022", UNION], ["BTIG agreed, Jan 2026", BTIGDEAL], ["BTIG completed, Jun 2026", BTIG]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Built-in-house AI tools.", "div": "bank", "rev": "tcs", "products": [
            P("tech", "AI, data & digital assets platform", "An internal AI Center of Excellence and Design Assistant for every experience designer (December 2025), AI in contact centres, and a Digital Asset Platform built in-house to mint, redeem, freeze and claw back tokens.",
              s=["corp"], st="new", neo=[0, ""], src=[["Design Assistant, Mar 2026", DESIGN], ["USBDC pilot, Sep 2026", USBDC]]),
            P("stat", "Statement Analyzer", "An AI tool, built in-house, that reads a prospect's merchant statements and turns them into pricing proposals for Merchant Payment Services, cutting weeks of analysis to one meeting (May 2026).",
              s=["merch"], lc="move", st="new", ay="May 2026", neo=[0, ""], src=[["Statement Analyzer, May 2026", STAT]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy", "blurb": "Growth, payments, expenses.", "div": "usb", "rev": "tcs", "products": [
            P("strategy", "Three priorities & medium-term targets", "Organic growth, payments transformation and expense management; targets for 2026–27 of ROA 1.15–1.35%, ROTCE in the high teens, mid-single-digit fee growth and positive operating leverage; 2026 revenue guidance raised to +8–9%.",
              s=["corp"], neo=[0, ""], src=[["PMI leadership, Feb 2026", PMI], ["Q3 2026 presentation", Q3PRES]]),
            P("payorg", "Payments transformation", "Payment Services split into Payments: Merchant and Institutional (Elavon, corporate payments, Payments Europe) and Payments: Consumer and Small Business (cards, Elan, co-brand) from early 2025; combined payments revenue up 6.5% in Q3 2026, but segment net income fell 31% on the Amazon portfolio provision.",
              s=["corp", "merch"], st="flux", neo=[0, ""], src=[["Payments split in two, Oct 2024", PAYORG], ["Q3 2026 results", Q3]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: Visa debit and Visa bank-brand credit, Mastercard on the Split card and on Amazon, BMW and Edward Jones co-brands, Visa small-business cards, Elan's agent cards for 1,300 banks, commercial and Voyager fleet cards, Elavon's acquiring for 2 million merchants, and Zelle, instant payments and the USBDC stablecoin.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "U.S. Bank Visa Debit.", "div": "bank", "rev": "cbb", "products": [
            P("debit", "U.S. Bank Visa Debit", "Debit for checking customers, redesigned in March 2026, with Cash Back Deals, Spend & Save transfers and digital-wallet use; issued under licence from Visa.",
              s=["con", "sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Visa Debit redesign, Mar 2026", DEBIT]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Consumer credit", "blurb": "Visa, plus a Split Mastercard.", "div": "cards", "rev": "pay", "products": [
            P("credit", "Bank-brand credit cards", "Smartly Visa Signature (up to 4% cash back with balances, September 2024), Cash+, Altitude Connect and Altitude Go Visa Signature, Shield Visa and secured Visa cards: all eight cards on the credit card page are Visa; average card loans $40.2 billion in Q3 2026.", short="Bank-brand credit (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["U.S. Bank: credit cards", CREDIT], ["Smartly card, Sep 2024", SMARTLY]]),
            P("split", "Split World Mastercard", "Every purchase is split automatically into three interest-free monthly payments, or six or 12 months for a fixed fee; no APR or annual fee; aimed at Gen Z as a bank alternative to buy now, pay later (November 2025).", short="Split (Mastercard)",
              s=["con"], lc="borrow", st="new", ay="Nov 2025", o="P", at="Mastercard", neo=[2, "World Mastercard."],
              mc="The bank's only own-brand consumer Mastercard, and its instalment showcase.",
              src=[["Split launch, Nov 2025", SPLIT]]),
        ]},
        {"id": "2.3", "ic": "gift", "name": "Co-brand cards", "blurb": "Amazon, BMW, Edward Jones.", "div": "cards", "rev": "pay", "products": [
            P("amazon", "Prime Business & Amazon Business Mastercard", "Amazon's small-business cards, moved from American Express to U.S. Bank on Mastercard: 5% or 3% back on Amazon, 2% in the top three categories, 0% instalments and U.S. Bank Spend Management; launched 13 May 2026, Amex accounts converted from 14 August 2026.", short="Amazon business (Mastercard)",
              s=["sme"], lc="borrow", st="new", ay="May 2026", o="P", at="Amazon, Mastercard", neo=[2, "Mastercard, won from Amex."],
              mc="Mastercard's biggest new co-brand at the bank; RWA rose $12 billion when a large co-brand was onboarded in Q3 2026.",
              src=[["Amazon cards launch, May 2026", AMZN], ["Amazon, U.S. Bank and Mastercard, Mar 2026", AMZNMC], ["Amazon card transition", AMZNTX], ["Q3 2026 presentation", Q3PRES]]),
            P("bmw", "BMW, MINI & BMW Motorrad Mastercard", "A co-brand since 2019, relaunched on 13 October 2026 with 3X points on BMW, double-value redemption at dealers, ExtendPay and points paid against BMW Financial Services loans.",
              s=["con"], lc="borrow", st="new", ay="Oct 2026", o="P", at="BMW Financial Services", neo=[2, "Mastercard."], src=[["BMW cards relaunch, Oct 2026", BMW]]),
            P("edwardjones", "Edward Jones Everyday Solutions cards", "Triple Rewards World Elite Mastercard, Flex Balance Mastercard and Business World Elite Mastercard with co-branded checking, sold by 20,000+ advisers to 9 million clients (November 2025); American Banker's 2026 Innovation of the Year.",
              s=["aff"], lc="borrow", st="new", ay="Nov 2025", o="P", at="Edward Jones", neo=[2, "World Elite Mastercard."], src=[["Edward Jones launch, Nov 2025", EJ], ["Innovation award, Jun 2026", EJAWARD]]),
            P("kroger", "Kroger co-brand", "Kroger cardholders are being moved to U.S. Bank Smartly Visa this autumn, with U.S. Bank keeping the accounts (announced 29 July 2026); the Kroger card's earlier network is not stated in the notice ⚠ believed Mastercard.", short="Kroger (to Visa)",
              s=["con"], lc="borrow", st="flux", ay="Jul 2026", o="P", at="Kroger", neo=[1, "Leaving for Smartly Visa ⚠."],
              mc="A grocery co-brand folding into a Visa card.",
              src=[["Kroger transition, Jul 2026", KROGER]]),
            P("visapartners", "Visa co-brands", "State Farm (Premier Cash Rewards, Good Neighbor, Business Cash Rewards, April 2021), AAA Cashback Visa Signature (renewed November 2025; begun in 2015 as a MasterCard ⚠), Harley-Davidson Visa Signature and Korean Air SKYPASS Visa.",
              s=["con"], lc="borrow", o="P", at="State Farm, AAA, Harley-Davidson, Korean Air", neo=[0, "Visa."], src=[["U.S. Bank: partner cards", COBRAND], ["AAA renewal, Nov 2025", AAA], ["State Farm cards, Apr 2021", STATEFARM]]),
        ]},
        {"id": "2.4", "ic": "briefcase", "name": "Small-business cards", "blurb": "Business Essentials on Visa.", "div": "cards", "rev": "pay", "products": [
            P("bizcards", "Business Essentials, Shield & Triple Cash", "Business Essentials Visa and Business Essentials Plus Visa Signature (2% unlimited cash back, up to 3.5% with deposits; 28 September 2026), Business Shield Visa (February 2026), Triple Cash Rewards Visa and Business Altitude Connect, launched in 2023 as a World Elite Mastercard and now Visa Signature ⚠.", short="Small-business cards (Visa)",
              s=["sme"], lc="borrow", st="new", ay="Sep 2026", o="P", at="Visa", neo=[0, "Visa; Altitude Connect left Mastercard ⚠."],
              mc="The new small-business flagship went to Visa the same year Amazon came to Mastercard.",
              src=[["Business Essentials cards, Sep 2026", ESSENTIALS], ["U.S. Bank: business credit cards", BIZCARDS], ["Business Altitude Connect WEMC, Feb 2023", ALTITUDE23], ["Business Shield Visa, Feb 2026", SHIELD]]),
        ]},
        {"id": "2.5", "ic": "network", "name": "Elan agent cards", "blurb": "Cards for 1,300+ banks.", "div": "elan", "rev": "pay", "products": [
            P("elan", "Elan agent credit card issuing", "Turnkey consumer and business credit cards for more than 1,300 banks and credit unions (one in four US institutions partner with Elan), including Max Cash Preferred and Fidelity Rewards; Fiserv's Credit Choice clients converted to Elan by the end of 2025. Mostly Visa, with some World Mastercard versions ⚠.", short="Elan (mostly Visa ⚠)",
              s=["fi"], lc="borrow", o="B", at="Fiserv", neo=[1, "Mostly Visa, some Mastercard ⚠."],
              mc="The largest network decision at the bank that is not yet public.",
              src=[["Elan Financial Services", ELAN], ["Fiserv Credit Choice, Jun 2025", FISERV]]),
        ]},
        {"id": "2.6", "ic": "building-2", "name": "Commercial & fleet cards", "blurb": "Number three; Voyager.", "div": "bank", "rev": "pay", "products": [
            P("commcard", "Corporate, purchasing & virtual cards", "Corporate travel, purchasing, managed-spend and virtual cards, the TravelBank-powered Commercial Rewards Card (June 2023) and GSA SmartPay 3 for federal agencies (to 2031); the number three US commercial card issuer by spend (Nilson, May 2026); issued on both Visa and Mastercard ⚠ split unknown.",
              s=["corp"], lc="move", o="B", at="Visa, Mastercard", neo=[1, "Visa and Mastercard ⚠."], src=[["Q3 2026 presentation", Q3PRES], ["Mastercard travel cards, Apr 2018", MCTRAVEL], ["TravelBank card, Jun 2023", TRAVELBANK], ["GSA SmartPay 3, Sep 2017", GSA]]),
            P("voyager", "Voyager Fleet & Voyager Mastercard", "The Voyager fleet card on its own network at more than 320,000 fuel and maintenance sites, and since August 2021 a dual-network Voyager Mastercard for tolls, repairs, hotels and cross-border fuel.",
              s=["corp"], lc="move", ay="Aug 2021", o="P", at="Mastercard", neo=[1, "Voyager network plus Mastercard."], src=[["Voyager Mastercard, Aug 2021", VOYAGER]]),
        ]},
        {"id": "2.7", "ic": "store", "name": "Elavon acquiring", "blurb": "2m merchants, US and Europe.", "div": "elavon", "rev": "pay", "products": [
            P("elavon", "Elavon merchant acquiring", "About 2 million merchants, more than 9 billion transactions and $600 billion a year; the fifth-largest US acquirer of Visa and Mastercard volume and second-largest owned by a bank (Nilson, March 2025); eight of the top ten global airlines; new CEO Wally Mlynarski (March 2026); merchant processing revenue $461 million in Q3 2026, down 4.9% on the quarter.",
              s=["merch"], lc="move", st="flux", o="B", neo=[1, "Accepts every network."],
              mc="Mastercard has no announced acceptance programme with Elavon.",
              src=[["Elavon: about", ELAVON], ["Elavon fifth in Nilson, Apr 2025", NILSON], ["Mlynarski named, Mar 2026", MLYN], ["Q3 2026 results", Q3]]),
            P("elavoneu", "Elavon Europe & Opayo", "U.S. Bank Europe DAC in Dublin, trading as Elavon Merchant Services and regulated by the Central Bank of Ireland, serving Ireland, the UK, Germany, Poland, Spain and the Nordics, with the Opayo gateway (Sage Pay, bought 2019).",
              s=["merch"], lc="move", o="A", neo=[1, "Accepts every network."], src=[["Elavon Europe: about", ELAVONEU]]),
            P("elavonsmb", "Elavon Business Solutions & All-In-One", "Industry bundles for small merchants with 24/7 human support (May 2026), and an All-In-One platform on Castles Android devices integrated with Oracle Simphony, Agilysys and Shiji (June 2026); gateway awards for Converge and the Elavon Payment Gateway.",
              s=["merch"], lc="move", st="new", ay="May 2026", o="P", at="Castles, Oracle", neo=[1, "Accepts every network."], src=[["Elavon Business Solutions, May 2026", ELAVONSMB], ["All-In-One expansion, Jun 2026", ALLINONE]]),
            P("paze", "Paze checkout", "The bank-owned Paze wallet for U.S. Bank debit and credit cards, with tokenised card numbers, and accepted through Elavon's Converge gateway (September 2024).",
              s=["con", "merch"], lc="move", ay="Sep 2024", o="P", at="Early Warning", neo=[0, "Bank wallet; rival to Click to Pay."], src=[["Paze launch, Sep 2024", PAZE]]),
        ]},
        {"id": "2.8", "ic": "zap", "name": "Instant & digital money", "blurb": "Zelle, instant, USBDC.", "div": "bank", "rev": "wccib", "products": [
            P("zelle", "Zelle", "Person-to-person since 2017; Zelle tags for small businesses (2026) and about 900,000 payments a month to small-business customers.",
              s=["con", "sme"], lc="move", o="P", at="Early Warning", neo=[0, "Zelle."], src=[["Zelle tags, Mar 2026", ZELLE]]),
            P("enhanced", "Enhanced Payments & embedded money movement", "A $25-a-month bundle of same-day ACH, digital wires and instant payments for small businesses (July 2026), and embedded payments with for-benefit-of accounts for platforms such as Updation (October 2026).",
              s=["sme", "corp"], lc="move", st="new", ay="Jul 2026", o="B", neo=[0, "Bank rails."], src=[["Enhanced Payments, Jul 2026", ENHANCED], ["Updation, Oct 2026", UPDATION]]),
            P("usbdc", "USBDC stablecoin", "A bank-issued US-dollar stablecoin on the Stellar blockchain, used in a live cross-border pilot between U.S. Bank entities in North America and Europe (September 2026); custody of stablecoin reserves for Anchorage Digital Bank (October 2025).",
              s=["corp"], lc="move", st="new", ay="Sep 2026", o="B", at="Stellar", neo=[0, "Own token on Stellar."],
              mc="Cross-border treasury on chain is where Mastercard's token and settlement work could meet the bank.",
              src=[["USBDC pilot, Sep 2026", USBDC], ["Digital Assets organisation, Oct 2025", DIGASSETS], ["Anchorage custody, Oct 2025", ANCHORAGE]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: Protect 360 identity monitoring, subscription management powered by Mastercard's Ethoca and Spend Management, ExtendPay, Split and Avvance instalments, and SinglePoint treasury with Kyriba's AI forecasting.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "Protect 360.", "div": "bank", "rev": "cbb", "products": [
            P("protect", "Protect 360", "Credit, identity and data-privacy monitoring in the app that can remove personal data from broker sites; free Essentials tier and a $9.99-a-month Premium tier with $1 million identity-theft cover (7 October 2026).",
              s=["con"], lc="everyday", st="new", ay="Oct 2026", o="B", neo=[0, ""],
              mc="Demand for identity tools; Mastercard's identity and scam products are not used publicly.",
              src=[["Protect 360, Oct 2026", PROTECT]]),
        ]},
        {"id": "3.2", "ic": "receipt-text", "name": "Card tools", "blurb": "Subscriptions via Ethoca.", "div": "cards", "rev": "pay", "products": [
            P("subs", "Subscription management & digital receipts", "Credit cardholders see and cancel subscriptions in the app and get itemised digital receipts from hundreds of merchants, powered by Ethoca, a Mastercard company (October 2025).", short="Subscriptions (Mastercard Ethoca)",
              s=["con"], lc="everyday", ay="Oct 2025", o="P", at="Mastercard (Ethoca)", neo=[3, "Ethoca, Mastercard's own."],
              mc="Mastercard's own service running across a mostly Visa card base.",
              src=[["Subscription management, Oct 2025", SUBS]]),
            P("spend", "Spend Management", "Card controls, receipt capture and accounting integration for business cards, built into the Business Shield, Business Essentials and Amazon cards.",
              s=["sme"], lc="everyday", o="B", neo=[1, "Runs on Visa and Mastercard cards."], src=[["Business Shield Visa, Feb 2026", SHIELD], ["Amazon cards launch, May 2026", AMZN]]),
            P("travel", "Travel Center & rewards", "Card rewards travel booking with Booking.com, powered by Rocket Travel by Agoda (November 2024), plus cash-back deals and merchant offers.",
              s=["con", "sme"], lc="grow", o="P", at="Booking.com, Agoda", neo=[0, ""], src=[["Travel Center, Nov 2024", TRAVEL]]),
        ]},
        {"id": "3.3", "ic": "hand-coins", "name": "Pay over time", "blurb": "ExtendPay and Avvance.", "div": "bank", "rev": "pay", "products": [
            P("avvance", "Avvance & ExtendPay", "Avvance embeds point-of-sale instalment loans for merchants (October 2023), now with six- and seven-year terms for home improvement and partners such as Skeps (March 2026); ExtendPay (2021) splits purchases on existing U.S. Bank cards.",
              s=["con", "merch"], lc="borrow", st="new", ay="Oct 2023", o="B", at="Skeps", neo=[0, "Bank loans; ExtendPay rides on the card."],
              mc="Instalments are built in-house; Mastercard Installments is not used publicly.",
              src=[["Avvance longer terms, Mar 2026", AVVANCE], ["Split launch, Nov 2025", SPLIT]]),
        ]},
        {"id": "3.4", "ic": "code-xml", "name": "Treasury & APIs", "blurb": "SinglePoint, Kyriba AI.", "div": "bank", "rev": "wccib", "products": [
            P("singlepoint", "SinglePoint & Liquidity Manager", "The next-generation SinglePoint treasury platform (October 2025) and Liquidity Manager, powered by Kyriba, with AI cash forecasting for mid-sized and large firms (November 2025).",
              s=["corp"], lc="move", st="new", ay="Oct 2025", o="P", at="Kyriba", neo=[0, ""], src=[["SinglePoint, Oct 2025", SINGLEPOINT], ["Liquidity Manager, Nov 2025", KYRIBA]]),
            P("embedded", "Embedded payments & APIs", "Payment APIs, for-benefit-of accounts and real-time payments for software platforms such as Updation's dealership system (October 2026).",
              s=["corp", "sme"], lc="move", st="new", o="B", neo=[0, ""], src=[["Updation, Oct 2026", UPDATION]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: Bank Smartly accounts and mortgages, banking for 2 million small businesses, corporate, commercial and institutional banking with BTIG, wealth management, and corporate payments led by freight and healthcare.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Consumer banking", "blurb": "Bank Smartly, mortgages.", "div": "bank", "rev": "cbb", "products": [
            P("smartly", "Bank Smartly accounts & mortgages", "Bank Smartly Checking and Savings with Smart Rewards, record consumer deposits in 2025–26, mortgages, and Consumer and Business Banking net income of $633 million in Q3 2026.",
              s=["con"], lc="everyday", neo=[0, "Visa debit."], src=[["Q3 2026 results", Q3], ["Smartly card, Sep 2024", SMARTLY]]),
        ]},
        {"id": "4.2", "ic": "briefcase-business", "name": "Small business", "blurb": "2 million businesses.", "div": "bank", "rev": "cbb", "products": [
            P("smallbiz", "Small-business banking", "More than 2 million small businesses, $45 billion of deposits and $18 billion of loans; Business Essentials checking with card acceptance, payroll and bill pay; banker teams in Florida, Georgia, Texas and Arizona.",
              s=["sme"], lc="everyday", st="new", neo=[0, "Visa cards; Amazon on Mastercard."], src=[["Q3 2026 presentation", Q3PRES], ["Business Essentials cards, Sep 2026", ESSENTIALS]]),
        ]},
        {"id": "4.3", "ic": "factory", "name": "Corporate & institutional", "blurb": "Capital markets with BTIG.", "div": "btig", "rev": "wccib", "products": [
            P("cib", "Corporate, commercial & institutional banking", "Serves nearly 90% of the Fortune 1000; capital markets revenue $640 million in Q3 2026 (+69%), $226 million of it from BTIG; custody in nearly 100 markets; segment net income $1.60 billion.",
              s=["corp"], lc="borrow", st="new", neo=[0, ""], src=[["Q3 2026 results", Q3], ["BTIG agreed, Jan 2026", BTIGDEAL]]),
        ]},
        {"id": "4.4", "ic": "gem", "name": "Wealth", "blurb": "$802m trust fees a quarter.", "div": "wealth", "rev": "wccib", "products": [
            P("wealth", "Wealth management", "U.S. Bank Wealth Management, Private Wealth and U.S. Bancorp Advisors; trust and investment management fees of $802 million in Q3 2026 (+9.9%); the Edward Jones alliance reaches 9 million advisory clients.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["Q3 2026 results", Q3], ["Edward Jones launch, Nov 2025", EJ]]),
        ]},
        {"id": "4.5", "ic": "plane", "name": "Corporate payments", "blurb": "Freight and healthcare.", "div": "bank", "rev": "pay", "products": [
            P("industry", "Freight, healthcare & public-sector payments", "The largest US freight payments provider by volume, healthcare payments under Eric Levine (June 2026) and Salucro's MedEpay, and federal card programmes; corporate payment and treasury management revenue $457 million in Q3 2026 (+12.3%).",
              s=["corp"], lc="move", st="new", neo=[1, "Card programmes on Visa and Mastercard ⚠."],
              mc="Commercial virtual cards and B2B data are where Mastercard fits the PMI push.",
              src=[["Q3 2026 presentation", Q3PRES], ["Healthcare payments, Jun 2026", LEVINE], ["Q3 2026 results", Q3]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the U.S. Bank app and online banking, branches being refurbished on a ten-year cycle, and partners: State Farm agents, Edward Jones advisers, Amazon, Elan's banks and Elavon's software partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "App & online", "blurb": "Protect 360, Split, Spend.", "div": "bank", "rev": "cbb", "products": [
            P("app", "U.S. Bank Mobile App & online banking", "The home of Protect 360, subscription management, Split plans and Spend Management; digital-user numbers are not published ⚠.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["Protect 360, Oct 2026", PROTECT], ["Subscription management, Oct 2025", SUBS]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "Refreshed on a 10-year cycle.", "div": "bank", "rev": "cbb", "products": [
            P("branches", "Branches", "A multi-year refurbishment on a ten-year cycle, starting in Denver, Minneapolis-St Paul, Nashville, Portland and California (December 2025); branch count not published in the Q3 2026 materials ⚠.",
              s=["con", "sme"], lc="open", neo=[0, ""], src=[["Branch refresh, Dec 2025", BRANCHES]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Alliances & partners", "blurb": "State Farm, Edward Jones.", "div": "usb", "rev": "cbb", "products": [
            P("alliances", "Alliances & partner channels", "State Farm's 19,400 agents and Edward Jones' 20,000+ advisers sell U.S. Bank accounts and cards; Elan reaches 1,300+ institutions; Elavon sells through software partners and the Microsoft Marketplace.",
              s=["con", "fi", "merch"], lc="open", o="P", at="State Farm, Edward Jones", neo=[1, "Edward Jones on Mastercard; State Farm on Visa."], src=[["Edward Jones alliance, Aug 2024", EJ24], ["Edward Jones launch, Nov 2025", EJ], ["Elan Financial Services", ELAN]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at U.S. Bank", "blurb": "Partner cards, not the core.", "products": [
        P("mcatusb", "Mastercard at U.S. Bank", "Visa carries U.S. Bank's debit, every bank-brand consumer card, the new small-business cards, most co-brands and most of Elan. Mastercard carries the Amazon small-business cards won from American Express in 2026, Edward Jones, BMW, the Split card, Voyager Mastercard and part of commercial cards, and Ethoca runs subscription management; Kroger is moving to Visa.",
          s=["con"], div="usb", rev="pay", mc="The relationship this map is drawn for.",
          src=[["Amazon cards launch, May 2026", AMZN], ["U.S. Bank: credit cards", CREDIT], ["Kroger transition, Jul 2026", KROGER]]),
    ]},
    {"id": "pillar-market", "name": "US payments", "blurb": "Co-brand fights, stablecoins.", "products": [
        P("market", "The US market", "Co-brand portfolios changing hands (Amazon from Amex, Kroger into own-brand Visa), bank wallets (Paze) and Zelle, instant payments, the GENIUS Act for stablecoins (July 2025), and Elavon fifth among US acquirers.",
          s=["con"], div="usb", rev="pay", src=[["Anchorage custody, Oct 2025", ANCHORAGE], ["Elavon fifth in Nilson, Apr 2025", NILSON], ["Payments Dive via Yahoo, Mar 2026", AMZNPD]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
