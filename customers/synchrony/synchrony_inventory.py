"""Synchrony Financial's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the company's own unless a source says otherwise: the 2Q26 results (21 July 2026), the 2Q26
10-Q and the FY2025 10-K (6 February 2026). ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

SEC = "https://www.sec.gov/Archives/edgar/data/1601712/"
K25 = SEC + "000160171226000006/syf-20251231.htm"
Q2 = SEC + "000160171226000030/earningsrelease2q26.htm"
Q2P = SEC + "000160171226000030/a2q26earningspresentatio.htm"
Q2Q = SEC + "000160171226000033/syf-20260630.htm"
Q1 = SEC + "000160171226000013/earningsrelease1q26.htm"
NEWS = "https://www.synchrony.com/contenthub/newsroom/"
ONEPAY = NEWS + "onepay-and-synchrony-to-launch-new-industry-leading-credit-card.html"
LOWES = NEWS + "synchrony-expands-partnership-with-lowes.html"
LEAD = NEWS + "synchrony-announces-executive-leadership-changes.html"
AIC = NEWS + "2026-ai-in-commerce-study.html"
WALG = NEWS + "walgreens-expands-partnership-with-synchrony-and-mastercard.html"
JCREW = NEWS + "jcrew-group-partners-with-synchrony-and-mastercard-for-new-cr.html"
VIRGIN = NEWS + "virgin-red-announces-new-multi-year-partnership.html"
SAMS = NEWS + "synchrony-renews-30-year-relationship-dedicated-to-enhancing.html"
VERS = NEWS + "versatile-synchrony.html"
AGENT = "https://www.synchrony.com/contenthub/insights/blog-post-by-mike-storiale.html"
INNOV = "https://innovationleader.com/financial-services/how-synchrony-financial-is-preparing-for-the-arrival-of-agentic-commerce/"
PPCARD = "https://www.paypal.com/us/digital-wallet/manage-money/paypal-cashback-mastercard"
CCMC = "https://carecredit.com/Mastercard"
CCWMT = "https://www.grocerydive.com/press-release/20260413-synchronys-carecredit-credit-card-now-accepted-on-walmartcom/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · charter · partners", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $102 billion of loan receivables funded 83% by deposits, a savings-and-loan charter, a GE heritage, partner agreements that run to 2035, and a technology and AI organisation preparing for shopping agents.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & capital", "blurb": "$102 billion of receivables.", "div": "grp", "rev": "grp", "products": [
            P("balance", "Balance sheet", "Loan receivables of $102.2 billion and deposits of $82.8 billion (83% of funding) at 30 June 2026; 68.4 million active accounts; net interest margin 15.08%.",
              s=["corp"], neo=[0, ""], src=[["2Q26 results", Q2]]),
            P("earnings", "Earnings & capital", "Net earnings of $3.55 billion in 2025 and $885 million in 2Q26 (ROTCE 25.2%); CET1 13.2%; a $6.5 billion buyback approved in April 2026 and the dividend raised to $0.34; rated BBB- (S&P, positive) and BBB (Fitch). 2026 EPS guidance $9.25–9.50.",
              s=["corp"], neo=[0, ""], src=[["2Q26 results", Q2], ["1Q26 results", Q1]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Charter & leadership", "blurb": "A federal savings bank.", "div": "bank", "rev": "grp", "products": [
            P("charter", "Synchrony Bank & regulation", "A savings-and-loan holding company supervised by the Federal Reserve; Synchrony Bank is a federal savings association regulated by the OCC, with the CFPB and FDIC. The CFPB's $8 late-fee rule was vacated in April 2025.",
              s=["corp"], neo=[0, ""], src=[["FY2025 10-K", K25]]),
            P("leadership", "Leadership", "CEO Brian Doubles; CFO Brian Wenzel; Carol Juel runs Digital (June 2026), Florin Arghirescu is CTO with the AI agenda, Nimrod Barak is Chief AI Officer; platform CEOs Curtis Howse (Home & Auto), Courtney Gentleman (Diversified & Value) and Beto Casellas (Health & Wellness).",
              s=["corp"], neo=[0, ""], src=[["Synchrony: leadership changes, Jun 2026", LEAD]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage", "blurb": "GE Capital Retail Finance.", "div": "grp", "rev": "grp", "products": [
            P("heritage", "From GE Capital to Synchrony", "GE Capital's retail-finance arm, with roots to 1932; listed in 2014 and fully separated from GE in 2015 ⚠. CareCredit dates from 1987. Walmart's card went to Capital One in 2019 and came back, through OnePay, in 2025.",
              s=["corp"], o="I", neo=[0, ""], src=[["FY2025 10-K", K25], ["CareCredit: about", "https://www.carecredit.com/about/"]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Getting ready for shopping agents.", "div": "grp", "rev": "grp", "products": [
            P("tech", "Technology, AI & tokenisation", "A technology organisation under the CTO with an explicit AI agenda, its own tokenisation platform for single-use virtual cards, and a 2026 study with Oxford Economics on shopping with AI agents (82% put data security first).",
              s=["corp", "partner"], neo=[0, ""], src=[["FY2025 10-K", K25], ["Synchrony: AI in Commerce study, Sep 2026", AIC]]),
        ]},
        {"id": "1.5", "ic": "users-round", "name": "Partner concentration", "blurb": "Top five: 54% of interest and fees.", "div": "grp", "rev": "grp", "products": [
            P("partners", "Partner agreements", "Amazon, Lowe's, PayPal, Sam's Club and TJX made 54% of 2025 interest and fees and 52% of receivables; Lowe's, PayPal and Sam's each exceed 10%. Their agreements run out between 2030 and 2035; 30-plus partners were added or renewed in the first half of 2026.",
              s=["partner"], neo=[0, ""], src=[["FY2025 10-K", K25], ["2Q26 10-Q", Q2Q]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Five ways credit moves: private-label cards that work at one partner, Dual and co-brand cards that work everywhere (most on Mastercard), Pay Later and instalment loans, the CareCredit and Car Care acceptance networks, and tokens for wallets.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Private-label cards", "blurb": "About two-thirds of receivables.", "div": "syf", "rev": "dv", "products": [
            P("privatelabel", "Private-label credit cards", "Cards that work only at the partner: Amazon, Lowe's, JCPenney, Belk, TJX and hundreds more. With instalment loans they are about two-thirds of receivables, off the card networks entirely.", short="Private label",
              s=["con", "partner"], lc="borrow", neo=[0, "Closed loop, no network."],
              mc="The largest pool Mastercard does not touch, and Synchrony's moat; tokens and Click to Pay could reach it without converting it.",
              src=[["FY2025 10-K", K25], ["2Q26 10-Q", Q2Q]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Dual & co-brand cards", "blurb": "$35.7 billion, up 25%.", "div": "syf", "rev": "digital", "products": [
            P("mcdual", "Mastercard Dual & co-brand cards", "Most of the named general-purpose programmes run on Mastercard: PayPal Cashback, Sam's Club, OnePay CashRewards for Walmart, myWalgreens, J.Crew, Virgin Red World Elite, Belk, CareCredit Rewards and Synchrony Premier. Co-brand receivables were $35.7 billion in 2Q26, up 25%.", short="Mastercard co-brands",
              s=["con", "partner"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard for most named programmes."],
              mc="The core of the relationship, signed programme by programme; no enterprise-wide network agreement is public.",
              src=[["PayPal Cashback Mastercard", PPCARD], ["OnePay and Synchrony, Jun 2025", ONEPAY], ["2Q26 presentation", Q2P]]),
            P("onepay", "OnePay CashRewards Mastercard (Walmart)", "The Walmart card returned to Synchrony through Walmart's OnePay app: a Mastercard and a Walmart-only card, live September 2025 and, by management's account, the fastest-growing new programme in its history ⚠.", short="OnePay (Walmart)",
              s=["con"], lc="everyday", st="new", ay="Sep 2025", o="P", at="OnePay, Walmart, Mastercard", neo=[2, "Mastercard."],
              src=[["OnePay and Synchrony, Jun 2025", ONEPAY], ["FY2025 10-K", K25]]),
            P("visaamex", "Venmo & Verizon (Visa), Lowe's Pro (Amex)", "The Venmo Credit Card and Verizon Visa Card run on Visa; the MyLowe's Pro Rewards card, bought with Lowe's $0.7 billion commercial portfolio in April 2026, runs on American Express.", short="Visa & Amex programmes",
              s=["con", "sme"], lc="everyday", o="P", at="Visa, American Express", neo=[0, "Visa and Amex."],
              mc="Visa holds two large digital programmes and Amex has just entered through Lowe's Pro.",
              src=[["Synchrony expands Lowe's partnership, Apr 2026", LOWES], ["CFPB: Venmo Visa", "https://www.consumerfinance.gov/consumer-tools/credit-cards/explore-cards/cards/synchrony-financial-venmo-visa-card"]]),
        ]},
        {"id": "2.3", "ic": "receipt-text", "name": "Pay Later & instalments", "blurb": "Pay in 4 at Amazon.", "div": "syf", "rev": "home", "products": [
            P("paylater", "Synchrony Pay Later", "Pay monthly, or Pay in 4 with no interest, at Amazon (2025), JCPenney and others ⚠ 6,200+ merchants; single-use virtual cards make it work in store.",
              s=["con"], lc="borrow", st="new", neo=[0, "Synchrony's own tokens."],
              mc="Competes with Affirm and Klarna inside partner checkouts; Mastercard Installments could carry it further.",
              src=[["FY2025 10-K", K25], ["2Q25 results", SEC + "000160171225000228/earningsrelease2q25.htm"]]),
            P("instalment", "Instalment loans & promotional financing", "Secured loans for power sports (Suzuki, Polaris), equal-payment loans at Harbor Freight, and deferred-interest promotions at Bob's Discount Furniture, Ashley and PayPal Credit.",
              s=["con", "home"], lc="borrow", neo=[0, ""], src=[["FY2025 10-K", K25], ["1Q26 results", Q1]]),
        ]},
        {"id": "2.4", "ic": "network", "name": "Acceptance networks", "blurb": "CareCredit, Car Care, HOME.", "div": "carecredit", "rev": "health", "products": [
            P("ccnetwork", "CareCredit network", "More than 12 million cardholders and 290,000-plus places that take CareCredit, from dentists to vets; accepted on Walmart.com since April 2026.",
              s=["health"], lc="borrow", neo=[0, "Synchrony's own network."], src=[["CareCredit on Walmart.com, Apr 2026", CCWMT], ["FY2025 10-K", K25]]),
            P("carcare", "Car Care & Synchrony HOME", "Multi-merchant private-label networks: Car Care at more than a million auto locations, HOME across furniture and home improvement.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["FY2025 10-K", K25]]),
        ]},
        {"id": "2.5", "ic": "fingerprint", "name": "Tokens & wallets", "blurb": "Apple Pay, Google, Amazon Pay.", "div": "syf", "rev": "digital", "products": [
            P("wallets", "Wallets & virtual cards", "Cards provisioned into Apple Pay, Google Wallet and Amazon Pay, and Synchrony's own tokenisation for single-use virtual cards behind Pay Later in store.",
              s=["con"], lc="move", neo=[1, "Mastercard tokens on the Mastercard cards."],
              mc="The 10-K flags wallet compatibility for private-label cards as a risk; network tokens and Click to Pay are the answer Mastercard sells.",
              src=[["FY2025 10-K", K25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: instant credit decisions at the till, fraud models, loyalty that now costs more than interchange earns, partner economics, and early work on payments by AI agents with Mastercard, Visa and Google.",
    "tiles": [
        {"id": "3.1", "ic": "gauge", "name": "Underwriting & decisions", "blurb": "Instant credit at the till.", "div": "syf", "rev": "grp", "products": [
            P("underwriting", "Instant credit decisions", "Fully automated underwriting in store and online, using partner and alternative data; net charge-offs 5.43% in 2Q26 against a target below 5.5%.",
              s=["con", "partner"], lc="open", neo=[0, ""], src=[["2Q26 results", Q2], ["FY2025 10-K", K25]]),
            P("versatile", "Versatile Credit", "A multi-lender point-of-sale platform bought in October 2025: if Synchrony says no, the next lender in the waterfall can say yes.",
              s=["partner", "home"], lc="open", st="new", ay="Oct 2025", o="A", neo=[0, ""], src=[["Synchrony: Versatile Credit, Oct 2025", VERS]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud & identity", "blurb": "Operational losses rising.", "div": "syf", "rev": "grp", "products": [
            P("fraud", "Fraud models", "Proprietary new-account and transaction fraud models; other expense rose 7% in 2Q26, driven by higher operational losses.",
              s=["con"], lc="everyday", neo=[0, "No Mastercard fraud product announced."],
              mc="Identity checks at instant point-of-sale credit and Decision Intelligence on the Mastercard cards.",
              src=[["FY2025 10-K", K25], ["2Q26 results", Q2]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty & partner economics", "blurb": "Loyalty costs above interchange.", "div": "syf", "rev": "grp", "products": [
            P("loyalty", "Rewards & loyalty engine", "Points, discounts, cash back and statement credits run for partners; loyalty costs exceeded interchange in 2025, and higher loyalty costs held back 2Q26 other income.",
              s=["con", "partner"], lc="grow", neo=[0, ""],
              mc="Card-linked offers and merchant-funded rewards could carry some of the cost.",
              src=[["FY2025 10-K", K25], ["2Q26 results", Q2]]),
            P("rsa", "Retailer share arrangements", "About $1.0 billion a quarter shared with partners (4.1% of average receivables in 2Q26).",
              s=["partner"], lc="grow", neo=[0, ""], src=[["2Q26 results", Q2]]),
        ]},
        {"id": "3.4", "ic": "bot", "name": "Agentic commerce", "blurb": "Still in testing.", "div": "syf", "rev": "digital", "products": [
            P("agentic", "Agent payments", "Synchrony says it works with Mastercard and Visa on agent-pay frameworks and contributes to Google's AP2 (October 2025); a Synchrony Marketplace pilot ran with Mastercard, Visa and Google, but agentic payments were 'still in testing' in August 2026.",
              s=["con", "fin"], lc="move", st="new", neo=[1, "Mastercard among three partners."],
              mc="Agent Pay for the Mastercard co-brands first, then a way for agents to use private-label credit.",
              src=[["Synchrony: agentic commerce, Oct 2025", AGENT], ["Innovation Leader, Aug 2026", INNOV]]),
        ]},
        {"id": "3.5", "ic": "plug", "name": "Embedded finance", "blurb": "Clover, Vetspire, OnePay.", "div": "syf", "rev": "health", "products": [
            P("embedded", "Embedded & API finance", "Credit inside the OnePay app, the Pay with Synchrony app on Clover, and CareCredit inside practice software (Vetspire, September 2026; Dental Intelligence, 9,000 practices).",
              s=["fin", "health"], lc="open", st="new", neo=[0, ""],
              src=[["Synchrony: CareCredit and Vetspire, Sep 2026", NEWS + "carecredit-partners-with-vetspire.html"], ["FY2025 10-K", K25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Five sales platforms, opened out into the partners behind them: Digital (Amazon, PayPal, Verizon), Home & Auto (Lowe's), Diversified & Value (Walmart, Sam's, TJX), Health & Wellness (CareCredit) and Lifestyle, plus deposits.",
    "tiles": [
        {"id": "4.1", "ic": "monitor", "name": "Digital", "blurb": "Amazon, PayPal, Verizon.", "div": "syf", "rev": "digital", "products": [
            P("amazon", "Amazon", "The largest programme: the Amazon Store and Prime Store cards, renewed in 2025 with Pay Later added. (Amazon's Visa co-brand is Chase's.)",
              s=["con"], lc="borrow", o="P", at="Amazon", neo=[0, "Private label."], src=[["FY2025 10-K", K25]]),
            P("paypal", "PayPal & Venmo", "PayPal Credit, the PayPal Cashback Mastercard and the Venmo Visa: more than 10% of interest and fees.",
              s=["con"], lc="everyday", o="P", at="PayPal", neo=[1, "PayPal card Mastercard; Venmo Visa."], src=[["PayPal Cashback Mastercard", PPCARD], ["FY2025 10-K", K25]]),
            P("digitalother", "Verizon, QVC & Virgin Red", "The Verizon Visa Card, QVC and HSN cards, and the Virgin Red Rewards World Elite Mastercard (2024, Mastercard exclusive).",
              s=["con"], lc="everyday", o="P", at="Verizon, QVC, Virgin Red", neo=[1, "Virgin Red Mastercard; Verizon Visa."], src=[["Virgin Red and Synchrony, May 2024", VIRGIN]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Home & Auto", "blurb": "Lowe's, 46 years.", "div": "syf", "rev": "home", "products": [
            P("lowes", "Lowe's", "A 46-year partnership: MyLowe's Rewards for consumers and, since April 2026, the commercial co-brand on American Express.",
              s=["home", "sme"], lc="borrow", o="P", at="Lowe's", neo=[0, "Private label and Amex."], src=[["Synchrony expands Lowe's partnership, Apr 2026", LOWES]]),
            P("homeauto", "Furniture, flooring & auto", "Ashley, Floor & Decor, Mattress Firm, Bob's, RH, Generac, Chevron, Discount Tire and the Car Care network; $30.4 billion of receivables.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["2Q26 presentation", Q2P]]),
        ]},
        {"id": "4.3", "ic": "store", "name": "Diversified & Value", "blurb": "Walmart, Sam's, TJX.", "div": "syf", "rev": "dv", "products": [
            P("sams", "Sam's Club", "Renewed January 2025 after 30 years; the Sam's Club Mastercard plus business and commercial cards.",
              s=["con", "sme"], lc="everyday", o="P", at="Sam's Club", neo=[2, "Consumer card Mastercard."], src=[["Synchrony: Sam's Club renewal, Jan 2025", SAMS]]),
            P("dvother", "TJX, JCPenney, Belk & Fleet Farm", "The fastest-growing platform, with purchase volume up 12% in 2Q26; TJX Rewards ⚠ Mastercard, the Belk Rewards Mastercard, and JCPenney with Pay Later.",
              s=["con"], lc="everyday", neo=[1, "TJX and Belk Mastercard."], src=[["2Q26 presentation", Q2P], ["FY2025 10-K", K25]]),
        ]},
        {"id": "4.4", "ic": "shield-check", "name": "Health & Wellness", "blurb": "CareCredit.", "div": "carecredit", "rev": "health", "products": [
            P("carecredit", "CareCredit", "Financing for dental, veterinary, vision and cosmetic care, with the CareCredit Rewards Mastercard as its Dual Card; $15.4 billion of receivables, half of it dental.",
              s=["health"], lc="borrow", neo=[1, "CareCredit Rewards Mastercard."], src=[["CareCredit Rewards Mastercard", CCMC], ["2Q26 presentation", Q2P]]),
            P("walgreens", "Walgreens & pet care", "The myWalgreens Mastercard (2021, with Mastercard), Mars Petcare, and pet-insurance reimbursement to CareCredit with Figo, Embrace, Pets Best and Pumpkin.",
              s=["health", "con"], lc="everyday", o="P", at="Walgreens, Mastercard", neo=[2, "Mastercard."], src=[["Walgreens, Synchrony and Mastercard, Jan 2021", WALG], ["1Q26 results", Q1]]),
        ]},
        {"id": "4.5", "ic": "rocket", "name": "Lifestyle", "blurb": "J.Crew, DICK'S, Polaris.", "div": "syf", "rev": "life", "products": [
            P("lifestyle", "Lifestyle partners", "J.Crew (Mastercard, 2023), American Eagle, DICK'S (10% back, refreshed 2026), Guitar Center, Polaris, Suzuki and, new in 2026, Indian Motorcycle.",
              s=["con"], lc="everyday", neo=[1, "J.Crew Mastercard."], src=[["J.Crew, Synchrony and Mastercard, Nov 2023", JCREW], ["2Q26 results", Q2]]),
        ]},
        {"id": "4.6", "ic": "coins", "name": "Synchrony Bank", "blurb": "$82.8 billion of deposits.", "div": "bank", "rev": "grp", "products": [
            P("deposits", "Savings, CDs & IRAs", "High-yield savings, CDs, money market and IRAs with no minimums: $82.8 billion of deposits, 83% of funding.",
              s=["save"], lc="grow", neo=[0, ""], src=[["2Q26 results", Q2], ["Synchrony: high-yield savings", "https://www.synchrony.com/banking/high-yield-savings"]]),
            P("premier", "Synchrony Premier World Mastercard", "Synchrony's own general-purpose card, 2% cash back ⚠ details unverified.",
              s=["con", "save"], lc="everyday", neo=[2, "Mastercard."], src=[["Synchrony: press kit", "https://www.synchrony.com/press-kit.html"]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Synchrony: through the partner's till, website or app first, then 290,000 care providers, dealer networks, Synchrony's own app and bank, and the wallets on their phones.",
    "tiles": [
        {"id": "5.1", "ic": "store", "name": "Partner checkouts", "blurb": "60% of applications digital.", "div": "syf", "rev": "dv", "products": [
            P("pos", "Partner stores & websites", "Applications at the partner's till or checkout, about 60% of them digital, with an answer in seconds.",
              s=["con", "partner"], lc="open", neo=[0, ""], src=[["FY2025 10-K", K25]]),
        ]},
        {"id": "5.2", "ic": "smartphone", "name": "Apps & wallets", "blurb": "OnePay, Synchrony, wallets.", "div": "syf", "rev": "digital", "products": [
            P("apps", "Synchrony & partner apps", "The OnePay app for Walmart cards, Synchrony's servicing app, Pay with Synchrony on Clover, and the phone wallets.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["FY2025 10-K", K25], ["OnePay and Synchrony, Jun 2025", ONEPAY]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Providers & dealers", "blurb": "290,000 locations.", "div": "carecredit", "rev": "health", "products": [
            P("providers", "Care providers & dealers", "CareCredit's 290,000-plus providers, and the dealer networks of Polaris, Suzuki, Indian Motorcycle and Discount Tire.",
              s=["health", "partner"], lc="open", neo=[0, ""], src=[["FY2025 10-K", K25]]),
        ]},
        {"id": "5.4", "ic": "headset", "name": "Service & hubs", "blurb": "20,000 people.", "div": "grp", "rev": "grp", "products": [
            P("service", "Servicing & customer care", "More than 20,000 employees, a new Atlanta hub (October 2026) and servicing, collections and care under DJ Casto.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Synchrony: Atlanta hub, Oct 2026", NEWS + "synchrony-leaders-celebrate-opening-of-atlanta-hub.html"]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Synchrony", "blurb": "Programme by programme.", "products": [
        P("mcatsyf", "Mastercard at Synchrony", "Mastercard carries most of Synchrony's named Dual and co-brand cards (PayPal, Sam's, OnePay/Walmart, Walgreens, J.Crew, Virgin Red, Belk, CareCredit Rewards, Synchrony Premier), with Linda Kirkpatrick on the Walgreens and OnePay deals and Chiro Aikat on J.Crew and Virgin Red. Visa has Venmo and Verizon; Amex has Lowe's Pro; two-thirds of the book is private label.",
          s=["fin"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["OnePay and Synchrony, Jun 2025", ONEPAY], ["J.Crew, Synchrony and Mastercard, Nov 2023", JCREW]]),
    ]},
    {"id": "pillar-market", "name": "US consumer credit", "blurb": "Late fees, BNPL, agents.", "products": [
        P("market", "The US consumer-credit market", "The CFPB late-fee rule vacated (April 2025), a proposed Visa/Mastercard merchant settlement, BNPL competition from Affirm, Afterpay and Klarna, Capital One/Discover and Citi Retail Services as rivals for partners, and AI agents choosing how to pay.",
          s=["con"], div="grp", rev="grp", src=[["FY2025 10-K", K25]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
