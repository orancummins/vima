"""Bank of America's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the Q3 2026 results (14 October 2026), the 2025
Form 10-K (25 February 2026) and the Investor Day (5 November 2025). ``neo`` is the Mastercard lens:
[depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q3 = "https://www.sec.gov/Archives/edgar/data/70858/000007085826000481/bac09302026ex991.htm"
Q3S = "https://www.sec.gov/Archives/edgar/data/0000070858/000007085826000481/bac-09302026ex993.htm"
Q3P = "https://www.sec.gov/Archives/edgar/data/70858/000007085826000481/bac09302026ex992.htm"
Q4 = "https://www.sec.gov/Archives/edgar/data/70858/000007085826000020/bac12312025ex991.htm"
K25 = "https://www.sec.gov/Archives/edgar/data/70858/000007085826000157/bac-20251231.htm"
FACTS = "https://newsroom.bankofamerica.com/content/newsroom/company-overview/bank-of-america-fast-facts.html"
RATINGS = "https://investor.bankofamerica.com/fixed-income/credit-ratings"
NR = "https://newsroom.bankofamerica.com/content/newsroom/"
LEAD = NR + "press-releases/2025/09/bank-of-america-announces-senior-leadership-changes.html"
BIOS = NR + "executive-bios.html"
CDN = "https://d1io3yog0oux5.cloudfront.net/_c9b25c8cee0ccacc5ccbdc9655b1ed01/bankofamerica/db/968/"
IDFIN = CDN + "10420/file_upload/BofAInvestorDay_FinancialOverview_ADA.pdf"
IDPAY = CDN + "10413/file_upload/BofAInvestorDay_EnterprisePlatforms_ADA.pdf"
IDCON = CDN + "10426/file_upload/BofAInvestorDay_Consumer_ADA.pdf"
CARDS = "https://www.bankofamerica.com/credit-cards/"
BIZCARDS = "https://business.bankofamerica.com/en/credit-cards"
FIFA = NR + "press-releases/2025/12/bofa-offers-exclusive-fifa-world-cup-2026--custom-card-design-an.html"
VISASWEEP = NR + "press-releases/2026/03/bofa-teams-with-visa-to-offer-cardholders-a-chance-to-win-a-trip.html"
SUMMIT = NR + "press-releases/2025/08/alaska-airlines-and-bank-of-america-present-a-new-premium-credit.html"
ALASKA = NR + "press-releases/2026/04/alaska-air-group-and-bank-of-america-expand-long-standing-credit.html"
REWARDS = NR + "press-releases/2026/02/new-bofa-rewards--program-to-reach-millions-more-clients-with-ex.html"
REWARDS3M = NR + "press-releases/2026/07/3-million--clients-enroll-in-new-bofa-rewards--program-in-first-.html"
PAYPLAN = NR + "press-releases/2026/06/bank-of-america-introduces-new-ways-to-reward-clients--manage-pa.html"
DIGITAL = NR + "press-releases/2026/03/bofa-ai-and-digital-innovations-fuel-30-billion-client-interacti.html"
ERICA3B = NR + "press-releases/2025/08/a-decade-of-ai-innovation--bofa-s-virtual-assistant-erica-surpas.html"
ERICAASSIST = NR + "press-releases/2026/07/bank-of-america-enhances-ericaassist-with-generative-ai-to-help-.html"
PAZE = NR + "press-releases/2024/12/paze-checkout-solution-makes-online-shopping-fast-and-streamline.html"
ZELLEINTL = "https://www.zelle.com/press-releases/zelle-goes-international-early-warning-expands-1t-payments-network-stablecoin"
EWS = "https://earlywarning.com/press-releases"
XBRTP = NR + "press-releases/2026/06/bank-of-america-to-launch-cross-border-real-time-payments---expa.html"
BRADESCO = NR + "press-releases/2026/09/bradesco-completes-first-pilot-transaction-using-bofa-s-cross-bo.html"
RTP = NR + "press-releases/2026/09/bofa-clients-accelerate-rtp--use--led-by-liquidity-management.html"
INSIGHTS = NR + "press-releases/2026/09/bank-of-america-launches-payments-insights-for-cashpro--clients.html"
ASKGPS = NR + "press-releases/2026/09/bank-of-america-expands--ask-global-payments-solutions--with-new.html"
AGENTIC = NR + "press-releases/2026/09/global-banks-collaborate-on-principles-for-trusted-agentic-comme.html"
VPD = NR + "press-releases/2024/10/bofa-unveils-virtual-payables-solution-to-support-the-booming-b2.html"
JDP = NR + "press-releases/2026/02/bofa-merchant-services-ranks-no--1-by-j-d--power-for-customer-sa.html"
NETWORKS = "https://merchanthelp.bankofamerica.com/Merchant_Services_Payment_Methods_and_Networks_Support"
JV = "https://www.paymentsjournal.com/bank-of-america-and-first-data-to-unwind-joint-venture/amp/"
STARBUCKS = NR + "press-releases/2024/02/bank-of-america-and-starbucks-launch-loyalty-partnership.html"
MDSEC = NR + "press-releases/2026/07/bank-of-america-to-acquire-information-security-consultancy-mdse.html"
JIO = NR + "press-releases/2026/08/bank-of-america-enters-into-a-joint-venture-agreement-with-jio-f.html"
TRAVEL = NR + "press-releases/2026/07/book-your-next-getaway--new-bank-of-america-travel-center-makes-.html"
EPI2007 = "https://www.electronicpaymentsinternational.com/news/bank-of-america-aids-mastercard-in-debit-battle-with-visa/"
WALLETHUB = "https://wallethub.com/answers/cc/what-type-of-card-is-bank-of-america-1000183-2140795837/"
REUTERS = "https://finance.yahoo.com/news/bofa-appoints-co-presidents-ceo-202636986.html"
APAC = NR + "press-releases/2026/06/bank-of-america-highlights-surging-demand-for-ai-led-treasury--f.html"
DEBIT = "https://www.bankofamerica.com/deposits/checking/debit-card/"
STABLE = "https://www.benzinga.com/content/43993234/bank-of-america-ceo-hints-at-launching-dollar-pegged-bofa-stablecoins"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · heritage · technology", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $2 trillion of deposits and nearly 70 million clients, the bank that launched BankAmericard in 1958, $1.2 billion of anti-money-laundering consent orders in October 2026, a $14 billion technology budget, and Investor Day targets of 16–18% ROTCE.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "$2 trillion of deposits.", "div": "bac", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Deposits of $2.039 trillion and loans of $1.251 trillion at 30 September 2026; Q3 2026 revenue of $30.0 billion and net income of $6.9 billion (ROTCE 12.6%, CET1 10.9%); net income of $30.5 billion in 2025; market value $376.8 billion at 30 September 2026; rated A1/A-/AA- at the holding company (14 October 2026).",
              s=["corp"], neo=[0, ""], src=[["Q3 2026 results", Q3], ["Q3 2026 supplement", Q3S], ["Q4 2025 results", Q4], ["BofA: credit ratings", RATINGS]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Moynihan and two co-presidents.", "div": "bac", "rev": "other", "products": [
            P("leadership", "Leadership", "Chair and CEO Brian Moynihan, who plans to stay through the end of the decade; co-presidents Dean Athanasia and Jim DeMare since September 2025; CFO Alastair Borthwick; Holly O'Neill runs consumer, Sharon Miller business banking and merchant services, and Mark Monaco Global Payments Solutions. About 210,000 staff.",
              s=["corp"], neo=[0, ""], src=[["Leadership changes, Sep 2025", LEAD], ["Executive bios", BIOS], ["Reuters: co-presidents, Sep 2025", REUTERS]]),
        ]},
        {"id": "1.3", "ic": "flag", "name": "Heritage & regulation", "blurb": "BankAmericard, 1958.", "div": "bac", "rev": "other", "products": [
            P("heritage", "Heritage", "BankAmericard launched in 1958 and was spun out as Visa in 1976; Merrill's cash management account in 1977, CashPro in 1999 and the first mobile app in 2007. The group was built from NationsBank, BankAmerica, FleetBoston, MBNA, Countrywide and Merrill Lynch ⚠ dates not re-checked.",
              s=["con"], o="I", neo=[0, "Visa began as BankAmericard."],
              mc="Visa was born inside this bank.",
              src=[["Investor Day: payments, Nov 2025", IDPAY]]),
            P("orders", "Consent orders", "In October 2026 the bank consented to OCC and FinCEN orders on its anti-money-laundering and sanctions programmes and took a $1.2 billion charge; it also faces Zelle fraud litigation.",
              s=["corp"], st="new", ay="Oct 2026", neo=[0, ""], src=[["Q3 2026 results", Q3], ["Q3 2026 presentation", Q3P]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "$14 billion a year.", "div": "bac", "rev": "other", "products": [
            P("tech", "Technology & AI", "$14 billion a year on technology, more than $4.1 billion of it on new initiatives including AI; about 60,000 technology staff; 8,600 patents granted or pending, about 1,700 of them in AI; more than 30 AI uses live and 300 more in development ⚠ another release says $13 billion.",
              s=["corp"], neo=[0, ""], src=[["BofA fast facts, Jul 2026", FACTS], ["APAC treasury release, Jun 2026", APAC]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "ROTCE 16–18% target.", "div": "bac", "rev": "other", "products": [
            P("strategy", "Investor Day targets", "Medium-term targets set on 5 November 2025: ROTCE of 16–18%, efficiency ratio of 55–59%, EPS growth above 12%, deposits up 4%+ and loans up 5%+ a year; card penetration of credit-eligible checking clients from 71% to 80%.",
              s=["corp"], st="new", ay="Nov 2025", neo=[0, ""], src=[["Investor Day: financial overview", IDFIN], ["Investor Day: consumer", IDCON]]),
            P("acq", "Deals", "Agreed to buy MDSec, a UK cybersecurity consultancy (July 2026), and up to 49.9% of Jio Credit in India for about $1.9 billion (August 2026); the merchant joint venture with First Data was unwound from June 2020.",
              s=["corp"], o="A", st="new", neo=[0, ""], src=[["MDSec, Jul 2026", MDSEC], ["Jio Credit, Aug 2026", JIO], ["Payments Journal: JV unwind ⚠", JV]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Visa consumer and co-brand credit with a Mastercard BankAmericard ⚠ and cruise card, Mastercard small-business cards, Visa debit ⚠, Zelle and Paze, CashPro and real-time payments, and its own merchant acquiring.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Consumer credit", "blurb": "Mostly Visa; #4 issuer.", "div": "bofa", "rev": "consumer", "products": [
            P("cashrewards", "Customized Cash & Unlimited Cash Rewards", "No-fee cash-back cards, 3% in a chosen category or 1.5% flat; part of 39 million consumer cards, $101 billion of loans and $374 billion of annual purchases, making BofA the fourth-largest US card issuer by loans.", short="Cash Rewards (Visa)",
              s=["card"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              mc="The flagship cards, and the bank's 2026 FIFA marketing, are Visa's.",
              src=[["BofA credit cards", CARDS], ["Investor Day: consumer", IDCON], ["FIFA card designs, Dec 2025", FIFA]]),
            P("travelcards", "Travel Rewards, Premium Rewards & Premium Rewards Elite", "Travel and premium points cards from no fee to $550 ⚠ network read from card-art file names.", short="Travel & Premium (Visa ⚠)",
              s=["card"], lc="borrow", o="P", at="Visa", neo=[0, "Visa ⚠ from card art."], src=[["BofA credit cards", CARDS]]),
            P("bankamericard", "BankAmericard", "A low-rate card with 0% introductory APR for 21 cycles ⚠ Mastercard, from card art and WalletHub.", short="BankAmericard (Mastercard ⚠)",
              s=["card"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard ⚠ from card art."], src=[["BofA credit cards", CARDS], ["WalletHub: card network, Sep 2026 ⚠", WALLETHUB]]),
            P("custompay", "Custom Pay Plan", "Card instalments for a fixed monthly fee instead of interest, over 3 to 18 months, keeping rewards (June 2026).",
              s=["card"], lc="borrow", st="new", ay="Jun 2026", o="B", neo=[0, "BofA's own."],
              mc="Built in-house rather than on Mastercard Installments.",
              src=[["Custom Pay Plan, Jun 2026", PAYPLAN]]),
        ]},
        {"id": "2.2", "ic": "plane", "name": "Co-brand cards", "blurb": "Atmos on Visa; NCL on Mastercard.", "div": "bofa", "rev": "consumer", "products": [
            P("atmos", "Atmos Rewards Ascent & Summit", "Alaska and Hawaiian Airlines cards on Visa Signature and Visa Infinite; Summit launched August 2025; the partnership was extended in April 2026 with BofA moving towards being the single issuer of all Atmos cards.", short="Atmos (Visa)",
              s=["card"], lc="borrow", o="P", at="Alaska Air Group, Visa", neo=[0, "Visa."],
              mc="If Hawaiian's Mastercard cards fold into Atmos, Mastercard could lose that volume ⚠ inference.",
              src=[["Atmos Summit launch, Aug 2025", SUMMIT], ["Alaska extension, Apr 2026", ALASKA]]),
            P("cobrands", "Royal Caribbean, Air France KLM & Allegiant", "Royal ONE, Air France KLM and Allways Rewards cards, all on Visa.", short="Travel co-brands (Visa)",
              s=["card"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["BofA credit cards", CARDS]]),
            P("ncl", "Norwegian Cruise Line World Mastercard", "No-fee cruise card earning 3 WorldPoints per $1 on NCL.", short="NCL (Mastercard)",
              s=["card"], lc="borrow", o="P", at="Norwegian Cruise Line, Mastercard", neo=[2, "Mastercard World."], src=[["BofA credit cards", CARDS]]),
        ]},
        {"id": "2.3", "ic": "briefcase-business", "name": "Business & commercial cards", "blurb": "Business Advantage on Mastercard.", "div": "bofa", "rev": "gb", "products": [
            P("bizadvantage", "Business Advantage cards", "Unlimited Cash, Customized Cash and Travel Rewards cards for small businesses, all Mastercard (Travel is World Mastercard).", short="Business Advantage (Mastercard)",
              s=["sme"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's biggest lane at BofA: the whole small-business card line.",
              src=[["BofA small-business cards", BIZCARDS]]),
            P("commercial", "Commercial cards & Virtual Payables Direct", "Corporate, purchasing and virtual cards through Global Card Access, and Virtual Payables Direct in EMEA (October 2024), which pays suppliers by bank transfer with 25–120 days of credit ⚠ network not stated.", short="Commercial cards (network unknown)",
              s=["corp"], lc="move", ay="Oct 2024", neo=[None, "Network not stated."], src=[["Virtual Payables Direct, Oct 2024", VPD], ["Investor Day: payments, Nov 2025", IDPAY]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Debit & wallets", "blurb": "#1 in debit spend ⚠.", "div": "bofa", "rev": "consumer", "products": [
            P("debit", "Debit card", "Consumer debit in Paze, Apple Pay, Google Pay, Samsung Pay and PayPal, with $0 liability; ranked first in US debit spend (Nilson, 2024 ⚠ PIN definition) ⚠ Visa, per third-party sources.", short="Debit (Visa ⚠)",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa ⚠ third-party sources."], src=[["BofA debit card", DEBIT], ["WalletHub: card network, Sep 2026 ⚠", WALLETHUB], ["Investor Day: payments, Nov 2025", IDPAY]]),
            P("wallets", "Cards in mobile wallets", "22 million BofA cards provisioned to mobile wallets (July 2025), out of 95 million debit and credit cards; $266 billion of combined card spend in Q3 2026 (+8%).",
              s=["con", "card"], lc="everyday", neo=[1, "Both networks' tokens."], src=[["Investor Day: consumer", IDCON], ["Q3 2026 results", Q3]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Zelle & Paze", "blurb": "$556bn on Zelle in 2025.", "div": "bofa", "rev": "consumer", "products": [
            P("zelle", "Zelle", "1.8 billion transactions worth $556 billion in 2025; 25.7 million active users and $164 billion in Q3 2026; QR codes and tags for small businesses. BofA co-owns Early Warning, which announced the ZelleUSD stablecoin and an India corridor in June 2026.",
              s=["con", "sme"], lc="move", o="P", at="Early Warning Services", neo=[0, "Bank-owned rail."],
              mc="Competes with Mastercard Send and Move for payouts and remittances.",
              src=[["Digital interactions, Mar 2026", DIGITAL], ["Q3 2026 results", Q3], ["Zelle goes international, Oct 2025", ZELLEINTL], ["Early Warning releases", EWS]]),
            P("paze", "Paze", "Early Warning's tokenised checkout wallet, with no merchant fee; all eligible BofA cards enabled by 6 December 2024.",
              s=["con", "card"], lc="move", ay="Dec 2024", o="P", at="Early Warning Services", neo=[0, "Bank-owned wallet; competes with Click to Pay."], src=[["Paze rollout, Dec 2024", PAZE]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Treasury payments", "blurb": "CashPro, RTP, cross-border.", "div": "gps", "rev": "gb", "products": [
            P("cashpro", "CashPro", "Payments, liquidity, FX and trade for more than 35,000 clients; $1.2 trillion of payment approvals in the app in 2025 and $358 billion in Q3 2026 (+20%). Global Payments Solutions earned $11 billion in 2024.",
              s=["corp"], lc="move", neo=[0, ""], src=[["BofA fast facts, Jul 2026", FACTS], ["Q3 2026 results", Q3], ["Investor Day: payments, Nov 2025", IDPAY]]),
            P("rtp", "RTP & cross-border real-time payments", "Corporate RTP volume up 48% from January to July 2026; cross-border real-time payments to Mexico's SPEI, UK Faster Payments and India's UPI (June 2026), with a first pilot by Bradesco to Hong Kong (September 2026).",
              s=["corp"], lc="move", st="new", ay="Jun 2026", neo=[0, ""], src=[["RTP growth, Sep 2026", RTP], ["Cross-border RTP, Jun 2026", XBRTP], ["Bradesco pilot, Sep 2026", BRADESCO]]),
            P("wires", "Wires, ACH & bill pay", "$1.9 trillion of wires a day, the largest US ACH receiver, and about $250 billion of bill payments.",
              s=["corp", "con"], lc="move", neo=[0, ""], src=[["BofA fast facts, Jul 2026", FACTS], ["Investor Day: consumer", IDCON]]),
            P("stablecoin", "Stablecoins", "On Global Payments Solutions' list of what comes next; no product yet. Moynihan has said BofA would issue one once it is legal ⚠ membership of the 21-bank venture unverified.",
              s=["corp"], lc="move", st="unconf", neo=[None, "No product yet."],
              mc="Mastercard's BVNK and Global Money Platform fit the roadmap.",
              src=[["Investor Day: payments, Nov 2025", IDPAY], ["Benzinga: BofA stablecoin ⚠", STABLE]]),
        ]},
        {"id": "2.7", "ic": "store", "name": "Merchant services", "blurb": "First for satisfaction, 2026.", "div": "bams", "rev": "consumer", "products": [
            P("bams", "BofA Merchant Services", "Acquiring, processing and settlement, first in J.D. Power's 2026 merchant satisfaction study; accepts Visa, Mastercard, Amex, Discover, UnionPay, JCB and Diners, and routes PIN debit over Maestro, Interlink, STAR, NYCE, PULSE and Accel ⚠ current role of Fiserv and Clover not found.",
              s=["sme"], lc="move", neo=[1, "Accepts every network, Maestro included."], src=[["J.D. Power ranking, Feb 2026", JDP], ["Merchant payment networks", NETWORKS]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud, cyber and credit monitoring, Erica with 24 million users, CashPro's data and AI tools, and BofA Rewards, Deals and a new travel centre.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud, cyber & identity", "blurb": "MDSec, My Credit.", "div": "bac", "rev": "consumer", "products": [
            P("security", "Fraud & cyber security", "Fraud education and 'scaminars', the MDSec purchase (July 2026) and a CISO-led cyber programme, under consent orders and Zelle fraud litigation.",
              s=["con", "corp"], lc="everyday", st="new", neo=[0, "BofA's own."],
              mc="Payee-risk and scam tools for Zelle and RTP are open ground.",
              src=[["MDSec, Jul 2026", MDSEC], ["Q3 2026 presentation", Q3P]]),
            P("mycredit", "My Credit", "FICO score, alerts and identity monitoring, with dark-web and SSN monitoring for BofA Rewards members (June 2026).",
              s=["con"], lc="everyday", st="new", neo=[0, ""], src=[["Custom Pay Plan, Jun 2026", PAYPLAN]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "Erica & AI", "blurb": "24 million Erica users.", "div": "bofa", "rev": "consumer", "products": [
            P("erica", "Erica", "The virtual assistant launched in 2018: 24.2 million active users in Q3 2026 (+18%) and 3.6 billion interactions to date ⚠ other definitions give up to 25.7 million.",
              s=["con"], lc="everyday", neo=[0, ""],
              mc="BofA is shaping agentic-commerce principles; Agent Pay could carry them.",
              src=[["Q3 2026 results", Q3], ["Erica passes 3 billion, Aug 2025", ERICA3B]]),
            P("ericaassist", "EricaAssist & adviser AI", "Generative AI for 18,000 service reps (July 2026), ask MERRILL and ask Private Bank, and an AI meeting assistant (March 2026).",
              s=["wealth"], lc="grow", st="new", neo=[0, ""], src=[["EricaAssist, Jul 2026", ERICAASSIST], ["BofA fast facts, Jul 2026", FACTS]]),
        ]},
        {"id": "3.3", "ic": "code-xml", "name": "Treasury data & APIs", "blurb": "CashPro APIs since 2018.", "div": "gps", "rev": "gb", "products": [
            P("cashproai", "CashPro APIs, data & AI", "CashPro APIs since January 2018; CashPro Chat with Erica, used by 45% of CashPro clients; Payments Insights (September 2026); and AskGPS for about 3,000 payments staff.",
              s=["corp"], lc="move", neo=[0, ""], src=[["Payments Insights, Sep 2026", INSIGHTS], ["AskGPS, Sep 2026", ASKGPS], ["Investor Day: payments, Nov 2025", IDPAY]]),
            P("agentic", "Agentic-commerce principles", "BofA joined global banks setting principles for trusted agentic commerce (22 September 2026); Mark Monaco said it will need careful approaches to identity, authorisation, fraud and liability.",
              s=["corp", "con"], lc="move", st="new", ay="Sep 2026", neo=[None, "No network named."],
              mc="Agent Pay answers the identity and liability questions BofA has raised.",
              src=[["Agentic commerce principles, Sep 2026", AGENTIC]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards & offers", "blurb": "17.6 million in BofA Rewards.", "div": "bofa", "rev": "consumer", "products": [
            P("bofarewards", "BofA Rewards", "Four tiers replacing Preferred Rewards, launched 27 May 2026 with card-rewards bonuses of 10–75%; 17.6 million enrolled by Q3 2026.",
              s=["con", "card"], lc="grow", st="new", ay="May 2026", neo=[0, "BofA's own."], src=[["BofA Rewards announced, Feb 2026", REWARDS], ["3 million enrol, Jul 2026", REWARDS3M], ["Q3 2026 results", Q3]]),
            P("bankamerideals", "BankAmeriDeals & Starbucks", "Card-linked deals since 2012 with more than 15,000 merchants, and Starbucks linked loyalty (February 2024).",
              s=["con", "card"], lc="grow", o="P", at="Starbucks", neo=[0, ""],
              mc="Mastercard card-linked offers could feed the deals engine.",
              src=[["Starbucks partnership, Feb 2024", STARBUCKS], ["BofA Rewards announced, Feb 2026", REWARDS]]),
            P("travelcenter", "BofA Travel Center", "Relaunched July 2026, powered by Rocket Travel by Agoda.",
              s=["card"], lc="beyond", st="new", ay="Jul 2026", o="P", at="Agoda", neo=[0, ""], src=[["Travel Center, Jul 2026", TRAVEL]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: 38.9 million checking accounts and four million small businesses, Merrill and the Private Bank with $5.1 trillion of client balances, Global Banking for most of the Fortune 500, Global Markets, and a growing international arm.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Consumer & small business", "blurb": "38.9 million checking accounts.", "div": "bofa", "rev": "consumer", "products": [
            P("checking", "Checking & deposits", "38.9 million consumer checking accounts, 92% of them primary, after 31 quarters of net growth; the largest US consumer deposit base. Consumer Banking earned $11.6 billion of revenue in Q3 2026.",
              s=["con"], lc="everyday", neo=[0, "Visa debit ⚠."], src=[["Q3 2026 results", Q3], ["Q3 2026 supplement", Q3S], ["Investor Day: consumer", IDCON]]),
            P("smallbiz", "Business Banking", "About four million small-business clients and the largest small-business lender (FDIC); run by Sharon Miller, with merchant services.",
              s=["sme"], lc="everyday", neo=[1, "Mastercard business cards."], src=[["BofA fast facts, Jul 2026", FACTS], ["J.D. Power ranking, Feb 2026", JDP]]),
        ]},
        {"id": "4.2", "ic": "gem", "name": "Wealth", "blurb": "$5.1 trillion of balances.", "div": "merrill", "rev": "gwim", "products": [
            P("merrill", "Merrill Wealth Management & Merrill Edge", "Merrill holds $4 trillion of client balances; about 21,000 net new relationships in 2025 ⚠ adviser count not found.",
              s=["wealth"], lc="grow", neo=[0, ""], src=[["Q4 2025 results", Q4]]),
            P("privatebank", "Bank of America Private Bank", "$759 billion of client balances (Q4 2025); GWIM earned $7.1 billion of revenue in Q3 2026.",
              s=["wealth"], lc="grow", neo=[0, ""], src=[["Q4 2025 results", Q4], ["Q3 2026 supplement", Q3S]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Global Banking", "blurb": "78% of the Global Fortune 500.", "div": "bofa", "rev": "gb", "products": [
            P("globalbanking", "Corporate, investment & commercial banking", "Relationships with 78% of the Global Fortune 500 and 96% of the US Fortune 1,000; Q3 2026 revenue of $6.2 billion; top four globally in investment-banking fees.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["BofA fast facts, Jul 2026", FACTS], ["Q3 2026 supplement", Q3S]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Global Markets", "blurb": "$5.1bn of trading.", "div": "bofas", "rev": "gm", "products": [
            P("markets", "Global Markets", "About 8,000 clients; Q3 2026 sales and trading revenue of $5.1 billion ($2.6 billion FICC, $2.5 billion equities).",
              s=["corp"], lc="grow", neo=[0, ""], src=[["Q3 2026 results", Q3], ["BofA fast facts, Jul 2026", FACTS]]),
        ]},
        {"id": "4.5", "ic": "earth", "name": "International", "blurb": "35 countries, Jio Credit.", "div": "bac", "rev": "gb", "products": [
            P("intl", "International", "Operations in more than 35 countries under Bernard Mensah, with a joint venture for up to 49.9% of Jio Credit in India (August 2026).",
              s=["corp"], lc="borrow", st="new", neo=[0, ""], src=[["BofA fast facts, Jul 2026", FACTS], ["Jio Credit, Aug 2026", JIO]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How clients reach the bank: one app for 42.6 million, 3,531 financial centres and about 15,000 ATMs, CashPro and BA360 for companies, and partners from Alaska Airlines to Starbucks.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Mobile app", "blurb": "50 million digital users.", "div": "bofa", "rev": "consumer", "products": [
            P("app", "Bank of America app", "42.6 million active mobile users and 50 million active digital users; banking, investing and retirement in one app since 2024; 71% of consumer sales are digital.",
              s=["con", "card", "wealth"], lc="everyday", neo=[0, ""], src=[["Q3 2026 presentation", Q3P], ["Q3 2026 results", Q3]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Financial centres", "blurb": "3,531 centres.", "div": "bofa", "rev": "consumer", "products": [
            P("centres", "Financial centres & ATMs", "3,531 financial centres and 14,965 ATMs at 30 September 2026.",
              s=["con", "sme"], lc="open", neo=[0, ""], src=[["Q3 2026 supplement", Q3S]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "Platforms & partners", "blurb": "CashPro app, BA360.", "div": "gps", "rev": "gb", "products": [
            P("platforms", "CashPro app, BA360 & Global Card Access", "The business platforms for treasury, small-business and card programme clients.",
              s=["corp", "sme"], lc="move", neo=[0, ""], src=[["Investor Day: payments, Nov 2025", IDPAY]]),
            P("partners", "Partners", "Alaska Airlines and Atmos, Royal Caribbean, Norwegian Cruise Line, Air France KLM, Allegiant, Volvo, Starbucks and Agoda.",
              s=["card"], lc="open", o="P", neo=[1, "NCL on Mastercard; the rest Visa."], src=[["BofA credit cards", CARDS], ["Investor Day: payments, Nov 2025", IDPAY]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BofA", "blurb": "Small-business cards, a cruise card.", "products": [
        P("mcatbofa", "Mastercard at Bank of America", "The bank that started BankAmericard runs a Visa-led consumer book: the flagship cash, travel and premium cards, the airline and cruise co-brands bar one, and debit ⚠. Mastercard carries the whole Business Advantage small-business line, the NCL World Mastercard and, it appears, the BankAmericard ⚠, and is accepted and routed through BofA Merchant Services. No joint programme since 2015 was found; a 2007 pricing deal is the last public one.",
          s=["card"], div="bac", rev="other", mc="The relationship this map is drawn for.",
          src=[["BofA credit cards", CARDS], ["BofA small-business cards", BIZCARDS], ["Visa sweepstakes, Mar 2026", VISASWEEP], ["EPI: BofA and MasterCard, Aug 2007", EPI2007]]),
    ]},
    {"id": "pillar-market", "name": "US banking", "blurb": "Interchange, Zelle, stablecoins.", "products": [
        P("market", "The US market", "Interchange litigation and changes to Visa's and Mastercard's network rules, Zelle fraud litigation, anti-money-laundering consent orders, and a stablecoin regime under the GENIUS Act ⚠ OCC issuer rules reportedly due on 18 January 2027.",
          s=["corp"], div="bac", rev="other", src=[["2025 Form 10-K", K25], ["Q3 2026 presentation", Q3P]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
