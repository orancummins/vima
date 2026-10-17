"""Wells Fargo's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the company's own unless a source says otherwise: the Q3 2026 results (13 October 2026), the
Q4 2025 results (14 January 2026) and the 2025 Form 10-K (24 February 2026). ``neo`` is the Mastercard
lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q3R = "https://www.sec.gov/Archives/edgar/data/0000072971/000007297126000318/wfc3qer10-13x26ex991xrelea.htm"
Q3 = "https://www.wellsfargo.com/assets/pdf/about/investor-relations/earnings/third-quarter-2026-financial-results.pdf"
Q3S = "https://www.wellsfargo.com/assets/pdf/about/investor-relations/earnings/third-quarter-2026-earnings-supplement.pdf"
Q4 = "https://www.wellsfargo.com/assets/pdf/about/investor-relations/earnings/fourth-quarter-2025-earnings.pdf"
Q4R = "https://www.wellsfargo.com/assets/pdf/about/investor-relations/earnings/fourth-quarter-2025-financial-results.pdf"
K25 = "https://www.sec.gov/Archives/edgar/data/72971/000007297126000133/wfc-20251231_d2.htm"
Q1Q = "https://www.sec.gov/Archives/edgar/data/72971/000007297126000217/wfc-20260331.htm"
Q2Q = "https://www.sec.gov/Archives/edgar/data/72971/000007297126000302/wfc-20260630.htm"
RATINGS = "https://www.wellsfargo.com/about/investor-relations/credit-ratings/"
MCAP = "https://stockanalysis.com/stocks/wfc/market-cap/"
NR = "https://newsroom.wf.com/news-releases/news-details/"
CAP = NR + "2025/Wells-Fargo-Confirms-that-the-Federal-Reserve-Has-Removed-the-Limits-on-Growth-in-Total-Assets-Imposed-in-its-2018-Consent-Order-and-Announces-a-Special-Employee-Award/default.aspx"
FED = NR + "2026/Wells-Fargo-2018-Federal-Reserve-Consent-Order-Terminated/default.aspx"
AI = NR + "2025/Wells-Fargo-Names-Saul-Van-Beurden-to-Lead-Artificial-Intelligence-Kleber-Santos-to-Expand-Responsibilities-and-Serve-as-Co-CEO-of-Consumer-Banking-and-Lending-with-Van-Beurden/default.aspx"
CRO = NR + "2026/Wells-Fargo-Announces-Retirement-of-Chief-Risk-Officer-Derek-Flowers-Chief-Operating-Officer-Scott-Powell-to-Become-Chief-Risk-Officer/default.aspx"
BIZHEAD = NR + "2026/Wells-Fargo-Names-Dennis-Devine-to-Lead-Business-Banking/default.aspx"
OLEBE = NR + "2025/Wells-Fargo-Names-Ed-Olebe-as-Head-of-Cards-and-Merchant-Services/default.aspx"
DIGITAL = NR + "2026/Wells-Fargo-Reaches-Major-Digital-Milestones/default.aspx"
GOOGLE = NR + "2025/Wells-Fargo-announces-expansion-of-strategic-relationship-with-Google-Cloud/default.aspx"
TOKDEP = NR + "2026/Wells-Fargo-to-Launch-Tokenized-Deposits-for-Corporate-and-Commercial-Clients/default.aspx"
CONSORT = NR + "2026/Group-of-leading-international-financial-institutions-to-establish-stablecoin-enterprise/default.aspx"
TEAMMATE = NR + "2026/Wells-Fargo-introduces-AI-Teammate-bringing--AI-powered-support-to-the-advisor-experience/default.aspx"
ADVGW = NR + "2026/Wells-Fargo-launches-Advisor-Gateway-for-financial-advisors/default.aspx"
PAZE = NR + "2024/Wells-Fargo-Offers-Customers-a-Convenient-Way-to-Check-Out-Online-With-Paze/default.aspx"
ACTIVE = NR + "2021/Wells-Fargo-Announces-Active-Cash-Credit-Card-Cash-Back-Card-is-First-in-New-Multi-Card-Suite/default.aspx"
REFLECT = NR + "2021/Wells-Fargo-Introduces-ReflectSM-a-New-Credit-Card-that-Rewards-Cardholders-for-On-Time-Payments/default.aspx"
AUTOGRAPH = NR + "2022/Wells-Fargo-to-Launch-AutographSM-a-New-Visa-Rewards-Credit-Card-that-Offers-3X-Points-Across-Top-Spending-Categories/default.aspx"
JOURNEY = NR + "2024/Wells-Fargo-to-Launch-Autograph-Journey-Card-Designed-for-Frequent-Travelers/default.aspx"
BILT = NR + "2022/Wells-Fargo-Partners-with-Bilt-Rewards-and-Mastercard-to-Issue-the-First-Credit-Card-that-Earns-Points-on-Rent-payments-without-the-Transaction-Fee/default.aspx"
CHOICE = NR + "2023/Choice-Hotels-Wells-Fargo-and-Mastercard-to-Launch-New-Cobranded-Credit-Card/default.aspx"
ONEKEY = NR + "2024/Expedia-Group-Wells-Fargo-and-Mastercard-announce-new-suite-of-One-Key-credit-cards/default.aspx"
ATTUNE = NR + "2024/Wells-Fargo-Introduces-the-New-Attune-World-Elite-Mastercard/default.aspx"
SIGNIFY = NR + "2024/Wells-Fargo-Launches-Signify-Business-Cash-Mastercard/default.aspx"
JETBLUE = NR + "2025/Wells-Fargo-Welcomes-JetBlue-as-Newest-Rewards-Points-Transfer-Partner/default.aspx"
CATHAY = NR + "2026/Wells-Fargo-Adds-Cathay-Pacific-as-New-Rewards-Points-Transfer-Partner/default.aspx"
VIRTUAL = NR + "2020/Wells-Fargo-Launches-WellsOne-Virtual-Card-Payments-Service/default.aspx"
VANTAGE = NR + "2022/Wells-Fargos-Vantage-Platform-Enhances-Commercial-and-Corporate-Clients-Digital-Experience-Grows-with-Businesses-at-Scale/default.aspx"
FARGO = NR + "2022/Wells-Fargos-New-Virtual-Assistant-Fargo-to-Be-Powered-by-Google-Cloud-AI/default.aspx"
APIS = NR + "2024/Wells-Fargo-Expands-API-Capabilities-for-its-Commercial-Banking-Business/default.aspx"
RAIL = NR + "2025/Wells-Fargo-Enters-into-Agreement-to-Sell-Rail-Equipment-Assets/default.aspx"
VW = NR + "2025/Volkswagen-Financial-Services-U-S--and-Wells-Fargo-launch-agreement-for-purchase-financing-of-Volkswagen-and-Audi-vehicles-in-the-United-States/default.aspx"
BILTNEW = "https://newsroom.biltrewards.com/getreadynewbiltcard"
BILTEXIT = "https://frequentmiler.com/bilt-to-ditch-wells-fargo-for-cardless-while-adding-two-premium-cards"
FISERV = "https://www.paymentsdive.com/news/fiserv-wells-fargo-to-end-joint-venture/728312/"
CARDS = "https://creditcards.wellsfargo.com/"
AGREEMENT = "https://www.wellsfargo.com/assets/pdf/small-business/agreement.pdf"
GPL = "https://www.wellsfargo.com/com/solutions/global-payments-liquidity/"
MERCHANT = "https://www.wellsfargo.com/biz/merchant/"
ZELLEUSD = "https://www.pymnts.com/news/cross-border-payments/2026/zelle-readies-stablecoin-for-first-cross-border-push/"
FINICITY = "https://www.mastercard.com/us/en/news-and-trends/Insights/2017/Finicity-and-wells-fargo-ink-data-exchange-deal.html"
DEBIT = "https://www.wellsfargo.com/debit-card/"
HISTORY = "https://history.wf.com/"
STAR = "https://finance.yahoo.com/markets/stocks/articles/fiserv-debit-network-talks-raise-142500340.html"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · regulation · technology", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $2.25 trillion of assets and ROTCE of 16.3%, a bank freed from its asset cap in 2025 and its last Fed consent order in 2026, an AI programme run from the top, and a new 17–18% returns target.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "$2.25 trillion, ROTCE 16.3%.", "div": "wfc", "rev": "corp", "products": [
            P("balance", "Balance sheet & earnings", "Assets of $2,253 billion, loans of $1,048 billion and deposits of $1,503 billion at 30 September 2026; Q3 2026 revenue of $21.9 billion and net income of $5.95 billion (ROTCE 16.3%, CET1 10.0%); $21.3 billion of net income in 2025; market value about $252 billion on 16 October 2026; rated A1/A-/A+ at holding-company level ⚠ no date on the ratings page.",
              s=["corp"], neo=[0, ""], src=[["Q3 2026 results", Q3R], ["Q3 2026 supplement", Q3S], ["Q4 2025 results", Q4], ["Market cap, Oct 2026", MCAP], ["Wells Fargo: credit ratings", RATINGS]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Scharf, chair and CEO.", "div": "wfc", "rev": "corp", "products": [
            P("leadership", "Operating committee", "Charles Scharf, chairman since October 2025 and CEO since 2019; CFO Mike Santomassimo; COO Scott Powell, who becomes CRO in January 2027; Kleber Santos and Saul Van Beurden co-run Consumer Banking & Lending; Ed Olebe, formerly of Mastercard, has run cards and merchant services since January 2025. About 194,000 staff, down 8% in a year.",
              s=["corp"], neo=[0, ""], mc="The head of cards is a former Mastercard executive.",
              src=[["2025 Form 10-K", K25], ["Olebe named, Jan 2025", OLEBE], ["Powell to become CRO, Sep 2026", CRO], ["Q3 2026 results", Q3]]),
        ]},
        {"id": "1.3", "ic": "flag", "name": "Heritage & regulation", "blurb": "Asset cap lifted in 2025.", "div": "wf", "rev": "corp", "products": [
            P("heritage", "Heritage", "Founded by Henry Wells and William G. Fargo (1852 ⚠); today's company is the former Norwest, which took the name in 1998, and it absorbed Wachovia (2008 ⚠).",
              s=["con"], o="I", neo=[0, ""], src=[["Wells Fargo history", HISTORY], ["2025 Form 10-K", K25]]),
            P("reset", "Regulatory reset", "The Fed lifted the 2018 asset cap on 3 June 2025; the 2015 OCC agreements ended in May 2025, the 13th consent order closed since 2019; the 2018 Fed consent order itself ended on 5 March 2026.",
              s=["corp"], st="new", ay="Jun 2025", neo=[0, ""], src=[["Asset cap lifted, Jun 2025", CAP], ["Fed consent order ended, Mar 2026", FED]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "AI on 180,000 desktops.", "div": "wfc", "rev": "corp", "products": [
            P("tech", "Cloud & enterprise AI", "Saul Van Beurden heads enterprise AI (November 2025); Google Cloud Agentspace for agentic AI (August 2025); more than 90,000 staff trained and AI tools on more than 180,000 desktops; applications moving to public and private cloud.",
              s=["corp"], st="new", o="P", at="Google Cloud", neo=[0, ""],
              mc="One of the most AI-forward US banks, with no agentic-payments partner announced.",
              src=[["AI leadership, Nov 2025", AI], ["Google Cloud, Aug 2025", GOOGLE], ["Q4 2025 results", Q4R]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "ROTCE 17–18% target.", "div": "wfc", "rev": "corp", "products": [
            P("strategy", "Targets & 2026 priorities", "A medium-term ROTCE target of 17–18% (January 2026), $15 billion of gross expense cuts over five years, and 2026 investment in core credit-card capabilities, Premier cards, the app, Fargo, Zelle (including a stablecoin), Paze, tokenised deposits and instant cross-border payments.",
              s=["corp"], st="new", neo=[0, ""], src=[["Q4 2025 results", Q4], ["Q4 2025 financial results", Q4R]]),
            P("deals", "Deals", "Bought out Fiserv's 40% of the merchant-services joint venture (April 2025); sold rail equipment leasing (closed Q1 2026); earlier sales of asset management and corporate trust (2021) and commercial mortgage servicing (2024).",
              s=["corp"], o="A", neo=[0, ""], src=[["10-Q Q1 2026", Q1Q], ["Rail sale, May 2025", RAIL], ["Payments Dive: Fiserv JV, Sep 2024", FISERV]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: a Visa credit suite and Visa debit, Mastercard co-brand and small-business cards, commercial and virtual cards, merchant acquiring it now owns outright, Zelle and Paze, and cross-border payments, tokenised deposits and stablecoins.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Own-brand credit", "blurb": "A Visa suite since 2021.", "div": "cards", "rev": "cbl", "products": [
            P("activecash", "Active Cash Visa", "No annual fee and unlimited 2% cash rewards; launched in June 2021 as the first card of the new Visa suite.", short="Active Cash (Visa)",
              s=["card"], lc="borrow", ay="Jun 2021", o="P", at="Visa", neo=[0, "Visa."], src=[["Active Cash launch, Jun 2021", ACTIVE], ["Wells Fargo credit cards", CARDS]]),
            P("reflect", "Reflect Visa", "No annual fee and a 0% introductory APR for 21 months; launched October 2021.", short="Reflect (Visa)",
              s=["card"], lc="borrow", ay="Oct 2021", o="P", at="Visa", neo=[0, "Visa."], src=[["Reflect launch, Oct 2021", REFLECT]]),
            P("autograph", "Autograph & Autograph Journey Visa", "Autograph (June 2022, 3X on everyday categories), which Wells Fargo said 'solidifies' its Visa partnership, and Autograph Journey ($95, March 2024, 5X hotels and 4X airlines); the legacy Visa Signature points cards remain. Q3 2026: credit card purchase volume $45.0 billion (+12%), card loans $54.5 billion and 661,000 new accounts.", short="Autograph (Visa)",
              s=["card"], lc="borrow", ay="Jun 2022", o="P", at="Visa", neo=[0, "Visa."],
              mc="The core consumer book and the 2026 card investment sit on Visa.",
              src=[["Autograph launch, Jun 2022", AUTOGRAPH], ["Autograph Journey, Mar 2024", JOURNEY], ["Q3 2026 supplement", Q3S]]),
        ]},
        {"id": "2.2", "ic": "plane", "name": "Co-brand cards", "blurb": "Choice and Expedia on Mastercard.", "div": "cards", "rev": "cbl", "products": [
            P("choice", "Choice Privileges Mastercard", "Two Choice Hotels cards ($0 and $95) issued by Wells Fargo, with Mastercard as exclusive network (February 2023).", short="Choice Privileges (Mastercard)",
              s=["card"], lc="borrow", ay="Feb 2023", o="P", at="Choice Hotels, Mastercard", neo=[2, "Mastercard, exclusive network."], src=[["Choice Hotels card, Feb 2023", CHOICE], ["Wells Fargo credit cards", CARDS]]),
            P("onekey", "One Key cards", "One Key ($0) and One Key+ ($99) with Expedia Group, a multiyear deal from July 2024 with World Elite benefits.", short="One Key (Mastercard)",
              s=["card"], lc="borrow", ay="Jul 2024", o="P", at="Expedia Group, Mastercard", neo=[2, "Mastercard World Elite."],
              src=[["One Key cards, Jul 2024", ONEKEY]]),
            P("attune", "Attune World Elite Mastercard", "Launched June 2024 with 4% on wellness and entertainment ⚠ not on the card page on 17 October 2026, so it may be closed to new applicants.", short="Attune (Mastercard)",
              s=["card"], lc="borrow", st="unconf", ay="Jun 2024", o="P", at="Mastercard", neo=[2, "Mastercard World Elite ⚠ status."], src=[["Attune launch, Jun 2024", ATTUNE]]),
            P("bilt", "Bilt Mastercard", "Issued from March 2022, the first new Wells Fargo–Mastercard card in more than five years; exit announced July 2025 and cardholders moved to Cardless and Column N.A. on 7 February 2026, still on Mastercard ⚠ press said Wells Fargo was losing money on it.", short="Bilt (left Feb 2026)",
              s=["card"], lc="borrow", st="retired", ay="Mar 2022", o="P", at="Bilt, Mastercard", neo=[2, "Mastercard; now issued by Cardless."],
              mc="Mastercard's largest Wells Fargo co-brand left the bank in February 2026.",
              src=[["Bilt card launch, Mar 2022", BILT], ["Frequent Miler: Bilt to Cardless, Jul 2025", BILTEXIT], ["Bilt: new card, Feb 2026", BILTNEW]]),
        ]},
        {"id": "2.3", "ic": "briefcase-business", "name": "Business & commercial cards", "blurb": "Signify on Mastercard.", "div": "cards", "rev": "cbl", "products": [
            P("signify", "Signify Business Cash World Elite Mastercard", "2% unlimited cash rewards and no annual fee; launched May 2024 as the 'first step' in rebuilding the business card line.", short="Signify Business (Mastercard)",
              s=["sme"], lc="borrow", ay="May 2024", o="P", at="Mastercard", neo=[2, "Mastercard World Elite."],
              mc="The base for a rebuilt small-business card range under a new Business Banking head.",
              src=[["Signify launch, May 2024", SIGNIFY]]),
            P("commcard", "WellsOne Commercial Card & Virtual Card", "Corporate cards and single-use virtual card numbers for supplier payments (November 2020) ⚠ network not confirmed.", short="WellsOne (network unknown)",
              s=["corp"], lc="move", ay="Nov 2020", neo=[None, "Network not confirmed."], src=[["WellsOne Virtual Card, Nov 2020", VIRTUAL]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Debit", "blurb": "$145bn a quarter, Visa ⚠.", "div": "wf", "rev": "cbl", "products": [
            P("debit", "Debit & ATM cards", "Q3 2026 debit purchase volume of $144.9 billion on 2.8 billion transactions, $424 billion in the first nine months (+8%); in Apple Pay, Google Pay, Samsung Pay, Garmin Pay, PayPal and Paze, with card on/off controls ⚠ Visa, inferred from 'Visa-branded' in the account agreement.", short="Debit (Visa ⚠)",
              s=["con", "sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa ⚠ inferred."], src=[["Q3 2026 supplement", Q3S], ["Account agreement, Jul 2026", AGREEMENT], ["Wells Fargo: debit card", DEBIT]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Merchant services", "blurb": "Wholly owned since 2025.", "div": "wfms", "rev": "cbl", "products": [
            P("merchant", "Wells Fargo Merchant Services", "Wholly owned since Wells Fargo bought Fiserv's 40% in April 2025 (an $877 million intangible), with Fiserv staying on as processor; point of sale on Clover and Clover Gateway for invoices and payment links; merchant revenue now booked in card fees.",
              s=["sme"], lc="move", st="new", ay="Apr 2025", o="A", at="Fiserv, Clover", neo=[1, "Accepts every network."],
              mc="A newly owned acquirer with no Mastercard risk or data services announced.",
              src=[["10-Q Q1 2026", Q1Q], ["Payments Dive: Fiserv JV, Sep 2024", FISERV], ["Wells Fargo: merchant services", MERCHANT]]),
            P("sponsor", "Network sponsorship", "Wells Fargo sponsors a payment company on the card networks; maximum chargeback exposure was $322 billion at 30 June 2026 (four months' volume) ⚠ the company is not named.",
              s=["corp"], lc="move", neo=[1, "Card-network sponsor ⚠ unnamed."], src=[["10-Q Q2 2026", Q2Q]]),
        ]},
        {"id": "2.6", "ic": "zap", "name": "Zelle, Paze & instant", "blurb": "Bank-owned rails.", "div": "wf", "rev": "cbl", "products": [
            P("zelle", "Zelle", "Wells Fargo is one of seven owner banks of Early Warning Services; Zelle carried more than $1.2 trillion in 2025.",
              s=["con", "sme"], lc="move", o="P", at="Early Warning Services", neo=[0, "Bank-owned rail."], src=[["PYMNTS: ZelleUSD, Jun 2026", ZELLEUSD]]),
            P("paze", "Paze", "Early Warning's bank wallet, switched on for all eligible Wells Fargo debit and credit cards on 29 October 2024.",
              s=["con", "card"], lc="move", ay="Oct 2024", o="P", at="Early Warning Services", neo=[0, "Bank-owned wallet; competes with Click to Pay."],
              mc="Wells Fargo cards are tokenised for online checkout through Paze, not Click to Pay.",
              src=[["Paze launch, Oct 2024", PAZE]]),
            P("instant", "RTP & FedNow", "Instant payments 24/7 on both US real-time rails, with API routing.",
              s=["corp"], lc="move", neo=[0, ""], src=[["Wells Fargo: global payments & liquidity", GPL]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Cross-border & digital money", "blurb": "Tokenised deposits, stablecoins.", "div": "wfc", "rev": "cib", "products": [
            P("crossborder", "Cross-border payments & FX", "Cross-border payments, global invoice payments and FX; Wells Fargo cites '1 in 7 cross-border transactions globally' (Swift data, June 2024).",
              s=["corp"], lc="move", neo=[0, ""], src=[["Wells Fargo: global payments & liquidity", GPL]]),
            P("tokdep", "Tokenized deposits", "Launched 4 August 2026 on Wells Fargo's own blockchain; USD to GBP for selected clients from autumn 2026, more through 2027.",
              s=["corp"], lc="move", st="new", ay="Aug 2026", neo=[0, "Own blockchain."], src=[["Tokenized deposits, Aug 2026", TOKDEP]]),
            P("stablecoin", "Stablecoins", "One of 21 institutions in a bank stablecoin venture (1 September 2026), USD first, targeted for H1 2027; and ZelleUSD, Early Warning's stablecoin, announced June 2026 for US-to-India payments before the end of 2026.",
              s=["corp", "con"], lc="move", st="new", ay="Sep 2026", o="P", neo=[0, ""],
              mc="Bank tokens and stablecoins are routes around card rails for cross-border and B2B.",
              src=[["Stablecoin venture, Sep 2026", CONSORT], ["PYMNTS: ZelleUSD, Jun 2026", ZELLEUSD]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: treasury fraud controls, Fargo and the AI tools behind it, the Gateway API portal and an old data link with Finicity, and points that transfer to airlines and hotels.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & validation", "blurb": "Positive Pay, account checks.", "div": "wf", "rev": "cb", "products": [
            P("fraud", "Treasury fraud controls", "Positive Pay with payee validation, ACH Fraud Filter, account validation services, Fraud Manager and Payment Authorization for business clients.",
              s=["corp", "sme"], lc="move", neo=[0, "Wells Fargo's own."], src=[["Wells Fargo: global payments & liquidity", GPL]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI for customers", "blurb": "Fargo: 1bn+ interactions.", "div": "wf", "rev": "cbl", "products": [
            P("fargo", "Fargo virtual assistant", "More than a billion interactions (March 2026) and 3 million Spanish-speaking users; powered by Google Cloud AI.",
              s=["con"], lc="everyday", o="P", at="Google Cloud", neo=[0, ""],
              mc="A natural home for Agent Pay, unclaimed by either network.",
              src=[["Digital milestones, Mar 2026", DIGITAL], ["Fargo on Google Cloud, Oct 2022", FARGO]]),
            P("aiteammate", "AI Teammate", "AI support for financial advisers, launched July 2026.",
              s=["wealth"], lc="grow", st="new", ay="Jul 2026", neo=[0, ""], src=[["AI Teammate, Jul 2026", TEAMMATE]]),
        ]},
        {"id": "3.3", "ic": "code-xml", "name": "APIs & data", "blurb": "Gateway, Finicity ⚠.", "div": "wf", "rev": "cb", "products": [
            P("gateway", "Gateway API portal", "Payment, data and reporting APIs for business clients, with floorplan and channel-finance APIs added in September 2024.",
              s=["corp"], lc="move", neo=[0, ""], src=[["Wells Fargo: global payments & liquidity", GPL], ["Commercial APIs, Sep 2024", APIS]]),
            P("finicity", "Data exchange with Finicity", "Data-sharing APIs with aggregators, the first with Finicity, now Mastercard's, in April 2017 ⚠ date from a search snippet; current status unknown.",
              s=["con"], lc="open", ay="Apr 2017", o="P", at="Finicity (Mastercard)", neo=[3, "Finicity, Mastercard's ⚠ 2017."], src=[["Mastercard: Finicity and Wells Fargo, 2017", FINICITY]]),
            P("receivables", "Integrated receivables", "Integrated receivables and Perfect Receivables matching for treasury clients.",
              s=["corp"], lc="move", neo=[0, ""], src=[["Wells Fargo: global payments & liquidity", GPL]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards", "blurb": "Points to airlines and hotels.", "div": "cards", "rev": "cbl", "products": [
            P("rewards", "Rewards & points transfer", "Points transfer from April 2024 to Choice, Flying Blue, Avios, JetBlue (November 2025), Wyndham and Cathay (April 2026), and Autograph Card Exclusives for concert access.",
              s=["card"], lc="grow", neo=[0, "Wells Fargo's own."],
              mc="Premier and travel card plans need benefits and offers.",
              src=[["Autograph Journey, Mar 2024", JOURNEY], ["JetBlue partner, Nov 2025", JETBLUE], ["Cathay partner, Apr 2026", CATHAY]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: consumer and small-business banking with $825 billion of deposits, home, auto and personal loans, Commercial Banking, Corporate & Investment Banking, and Wealth & Investment Management with $2.45 trillion of client assets.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Consumer & small business", "blurb": "$825bn of deposits.", "div": "wf", "rev": "cbl", "products": [
            P("cbb", "Consumer, Small & Business Banking", "Q3 2026 revenue of $7.58 billion within Consumer Banking & Lending ($10.66 billion, +5%), and average deposits of $825 billion.",
              s=["con"], lc="everyday", neo=[0, "Visa debit ⚠."], src=[["Q3 2026 results", Q3]]),
            P("premier", "Wells Fargo Premier", "The affluent offer; deposits and investments up 14% in 2025, with more Premier card products planned for 2026 ⚠ network not announced.",
              s=["wealth", "card"], lc="grow", st="new", neo=[None, "Premier card network not announced."],
              mc="Open ground: new Premier cards have no network named.",
              src=[["Q4 2025 results", Q4], ["Q4 2025 financial results", Q4R]]),
            P("business", "Business Banking", "Owners with sales up to $25 million; Dennis Devine took over in February 2026.",
              s=["sme"], lc="everyday", st="new", neo=[1, "Mastercard business card; Visa debit ⚠."], src=[["Devine to lead Business Banking, Feb 2026", BIZHEAD]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Home, auto & personal", "blurb": "Auto revenue +33%.", "div": "wf", "rev": "cbl", "products": [
            P("homelending", "Home Lending", "Q3 2026 revenue of $0.74 billion.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["Q3 2026 results", Q3]]),
            P("auto", "Auto lending", "Q3 2026 originations of $10.1 billion and revenue of $0.34 billion (+33%); preferred purchase-finance provider for Volkswagen and Audi (May 2025) and Ducati (April 2026).",
              s=["home"], lc="borrow", o="P", at="Volkswagen Financial Services", neo=[0, ""], src=[["Q3 2026 supplement", Q3S], ["Volkswagen deal, May 2025", VW]]),
            P("personal", "Personal Lending", "Q3 2026 revenue of $0.28 billion.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Q3 2026 results", Q3]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Commercial Banking", "blurb": "$240bn of loans.", "div": "wf", "rev": "cb", "products": [
            P("commercial", "Commercial Banking", "Q3 2026 revenue of $3.24 billion (+6%) and net income of $1.20 billion; average loans $240 billion, deposits $199 billion; Kyle Hranicky is CEO.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Q3 2026 results", Q3], ["2025 Form 10-K", K25]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Corporate & Investment Banking", "blurb": "$5bn a quarter.", "div": "wfc", "rev": "cib", "products": [
            P("cib", "Corporate & Investment Banking", "Q3 2026 revenue of $5.01 billion: banking $1.99 billion (treasury management and payments $683 million), commercial real estate $1.17 billion and markets $1.84 billion; sixth in US M&A this year.",
              s=["corp"], lc="move", neo=[0, ""], src=[["Q3 2026 results", Q3]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "Wealth & investment", "blurb": "$2.45 trillion of client assets.", "div": "advisors", "rev": "wim", "products": [
            P("wim", "Wells Fargo Advisors, FiNet & First Clearing", "Wealth & Investment Management: Q3 2026 revenue of $4.10 billion (+12%) and client assets of $2.45 trillion.",
              s=["wealth"], lc="grow", neo=[0, ""], src=[["Q3 2026 results", Q3]]),
            P("privatebank", "Wells Fargo Private Bank", "The private bank for the wealthiest clients, inside WIM.",
              s=["wealth"], lc="grow", neo=[0, ""], src=[["Q3 2026 results", Q3]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Wells Fargo: the app for 34 million, 4,068 branches, Vantage for companies, Advisor Gateway for advisers, and partners from Choice and Expedia to Volkswagen dealers and Clover.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Mobile app", "blurb": "34 million active.", "div": "wf", "rev": "cbl", "products": [
            P("app", "Wells Fargo Mobile app", "34.0 million mobile-active and 38.2 million digital-active customers (Q3 2026); rated 4.9 from more than 10 million reviews.",
              s=["con", "card", "sme"], lc="everyday", neo=[0, ""], src=[["Q3 2026 supplement", Q3S], ["Digital milestones, Mar 2026", DIGITAL]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "4,068 branches.", "div": "wf", "rev": "cbl", "products": [
            P("branches", "Branches", "4,068 branches at 30 September 2026.",
              s=["con", "home"], lc="open", neo=[0, ""], src=[["Q3 2026 supplement", Q3S]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "Portals & partners", "blurb": "Vantage, Advisor Gateway.", "div": "wfc", "rev": "cb", "products": [
            P("vantage", "Vantage", "The portal for commercial and corporate clients, which replaced CEO in December 2022.",
              s=["corp"], lc="move", ay="Dec 2022", neo=[0, ""], src=[["Vantage, Dec 2022", VANTAGE]]),
            P("advisorgw", "Advisor Gateway", "More than 200 tools for advisers, built on $1 billion of WIM technology investment (May 2026).",
              s=["wealth"], lc="grow", st="new", ay="May 2026", neo=[0, ""], src=[["Advisor Gateway, May 2026", ADVGW]]),
            P("partners", "Partner channels", "Co-brand partners Choice Hotels and Expedia, Volkswagen and Audi dealers, and Clover for merchants.",
              s=["card", "home", "sme"], lc="open", o="P", neo=[1, "Co-brands on Mastercard."], src=[["Choice Hotels card, Feb 2023", CHOICE], ["One Key cards, Jul 2024", ONEKEY], ["Volkswagen deal, May 2025", VW], ["Wells Fargo: merchant services", MERCHANT]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Wells Fargo", "blurb": "Partner and business cards.", "products": [
        P("mcatwf", "Mastercard at Wells Fargo", "Visa carries Wells Fargo's own consumer credit suite, launched from 2021, and, by inference, its debit ⚠. Mastercard holds the partner co-brands (Choice Hotels, exclusive, and Expedia's One Key), the Signify small-business card and Attune ⚠; it lost Bilt from Wells Fargo's books in February 2026, though Bilt stays on Mastercard. Its Finicity unit signed a data-exchange deal in 2017 ⚠. Wallet checkout runs through Paze, which Wells Fargo co-owns.",
          s=["card"], div="wfc", rev="corp", mc="The relationship this map is drawn for.",
          src=[["Autograph launch, Jun 2022", AUTOGRAPH], ["Choice Hotels card, Feb 2023", CHOICE], ["Signify launch, May 2024", SIGNIFY], ["Bilt: new card, Feb 2026", BILTNEW]]),
    ]},
    {"id": "pillar-market", "name": "US banking", "blurb": "Asset cap gone, stablecoins coming.", "products": [
        P("market", "The US market", "Wells Fargo is free to grow its balance sheet after June 2025; Visa and Mastercard settled the interchange equitable-relief class in November 2025, subject to court approval; bank stablecoins are being built under the GENIUS Act; and big banks were reported in July 2026 to have explored buying Fiserv's STAR and Accel debit networks ⚠ preliminary.",
          s=["corp"], div="wfc", rev="corp", src=[["10-Q Q1 2026", Q1Q], ["Stablecoin venture, Sep 2026", CONSORT], ["Asset cap lifted, Jun 2025", CAP], ["MarketBeat: debit network talks, Jul 2026 ⚠", STAR]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
