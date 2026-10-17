"""Royal Bank of Canada's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the Q3 2026 Report to Shareholders and release
(27 August 2026), the 2025 Annual Report and fiscal 2025 release (3 December 2025), RBC newsroom releases and
the RBC Royal Bank card pages as at 17 October 2026. Mastercard's Canadian newsroom could not be reached, so
items resting on it are marked ⚠. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own
product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

NEWS = "https://www.rbc.com/newsroom/news/article.html?article="
Q3R = "https://www.rbc.com/investor-relations/_assets-custom/pdf/2026q3_report.pdf"
Q3 = "https://www.newswire.ca/news-releases/royal-bank-of-canada-reports-third-quarter-2026-results-873288683.html"
FY25 = NEWS + "126055"
AR25 = "https://www.rbc.com/investor-relations/_assets-custom/pdf/ar_2025_e.pdf"
CARDPROD = "https://www.rbcroyalbank.com/onlinebanking/rates/cardprod.html"
ALLCARDS = "https://www.rbcroyalbank.com/credit-cards/all-credit-cards.html"
BIZCARDS = "https://www.rbcroyalbank.com/business/credit-cards/index.html"
VVD = "https://www.rbcroyalbank.com/banking-services/virtual-visa-debit/index.html"
RBCBANK = "https://www.rbcbank.com/"
CNB = "https://www.cnb.com/personal-banking/credit-cards.html"
CARIB = "https://www.rbcroyalbank.com/caribbean/tt/everyday-banking/debit-cards/visa-debit-classic.html"
HSBCMAP = "https://hardbacon.ca/en/credit-cards/hsbc-rewards-mastercard-review"
HSBCMAP2 = "https://milesopedia.com/en/?p=341049"
HSBCDEAL = "https://milesopedia.com/en/?p=241732"
INVDAY = "https://fidelity.com/news/article/default/202503271053RTRSNEWSCOMBINED_L3N3QA15B_1"
RTR = "https://www.payments.ca/systems-services/payment-systems/real-time-rail-payment-system"
OPENBANK = "https://www.canada.ca/en/department-finance/programs/financial-sector-policy/open-banking-implementation/budget-2025-canadas-framework-for-consumer-driven-banking.html"
INTERAC = "https://www.interac.ca/en/about/our-company/"
MCFORUM = "https://www.mastercard.com/ca/en/news-and-trends/press/2026/april/forward-together-defining-the-next-chapter-of-canada-innovation-economy.html"
MCSME = "https://www.mastercard.com/ca/en/business/industry-segment/small-medium-business/sme-payment-solutions/search-by-bank-commercial.html"
WESTJET09 = "https://westjet.mediaroom.com/news-releases?item=350"
SHOPPERSEND = "https://ratehub.ca/blog/rbc-shoppers-drug-mart-end-partnership"

HSBC = NEWS + "125885"
EXECS24 = NEWS + "125922"
CFO = NEWS + "125939"
AIGROUP = NEWS + "126074"
EVIDENT = NEWS + "126160"
IDC = NEWS + "126132"
COHERE = NEWS + "125967"
QUANTUM = NEWS + "126155"
VANCOUVER = NEWS + "126106"
PINCH = NEWS + "126084"
RBCX = NEWS + "126145"
MONERIS = NEWS + "126130"
GTB = NEWS + "126136"
CADTOK = NEWS + "126151"
IMT = NEWS + "126157"
WJREFRESH = NEWS + "126031"
WJBIZ = NEWS + "126021"
AMPLI = NEWS + "123906"
SHOPPERS = NEWS + "122796"
ION = NEWS + "125730"
MORE = NEWS + "125976"
MORE2 = NEWS + "126008"
METRO = NEWS + "125947"
CTC = NEWS + "126062"
DOORDASH = NEWS + "126051"
PETRO = NEWS + "122554"
AVION22 = NEWS + "125726"
AVIONOPEN = NEWS + "125816"
AVIONSELECT = NEWS + "125879"
AVIONAWARD = NEWS + "126098"
AVIONTRAVEL = NEWS + "126147"
HOPPER = NEWS + "126088"
LIVENATION = NEWS + "126115"
VISAINST = NEWS + "125747"
PAYPLAN = NEWS + "125398"
IKEA = NEWS + "125903"
WALLET = NEWS + "122693"
HCE = NEWS + "122658"
APPLEPAY = NEWS + "124027"
CCLOCK = NEWS + "122536"
DCLOCK = NEWS + "122518"
VVD13 = NEWS + "122708"
ETBIZ = NEWS + "125479"
BULKRM = NEWS + "125232"
PAYEDGE = NEWS + "125837"
TRREB = NEWS + "125898"
CLEAR = NEWS + "125890"
NEWCOMER = NEWS + "126146"
NOVA = NEWS + "125916"
JDPOWER = NEWS + "126042"
EUROPE = NEWS + "126121"
Q2 = NEWS + "126103"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · charter · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: C$2.5 trillion of assets, Canada's largest bank by market value, an AI Group reporting to the CEO, and HSBC Canada folded in since 2024.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "C$2.5tn; ROE 17.9%.", "div": "group", "rev": "pb", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of C$2,498.8 billion, loans of C$1,108.7 billion and deposits of C$1,644.6 billion at 31 July 2026. Q3 2026 net income was a record C$6.0 billion, up 11%; ROE 17.9%; CET1 13.5%. Fiscal 2025 net income C$20.4 billion. Market value C$406 billion on the TSX at 31 July 2026.",
              s=["inv"], neo=[0, ""], src=[["Q3 2026 Report to Shareholders", Q3R], ["Q3 2026 results release", Q3], ["Fiscal 2025 results", FY25]]),
        ]},
        {"id": "1.2", "ic": "badge-check", "name": "Charter & leadership", "blurb": "Since 1864; 19m+ clients.", "div": "group", "rev": "pb", "products": [
            P("heritage", "Charter, listing & ratings", "Royal Bank of Canada, founded 1864, listed on the TSX and NYSE (RY). More than 19 million clients in Canada, the US and 27 other countries, and 105,000+ employees. Legacy senior debt rated Aa1, AA-, AA and AA (high), all stable (December 2025).",
              s=["inv"], o="I", neo=[0, ""], src=[["Q3 2026 Report to Shareholders", Q3R], ["Annual Report 2025", AR25], ["RBC: HSBC Canada closes, Mar 2024", HSBC]]),
            P("leadership", "Group Executive", "CEO Dave McKay; CFO Katherine Gibson (from 2024); chair Jacynthe Côté. Group heads Erica Nielsen (Personal Banking), Sean Amato-Gauci (Commercial Banking), Neil McLaughlin (Wealth), Jennifer Publicover (Insurance), Derek Neldner (Capital Markets), Bruce Ross (AI) and Naim Kazmi (Technology & Operations). Vinita Savani runs Cards & Loyalty.",
              s=["inv"], neo=[0, ""], src=[["Annual Report 2025", AR25], ["RBC: CFO appointed, Sep 2024", CFO], ["RBC: AI Group, Feb 2026", AIGROUP], ["RBC: executive changes, Jul 2024", EXECS24]]),
        ]},
        {"id": "1.3", "ic": "brain", "name": "AI & technology", "blurb": "#3 globally for AI.", "div": "group", "rev": "cm", "products": [
            P("aigroup", "AI Group & the C$1bn AI target", "An AI Group under Bruce Ross, reporting to the CEO, from February 2026, chasing C$700 million to C$1 billion of enterprise value from AI by 2027. RBC is #1 in Canada and #3 globally in the Evident AI Index (October 2026). Quantum programme with a new director (September 2026).",
              s=["corp"], st="new", ay="Feb 2026", o="B", neo=[0, ""], src=[["RBC: AI Group, Feb 2026", AIGROUP], ["RBC: Evident AI Index, Oct 2026", EVIDENT], ["RBC: quantum strategy, Sep 2026", QUANTUM]]),
            P("atom", "ATOM, Aiden & RBC Assist", "ATOM, RBC's own foundation model for financial services, drives credit decisions and Avion personalisation. Aiden serves all 8,000 Capital Markets staff; more than 72,000 employees use RBC Assist or Aiden. Cohere co-develops North for Banking (January 2025).",
              s=["corp"], o="B", neo=[0, ""], src=[["Annual Report 2025", AR25], ["RBC: Evident AI Index, Oct 2026", EVIDENT], ["RBC and Cohere, Jan 2025", COHERE]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & portfolio", "blurb": "ROE 17%+; HSBC Canada in.", "div": "group", "rev": "pb", "products": [
            P("strategy", "Investor Day & ROE objective", "Investor Day on 27 March 2025 set a 16%+ ROE target and the AI value goal; the fiscal 2026 ROE objective was raised to 17%+ in December 2025. Reported unit targets, such as 2.4 million net new Personal Banking clients over five years, are secondary-sourced ⚠.",
              s=["inv"], neo=[0, ""], src=[["Fiscal 2025 results", FY25], ["Reuters via Fidelity: Investor Day, Mar 2025 ⚠", INVDAY]]),
            P("hsbc", "HSBC Canada integration", "Acquisition closed 28 March 2024 (about C$13.5 billion ⚠), adding 4,500 staff and 780,000 clients; branches reopened as RBC on 1 April 2024. HSBC Canada's Mastercard credit cards were reissued as RBC cards, most of them Visa ⚠.",
              s=["con", "new"], o="A", ay="Mar 2024", at="HSBC", neo=[0, "HSBC's Mastercard cards moved mostly to Visa ⚠."],
              mc="A Mastercard card book that moved mostly to Visa ⚠.", src=[["RBC: HSBC Canada closes, Mar 2024", HSBC], ["Hardbacon: HSBC card mapping ⚠", HSBCMAP], ["Milesopedia: the transaction ⚠", HSBCDEAL]]),
            P("deals", "Deals 2025–26", "Pinch Financial, a digital mortgage-qualification fintech (March 2026); a unified Global Transaction Banking business (August 2026); the C$1.4 billion RBCx Growth Fund initiative (September 2026); and the agreed sale of Moneris (see Acquiring).",
              s=["corp"], st="new", neo=[0, ""], src=[["RBC: Pinch Financial, Mar 2026", PINCH], ["RBC: Global Transaction Banking, Aug 2026", GTB], ["RBC: RBCx Growth Fund, Sep 2026", RBCX]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: Avion and most cards on Visa, WestJet and cash back cards on Mastercard, commercial cards on Visa, Interac debit with a Virtual Visa Debit, e-Transfer and transfers abroad, Visa cards in the US, a CAD deposit token, and Moneris, now for sale.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Visa credit cards", "blurb": "Avion, ION, grocery co-brands.", "div": "royal", "rev": "pb", "products": [
            P("avion", "RBC Avion Visa cards", "Avion Visa Infinite, Avion Visa Infinite Privilege and Avion Visa Platinum, the travel flagship, plus the British Airways Visa Infinite. Fixed-points flights on any airline. Avion Concierge launched for Private Banking cardholders in 2025.", short="Avion (Visa)",
              s=["card"], lc="borrow", o="B", neo=[0, "Visa."],
              mc="The flagship line, on Visa.", src=[["RBC: all credit cards", ALLCARDS], ["RBC: card rates, 17 Oct 2026", CARDPROD], ["Annual Report 2025", AR25]]),
            P("ion", "RBC ION & ION+ Visa", "Everyday cards launched September 2022: ION earns 1.5 Avion points per dollar and ION+ 3 points in grocery, dining, transit, gas, EV charging and streaming. Also the RBC Visa Platinum and Visa Classic Low Rate Option.", short="ION (Visa)",
              s=["card", "new"], lc="borrow", ay="Sep 2022", o="B", neo=[0, "Visa."], src=[["RBC: ION and ION+ Visa, Sep 2022", ION], ["RBC: all credit cards", ALLCARDS]]),
            P("groceryco", "moi RBC Visa & More Rewards RBC Visa", "Grocery co-brands: moi RBC Visa with Metro, and More Rewards RBC Visa and Visa Infinite with Pattison Food Group in Western Canada (February 2025).", short="Grocery co-brands (Visa)",
              s=["card"], lc="borrow", ay="Feb 2025", o="P", at="Metro, Pattison Food Group", neo=[0, "Visa."], src=[["RBC and Pattison: More Rewards Visa, Feb 2025", MORE], ["METRO and RBC: Moi Rewards, Oct 2024", METRO]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Mastercard credit cards", "blurb": "WestJet and cash back.", "div": "royal", "rev": "pb", "products": [
            P("westjet", "WestJet RBC Mastercard cards", "The WestJet RBC World Elite Mastercard and WestJet RBC Mastercard, on Mastercard since about 2009 ⚠. Refreshed from 5 November 2025: 2 WestJet points per dollar on WestJet, Sunwing, grocery, gas, EV charging and transit on the World Elite card.", short="WestJet (Mastercard)",
              s=["card"], lc="borrow", st="new", ay="Nov 2025", o="P", at="WestJet", neo=[2, "Mastercard."],
              mc="RBC's largest Mastercard programme and its co-brand anchor.", src=[["RBC and WestJet: card refresh, Sep 2025", WJREFRESH], ["RBC and WestJet: Ampli, Jun 2018", AMPLI], ["WestJet news releases ⚠", WESTJET09]]),
            P("cashback", "RBC Cash Back Mastercard cards", "The no-fee RBC Cash Back Mastercard and the RBC Cash Back Preferred World Elite Mastercard. The line descends from the RBC Shoppers Optimum MasterCard of 2012, whose portfolio RBC bought ⚠; HSBC's Cash Rewards Mastercard holders moved to it in 2024 ⚠.", short="Cash Back (Mastercard)",
              s=["card", "new"], lc="borrow", o="I", neo=[2, "Mastercard."], src=[["RBC: card rates, 17 Oct 2026", CARDPROD], ["RBC and Shoppers: Optimum MasterCard, Sep 2012", SHOPPERS], ["Ratehub: Shoppers partnership ends ⚠", SHOPPERSEND], ["Hardbacon: HSBC card mapping ⚠", HSBCMAP]]),
        ]},
        {"id": "2.3", "ic": "briefcase", "name": "Business & commercial cards", "blurb": "Visa, with two Mastercards.", "div": "royal", "rev": "cb", "products": [
            P("westjetbiz", "WestJet RBC World Elite Mastercard for Business", "Launched 14 August 2025: Canada's first business travel card with instant airline status (WestJet Silver), up to 6 points per dollar on WestJet; RBC's only business travel Mastercard.", short="WestJet Business (Mastercard)",
              s=["sme"], lc="borrow", st="new", ay="Aug 2025", o="P", at="WestJet", neo=[2, "Mastercard."],
              mc="The newest Mastercard launch at RBC.", src=[["WestJet and RBC: business card, Aug 2025", WJBIZ]]),
            P("bizcards", "Small-business cards", "Avion Visa Infinite Business, Avion Visa Business, RBC Visa Business and Visa CreditLine for Small Business, beside the RBC Business Cash Back Mastercard. Mastercard Canada lists RBC among its small-business card issuers ⚠.", short="Business cards (mostly Visa)",
              s=["sme"], lc="borrow", o="B", neo=[1, "Mostly Visa; Business Cash Back Mastercard."], src=[["RBC: business credit cards", BIZCARDS], ["Mastercard Canada: commercial card issuers ⚠", MCSME]]),
            P("commercial", "RBC commercial cards", "Commercial Avion Visa, Commercial Cash Back Visa, Commercial Visa and Commercial U.S. Dollar Visa for larger companies. All commercial cards are Visa.", short="Commercial cards (Visa)",
              s=["corp"], lc="move", o="B", neo=[0, "Visa."],
              mc="Commercial cards are all Visa.", src=[["RBC: card rates, 17 Oct 2026", CARDPROD], ["RBC: business credit cards", BIZCARDS]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Debit", "blurb": "Interac and Virtual Visa Debit.", "div": "royal", "rev": "pb", "products": [
            P("interacdebit", "RBC Client Card (Interac Debit)", "The RBC debit card runs on Interac at stores, ATMs and online. Interac has handled more than 6.5 billion debit transactions ⚠ period not stated.", short="Interac Debit",
              s=["con"], lc="everyday", o="P", at="Interac", neo=[0, "Interac."], src=[["RBC: Virtual Visa Debit", VVD], ["Interac: our company", INTERAC]]),
            P("vvd", "RBC Virtual Visa Debit", "A separate Visa debit number on the client's account for online, in-app, recurring and foreign wallet payments, activated in the RBC Mobile app; offered since at least October 2013. No Debit Mastercard found.", short="Virtual Visa Debit",
              s=["con", "new"], lc="everyday", ay="Oct 2013", o="P", at="Visa", neo=[0, "Visa."],
              mc="Online and cross-border debit went to Visa.", src=[["RBC: Virtual Visa Debit", VVD], ["RBC: Virtual Visa Debit card, Oct 2013", VVD13]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Real-time & cross-border", "blurb": "e-Transfer; transfers abroad.", "div": "gtb", "rev": "cb", "products": [
            P("etransfer", "Interac e-Transfer", "Person-to-person transfers for personal clients. Payments Canada's Real-Time Rail launches in Q4 2026 and is in industry testing.",
              s=["con"], lc="move", o="P", at="Interac", neo=[0, "Interac."], src=[["Interac: our company", INTERAC], ["Payments Canada: Real-Time Rail", RTR]]),
            P("etbiz", "Interac e-Transfer for Business", "Real-time, data-rich business payments from August 2021, after RBC became the first Canadian bank with e-Transfer Bulk Request Money (February 2020).",
              s=["sme", "corp"], lc="move", ay="Aug 2021", o="P", at="Interac", neo=[0, "Interac."], src=[["RBC: e-Transfer for Business, Aug 2021", ETBIZ], ["RBC: Bulk Request Money, Feb 2020", BULKRM]]),
            P("imt", "International Money Transfers", "No-fee transfers abroad in USD (early 2026) and from EUR, GBP and HKD accounts (1 October 2026), up to C$50,000 a day, in the app and online. The network or provider behind it is not stated ⚠.",
              s=["new", "con"], lc="move", st="new", ay="Oct 2026", o="B", neo=[None, "Provider not stated ⚠."],
              mc="Remittances and newcomers: where Mastercard Move would fit.", src=[["RBC: International Money Transfers, Oct 2026", IMT]]),
        ]},
        {"id": "2.6", "ic": "flag", "name": "U.S. & Caribbean cards", "blurb": "Visa in both.", "div": "us", "rev": "pb", "products": [
            P("uscards", "RBC Bank & City National cards", "RBC Bank (Georgia) offers cross-border banking in all 50 states and the RBC Bank U.S. Visa Signature Black, earning Avion points. City National issues Crystal Visa Infinite and Visa Signature cards.", short="US cards (Visa)",
              s=["us"], lc="borrow", o="B", neo=[0, "Visa."], src=[["RBC Bank (US)", RBCBANK], ["City National: credit cards", CNB]]),
            P("caribdebit", "RBC Royal Bank Caribbean debit", "Visa Debit cards in the Caribbean ⚠. Caribbean credit-card networks were not checked ⚠.",
              s=["us"], lc="everyday", st="unconf", neo=[0, "Visa ⚠."], src=[["RBC Caribbean: Visa Debit ⚠", CARIB]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Digital money", "blurb": "A CAD deposit token.", "div": "cm", "rev": "cm", "products": [
            P("cadtoken", "CAD tokenised deposits", "One of six Canadian banks (with BMO, CIBC, National Bank, Scotiabank and TD) exploring a Canadian-dollar tokenised deposit, announced 22 September 2026. Phase one moves tokens between Canadian institutions.",
              s=["corp"], lc="move", st="new", ay="Sep 2026", o="P", at="Five Canadian banks", neo=[0, "Mastercard not named."],
              mc="A bank-led token that could move flows off card rails.", src=[["RBC: CAD tokenised deposits, Sep 2026", CADTOK]]),
        ]},
        {"id": "2.8", "ic": "store", "name": "Acquiring", "blurb": "Moneris, being sold.", "div": "moneris", "rev": "cb", "products": [
            P("moneris", "Moneris", "RBC's 50/50 joint venture with BMO, serving over 325,000 points of commerce, agreed to be sold to Francisco Partners for about C$2 billion (10 August 2026). Closing by the end of Q1 fiscal 2027, with a C$475 million after-tax gain to RBC and new exclusive, long-term referral arrangements.",
              s=["sme"], lc="move", st="flux", o="P", at="BMO, Francisco Partners", neo=[1, "Accepts every network."], src=[["RBC: sale of Moneris, Aug 2026", MONERIS], ["Q3 2026 Report to Shareholders", Q3R]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card and account: Avion Rewards, linked-card offers with big Canadian retailers, wallets and RBC's own tokens, instalments from Visa and PayPlan, and card controls and AI credit.",
    "tiles": [
        {"id": "3.1", "ic": "gift", "name": "Avion Rewards", "blurb": "Global loyalty programme of 2026.", "div": "avion", "rev": "pb", "products": [
            P("avionrewards", "Avion Rewards", "Canada's largest proprietary loyalty programme, relaunched from RBC Rewards in September 2022, open to all Canadians since August 2023 with offers from 2,400+ retailers, and named International Loyalty Program of the Year – Global in May 2026. Points redeem on Ticketmaster since June 2026. Member count not disclosed ⚠.",
              s=["card", "con"], lc="grow", o="B", neo=[0, "RBC's own; earns on Visa and Mastercard cards."],
              mc="RBC's own engine; offers and data services could feed it.", src=[["RBC: Avion Rewards launch, Sep 2022", AVION22], ["RBC: Avion open to all, Aug 2023", AVIONOPEN], ["RBC: Avion award, May 2026", AVIONAWARD], ["RBC and Live Nation, Jun 2026", LIVENATION]]),
            P("aviontravel", "Avion Rewards Travel", "A booking platform on HTS (Hopper Technology Solutions), launched 14 September 2026: 500+ airlines, AI price prediction and fare alerts, pay with points, card or both.",
              s=["card"], lc="beyond", st="new", ay="Sep 2026", o="P", at="HTS (Hopper)", neo=[0, ""], src=[["RBC: Avion Rewards Travel, Sep 2026", AVIONTRAVEL], ["RBC and HTS, Mar 2026", HOPPER]]),
        ]},
        {"id": "3.2", "ic": "sparkles", "name": "Linked-card offers", "blurb": "Petro-Canada to Canadian Tire.", "div": "avion", "rev": "pb", "products": [
            P("linked", "Linked-card partnerships", "Any eligible RBC credit or debit card can be linked to partner loyalty: Petro-Canada (October 2017), Metro Moi (October 2024), Pattison More Rewards (2x points, June 2025) and Canadian Tire Triangle Rewards (3x CT Money, January 2026; nearly 12 million Triangle members).",
              s=["card", "con"], lc="grow", o="P", at="Petro-Canada, Metro, Pattison, Canadian Tire", neo=[1, "Runs on any RBC card, Mastercard ones included."], src=[["RBC and Canadian Tire, Jan 2026", CTC], ["RBC and Pattison, Jun 2025", MORE2], ["RBC and Petro-Canada, Oct 2017", PETRO], ["METRO and RBC, Oct 2024", METRO]]),
            P("doordash", "DashPass for cardholders", "Extended November 2025: 12 months of DashPass for Avion credit cards and the WestJet RBC World Elite Mastercard, six months for other RBC cards, two months for Avion members without an RBC product.",
              s=["card"], lc="beyond", st="new", ay="Nov 2025", o="P", at="DoorDash", neo=[1, "Avion Visa and WestJet World Elite Mastercard alike."], src=[["RBC and DoorDash, Nov 2025", DOORDASH]]),
        ]},
        {"id": "3.3", "ic": "wallet", "name": "Wallets & tokens", "blurb": "Secure Cloud, HCE, Apple Pay.", "div": "royal", "rev": "pb", "products": [
            P("wallets", "RBC Wallet, Secure Cloud & Apple Pay", "RBC Wallet on RBC Secure Cloud (January 2014, Interac Debit and Visa credit), the first host card emulation by a North American bank (December 2014), and Apple Pay for RBC debit and credit cards (May 2016). The token service used for Mastercard cards is not named ⚠.",
              s=["con", "card"], lc="everyday", o="B", neo=[1, "Mastercard cards in Apple Pay; token service not named ⚠."],
              mc="RBC built its own tokens early; Click to Pay and Agent Pay would sit here.", src=[["RBC: RBC Wallet, Jan 2014", WALLET], ["RBC: host card emulation, Dec 2014", HCE], ["RBC: Apple Pay, May 2016", APPLEPAY]]),
        ]},
        {"id": "3.4", "ic": "receipt-text", "name": "Instalments", "blurb": "Visa Installments, PayPlan.", "div": "royal", "rev": "pb", "products": [
            P("visainst", "Installments enabled by Visa", "From November 2022, eligible RBC personal Visa cardholders can split qualifying purchases at participating merchants. Mastercard Installments not found.",
              s=["card"], lc="borrow", ay="Nov 2022", o="P", at="Visa Canada", neo=[0, "Visa."], src=[["Visa Canada and RBC: instalments, Nov 2022", VISAINST]]),
            P("payplan", "PayPlan by RBC", "Point-of-sale financing on Bread's platform (launched 2020, announced January 2021), in IKEA Canada stores from May 2024 at rates as low as 0%.",
              s=["con"], lc="borrow", o="P", at="Bread, IKEA Canada", neo=[0, "Not card-based."], src=[["RBC and Bread: PayPlan, Jan 2021", PAYPLAN], ["IKEA Canada and RBC, May 2024", IKEA]]),
        ]},
        {"id": "3.5", "ic": "shield-check", "name": "Controls & AI credit", "blurb": "Card locks, AI underwriting.", "div": "royal", "rev": "pb", "products": [
            P("controls", "Card controls", "Credit card lock in the RBC Mobile app (June 2018) and debit card lock, a Canadian first (April 2019).",
              s=["con", "card"], lc="everyday", o="B", neo=[0, "RBC's own."], src=[["RBC: credit card controls, Jun 2018", CCLOCK], ["RBC: debit card lock, Apr 2019", DCLOCK]]),
            P("aicredit", "AI credit underwriting", "AI-assisted retail underwriting (IDC CIO award, August 2026); machine learning gives about 40% more credit-limit increases to people with under two years of credit history, close to C$300 million of extra credit.",
              s=["new", "con"], lc="borrow", st="new", o="B", neo=[0, ""], src=[["RBC: IDC CIO award, Aug 2026", IDC], ["RBC: Evident AI Index, Oct 2026", EVIDENT]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What clients buy, by reported segment: Personal Banking, Commercial Banking with Global Transaction Banking, Wealth Management and Insurance, and Capital Markets.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Personal Banking", "blurb": "15m clients; C$197bn card spend.", "div": "royal", "rev": "pb", "products": [
            P("personal", "Personal Banking", "About 15 million clients in Canada and #1 market share in all key retail products. Fiscal 2025: net income C$7.1 billion, credit card purchase volumes C$196.6 billion, average card balances C$25.2 billion. Q3 2026 net income C$1.9 billion. Includes Caribbean & U.S. Banking.",
              s=["con", "card"], lc="everyday", neo=[1, "Cards mostly Visa; WestJet and cash back on Mastercard."], src=[["Annual Report 2025", AR25], ["Q3 2026 Report to Shareholders", Q3R]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Commercial Banking & GTB", "blurb": "1.4m clients; GTB.", "div": "gtb", "rev": "cb", "products": [
            P("gtb", "Commercial Banking & Global Transaction Banking", "About 1.4 million clients and #1 in commercial lending and deposits. Global Transaction Banking became one business in August 2026, co-led by Sean Amato-Gauci and Derek Neldner, with RBC Edge in Canada and RBC Clear in the US (April 2024). Q3 2026 net income C$936 million.",
              s=["corp", "sme"], lc="move", st="new", ay="Aug 2026", o="B", neo=[0, ""], src=[["RBC: Global Transaction Banking, Aug 2026", GTB], ["RBC: RBC Clear, Apr 2024", CLEAR], ["Annual Report 2025", AR25]]),
            P("payedge", "RBC PayEdge", "An accounts-payable platform that pays suppliers from any Canadian bank account, integrated with Xero (October 2023) and used by the Toronto Regional Real Estate Board (May 2024).",
              s=["sme", "corp"], lc="move", o="B", neo=[0, ""], src=[["RBC and Xero, Oct 2023", PAYEDGE], ["RBC and TRREB, May 2024", TRREB]]),
        ]},
        {"id": "4.3", "ic": "trending-up", "name": "Wealth & insurance", "blurb": "C$6.2tn AUA.", "div": "wealth", "rev": "wm", "products": [
            P("wealth", "RBC Wealth Management", "RBC Dominion Securities, RBC Direct Investing, RBC Global Asset Management, RBC Brewin Dolphin in the UK and RBC Investor Services. Group AUA C$6.2 trillion; Wealth net income C$1.4 billion in Q3 2026, up 32%. New co-CEOs for RBC Europe (July 2026).",
              s=["inv"], lc="grow", neo=[0, ""], src=[["Q3 2026 Report to Shareholders", Q3R], ["RBC: Europe co-CEOs, Jul 2026", EUROPE]]),
            P("citynational", "City National Bank", "RBC's US bank for businesses and wealthy clients, reported in U.S. Wealth Management; its cards are Visa.",
              s=["us", "inv"], lc="grow", o="A", neo=[0, "Visa."], src=[["Q3 2026 Report to Shareholders", Q3R], ["City National: credit cards", CNB]]),
            P("insurance", "RBC Insurance", "Life, health, travel and creditor insurance for about 4.9 million clients; Canada's largest bank-owned life insurer. Q3 2026 net income C$197 million.",
              s=["inv", "con"], lc="beyond", neo=[0, ""], src=[["Annual Report 2025", AR25], ["Q3 2026 Report to Shareholders", Q3R]]),
        ]},
        {"id": "4.4", "ic": "chart-candlestick", "name": "Capital Markets", "blurb": "#1 investment bank in Canada.", "div": "cm", "rev": "cm", "products": [
            P("capmkts", "RBC Capital Markets", "Canada's #1 investment bank by market share, with 22,900+ clients. Q3 2026 net income C$1.5 billion, up 16%; fiscal 2025 C$5.4 billion.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["Annual Report 2025", AR25], ["Q3 2026 results release", Q3]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How clients reach RBC: the RBC Mobile app and MyAdvisor, a self-serve account for newcomers before they arrive, 1,249 branches, and partners from WestJet to Live Nation.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Digital banking", "blurb": "App, MyAdvisor, newcomers.", "div": "royal", "rev": "pb", "products": [
            P("app", "RBC Mobile app & Online Banking", "Mortgage renewal, GICs, TFSAs and RRSPs opened in the app; J.D. Power's highest customer satisfaction among the Big Five banks for the second straight year (October 2025).",
              s=["con", "card"], lc="everyday", o="B", neo=[0, ""], src=[["Annual Report 2025", AR25], ["RBC: J.D. Power ranking, Oct 2025", JDPOWER]]),
            P("myadvisor", "MyAdvisor", "RBC's digital advice platform, which has connected more than 5.1 million Canadians to a personal plan.",
              s=["inv", "con"], lc="grow", o="B", neo=[0, ""], src=[["Annual Report 2025", AR25]]),
            P("newcomer", "Pre-Arrival Account Open", "A 15-minute self-serve account opening for newcomers from Hong Kong, China, India and six other countries, with transfers of up to C$75,000 before arrival (September 2026); credit history imported through Nova Credit (June 2024).",
              s=["new"], lc="open", st="new", ay="Sep 2026", o="B", neo=[0, ""], src=[["RBC: Pre-Arrival Account Open, Sep 2026", NEWCOMER], ["RBC: Global Credit Connect, Jun 2024", NOVA]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ATMs", "blurb": "1,249 branches.", "div": "royal", "rev": "pb", "products": [
            P("branches", "Branches & ATMs", "1,249 branches and 4,097 ATMs at 31 July 2026, the largest network in Canada; HSBC Canada's branches reopened as RBC on 1 April 2024.",
              s=["con", "sme"], lc="open", neo=[0, ""], src=[["Q3 2026 Report to Shareholders", Q3R], ["RBC: HSBC Canada closes, Mar 2024", HSBC]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners & ventures", "blurb": "WestJet, Live Nation, RBCx.", "div": "group", "rev": "pb", "products": [
            P("partners", "Brand partners", "WestJet (co-brand cards on Mastercard), Live Nation Canada (RBC Amphitheatre and Ticketmaster redemption), IKEA Canada (PayPlan), and the grocery, fuel and retail partners in Avion Rewards.",
              s=["card", "con"], lc="beyond", o="P", at="WestJet, Live Nation, IKEA", neo=[1, "WestJet cards are Mastercard."], src=[["RBC and WestJet: card refresh, Sep 2025", WJREFRESH], ["RBC and Live Nation, Jun 2026", LIVENATION], ["IKEA Canada and RBC, May 2024", IKEA]]),
            P("rbcx", "RBCx ventures", "Ownr (239,000+ businesses registered), Mydoh for families (320,000+ Canadians) and Dr.Bill, plus the RBCx Growth Fund I (September 2026).",
              s=["sme", "con"], lc="beyond", o="B", neo=[0, ""], src=[["Annual Report 2025", AR25], ["RBC: RBCx Growth Fund, Sep 2026", RBCX]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at RBC", "blurb": "WestJet and cash back; Visa elsewhere.", "products": [
        P("mcatrbc", "Mastercard at RBC", "Mastercard carries the WestJet RBC cards (personal, and business since August 2025), the RBC Cash Back cards and the Business Cash Back card. Visa carries Avion, ION, the grocery co-brands, all commercial cards, Virtual Visa Debit and the US cards; Interac runs debit. Most HSBC Canada Mastercard holders were moved to Visa in 2024 ⚠. Dave McKay and Michael Miebach shared a stage at Mastercard's Canadian forum in April 2026 ⚠. No network agreement or renewal date is public.",
          s=["card"], div="group", rev="pb", mc="The relationship this map is drawn for.",
          src=[["RBC: card rates, 17 Oct 2026", CARDPROD], ["WestJet and RBC: business card, Aug 2025", WJBIZ], ["Hardbacon: HSBC card mapping ⚠", HSBCMAP2], ["Mastercard Canada: innovation forum, Apr 2026 ⚠", MCFORUM]]),
    ]},
    {"id": "pillar-market", "name": "Canadian banking", "blurb": "RTR, open banking, tokens.", "products": [
        P("market", "The Canadian market", "Payments Canada's Real-Time Rail launches in Q4 2026. Consumer-driven banking is legislated through Budget 2025, with the Bank of Canada overseeing it; read access comes first and payments later (November 2025). Six big banks are exploring a CAD deposit token. Card network shares in Canada were not found ⚠.",
          s=["con"], div="group", rev="pb", src=[["Payments Canada: Real-Time Rail", RTR], ["Finance Canada: consumer-driven banking", OPENBANK], ["RBC: CAD tokenised deposits, Sep 2026", CADTOK]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
