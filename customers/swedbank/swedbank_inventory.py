"""Swedbank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

One customer, four home markets: Sweden, Estonia, Latvia and Lithuania. Figures are the group's own unless
a source says otherwise: the Q2 2026 interim report and Factbook (17 July 2026), the Q1 2026 report
(29 April 2026) and the 2025 full-year report (29 January 2026); card networks are read from each market's
own card pages on 17 October 2026. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own
product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://mb.cision.com/Main/67/4375557/4196737.pdf"
Q1 = "https://internetbank.swedbank.se/ConditionsEarchive/download?bankid=1111&id=WEBDOC-PRODE294836035"
FY25 = "https://mb.cision.com/Main/67/4299468/3904840.pdf"
FB = "https://internetbank.swedbank.se/ConditionsEarchive/download?bankid=1111&id=WEBDOC-PRODE307025170"
PRES = "https://internetbank.swedbank.se/ConditionsEarchive/download?bankid=1111&id=WEBDOC-PRODE307027205"
CALL = "https://internetbank.swedbank.se/ConditionsEarchive/download?bankid=1111&id=WEBDOC-PRODE307027523"
GEC = "https://www.swedbank.com/newsroom/press-releases.details.changes-in-swedbank%E2%80%99s-group-executive-committee.D0FB291B9BBC4DEF.html"
Q3INV = "https://www.swedbank.com/newsroom/press-releases.details.invitation-%E2%80%93-swedbank%E2%80%99s-interim-report-for-the-third-quarter-2026.606A87B3336AE08C.html"
ORG = "https://www.swedbank.com/about-swedbank/organisation.html"
SUBS = "https://www.swedbank.com/about-swedbank/subsidiaries.html"
HIST = "https://www.swedbank.com/about-swedbank/our-history.html"
AI = "https://www.swedbank.com/about-swedbank/how-swedbank-uses-ai.html"
PAY = "https://www.swedbank.com/about-swedbank/subsidiaries/swedbank-pay.html"
SEDEB = "https://www.swedbank.se/privat/kort/bankkort.html"
SECRED = "https://www.swedbank.se/privat/kort/kreditkort.html"
SEC2P = "https://www.swedbank.se/privat/kort/sa-anvander-du-ditt-kort/handla-med-kort-pa-natet/click-to-pay.html"
SESWISH = "https://www.swedbank.se/privat/betala-och-overfora/swish.html"
SEBIZ = "https://www.swedbank.se/foretag/betala-och-ta-betalt/foretagskort.html"
SEISO = "https://www.swedbank.se/foretag/betala-och-ta-betalt/ny-standard-for-betalningar-i-sverige.html"
EEDEB = "https://www.swedbank.ee/private/d2d/cards/cards"
EECRED = "https://www.swedbank.ee/private/cards/cards/credit"
EEC2P = "https://www.swedbank.ee/private/cards/paymentSolutions/clicktopay"
EEPLUS = "https://www.swedbank.ee/private/cards/cards/debit/debitplus"
LVDEB = "https://www.swedbank.lv/private/cards/cards/debit"
LVCRED = "https://www.swedbank.lv/private/cards/cards/credit"
LTDEB = "https://www.swedbank.lt/private/cards/cards/debit"
LTCRED = "https://www.swedbank.lt/private/cards/cards/credit"
ENTDEAL = "https://filingreader.com/news-wire/oslo/2025-08-28/swedbank-acquires-entercard-strengthens-nordic-and-baltic-card-business"
UPI = "https://retailbankerinternational.com/news/unionpay-signs-agreement-with-swedish-acquirer-swedbank-270916-5015950"
FLV = "https://www.financelatvia.eu/wp-content/uploads/2020/09/Maksajumu-karsu-statistika-2020.-gada-2.-ceturksni.pdf"
LBBIZ = "https://www.lb.lt/lt/cbr/tab.verslo-korteles?type=1"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · four markets · savings-bank roots", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: SEK 1,934 billion of loans and RoE near 15%, four home markets from Sweden to Lithuania, savings-bank roots from 1820, every US investigation now closed, and the Swedbank 15/27 plan.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "SEK 14.5bn profit in H1 2026.", "div": "group", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Loans of SEK 1,934 billion and deposits of SEK 1,349 billion at 30 June 2026; profit of SEK 14.5 billion in the first half (RoE 13.6%, 14.3% before restructuring costs) and SEK 32.8 billion in 2025 (RoE 15.2%); CET1 17.4%; Moody's and Fitch raised their ratings in the second quarter.",
              s=["con"], neo=[0, ""], src=[["Swedbank Q2 2026 interim report", Q2], ["Swedbank full-year report 2025", FY25]]),
        ]},
        {"id": "1.2", "ic": "earth", "name": "Four home markets", "blurb": "Sweden and the three Baltic states.", "div": "group", "rev": "baltic", "products": [
            P("mkt_se", "Sweden", "3.8 million private and 246,000 corporate customers, 140 branches, 4.6 million cards and 9,758 employees; a 22% share of mortgages and 17% of private deposits.",
              s=["con", "sme"], div="se", rev="swe", neo=[0, ""], src=[["Swedbank Factbook Q2 2026", FB]]),
            P("mkt_ee", "Estonia", "0.8 million private and 130,000 corporate customers, 14 branches, 1.1 million cards; 45% of private deposits and 54% of domestic payments. H1 2026 profit SEK 1,317 million (RoAE 15.6%).",
              s=["con", "sme"], div="ee", rev="baltic", neo=[0, ""], src=[["Swedbank Factbook Q2 2026", FB]]),
            P("mkt_lv", "Latvia", "1.0 million private and 79,000 corporate customers, 19 branches, 1.1 million cards; 42% of private deposits and 62% of all payments. H1 2026 profit SEK 704 million (RoAE 12.8%).",
              s=["con", "sme"], div="lv", rev="baltic", neo=[0, ""], src=[["Swedbank Factbook Q2 2026", FB]]),
            P("mkt_lt", "Lithuania", "1.7 million private and 93,000 corporate customers, 36 branches, 1.9 million cards; 46% of private deposits and 39% of mortgages. H1 2026 profit SEK 2,289 million (RoAE 24.6%), the group's most profitable market.",
              s=["con", "sme"], div="lt", rev="baltic", neo=[0, ""], src=[["Swedbank Factbook Q2 2026", FB]]),
        ]},
        {"id": "1.3", "ic": "scale", "name": "Governance & heritage", "blurb": "Henriksson, Persson, 1820.", "div": "group", "rev": "other", "products": [
            P("leadership", "Board & executive committee", "CEO Jens Henriksson, CFO Jon Lidefelt, Chair Göran Persson (elected March 2026); Henrik Liljeblad heads Group Business Support; a new Chief Compliance Officer and Head of Corporates and Institutions are being recruited (September 2026). Heads of the Baltic banks not captured ⚠.",
              s=["corp"], neo=[0, ""], src=[["Swedbank: executive changes, Sep 2026", GEC], ["Swedbank Q1 2026 interim report", Q1], ["Swedbank: Q3 2026 invitation", Q3INV]]),
            P("heritage", "Savings-bank heritage & investigations closed", "Born from Sweden's first savings bank (Gothenburg, 1820), Swedbank since 2006 after buying Hansabank in the Baltics (2005). The US DoJ closed its AML investigation in January 2026 and a USD 50 million DFS settlement (July 2026) closed the last one.",
              s=["con"], o="I", neo=[0, ""], src=[["Swedbank: our history", HIST], ["Swedbank Q2 2026 interim report", Q2]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Swedbank 15/27", "blurb": "RoE at least 15%, C/I 0.40.", "div": "group", "rev": "other", "products": [
            P("strategy", "Swedbank 15/27 & restructuring", "Strengthen customer interactions, grow volumes and raise efficiency: RoE of at least 15%, C/I no higher than 0.40, payout 60–70%. A 2026 programme centralises IT, moves product development into the business areas and reviews cards and consumer credit: SEK 1.3 billion of one-off costs, SEK 1 billion lower costs by end-2028, about 16,800 staff by end-2027.",
              s=["corp"], st="new", neo=[0, ""], src=[["Swedbank Q2 2026 presentation", PRES], ["Swedbank Q1 2026 interim report", Q1]]),
            P("deals", "Deals", "Entercard wholly owned from 1 December 2025 (SEK 2.76 billion for Barclays' stake), Stabelo bought in November 2025 (SEK 349 million), Entercard's SEK 11 billion consumer-loan book and PayEx put up for sale in 2026.",
              s=["con"], o="A", st="flux", neo=[0, ""], src=[["Swedbank Q2 2026 interim report", Q2], ["Swedbank Q2 2026 presentation", PRES]]),
        ]},
        {"id": "1.5", "ic": "database", "name": "Technology & AI", "blurb": "IT centralised, Oken for all.", "div": "group", "rev": "other", "products": [
            P("tech", "Technology, data & AI", "IT centralised in 2026 under Group Channels and Technologies, which also owns security, financial crime, data and AI; AI used for fraud detection and internal efficiency under guidelines aligned with the EU AI Act.",
              s=["corp"], st="flux", neo=[0, ""], src=[["Swedbank full-year report 2025", FY25], ["Swedbank: how we use AI", AI]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Mastercard debit in Sweden, Mastercard credit through Entercard, Mastercard cards in all three Baltic states, Click to Pay and mobile wallets, Swedbank Pay's acquiring, and the account rails — Swish, Bankgirot and Baltic transfers — that carry most payments.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit in Sweden", "blurb": "Bankkort Mastercard.", "div": "se", "rev": "swe", "products": [
            P("sedebit", "Bankkort Mastercard", "Swedbank's Swedish debit card is a Mastercard (Maestro no longer sold), SEK 300 a year, made of recycled plastic; 4.6 million cards and 393 million purchases in the second quarter of 2026. An earlier move from Visa to Mastercard is reported but undated ⚠.", short="Debit (Mastercard)",
              s=["con"], lc="everyday", o="B", at="Mastercard", neo=[2, "Mastercard debit."],
              mc="The core of the relationship: 4.6 million Swedish debit cards on Mastercard.",
              src=[["swedbank.se: Bankkort", SEDEB], ["Swedbank Q2 2026 interim report", Q2]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit, company cards & Entercard", "blurb": "Mastercard Standard to Platinum.", "div": "entercard", "rev": "other", "products": [
            P("secredit", "Betal- och kreditkort Mastercard", "Mastercard Standard (SEK 195 a year), Guld (SEK 495) and Platinum (SEK 1,700, 1,200 lounges, concierge), issued by Entercard and sold by Swedbank and the savings banks.", short="Credit (Mastercard)",
              s=["con"], lc="borrow", o="P", at="Entercard", neo=[2, "Mastercard credit."], src=[["swedbank.se: Kreditkort", SECRED]]),
            P("entercard", "Entercard", "Wholly owned since December 2025: 1.4 million cards (0.6 million for Swedbank and the savings banks, 0.8 million re:member and partner cards) in Sweden, Norway, Denmark and Finland; its unsecured loan book is for sale and its card issuing is being folded into one Swedbank card business.", short="Entercard",
              s=["con"], lc="borrow", st="flux", ay="Dec 2025", o="A", neo=[1, "Swedbank cards on Mastercard; re:member and partner networks ⚠."],
              mc="Card synergies are an explicit 2026 goal: a consolidation Mastercard can shape.",
              src=[["Swedbank Q2 2026 interim report", Q2], ["Swedbank Q1 2026 interim report", Q1], ["Entercard stake deal, Aug 2025", ENTDEAL]]),
            P("bizcards", "Company cards", "Account-linked and invoiced company cards for Swedish businesses, usable in mobile and watch wallets; the network is not stated on the page ⚠.",
              s=["sme"], lc="everyday", div="se", rev="swe", neo=[None, "Network not stated."], src=[["swedbank.se: Företagskort", SEBIZ]]),
        ]},
        {"id": "2.3", "ic": "flag", "name": "Baltic cards", "blurb": "Mastercard in Estonia, Latvia, Lithuania.", "div": "group", "rev": "baltic", "products": [
            P("eecards", "Estonia: debit & credit", "Debit card, Debit card Plus, ISIC Mastercard student and Mastercard Private Banking cards, and Mastercard credit up to Platinum (no FX fee); 1.1 million cards, 77 million purchases in Q2 2026. No Visa consumer card on the site.", short="Estonia (Mastercard)",
              s=["con"], lc="everyday", div="ee", at="Mastercard", neo=[2, "Mastercard."], src=[["swedbank.ee: debit cards", EEDEB], ["swedbank.ee: credit cards", EECRED], ["Swedbank Factbook Q2 2026", FB]]),
            P("lvcards", "Latvia: debit & credit", "Swedbank Mastercard debit and credit cards with Priceless, LoungeKey and Flexiroam data roaming; 1.1 million cards, 86 million purchases in Q2 2026. The site also mentions Visa cards issued by Swedbank ⚠ (legacy or business).", short="Latvia (mostly Mastercard)",
              s=["con"], lc="everyday", div="lv", at="Mastercard", neo=[1, "Mastercard, some Visa ⚠."], src=[["swedbank.lv: debit cards", LVDEB], ["swedbank.lv: credit cards", LVCRED], ["Finance Latvia card statistics Q2 2020", FLV]]),
            P("ltcards", "Lithuania: debit & credit", "Contactless Debit Mastercard, Mastercard WEB for young people from age six, Mastercard Standard, Gold and Platinum credit; 1.9 million cards, 137 million purchases in Q2 2026. The central bank's table lists a Swedbank Visa Business Debit card ⚠.", short="Lithuania (Mastercard)",
              s=["con"], lc="everyday", div="lt", at="Mastercard", neo=[2, "Mastercard consumer cards; business Visa ⚠."], src=[["swedbank.lt: debit cards", LTDEB], ["swedbank.lt: credit cards", LTCRED], ["Bank of Lithuania: business cards", LBBIZ]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Click to Pay & wallets", "blurb": "In all four markets.", "div": "group", "rev": "swe", "products": [
            P("c2p", "Click to Pay", "Mastercard Click to Pay for Mastercard debit in Sweden (signed with Mobile BankID) and for all cards in Estonia, Latvia and Lithuania, with a digital card number for each purchase.",
              s=["con"], lc="move", o="P", at="Mastercard", neo=[3, "Mastercard Click to Pay."], src=[["swedbank.se: Click to Pay", SEC2P], ["swedbank.ee: Click to Pay", EEC2P]]),
            P("wallets", "Apple Pay, Google Pay & wearables", "Mobile and wearable payments with Apple Pay, Google Pay, Garmin Pay, rings and key fobs in the Baltics, and phone and watch payments in Sweden.",
              s=["con"], lc="move", o="P", at="Apple, Google, Garmin", neo=[2, "Tokens on Mastercard cards."], src=[["swedbank.ee: Debit card Plus", EEPLUS], ["swedbank.lv: debit cards", LVDEB]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acquiring", "blurb": "Swedbank Pay: 983m a quarter.", "div": "pay", "rev": "ci", "products": [
            P("swpay", "Swedbank Pay", "In-store and online acceptance of cards, Swish and invoice in the Nordics and Baltics, more than 3 billion card transactions a year; 983 million acquired in Q2 2026, down 5% in the Nordics and up 5% in the Baltics. Took over PayEx's card acquiring in late 2025; UnionPay accepted since 2016.",
              s=["merchant", "sme"], lc="move", st="flux", o="B", neo=[1, "Accepts every network."],
              mc="Nordic acquired volume fell 4% to SEK 225 billion in Q2 2026: room for acquirer risk and merchant data tools.",
              src=[["Swedbank: Swedbank Pay", PAY], ["Swedbank Q2 2026 interim report", Q2], ["Retail Banker International: UnionPay, Sep 2016", UPI]]),
        ]},
        {"id": "2.6", "ic": "arrow-left-right", "name": "Account payments", "blurb": "Swish, Bankgirot, Baltic transfers.", "div": "group", "rev": "swe", "products": [
            P("swish", "Swish", "Sweden's bank-owned mobile payments, co-founded by Swedbank in 2012 (it is a shareholder of Getswish AB); up to SEK 10,000 a day to people and SEK 30,000 to businesses; Swish Recurring Payments launched in Q1 2026.",
              s=["con", "sme"], lc="move", div="se", st="new", o="P", at="Getswish", neo=[0, "Bank-owned account rail."],
              mc="Swish Recurring now competes with card-on-file subscriptions.",
              src=[["swedbank.se: Swish", SESWISH], ["Swedbank Q1 2026 interim report", Q1], ["Swedbank full-year report 2025", FY25]]),
            P("sepay", "Swedish payments & ISO 20022", "284 million domestic payments in Q2 2026 and 34% of Bankgirot payments; Sweden's new infrastructure ends Bankgirot formats on 1 September 2026 in favour of ISO 20022; 1.3 million international payments a quarter.",
              s=["sme", "corp"], lc="move", div="se", st="flux", neo=[0, ""], src=[["Swedbank Q2 2026 interim report", Q2], ["swedbank.se: ISO 20022", SEISO]]),
            P("balticpay", "Baltic transfers & cross-border", "155 million domestic payments in the Baltics in Q2 2026 (up 10%) and 13 million international payments (up 27%); SEPA instant obligations not covered in sources ⚠.",
              s=["con", "corp"], lc="move", rev="baltic", neo=[0, ""],
              mc="Fast-growing Baltic cross-border flows are a fit for Mastercard Move ⚠.",
              src=[["Swedbank Q2 2026 interim report", Q2], ["Swedbank Factbook Q2 2026", FB]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: BankID and Smart-ID with Mastercard Identity Check, AI fraud detection, the Oken assistant for staff, Priceless and card benefits, Mikroinvest round-ups and corporate cash management.",
    "tiles": [
        {"id": "3.1", "ic": "fingerprint", "name": "Identity", "blurb": "BankID, Smart-ID, Identity Check.", "div": "group", "rev": "swe", "products": [
            P("bankid", "BankID & Smart-ID", "Mobile BankID signs Swish, Click to Pay and internet-bank actions in Sweden (Swedbank part-owns Finansiell ID-teknik BID AB); Smart-ID, Mobile-ID and eID confirm purchases in the Baltics.",
              s=["con"], lc="open", o="P", at="BankID, Smart-ID", neo=[0, ""], src=[["Swedbank full-year report 2025", FY25], ["swedbank.ee: debit cards", EEDEB]]),
            P("idcheck", "Mastercard Identity Check", "3-D Secure for online card purchases in Estonia and Lithuania, confirmed with biometrics, Smart-ID or the internet bank.",
              s=["con"], lc="move", rev="baltic", o="P", at="Mastercard", neo=[3, "Mastercard's own."], src=[["swedbank.ee: debit cards", EEDEB], ["swedbank.lt: debit cards", LTDEB]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud & financial crime", "blurb": "AI detection, crypto warnings.", "div": "group", "rev": "other", "products": [
            P("fraud", "Fraud & financial-crime controls", "AI-based fraud detection, warnings about crypto fraud and controls on temporary limit raises (late 2025), and the AML programme rebuilt since 2019.",
              s=["con", "sme"], lc="everyday", neo=[0, "Swedbank's own."],
              mc="No public scam-scoring or Decision Intelligence deal: an open door.",
              src=[["Swedbank: how we use AI", AI], ["Swedbank full-year report 2025", FY25]]),
        ]},
        {"id": "3.3", "ic": "bot", "name": "AI", "blurb": "Oken for every employee.", "div": "group", "rev": "other", "products": [
            P("oken", "Oken", "An AI assistant rolled out to all employees during 2026 for quality, security, efficiency and cost control; customer-facing AI not announced.",
              s=["corp"], st="new", neo=[0, ""],
              mc="Agentic payments are untouched ground.",
              src=[["Swedbank Q2 2026 call transcript", CALL]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Benefits & round-ups", "blurb": "Priceless, LoungeKey, Mikroinvest.", "div": "group", "rev": "baltic", "products": [
            P("priceless", "Mastercard Priceless", "Concert pre-sales and experiences for Swedbank Mastercard holders in Sweden (priceless.com/swedbank), Latvia and Lithuania.",
              s=["con"], lc="grow", o="P", at="Mastercard", neo=[3, "Mastercard's own."], src=[["swedbank.se: Bankkort", SEDEB], ["swedbank.lv: debit cards", LVDEB], ["swedbank.lt: debit cards", LTDEB]]),
            P("benefits", "Card insurance & travel benefits", "Travel insurance and purchase protection added to cards in Estonia (Q3 2025) and Latvia and Lithuania (Q4 2025); LoungeKey, Mastercard Airport Fast Track and Flexiroam data roaming on Baltic credit cards.",
              s=["con"], lc="grow", st="new", o="P", at="Mastercard", neo=[2, "Mastercard benefits."], src=[["Swedbank full-year report 2025", FY25], ["swedbank.lv: credit cards", LVCRED]]),
            P("mikroinvest", "Mikroinvest", "Rounds up Baltic card payments and invests the difference in Swedbank Robur funds; more than 100,000 users by Q2 2026.",
              s=["saver"], lc="grow", st="new", neo=[1, "Runs on Mastercard card spend."],
              mc="Card-linked savings and offers could build on it.",
              src=[["Swedbank Q2 2026 interim report", Q2]]),
        ]},
        {"id": "3.5", "ic": "webhook", "name": "Cash management & integration", "blurb": "ERP links, ISO 20022.", "div": "group", "rev": "ci", "products": [
            P("cashmgmt", "Corporate internet bank & ERP integration", "Liquidity-management tools added to the corporate internet bank in Q2 2026, ERP integration on Swedbank's ISO 20022 message guide, e-invoicing and the Nordics' first digital guarantee transactions (Q1 2026).",
              s=["corp", "sme"], lc="move", st="new", neo=[0, ""], src=[["Swedbank Q2 2026 interim report", Q2], ["swedbank.se: ISO 20022", SEISO], ["Swedbank Q1 2026 interim report", Q1]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: about a fifth of Swedish mortgages and two-fifths of Baltic ones, everyday accounts, Entercard consumer credit, corporate banking across four markets, and Swedbank Robur funds and pensions.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Mortgages", "blurb": "22% in Sweden, ~40% in the Baltics.", "div": "se", "rev": "swe", "products": [
            P("semort", "Swedish mortgages & Swedbank Hypotek", "SEK 945 billion of Swedish mortgages, a 22% share with the savings banks; about 20% of market growth in Swedbank's own channels in Q2 2026; Hypotek has about 1 million customers.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["Swedbank Factbook Q2 2026", FB], ["Swedbank Q2 2026 interim report", Q2]]),
            P("stabelo", "Stabelo", "Digital mortgage challenger bought in November 2025, run under its own brand and adding about 3 points of Swedbank's market growth in Q1 2026.",
              s=["home"], lc="borrow", st="new", ay="Nov 2025", o="A", neo=[0, ""], src=[["Swedbank Q1 2026 interim report", Q1]]),
            P("balticmort", "Baltic mortgages", "SEK 147 billion, with shares of 39% in Estonia, 41% in Latvia and 39% in Lithuania; an automated digital mortgage offer giving a rate within minutes launched in all three countries in Q2 2026.",
              s=["home"], lc="borrow", div="group", rev="baltic", st="new", neo=[0, ""], src=[["Swedbank Q2 2026 interim report", Q2], ["Swedbank Factbook Q2 2026", FB]]),
        ]},
        {"id": "4.2", "ic": "wallet", "name": "Everyday accounts", "blurb": "17% to 46% of private deposits.", "div": "group", "rev": "swe", "products": [
            P("deposits", "Accounts & deposits", "SEK 1,349 billion of customer deposits; private-deposit shares of 17% in Sweden, 45% in Estonia, 42% in Latvia and 46% in Lithuania; every account comes with a Mastercard debit card.",
              s=["con"], lc="everyday", neo=[1, "Mastercard debit attached."], src=[["Swedbank Factbook Q2 2026", FB]]),
        ]},
        {"id": "4.3", "ic": "hand-coins", "name": "Consumer credit", "blurb": "Loan book for sale.", "div": "entercard", "rev": "other", "products": [
            P("consumer", "Consumer loans", "Entercard's unsecured consumer-loan portfolio (SEK 11.4 billion contractual, 83% Swedish) is held for sale; Swedbank is building one consumer-credit business under its own credit standards.",
              s=["con"], lc="borrow", st="flux", neo=[0, ""], src=[["Swedbank Q2 2026 interim report", Q2], ["Swedbank Q2 2026 presentation", PRES]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Corporate & SME", "blurb": "548,000 business customers.", "div": "group", "rev": "ci", "products": [
            P("corporate", "Corporates & Institutions", "SEK 588 billion of lending, one of the largest arrangers in the Swedish bond market, FX and rates trading, and branches in Norway, Finland, the US and China; corporate lending grew SEK 18 billion in Q2 2026.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Swedbank Q2 2026 interim report", Q2], ["Swedbank: organisation", ORG]]),
            P("sme", "Small-business banking", "About 548,000 corporate customers across the four markets; Baltic SMEs backed by a European Investment Fund guarantee programme and a renewed leasing offer (Q1 2026).",
              s=["sme"], lc="borrow", rev="baltic", neo=[0, ""], src=[["Swedbank Factbook Q2 2026", FB], ["Swedbank Q1 2026 interim report", Q1]]),
            P("payex", "PayEx", "Invoicing, factoring, sales finance and collection since 1972; about SEK 400 million of income and 300 staff; Swedbank decided to sell it in April 2026.",
              s=["sme"], lc="beyond", div="pay", rev="other", st="flux", o="A", neo=[0, ""], src=[["Swedbank Q1 2026 interim report", Q1], ["Swedbank Q2 2026 presentation", PRES]]),
        ]},
        {"id": "4.5", "ic": "coins", "name": "Savings & pensions", "blurb": "Robur leads Sweden and the Baltics.", "div": "robur", "rev": "wealth", "products": [
            P("robur", "Swedbank Robur", "Leading fund manager in Sweden (22% share) and the Baltics (40%, 37% and 33%); SEK 22 billion of Swedish net inflows in Q2 2026, against SEK 18 billion of outflows in Lithuania after its pension reform.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["Swedbank Q2 2026 interim report", Q2]]),
            P("insurance", "Swedbank Försäkring & Baltic insurance", "Sweden's largest unit-linked insurer with SEK 512 billion under management; life and non-life insurance in the Baltics.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["Swedbank: subsidiaries", SUBS], ["Swedbank Factbook Q2 2026", FB]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Swedbank: the app for 6.3 million digitally active customers, 209 branches and the phone bank, and the savings banks, Fastighetsbyrån and Stabelo as partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "App & internet bank", "blurb": "6.3m digitally active.", "div": "group", "rev": "swe", "products": [
            P("app", "Swedbank app & internet bank", "3.7 million digitally active customers in Sweden (with the savings banks) and 2.6 million in the Baltics (0.6m Estonia, 0.7m Latvia, 1.2m Lithuania); a new app navigation in Q2 2026.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["Swedbank Factbook Q2 2026", FB], ["Swedbank Q2 2026 interim report", Q2]]),
        ]},
        {"id": "5.2", "ic": "headset", "name": "Branches & phone", "blurb": "209 branches.", "div": "group", "rev": "swe", "products": [
            P("branches", "Branches & telephone bank", "140 branches in Sweden, 14 in Estonia, 19 in Latvia and 36 in Lithuania; more than 80% of Swedish calls answered within three minutes in 2025 and a Senior Line from Q1 2026.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Swedbank Factbook Q2 2026", FB], ["Swedbank full-year report 2025", FY25]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Savings banks & partners", "blurb": "Savings banks, Fastighetsbyrån.", "div": "se", "rev": "swe", "products": [
            P("savingsbanks", "Savings banks & Fastighetsbyrån", "Independent Swedish savings banks sell Swedbank products (4% of mortgages, 1.2 million digital customers) and part-own the bank; Fastighetsbyrån estate agents refer buyers into Swedbank's mortgage process.",
              s=["home", "con"], lc="open", o="P", at="Savings banks", neo=[0, ""], src=[["Swedbank Factbook Q2 2026", FB], ["Swedbank Q2 2026 interim report", Q2], ["Swedbank: our history", HIST]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Swedbank", "blurb": "Every consumer card, four markets.", "products": [
        P("mcatswedbank", "Mastercard at Swedbank", "Every consumer debit and credit card on Swedbank's Swedish, Estonian, Latvian and Lithuanian sites is a Mastercard, about 8.6 million cards plus Entercard's 1.4 million, with Priceless, Click to Pay, Identity Check and LoungeKey on top. No public network agreement was found; Visa keeps a foothold through Visa Inc. shares, some Latvian and business Visa cards ⚠.",
          s=["con"], div="group", rev="other", mc="The relationship this map is drawn for.",
          src=[["swedbank.se: Bankkort", SEDEB], ["swedbank.lt: debit cards", LTDEB], ["Swedbank Q2 2026 interim report", Q2]]),
    ]},
    {"id": "pillar-market", "name": "Sweden & the Baltics", "blurb": "Account rails, pension reform, ISO 20022.", "products": [
        P("market", "The markets", "Sweden's move to ISO 20022 and a new payment infrastructure in 2026, Swish as the default person-to-person rail, Riksbank interest-free deposits (SEK 5.4 billion for Swedbank), and Lithuania's pension reform allowing early withdrawals; Baltic GDP growth of about 2–3% expected in 2026.",
          s=["con"], div="group", rev="baltic", src=[["Swedbank Q2 2026 interim report", Q2], ["swedbank.se: ISO 20022", SEISO]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
