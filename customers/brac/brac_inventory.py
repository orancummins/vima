"""BRAC Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the H1 2026 earnings disclosure (13 August 2026)
and the 2025 annual report (updated 9 July 2026). ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://brackweb.s3.ap-southeast-1.amazonaws.com/uploads/all/Earnings_Disclosure_-_H1%27266a8407af17196.pdf"
AR25 = "https://brackweb.s3.ap-southeast-1.amazonaws.com/uploads/all/BRAC_Bank_AR_2025_Final_Version_updated_on_09.07.2026_compressed6a549062be056.pdf"
FEH1 = "https://thefinancialexpress.com.bd/bangladesh/brac-bank-reports-stellar-performance-in-h1-2026"
TBS25 = "https://www.tbsnews.net/node/1448196"
CARDS = "https://www.bracbank.com/retail/card"
SMECARDS = "https://www.bracbank.com/sme/card"
ASTHA = "https://www.bracbank.com/digital-service/astha"
MCDEBIT = "https://www.thedailystar.net/business/banking/news/brac-bank-launches-platinum-multicurrency-debit-card-mastercard-4042621"
MCWORLD = "https://www.thedailystar.net/business/economy/banks/news/mastercard-brac-bank-launch-world-credit-card-3352636"
TARAW = "https://www.tbsnews.net/node/299551"
MILL = "https://www.tbsnews.net/node/320143"
VISA19 = "https://en.prothomalo.com/corporate/BRAC-Bank-launches-four-new-VISA-credit-cards"
VDIRECT = "https://www.thedailystar.net/business/banking/news/brac-bank-visa-partnership-launch-visa-direct-account-remittances-3928561"
VSME = "https://www.thedailystar.net/news/brac-bank-launches-multicurrency-sme-business-debit-credit-cards-4088071"
GPAY = "https://www.tbsnews.net/node/1356556"
JUBILEE = "https://www.tbsnews.net/economy/corporates/brac-bank-honours-25-institutions-silver-jubilee-1481356"
REMIT = "https://www.thedailystar.net/business/news/brac-bank-expands-global-remittance-network-new-partners-3838206"
BKMOVE = "https://thefinancialexpress.com.bd/trade/bkash-teams-up-with-mastercard-to-enable-faster-easier-remittance-access-across-bangladesh"
BKSEND = "https://nextbillion.net/news/mastercard-drives-new-p2p-solution-in-bangladesh/"
BKDB = "https://bdnews24.com/bangladesh/ghov62tiaw"
BKWIKI = "https://en.wikipedia.org/wiki/BKash"
WIKI = "https://en.wikipedia.org/wiki/BRAC_Bank"
BQR = "https://www.thedailystar.net/supplements/the-qr-era/news/bangla-qr-incentivising-merchants-cashless-bangladesh-4232656"
TAKAPAY = "https://www.thedailystar.net/business/economy/news/taka-pay-launching-tomorrow-3457676"
SHARE = "https://bangladeshmonitor.com.bd/en/visa-most-popular-credit-card-in-bd"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · BRAC · 25 years", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: BDT 1.45 trillion of assets and profit up 57% in H1 2026, BRAC as the anchor shareholder, 25 years of banking small businesses, modernised core and card systems, and the 'Missing Majority' strategy.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Profit up 57%, ROE 21.5%.", "div": "brac", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Consolidated assets of BDT 145,270 Cr (about BDT 1.45 trillion), loans BDT 76,189 Cr (+18%) and deposits BDT 109,491 Cr (+25%) at 30 June 2026; consolidated profit after tax BDT 1,423 Cr in H1 2026 (+57%), ROE 21.5%, NPL 2.03%, CRAR 19.95%. 2025 profit was BDT 2,251 Cr (+57%), with 2.3 million customers.",
              s=["con"], neo=[0, ""], src=[["H1 2026 earnings disclosure", H1], ["Financial Express: H1 2026, Aug 2026", FEH1], ["TBS: 2025 and Q1 2026, May 2026", TBS25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "BRAC 46%; Khan as CEO.", "div": "brac", "rev": "group", "products": [
            P("owners", "Ownership, listing & ratings", "Listed in Dhaka and Chittagong (BRACBANK); BRAC holds 46.2% and institutions, foreign investors and the public 53.8%; market value BDT 125.6 billion at end-2025, about USD 1 billion and the highest among Bangladeshi banks; rated B+ (S&P) and B2 (Moody's), at the sovereign ceiling, and AAA by CRAB.",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025", AR25]]),
            P("leadership", "Board & management", "Chairperson Meheriar M. Hasan; Managing Director and CEO Tareq Refat Ullah Khan, who followed Selim R. F. Hussain after his resignation in May 2025; CFO M Masud Rana; CIO A.S.M. Wasi Noman (from March 2026); Md. Mahiul Islam runs retail banking.",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025", AR25], ["TBS: silver jubilee, Jul 2026", JUBILEE]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & values", "blurb": "25 years, values-based.", "div": "brac", "rev": "sme", "products": [
            P("heritage", "BRAC heritage", "Opened on 4 July 2001 by Sir Fazle Hasan Abed's BRAC to bank small businesses; bKash followed in 2011 and TARA in 2017. It is Bangladesh's only member of the Global Alliance for Banking on Values, with more than 10,000 staff in 2026.",
              s=["sme"], o="I", neo=[0, ""], src=[["Annual report 2025", AR25], ["TBS: silver jubilee, Jul 2026", JUBILEE]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology", "blurb": "New loan and card systems.", "div": "brac", "rev": "group", "products": [
            P("tech", "Core, card & data systems", "Loan management and card systems modernised in 2025, the debit and ATM switch (IRIS) upgraded to PCI SSF 5.7, data-centre and disaster-recovery work, and a first Chief Information Officer from 1 March 2026.",
              s=["corp"], neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "The 'Missing Majority'.", "div": "brac", "rev": "group", "products": [
            P("strategy", "'Missing Majority' strategy", "For its 25th year the bank is moving from access to engagement, aiming at the about 72% of Bangladeshi adults outside formal finance, through digital channels, SME lending and sustainable finance (82% of the portfolio).",
              s=["con", "sme"], st="new", neo=[0, ""], src=[["Annual report 2025", AR25], ["H1 2026 earnings disclosure", H1]]),
            P("deals", "Capital & deals", "USD 30 million from IFC (April 2021), a USD 50 million DEG loan (January 2023), a BDT 1,000 Cr social bond, a EUR 60 million EIB credit line, and SoftBank's USD 250 million into bKash (November 2021).",
              s=["corp"], o="P", neo=[0, ""], src=[["Wikipedia: BRAC Bank", WIKI], ["H1 2026 earnings disclosure", H1], ["Wikipedia: bKash", BKWIKI]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: credit cards on Visa, Mastercard and Diners, debit mostly on Visa with Mastercard since 2025 and TakaPay, Google Pay on Visa, acquiring on both networks' gateways, NPSB and Bangla QR, more than USD 2 billion of remittances, and bKash.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "Visa on top, Mastercard second.", "div": "brac", "rev": "retail", "products": [
            P("visacredit", "Visa credit cards", "Visa Infinite (launched July 2019, revamped 2025), Visa Signature, Platinum Flexi, Cashback and TARA Platinum: the bank's top-tier credit cards. The credit book was BDT 1,723 Cr at June 2026 (+14%).", short="Visa credit",
              s=["con"], lc="borrow", ay="Jul 2019", o="P", at="Visa", neo=[0, "Visa."], src=[["BRAC Bank: cards", CARDS], ["Prothom Alo: four Visa credit cards, Jul 2019", VISA19], ["H1 2026 earnings disclosure", H1]]),
            P("mccredit", "Mastercard credit cards", "Mastercard World with health and wellness benefits (June 2023, a first in Bangladesh), Mastercard TARA World for women (September 2021) and Mastercard Millennial Titanium (October 2021); three Mastercard Excellence Awards for credit cards in 2025.", short="Mastercard credit",
              s=["con", "women"], lc="borrow", ay="Sep 2021", o="P", at="Mastercard", neo=[2, "Mastercard cards."],
              mc="Mastercard's main foothold at the bank.",
              src=[["Daily Star: Mastercard World, Jun 2023", MCWORLD], ["TBS: Mastercard TARA World, Sep 2021", TARAW], ["TBS: Millennial Titanium, Oct 2021", MILL], ["Annual report 2025", AR25]]),
            P("dualcredit", "Classic, Gold & Platinum credit", "The mass-market Classic, Gold/Gold Flexi and Platinum credit cards are offered on either Visa or Mastercard.", short="Visa/Mastercard credit",
              s=["con"], lc="borrow", o="P", at="Visa, Mastercard", neo=[1, "Visa or Mastercard."], src=[["BRAC Bank: cards", CARDS]]),
            P("diners", "Diners Club Emerald", "A Diners Club International credit card for lifestyle customers, launched 30 December 2025.",
              s=["con"], lc="borrow", st="new", ay="Dec 2025", o="P", at="Diners Club", neo=[0, "Diners Club."], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Debit cards", "blurb": "Mostly Visa; Mastercard since 2025.", "div": "brac", "rev": "retail", "products": [
            P("visadebit", "Visa debit cards", "Most of the debit range: Visa Platinum Multicurrency (also TARA and virtual), Signature Premium Banking, Medical Quota for treatment abroad, RFCD, Local Currency, Business Freelancer and the ARQ Express, a first in Bangladesh (2025). Debit spend BDT 1,787 Cr in H1 2026 (+29%).", short="Visa debit",
              s=["con", "probashi"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["BRAC Bank: cards", CARDS], ["Annual report 2025", AR25], ["H1 2026 earnings disclosure", H1]]),
            P("mcdebit", "Mastercard Platinum Multicurrency Debit", "The bank's first international Mastercard debit cards, the Platinum Multicurrency and the TARA version for women, launched 23 November 2025 with debit rewards on everyday spending at home and abroad.", short="Mastercard debit",
              s=["con", "women"], lc="everyday", st="new", ay="Nov 2025", o="P", at="Mastercard", neo=[2, "Mastercard cards."],
              mc="A first step into debit, which Visa has long held here.",
              src=[["Daily Star: Mastercard debit, Nov 2025", MCDEBIT], ["Annual report 2025", AR25]]),
            P("takapay", "TakaPay debit", "Cards on Bangladesh Bank's domestic scheme, launched in November 2023 to cut reliance on Visa and Mastercard, running on the national switch NPSB; BRAC Bank issues TakaPay and TakaPay TARA cards.", short="TakaPay (domestic)",
              s=["con"], lc="everyday", o="P", at="Bangladesh Bank", neo=[0, "Domestic scheme."], src=[["BRAC Bank: cards", CARDS], ["Daily Star: Taka Pay launch, Oct 2023", TAKAPAY]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "Wallets & tokens", "blurb": "Google Pay, Visa only.", "div": "brac", "rev": "retail", "products": [
            P("gpay", "Google Pay", "Google Pay for Visa credit cardholders from 9 February 2026, with tokens managed in Visa's CyberSource; Mastercard cards were not included and Mastercard token status is not public ⚠.",
              s=["con"], lc="everyday", st="new", ay="Feb 2026", o="P", at="Google, Visa", neo=[0, "Visa credit only."],
              mc="Mastercard cardholders cannot yet tap with a phone.",
              src=[["TBS: Google Pay, Feb 2026", GPAY], ["Annual report 2025", AR25]]),
            P("virtual", "Virtual cards & QR cash", "Virtual Visa debit cards for e-commerce and QR, and Bangladesh's first QR cash withdrawal at ATMs and CRMs with the Astha app.",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, "Visa virtual cards."], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acceptance", "blurb": "11,000 merchants, two gateways.", "div": "brac", "rev": "retail", "products": [
            P("acquiring", "Merchant acquiring", "POS, e-commerce and QR acceptance for more than 11,000 merchants, 2,500 of them premier, with 38.92 million transactions in 2025 (+14%); lead bank for Bangladesh Bank's Cashless Bangladesh drives.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["Annual report 2025", AR25]]),
            P("gateways", "Payment gateways: MPGS & CyberSource", "E-commerce runs on Mastercard Payment Gateway Services (Diners Club added in 2025) and Visa's CyberSource (account funding and token management added in 2025).", short="MPGS & CyberSource",
              s=["sme"], lc="move", o="P", at="Mastercard, Visa", neo=[1, "MPGS is Mastercard's; CyberSource is Visa's."],
              mc="MPGS gives Mastercard a working gateway inside the bank.",
              src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "NPSB & Bangla QR", "blurb": "The national rails.", "div": "brac", "rev": "sme", "products": [
            P("npsb", "NPSB real-time payments", "Bangladesh Bank's national switch: BRAC Bank uses it for real-time interbank collections into virtual accounts, automated incoming transfers and transfers in Astha.",
              s=["con", "sme"], lc="move", o="P", at="Bangladesh Bank", neo=[0, "National switch."], src=[["Annual report 2025", AR25]]),
            P("banglaqr", "Bangla QR", "The interoperable national QR, launched January 2023 and mandatory from 1 July 2026, with about 963,000 merchants by end-2025; the bank says it was the first to integrate with the bKash QR platform.",
              s=["sme", "wallet"], lc="move", st="flux", o="P", at="Bangladesh Bank, bKash", neo=[0, "National QR."], src=[["Daily Star: Bangla QR, Jul 2026", BQR], ["Annual report 2025", AR25]]),
        ]},
        {"id": "2.6", "ic": "earth", "name": "Cross-border", "blurb": "USD 2bn+ of remittances.", "div": "brac", "rev": "wholesale", "products": [
            P("remitin", "Inward remittances", "More than USD 2 billion in 2025 through more than 80 exchange-house partners, six added in March 2025 in the UK, Canada, Italy, the UAE, Oman and Qatar, paid into accounts and Astha. A secondary report ranks it third by FY26 remittances ⚠.",
              s=["probashi"], lc="move", o="P", at="Exchange houses", neo=[0, "No network named."],
              mc="Mastercard Move already serves bKash; the bank's own flows are open.",
              src=[["Annual report 2025", AR25], ["Daily Star: remittance partners, Mar 2025", REMIT]]),
            P("visadirect", "Visa Direct for Account", "Outward transfers for visa fees, study and treatment abroad, signed with Visa in June 2025.",
              s=["con"], lc="move", st="new", ay="Jun 2025", o="P", at="Visa", neo=[0, "Visa."], src=[["Daily Star: Visa Direct, Jun 2025", VDIRECT]]),
            P("saajan", "BRAC Saajan Exchange", "A UK money-transfer company bought in 2011, about 98% owned, which made a small loss in H1 2026.",
              s=["probashi"], lc="move", o="A", div="saajan", rev="group", neo=[None, "Nothing public."], src=[["H1 2026 earnings disclosure", H1], ["Wikipedia: BRAC Bank", WIKI]]),
        ]},
        {"id": "2.7", "ic": "smartphone", "name": "bKash", "blurb": "84 million customers.", "div": "bkash", "rev": "group", "products": [
            P("bkash", "bKash wallet", "Bangladesh's largest mobile financial service, set up by BRAC Bank in 2011: 84 million customers (50 million active), 950,000 merchants and BDT 1,363 billion a month in H1 2026; 2025 profit BDT 6.6 billion. BRAC Bank holds 51% of the ordinary shares and about 36% of the economics.", short="bKash",
              s=["wallet"], lc="everyday", o="B", neo=[0, "bKash's own rails."], src=[["H1 2026 earnings disclosure", H1], ["Annual report 2025", AR25], ["Wikipedia: bKash", BKWIKI]]),
            P("bkmove", "bKash remittances on Mastercard Move", "Money from banks and transfer companies on Mastercard's network lands directly in bKash wallets (June 2026), following Mastercard Send with Western Union and BRAC Bank in April 2016; bKash remittance volume was BDT 146 billion in H1 2026 (+51%).", short="Mastercard Move",
              s=["wallet", "probashi"], lc="move", st="new", ay="Jun 2026", o="P", at="Mastercard", neo=[3, "Mastercard Move."],
              mc="Mastercard's own product, live in the group.",
              src=[["Financial Express: bKash and Mastercard, Jun 2026", BKMOVE], ["NextBillion: Mastercard Send, Apr 2016", BKSEND], ["H1 2026 earnings disclosure", H1]]),
            P("bkdigital", "bKash Digital Bank", "Bangladesh Bank gave initial approval on 24 September 2026, one of five digital banks; the final licence depends on conditions being met.",
              s=["wallet"], lc="open", st="new", ay="Sep 2026", o="B", neo=[None, "Network not announced."],
              mc="A new bank behind 84 million wallets will need cards and tokens.",
              src=[["bdnews24: digital banks, Sep 2026", BKDB]]),
            P("bkcash", "bKash 24/7 cash management", "Distributors, agents and billers turn bKash e-money into BRAC Bank deposits through the bKash app: 19,600+ customers and 1.88 million transactions in 2025.",
              s=["sme", "wallet"], lc="move", o="B", div="brac", rev="wholesale", neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud controls reported to the card schemes, eKYC and a fully digital credit-card journey, credit scoring and personalised offers, and rewards on debit and credit.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & risk", "blurb": "No named scheme tools.", "div": "brac", "rev": "group", "products": [
            P("fraud", "Fraud & card risk", "Fraud incidents are reported to Visa, Mastercard and other schemes, and the debit switch is PCI certified; no Mastercard or Visa fraud product is named ⚠. NPL was 2.03% in June 2026.",
              s=["con"], lc="everyday", o="B", neo=[None, "Nothing public."],
              mc="Fraud risk grows as QR, virtual cards and wallets spread.",
              src=[["Annual report 2025", AR25], ["H1 2026 earnings disclosure", H1]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Identity & onboarding", "blurb": "Digital credit cards.", "div": "brac", "rev": "retail", "products": [
            P("ekyc", "eKYC", "Electronic KYC for accounts, foreign-currency accounts for non-residents and agent banking.",
              s=["con", "probashi"], lc="open", o="B", neo=[0, ""], src=[["Annual report 2025", AR25], ["Daily Star: remittance partners, Mar 2025", REMIT]]),
            P("digitalcard", "Digital credit-card onboarding", "Bangladesh's first fully digital credit-card application with e-signature (2025); about 41,000 new-to-bank credit cards were issued that year.",
              s=["con"], lc="open", st="new", o="B", neo=[1, "For Visa and Mastercard cards."], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "3.3", "ic": "brain", "name": "Data & AI", "blurb": "Scoring and automation.", "div": "brac", "rev": "group", "products": [
            P("data", "Credit scoring & automation", "Credit-scoring models, intelligent automation and customer-support tools across retail and SME lending; no named AI programme was found ⚠.",
              s=["sme"], lc="borrow", o="B", neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards & offers", "blurb": "Points on debit too.", "div": "brac", "rev": "retail", "products": [
            P("rewards", "Rewards & offers", "Reward points on debit as well as credit, which the bank calls unique in Bangladesh, double TARA points on Tuesdays, automated reward journeys and merchant offers at thousands of outlets.",
              s=["con", "women"], lc="grow", o="B", neo=[1, "On Visa and Mastercard cards."],
              mc="Card-linked offers could make it richer.",
              src=[["Daily Star: Mastercard debit, Nov 2025", MCDEBIT], ["Annual report 2025", AR25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: SME loans for more than 2 million businesses, TARA for 465,000 women, retail and premium banking, accounts for Bangladeshis abroad, and wholesale banking and broking.",
    "tiles": [
        {"id": "4.1", "ic": "briefcase", "name": "SME Banking", "blurb": "2 million SMEs served.", "div": "brac", "rev": "sme", "products": [
            P("sme", "SME loans & deposits", "The bank's founding business: SME assets of BDT 35,538 Cr and deposits of BDT 21,359 Cr (+28%) at June 2026, NPL 1.72%, and about BDT 2,000 billion of collateral-free loans since 2001; CMSMEs are more than 42% of loans.",
              s=["sme"], lc="borrow", neo=[0, ""], src=[["H1 2026 earnings disclosure", H1], ["Annual report 2025", AR25]]),
            P("smecards", "SME business cards", "Visa Multicurrency SME Business Debit and Credit (Uddomi) cards, launched January 2026 with a USD 3,000 annual FX quota, plus Borenno, TARA and Smart Farmer versions; networks for some are not stated ⚠.", short="SME cards (Visa)",
              s=["sme"], lc="everyday", st="new", ay="Jan 2026", o="P", at="Visa", neo=[0, "Visa where stated ⚠."],
              mc="Visa took the SME multicurrency card; commercial cards stay open.",
              src=[["Daily Star: SME cards, Jan 2026", VSME], ["BRAC Bank: SME cards", SMECARDS]]),
        ]},
        {"id": "4.2", "ic": "user-round", "name": "TARA", "blurb": "465,000 women.", "div": "tara", "rev": "retail", "products": [
            P("tara", "TARA women's banking", "Launched 2017 as Bangladesh's first full proposition for women: 465,340 customers (about 20% of the bank's), BDT 2,608 Cr of loans to women in 2025, with TARA cards on Mastercard (World, debit) and Visa (Platinum, debit).",
              s=["women"], lc="everyday", o="B", neo=[1, "TARA cards on Mastercard and Visa."],
              mc="Mastercard already carries TARA's top credit and new debit cards.",
              src=[["Annual report 2025", AR25], ["TBS: Mastercard TARA World, Sep 2021", TARAW]]),
        ]},
        {"id": "4.3", "ic": "house", "name": "Retail & premium", "blurb": "Deposits up 38%.", "div": "brac", "rev": "retail", "products": [
            P("retail", "Retail accounts & loans", "Retail deposits of BDT 50,324 Cr (+38%) and loans of BDT 13,625 Cr at June 2026; savings, DPS, fixed deposits, home and auto loans; retail funds under management BDT 552 billion in 2025.",
              s=["con"], lc="everyday", neo=[1, "Mostly Visa debit; Mastercard since 2025."], src=[["H1 2026 earnings disclosure", H1], ["Annual report 2025", AR25]]),
            P("premium", "Premium Banking", "Relationship banking for affluent customers, with Visa Signature and Platinum Premium Banking debit cards and Visa Infinite credit.",
              s=["con"], lc="grow", neo=[0, "Visa cards."], src=[["BRAC Bank: cards", CARDS]]),
        ]},
        {"id": "4.4", "ic": "plane", "name": "Probashi banking", "blurb": "Accounts from abroad.", "div": "brac", "rev": "retail", "products": [
            P("probashi", "Probashi & non-resident banking", "Accounts for Bangladeshis abroad and their families opened by eKYC, with foreign-currency deposits, NRB bonds and the Probashi Poribar account with life cover.",
              s=["probashi"], lc="open", neo=[0, ""], src=[["Daily Star: remittance partners, Mar 2025", REMIT]]),
        ]},
        {"id": "4.5", "ic": "building-2", "name": "Wholesale & markets", "blurb": "Trade of USD 4.4bn.", "div": "brac", "rev": "wholesale", "products": [
            P("wholesale", "Wholesale banking", "Corporate, commercial and institutional banking: assets of BDT 27,762 Cr, deposits of BDT 23,470 Cr and trade of USD 4.4 billion in H1 2026, plus an offshore unit of USD 938 million.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["H1 2026 earnings disclosure", H1]]),
            P("epl", "BRAC EPL investment & broking", "BRAC EPL Investments (100%) and BRAC EPL Stock Brokerage (90%), bought in 2009, plus treasury and bancassurance.",
              s=["corp"], lc="grow", o="A", div="epl", rev="group", neo=[0, ""], src=[["H1 2026 earnings disclosure", H1], ["Wikipedia: BRAC Bank", WIKI]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: the Astha app for 1.2 million, CORPnet for corporates, 310 branches and sub-branches with 446 SME offices, 1,122 agent outlets, and bKash's 369,000 agents.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Astha app", "blurb": "1.2 million users.", "div": "astha", "rev": "retail", "products": [
            P("astha", "Astha", "The digital banking app, launched in 2021: about 1.2 million users and more than BDT 200 billion of transactions a month, the majority of the bank's activity.",
              s=["con", "probashi", "women"], lc="everyday", o="B", neo=[0, ""], src=[["Annual report 2025", AR25], ["BRAC Bank: Astha", ASTHA]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "CORPnet", "blurb": "BDT 2.3 trillion a year.", "div": "brac", "rev": "wholesale", "products": [
            P("corpnet", "CORPnet", "The corporate banking portal, which handled BDT 2,273 billion in 2025.",
              s=["corp"], lc="move", o="B", neo=[0, ""], src=[["Annual report 2025", AR25]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & SME offices", "blurb": "310 branches, 446 SME offices.", "div": "brac", "rev": "sme", "products": [
            P("branches", "Branches, SME offices & ATMs", "194 branches, 116 sub-branches, 446 SME unit offices, 329 ATMs and 103 cash recyclers at end-2025.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["Annual report 2025", AR25], ["TBS: silver jubilee, Jul 2026", JUBILEE]]),
        ]},
        {"id": "5.4", "ic": "users-round", "name": "Agents", "blurb": "Bank agents and bKash's.", "div": "brac", "rev": "sme", "products": [
            P("agents", "Agent banking", "1,122 agent outlets reaching rural Bangladesh since 2018.",
              s=["con", "sme"], lc="open", o="P", neo=[0, ""], src=[["Annual report 2025", AR25]]),
            P("bkagents", "bKash agents & app", "About 369,000 bKash agents (H1 2026) and the bKash app, used actively by about 23.6 million customers at end-2025.",
              s=["wallet"], lc="everyday", div="bkash", rev="group", neo=[0, ""], src=[["H1 2026 earnings disclosure", H1], ["Annual report 2025", AR25]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at BRAC Bank", "blurb": "Second network, bKash's remittance rail.", "products": [
        P("mcatbrac", "Mastercard at BRAC Bank", "Visa carries the top credit cards, most debit, Google Pay, tokens, outbound remittance and the new SME cards. Mastercard carries World, TARA World, Millennial and the dual-network cards, the first Mastercard debit cards (November 2025) and the MPGS gateway, and bKash receives remittances on Mastercard Move (June 2026).",
          s=["con"], div="brac", rev="group", mc="The relationship this map is drawn for.",
          src=[["Daily Star: Mastercard debit, Nov 2025", MCDEBIT], ["Financial Express: bKash and Mastercard, Jun 2026", BKMOVE]]),
    ]},
    {"id": "pillar-market", "name": "Bangladesh payments", "blurb": "Visa 72%, TakaPay, Bangla QR.", "products": [
        P("market", "The Bangladeshi market", "Visa had about 71.8% of domestic credit-card spending in March 2025 against Mastercard's 17.5% and Amex's 10.4%; Bangladesh Bank is pushing TakaPay, NPSB and a Bangla QR mandate (July 2026), and approved five digital banks in September 2026.",
          s=["con"], div="brac", rev="group", src=[["Bangladesh Monitor: card shares, Jul 2025", SHARE], ["Daily Star: Bangla QR, Jul 2026", BQR], ["bdnews24: digital banks, Sep 2026", BKDB]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
