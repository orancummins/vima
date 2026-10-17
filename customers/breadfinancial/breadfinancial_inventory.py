"""Bread Financial's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the company's own unless a source says otherwise: the 2Q26 results (23 July 2026), the 2Q26
10-Q, the 4Q25 results and presentation (29 January 2026) and the FY2025 10-K (13 February 2026). Card
networks come from the partner releases and the CFPB credit card agreement database. ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

SEC = "https://www.sec.gov/Archives/edgar/data/"
Q2 = SEC + "0001101215/000110121526000068/exh991-2q26bfhepr_final.htm"
Q1 = SEC + "1101215/000110121526000036/exh991-1q26bfhepr_final.htm"
Q4 = SEC + "1101215/000110121526000007/exhibit991epr01-29x26.htm"
Q4S = SEC + "1101215/000110121526000007/exhibit993slides01-29x26.htm"
K25 = SEC + "1101215/000110121526000016/bfh-20251231.htm"
Q2Q = SEC + "0001101215/000110121526000074/bfh-20260630.htm"
LEAD = SEC + "0001101215/000110121526000065/exhibit991pressrelease-exe.htm"
MERGE = SEC + "0001101215/000110121526000081/bfh-20260903.htm"
NEWS = "https://newsroom.breadfinancial.com/"
VS = NEWS + "bread-financialr-and-victorias-secret-launch-new-co-brand-mastercardr-renew-long-standing"
SAKS = NEWS + "saks-credit-card-program"
SIGNET = NEWS + "signet-renewal-announcement"
ULTA22 = NEWS + "alliance-data-signs-long-term-renewal-agreement-ulta-beauty"
ULTA16 = SEC + "0001101215/000110121516000402/exhibit_99-1.htm"
FORD = "https://www.stocktitan.net/news/BFH/ford-and-bread-financial-accelerate-customer-benefits-with-new-hqwf95h7n7yg.html"
CFPB = "https://www.consumerfinance.gov/credit-cards/agreements/issuer/comenity-capital-bank/"
CFPB2 = CFPB + "?page=2"
CFPB3 = CFPB + "?page=3"
CFPBCB = "https://www.consumerfinance.gov/credit-cards/agreements/issuer/comenity-bank/"
CALL = "https://www.webull.com/news/15277132437464064"
WIKI = "https://en.wikipedia.org/wiki/Bread_Financial"
MCAP = "https://equibles.com/stocks/BFH"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · banks · partners", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $18.5 billion of card loans funded half by direct-to-consumer deposits, two Comenity banks becoming one, thirty years of Alliance Data heritage, Fiserv processing on the cloud, and a book in which five partners make about half the revenue.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & capital", "blurb": "$18.5 billion of loans.", "div": "grp", "rev": "grp", "products": [
            P("balance", "Balance sheet", "Loans of $18.5 billion at 30 June 2026 (up 5%) across about 34 million open accounts; interest-bearing deposits $14.7 billion, with direct-to-consumer deposits of $9.4 billion now 50% of funding.",
              s=["corp", "save"], neo=[0, ""], src=[["2Q26 results", Q2], ["2Q26 10-Q", Q2Q], ["FY2025 10-K", K25]]),
            P("earnings", "Earnings & capital", "Revenue $3.85 billion and diluted EPS $10.96 in 2025; in 2Q26 net income $146 million, EPS $3.55, net interest margin 18.5%, CET1 12.9%. About 7% of shares retired in 2Q26 alone; Moody's and Fitch upgraded the company in 2025. Market value about $4.3 billion ⚠ (August 2026).",
              s=["corp"], neo=[0, ""], src=[["2Q26 results", Q2], ["4Q25 results", Q4], ["Equibles: BFH", MCAP]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Banks, heritage & leadership", "blurb": "Two Comenity banks become one.", "div": "ccb", "rev": "grp", "products": [
            P("banks", "Comenity Bank & Comenity Capital Bank", "Comenity Bank, a Delaware credit card bank, is merging into Comenity Capital Bank, a Utah industrial bank: approved 31 July 2026 and expected on or around 1 October 2026 ⚠ completion not yet confirmed. Pro forma, about $21.4 billion of assets.",
              s=["corp"], st="flux", neo=[0, ""], src=[["8-K: bank merger, Sep 2026", MERGE], ["FY2025 10-K", K25]]),
            P("heritage", "From Alliance Data to Bread", "Formed in 1996 from J.C. Penney's card processor and The Limited's card bank; sold Epsilon (2019), bought Bread (December 2020), spun off LoyaltyOne (November 2021) and took the Bread Financial name in March 2022. Headquarters in Columbus, Ohio; about 6,000 staff.",
              s=["corp"], o="I", neo=[0, ""], src=[["Wikipedia: Bread Financial", WIKI], ["FY2025 10-K", K25]]),
            P("leadership", "Leadership", "CEO Ralph Andretta (since 2019, formerly Citi); CFO Perry Beberman; Chief Commercial Officer Val Greer retires in February 2027; Dennis McCarthy, ex-Citi, became Chief Revenue Officer in September 2026.",
              s=["corp"], st="flux", neo=[0, ""], src=[["Bread: leadership changes, Jul 2026", LEAD]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology & AI", "blurb": "Fiserv core, AWS and Microsoft cloud.", "div": "grp", "rev": "grp", "products": [
            P("tech", "Core processing & cloud", "Card processing moved to Fiserv in June 2022 (each bank paid a $1 million penalty over the conversion in 2024); infrastructure on Amazon Web Services and Microsoft; investment in machine learning and automation.",
              s=["corp", "partner"], o="P", at="Fiserv, AWS, Microsoft", neo=[0, ""], src=[["FY2025 10-K", K25]]),
            P("ai", "AI programme", "AI for productivity, innovation and risk; technology and AI spending 'ramping up' in 2026, by the CFO's account.",
              s=["corp"], st="new", neo=[0, ""], src=[["2Q26 call", CALL]]),
        ]},
        {"id": "1.4", "ic": "users-round", "name": "Partner concentration", "blurb": "Top five: 49% of revenue.", "div": "grp", "rev": "grp", "products": [
            P("partners", "Partner agreements", "About 100 brands. The five largest programmes made about 49% of 2025 revenue and 44% of loans; Signet, Ulta Beauty and Victoria's Secret each made 10% or more. All top-ten programmes run to at least 2028; agreements usually last five to ten years.",
              s=["partner", "corp"], neo=[0, ""],
              mc="Two of the three largest partners, Ulta Beauty and Victoria's Secret, carry Mastercard co-brands.",
              src=[["FY2025 10-K", K25], ["4Q25 results", Q4]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways credit moves: private-label cards that work only at the brand, co-brand cards on Mastercard and on Visa, Bread's own cards on American Express, Bread Pay instalments, and the wallets and virtual cards that carry them.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Private-label cards", "blurb": "About 43% of credit sales.", "div": "cb", "rev": "pl", "products": [
            P("privatelabel", "Private-label credit cards", "Cards that work only at the brand: KAY, Zales and Jared, Burlington, Boscov's, Carter's, Michaels, Torrid, Express, GameStop Pro and dozens more. About 43% of 2025 credit sales; they earn no interchange.", short="Private label",
              s=["con", "partner"], lc="borrow", neo=[0, "Closed loop, no network."],
              mc="The share of the book that no network touches; tokens and Click to Pay could reach it without converting it.",
              src=[["FY2025 10-K", K25], ["CFPB: Comenity Bank agreements", CFPBCB]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Mastercard co-brands", "blurb": "Victoria's Secret, Ulta, Saks.", "div": "ccb", "rev": "cobrand", "products": [
            P("mccobrand", "Co-brand cards on Mastercard", "About 18 Mastercard programmes on file: Ulta Beauty Rewards, Unity by Hard Rock, myAcademy Rewards, PENN Entertainment, Ross, Petco Pay, the Yankees and Packers cards, Ann Taylor, LOFT and Talbots World, Houzz and the Comenity Mastercard ⚠ some may be closed to new applicants.", short="Mastercard co-brands",
              s=["con", "fan", "partner"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's base at Bread: the beauty, fashion and casino programmes.",
              src=[["CFPB: Comenity Capital Bank agreements", CFPB3], ["CFPB: agreements p.2", CFPB2], ["CFPB: Comenity Bank agreements", CFPBCB]]),
            P("vsmc", "Victoria's Secret Mastercard", "Launched 29 March 2022 when the nearly 30-year partnership was renewed: 5% back at Victoria's Secret and PINK, 2% on travel, dining and streaming, tap to pay and every wallet. Mastercard's John Levitsky spoke at the launch.", short="Victoria's Secret",
              s=["con"], lc="everyday", ay="Mar 2022", o="P", at="Victoria's Secret, Mastercard", neo=[2, "Mastercard, for both the co-brand and the store card."],
              src=[["Bread: Victoria's Secret Mastercard, Mar 2022", VS]]),
            P("saksmc", "Saks World Elite Mastercard", "Won from another issuer in June 2024 and issued from August 2024: 2 points per dollar wherever Mastercard is accepted. Saks filed for Chapter 11 in January 2026.", short="Saks World Elite",
              s=["con"], lc="everyday", st="flux", ay="Aug 2024", o="A", at="Saks, Mastercard", neo=[2, "World Elite Mastercard."],
              src=[["Bread: Saks programme, Jun 2024", SAKS], ["FY2025 10-K", K25]]),
        ]},
        {"id": "2.3", "ic": "network", "name": "Visa co-brands", "blurb": "AAA, Caesars, Ford, Crypto.com.", "div": "ccb", "rev": "cobrand", "products": [
            P("visacobrand", "Co-brand cards on Visa", "About 17 Visa programmes on file: AAA and Caesars Rewards Visa Signature, Crypto.com Visa Signature (2025), Toyota Rewards and Lexus Pursuits, NFL Extra Points, IKEA, Sephora, PlayStation, Lands' End and Good Sam.", short="Visa co-brands",
              s=["con", "fan", "home"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa has won most of the new travel, auto and fintech programmes since 2025.",
              src=[["CFPB: Comenity Capital Bank agreements", CFPB], ["CFPB: agreements p.2", CFPB2], ["CFPB: agreements p.3", CFPB3]]),
            P("ford", "Ford Rewards Visa Signature", "Signed 10 March 2026 with Ford's 18-million-member Ford Rewards: up to 16 points per dollar at Ford and its dealers, plus instalment loans at nearly 3,000 dealers and online.", short="Ford (Visa)",
              s=["home"], lc="everyday", st="new", ay="Mar 2026", o="P", at="Ford, Visa", neo=[0, "Visa."],
              src=[["Ford and Bread Financial, Mar 2026", FORD]]),
        ]},
        {"id": "2.4", "ic": "gem", "name": "Bread's own cards", "blurb": "On American Express.", "div": "cashback", "rev": "dtc", "products": [
            P("cashback", "Bread Cashback American Express", "Bread's own card since April 2022: 2% unlimited cash back, no annual fee. Direct-to-consumer cards are issued on American Express.",
              s=["con", "save"], lc="everyday", ay="Apr 2022", o="P", at="American Express", neo=[0, "American Express."],
              src=[["FY2025 10-K", K25], ["Wikipedia: Bread Financial", WIKI]]),
            P("rewardsamex", "Bread Rewards American Express", "3% rewards on gas, grocery, dining and utilities; average balances on direct cards were $2,295 in 2025, the highest of any product.",
              s=["con"], lc="everyday", o="P", at="American Express", neo=[0, "American Express."],
              src=[["FY2025 10-K", K25], ["CFPB: Comenity Bank agreements", CFPBCB]]),
        ]},
        {"id": "2.5", "ic": "receipt-text", "name": "Bread Pay", "blurb": "Instalments and pay in four.", "div": "breadpay", "rev": "pay", "products": [
            P("instalments", "Bread Pay instalment loans", "Loans of 3 to 84 months at checkout, now offered with AAA, Dell, Ford, Vivint and Academy Sports as well as more than 1,400 smaller merchants.",
              s=["con", "home", "smb"], lc="borrow", st="new", o="A", neo=[0, "Bread's own."],
              mc="Competes with Affirm and Klarna at partner checkouts; Mastercard Installments could carry it on card.",
              src=[["1Q26 results", Q1], ["FY2025 10-K", K25], ["2Q26 call", CALL]]),
            P("splitpay", "Split-pay", "Interest-free pay-in-four loans from the Bread platform bought in 2020.",
              s=["con", "smb"], lc="borrow", o="A", neo=[0, "Bread's own."], src=[["FY2025 10-K", K25]]),
        ]},
        {"id": "2.6", "ic": "smartphone", "name": "Wallets & virtual cards", "blurb": "Every wallet, virtual cards next.", "div": "grp", "rev": "cobrand", "products": [
            P("wallets", "Digital wallets", "Co-brand cards work in phone wallets: the Victoria's Secret Mastercard was launched as 'compatible with all digital wallets'.",
              s=["con"], lc="move", neo=[1, "Mastercard tokens on the Mastercard cards."],
              mc="No Bread-specific tokenisation or Click to Pay announcement is public.",
              src=[["Bread: Victoria's Secret Mastercard, Mar 2022", VS]]),
            P("virtual", "Virtual cards", "Bread lists the commercialisation of virtual cards among its 2025 digital work ⚠ details not public.",
              s=["con", "partner"], lc="move", st="unconf", neo=[None, "Not disclosed."], src=[["FY2025 10-K", K25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: credit decisions and losses now falling, fraud and payment protection, loyalty run for brands, a digital suite and APIs for partners, and early work on agentic commerce.",
    "tiles": [
        {"id": "3.1", "ic": "gauge", "name": "Underwriting & credit", "blurb": "Net loss rate 6.98%.", "div": "grp", "rev": "grp", "products": [
            P("underwriting", "Credit decisions", "Decisions at the till and online; net loss rate 6.98% in 2Q26 (7.7% for 2025, 8.2% for 2024), delinquency 5.25%, reserve 11.23% of loans; 2026 loss guidance cut to 7.0–7.1%.",
              s=["con", "partner"], lc="open", neo=[0, ""], src=[["2Q26 results", Q2], ["FY2025 10-K", K25]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud & protection", "blurb": "$65 million a year of fraud losses.", "div": "grp", "rev": "grp", "products": [
            P("fraud", "Fraud controls", "Fraud operational losses of $65 million in both 2025 and 2024, down from $127 million in 2023.",
              s=["con"], lc="everyday", neo=[None, "No Mastercard fraud product announced."],
              mc="Identity checks at instant credit and Decision Intelligence on the Mastercard cards.",
              src=[["FY2025 10-K", K25]]),
            P("protection", "Payment protection", "Payment protection products, with revenue rising in 2026 through new enrolment channels.",
              s=["con"], lc="beyond", neo=[0, ""], src=[["2Q26 10-Q", Q2Q]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty & partner economics", "blurb": "Rewards run for brands.", "div": "grp", "rev": "cobrand", "products": [
            P("loyalty", "Rewards programmes", "Points, cash back and tiers run for each brand, from Victoria's Secret and Ulta to Caesars and Ford Rewards.",
              s=["con", "fan", "partner"], lc="grow", neo=[0, ""],
              mc="Card-linked, merchant-funded offers could carry some of the cost.",
              src=[["Bread: Victoria's Secret Mastercard, Mar 2022", VS], ["Ford and Bread Financial, Mar 2026", FORD]]),
            P("rsa", "Retailer share arrangements", "Payments to partners that rise with renewals; interchange and merchant fees partly offset them in 2Q26.",
              s=["partner"], lc="grow", neo=[0, ""], src=[["2Q26 call", CALL]]),
        ]},
        {"id": "3.4", "ic": "code-xml", "name": "Digital suite & APIs", "blurb": "Pre-qualification, APIs, SDKs.", "div": "grp", "rev": "grp", "products": [
            P("eds", "Enhanced Digital Suite", "Tools for partners: targeted messages and pre-qualification online, in app and in store, as rolled out for Saks; data-driven insights with Ford.",
              s=["partner"], lc="open", neo=[0, ""], src=[["Bread: Saks programme, Jun 2024", SAKS], ["Ford and Bread Financial, Mar 2026", FORD]]),
            P("apis", "APIs & SDKs", "APIs and SDKs to put Bread credit into partner checkouts and apps.",
              s=["partner", "smb"], lc="open", neo=[0, ""], src=[["FY2025 10-K", K25]]),
        ]},
        {"id": "3.5", "ic": "bot", "name": "Agentic commerce", "blurb": "Use cases with partners.", "div": "grp", "rev": "grp", "products": [
            P("agentic", "Agentic commerce", "Bread is 'collaborating with our partners to develop use cases in agentic commerce and servicing' (CEO Ralph Andretta, July 2026) ⚠ no network partner named.",
              s=["partner", "con"], lc="move", st="new", neo=[None, "No network partner named."],
              mc="Open ground: Agent Pay for the Mastercard co-brands.",
              src=[["2Q26 call", CALL]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Bread's verticals, opened out into the brands behind them: specialty apparel and luxury, beauty, travel and entertainment, jewellery and home, auto and technology, and Bread's own savings and cards.",
    "tiles": [
        {"id": "4.1", "ic": "store", "name": "Apparel & luxury", "blurb": "Victoria's Secret, Saks.", "div": "cb", "rev": "cobrand", "products": [
            P("victoria", "Victoria's Secret", "A partner for almost 30 years and one of three above 10% of revenue; store card and co-brand both on Mastercard since 2022.",
              s=["con"], lc="everyday", o="P", at="Victoria's Secret", neo=[2, "Mastercard."], src=[["Bread: Victoria's Secret Mastercard, Mar 2022", VS], ["FY2025 10-K", K25]]),
            P("apparel", "Fashion brands", "Ann Taylor, LOFT and Talbots (Mastercard), and store cards for J.Crew, Express, Torrid, Lane Bryant, Burlington and Carter's.",
              s=["con"], lc="everyday", neo=[1, "Ann Taylor, LOFT, Talbots Mastercard."], src=[["CFPB: Comenity Bank agreements", CFPBCB], ["CFPB: Comenity Capital Bank agreements", CFPB]]),
        ]},
        {"id": "4.2", "ic": "sparkles", "name": "Health & beauty", "blurb": "Ulta Beauty.", "div": "ccb", "rev": "cobrand", "products": [
            P("ulta", "Ulta Beauty", "Signed in 2016 and renewed in 2022: the Ulta Beauty Rewards card and the Ulta Beauty Rewards Mastercard; above 10% of revenue.",
              s=["con"], lc="everyday", o="P", at="Ulta Beauty", neo=[1, "Co-brand Mastercard; store card closed loop."], src=[["Alliance Data: Ulta, Jul 2016", ULTA16], ["Alliance Data: Ulta renewal, Jan 2022", ULTA22], ["CFPB: agreements p.3", CFPB3]]),
            P("sephora", "Sephora & salon brands", "The Sephora Visa and store card ⚠, Sally Beauty, Cosmo Prof and SalonCentric.",
              s=["con"], lc="everyday", neo=[0, "Sephora Visa."], src=[["CFPB: agreements p.3", CFPB3]]),
        ]},
        {"id": "4.3", "ic": "plane", "name": "Travel & entertainment", "blurb": "Caesars, Hard Rock, AAA, NFL.", "div": "ccb", "rev": "cobrand", "products": [
            P("caesars", "Caesars Rewards", "Caesars Rewards Visa Signature and Prestige cards, extended in 2025 into at least 2028.",
              s=["fan"], lc="everyday", o="P", at="Caesars, Visa", neo=[0, "Visa."], src=[["4Q25 results", Q4], ["CFPB: Comenity Bank agreements", CFPBCB]]),
            P("casinos", "Hard Rock & PENN", "Unity by Hard Rock Mastercard and the PENN Entertainment Mastercard.",
              s=["fan"], lc="everyday", o="P", at="Hard Rock, PENN, Mastercard", neo=[2, "Mastercard."], src=[["CFPB: agreements p.3", CFPB3], ["CFPB: agreements p.2", CFPB2]]),
            P("aaa", "AAA", "The AAA Visa Signature card and, from 2026, Bread Pay instalments.",
              s=["fan", "home"], lc="everyday", o="P", at="AAA, Visa", neo=[0, "Visa."], src=[["CFPB: Comenity Capital Bank agreements", CFPB], ["1Q26 results", Q1]]),
            P("sports", "NFL & teams", "NFL Extra Points Visa, and Mastercard cards for the New York Yankees and the Green Bay Packers ⚠ programme history unclear.",
              s=["fan"], lc="everyday", neo=[1, "Team cards Mastercard; NFL Visa."], src=[["CFPB: agreements p.2", CFPB2], ["CFPB: Comenity Bank agreements", CFPBCB]]),
        ]},
        {"id": "4.4", "ic": "house", "name": "Jewellery & home", "blurb": "Signet, Raymour, Ethan Allen.", "div": "cb", "rev": "pl", "products": [
            P("signet", "Signet Jewelers", "KAY, Zales, Jared and, from autumn 2026, Blue Nile: renewed long term on 15 September 2026; above 10% of revenue.",
              s=["con"], lc="borrow", o="P", at="Signet", neo=[0, "Private label."], src=[["Bread: Signet renewal, Sep 2026", SIGNET], ["FY2025 10-K", K25]]),
            P("home", "Furniture & home", "Raymour & Flanigan, Furniture First and Bed Bath & Beyond (2025), Ethan Allen (2026), Floor & Decor and Arhaus.",
              s=["home"], lc="borrow", st="new", neo=[0, "Private label."], src=[["4Q25 presentation", Q4S], ["1Q26 results", Q1]]),
        ]},
        {"id": "4.5", "ic": "rocket", "name": "Auto, tech & sport", "blurb": "Ford, Dell, Academy, Crypto.com.", "div": "ccb", "rev": "cobrand", "products": [
            P("auto", "Ford, Toyota & Lexus", "Ford Rewards (2026), Toyota Rewards and Lexus Pursuits cards, all on Visa, with store versions alongside.",
              s=["home"], lc="borrow", neo=[0, "Visa."], src=[["Ford and Bread Financial, Mar 2026", FORD], ["CFPB: agreements p.3", CFPB3]]),
            P("academy", "Academy Sports + Outdoors", "Co-brand, private label and instalments since 1Q26: the myAcademy Rewards Mastercard and store card.",
              s=["con"], lc="everyday", st="new", o="P", at="Academy Sports + Outdoors", neo=[1, "myAcademy Rewards Mastercard."], src=[["1Q26 results", Q1], ["CFPB: agreements p.2", CFPB2]]),
            P("techbrands", "Dell, Crypto.com, Cricket & Vivint", "Dell Pay credit and instalments, the Crypto.com Visa Signature, Cricket Wireless and Vivint (2025), GameStop Pro and PlayStation Visa.",
              s=["con", "home"], lc="borrow", st="new", neo=[0, "Visa or private label."], src=[["4Q25 presentation", Q4S], ["CFPB: Comenity Capital Bank agreements", CFPB]]),
        ]},
        {"id": "4.6", "ic": "coins", "name": "Bread Savings", "blurb": "$9.4 billion direct.", "div": "savings", "rev": "dtc", "products": [
            P("savings", "Savings, CDs & IRAs", "High-yield savings, CDs and IRAs online: direct-to-consumer deposits of $9.4 billion at 30 June 2026, up 16%, and half of funding.",
              s=["save"], lc="grow", neo=[0, ""], src=[["2Q26 results", Q2], ["FY2025 10-K", K25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Bread: through the brand's till, website or dealer first, then Bread's own app and service centres, and the checkouts of smaller merchants using Bread Pay.",
    "tiles": [
        {"id": "5.1", "ic": "store", "name": "Partner stores & dealers", "blurb": "Pre-qualified at the till.", "div": "grp", "rev": "pl", "products": [
            P("pos", "Partner stores, sites & dealers", "Applications and pre-qualification at the brand's till, website or app, and at Ford's nearly 3,000 dealers.",
              s=["con", "partner"], lc="open", neo=[0, ""], src=[["Bread: Saks programme, Jun 2024", SAKS], ["Ford and Bread Financial, Mar 2026", FORD]]),
        ]},
        {"id": "5.2", "ic": "smartphone", "name": "App & care", "blurb": "NPS 54.5.", "div": "grp", "rev": "grp", "products": [
            P("app", "Bread app & customer care", "An integrated mobile app and online servicing; a net promoter score of 54.5 in 2025 and a BenchmarkPortal Center of Excellence for the 21st year (September 2026).",
              s=["con", "save"], lc="everyday", neo=[0, ""], src=[["FY2025 10-K", K25], ["Bread Financial newsroom", NEWS]]),
        ]},
        {"id": "5.3", "ic": "briefcase-business", "name": "Bread Pay merchants", "blurb": "1,400+ small retailers.", "div": "breadpay", "rev": "pay", "products": [
            P("smbs", "Small-merchant checkouts", "Bread Pay at more than 1,400 small and mid-sized retailers and merchants.",
              s=["smb"], lc="open", neo=[0, ""], src=[["FY2025 10-K", K25]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Bread Financial", "blurb": "Programme by programme.", "products": [
        P("mcatbread", "Mastercard at Bread Financial", "Mastercard carries two of Bread's three biggest programmes, Victoria's Secret (2022, with Mastercard's John Levitsky) and Ulta Beauty (since 2016), plus Saks World Elite, Hard Rock, PENN and Academy. Visa has AAA, Caesars, Ford, Toyota and Crypto.com; American Express has Bread's own cards; private label and Bread Pay use no network.",
          s=["partner"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Bread: Victoria's Secret Mastercard, Mar 2022", VS], ["CFPB: agreements p.3", CFPB3]]),
    ]},
    {"id": "pillar-market", "name": "US card regulation", "blurb": "Interchange, partners, losses.", "products": [
        P("market", "The US card market", "A proposed Visa/Mastercard merchant settlement that would cut interchange, Illinois's interchange law from 1 July 2026, Saks's Chapter 11, and Synchrony, Citi and Capital One as rivals for partners ⚠ ranking not sourced.",
          s=["corp"], div="grp", rev="grp", src=[["FY2025 10-K", K25]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
