"""USAA's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are USAA's own unless a source says otherwise: the 2025 Annual Report to Members (spring 2026), USAA's
newsroom and product pages, and FDIC call-report data for USAA Federal Savings Bank to 30 June 2026. USAA is a
member-owned association and publishes no 10-K. ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

AR25 = "https://static.usaa.com/content/dam/digital/documents/pdf/brand/2025-annual-report-to-members.pdf"
AR25REL = "https://usaa-newsroom.prgloo.com/news/usaa-2025-annual-report-reflects-a-year-of-strength-service-and-commitment-to-members-1"
FY24 = "https://usaa-newsroom.prgloo.com/news/strong-financial-performance-reflects-usaas-unwavering-commitment-to-members-and-the-military-community"
REW25 = "https://usaa-newsroom.prgloo.com/news/usaa-members-benefit-from-usd-3-7-billion-in-financial-rewards-in-2025"
FDIC = "https://api.fdic.gov/banks/financials?filters=CERT:32188"
CARDS26 = "https://usaa-newsroom.prgloo.com/news/usaa-bank-credit-cards-july-2026"
CC = "https://www.usaa.com/banking/credit-cards/"
DEBIT = "https://www.usaa.com/banking/debit-card/"
CHK = "https://www.usaa.com/banking/checking/"
BANK = "https://www.usaa.com/banking/"
AB15 = "https://www.americanbanker.com/payments/news/visa-replacing-mastercard-as-usaa-partner-for-credit-debit"
PJ15 = "https://www.paymentsjournal.com/usaa-switching-credit-debit-cards-to-visa-from-longtime-partner-mastercard/"
ANDRADE = "https://usaa-newsroom.prgloo.com/news/usaa-announces-juan-c-andrade-as-president-and-chief-executive-officer"
MORAN = "https://usaa-newsroom.prgloo.com/news/usaa-bank-board-appoints-michael-moran-as-bank-president"
MELCHER = "https://usaa-newsroom.prgloo.com/news/test"
IBM26 = "https://www.insurancebusinessmag.com/us/news/breaking-news/usaa-names-a-new-board-chairman-as-it-returns-to-financial-strength-587160.aspx"
CIO = "https://usaa-newsroom.prgloo.com/news/usaa-names-dan-griffiths-chief-information-officer-to-drive-secure-simplified-digital-member-experiences"
CRO = "https://usaa-newsroom.prgloo.com/news/usaa-appoints-brian-goldman-as-chief-risk-officer"
OCC24 = "https://www.bankingdive.com/news/occ-usaa-cease-desist-order-deficiencies-risk-management/736064/"
SAR = "https://sanantonioreport.org/usaa-capital-growth-members-report-2025-lower-insurance-rates/"
BOFA = "https://usaa-newsroom.prgloo.com/news/bofa-and-usaa-enter-patent-cross-license-agreement"
TRUIST = "https://usaa-newsroom.prgloo.com/news/usaa-truist-settle-remote-deposit-capture-litigation"
AGENT = "https://usaa-newsroom.prgloo.com/news/usaa-bank-launches-agent-connection-to-help-reduce-costs-and-simplify-home-buying-and-selling-for-military-families-veterans"
NOBLR = "https://usaa-newsroom.prgloo.com/news/usaa-announces-plans-to-acquire-insurtech-company-noblr-inc"
HTA = "https://usaa-newsroom.prgloo.com/news/usaa-launches-honor-through-action-committing-usd-500-million-over-five-years-to-champion-the-military-community"
SCHWAB = "https://thinkadvisor.com/2019/07/25/schwab-to-buy-usaa-brokerage-business-for-1-8b"
VICTORY = "https://themilitarywallet.com/usaa-victory-capital-schwab/"
APP22 = "https://usaa-newsroom.prgloo.com/news/usaa-improving-member-experience-with-faster-modernized-mobile-app"
CHES = "https://usaa-newsroom.prgloo.com/news/usaa-to-expand-workforce-in-chesapeake-to-support-growing-membership"
DOC = "https://www.doctorofcredit.com/usaa-launches-new-eagle-adapt-card-200-bonus-15-month-0-period-3-cashback/"
NILSON = "https://wtop.com/news/2026/03/8-biggest-u-s-credit-card-companies-this-year/"
AGENTPAY = "https://www.mastercard.com/us/en/news-and-trends/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai.html"
S1033 = "https://www.consumerfinancemonitor.com/2026/08/06/cfpb-sends-new-section-1033-open-banking-proposal-to-oira-for-review/"
CCCA = "https://www.congress.gov/bill/119th-congress/senate-bill/3623/text"
ZELLEINTL = "https://www.zelle.com/press-releases/zelle-goes-international-early-warning-expands-1t-payments-network-stablecoin"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "members · capital · charter", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: 14.3 million members who own the association, $38.6 billion of net worth, a $106 billion savings bank under an OCC order, 3,000 patents and a new CEO focused on member value.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & net worth", "blurb": "14.3m members, $38.6bn net worth.", "div": "usaa", "rev": "corp", "products": [
            P("scale", "Association scale", "14.3 million members at end-2025 (more than 14.5 million by July 2026); total assets $235.8 billion and net worth $38.6 billion (up 20%); a record $3.8 billion returned to members in 2025, up from $2.2 billion. 2024 revenue was $48.6 billion and net income $3.9 billion; 2025 revenue and income were not published.",
              s=["con", "vet"], neo=[0, ""], src=[["2025 Annual Report to Members", AR25], ["2024 results, Apr 2025", FY24], ["San Antonio Report, May 2026", SAR]]),
            P("bankscale", "USAA Federal Savings Bank", "$106.2 billion of assets and $92.0 billion of deposits at 30 June 2026, but only $44.3 billion of net loans: cards $18.6 billion and auto $17.4 billion. H1 2026 net income $484 million (ROE about 17%); 11,883 staff, down from 14,007 in March 2025.",
              s=["con"], neo=[0, ""], src=[["FDIC BankFind: USAA FSB call reports", FDIC]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & regulation", "blurb": "Andrade, Melcher, an OCC order.", "div": "usaa", "rev": "corp", "products": [
            P("leadership", "Board & executives", "Chairman Lt. Gen. David F. Melcher (Ret.) from August 2026; CEO Juan C. Andrade from April 2025 (ex-Everest, Chubb, The Hartford); CFO Brett Seybold; USAA Bank president Michael Moran (January 2025); CIO Dan Griffiths (ex-Santander US, February 2026); CRO Brian Goldman (ex-Comerica, May 2025).",
              s=["con"], st="new", neo=[0, ""], src=[["USAA: Melcher chairman, Aug 2026", MELCHER], ["USAA: Andrade CEO, Jan 2025", ANDRADE], ["USAA: Moran bank president, Jan 2025", MORAN], ["USAA: Griffiths CIO, Feb 2026", CIO], ["USAA: Goldman CRO, May 2025", CRO]]),
            P("occ", "OCC cease-and-desist order", "A comprehensive OCC order of December 2024 replaced the 2019 risk-governance order ($85 million penalty) and the 2022 anti-money-laundering order ($140 million with FinCEN). New products and membership changes need 90 days' notice and documented controls; incentive pay to covered staff stopped from April 2025. No termination found ⚠.",
              s=["con"], st="flux", neo=[0, ""],
              mc="Any new Mastercard service at the bank has to clear the OCC's new-product notice.",
              src=[["Banking Dive: OCC order, Dec 2024", OCC24]]),
        ]},
        {"id": "1.3", "ic": "flag", "name": "Heritage & membership", "blurb": "Founded by 25 officers in 1922.", "div": "usaa", "rev": "corp", "products": [
            P("heritage", "A military mutual", "Founded in San Antonio in 1922 by 25 Army officers insuring each other's cars; a reciprocal inter-insurance exchange owned by its policyholders. Membership is open to serving and former military, cadets and their spouses and children; 77% of member households hold more than one product and retention is 96%.",
              s=["con", "vet", "young"], o="I", neo=[0, ""], src=[["2025 Annual Report to Members", AR25], ["USAA Bank", BANK]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & patents", "blurb": "3,000+ patents, 240 in AI.", "div": "usaa", "rev": "corp", "products": [
            P("patents", "Patents & RDC licensing", "More than 3,000 issued patents, 240 of them in AI. Deposit@Mobile patents are licensed to other banks (Truist settlement October 2023) and a full cross-licence with Bank of America was signed in August 2026, covering AI, security, payment processing and mobile deposit.",
              s=["con"], o="B", neo=[0, ""], src=[["2025 Annual Report to Members", AR25], ["USAA: BofA cross-licence, Aug 2026", BOFA], ["USAA: Truist settlement, Oct 2023", TRUIST]]),
            P("tech", "Core technology & cyber", "Nearly 8 billion cyberthreats blocked in 2025; a new CIO from Santander US to modernise platforms and cybersecurity (February 2026); machine learning in claims and underwriting.",
              s=["con"], st="new", neo=[0, ""], src=[["2025 Annual Report to Members", AR25], ["USAA: Griffiths CIO, Feb 2026", CIO]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Member value, $500m pledge.", "div": "usaa", "rev": "corp", "products": [
            P("strategy", "Member value strategy", "Andrade's 'deliberate choice' to put members first: record returns, auto premium cuts for about half of policyholders in 2026, better card rewards and savings rates, more branches and ATMs on bases, and Honor Through Action, $500 million over five years for military families (November 2025).",
              s=["con", "vet"], st="new", ay="2025", neo=[0, ""], src=[["2025 Annual Report to Members", AR25], ["USAA: Honor Through Action", HTA], ["USAA: rewards in 2025, Dec 2025", REW25]]),
            P("deals", "Deals", "Sold asset management to Victory Capital ($850 million ⚠, 2019) and brokerage to Charles Schwab ($1.8 billion, closed 2020); agreed to buy usage-based insurer Noblr (June 2021); patent licences and the BofA cross-licence (2023–26).",
              s=["con"], o="A", neo=[0, ""], src=[["ThinkAdvisor: Schwab deal, Jul 2019", SCHWAB], ["Military Wallet: Victory and Schwab ⚠", VICTORY], ["USAA: Noblr, Jun 2021", NOBLR]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Visa debit, six Visa credit cards and three American Express cards for more than 4 million cardholders, a Mastercard relationship that ended in 2016, Zelle, and patented mobile deposit with a 100,000-ATM network.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Visa since 2016.", "div": "fsb", "rev": "bank", "products": [
            P("debit", "USAA Bank debit card", "The Classic Checking debit card, accepted 'with all merchants who accept Visa', with Visa Secure online, contactless cards and Apple Pay, Google Pay and Samsung Pay. Converted from Mastercard in 2016.", short="Debit (Visa)",
              s=["con", "vet", "young"], lc="everyday", ay="2016", o="P", at="Visa", neo=[0, "Visa."],
              src=[["USAA: debit cards", DEBIT], ["American Banker: Visa replaces Mastercard, Oct 2015", AB15]]),
            P("wallets", "Digital wallets & tokens", "Debit and credit cards in Apple Pay, Google Pay and Samsung Pay; contactless cards sent on every renewal or replacement; Visa Secure for online purchases.",
              s=["con", "young"], lc="everyday", o="P", at="Visa, Apple, Google, Samsung", neo=[0, "Visa tokens."], src=[["USAA: debit cards", DEBIT]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Visa credit cards", "blurb": "Six cards, new Eagle Adapt.", "div": "fsb", "rev": "bank", "products": [
            P("eagleadapt", "Eagle Adapt Visa", "Launched 15 July 2026: 3% cash back on the first $3,000 a quarter in groceries, dining, gas, home improvement and similar, 1% otherwise, no annual fee, and a $200 welcome bonus ⚠.", short="Eagle Adapt (Visa)",
              s=["con", "vet"], lc="borrow", st="new", ay="Jul 2026", o="P", at="Visa", neo=[0, "Visa."],
              src=[["USAA: new rewards cards, Jul 2026", CARDS26], ["Doctor of Credit: Eagle Adapt ⚠", DOC]]),
            P("visacredit", "Eagle Navigator, Preferred Cash, Rewards, Rate Advantage & Secured Visa", "The rest of the Visa family: travel (Eagle Navigator), flat cash back (Preferred Cash Rewards), points (Rewards), low-rate (Rate Advantage) and a secured card for credit building. Foreign transaction fees were dropped when the cards moved to Visa in 2016.", short="Visa credit family",
              s=["con", "vet", "young"], lc="borrow", ay="2016", o="P", at="Visa", neo=[0, "Visa."],
              mc="USAA's card book of $18.6 billion sits on Visa and Amex; a re-tender is the only way back for the brand.",
              src=[["USAA: credit cards", CC], ["American Banker: Visa replaces Mastercard, Oct 2015", AB15], ["FDIC BankFind: USAA FSB", FDIC]]),
        ]},
        {"id": "2.3", "ic": "gem", "name": "American Express cards", "blurb": "The military-base card.", "div": "fsb", "rev": "bank", "products": [
            P("cashbackplus", "Cashback Rewards Plus American Express", "The flagship military card, refreshed in December 2025 and July 2026: 5% on the first $5,000 of on-base purchases and the first $3,000 of gas, 3% on the first $3,000 of groceries, no annual fee; projected to pay nearly $2 million more in rewards in 2026.", short="Cashback Plus (Amex)",
              s=["con", "vet"], lc="borrow", st="new", ay="Jul 2026", o="P", at="American Express", neo=[0, "American Express."],
              src=[["USAA: new rewards cards, Jul 2026", CARDS26], ["2025 Annual Report to Members", AR25]]),
            P("eagleascend", "Eagle Ascend & Rewards American Express", "Eagle Ascend (July 2026) for members early in their credit journey: 2% on the top monthly category, a credit-limit review in six months and a Walmart+ credit; plus the USAA Rewards American Express points card. American Express network offers come with both.",
              s=["young", "con"], lc="borrow", st="new", ay="Jul 2026", o="P", at="American Express", neo=[0, "American Express."],
              src=[["USAA: new rewards cards, Jul 2026", CARDS26], ["USAA: credit cards", CC]]),
        ]},
        {"id": "2.4", "ic": "refresh-cw", "name": "The Mastercard years", "blurb": "About 30 years, ended 2016.", "div": "fsb", "rev": "bank", "products": [
            P("mcexit", "Former Mastercard portfolio", "Mastercard carried USAA's credit and debit cards for 'roughly 30 years' until USAA moved the whole portfolio to Visa through 2016 (announced 26 October 2015). Mastercard said the economics 'did not make sense' and that it would keep 'certain processing and other services'; whether any remain is not public ⚠.", short="Mastercard (to 2016)",
              s=["con", "vet"], lc="everyday", st="retired", ay="Oct 2015", o="P", at="Mastercard", neo=[None, "Some processing kept in 2015 ⚠ status unknown."],
              mc="The defining loss: a whole military portfolio, debit and credit, went to Visa in one move.",
              src=[["PaymentsJournal: USAA switches to Visa, Oct 2015", PJ15], ["American Banker: Visa replaces Mastercard, Oct 2015", AB15]]),
            P("funding", "Account funding by card", "New checking and savings accounts can be funded with up to $100 from a Visa or Mastercard debit or credit card, so members' outside Mastercard cards still touch USAA at onboarding.",
              s=["young", "con"], lc="open", neo=[1, "Accepts Mastercard and Visa."], src=[["USAA: Classic Checking", CHK]]),
        ]},
        {"id": "2.5", "ic": "send", "name": "Zelle & transfers", "blurb": "Higher limits from June 2026.", "div": "fsb", "rev": "bank", "products": [
            P("zelle", "Zelle & external transfers", "Free Zelle in the USAA app, with a higher daily send limit from June 2026, and easier transfers to and from external accounts after members said moving money was too hard; USAA Pay Bills for payees in the US and APO/FPO.",
              s=["con", "vet"], lc="move", st="new", ay="Jun 2026", o="P", at="Zelle (Early Warning)", neo=[0, "Zelle."],
              mc="Zelle is going international and into stablecoins; A2A scam tools are network-neutral ground.",
              src=[["2025 Annual Report to Members", AR25], ["USAA: Classic Checking", CHK], ["Zelle: international expansion", ZELLEINTL]]),
        ]},
        {"id": "2.6", "ic": "landmark", "name": "Mobile deposit & ATMs", "blurb": "Deposit@Mobile, 100,000 ATMs.", "div": "fsb", "rev": "bank", "products": [
            P("rdc", "Deposit@Mobile", "Patented mobile cheque deposit from the USAA app, the technology USAA now licenses to other banks.",
              s=["con", "vet"], lc="everyday", o="B", neo=[0, "USAA's own."], src=[["USAA Bank", BANK], ["USAA: BofA cross-licence, Aug 2026", BOFA]]),
            P("atm", "ATMs & cash", "More than 100,000 preferred ATMs, up to $10 a month of other banks' fees refunded, and about $136 million of ATM fees saved for members in 2025; over-the-counter cash deposits at selected retailers and more base ATMs planned.",
              s=["con", "young"], lc="everyday", st="new", neo=[None, "ATM network not named ⚠."], src=[["USAA: debit cards", DEBIT], ["2025 Annual Report to Members", AR25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every member: fraud defences that blocked 8 billion threats, AI in underwriting and service, USAA Perks and card rewards, shutdown relief and advice, and telematics that price insurance.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & scams", "blurb": "8 billion threats blocked.", "div": "fsb", "rev": "bank", "products": [
            P("fraud", "Fraud monitoring", "24/7 monitoring and alerts on cards and accounts, zero liability, temporary card blocks, biometrics and multifactor log-on; nearly 8 billion cyberthreats blocked in 2025.",
              s=["con", "vet"], lc="everyday", o="B", neo=[0, "USAA's own; Visa Secure online."],
              mc="Scam and identity scoring for transfers could sit beside USAA's own models whatever the card brand.",
              src=[["USAA: debit cards", DEBIT], ["USAA Bank", BANK], ["2025 Annual Report to Members", AR25]]),
            P("scams", "Scam education", "The STOP method (stay cautious, take your time, only trust verified sources, protect your information), proactive fraud emails and member stories of impostor calls stopped.",
              s=["vet", "con"], lc="everyday", neo=[0, ""], src=[["2025 Annual Report to Members", AR25]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & data", "blurb": "240 AI patents.", "div": "usaa", "rev": "corp", "products": [
            P("ai", "AI in service & underwriting", "Fast Track AI waives the medical exam on about 45% of life applications; an AI phone-routing system that understands conversational speech is due in 2026; machine learning and 3D imaging speed claims; the EVA assistant runs inside the app.",
              s=["con", "driver"], lc="everyday", st="new", o="B", neo=[0, ""],
              mc="An AI-heavy insurer-bank with 240 AI patents is natural ground for Agent Pay, if tokens stay network-agnostic.",
              src=[["2025 Annual Report to Members", AR25], ["USAA: modernised app, Apr 2022", APP22], ["Mastercard: Agent Pay, Apr 2025", AGENTPAY]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & Perks", "blurb": "$1.24bn saved through Perks.", "div": "alliance", "rev": "bank", "products": [
            P("perks", "USAA Perks", "A member discount programme for shopping, travel, cars, home, health and moving that saved members $1.24 billion over five years (2020–24), run by USAA Alliance Services.",
              s=["con", "vet"], lc="beyond", o="P", neo=[0, ""],
              mc="Card-linked offers could extend Perks to the card; Mastercard's offers platforms are not tied to the brand.",
              src=[["2025 Annual Report to Members", AR25]]),
            P("cardrewards", "Card rewards & Shop With Rewards", "Reward redemptions by USAA Bank cardholders rose 47% in 2025, led by Shop With Rewards, which uses points against gas, grocery or retail spending; Amex cardholders also get American Express network offers.",
              s=["con", "young"], lc="borrow", st="new", neo=[0, "Visa and Amex cards."], src=[["USAA: new rewards cards, Jul 2026", CARDS26]]),
        ]},
        {"id": "3.4", "ic": "hand-coins", "name": "Relief & advice", "blurb": "$465m of shutdown relief.", "div": "fsb", "rev": "bank", "products": [
            P("relief", "Financial relief", "Nearly $450 million of no-interest loans, payment extensions and fee waivers for more than 127,000 members in the October 2025 shutdown, rising to about $465 million by March 2026; disaster payment and loan deferrals.",
              s=["con"], lc="borrow", st="new", ay="Oct 2025", o="B", neo=[0, ""], src=[["2025 Annual Report to Members", AR25]]),
            P("advice", "Advice & military life", "About 24 million advice interactions with members in 2025, PCS move planning, deployment checklists, SCRA benefits applied automatically and the USAA Educational Foundation.",
              s=["con", "young", "vet"], lc="open", neo=[0, ""], src=[["2025 Annual Report to Members", AR25]]),
        ]},
        {"id": "3.5", "ic": "gauge", "name": "Telematics & prevention", "blurb": "SafePilot, Connected Home.", "div": "pcco", "rev": "pc", "products": [
            P("safepilot", "SafePilot & Connected Home", "SafePilot and SafePilot Miles telematics save an average of $200 per six-month policy; Connected Home sensors detected more than 40,000 water leaks and electrical hazards; Noblr added usage-based pricing (2021).",
              s=["driver"], lc="beyond", o="A", neo=[0, ""], src=[["2025 Annual Report to Members", AR25], ["USAA 2025 annual report release", AR25REL], ["USAA: Noblr, Jun 2021", NOBLR]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What members buy: auto and home insurance from the fifth-largest US auto insurer, life and health cover, $92 billion of fee-free deposits, card, auto and home lending, and investments now mostly through Schwab.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Property & casualty", "blurb": "Fifth-largest auto insurer.", "div": "pcco", "rev": "pc", "products": [
            P("autoins", "Auto & property insurance", "The fifth-largest US auto insurer, plus home, renters, umbrella and small-business cover; 62 catastrophes and nearly $5 billion of losses in 2025; bundling saved $1.2 billion; about half of policyholders due an auto premium cut in 2026.",
              s=["driver", "home"], lc="beyond", neo=[0, ""],
              mc="Claims payments for millions of policyholders are a disbursement flow, today paid by USAA's own rails.",
              src=[["2025 Annual Report to Members", AR25], ["USAA 2025 annual report release", AR25REL]]),
        ]},
        {"id": "4.2", "ic": "users-round", "name": "Life & health", "blurb": "Fast Track life cover.", "div": "lifeco", "rev": "life", "products": [
            P("life", "Life, annuities & Medicare", "USAA Life term and whole life (including Secure Start for children, July 2026), annuities, military riders, Trust & Will estate planning and a Medicare marketplace.",
              s=["saver", "vet"], lc="grow", st="new", neo=[0, ""], src=[["2025 Annual Report to Members", AR25]]),
        ]},
        {"id": "4.3", "ic": "wallet", "name": "Deposits", "blurb": "$92bn, no monthly fees.", "div": "fsb", "rev": "bank", "products": [
            P("deposits", "Checking, savings & youth accounts", "Classic Checking and savings with no monthly fees and $25 to open, CDs, youth spending accounts and pay up to two days early; deposits of $92.0 billion at 30 June 2026; a new checking product and better savings rates planned.",
              s=["con", "young", "saver"], lc="everyday", neo=[0, "Visa debit."], src=[["USAA: Classic Checking", CHK], ["FDIC BankFind: USAA FSB", FDIC], ["2025 Annual Report to Members", AR25]]),
        ]},
        {"id": "4.4", "ic": "coins", "name": "Lending", "blurb": "Cards, cars, VA loans.", "div": "fsb", "rev": "bank", "products": [
            P("cardbook", "Credit-card lending", "$18.6 billion of card loans at 30 June 2026, more than 4 million cardholders, and APRs below the industry average that USAA says saved members about $500 million of interest in 2025.",
              s=["con", "vet"], lc="borrow", neo=[0, "Visa and Amex."], src=[["FDIC BankFind: USAA FSB", FDIC], ["USAA: new rewards cards, Jul 2026", CARDS26], ["2025 Annual Report to Members", AR25]]),
            P("autoloans", "Auto & personal loans", "$17.4 billion of auto loans, plus personal, RV, boat and motorcycle loans; a combined car search, lending and insurance experience is in the works.",
              s=["driver"], lc="borrow", neo=[0, ""], src=[["FDIC BankFind: USAA FSB", FDIC], ["2025 Annual Report to Members", AR25]]),
            P("mortgages", "VA & home loans", "VA, conventional and refinance mortgages, mostly sold rather than held ($3.2 billion on the balance sheet) ⚠; USAA Agent Connection, powered by HomeStory, offers vetted agents and commission credits (September 2026).",
              s=["home"], lc="borrow", st="new", ay="Sep 2026", o="P", at="HomeStory", neo=[0, ""], src=[["USAA: Agent Connection, Sep 2026", AGENT], ["FDIC BankFind: USAA FSB", FDIC]]),
        ]},
        {"id": "4.5", "ic": "chart-column", "name": "Investments", "blurb": "Schwab since 2020.", "div": "uis", "rev": "corp", "products": [
            P("invest", "Investments & retirement", "Brokerage and managed portfolios sold to Charles Schwab for $1.8 billion (closed 2020) and funds to Victory Capital; USAA Investment Services still offers brokerage, IRAs, 529s and automated investing on usaa.com ⚠ partly referral-based.",
              s=["saver"], lc="grow", st="retired", o="P", at="Charles Schwab", neo=[0, ""], src=[["ThinkAdvisor: Schwab deal, Jul 2019", SCHWAB], ["2025 Annual Report to Members", AR25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How members reach USAA: one app for banking and insurance, contact centres in seven US cities and four overseas, a small base footprint about to grow, and partners from HomeStory to American Express.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "USAA Mobile App", "blurb": "Banking and insurance in one.", "div": "usaa", "rev": "corp", "products": [
            P("app", "USAA Mobile App", "One app for banking, insurance and claims, with mobile deposit, Zelle, bill pay and the EVA assistant; nearly 10 million unique users in 2022 ⚠ no newer figure; tools to see all accounts in one place are being expanded.",
              s=["con", "vet", "young"], lc="everyday", o="B", neo=[0, ""], src=[["USAA: modernised app, Apr 2022", APP22], ["2025 Annual Report to Members", AR25]]),
        ]},
        {"id": "5.2", "ic": "headset", "name": "Contact centres", "blurb": "7 US cities, 4 overseas.", "div": "usaa", "rev": "corp", "products": [
            P("contact", "Phone & service centres", "More than 36,000 employees in seven US cities and four overseas locations (July 2026), with Chesapeake staff expanding (June 2025) and AI phone routing coming in 2026.",
              s=["con", "vet"], lc="open", neo=[0, ""], src=[["USAA: new rewards cards, Jul 2026", CARDS26], ["USAA: Chesapeake, Jun 2025", CHES], ["2025 Annual Report to Members", AR25]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Military bases", "blurb": "More branches planned.", "div": "fsb", "rev": "bank", "products": [
            P("bases", "Branches & ATMs on bases", "A small physical footprint (two FDIC-listed offices) that USAA Bank plans to expand with more branches and ATMs on military bases; the Cashback Rewards Plus card pays 5% on base spending.",
              s=["con", "young"], lc="open", st="new", neo=[0, ""], src=[["2025 Annual Report to Members", AR25], ["FDIC BankFind: USAA FSB", FDIC]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Partners", "blurb": "HomeStory, Amex, Trust & Will.", "div": "usaa", "rev": "corp", "products": [
            P("partners", "Partners & marketplaces", "HomeStory for estate agents, Trust & Will for wills, Medicare carriers, Schwab for investing, and American Express and Visa for the cards.",
              s=["home", "saver"], lc="beyond", o="P", neo=[0, ""], src=[["USAA: Agent Connection, Sep 2026", AGENT], ["2025 Annual Report to Members", AR25], ["USAA: new rewards cards, Jul 2026", CARDS26]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at USAA", "blurb": "Thirty years, then Visa.", "products": [
        P("mcatusaa", "Mastercard at USAA", "Mastercard carried USAA's credit and debit cards for about 30 years until USAA moved the whole portfolio to Visa through 2016. Today debit is Visa and the nine credit cards are six Visa and three American Express. Mastercard said in 2015 it would keep some processing ⚠; no joint initiative has been announced since.",
          s=["con"], div="fsb", rev="bank", mc="The relationship this map is drawn for.",
          src=[["PaymentsJournal: USAA switches to Visa, Oct 2015", PJ15], ["USAA: credit cards", CC], ["USAA: debit cards", DEBIT]]),
    ]},
    {"id": "pillar-market", "name": "US cards and banking", "blurb": "Issuers, interchange, open banking.", "products": [
        P("market", "The US market", "USAA is outside the top eight card issuers by 2025 purchase volume (Chase $1.4 trillion to Barclays about $100 billion); the Credit Card Competition Act was reintroduced in January 2026; and a new Section 1033 open-banking proposal went to OIRA in August 2026.",
          s=["con"], div="usaa", rev="corp", src=[["WTOP: biggest US card companies, Mar 2026", NILSON], ["Congress.gov: S.3623", CCCA], ["Consumer Finance Monitor: Section 1033, Aug 2026", S1033]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
