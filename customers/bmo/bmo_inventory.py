"""BMO Financial Group's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the Q3 2026 results and MD&A (25 August 2026), the
fiscal 2025 results (4 December 2025) and the 2025 Annual Information Form. BMO's product pages could not be
reached, so card networks come from BMO's press releases. ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

Q3 = "https://newsroom.bmo.com/2026-08-25-BMO-Financial-Group-Reports-Third-Quarter-2026-Results"
MDA = "https://www.sec.gov/Archives/edgar/data/0000927971/000092797126000108/q32026mda.htm"
FY25 = "https://newsroom.bmo.com/2025-12-04-BMO-Financial-Group-Reports-Fourth-Quarter-and-Fiscal-2025-Results"
AIF = "https://www.sec.gov/Archives/edgar/data/927971/000119312525307982/d938207dex991.htm"
Q1 = "https://newsroom.bmo.com/2026-02-25-BMO-Financial-Group-Reports-First-Quarter-2026-Results"
INVDAY = "https://www.kitco.com/news/off-the-wire/2026-03-26/bank-montreal-targets-15-return-equity-wealth-us-businesses-growth"
BRANCHES = "https://newsroom.bmo.com/2026-09-04-BMO-Completes-Sale-of-138-U-S-Branches-to-First-Citizens-Bank"
STONEPEAK = "https://newsroom.bmo.com/2026-05-11-BMO-Announces-Strategic-Sale-of-Transportation-and-Vendor-Finance-Businesses"
MONERIS = "https://newsroom.bmo.com/2026-08-10-BMO-Announces-Sale-of-Moneris"
COMMEXP = "https://newsroom.bmo.com/2026-10-01-BMO-and-Mastercard-Enable-Embedded-Commercial-Payments-Directly-Within-Enterprise-Software-Across-North-America"
CADTOK = "https://newsroom.bmo.com/2026-09-22-Six-Canadian-banks-explore-development-of-a-secure-CAD-tokenized-deposit-solution"
AGORA = "https://newsroom.bmo.com/2026-09-29-BMO-Joins-Project-Agora-to-Advance-Cross-Border-Payments-Through-Tokenization"
CME = "https://newsroom.bmo.com/2026-03-24-BMO-Introduces-Tokenized-Cash-and-Deposit-Platform-with-CME-Group-and-Google-Cloud"
AIQ = "https://newsroom.bmo.com/2026-04-09-BMO-Establishes-Institute-for-Applied-Artificial-Intelligence-Quantum"
EVIDENT = "https://newsroom.bmo.com/2026-10-06-BMO-Earns-Top-Recognition-for-Responsible-AI-Leadership-in-Global-Banking"
BLUE = "https://newsroom.bmo.com/2026-06-02-BMO-Launches-Blue-Rewards-A-New,-Bold-and-Rewarding-Loyalty-Experience-for-Canadians"
BLUEJAN = "https://newsroom.bmo.com/2026-01-26-BMO-Boldly-Reimagines-Loyalty-with-Launch-of-Blue-Rewards"
BLUESEP = "https://newsroom.bmo.com/2026-09-08-BMO-Makes-Everyday-Banking-More-Rewarding-with-Enhanced-Blue-Rewards-Benefits"
BLUEINS = "https://newsroom.bmo.com/2026-09-18-Blue-Rewards-Members-Earn-Points-with-BMO-Insurance"
APIS = "https://newsroom.bmo.com/2025-12-02-BMO-Launches-Payment-APIs-To-Power-Embedded-Finance-Experiences-Across-North-America"
WALMART = "https://newsroom.bmo.com/2025-12-03-BMO-and-Walmart-Canada-Team-Up-to-Make-Shopping-Fast,-Convenient-and-Affordable"
AWARDS26 = "https://newsroom.bmo.com/2026-05-26-BMO-Wins-Seven-Awards-for-AI,-Digital-Innovation-and-Client-Experiences,1"
CELENT = "https://newsroom.bmo.com/2025-06-19-BMO-Recognized-with-2025-Celent-Model-Bank-Award-for-Payments-Innovation"
AWARDS25 = "https://newsroom.bmo.com/2025-10-30-BMO-Wins-11-Honours-for-AI-and-Digital-Innovation"
TPSAWARDS = "https://newsroom.bmo.com/2025-12-22-BMO-Recognized-with-Six-Treasury-Payments-Solutions-Awards-in-2025"
PORTER = "https://newsroom.bmo.com/2025-03-24-Porter-Airlines,-BMO-and-Mastercard-Launch-First-Canadian-Credit-Card-Program-Granting-Immediate-Airline-Loyalty-Benefits"
ECLIPSE = "https://newsroom.bmo.com/2020-11-03-BMO-and-Visa-Canada-Collaborate-to-Introduce-Two-New-Reward-Credit-Cards-to-meet-Canadians-Lifestyle-Needs"
RISE = "https://newsroom.bmo.com/2023-12-13-New-BMO-eclipse-rise-Visa-Credit-Card-Helps-Gen-Z-and-Millennials-Build-Good-Financial-Habits"
TRANSIT = "https://newsroom.bmo.com/2023-02-15-BMO-Makes-Public-Transit-Rides-Fee-Free-Across-Canada"
EXTEND = "https://newsroom.bmo.com/2023-08-28-BMO-Launches-Mobile-Wallet-for-Virtual-Cards-with-Mastercard-and-Extend"
TRUENAME = "https://newsroom.bmo.com/2022-03-14-BMO-is-First-Canadian-Financial-Institution-to-Launch-True-Name-TM-by-Mastercard"
USCASH = "https://newsroom.bmo.com/2022-03-15-BMO-Harris-Bank-Refreshes-Cash-Back-Mastercard-with-More-Value-and-Enhanced-Benefits"
WEBIZ = "https://newsroom.bmo.com/2021-11-25-BMO-Introduces-the-First-World-Elite-Mastercard-Credit-Cards-for-Business-Owners-in-Canada"
COMMSUITE = "https://newsroom.bmo.com/2017-04-27-BMO-Financial-Group-Launches-New-Suite-of-Commercial-Mastercard-Offerings,1"
TRUEUS = "https://newsroom.bmo.com/2019-11-08-Mastercard-partners-with-BMO-Harris-and-Superbia-to-bring-the-True-Name-TM-feature-to-their-card-offerings"
BIOMETRIC = "https://newsroom.bmo.com/2016-03-23-BMO-Financial-Group-and-MasterCard-Begin-Roll-Out-of-First-in-Canada-and-U-S-Biometric-Corporate-Card-Program"
PERKS = "https://newsroom.bmo.com/2015-09-28-BMO-Launches-New-Rewards-Program-That-Provides-BMO-MasterCard-Customers-with-a-Personalized-Shopping-Experience"
GLOBALPAY = "https://newsroom.bmo.com/2020-10-09-BMO-Announces-Partnership-with-The-Clearing-House-Launches-Global-Pay-for-U-S-Business-Customers"
INSTACART = "https://newsroom.bmo.com/2025-10-29-BMO-Partners-with-Instacart-to-Deliver-Convenience-and-Savings-for-Canadians"
EUROZ = "https://newsroom.bmo.com/2026-06-29-BMO-to-Acquire-Australia-Based-Capital-Markets-Business-of-Euroz-Hartleys-Group,-Strengthening-Global-Metals-Mining-Leadership"
ASCEND = "https://newsroom.bmo.com/2022-05-10-Travel-is-back-and-the-BMO-AscendTM-World-Elite-Mastercard-is-soaring-to-new-heights"
CFO = "https://newsroom.bmo.com/2025-09-17-BMO-Announces-Retirement-of-Tayfun-Tuzun,-Names-Rahul-Nalgirkar-CFO,-BMO-Financial-Group"
RTR = "https://www.payments.ca/systems-services/payment-systems/real-time-rail-payment-system"
OPENBANK = "https://www.canada.ca/en/department-finance/programs/financial-sector-policy/open-banking-implementation/budget-2025-canadas-framework-for-consumer-driven-banking.html"
FCAC = "https://www.canada.ca/en/financial-consumer-agency/services/banking/open-banking.html"
INTERAC = "https://www.interac.ca/en/about/our-company/"
MKTCAP = "https://stockanalysis.com/stocks/bmo/market-cap/"
ZELLE = "https://newsroom.bmo.com/2020-01-23-BMO-Harris-Bank-Offers-Zelle-R-to-Commercial-Banking-Customers"
APPLEPAY = "https://newsroom.bmo.com/2016-05-10-BMO-Brings-Apple-Pay-to-Canadian-Customers"
MASTERPASS = "https://newsroom.bmo.com/2017-09-25-BMO-Harris-Debuts-Small-Business-Masterpass-TM-Apple-Pay-TM-Android-Pay-TM-and-Samsung-Pay-TM"
NEWSSEP = "https://newsroom.bmo.com/index.php?s=2429&o=10"
QUANTUM = "https://newsroom.bmo.com/2026-04-13-BMO-Announces-Partnership-with-Quantum-Industry-Canada-and-Chicago-Quantum-Exchange"
USDEBIT = "https://newsroom.bmo.com/2019-12-02-BMO-Harris-Bank-announces-availability-of-True-Name-TM-feature-for-Mastercard-debit-cardholders"
ETRANSFER = "https://newsroom.bmo.com/2017-03-01-BMO-Introduces-Free-Unlimited-Interac-e-Transfer-Transactions-for-All-Everyday-Bank-Plans"
BULK = "https://newsroom.bmo.com/2020-09-10-BMO-Introduces-Interac-e-Transfer-Bulk-Receivables-for-Canadian-Commercial-Clients"
INSURE = "https://newsroom.bmo.com/2026-06-15-BMO-Insurance-Launches-New-Health-and-Dental-Insurance-Coverage-and-Care-Plan-for-Canadians,-powered-by-GreenShield"
SMARTDEC = "https://newsroom.bmo.com/2026-07-09-BMO-Insurance-launches-AI-enhanced-SmartDecision-tool-delivering-a-faster-and-more-seamless-path-to-coverage-for-clients-and-advisors"
EMARKETER = "https://newsroom.bmo.com/2026-05-19-BMO-Ranked-First-in-EMARKETERs-2026-Canada-Mobile-Banking-Emerging-Features-Benchmark"
EUROMONEY = "https://newsroom.bmo.com/2026-07-28-BMO-Named-Canadas-Best-Retail-Bank-at-Euromoney-Awards-for-Excellence-2026"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · charter · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: C$1.54 trillion of assets, Canada's first chartered bank (1817), an AI and quantum institute, and a 15% ROE target reached partly by selling businesses in the US.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "C$1.54tn; CET1 13.0%.", "div": "group", "rev": "corp", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of C$1,538.7 billion, deposits of C$1,017.8 billion and net loans of C$697.9 billion at 31 July 2026. Q3 2026 revenue C$9.9 billion; adjusted net income C$2.86 billion (reported C$1.75 billion after a C$962 million charge on the Stonepeak sale); CET1 13.0%. Fiscal 2025 net income C$8.7 billion. About 13 million clients; market value about US$116 billion ⚠.",
              s=["corp"], neo=[0, ""], src=[["Q3 2026 results", Q3], ["Q3 2026 MD&A", MDA], ["Fiscal 2025 results", FY25], ["Stock Analysis: market cap ⚠", MKTCAP]]),
        ]},
        {"id": "1.2", "ic": "badge-check", "name": "Charter & leadership", "blurb": "Canada's first bank, 1817.", "div": "group", "rev": "corp", "products": [
            P("heritage", "Charter & listing", "Began business in Montreal in 1817; a Schedule I bank under the Bank Act. Head office in Montreal, executive offices in Toronto. Listed on the TSX and NYSE. More than 53,000 staff; rated A+/Aa2/AA/AA on deposits.",
              s=["con"], o="I", neo=[0, ""], src=[["Annual Information Form 2025", AIF]]),
            P("leadership", "Executive committee", "CEO Darryl White, CFO Rahul Nalgirkar (from January 2026), chair George Cope. Co-heads of Canadian P&C Mathew Mehrotra and Sharon Haward-Laird; Aron Levine runs U.S. Banking, Deland Kamanga wealth, Alan Tannenbaum capital markets.",
              s=["corp"], neo=[0, ""], src=[["Annual Information Form 2025", AIF], ["BMO: new CFO, Sep 2025", CFO]]),
        ]},
        {"id": "1.3", "ic": "brain", "name": "AI & quantum", "blurb": "An institute, from April 2026.", "div": "group", "rev": "corp", "products": [
            P("aiq", "Institute for Applied AI & Quantum", "An enterprise centre led by Kristin Milchanowski, Chief AI & Quantum Officer, from April 2026. BMO joined the IBM Quantum Network in February 2025, the first Canadian bank to do so.",
              s=["corp"], st="new", ay="Apr 2026", o="B", neo=[0, ""], src=[["BMO: AI & Quantum Institute, Apr 2026", AIQ], ["BMO: quantum partnerships, Apr 2026", QUANTUM]]),
            P("responsibleai", "Responsible AI", "Top responsible-AI scores in the Evident AI Index 2026, and second of 50 banks for AI use-case outcomes.",
              s=["corp"], neo=[0, ""], src=[["BMO: Evident AI recognition, Oct 2026", EVIDENT]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & portfolio", "blurb": "15% ROE; fewer US lines.", "div": "group", "rev": "corp", "products": [
            P("strategy", "Investor Day targets", "At Investor Day on 26 March 2026, BMO set out a line of sight to a 15% ROE. The timing is reported as exiting fiscal 2027 or by 2028 ⚠. Other reported targets are U.S. Banking ROE rising from about 8% to 12% and EPS growth of 7–10% ⚠.",
              s=["corp"], st="new", neo=[0, ""], src=[["Kitco (Reuters): Investor Day, Mar 2026", INVDAY]]),
            P("deals", "Acquisitions", "Bank of the West from BNP Paribas (February 2023, US$13.8 billion), AIR MILES (June 2023, US$160 million), Burgundy Asset Management (November 2025, C$625 million) and the Australian capital-markets business of Euroz Hartleys (agreed June 2026).",
              s=["us", "inv"], o="A", neo=[0, ""], src=[["Annual Information Form 2025", AIF], ["BMO: Euroz Hartleys, Jun 2026", EUROZ]]),
            P("pruning", "Disposals", "138 US branches sold to First Citizens (closed 4 September 2026; about US$5.3 billion of deposits); Transportation and Vendor Finance sold to Stonepeak (agreed May 2026, BMO keeps 19.9%); Moneris to be sold (see Acquiring).",
              s=["us", "corp"], st="flux", neo=[0, ""], src=[["BMO: branch sale closes, Sep 2026", BRANCHES], ["BMO: Stonepeak sale, May 2026", STONEPEAK], ["Q3 2026 MD&A", MDA]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Nine ways money moves: Canadian credit cards mostly on Mastercard with a Visa premium line, commercial and corporate cards on Mastercard, Interac debit, US cards on Mastercard, Interac e-Transfer and RTP, cross-border on Mastercard, tokenised deposits, and Moneris, now for sale.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Canadian credit cards", "blurb": "Mastercard, with Visa eclipse.", "div": "canada", "rev": "cpc", "products": [
            P("bluecard", "BMO Blue Rewards Mastercard cards", "The Blue Rewards World Elite Mastercard and Blue Rewards Mastercard, launched on 2 June 2026. Up to 10 points per dollar on Blue Rewards Travel; welcome offers of up to 100,000 points.", short="Blue Rewards (Mastercard)",
              s=["card"], lc="borrow", st="new", ay="Jun 2026", o="B", neo=[2, "Mastercard."],
              mc="The new flagship credit line, all on Mastercard.", src=[["BMO: Blue Rewards launch, Jun 2026", BLUE]]),
            P("viporter", "BMO VIPorter Mastercard", "Co-branded with Porter Airlines and Mastercard, launched 24 March 2025. The World Elite card earns 3 points per dollar at Porter and gives a companion pass at C$50,000 a year.", short="VIPorter (Mastercard)",
              s=["card"], lc="borrow", st="new", ay="Mar 2025", o="P", at="Porter Airlines", neo=[2, "Mastercard."], src=[["BMO: VIPorter launch, Mar 2025", PORTER]]),
            P("legacy", "Ascend & AIR MILES Mastercard cards", "The Ascend World Elite Mastercard (travel, lounge passes) and the AIR MILES Mastercard family, which moved to Blue Rewards in summer 2026. Existing cardholders keep their cards; the line's future is not stated ⚠. Mass-market cards such as CashBack were not checked ⚠.", short="Ascend & AIR MILES (Mastercard)",
              s=["card"], lc="borrow", st="flux", neo=[2, "Mastercard."], src=[["BMO: Ascend refresh, May 2022", ASCEND], ["BMO: Blue Rewards announced, Jan 2026", BLUEJAN]]),
            P("eclipse", "BMO eclipse Visa cards", "eclipse Visa Infinite and the metal eclipse Visa Infinite Privilege (November 2020, with Visa Canada), and the no-fee eclipse rise Visa for younger clients (December 2023). Visa's only BMO line in Canada.", short="eclipse (Visa)",
              s=["card"], lc="borrow", ay="Nov 2020", o="P", at="Visa Canada", neo=[0, "Visa."],
              mc="The premium lifestyle line went to Visa in 2020.", src=[["BMO: eclipse with Visa, Nov 2020", ECLIPSE], ["BMO: eclipse rise Visa, Dec 2023", RISE]]),
        ]},
        {"id": "2.2", "ic": "briefcase", "name": "Business & commercial cards", "blurb": "World Elite for business.", "div": "canada", "rev": "cpc", "products": [
            P("commercial", "Business & commercial Mastercard cards", "Canada's first World Elite business cards (November 2021), the Blue Rewards business cards and Commercial Card (network not stated ⚠), and the Commercial Mastercard suite of 2017: standard, CashBack, AIR MILES, not-for-profit and US-dollar cards, with Spend Dynamics for expenses.", short="Business cards (Mastercard)",
              s=["sme"], lc="borrow", neo=[2, "Mastercard."], src=[["BMO: World Elite business cards, Nov 2021", WEBIZ], ["BMO: commercial Mastercard suite, Apr 2017", COMMSUITE], ["BMO: Blue Rewards launch, Jun 2026", BLUE]]),
            P("biometric", "Biometric corporate card", "Selfie or fingerprint checks on corporate card purchases through Mastercard Identity Check, rolled out in Canada and the US in March 2016.",
              s=["corp"], lc="move", ay="Mar 2016", o="P", at="Mastercard", neo=[3, "Mastercard Identity Check."], src=[["BMO: biometric corporate card, Mar 2016", BIOMETRIC]]),
        ]},
        {"id": "2.3", "ic": "receipt-text", "name": "Corporate & virtual cards", "blurb": "Commercial Express, Oct 2026.", "div": "canada", "rev": "cpc", "products": [
            P("commexpress", "Corporate Card & embedded virtual cards", "BMO Corporate Card payments inside ERP, procurement, accounts-payable and travel software through Mastercard Commercial Express, in Canada and the US (1 October 2026). BMO says it is the first Canadian Mastercard issuer to offer it.", short="Commercial Express (Mastercard)",
              s=["corp"], lc="move", st="new", ay="Oct 2026", o="P", at="Mastercard", neo=[3, "Mastercard Commercial Express."],
              mc="The newest joint launch, with Mastercard Canada's Diane Miquelon.", src=[["BMO and Mastercard: embedded payments, Oct 2026", COMMEXP]]),
            P("extend", "Extend for BMO", "Virtual cards issued from an app (December 2022) and pushed to mobile wallets using Mastercard's tokenisation (August 2023). BMO calls itself the first global Mastercard issuer to do this.",
              s=["corp", "sme"], lc="move", ay="Aug 2023", o="P", at="Extend", neo=[2, "Mastercard virtual cards and tokens."], src=[["BMO: virtual cards with Mastercard and Extend, Aug 2023", EXTEND]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Debit in Canada", "blurb": "Interac first.", "div": "canada", "rev": "cpc", "products": [
            P("interacdebit", "Interac Debit", "BMO's Canadian debit card runs on Interac, including fee-free transit taps for all debit cardholders from February 2023. Interac handles about 18.6 million transactions a day across 300+ institutions.",
              s=["con"], lc="everyday", o="P", at="Interac", neo=[0, "Interac."], src=[["BMO: fee-free transit, Feb 2023", TRANSIT], ["Interac: about us", INTERAC]]),
            P("debitmc", "BMO Debit Mastercard", "A Debit Mastercard appears only in newsroom navigation ⚠. Co-badging with Interac is assumed, not verified.", short="Debit Mastercard ⚠",
              s=["con"], lc="everyday", st="unconf", neo=[1, "Debit Mastercard beside Interac ⚠."],
              mc="Online and cross-border debit is where Mastercard can add to Interac.", src=[["BMO: fee-free transit, Feb 2023", TRANSIT]]),
        ]},
        {"id": "2.5", "ic": "credit-card", "name": "U.S. cards", "blurb": "Mastercard credit and debit.", "div": "us", "rev": "usb", "products": [
            P("uscashback", "BMO Cash Back Mastercard (US)", "5%, 3% and 1% cash back, refreshed in March 2022. The rest of the US credit portfolio was not checked ⚠.", short="Cash Back (Mastercard)",
              s=["us"], lc="borrow", neo=[2, "Mastercard."], src=[["BMO Harris: Cash Back Mastercard, Mar 2022", USCASH]]),
            P("usdebit", "BMO US debit card", "On Mastercard: BMO Harris was the first issuer of Mastercard True Name, on debit, in 2019. The networks on legacy Bank of the West cards were not verified ⚠.", short="US debit (Mastercard)",
              s=["us"], lc="everyday", neo=[2, "Mastercard since 2019 ⚠ legacy Bank of the West cards unverified."], src=[["Mastercard and BMO Harris: True Name, Nov 2019", TRUEUS], ["BMO Harris: True Name on debit, Dec 2019", USDEBIT]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Real-time, A2A & APIs", "blurb": "e-Transfer, RTP, APIs.", "div": "group", "rev": "cpc", "products": [
            P("etransfer", "Interac e-Transfer", "Free and unlimited on all everyday bank plans since March 2017; bulk receivables for commercial clients since September 2020.",
              s=["con", "sme"], lc="move", o="P", at="Interac", neo=[0, "Interac."], src=[["BMO: free e-Transfer, Mar 2017", ETRANSFER], ["BMO: e-Transfer bulk receivables, Sep 2020", BULK]]),
            P("usrt", "RTP & Zelle (US)", "Receiving on The Clearing House's RTP network from 2020 and sending from 2021; Zelle for US commercial clients from January 2020. FedNow participation not found ⚠.",
              s=["us", "corp"], lc="move", o="P", at="The Clearing House, Zelle", neo=[0, "The Clearing House and Zelle."], src=[["BMO: The Clearing House and Global Pay, Oct 2020", GLOBALPAY], ["BMO Harris: Zelle, Jan 2020", ZELLE]]),
            P("apis", "Payment APIs & BMO Sync", "Payment APIs and a developer portal (December 2025) for real-time payments inside clients' ERP systems, with a cross-border sandbox; and BMO Sync, embedded banking in ERP systems built with FISPAN.",
              s=["corp"], lc="move", st="new", ay="Dec 2025", o="B", neo=[0, ""], src=[["BMO: Payment APIs, Dec 2025", APIS], ["BMO: TPS awards, Dec 2025", TPSAWARDS]]),
        ]},
        {"id": "2.7", "ic": "earth", "name": "Cross-border", "blurb": "Global Pay on Mastercard.", "div": "group", "rev": "usb", "products": [
            P("globalpay", "BMO Global Pay", "Business payments to more than 30 countries, built on Mastercard Cross-Border Services; launched for US clients in October 2020 after Canada.", short="Global Pay (Mastercard)",
              s=["corp", "sme"], lc="move", ay="Oct 2020", o="P", at="Mastercard", neo=[3, "Mastercard Cross-Border Services."],
              mc="Mastercard already moves BMO's business payments abroad.", src=[["BMO: Global Pay for US business, Oct 2020", GLOBALPAY]]),
        ]},
        {"id": "2.8", "ic": "coins", "name": "Digital money", "blurb": "Tokenised cash and deposits.", "div": "cm", "rev": "bcm", "products": [
            P("tokcash", "Tokenised cash with CME Group", "Tokenised cash and deposits on CME Group's network, built on Google Cloud Universal Ledger, announced March 2026 for the second half of 2026, pending approval.",
              s=["corp"], lc="move", st="new", ay="Mar 2026", o="P", at="CME Group, Google Cloud", neo=[0, "Mastercard not named."], src=[["BMO: tokenised cash with CME and Google Cloud, Mar 2026", CME]]),
            P("tokdeposits", "CAD tokenised deposits & Project Agorá", "Exploring a Canadian-dollar deposit token with RBC, TD, Scotiabank, CIBC and National Bank (September 2026), and joining the BIS-led Project Agorá for cross-border payments (September 2026).",
              s=["corp"], lc="move", st="new", ay="Sep 2026", o="P", at="Five Canadian banks", neo=[0, "Mastercard not named."],
              mc="Bank-led tokens that could move flows off card rails.", src=[["BMO: CAD tokenised deposits, Sep 2026", CADTOK], ["BMO: Project Agorá, Sep 2026", AGORA]]),
        ]},
        {"id": "2.9", "ic": "store", "name": "Acquiring", "blurb": "Moneris, being sold.", "div": "moneris", "rev": "cpc", "products": [
            P("moneris", "Moneris", "BMO's 50/50 merchant-acquiring joint venture with RBC, agreed to be sold to Francisco Partners for about C$2.0 billion (August 2026), closing by the end of Q1 fiscal 2027. BMO keeps exclusive, long-term referral arrangements. US acquiring arrangements not found ⚠.",
              s=["sme"], lc="move", st="flux", o="P", at="RBC", neo=[1, "Accepts every network."], src=[["BMO: sale of Moneris, Aug 2026", MONERIS]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card and account: Blue Rewards, the coalition that replaced AIR MILES, Google push provisioning, Mastercard True Name and card controls, instalments, and AI for clients and staff.",
    "tiles": [
        {"id": "3.1", "ic": "gift", "name": "Blue Rewards & offers", "blurb": "400+ brands.", "div": "blue", "rev": "cpc", "products": [
            P("bluerewards", "Blue Rewards", "BMO's own coalition loyalty programme, which replaced AIR MILES on 2 June 2026 with no loss of value. More than 400 brands, including Porter, Accor, Instacart, Dollarama and BMO Insurance; travel booked through Expedia Group. Chequing clients earn on debit for grocery, gas and EV purchases.",
              s=["card", "con"], lc="grow", st="new", ay="Jun 2026", o="A", neo=[0, "BMO's own coalition."],
              mc="Card-linked offers and loyalty services could plug into it.", src=[["BMO: Blue Rewards launch, Jun 2026", BLUE], ["BMO: Blue Rewards benefits, Sep 2026", BLUESEP], ["BMO: Blue Rewards and BMO Insurance, Sep 2026", BLUEINS]]),
            P("perks", "BMO Perks & in-app offers", "Card-linked offers for BMO Mastercard holders, launched with Mastercard Canada in September 2015 ⚠ current status. In-app offers personalisation won an award in 2025.",
              s=["card"], lc="grow", st="unconf", ay="Sep 2015", o="P", at="Mastercard", neo=[2, "For BMO Mastercard holders, with Mastercard Canada ⚠."], src=[["BMO: BMO Perks, Sep 2015", PERKS], ["BMO: 11 honours, Oct 2025", AWARDS25]]),
        ]},
        {"id": "3.2", "ic": "wallet", "name": "Wallets & tokens", "blurb": "Google push provisioning.", "div": "group", "rev": "cpc", "products": [
            P("pushprov", "Google push provisioning & card benefits", "Tokenised debit and credit cards pushed into Google Wallet, Chrome autofill and Google checkout; BMO is one of five banks globally and the only Canadian one. Card benefits and card art shown at checkout in Chrome (2026). Mastercard's token service is not named ⚠.",
              s=["con", "card"], lc="everyday", st="new", o="P", at="Google", neo=[None, "Token service not named ⚠."],
              mc="The checkout surfaces where Click to Pay and Agent Pay would sit.", src=[["BMO: Celent award, Jun 2025", CELENT], ["BMO: seven awards, May 2026", AWARDS26]]),
            P("applepay", "Apple Pay & Masterpass", "Apple Pay in the US from April 2015 and Canada from May 2016; Masterpass for BMO Harris small-business clients in 2017.",
              s=["con", "sme"], lc="everyday", o="P", at="Apple", neo=[1, "Masterpass at BMO Harris, 2017."], src=[["BMO: Apple Pay in Canada, May 2016", APPLEPAY], ["BMO Harris: Masterpass, Sep 2017", MASTERPASS]]),
        ]},
        {"id": "3.3", "ic": "fingerprint", "name": "Card features & controls", "blurb": "True Name, controls, PaySmart.", "div": "group", "rev": "cpc", "products": [
            P("truename", "Mastercard True Name", "Chosen names on cards: first on US debit in 2019, and on Canadian credit cards from March 2022, the first Canadian issuer.",
              s=["con", "card"], lc="everyday", ay="Mar 2022", o="P", at="Mastercard", neo=[3, "Mastercard True Name."], src=[["BMO: True Name in Canada, Mar 2022", TRUENAME]]),
            P("controls", "Digital card controls", "The Digital Card Controls Suite in Canada and the US (US award May 2026), credit-card PIN reset in the app, and FundsNow instant cheque funds in the US.",
              s=["con", "us"], lc="everyday", o="B", neo=[0, "BMO's own."], src=[["BMO: Celent award, Jun 2025", CELENT], ["BMO: seven awards, May 2026", AWARDS26]]),
            P("instalments", "BMO PaySmart & Enhanced Transaction Details", "Issuer instalment plans on credit cards, and merchant details with the option to convert a purchase to instalments. Mastercard Installments not found.",
              s=["card"], lc="borrow", o="B", neo=[0, "BMO's own."], src=[["BMO: eclipse rise Visa, Dec 2023", RISE], ["BMO: Celent award, Jun 2025", CELENT]]),
        ]},
        {"id": "3.4", "ic": "bot", "name": "AI for clients & staff", "blurb": "Lumi and Call Assist.", "div": "group", "rev": "cpc", "products": [
            P("lumi", "Lumi Assistant & Next Best Offer", "A generative-AI assistant for clients, a next-best-offer model and a mortgage forecasting model, recognised in 2025.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["BMO: 11 honours, Oct 2025", AWARDS25]]),
            P("callassist", "Call Assist, SAFE & Credit Coach", "An agent copilot, SAFE (AI for signer records), Credit Coach and My Financial Progress, recognised in May 2026.",
              s=["con", "corp"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["BMO: seven awards, May 2026", AWARDS26]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What clients buy, by reported segment: Canadian personal and commercial banking, U.S. Banking after a branch sale, wealth and insurance, and BMO Capital Markets.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Canadian personal banking", "blurb": "Chequing, mortgages, cards.", "div": "canada", "rev": "cpc", "products": [
            P("chequing", "Personal & Business Banking", "Performance and Premium chequing, Savings Amplifier, mortgages and cards. Canadian P&C earned C$3.3 billion in fiscal 2025. Euromoney named BMO Canada's best retail bank in July 2026.",
              s=["con"], lc="everyday", neo=[0, "Interac debit."], src=[["BMO and Walmart Canada, Dec 2025", WALMART], ["Fiscal 2025 results", FY25], ["BMO: Euromoney award, Jul 2026", EUROMONEY]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Commercial banking & TPS", "blurb": "Treasury & Payment Solutions.", "div": "canada", "rev": "cpc", "products": [
            P("tps", "Commercial Banking and Treasury & Payment Solutions", "Canadian commercial banking, with Treasury & Payment Solutions under Derek Vernon serving clients across North America. Named Best Bank for Collections in North America (2025).",
              s=["sme", "corp"], lc="everyday", neo=[0, ""], src=[["BMO: TPS awards, Dec 2025", TPSAWARDS], ["BMO: Payment APIs, Dec 2025", APIS]]),
        ]},
        {"id": "4.3", "ic": "flag", "name": "U.S. Banking", "blurb": "C$2.8bn; a smaller footprint.", "div": "us", "rev": "usb", "products": [
            P("usbanking", "U.S. Banking", "Deposits, home lending, consumer credit, small-business lending, cards and cash management through BMO Bank N.A., with BMO and Allpoint ATMs. Net income C$2.8 billion in fiscal 2025; US wealth folded in from Q4 2025. Smaller after the 138-branch sale.",
              s=["us"], lc="everyday", st="flux", neo=[1, "Its cards are Mastercard."], src=[["Annual Information Form 2025", AIF], ["Fiscal 2025 results", FY25], ["BMO: branch sale closes, Sep 2026", BRANCHES]]),
        ]},
        {"id": "4.4", "ic": "trending-up", "name": "Wealth & insurance", "blurb": "InvestorLine, Burgundy.", "div": "wealth", "rev": "wm", "products": [
            P("investorline", "BMO InvestorLine & ETFs", "Commission-free stock and ETF trades on InvestorLine from 9 September 2026; BMO ETFs, and ETNs with REX Shares.",
              s=["inv"], lc="grow", st="new", ay="Sep 2026", neo=[0, ""], src=[["BMO newsroom, Sep 2026", NEWSSEP]]),
            P("privatewealth", "Nesbitt Burns & Burgundy", "Full-service brokerage through BMO Nesbitt Burns, and Burgundy Asset Management, bought in November 2025. Wealth Management earned C$1.4 billion in fiscal 2025.",
              s=["inv"], lc="grow", o="A", neo=[0, ""], src=[["Annual Information Form 2025", AIF], ["Q1 2026 results", Q1]]),
            P("insurance", "BMO Insurance", "Life cover, and health and dental with GreenShield (June 2026); an AI underwriting tool, SmartDecision (July 2026). Blue Rewards members earn points on it.",
              s=["inv", "con"], lc="beyond", st="new", o="P", at="GreenShield", neo=[0, ""], src=[["BMO Insurance: health and dental, Jun 2026", INSURE], ["BMO Insurance: SmartDecision, Jul 2026", SMARTDEC]]),
        ]},
        {"id": "4.5", "ic": "chart-candlestick", "name": "Capital markets", "blurb": "Metals and mining.", "div": "cm", "rev": "bcm", "products": [
            P("capmkts", "BMO Capital Markets", "BMO's investment bank, led by Alan Tannenbaum, with a metals-and-mining franchise extending to Australia through Euroz Hartleys (agreed June 2026, about 40 staff). Net income C$2.0 billion in fiscal 2025.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["BMO: Euroz Hartleys, Jun 2026", EUROZ], ["Fiscal 2025 results", FY25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How clients reach BMO: the mobile app and online banking for business, about 1,800 branches before the US sale, and partners such as Walmart Canada and Instacart.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Digital banking", "blurb": "First in a 2026 benchmark.", "div": "canada", "rev": "cpc", "products": [
            P("app", "BMO Mobile Banking app", "Ranked first in EMARKETER's 2026 Canada mobile-banking emerging-features benchmark. The Blue Rewards app adds in-store receipt scanning.",
              s=["con", "card"], lc="everyday", neo=[0, ""], src=[["BMO: EMARKETER ranking, May 2026", EMARKETER], ["BMO: Blue Rewards announced, Jan 2026", BLUEJAN]]),
            P("olbb", "Online Banking for Business", "BMO's online banking for business clients, recognised by Datos Insights in 2025.",
              s=["sme"], lc="everyday", neo=[0, ""], src=[["BMO: TPS awards, Dec 2025", TPSAWARDS]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "1,800 less 138.", "div": "group", "rev": "cpc", "products": [
            P("branches", "Branches & ATMs", "More than 1,800 branches at 31 October 2025, less the 138 US branches sold in September 2026; BMO and Allpoint ATMs in the US.",
              s=["con", "us"], lc="open", st="flux", neo=[0, ""], src=[["Annual Information Form 2025", AIF], ["BMO: branch sale closes, Sep 2026", BRANCHES]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "Walmart, Instacart.", "div": "canada", "rev": "cpc", "products": [
            P("walmart", "Walmart Canada", "BMO products in Walmart stores and a 12-month Delivery Pass for new chequing clients (December 2025).",
              s=["con"], lc="open", o="P", at="Walmart Canada", neo=[0, ""], src=[["BMO and Walmart Canada, Dec 2025", WALMART]]),
            P("instacart", "Instacart+ for cardholders", "Instacart+ perks for BMO credit cardholders to October 2027; the premium tier covers World and World Elite Mastercard and Visa Infinite cards alike.",
              s=["card"], lc="beyond", o="P", at="Instacart", neo=[1, "World Elite Mastercard and Visa Infinite alike."], src=[["BMO and Instacart, Oct 2025", INSTACART]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BMO", "blurb": "Most cards, Global Pay, a Visa line.", "products": [
        P("mcatbmo", "Mastercard at BMO", "Mastercard carries most of BMO's Canadian credit cards (Blue Rewards, VIPorter, Ascend), its business, commercial and corporate cards, US credit and debit, and Global Pay. Visa holds the eclipse line since 2020; Interac runs Canadian debit. No public network agreement or renewal date was found.",
          s=["card"], div="group", rev="corp", mc="The relationship this map is drawn for.",
          src=[["BMO and Mastercard: embedded payments, Oct 2026", COMMEXP], ["BMO: eclipse with Visa, Nov 2020", ECLIPSE]]),
    ]},
    {"id": "pillar-market", "name": "Canadian banking", "blurb": "RTR, open banking, tokens.", "products": [
        P("market", "The Canadian market", "Payments Canada's Real-Time Rail is due in Q4 2026 (vendor roles unverified ⚠). Consumer-driven banking is legislated, with the Bank of Canada overseeing a single API standard, but not yet live (December 2025). Six large banks are exploring a CAD deposit token.",
          s=["con"], div="group", rev="corp", src=[["Payments Canada: Real-Time Rail", RTR], ["Finance Canada: consumer-driven banking", OPENBANK], ["FCAC: open banking", FCAC]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
