"""Kapital Bank's (Birbank's) layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the statutory indicators to 30 September 2026
(published 13 October 2026), the 2025 consolidated IFRS statements (22 April 2026) and the 2024 Sustainability
Report, all on the Reports page. Card networks are partly read from card artwork on birbank.az (marked ⚠).
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

ABOUT = "https://www.kapitalbank.az/en/about"
REPORTS = "https://www.kapitalbank.az/en/reports"
RATINGS = "https://www.kapitalbank.az/en/ratings"
ECOSYS = "https://birbank.az/en/ecosystem"
HOME = "https://birbank.az/en"
DEBIT = "https://birbank.az/en/debet-kartlar"
CREDIT = "https://birbank.az/en/kredit-kartlar"
MILES = "https://cards.kapitalbank.az/en/BRML/"
CASHBACK = "https://cards.kapitalbank.az/en/BRCB_BLACK/"
STAR = "https://cards.kapitalbank.az/en/BRST/"
PRIVATE = "https://birbank.az/en/birbank-private"
TELEBE = "https://birbank.az/en/cards/talabaplus"
TEHSIL = "https://birbank.az/en/cards/tehsilplus"
TEHSIL_TR = "https://www.trend.az/business/4161690.html"
BIZCARD = "https://birbank.business/kartlar/visa-biznes"
POS = "https://birbank.business/pos-xidmetleri/pos-terminal"
MPOS = "https://birbank.business/pos-xidmetleri/mobil-pos"
SAHIBKAR = "https://birbank.az/en/news/accept-payments-without-limits-with-birbank-sahibkar-and-biznes-cards"
MILLION = "https://birbank.az/en/news/birbank-operations-at-6-500-millioen-terminals-are-commission-free"
FEES = "https://birbank.az/en/news/news-data-18"
BIRKART = "https://birbank.az/news/birkart-rebrendinq-en"
BNPL = "https://birbank.az/en/bokt/indi-al-sonra-ode"
NINJA = "https://birbank.az/en/ninja"
REBRAND = "https://www.trend.az/azerbaijan/business/3983963.html"
TRANSIT = "https://www.trend.az/azerbaijan/business/3983975.html"
AI = "https://www.trend.az/business/finance/3955925.html"
PAYSYS = "https://www.trend.az/business/economy/4195974.html"
FY25 = "https://www.trend.az/business/4177478.html"
INVEST = "https://www.trend.az/business/4177468.html"
MASHREQ = "https://www.trend.az/azerbaijan/business/4116490.html"
RANK = "https://www.trend.az/business/4073328.html"
SECTOR = "https://interfax.com/newsroom/top-stories/118650/"
CARDS_AZ = "https://report.az/en/amp/finance/cashless-payments-in-azerbaijan-down-2-2-in-april"
IPS = "https://en.apa.az/finance/cba-daily-transactions-through-instant-payment-system-reach-1-million-529663"
CBFEES = "https://www.trend.az/business/finance/4234660.html"
VISA26 = "https://www.trend.az/business/4209712.html"
PASHAPAY = "https://pashapay.az/news/eng/pashapay_partners_mastercard"
APPLEPAY = "https://appleinsider.com/articles/21/11/02/apple-pay-launching-in-azerbaijan-colombia-costa-rica"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · PASHA · 150 years", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: AZN 13.9 billion of assets and AZN 297 million of nine-month profit, PASHA Holding's ownership, a savings bank dating from 1874, the move from Kapital Bank to the Birbank brand, and an in-house digital platform.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "AZN 13.9bn, number two.", "div": "kb", "rev": "treasury", "products": [
            P("balance", "Balance sheet & earnings", "Total assets AZN 13.92 billion, gross loans AZN 6.39 billion and deposits AZN 10.31 billion at 30 September 2026; nine-month net profit AZN 297.0 million, up 30%; total capital ratio 13.64%. 2025 IFRS net profit AZN 274.6 million, up 15%. Second-largest bank by assets after ABB (June 2025). Rated BB by S&P and Ba2 for deposits by Moody's (outlook positive).",
              s=["con", "corp"], neo=[0, ""], src=[["Kapital Bank: reports (Q3 2026, 2025 IFRS)", REPORTS], ["Trend: 2025 profit, Apr 2026", FY25], ["Kapital Bank: ratings", RATINGS], ["Trend: banks by assets, Jul 2025", RANK]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "PASHA Holding; CEO Huseynov.", "div": "kb", "rev": "corporate", "products": [
            P("owners", "PASHA Holding & Bir ecosystem", "PASHA Holding owned 99.89% at end-2025 ⚠ (the About page shows 81.08% PASHA Holding, 7.52% PASHA Sigorta, 11.40% others). From January 2026 the bank sits in Bir ecosystem LLC under PASHA's new financial holding. Not listed; no market value.",
              s=["corp"], st="flux", neo=[0, ""], src=[["Kapital Bank: reports (2025 IFRS)", REPORTS], ["Kapital Bank: about", ABOUT]]),
            P("leadership", "Supervisory & management boards", "Farid Mammadov chairs the supervisory board. Farid Huseynov has been CEO since May 2023, with Javid Mirzayev First Deputy Chairman, Jalal Orujov Deputy Chairman, Rauf Atakishiyev CFO, Farid Hidayatzada corporate sales and Agharza Bakhshiyev risk. 5,765 employees at end-2025.",
              s=["corp"], neo=[0, ""], src=[["Kapital Bank: about", ABOUT]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brand", "blurb": "1874, now Birbank.", "div": "birbank", "rev": "retail", "products": [
            P("heritage", "From Kapital Bank to Birbank", "Heir to the Savings Bank of Azerbaijan, founded 1874, with a 150th anniversary in 2024. All products moved to the Birbank brand from 2025, with branches converting over about two years; Kapital Bank remains the legal and corporate name.",
              s=["con"], o="I", st="flux", ay="2025", neo=[0, ""], src=[["Trend: rebrand to Birbank, Dec 2024", REBRAND], ["Kapital Bank: about", ABOUT]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "In-house, cloud, AI.", "div": "kb", "rev": "retail", "products": [
            P("tech", "Birbank platform, data & AI", "An in-house Birbank platform moved to microservices and cloud, with retail IT from the Competo subsidiary; AI and analytics prioritised for engagement, efficiency and revenue, including lifetime-value and churn models. Global Finance award for AI in digital transformation, 2024.",
              s=["corp"], o="B", neo=[0, ""], src=[["Trend: analytics and AI, Oct 2024", AI], ["Kapital Bank: reports (2024 sustainability report)", REPORTS]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Retail lead, SMB, ecosystem.", "div": "kb", "rev": "treasury", "products": [
            P("strategy", "Strategic goals", "Keep the retail lead, make micro-business lending profitable, grow SMB, join financial and non-financial products in one ecosystem and build data-based products. Customers are being steered to the app: branch fees for PIN, card details and second physical cards from September to November 2026.",
              s=["corp"], neo=[0, ""], src=[["Kapital Bank: about", ABOUT], ["Birbank: fee changes, Oct 2026", FEES]]),
            P("deals", "Deals & funding", "PashaPay brought under control (March 2022), Competo a subsidiary (2024), subordinated US dollar bonds (July 2024) and a first syndicated loan of USD 50 million arranged by Mashreq (November 2025).",
              s=["corp"], o="A", neo=[0, ""], src=[["Trend: Mashreq syndicated loan, Nov 2025", MASHREQ], ["Kapital Bank: reports (2025 IFRS)", REPORTS]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Taksit and Star cards on Visa, debit and Miles cards split between Visa and Mastercard, premium and public-sector programmes on both, Visa business cards, POS acceptance, QR and transfers, and the PashaPay wallet and terminals.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Taksit & credit cards", "blurb": "60% of instalment cards.", "div": "birbank", "rev": "retail", "products": [
            P("taksit", "Birbank Cashback / Taksit card", "The ex-BirKart instalment card (2016): up to 24 months interest-free at partners, up to 63 days' grace, cashback up to 30% and double VAT refund on QR payments; a 60% share of Azerbaijan's instalment-card market at rebrand. Card artwork shows Visa ⚠.", short="Taksit (Visa ⚠)",
              s=["con"], lc="borrow", o="B", at="Visa", neo=[0, "Visa ⚠ (artwork)."],
              mc="The mass-market Birbank card is a Visa card.",
              src=[["Birbank: credit cards", CREDIT], ["Birbank: Cashback card", CASHBACK], ["Birbank: BirKart rebrand", BIRKART]]),
            P("star", "Birbank Star", "A credit line up to AZN 30,000 with no annual interest and a monthly usage fee, cashback and double VAT on QR payments; launched 2024. Card artwork named Star-Visa.", short="Star (Visa)",
              s=["con"], lc="borrow", ay="2024", o="B", at="Visa", neo=[0, "Visa."], src=[["Birbank: Star card", STAR], ["Birbank: credit cards", CREDIT]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Debit & Miles", "blurb": "7.2m debit cards.", "div": "birbank", "rev": "retail", "products": [
            P("debit", "Birbank Debit", "Free debit card with partner bonuses and free withdrawals, ordered in the app and delivered by Wolt; digital cards free, a fee for extra physical cards from September 2026. The bank had 7.2 million debit cards at end-2024. Network not stated ⚠.",
              s=["con"], lc="everyday", neo=[None, "Network not stated ⚠."], src=[["Birbank: debit cards", DEBIT], ["Kapital Bank: reports (2024 sustainability report)", REPORTS]]),
            P("platinum", "Birbank Platinum & Platinum Miles", "Premium debit cards with bonuses or miles; miles can pay for flights, hotels and tours to the end of 2026. Visa Platinum artwork.",
              s=["con", "prem"], lc="everyday", at="Visa", neo=[0, "Visa."], src=[["Birbank: debit cards", DEBIT], ["Birbank: fee changes, Oct 2026", FEES]]),
            P("miles", "Birbank Miles", "Miles on every purchase (65 miles = AZN 1), up to 30,000 a month, for any airline ticket, with Mastercard Airport Experiences and LoungeKey. Miles Taksit is a Mastercard World card; Miles Debit artwork shows Visa ⚠.", short="Miles (Mastercard / Visa)",
              s=["con"], lc="everyday", o="P", at="Mastercard, Visa", neo=[1, "Miles Taksit on Mastercard World; Miles Debit Visa ⚠."],
              mc="Mastercard's main foothold in the Birbank card range.",
              src=[["Birbank: Miles card", MILES], ["Birbank: credit cards", CREDIT], ["Birbank: debit cards", DEBIT]]),
        ]},
        {"id": "2.3", "ic": "gem", "name": "Premium & public-sector cards", "blurb": "World Elite; TəhsilPlus.", "div": "private", "rev": "retail", "products": [
            P("private", "Birbank Private cards", "Visa Infinite Cashback, Visa Infinite Miles and Mastercard World Elite Miles for private-banking clients, with travel redemptions through PASHA Travel.",
              s=["prem"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Two Visa Infinite cards; one World Elite."], src=[["Birbank: Private", PRIVATE]]),
            P("telebe", "TələbəPlus", "Student card with the Education Development Fund and Visa (2024): scholarship, university access card and 200+ partner benefits, first issued at Baku State University.", short="TələbəPlus (Visa)",
              s=["edu"], lc="everyday", ay="2024", o="P", at="Visa, Education Development Fund", neo=[0, "Visa."], src=[["Birbank: TələbəPlus", TELEBE]]),
            P("tehsil", "TəhsilPlus", "Salary, debit and access card for about 450,000 education staff, with the Education Development Fund and Mastercard, including Mastercard Priceless Specials; first cards presented 6 March 2026 by Farid Hidayatzada and Mastercard's Engin Yashar.", short="TəhsilPlus (Mastercard)",
              s=["edu"], lc="everyday", st="new", ay="Mar 2026", o="P", at="Mastercard, Education Development Fund", neo=[2, "Mastercard card with Priceless Specials."],
              mc="Mastercard's newest and largest programme at the bank.",
              src=[["Trend: TəhsilPlus, Mar 2026", TEHSIL_TR], ["Birbank: TəhsilPlus", TEHSIL]]),
        ]},
        {"id": "2.4", "ic": "briefcase-business", "name": "Business cards", "blurb": "All Visa.", "div": "biznes", "rev": "corporate", "products": [
            P("bizcards", "Visa Biznes, Gold, Digital, Gömrük & Sahibkar", "Company expense cards, a customs card and salary cards; Birbank Sahibkar and Biznes cards are exempt from 2026 limits on incoming transfers and carry Visa business offers.", short="Business cards (Visa)",
              s=["micro", "corp"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="About 123,000 micro and SME clients hold Visa business cards; commercial cards are open ground.",
              src=[["Birbank Biznes: Visa Biznes", BIZCARD], ["Birbank: Sahibkar and Biznes cards, Aug 2026", SAHIBKAR]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "POS and tap-on-phone.", "div": "biznes", "rev": "corporate", "products": [
            P("pos", "POS terminals", "Terminals accepting Visa and Mastercard, contactless to AZN 100 without PIN, phones and watches; Bir Bonus redeemable at the bank's POS.",
              s=["micro"], lc="move", o="B", neo=[1, "Accepts Visa and Mastercard."], src=[["Birbank Biznes: POS terminal", POS]]),
            P("mpos", "Mobile POS", "Turns an NFC Android phone into a contactless terminal for cards, Apple Pay and Google Pay; AZN 5 a month from 2026.",
              s=["micro"], lc="move", st="new", o="B", neo=[1, "Accepts every contactless card."], src=[["Birbank Biznes: Mobile POS", MPOS]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Transfers, QR & instant", "blurb": "QR in-house; IPS rising.", "div": "birbank", "rev": "retail", "products": [
            P("qr", "Birbank QR payments", "QR payments brought in-house into Birbank and m10 in 2024, with double VAT refund on QR purchases; QR is 22% of transit transactions in the ecosystem.",
              s=["con", "micro"], lc="move", o="B", neo=[0, "Own QR rails."],
              mc="Own QR routes everyday spending off card rails.",
              src=[["Kapital Bank: reports (2024 sustainability report)", REPORTS], ["Bir ecosystem", ECOSYS]]),
            P("transfers", "Card-to-card & remittances", "Transfers to any bank card in the app and remittances by Western Union, Khazri and Zolotaya Korona; from 2026 a national cap of five incoming card transfers a day and AZN 20,000 a month for personal cards.",
              s=["con"], lc="move", o="P", at="Western Union", neo=[None, "Card-to-card rails not disclosed."],
              mc="Mastercard Move could carry Birbank's outbound sends.",
              src=[["Birbank home page", HOME], ["Birbank: Sahibkar and Biznes cards, Aug 2026", SAHIBKAR]]),
            P("ips", "Instant Payment System", "The central bank's 24/7 ISO 20022 system handled about 1 million transactions a day by October 2026, against a million a month in 2024, with lower fees from April 2027. Kapital Bank's own IPS use is not published ⚠.",
              s=["con", "corp"], lc="move", st="unconf", neo=[0, "Central-bank rails."], src=[["APA: IPS 1 million a day, Oct 2026", IPS], ["Trend: CBA fees, Oct 2026", CBFEES]]),
        ]},
        {"id": "2.7", "ic": "wallet", "name": "Wallets, terminals & transit", "blurb": "m10, MilliÖn, BakıKart.", "div": "pashapay", "rev": "eco", "products": [
            P("m10", "m10 e-wallet", "PashaPay's wallet: 829,000 users, 47.5 million transactions this year, the national e-wallet leader; Umico bonuses integrated.",
              s=["eco"], lc="move", o="A", neo=[0, "Own wallet."], src=[["Bir ecosystem", ECOSYS]]),
            P("million", "MilliÖn terminals", "The country's largest cash payment terminal network, 6,500 terminals, for bills, loan repayments and top-ups; Birbank operations commission-free from September 2026.",
              s=["con", "eco"], lc="move", o="A", neo=[0, ""], src=[["Birbank: MilliÖn terminals, Sep 2026", MILLION]]),
            P("wallets", "Apple Pay & Google Pay", "Apple Pay since its Azerbaijan launch on 2 November 2021, with Kapital Bank among the first banks; Google Pay for debit cards.",
              s=["con"], lc="move", ay="Nov 2021", o="P", at="Apple, Google", neo=[1, "Visa and Mastercard tokens."], src=[["AppleInsider: Apple Pay in Azerbaijan, Nov 2021", APPLEPAY], ["Birbank: debit cards", DEBIT]]),
            P("transit", "BakıKart & transit", "BakıKart top-ups in Birbank since May 2024 (550,000 users, 4.5 million tickets by December 2024); Visa cardholders pay on Baku and Ganja metro and buses through BakıKart, Payriff and Kapital Bank since 2025.",
              s=["con", "edu"], lc="move", o="P", at="BakıKart, Visa", neo=[0, "Visa transit."], src=[["Trend: Birbank transit users, Dec 2024", TRANSIT], ["Trend: CBA and Visa, Jul 2026", VISA26]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: Bir Bonus loyalty and automatic VAT refunds, the bank's own fraud controls with a Mastercard MoU at PashaPay, AI and analytics, and a payments office building notifications and subscription controls.",
    "tiles": [
        {"id": "3.1", "ic": "gift", "name": "Bir Bonus & VAT refunds", "blurb": "One loyalty engine.", "div": "competo", "rev": "eco", "products": [
            P("birbonus", "Bir Bonus", "One loyalty programme across thousands of partners, replacing m10 cashback and folding in Umico bonuses (2024); earned on cards, QR and the marketplace.",
              s=["con", "eco"], lc="beyond", o="B", neo=[0, ""],
              mc="Card-linked offers could feed Bir Bonus across 5 million users.",
              src=[["Bir ecosystem", ECOSYS], ["Kapital Bank: reports (2024 sustainability report)", REPORTS]]),
            P("vat", "Automatic VAT refund", "Receipts added to the customer's VAT refund automatically across more than 172 partner networks (September 2026).",
              s=["con"], lc="everyday", st="new", ay="Sep 2026", o="B", neo=[0, ""], src=[["Birbank: fee changes, Oct 2026", FEES]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud, identity & onboarding", "blurb": "Own controls; a Mastercard MoU.", "div": "kb", "rev": "retail", "products": [
            P("fraud", "Fraud & card security", "3D Secure, card freezes and limits in the app, phishing-skimming insurance and transaction alerts; an ABA award for digital payment security (2024). An unauthorised-transactions fraud at a subsidiary in 2026 may be material ⚠.",
              s=["con"], lc="everyday", o="B", neo=[0, "Own."],
              mc="Transaction risk and identity tools have a clear need after the 2026 incident.",
              src=[["Kapital Bank: reports (2025 IFRS, 2024 sustainability report)", REPORTS]]),
            P("mcmou", "PashaPay–Mastercard MoU", "Signed 3 June 2025 at Money20/20 Europe: cybersecurity, digital identity and fraud prevention, cross-border sends through Mastercard MoneySend, Cross-Border Send and Alias Directory, and loyalty for m10 users. Live use unconfirmed ⚠.",
              s=["eco"], lc="move", st="unconf", ay="Jun 2025", o="P", at="Mastercard", neo=[1, "MoU; live use unconfirmed ⚠."], src=[["PashaPay: Mastercard MoU, Jun 2025", PASHAPAY]]),
            P("onboarding", "Bir ID & digital onboarding", "One login across the ecosystem, remote onboarding for thin-file customers and video verification for business clients.",
              s=["con", "micro"], lc="open", o="B", neo=[0, ""], src=[["Bir ecosystem", ECOSYS], ["Kapital Bank: reports (2024 sustainability report)", REPORTS]]),
        ]},
        {"id": "3.3", "ic": "brain", "name": "Data, AI & notifications", "blurb": "Alerts and subscriptions.", "div": "kb", "rev": "retail", "products": [
            P("ai", "Personalisation & AI support", "Behavioural credit scoring, lifetime-value and churn models, product recommendations and an AI chatbot in the app.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["Trend: analytics and AI, Oct 2024", AI], ["Kapital Bank: reports (2024 sustainability report)", REPORTS]]),
            P("notify", "Transaction alerts & subscription manager", "Alerts that show where and when a card was used, which cut calls to the contact centre, and a subscription manager for recurring card payments in development (June 2026).",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, "Own build."],
              mc="Matches Mastercard's merchant clarity and recurring-payment tools.",
              src=[["Trend: payment-system innovations, Jun 2026", PAYSYS]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: a third of the country's consumer loans and instalments, mortgages and car finance, deposits, Birbank Invest and insurance, micro, SME and corporate banking, and the Birmarket marketplace.",
    "tiles": [
        {"id": "4.1", "ic": "hand-coins", "name": "Consumer lending & BNPL", "blurb": "34.1% of consumer loans.", "div": "birbank", "rev": "retail", "products": [
            P("cashloan", "Cash loans", "Cash loans up to AZN 80,000 from 10.9% over 3–59 months, with refinancing offers; consumer loans of AZN 3.54 billion at 30 September 2026 and a 34.1% market share.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Birbank home page", HOME], ["Bir ecosystem", ECOSYS], ["Kapital Bank: reports (Q3 2026)", REPORTS]]),
            P("bnpl", "Taksit partners, Ninja & Trendyol BNPL", "Instalments at partner stores, Ninja to split one-off purchases elsewhere, and a buy-now-pay-later credit line for Trendyol shoppers (400,000 users).",
              s=["con", "eco"], lc="borrow", o="P", at="Trendyol", neo=[0, "Own credit lines."], src=[["Birbank: Ninja", NINJA], ["Birbank: buy now, pay later", BNPL], ["Bir ecosystem", ECOSYS]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Mortgages & car finance", "blurb": "AZN 0.59bn of property loans.", "div": "birbank", "rev": "retail", "products": [
            P("mortgage", "Mortgages", "Real-estate loans of AZN 0.59 billion at 30 September 2026.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Kapital Bank: reports (Q3 2026)", REPORTS]]),
            P("car", "Car loans & leasing", "Car loans at 12% a year with 10% down, and car leasing.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Birbank home page", HOME]]),
        ]},
        {"id": "4.3", "ic": "coins", "name": "Savings, investing & insurance", "blurb": "Birbank Invest, 100,000 users.", "div": "invest", "rev": "retail", "products": [
            P("deposits", "Deposits & savings account", "Retail deposits of AZN 4.10 billion, up 32% in a year; term deposits up to 10%, a savings account, demand deposits and government bonds.",
              s=["con", "prem"], lc="grow", neo=[0, ""], src=[["Kapital Bank: reports (Q3 2026)", REPORTS], ["Birbank home page", HOME]]),
            P("invest", "Birbank Invest", "Brokerage app with PASHA Capital (2025): nearly 100,000 users and USD 25 million of turnover in nine months, 12,000+ instruments from USD 1.",
              s=["con", "prem"], lc="grow", st="new", ay="2025", o="P", at="PASHA Capital", neo=[0, ""], src=[["Trend: Birbank Invest, Apr 2026", INVEST]]),
            P("insurance", "Insurance", "Credit-life, unemployment, CASCO, school, accident, card-damage and phishing-skimming cover sold in the app.",
              s=["con"], lc="beyond", o="P", neo=[0, ""], src=[["Birbank home page", HOME]]),
        ]},
        {"id": "4.4", "ic": "briefcase", "name": "Micro, SME & corporate", "blurb": "123,000 small firms.", "div": "biznes", "rev": "corporate", "products": [
            P("sme", "Micro & SME banking", "106,406 micro-business and 16,716 SME customers; micro loans in Birbank and Birbank Biznes, state-backed SİF and AKİA loans, overdrafts and leasing; business loans up 33% to AZN 2.27 billion.",
              s=["micro"], lc="borrow", neo=[0, "Visa business cards."], src=[["Bir ecosystem", ECOSYS], ["Kapital Bank: reports (Q3 2026)", REPORTS]]),
            P("corp", "Corporate & treasury", "Accounts, guarantees, letters of credit, payroll and tax tools for 22,000+ legal entities, with AZN 6.21 billion of corporate deposits; treasury earned AZN 100.5 million in 2025.",
              s=["corp"], lc="everyday", neo=[0, ""], src=[["Kapital Bank: reports (Q3 2026, 2025 IFRS)", REPORTS], ["Kapital Bank: about", ABOUT]]),
        ]},
        {"id": "4.5", "ic": "store", "name": "Birmarket", "blurb": "Sales up 73%.", "div": "competo", "rev": "eco", "products": [
            P("birmarket", "Birmarket marketplace", "One-click marketplace with 2,737 sellers and more than 300,000 buyers, sales up 73% a year; the ecosystem segment lost AZN 86.8 million in 2025.",
              s=["eco"], lc="beyond", o="A", neo=[0, ""],
              mc="A checkout where Click to Pay and tokens could sit.",
              src=[["Bir ecosystem", ECOSYS], ["Kapital Bank: reports (2025 IFRS)", REPORTS]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the Birbank app for 3.5 million, Birbank Biznes, the country's largest branch network with about 1,300 ATMs, and partners from Wolt to 6,500 MilliÖn terminals.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Birbank app", "blurb": "3.5 million users.", "div": "birbank", "rev": "retail", "products": [
            P("app", "Birbank app", "3.5 million users and the top-ranked mobile bank in Azerbaijan (Markswebb, 2024); cards, loans, transfers, QR, BakıKart and investing in one app.",
              s=["con", "edu", "prem"], lc="everyday", o="B", neo=[0, ""], src=[["Bir ecosystem", ECOSYS], ["Kapital Bank: reports (2024 sustainability report)", REPORTS]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Birbank Biznes", "blurb": "95% use digital.", "div": "biznes", "rev": "corporate", "products": [
            P("bizapp", "Birbank Biznes app", "The main channel for business clients: digital registration, multi-user access, tax and VAT tools, payroll and QR cash-out at ATMs; 95.4% of SME clients use digital products.",
              s=["micro", "corp"], lc="everyday", o="B", neo=[0, ""], src=[["Bir ecosystem", ECOSYS], ["Kapital Bank: reports (2024 sustainability report)", REPORTS]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & ATMs", "blurb": "Largest network.", "div": "kb", "rev": "retail", "products": [
            P("branches", "Branches, digital centres & ATMs", "115–116 branches, 13 digital centres and about 51–53 divisions, the largest network in Azerbaijan, being rebranded Birbank; about 1,300 ATMs, including cash-in.",
              s=["con", "micro"], lc="open", st="flux", neo=[0, ""], src=[["Birbank home page", HOME], ["Birbank: fee changes, Oct 2026", FEES], ["Kapital Bank: reports (2025 IFRS)", REPORTS]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partners", "blurb": "Shops, Wolt, MilliÖn.", "div": "birbank", "rev": "retail", "products": [
            P("partners", "Partner channels", "Cards sold for AZN 1 at partner shops and delivered by Wolt, banking at 6,500 MilliÖn terminals, and instalment partners across electronics, furniture and clothing.",
              s=["con", "eco"], lc="open", o="P", at="Wolt, MilliÖn", neo=[0, ""], src=[["Birbank: Cashback card", CASHBACK], ["Birbank: MilliÖn terminals, Sep 2026", MILLION]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Kapital Bank", "blurb": "Second network, new public card.", "products": [
        P("mcatkb", "Mastercard at Kapital Bank", "The bank issues on both networks and is a member of both. Visa carries the mass-market Taksit and Star cards, premium Visa Infinite, students and all business cards. Mastercard carries Miles Taksit (World), World Elite Miles and, since March 2026, the TəhsilPlus card for about 450,000 education staff; its subsidiary PashaPay signed an MoU with Mastercard in June 2025.",
          s=["con"], div="kb", rev="retail", mc="The relationship this map is drawn for.",
          src=[["Trend: TəhsilPlus, Mar 2026", TEHSIL_TR], ["PashaPay: Mastercard MoU, Jun 2025", PASHAPAY], ["Birbank: credit cards", CREDIT]]),
    ]},
    {"id": "pillar-market", "name": "Azerbaijani banking", "blurb": "IPS, QR, transfer caps.", "products": [
        P("market", "The Azerbaijani market", "22 licensed banks with AZN 60.9 billion of assets (June 2026); 22.5 million payment cards and 160,000 POS terminals (May 2026); the central bank's instant payment system at about a million transactions a day; 2026 caps on incoming card transfers; and Visa reporting 10 local issuers on Click to Pay.",
          s=["con"], div="kb", rev="retail", src=[["Interfax: banking sector, Aug 2026", SECTOR], ["Report.az: card statistics, May 2026", CARDS_AZ], ["APA: IPS 1 million a day, Oct 2026", IPS], ["Trend: CBA and Visa, Jul 2026", VISA26]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
