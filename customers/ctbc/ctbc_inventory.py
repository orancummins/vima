"""CTBC Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are CTBC's own unless a source says otherwise: the 2Q26 results presentation (18 August 2026), the
monthly operating results to September 2026, and CTBC Holding's press releases. Several CTBC Bank card pages
sit behind a bot check, so networks for some co-brand cards come from CTBC's tier names or comparison sites
and are marked ⚠. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

MONTHLY = "https://ir.ctbcholding.com/c/financial"
Q2 = "https://media-ctbc.todayir.com/20260818161612135651828_en.pdf"
BANK = "https://www.ctbcholding.com/content/twhoo/en_tw/ctbc-bank/ctbc-bank.html"
BOD = "https://ir.ctbcholding.com/html/gov_bod.php"
RATINGS = "https://ir.ctbcholding.com/html/credit.php"
NEWS = "https://www.ctbcholding.com/content/dam/twhoo/file/news/"
EXEC24 = NEWS + "2024/20240726.pdf"
CARD50 = NEWS + "2024/20240901.pdf"
SIXTY = NEWS + "2026/20260331-2.pdf"
LHFG = NEWS + "2021/20210331-2.pdf"
SHINKONG = NEWS + "2024/20240820.pdf"
SK_AIR = "https://asiainsurancereview.com/News/View-NewsLetter-Article/id/89449/Type/eDaily/Conferences/Gallery"
SK_GF = "https://gfmag.com/news/taiwan-ctbc-financial-holding-shin-kong-standard-chartered-bank/"
AI100 = NEWS + "2026/20260122.pdf"
AIWM = NEWS + "2026/20260123.pdf"
CARDS25 = NEWS + "2026/20260115.pdf"
CARDS24 = NEWS + "2025/20250113.pdf"
FSC = "https://www.taipeitimes.com/News/biz/archives/2026/01/16/2003850668"
LP400 = NEWS + "2021/20210730.pdf"
LP7 = NEWS + "2024/20240104-2.pdf"
LPNET = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E7%94%A2%E5%93%81/%E4%B8%AD%E5%9C%8B%E4%BF%A1%E8%A8%97linepay%E5%8D%A1"
UNI = NEWS + "2025/20250821.pdf"
UNI1M = NEWS + "2026/20260826.pdf"
UNIUDN = "https://money.udn.com/money/story/5613/9716351"
MARRIOTT = NEWS + "2026/20260916-2.pdf"
MARRIOTT_LTN = "https://ec.ltn.com.tw/article/breakingnews/5576199"
PANDA = NEWS + "2023/20231215.pdf"
PANDANET = "https://roo.cash/creditcard/info/ctbc-foodpanda"
AGODA = NEWS + "2023/20230613.pdf"
SOGO = NEWS + "2024/20241008.pdf"
CPC21 = NEWS + "2021/20211208.pdf"
CPCPAY = NEWS + "2025/20250806-2.pdf"
DIAMOND = NEWS + "2026/20260106.pdf"
SMARTPAY = NEWS + "2026/20260722.pdf"
TAPPHONE = NEWS + "2021/20210115.pdf"
TAPIPHONE = NEWS + "2023/20230420.pdf"
CLOUDPOS = NEWS + "2023/20230328.pdf"
APPLEPAY = NEWS + "2017/20170201.pdf"
WALLETBIND = NEWS + "2021/20210804.pdf"
MPAY = "https://www.ctbcbank.com/twrbo/zh_tw/cc_index/cc_product/cc_mpay_index.html"
OB3 = NEWS + "2025/20250806.pdf"
OB3LIVE = NEWS + "2025/20251107.pdf"
ALERTS = NEWS + "2025/20250306.pdf"
DIGI8M = NEWS + "2025/20251015.pdf"
AIATM = NEWS + "2025/20251031.pdf"
HBR = NEWS + "2026/20261001-1.pdf"
FASTID = NEWS + "2025/20251002-1.pdf"
SOFTCERT = NEWS + "2023/20231117.pdf"
RECUR = NEWS + "2025/20250116.pdf"
AISEC = NEWS + "2025/20251107-1.pdf"
MC_AGENT = "https://www.mastercard.com/news/ap/zh-tw/%E6%96%B0%E8%81%9E%E4%B8%AD%E5%BF%83/%E6%96%B0%E8%81%9E%E7%A8%BF/zh-tw/2026/mar/%E8%90%AC%E4%BA%8B%E9%81%94%E5%8D%A1%E6%94%9C%E6%89%8B%E6%98%9F%E5%B1%95%E9%8A%80%E8%A1%8C-%E5%8F%B0%E7%81%A3-%E5%AE%8C%E6%88%90%E7%AC%AC%E4%B8%80%E7%AD%86%E4%BB%A3%E7%90%86%E5%BC%8Fai%E6%94%AF%E4%BB%98%E4%BA%A4%E6%98%93/"
MC_CTP = "https://www.mastercard.com/news/ap/zh-tw/%E6%96%B0%E8%81%9E%E4%B8%AD%E5%BF%83/%E6%96%B0%E8%81%9E%E7%A8%BF/zh-tw/2025/dec/%E8%90%AC%E4%BA%8B%E9%81%94%E5%8D%A1%E4%BD%88%E5%B1%80%E6%99%BA%E6%85%A7%E5%95%86%E5%8B%99-%E6%89%93%E9%80%A0ai%E6%94%AF%E4%BB%98%E6%96%B0%E6%9C%AA%E4%BE%86/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · group · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: NT$7.55 trillion of bank assets and record profits, a group with Taiwan Life and the national lottery, 60 years since 1966, AI built in-house since 2018, and the widest overseas network of any Taiwanese bank.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "NT$49.5bn profit to September.", "div": "bank", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Bank assets of NT$7.55 trillion, loans of NT$4.73 trillion (up 17.5%) and deposits of NT$6.23 trillion at 30 June 2026; bank profit of NT$31.2 billion in the half (up 12.3%) and NT$49.5 billion in January to September 2026; NT$57.3 billion in 2025; CAR 13.6%; rated A1 by Moody's and A by S&P.",
              s=["con"], neo=[0, ""], src=[["CTBC 2Q26 results presentation", Q2], ["CTBC monthly results, Sep 2026", MONTHLY], ["CTBC credit ratings", RATINGS]]),
            P("group", "CTBC Financial Holding", "The listed parent (TWSE: 2891): group profit of NT$63.2 billion to September 2026, with Taiwan Life (NT$10.3 billion in the half), CTBC Securities and Taiwan Lottery beside the bank, which earns about two-thirds of group profit.",
              s=["con", "wealth"], neo=[0, ""], src=[["CTBC monthly results, Sep 2026", MONTHLY], ["CTBC 2Q26 results presentation", Q2]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "James Chen and Yang Ming-hsiang.", "div": "holding", "rev": "group", "products": [
            P("leadership", "Board & management", "Holding chairman Wen-Long Yen, vice chairman Daniel I. Wu and president Rachael Kao (from July 2024); bank chairman James Chen (from July 2024) and president Yang Ming-hsiang ⚠ romanisation; Yang Shu-hui runs personal finance ⚠.",
              s=["corp"], neo=[0, ""], src=[["CTBC Holding: board", BOD], ["CTBC: management changes, Jul 2024", EXEC24], ["CTBC Marriott card launch, Sep 2026", MARRIOTT]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brand", "blurb": "60 years; Taiwan's first card.", "div": "bank", "rev": "consumer", "products": [
            P("heritage", "Heritage & 'We are Family'", "Founded in 1966 by the Koo family; issued Taiwan's first credit card in 1974 and opened the country's first bank customer-service centre; 60th anniversary in 2026.",
              s=["con"], o="I", neo=[0, ""], src=[["CTBC Bank overview", BANK], ["CTBC: 50 years of cards, Sep 2024", CARD50], ["CTBC: 60th anniversary card offers, Mar 2026", SIXTY]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "An AI team since 2018.", "div": "holding", "rev": "group", "products": [
            P("tech", "AI & data platform", "A dedicated AI team since 2018; the only financial firm to win Business Weekly's top 'AI Innovation 100' award (January 2026); generative-AI assistants for cards and wealth, and an AI carbon-finance platform, PathMatch, recognised by Singapore's MAS.",
              s=["corp"], st="new", neo=[0, ""], src=[["CTBC: AI Innovation 100, Jan 2026", AI100], ["CTBC 2Q26 results presentation", Q2]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Taiwan champion, Asia leader.", "div": "holding", "rev": "overseas", "products": [
            P("strategy", "Taiwan Champion, Asia Leader", "Lead at home in cards, wealth and lending, and grow the widest overseas network of any Taiwanese bank: 14 countries and regions and more than 370 outlets.",
              s=["corp"], neo=[0, ""], src=[["CTBC Bank overview", BANK]]),
            P("deals", "Deals", "Raised its stake in Thailand's LH Financial Group to 46.6% (2021); bid for 51% of Shin Kong Financial in August 2024, which the regulator rejected and Taishin then merged with; new branches in India's GIFT City (May 2026) and Indonesia (December 2025).",
              s=["corp"], o="A", neo=[0, ""], src=[["CTBC: LHFG stake, Mar 2021", LHFG], ["CTBC: Shin Kong tender, Aug 2024", SHINKONG], ["Asia Insurance Review: bid rejected, Sep 2024", SK_AIR], ["Global Finance: CTBC withdraws", SK_GF]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: Taiwan's largest card book on every network, co-brands split between Visa (LINE Pay, Marriott, foodpanda) and Mastercard (uniopen ⚠), debit, a Visa commercial virtual card, NT$930 billion of acquiring, phone wallets, open-banking payments and cross-border flows.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "NT$890bn spent in 2025.", "div": "cards", "rev": "consumer", "products": [
            P("cards", "CTBC credit cards", "Taiwan's largest issuer: NT$890 billion of credit-card spend in 2025, first in cards in force and active cards, and about 18% of the market's spend in November 2025. Issued on Visa, Mastercard, JCB and American Express.", short="Credit cards (all networks)",
              s=["con"], lc="everyday", o="B", neo=[1, "All four networks."],
              mc="The biggest card book in Taiwan, spread across every network.",
              src=[["CTBC: 2025 card spend over NT$1 trillion, Jan 2026", CARDS25], ["Taipei Times: FSC card data, Jan 2026", FSC]]),
            P("premium", "Ding Ji and Wealth Diamond premium cards", "Ding Ji is issued as Visa Infinite, World Mastercard and JCB Ultimate, with a Songshan airport lounge from February 2025; the Wealth Diamond card (January 2026) for wealth clients with NT$3 million or more pays up to 3% back abroad, network not stated ⚠.",
              s=["wealth"], lc="everyday", st="new", neo=[1, "World Mastercard is one of three tiers."],
              src=[["CTBC: 60th anniversary card offers, Mar 2026", SIXTY], ["CTBC: 2024 card spend, Jan 2025", CARDS24], ["CTBC: Wealth Diamond card, Jan 2026", DIAMOND]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Co-brand cards", "blurb": "LINE Pay on Visa, uniopen on Mastercard.", "div": "cards", "rev": "consumer", "products": [
            P("linepay", "CTBC LINE Pay card", "Launched in 2016–17, Taiwan's biggest co-brand with more than 4 million cards by July 2021; LINE POINTS on every purchase. Issued on Visa and JCB, with a Visa debit version.", short="LINE Pay card (Visa, JCB)",
              s=["con"], lc="everyday", o="P", at="LINE Pay", neo=[0, "Visa and JCB."],
              mc="The largest co-brand in Taiwan carries no Mastercard.",
              src=[["CTBC: LINE Pay card passes 4 million, Jul 2021", LP400], ["CTBC: LINE Pay card at 7, Jan 2024", LP7], ["money101: LINE Pay card networks", LPNET]]),
            P("uniopen", "CTBC uniopen co-brand card", "With the Uni-President group (7-Eleven, Starbucks, Carrefour and 27 more brands, about 10,000 outlets): launched August 2025, more than 1 million cards by August 2026, spend at the group's outlets up 80% and 120,000 new customers; target 3 million cards. Issued as World and Titanium cards, Mastercard tiers ⚠.", short="uniopen (Mastercard ⚠)",
              s=["con"], lc="everyday", st="new", ay="Aug 2025", o="P", at="Uni-President", neo=[2, "World and Titanium Mastercard tiers ⚠."],
              mc="Mastercard's biggest new programme at CTBC.",
              src=[["CTBC: uniopen card launch, Aug 2025", UNI], ["CTBC: uniopen passes 1 million, Aug 2026", UNI1M], ["UDN: uniopen 1 million, Aug 2026", UNIUDN]]),
            P("marriott", "CTBC Marriott Bonvoy card", "Taiwan's first international hotel-group co-brand, launched 16 September 2026 in Visa Signature and Visa Infinite tiers, with Marriott Gold or Platinum status and a 1,888-card metal edition.", short="Marriott Bonvoy (Visa)",
              s=["abroad", "wealth"], lc="everyday", st="new", ay="Sep 2026", o="P", at="Marriott, Visa", neo=[0, "Visa."],
              src=[["CTBC: Marriott card launch, Sep 2026", MARRIOTT], ["Liberty Times: Marriott Visa card, Sep 2026", MARRIOTT_LTN]]),
            P("foodpanda", "CTBC foodpanda card", "Taiwan's first food-delivery co-brand (December 2023), up to 10% back in pandacoins; Visa Signature.",
              s=["con"], lc="everyday", ay="Dec 2023", o="P", at="foodpanda", neo=[0, "Visa."],
              src=[["CTBC: foodpanda card, Dec 2023", PANDA], ["roo.cash: foodpanda card", PANDANET]]),
            P("cpc", "CPC co-brand card & CPC Pay", "With state oil company CPC: 1.1 million cards and 1 million CPC Pay app downloads by December 2021; a CPC Pay shopping mall added in August 2025. Network not confirmed ⚠.",
              s=["con"], lc="everyday", o="P", at="CPC", neo=[None, "Network not confirmed."],
              src=[["CTBC: CPC card 1.1 million, Dec 2021", CPC21], ["CTBC: CPC Pay mall, Aug 2025", CPCPAY]]),
            P("travelcards", "Travel & mall co-brands", "Agoda (June 2023), China Airlines and ANA mileage cards (ANA business card on Visa), Far Eastern SOGO (October 2024), Hotai, ALL ME and CTBC Brothers cards; networks for most not confirmed ⚠.",
              s=["abroad", "con"], lc="everyday", o="P", at="Agoda, SOGO, airlines", neo=[None, "Mixed; mostly not confirmed."],
              src=[["CTBC: Agoda card, Jun 2023", AGODA], ["CTBC: SOGO card, Oct 2024", SOGO], ["CTBC: 60th anniversary card offers, Mar 2026", SIXTY]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "Debit", "blurb": "NT$130bn in 2025.", "div": "bank", "rev": "consumer", "products": [
            P("debit", "Debit cards", "NT$130 billion of debit spend in 2025, first in the market. The LINE Pay debit card is Visa; networks for other debit cards not confirmed ⚠.",
              s=["con"], lc="everyday", neo=[None, "Visa for LINE Pay debit; others unconfirmed."],
              src=[["CTBC: 2025 card spend over NT$1 trillion, Jan 2026", CARDS25], ["money101: LINE Pay card networks", LPNET]]),
        ]},
        {"id": "2.4", "ic": "briefcase-business", "name": "Commercial cards", "blurb": "A Visa virtual card.", "div": "bank", "rev": "corporate", "products": [
            P("smartpay", "CTBC Smart Pay corporate card", "Launched with Visa on 22 July 2026: virtual card numbers pulled straight into a company's ERP through CTBC's API Banking, with time-limited authorisations for travel and online spend.", short="Smart Pay card (Visa)",
              s=["corp"], lc="move", st="new", ay="Jul 2026", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa took the commercial virtual-card launch.",
              src=[["CTBC: Smart Pay card with Visa, Jul 2026", SMARTPAY]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acquiring", "blurb": "NT$930bn acquired in 2025.", "div": "bank", "rev": "consumer", "products": [
            P("acquiring", "Merchant acquiring", "More than NT$930 billion acquired in 2025, with terminals, mobile terminals, cross-border collection, a merchant AI service desk and online sign-up.",
              s=["merch"], lc="move", neo=[1, "Accepts every network."],
              src=[["CTBC: 2025 card spend over NT$1 trillion, Jan 2026", CARDS25]]),
            P("softpos", "Phone & cloud acceptance", "Tap to Phone with Taiwan Taxi (2021), first to support Tap to Pay on iPhone (April 2023), and a cloud cash register and ECPay terminal for small merchants (March 2023).",
              s=["merch"], lc="move", o="P", at="Apple, ECPay, Taiwan Taxi", neo=[1, "Accepts every network."],
              src=[["CTBC: Tap to Phone, Jan 2021", TAPPHONE], ["CTBC: Tap to Pay on iPhone, Apr 2023", TAPIPHONE], ["CTBC: cloud cash register, Mar 2023", CLOUDPOS]]),
        ]},
        {"id": "2.6", "ic": "smartphone", "name": "Wallets & tokens", "blurb": "Apple Pay from day one.", "div": "cards", "rev": "consumer", "products": [
            P("wallets", "Phone wallets", "A first-wave Apple Pay bank (2017), with Google Pay, Samsung Pay, Garmin Pay, LINE Pay, PX Pay, OPEN Wallet and Taiwan Pay, and a 'wallet binding' view in the app since July 2021.",
              s=["con"], lc="everyday", o="P", at="Apple, Google, LINE", neo=[1, "Tokens on every network."],
              mc="Click to Pay was set for Taiwan in early 2026 with Union Bank, not CTBC.",
              src=[["CTBC: Apple Pay, Feb 2017", APPLEPAY], ["CTBC: wallet binding, Aug 2021", WALLETBIND], ["CTBC: mobile payments", MPAY], ["Mastercard: Click to Pay in Taiwan, Dec 2025", MC_CTP]]),
        ]},
        {"id": "2.7", "ic": "zap", "name": "Open-banking payments", "blurb": "Phase 3 live, November 2025.", "div": "bank", "rev": "consumer", "products": [
            P("openbanking", "Open banking", "Phase 2 data sharing from April 2021; phase 3 transactions (transfers and time deposits from the TDCC app over FISC's Open API) approved in August 2025 and live on 7 November 2025.",
              s=["con"], lc="move", st="new", ay="Nov 2025", neo=[0, "FISC's domestic rails."],
              src=[["CTBC: open banking phase 3 approved, Aug 2025", OB3], ["CTBC: phase 3 live, Nov 2025", OB3LIVE]]),
        ]},
        {"id": "2.8", "ic": "earth", "name": "Cross-border & FX", "blurb": "NT$2.65trn in FX deposits.", "div": "bank", "rev": "overseas", "products": [
            P("fx", "FX & cross-border banking", "Foreign-currency deposits of NT$2.65 trillion and loans of NT$1.64 trillion at June 2026, across 14 countries and regions.",
              s=["abroad", "corp"], lc="move", neo=[0, ""],
              mc="Remittances and payouts across 14 markets are open ground.",
              src=[["CTBC 2Q26 results presentation", Q2], ["CTBC Bank overview", BANK]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: CTBC's own fraud alerts and AI at the ATM, Fast-ID identity, a recurring-payment detector and an AI card secretary, and points that run across partners' wallets.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & scams", "blurb": "NT$4.3bn prevented in 3 years.", "div": "bank", "rev": "consumer", "products": [
            P("cardalerts", "Card security alerts", "Taiwan's first in-app card security alert (March 2025): a 'possible fraud' prompt when a payment is held, with online card lock; over NT$4.3 billion of fraud losses prevented in three years.",
              s=["con"], lc="everyday", neo=[0, "CTBC's own."],
              mc="Scam scoring and transaction alerts could add network data.",
              src=[["CTBC: app security alerts, Mar 2025", ALERTS], ["CTBC: 8 million digital users, Oct 2025", DIGI8M], ["CTBC 2Q26 results presentation", Q2]]),
            P("aiatm", "AI anti-fraud ATMs", "ATMs that warn customers on the phone while transferring (with the police 165 line, since 2019) and, from October 2025, detect masks and helmets; awarded by Harvard Business Review for AI anti-fraud work (October 2026).",
              s=["con"], lc="everyday", neo=[0, "CTBC's own."],
              src=[["CTBC: AI ATM, Oct 2025", AIATM], ["CTBC: HBR awards, Oct 2026", HBR]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Identity", "blurb": "Fast-ID across institutions.", "div": "bank", "rev": "consumer", "products": [
            P("fastid", "CTBC Fast-ID", "Face-ID verification from the CTBC app for other banks, insurers and brokers under the FSC's Fast-ID hub (October 2025).",
              s=["con"], lc="open", st="new", ay="Oct 2025", neo=[0, ""],
              src=[["CTBC: Fast-ID, Oct 2025", FASTID]]),
            P("softcert", "Digital card applications", "Income checks through JCIC with a software certificate, so card applicants and limit increases need no paper proof (November 2023).",
              s=["con"], lc="open", neo=[0, ""],
              src=[["CTBC: software certificate, Nov 2023", SOFTCERT]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "Data & AI for customers", "blurb": "An AI card secretary.", "div": "cards", "rev": "consumer", "products": [
            P("recurring", "Recurring-payment detector", "Finds every subscription charged to a CTBC card (January 2025); about 15% of cardholders had more than a million recurring charges a month in 2024. The launch cited Mastercard's Taiwan consumer survey.",
              s=["con"], lc="everyday", ay="Jan 2025", neo=[0, "CTBC's own."],
              mc="Fits subscription controls and Automatic Billing Updater.",
              src=[["CTBC: recurring-payment detector, Jan 2025", RECUR]]),
            P("aisecretary", "AI credit-card secretary", "A generative-AI assistant that tells customers which card to use where, sums their spending and flags risky payments (November 2025).",
              s=["con"], lc="everyday", st="new", ay="Nov 2025", neo=[0, ""],
              mc="Agent Pay's first Taiwan transaction ran with DBS Taiwan, not CTBC.",
              src=[["CTBC: AI card secretary, Nov 2025", AISEC], ["Mastercard: first Agent Pay transaction in Taiwan, Mar 2026", MC_AGENT]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards & points", "blurb": "Four ecosystems.", "div": "cards", "rev": "consumer", "products": [
            P("points", "Points & ecosystems", "CTBC points, LINE POINTS, OPENPOINT, pandacoins, Marriott Bonvoy points and air miles, earned and spent in real time through APIs into partners' wallets across retail, social, travel and 33 department stores.",
              s=["con"], lc="grow", neo=[0, "CTBC's and partners'."],
              src=[["CTBC: 2025 card spend over NT$1 trillion, Jan 2026", CARDS25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: wealth management (half of fee income), NT$1.52 trillion of mortgages, corporate and API banking, and banks in Japan, Thailand and across Asia.",
    "tiles": [
        {"id": "4.1", "ic": "gem", "name": "Wealth management", "blurb": "Half of fee income.", "div": "bank", "rev": "wealth", "products": [
            P("wealthmgmt", "Wealth management", "NT$17.5 billion of fees in the first half of 2026, 51% of the bank's fee income, from mutual funds, bancassurance, custody and trusts; 531 CFP holders, the most in Taiwan.",
              s=["wealth"], lc="grow", neo=[0, ""],
              src=[["CTBC 2Q26 results presentation", Q2], ["CTBC: CFP holders, Jan 2026", AIWM]]),
            P("aiadviser", "AI wealth-adviser assistant", "An AI assistant for relationship managers across investment, insurance and trust advice (January 2026).",
              s=["wealth"], lc="grow", st="new", ay="Jan 2026", neo=[0, ""],
              src=[["CTBC: AI wealth assistant, Jan 2026", AIWM]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Mortgages & loans", "blurb": "NT$1.52trn of mortgages.", "div": "bank", "rev": "consumer", "products": [
            P("mortgages", "Mortgages", "NT$1.52 trillion at June 2026, up 19.9% in a year.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["CTBC 2Q26 results presentation", Q2]]),
            P("unsecured", "Personal loans & card revolving", "NT$324 billion of unsecured loans and card revolving balances at June 2026; retail NPL ratio 0.10%.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["CTBC 2Q26 results presentation", Q2]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Corporate banking", "blurb": "NT$1.25trn of NTD loans.", "div": "bank", "rev": "corporate", "products": [
            P("corporate", "Corporate & institutional banking", "NT$1.25 trillion of corporate NTD loans at June 2026 (up 14.7%), syndications and offshore-wind project finance.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["CTBC 2Q26 results presentation", Q2]]),
            P("apibanking", "API Banking", "Bank-to-ERP connections that now issue virtual card numbers for the Smart Pay card (July 2026).",
              s=["corp"], lc="move", st="new", neo=[0, "Visa for its cards."], src=[["CTBC: Smart Pay card with Visa, Jul 2026", SMARTPAY]]),
        ]},
        {"id": "4.4", "ic": "globe", "name": "Overseas banking", "blurb": "Japan, Thailand and on.", "div": "tokyostar", "rev": "overseas", "products": [
            P("tokyostar", "The Tokyo Star Bank", "CTBC's Japanese subsidiary, owned since 2014 ⚠ date, with a Kumamoto office for the semiconductor supply chain (2023) that moved to a new branch in July 2026.",
              s=["corp", "abroad"], lc="borrow", o="A", neo=[None, "Card networks not checked."], src=[["CTBC Bank overview", BANK], ["CTBC 2Q26 results presentation", Q2]]),
            P("lhbank", "LH Financial Group (Thailand)", "46.6% owned since 2021, the largest shareholder, with a majority of board seats from October 2021.",
              s=["corp", "abroad"], lc="borrow", o="A", neo=[None, "Card networks not checked."], src=[["CTBC: LHFG stake, Mar 2021", LHFG], ["CTBC Bank overview", BANK]]),
            P("overseasnet", "Overseas network", "Subsidiaries in the US, Canada, the Philippines and Indonesia and branches in Vietnam, India and Singapore: 14 countries and regions and more than 370 outlets; overseas NPL ratio 2.49%.",
              s=["corp", "abroad"], lc="borrow", neo=[0, ""],
              mc="Cross-border payouts and issuing in 14 markets.",
              src=[["CTBC Bank overview", BANK], ["CTBC 2Q26 results presentation", Q2]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach CTBC: the mobile app and LINE account for more than 8 million digital users, branches and ATMs in 7-Eleven, and partners' apps and stores.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "App & LINE", "blurb": "8 million digital users.", "div": "bank", "rev": "consumer", "products": [
            P("app", "CTBC mobile banking app", "More than 8 million digital users (October 2025), about 700 functions, monthly active users up more than 10% in a year, and a LINE official account.",
              s=["con", "wealth"], lc="everyday", neo=[0, ""], src=[["CTBC: 8 million digital users, Oct 2025", DIGI8M]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "ATMs in 7-Eleven since 2001.", "div": "bank", "rev": "consumer", "products": [
            P("branches", "Branches & ATMs", "Branches across Taiwan, with new ones in Kaohsiung and Tainan in 2026, and ATMs in 7-Eleven stores since 2001.",
              s=["con", "home"], lc="everyday", neo=[0, ""], src=[["CTBC: uniopen card launch, Aug 2025", UNI], ["CTBC: AI ATM, Oct 2025", AIATM]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partner ecosystems", "blurb": "Uni-President, LINE, CPC.", "div": "cards", "rev": "consumer", "products": [
            P("ecosystems", "Partner apps & stores", "Retail (Uni-President), social (LINE, foodpanda), transport and travel (CPC, Hotai, China Airlines, Marriott) and 33 department stores, where CTBC cards, points and payments sit inside partners' apps.",
              s=["con", "merch"], lc="open", o="P", at="Uni-President, LINE, CPC", neo=[0, ""], src=[["CTBC: 2025 card spend over NT$1 trillion, Jan 2026", CARDS25]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at CTBC", "blurb": "uniopen, and Visa on the rest.", "products": [
        P("mcatctbc", "Mastercard at CTBC", "CTBC issues on every network. Mastercard has the uniopen co-brand (1 million cards in a year, World and Titanium tiers ⚠), the World Mastercard tier of the Ding Ji card, and acceptance. Visa has the LINE Pay card with JCB, and the 2023–26 showcase launches: foodpanda, Marriott Bonvoy and the Smart Pay commercial virtual card.",
          s=["con"], div="bank", rev="consumer", mc="The relationship this map is drawn for.",
          src=[["CTBC: uniopen passes 1 million, Aug 2026", UNI1M], ["CTBC: Smart Pay card with Visa, Jul 2026", SMARTPAY]]),
    ]},
    {"id": "pillar-market", "name": "Taiwan payments", "blurb": "60 million cards, 32 issuers.", "products": [
        P("market", "The Taiwan market", "60.42 million credit cards from 32 issuers (November 2025) and NT$4.53 trillion of card spend in January to November 2025; CTBC first in spend and new cards, Cathay United second; FSC open banking phase 3 and the Fast-ID hub; domestic rails run by FISC and NCCC.",
          s=["con"], div="holding", rev="group", src=[["Taipei Times: FSC card data, Jan 2026", FSC]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
