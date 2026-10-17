"""Landsbankinn's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the H1 2026 results and fact book (23 July 2026), the
Q1 2026 results (30 April 2026), the 2025 results presentation and the 2025 annual report (February 2026). No
Landsbankinn page names a card network; Visa is inferred from the price list, card artwork and the Visa emergency
line. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://www.landsbankinn.is/en/the-bank/investor-relations/news/landsbankinns-results-for-the-first-half-of-2026"
FB = "https://www.landsbankinn.is/uploads/documents/arsskyrsluroguppgjor/fact-book-h1-2026-en.pdf"
Q1 = "https://www.landsbankinn.is/en/the-bank/investor-relations/news/financial-results-of-landsbankinn-for-the-first-three-months-of-2026"
FY25 = "https://www.landsbankinn.is/uploads/documents/arsskyrsluroguppgjor/consolidated-financial-report-2025-presentation-en.pdf"
GOV = "https://arsskyrsla2025.landsbankinn.is/en/governance-and-organisation/governance"
STRAT = "https://arsskyrsla2025.landsbankinn.is/en/governance-and-organisation/strategy"
DEV = "https://arsskyrsla2025.landsbankinn.is/en/satisfied-customers/continuous-development"
PERS = "https://arsskyrsla2025.landsbankinn.is/en/satisfied-customers/personal-banking"
CORP = "https://arsskyrsla2025.landsbankinn.is/en/satisfied-customers/corporate-banking"
NEWS25 = "https://arsskyrsla2025.landsbankinn.is/en/governance-and-organisation/main-news-from-2025"
PRICE = "https://landsbankinn.is/uploads/documents/verdskra/verdskra-2025-01-01.pdf"
DEBIT = "https://landsbankinn.is/en/personal/cards/debit-card"
CREDIT = "https://landsbankinn.is/en/personal/cards/credit-cards"
CARDS = "https://www.landsbankinn.is/en/personal/cards"
BIZART = "https://images.prismic.io/landsbankinn/edcb5d89-d680-434f-b7b3-c888db272a1a_LBI+231206_Kort_Web_Business_1920x1920px.png"
AURB = "https://aurbjorg.is/en/kort/debit"
SAGA = "https://www.icelandair.com/en-ie/frequent-flyer/credit-cards/"
ACQ = "https://www.landsbankinn.is/en/corporate/acquiring"
ACQI = "https://www.landsbankinn.is/en/corporate/acquiring/acquiring-instructions"
RAPYD = "https://www.landsbankinn.is/en/news/2023/04/27/payment-card-bills-now-issued-by-rapyd-europe-not-valitor"
VBV = "https://www.landsbankinn.is/en/news/2021/11/09/verification-system-for-card-use-changes-to-visa"
DUP26 = "https://www.landsbankinn.is/en/news/2026/07/31/double-booked-payment-card-transactions"
SIA = "https://mondovisione.com/media-and-resources/news/central-bank-of-iceland-launches-with-sia-the-new-interbank-payment-system-cbi-20201126/"
TMDEAL = "https://www.landsbankinn.is/en/the-bank/investor-relations/news/contract-providing-for-landsbankinns-purchase-of-tm-concluded"
TMDONE = "https://www.mfn.se/one/a/kvika-banki/kvika-banki-hf-sale-of-tm-finalised-6619278a"
YAY = "https://www.landsbankinn.is/en/news/2025/06/04/yay-and-landsbankinn-found-yayland"
GMI = "https://www.landsbankinn.is/en/news/2025/10/23/landsbankinn-sells-its-share-in-greidslumidlun-islands-ehf"
ISB = "https://www.landsbankinn.is/en/news/2025/05/16/landsbankinn-corporate-finance-advisor-to-the-government-in-successful-islandsbanki-po"
CORPNB = "https://www.landsbankinn.is/en/news/2025/02/20/new-and-even-better-online-banking-for-corporates"
POLISH = "https://www.landsbankinn.is/en/news/2025/02/18/new-savings-account-in-polish-currency"
ANNIV = "https://www.landsbankinn.is/en/news/2026/08/18/140-and-70-year-anniversaries-of-landsbankinn-and-tm"
BLOOM = "https://news.bloomberglaw.com/banking-law/cyber-threats-spark-iceland-plan-to-process-payments-at-home"
ALTH = "https://www.althingi.is/altext/154/s/1770.html"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · state owner · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: ISK 2.4 trillion of assets and ROE of 13.4%, a state that owns 98.2%, a bank whose history runs back to 1886, its own technology and AI, and an 'ever-smarter bank' strategy that bought TM.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "ISK 2.4trn, ROE 13.4%.", "div": "lb", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of ISK 2,417 billion (about EUR 16.8 billion), loans of ISK 1,934 billion and deposits of ISK 1,331 billion at 30 June 2026; profit after tax of ISK 22.1 billion in the half (ROE 13.4%, cost-income 31.5%) and ISK 38.0 billion in 2025; total capital ratio 24.7%.",
              s=["con"], neo=[0, ""], src=[["H1 2026 results", H1], ["H1 2026 fact book", FB], ["2025 results presentation", FY25]]),
            P("ratings", "Ratings & dividends", "S&P A-/A-2 with a stable outlook, affirmed March 2026 after an upgrade in 2025; covered bonds A+. An ISK 34.9 billion dividend for 2025 (ISK 18.9 billion regular, ISK 16.1 billion special), mostly to the state.",
              s=["inv"], neo=[0, ""], src=[["Q1 2026 results", Q1], ["H1 2026 results", H1]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Owner & leadership", "blurb": "The state holds 98.2%.", "div": "lb", "rev": "other", "products": [
            P("owner", "State ownership", "The Icelandic State holds 98.2%, managed by the Ministry of Finance and Economic Affairs; about 770 shareholders; the shares are not listed. The state sold the last of Íslandsbanki in May 2025, with Landsbankinn advising; no sale of Landsbankinn is announced ⚠.",
              s=["corp"], o="I", neo=[0, ""], src=[["H1 2026 fact book", FB], ["Annual report 2025: governance", GOV], ["Íslandsbanki sale, May 2025", ISB]]),
            P("leadership", "Board & executive board", "Chair Jón Þorvarður Sigurgeirsson; CEO Lilja Björk Einarsdóttir; CFO Hreiðar Bjarnason; Helgi Teitur Helgason runs Personal Banking, Árni Þór Þorbjörnsson Corporate Banking and Arinbjörn Ólafsson IT.",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025: governance", GOV]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage", "blurb": "140 years in 2026.", "div": "lb", "rev": "other", "products": [
            P("heritage", "Heritage", "The current bank was set up on 7 October 2008; its predecessor's history runs back to 1886, and it marked 140 years in August 2026 alongside TM's 70. Head office at Reykjastræti 6, Reykjavík.",
              s=["con"], o="I", neo=[0, ""], src=[["H1 2026 fact book", FB], ["Landsbankinn: 140 and 70 years, Aug 2026", ANNIV]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology", "blurb": "Containers and TM's systems.", "div": "lb", "rev": "other", "products": [
            P("tech", "Technology platform", "TM's systems and software development moved in-house in 2025, the largest IT project of the year; container technology adopted, legacy systems retired; releases up 15% on 2024 and about 90% on 2021, with about 50% fewer incidents than in 2021.",
              s=["corp"], o="B", neo=[0, ""], src=[["Annual report 2025: continuous development", DEV]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "An ever-smarter bank.", "div": "lb", "rev": "other", "products": [
            P("strategy", "An ever-smarter bank", "Strategy since 2021 with three pillars: satisfied customers, continuous development and passion for success. 2026 guidance: ROE 11–13%, cost-income 32–35%, CET1 above 18% and a 50% payout plus a special dividend.",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025: strategy", STRAT], ["2025 results presentation", FY25]]),
            P("deals", "Deals", "TM bought from Kvika for about ISK 32.3 billion (completed 28 February 2025); Yayland formed with YAY for prepaid and gift cards (June 2025); a 47.9% stake in Greiðslumiðlun Íslands sold to Síminn at an ISK 3.5 billion valuation (October 2025) ⚠ completion not confirmed.",
              s=["con", "corp"], o="A", st="new", neo=[0, ""], src=[["TM contract concluded", TMDEAL], ["Kvika: sale of TM finalised", TMDONE], ["Yayland, Jun 2025", YAY], ["GMÍ stake sale, Oct 2025", GMI]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Visa debit and Visa credit cards with Saga Points, Visa business cards and prepaid cards run with Yayland, mobile wallets and Click to Pay, an acquiring business with 27% of the market that takes Visa and Mastercard, and instant and cross-border transfers.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Visa debit.", "div": "lb", "rev": "personal", "products": [
            P("debit", "Landsbankinn debit card", "Issued to the current account: ISK 790 a year, free for ages 9–24, ISK 18 a transaction (free to 18); ATM withdrawals up to ISK 300,000 a day. On Visa: the price list charges a margin on Visa's rate for all foreign card transactions and the emergency line is for Visa cards.", short="Debit (Visa)",
              s=["con", "young"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Landsbankinn: debit card", DEBIT], ["Price list, Jan 2025", PRICE], ["Aurbjörg: debit cards", AURB]]),
            P("youth", "Klassi & Náman", "Debit and student cards for young customers with an ISK 50,000 daily ATM limit, opened with a bank account from age 9 ⚠ Visa inferred.",
              s=["young"], lc="open", o="P", at="Visa", neo=[0, "Visa ⚠."], src=[["Landsbankinn: cards", CARDS]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Visa, with Saga Points.", "div": "lb", "rev": "personal", "products": [
            P("credit", "Personal credit cards", "General (ISK 3,700), Gold (ISK 14,400), Platinum (ISK 24,900, Priority Pass) and Premium (ISK 44,000, Saga Lounge); earn Aukakrónur or Saga Points; instalments at ISK 250 a transaction. Visa inferred ⚠ no page names it; separate Mastercard terms were dropped in March 2019.", short="Credit (Visa ⚠)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa ⚠."],
              mc="Iceland's biggest retail bank issues no Mastercard today.",
              src=[["Landsbankinn: credit cards", CREDIT], ["Price list, Jan 2025", PRICE]]),
            P("saga", "Icelandair Saga Club cards", "Gold, Platinum and Premium Vildarkort earning Icelandair Saga Points on domestic spend; Icelandair also co-brands with Arion, Íslandsbanki and Kvika.",
              s=["con"], lc="grow", o="P", at="Icelandair, Visa", neo=[0, "Visa ⚠."], src=[["Icelandair: credit cards", SAGA], ["Price list, Jan 2025", PRICE]]),
        ]},
        {"id": "2.3", "ic": "briefcase", "name": "Business & prepaid cards", "blurb": "Visa Business; Yayland.", "div": "lb", "rev": "corporate", "products": [
            P("bizcards", "Business & purchase cards", "Business debit, Business and Business Premium credit cards (ISK 9,900–32,900, with or without Saga Points) and purchase cards (ISK 2,000). The card artwork carries Visa.", short="Business cards (Visa)",
              s=["sme", "corp"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Landsbankinn: business card artwork", BIZART], ["Price list, Jan 2025", PRICE]]),
            P("prepaid", "Prepaid & gift cards", "Plúskort, Plúskort+ and Vasapeningar prepaid cards and the Landsbankinn gift card (ISK 540); since June 2025 issued and run by Yayland, a company formed with fintech YAY ⚠ network not stated.",
              s=["con", "young", "sme"], lc="everyday", st="new", ay="Jun 2025", o="P", at="YAY", div="yayland", neo=[None, "Network not stated."],
              mc="A new prepaid issuer with no network named.",
              src=[["Yayland, Jun 2025", YAY], ["Landsbankinn: cards", CARDS]]),
        ]},
        {"id": "2.4", "ic": "smartphone", "name": "Wallets & Click to Pay", "blurb": "Apple Pay, Google Pay, Click to Pay.", "div": "lb", "rev": "personal", "products": [
            P("wallets", "Mobile wallets", "Debit, credit and gift cards in Apple Pay, Google Pay, Garmin Pay and Fitbit Pay, with the same limits and benefits as the card.",
              s=["con", "young"], lc="everyday", o="P", at="Apple, Google", neo=[0, "Visa cards."], src=[["Landsbankinn: debit card", DEBIT], ["Landsbankinn: cards", CARDS]]),
            P("c2p", "Click to Pay", "Offered to cardholders from the end of 2025 for online shopping, with tokenised card data and no card number typed in. The standard is shared by the card schemes; Landsbankinn's cards are Visa ⚠.",
              s=["con"], lc="move", st="new", ay="End-2025", o="P", at="Visa", neo=[0, "Visa cards ⚠."], src=[["Annual report 2025: continuous development", DEV]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acquiring", "blurb": "27% share, Visa and Mastercard.", "div": "lb", "rev": "corporate", "products": [
            P("acquiring", "Landsbankinn Acquiring", "Launched in 2023: about 25% of the market at end-2025 and 27% at end-March 2026; transactions and turnover tripled in 2025 to about 7,227 an hour on 3,300 terminals; Verifone devices; blended or interchange++ pricing. Accepts Visa and Mastercard and no other brands.", short="Acquiring (Visa & Mastercard)",
              s=["sme", "corp"], lc="move", st="new", ay="2023", o="B", at="Verifone", neo=[1, "Accepts Mastercard and Visa."],
              mc="Mastercard's only visible place in the bank, and its fastest-growing line.",
              src=[["Landsbankinn: acquiring", ACQ], ["Acquiring instructions", ACQI], ["Q1 2026 results", Q1], ["Annual report 2025: corporate banking", CORP]]),
            P("ecom", "Online & in-app acceptance", "A development kit for POS integration, ready connections for e-commerce platforms, Android and iOS kits, Apple Pay and Google Pay, and settlement data sent by API into accounting systems.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts Mastercard and Visa."], src=[["Landsbankinn: acquiring", ACQ], ["Annual report 2025: corporate banking", CORP]]),
        ]},
        {"id": "2.6", "ic": "arrow-left-right", "name": "Transfers", "blurb": "Instant ISK, SWIFT, SEPA.", "div": "lb", "rev": "other", "products": [
            P("transfers", "Domestic transfers", "Instant krónur transfers between Icelandic banks over the Central Bank's interbank system, run on SIA's platform since November 2020.",
              s=["con", "sme"], lc="move", o="P", at="Central Bank of Iceland", neo=[0, ""], src=[["Mondo Visione: CBI and SIA, Nov 2020", SIA]]),
            P("crossborder", "Cross-border payments", "SWIFT MT/MX and SEPA payments (ISK 1,000 per outgoing SWIFT message); 98.1% of corporate international payments are self-served.",
              s=["sme", "corp"], lc="move", neo=[0, ""], src=[["Price list, Jan 2025", PRICE], ["Annual report 2025: corporate banking", CORP]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: a fraud hotline that handled 1,465 cases in 2025, electronic ID and biometrics, the chatbot Ellí, Aukakrónur and the new Vild programme, card processing with Rapyd, and settlement APIs.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "1,465 cases in 2025.", "div": "lb", "rev": "personal", "products": [
            P("fraud", "Fraud hotline", "Opened November 2024 and staffed 9:00–23:00: 1,465 fraud cases in 2025, about 25% with a loss; customers aged 65 and over bore nearly 60% of losses; Messenger takeovers were the commonest scam, investment scams the costliest.",
              s=["con"], lc="everyday", o="B", neo=[0, "Landsbankinn's own."],
              mc="A clear need for scam scoring on transfers.",
              src=[["Annual report 2025: personal banking", PERS], ["2025 results presentation", FY25]]),
            P("auth", "Authentication", "Electronic ID, the Auðkenni app and biometrics for corporate online banking (RSA tokens retired in 2025); card notifications; online card codes sent by Valitor under Verified by Visa (2021).",
              s=["con", "corp"], lc="open", neo=[0, "Visa 3-D Secure."], src=[["Annual report 2025: continuous development", DEV], ["Landsbankinn: Visa verification, Nov 2021", VBV]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "Ellí & AI", "blurb": "95.6% answered.", "div": "lb", "rev": "personal", "products": [
            P("elli", "Ellí chatbot", "Helped 32,588 customers in 2025 with 81% thumbs-up and answered 95.6% of questions by year-end; now in the app and corporate online banking; AI use expanding in service and internal processes.",
              s=["con", "sme"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["Annual report 2025: continuous development", DEV], ["2025 results presentation", FY25]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty", "blurb": "Aukakrónur and Vild.", "div": "aukakronur", "rev": "personal", "products": [
            P("aukakronur", "Aukakrónur", "Card-linked rewards: about ISK 713 million collected and ISK 671 million spent in 2025 at more than 200 partner merchants (33 new); 1% back on TM premiums paid by linked card.",
              s=["con", "young"], lc="grow", o="B", neo=[0, "Rides Visa cards."],
              mc="Card-linked offers and merchant content could feed it.",
              src=[["Annual report 2025: personal banking", PERS], ["2025 results presentation", FY25]]),
            P("vild", "Vild", "A loyalty programme launched in early summer 2026 that rewards the scope and length of a customer's relationship with the bank.",
              s=["con"], lc="grow", st="new", ay="Summer 2026", o="B", neo=[0, ""], src=[["H1 2026 results", H1]]),
        ]},
        {"id": "3.4", "ic": "receipt-text", "name": "Card operations", "blurb": "Rapyd, self-service.", "div": "lb", "rev": "personal", "products": [
            P("cardproc", "Card processing", "Visa card bills issued by Rapyd Europe, formerly Valitor, since April 2023 ⚠ current processing contract not public; duplicate card postings corrected on 31 July 2026.",
              s=["con"], lc="everyday", o="P", at="Rapyd", neo=[0, "Visa processing."], src=[["Landsbankinn: Rapyd Europe, Apr 2023", RAPYD], ["Landsbankinn: double bookings, Jul 2026", DUP26]]),
            P("cardops", "Card self-service & disputes", "Order, block, replace and change debit and credit cards in the app (2025), with fees, insurance and benefits shown; about 5,600 chargebacks handled after the Play airline bankruptcy in 2025.",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["Annual report 2025: continuous development", DEV], ["Annual report 2025: personal banking", PERS]]),
        ]},
        {"id": "3.5", "ic": "code-xml", "name": "Data & APIs", "blurb": "Settlement by API.", "div": "lb", "rev": "corporate", "products": [
            P("apis", "Settlement & banking APIs", "Merchant settlement data booked by API straight into accounting systems and automatic links to the bank's accounting services ⚠ no 2025–26 detail on open banking.",
              s=["sme", "corp"], lc="open", o="B", neo=[None, "Nothing public."], src=[["Annual report 2025: corporate banking", CORP], ["Landsbankinn: acquiring", ACQ]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: 40.2% of the retail market, mortgages and car loans, about 40% of corporate lending, ISK 936 billion under management with Landsbréf, and TM insurance.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Personal banking", "blurb": "40.2% retail share.", "div": "lb", "rev": "personal", "products": [
            P("accounts", "Accounts", "131,200 active individual customers at end-2025 and a 40.2% retail market share; the first Icelandic bank with a Polish-zloty savings account (February 2025), with 24,000 users on a Polish interface.",
              s=["con"], lc="everyday", neo=[0, "Visa debit."], src=[["Annual report 2025: personal banking", PERS], ["Landsbankinn: Polish account, Feb 2025", POLISH]]),
            P("savings", "Smart Savings", "78,100 customers with app savings accounts (+23%, ISK 34.6 billion of growth in 2025); round-up saving from credit-card spending; app savings up 19.1% in H1 2026.",
              s=["con", "inv"], lc="grow", o="B", neo=[0, ""], src=[["Annual report 2025: personal banking", PERS], ["H1 2026 results", H1]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Mortgages & car loans", "blurb": "55% to first-time buyers.", "div": "lb", "rev": "personal", "products": [
            P("mortgages", "Mortgages", "A new offering on 24 October 2025, ten days after a Supreme Court ruling; about 85% of applications digital; about 55% of new H1 2026 mortgages went to first-time buyers, averaging about ISK 44 million.",
              s=["home"], lc="borrow", st="flux", neo=[0, ""], src=[["Annual report 2025: personal banking", PERS], ["H1 2026 results", H1]]),
            P("carloans", "Car & equipment finance", "Car lending of about ISK 14.6 billion in 2025, about 16% of it for electric vehicles; vehicle and equipment finance of ISK 44.4 billion.",
              s=["con", "sme"], lc="borrow", neo=[0, ""], src=[["Annual report 2025: personal banking", PERS], ["Annual report 2025: corporate banking", CORP]]),
        ]},
        {"id": "4.3", "ic": "factory", "name": "Corporate banking", "blurb": "About 40% of lending.", "div": "lb", "rev": "corporate", "products": [
            P("corporate", "Corporate lending", "About 40% of corporate lending in Iceland and around half in fisheries and construction; ISK 1,018 billion lent to companies at March 2026; about 2,000 new companies in 2025.",
              s=["corp", "sme"], lc="borrow", neo=[0, ""], src=[["Annual report 2025: corporate banking", CORP], ["Q1 2026 results", Q1]]),
            P("corpnb", "Corporate online banking", "A new platform from February 2025 with a shared workspace and batch payment approval; 83.1% of corporate credit-card applications self-served.",
              s=["sme", "corp"], lc="everyday", st="new", ay="Feb 2025", o="B", neo=[0, ""], src=[["Landsbankinn: corporate online banking, Feb 2025", CORPNB], ["Annual report 2025: corporate banking", CORP]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Markets & wealth", "blurb": "ISK 936bn managed.", "div": "landsbref", "rev": "am", "products": [
            P("landsbref", "Landsbréf & asset management", "ISK 936 billion under management at end-2025, 43 funds and a new ISK 15 billion private-equity fund, Horn V; 39,000 securities contracts.",
              s=["inv"], lc="grow", neo=[0, ""], src=[["2025 results presentation", FY25]]),
            P("cf", "Corporate Finance & funding", "Corporate Finance advised the state on the ISK 90.6 billion Íslandsbanki sale (May 2025); the bank issued two EUR 300 million green bonds in 2025 and an ISK 16 billion AT1 in 2026.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["Íslandsbanki sale, May 2025", ISB], ["Annual report 2025: main news", NEWS25], ["Q1 2026 results", Q1]]),
        ]},
        {"id": "4.5", "ic": "shield-check", "name": "TM insurance", "blurb": "Bought February 2025.", "div": "tm", "rev": "tm", "products": [
            P("tm", "TM tryggingar", "Non-life insurer bought in February 2025: combined ratio 89.9% in H1 2026; insurance sold through the bank's branches and app since Q1 2026, with demand above expectations.",
              s=["con", "sme"], lc="beyond", st="new", ay="Feb 2025", o="A", neo=[0, ""],
              mc="Premiums paid by card earn Aukakrónur.",
              src=[["H1 2026 results", H1], ["Q1 2026 results", Q1], ["Kvika: sale of TM finalised", TMDONE]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: an app used by 88% of retail customers, 34 branches and 84 ATMs, a contact centre, and partners from Icelandair to 200 Aukakrónur merchants.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "App & online banking", "blurb": "88% use the app.", "div": "lb", "rev": "personal", "products": [
            P("app", "Landsbankinn app", "Used by 88% of retail customers, about 70% of them only the app; 52.5 million log-ins in 2025; rated 4.8 out of 5; cards, savings, mortgages and TM insurance inside.",
              s=["con", "young"], lc="everyday", o="B", neo=[0, ""], src=[["2025 results presentation", FY25], ["Annual report 2025: continuous development", DEV]]),
            P("netbank", "Online banking", "More than 9 million online-banking log-ins and 13 million website visits in 2025; most companies bank online only.",
              s=["sme", "corp"], lc="everyday", o="B", neo=[0, ""], src=[["2025 results presentation", FY25]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & service", "blurb": "34 branches, 84 ATMs.", "div": "lb", "rev": "personal", "products": [
            P("branches", "Branches & ATMs", "34 branches and outlets, the largest network in Iceland, and 84 ATMs at 43 locations; 862,811 branch visits in 2025; TM and bank branches merged in four towns.",
              s=["con"], lc="everyday", st="flux", neo=[0, ""], src=[["Annual report 2025: personal banking", PERS], ["H1 2026 fact book", FB]]),
            P("contact", "Customer service centre", "251,482 calls, 104,755 emails and 22,459 online chats in 2025, alongside the fraud hotline.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["2025 results presentation", FY25]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "Icelandair, merchants.", "div": "lb", "rev": "personal", "products": [
            P("partners", "Partners", "Icelandair Saga Club on credit cards, more than 200 Aukakrónur merchants, Verifone for terminals, Rapyd for card processing and Yayland for prepaid cards.",
              s=["con", "sme"], lc="open", o="P", at="Icelandair, Verifone, Rapyd", neo=[0, ""], src=[["Icelandair: credit cards", SAGA], ["Annual report 2025: personal banking", PERS], ["Acquiring instructions", ACQI]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Landsbankinn", "blurb": "Accepted, not issued.", "products": [
        P("mcatlb", "Mastercard at Landsbankinn", "Every Landsbankinn card points to Visa: the price list margin on Visa's rate for all foreign card transactions, the Visa emergency line and Visa business artwork; Rapyd (formerly Valitor) produces the Visa bills. Separate Mastercard credit-card terms were dropped in March 2019. Mastercard's only visible role is acceptance in the bank's acquiring business (27% share); no joint initiative was found. Íslandsbanki's debit range is Mastercard.",
          s=["con"], div="lb", rev="other", mc="The relationship this map is drawn for.",
          src=[["Price list, Jan 2025", PRICE], ["Landsbankinn: acquiring instructions", ACQI], ["Aurbjörg: debit cards", AURB]]),
    ]},
    {"id": "pillar-market", "name": "Icelandic banking", "blurb": "Three banks and a home-grown rail.", "products": [
        P("market", "The Icelandic market", "Three large banks (Landsbankinn, Arion and Íslandsbanki, private since May 2025); more than 90% of retail payments run on Visa and Mastercard, and the Central Bank is building a domestic account-to-account option for resilience ⚠ launch not confirmed; 2024 law gave it payment-resilience powers; inflation 10.3% annualised in Q1 2026.",
          s=["con"], div="lb", rev="other", src=[["Bloomberg Law: Iceland payments plan, Jan 2025", BLOOM], ["Althingi: Central Bank Act amendment, 2024", ALTH], ["Q1 2026 results", Q1]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
