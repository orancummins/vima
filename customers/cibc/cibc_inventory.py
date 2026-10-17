"""CIBC's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the Q3 2026 news release, Report to Shareholders
and investor presentation (27 August 2026), the Q2 2026 news release (28 May 2026), the fiscal 2025 results
(4 December 2025) and the 2025 Annual Report. Card networks come from cibc.com, simplii.com and us.cibc.com
product pages and CIBC press releases. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's
own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

IR = "https://www.cibc.com/content/dam/cibc-public-assets/about-cibc/investor-relations/pdfs/quarterly-results"
Q3 = IR + "/2026/q326newsrelease-en.pdf"
Q3RPT = IR + "/2026/q326report-en.pdf"
Q3PRES = IR + "/2026/q326presentation-en.pdf"
Q2 = IR + "/2026/q226newsrelease-en.pdf"
FY25 = IR + "/2025/q425newsrelease-en.pdf"
AR25 = IR + "/2025/ar-25-en.pdf"
CEO = "https://www.sec.gov/Archives/edgar/data/1045520/000127956925000258/ex991.htm"
INVDAY = "https://cibc.mediaroom.com/2026-08-27-CIBC-to-host-Investor-Day-on-December-9,-2026"
TAB = "https://cibc.mediaroom.com/2026-10-01-CIBC-ranks-as-North-Americas-third-strongest-bank-in-2026-TAB-Global-1000-rankings"
CAI = "https://cibc.mediaroom.com/2025-05-27-CIBC-launches-in-house-AI-platform-enterprise-wide-after-successful-pilot"
DB26 = "https://cibc.mediaroom.com/2026-07-28-CIBC-wins-two-Digital-Banker-awards-for-AI-innovation-and-digital-transformation"
AI26 = "https://cibc.mediaroom.com/2026-10-15-CIBC-recognized-by-The-Digital-Banker-with-two-awards-for-enhancing-client-experience-through-AI-innovation"
MSFT = "https://cibc.mediaroom.com/2021-07-08-CIBC-and-Microsoft-announce-strategic-relationship-to-accelerate-the-banks-transformation-and-cloud-first-approach"
NCINO = "https://cibc.mediaroom.com/2022-01-12-CIBC-Selects-nCinos-Platform-to-Deliver-Enhanced-Client-Experience-for-Business-Banking-Clients"
CARDS = "https://www.cibc.com/en/personal-banking/credit-cards/all-credit-cards.html"
BIZCARDS = "https://www.cibc.com/en/business/credit-cards.html"
AEROPLAN20 = "https://cibc.mediaroom.com/2020-11-10-CIBC-launches-enhanced-suite-of-Aeroplan-R-Visa-credit-cards-to-help-Canadians-realize-their-travel-ambitions"
AEROPLAN18 = "https://cibc.mediaroom.com/2018-11-26-CIBC-completes-definitive-agreements-with-Air-Canada-regarding-Aeroplan"
AEROPLAN13 = "https://cibc.mediaroom.com/2013-09-16-CIBC-confirms-agreements-with-Aimia-and-TD-Bank-Group,1"
DIVIDEND = "https://cibc.mediaroom.com/2021-02-02-New-CIBC-Dividend-R-credit-card-enhancements-offer-more-cash-back-opportunities-for-everyday-spending"
EXPEDIA = "https://cibc.mediaroom.com/2024-10-01-CIBC-Aventura-clients-now-have-access-to-more-travel-options-through-new-CIBC-by-Expedia-CIBC-Rewards-Centre"
ADAPTA = "https://cibc.mediaroom.com/2025-05-01-CIBC-launches-CIBC-Adapta-TM-Mastercard-R-,-the-first-credit-card-in-Canada-that-automatically-adapts-to-spending-behaviour,-rewarding-cardholders-more-for-everyday-purchases"
COSTCO = "https://www.capitalone.ca/costco"
COSTCOBB = "https://www.bloomberg.com/news/articles/2021-09-02/cibc-to-take-over-capital-one-s-canadian-costco-card-business"
CARDSII = "https://cibc.mediaroom.com/2024-04-29-CIBC-announces-an-amendment-to-its-CARDS-II-securitization-program"
CTPMC = "https://www.cibc.com/content/dam/legal/pricing-consumer-mastercard-en.pdf"
CTPVISA = "https://www.cibc.com/content/dam/legal/pricing-consumer-visa-en.pdf"
DEBIT = "https://www.cibc.com/en/personal-banking/ways-to-bank/ways-to-pay/advantage-debit-card.html"
WAYSTOPAY = "https://www.cibc.com/en/personal-banking/ways-to-bank/ways-to-pay.html"
SIMPLIIDM = "https://www.simplii.com/en/bank-accounts/no-fee-chequing/debit-mastercard.html"
SIMPLIICARDS = "https://www.simplii.com/en/credit-cards.html"
USDEBIT = "https://us.cibc.com/en/personal/cibc-insights/benefits-of-a-cibc-debit-card.html"
USCROSS = "https://cibc.mediaroom.com/2018-05-22-CIBC-introduces-new-banking-solutions-for-Canadians-transacting-south-of-the-border"
RTR = "https://www.payments.ca/systems-services/payment-systems/real-time-rail-payment-system"
GMT = "https://www.cibc.com/en/personal-banking/ways-to-bank/how-to/global-money-transfer.html"
VISADIRECT = "https://cibc.mediaroom.com/2021-12-13-CIBC-expands-Global-Money-Transfer-capabilities-with-Visa-Direct"
MONEYGRAM = "https://cibc.mediaroom.com/2022-08-29-CIBC-continues-innovation-by-offering-clients-no-fee-same-day-cash-pick-up-abroad-through-MoneyGram-with-its-Global-Money-Transfer-service"
ALIPAY = "https://cibc.mediaroom.com/2023-03-02-CIBC-and-Simplii-Financial-launch-real-time-payments-to-the-worlds-most-popular-mobile-payment-platform"
PREPAID = "https://cibc.mediaroom.com/2016-09-26-CIBC-takes-leadership-position-in-foreign-exchange-innovation-through-new-CIBC-Smart-prepaid-card-launch"
AGORA = "https://cibc.mediaroom.com/2026-09-29-CIBC-joins-global-initiative-to-advance-cross-border-payments"
CADTOK = "https://cibc.mediaroom.com/2026-09-22-Six-Canadian-banks-explore-development-of-a-secure-CAD-tokenized-deposit-solution"
MERCHANT = "https://www.cibc.com/en/business/merchant-services.html"
TYL = "https://cibc.mediaroom.com/2022-02-23-CIBC-and-Pollinate-announce-exclusive-partnership-to-launch-Tyl-by-CIBC-in-Canada"
PAYMI = "https://cibc.mediaroom.com/2018-11-16-CIBC-introduces-new-digital-credit-and-debit-card-innovations"
VISAINST = "https://cibc.mediaroom.com/2021-06-24-CIBC-to-expand-installment-payment-options-for-online-credit-card-purchases-with-Visa-Canada"
REPLACE = "https://cibc.mediaroom.com/2019-10-28-Another-CIBC-Digital-Banking-First-Instantly-replace-a-lost-or-stolen-credit-card-on-your-mobile-phone"
ANDROIDPAY = "https://cibc.mediaroom.com/2017-05-31-CIBC-joins-Android-Pay-in-Canada"
DIGID = "https://cibc.mediaroom.com/2021-07-27-CIBCs-digital-identity-verification-makes-it-faster-and-easier-to-open-new-accounts-online"
NEWCOMER = "https://cibc.mediaroom.com/2024-05-27-New-innovative-digital-application-from-CIBC-makes-first-Canadian-banking-experience-for-newcomers-faster-and-more-convenient"
CRTEX = "https://cibc.mediaroom.com/2025-10-16-CIBC-launches-CIBC-CRTeX-TM-,-an-AI-enabled-client-personalization-engagement-engine-to-further-its-industry-leading-digital-capabilities-and-enhance-client-experiences"
INSIGHTS = "https://cibc.mediaroom.com/2021-02-03-New-CIBC-Mobile-Banking-feature-uses-AI-to-give-clients-personalized-data-driven-insights-into-their-spending-and-saving"
MX = "https://cibc.mediaroom.com/2022-08-08-CIBC-TO-ENHANCE-SECURE-AND-SEAMLESS-ACCESS-TO-FINANCIAL-TOOLS-AND-APPS-FOR-CLIENTS-THROUGH-AGREEMENT-WITH-MX"
OPENBANK = "https://www.canada.ca/en/department-finance/programs/financial-sector-policy/open-banking-implementation/budget-2025-canadas-framework-for-consumer-driven-banking.html"
SMART = "https://cibc.mediaroom.com/2025-08-27-CIBC-Launching-Innovative-Chequing-Account-to-Further-Recognize-Client-Relationships"
SIMPLII26 = "https://cibc.mediaroom.com/2026-10-13-Simplii-Financial-banks-on-simplicity-and-calm-with-its-next-evolution"
SIMPLII17 = "https://cibc.mediaroom.com/2017-08-16-CIBC-launches-new-direct-banking-brand-through-Simplii-Financial"
DEFENCE = "https://cibc.mediaroom.com/2026-09-10-CIBC-commits-2-billion-to-help-Canadian-defence-and-dual-use-businesses-grow"
DSRB = "https://cibc.mediaroom.com/2026-02-02-CIBC-Announces-Support-for-the-Defence,-Security,-and-Resilience-Bank"
PEARSON = "https://cibc.mediaroom.com/2024-12-16-Ambitions-take-flight-with-CIBC-through-expanded-relationship-with-Toronto-Pearson-airport"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · charter · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: C$1.18 trillion of assets, a Big Six charter, an in-house AI platform on Microsoft's cloud, and a strategy that sells the Caribbean bank to put capital into North America.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "C$1.18tn; CET1 13.4%.", "div": "group", "rev": "corp", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of C$1,177.8 billion, loans of C$611.4 billion and deposits of C$852.2 billion at 31 July 2026. Q3 2026 revenue C$8.4 billion; reported net income C$2.41 billion (adjusted C$2.65 billion, after a C$232 million after-tax charge on the Caribbean sale); adjusted ROE 16.8%; CET1 13.4%. Fiscal 2025 revenue C$29.1 billion and net income C$8.45 billion. Market value C$150.8 billion at 31 July 2026.",
              s=["corp"], neo=[0, ""], src=[["Q3 2026 results", Q3], ["Q3 2026 Report to Shareholders", Q3RPT], ["Fiscal 2025 results", FY25]]),
        ]},
        {"id": "1.2", "ic": "badge-check", "name": "Charter & leadership", "blurb": "Big Six; Culham CEO.", "div": "group", "rev": "corp", "products": [
            P("heritage", "Charter, listing & ratings", "A Schedule I bank headquartered in Toronto, listed on the TSX and NYSE as CM. About 15 million clients and 51,711 full-time-equivalent staff (July 2026). Rated AA (Morningstar DBRS and Fitch), Aa2 (Moody's) and A+ (S&P) on deposits. Ranked North America's third-strongest bank in the TAB Global 1000 (October 2026).",
              s=["con"], o="I", neo=[0, ""], src=[["2025 Annual Report", AR25], ["Q3 2026 Report to Shareholders", Q3RPT], ["CIBC: TAB Global 1000, Oct 2026", TAB]]),
            P("leadership", "Executive team", "Harry Culham, CEO since 1 November 2025, succeeding Victor Dodig; chair Katharine Stevenson. CFO Robert Sedran; Hratch Panossian runs Personal and Business Banking, Susan Rimmer Commercial Banking and Wealth, Kevin Li the U.S. region and Christian Exshaw Capital Markets.",
              s=["corp"], neo=[0, ""], src=[["CIBC: CEO succession, Mar 2025", CEO], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "1.3", "ic": "brain", "name": "AI, data & cloud", "blurb": "CAI; Azure.", "div": "group", "rev": "corp", "products": [
            P("cai", "CIBC AI (CAI)", "An in-house generative-AI platform, rolled out bank-wide in May 2025 after a pilot that saved more than 200,000 hours. CAI 2.0, piloted in Q3 2026, is described as the first enterprise-wide agentic AI workspace in Canadian banking, with an Agents Marketplace.",
              s=["corp"], st="new", ay="May 2025", o="B", neo=[0, ""], src=[["CIBC: CAI launch, May 2025", CAI], ["Q3 2026 results", Q3], ["CIBC: Digital Banker awards, Jul 2026", DB26]]),
            P("aitools", "AdvisorAssist & DocuMind", "AdvisorAssist summarises client meetings and cuts advisers' charting time by up to 50%; DocuMind reads documents for faster lending decisions and fraud detection. Both won Digital Banker awards in October 2026.",
              s=["inv", "corp"], st="new", o="B", neo=[0, ""], src=[["CIBC: AI awards, Oct 2026", AI26]]),
            P("cloud", "Cloud & core platforms", "Microsoft Azure as the primary cloud under a multi-year agreement (July 2021), nCino for Business Banking (January 2022) and Salesforce for client relationships.",
              s=["corp"], o="P", at="Microsoft, nCino", neo=[0, ""], src=[["CIBC and Microsoft, Jul 2021", MSFT], ["nCino and CIBC, Jan 2022", NCINO]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & portfolio", "blurb": "Four priorities; Investor Day 9 Dec.", "div": "group", "rev": "corp", "products": [
            P("strategy", "Strategic priorities", "Four priorities: mass affluent and private wealth, digital-first personal banking, connectivity across the bank, and a simpler, safer bank. Mass-affluent clients grew 4% in the year to Q3 2026. New financial objectives are due at Investor Day on 9 December 2026.",
              s=["corp"], neo=[0, ""], src=[["2025 Annual Report", AR25], ["Q3 2026 presentation", Q3PRES], ["CIBC: Investor Day, Aug 2026", INVDAY]]),
            P("deals", "Acquisitions & stakes", "The Costco credit card portfolio from Capital One (closed March 2022), a stake in Pollinate (2022) and 19.15% of the US wealth firm &Partners (closed July 2026).",
              s=["card", "inv"], o="A", neo=[0, ""], src=[["Capital One: Costco card moves to CIBC", COSTCO], ["Q3 2026 Report to Shareholders", Q3RPT]]),
            P("caribbean", "CIBC Caribbean sale", "Agreement of May 2026 to sell CIBC's 91.67% of CIBC Caribbean to Butterfield for about US$1.6 billion, US$1 billion in cash and about 22% of Butterfield; closing expected in the first half of 2027.",
              s=["corp"], st="flux", neo=[0, ""], src=[["Q2 2026 results", Q2], ["Q3 2026 Report to Shareholders", Q3RPT]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: own-brand credit cards on Visa, the Costco and Adapta cards on Mastercard, business cards mostly on Visa, debit on Interac with Visa Debit (Mastercard at Simplii and in the US), Interac e-Transfer, Global Money Transfer and tokenised deposits, and acceptance through Global Payments.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards on Visa", "blurb": "Aventura, Aeroplan, Dividend.", "div": "canada", "rev": "cpbb", "products": [
            P("aventura", "CIBC Aventura Visa cards", "The travel-rewards line from Visa Infinite Privilege to Gold, plus a US-dollar Aventura Gold Visa. Points redeem through the CIBC Rewards Centre and, since October 2024, CIBC by Expedia.", short="Aventura (Visa)",
              s=["card"], lc="borrow", o="B", neo=[0, "Visa."], src=[["CIBC: all credit cards", CARDS], ["CIBC by Expedia, Oct 2024", EXPEDIA]]),
            P("aeroplan", "CIBC Aeroplan Visa cards", "Aeroplan Visa Infinite Privilege, Visa Infinite, Visa and student cards under agreements with Air Canada (November 2018), relaunched in November 2020. CIBC kept about 630,000 accounts when TD bought about half its Aeroplan portfolio in 2013.", short="Aeroplan (Visa)",
              s=["card"], lc="borrow", o="P", at="Air Canada", neo=[0, "Visa."], src=[["CIBC: Aeroplan Visa suite, Nov 2020", AEROPLAN20], ["CIBC: Air Canada agreements, Nov 2018", AEROPLAN18], ["CIBC: Aimia and TD agreements, Sep 2013", AEROPLAN13]]),
            P("dividend", "CIBC Dividend, Select & Classic Visa cards", "Cash-back Dividend cards from Visa Infinite to student, refreshed in February 2021, and the low-rate Select and Classic Visa. Gross credit card loans across the bank were C$21.6 billion at October 2025.", short="Dividend (Visa)",
              s=["card", "con"], lc="borrow", o="B", neo=[0, "Visa."], src=[["CIBC: Dividend refresh, Feb 2021", DIVIDEND], ["CIBC: all credit cards", CARDS], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards on Mastercard", "blurb": "Costco and Adapta.", "div": "canada", "rev": "cpbb", "products": [
            P("costco", "CIBC Costco Mastercard", "CIBC became the exclusive issuer of Costco's credit card in Canada and bought Capital One's Costco Mastercard portfolio on 4 March 2022 (reported at more than C$3 billion of balances ⚠). The card doubles as the Costco membership card. In April 2024 CIBC opened its CARDS II securitisation trust to Mastercard accounts.", short="Costco (Mastercard)",
              s=["card"], lc="borrow", ay="Mar 2022", o="A", at="Costco", neo=[2, "Mastercard."],
              mc="CIBC's largest Mastercard book, and a member-acquisition channel.", src=[["Capital One: Costco card moves to CIBC", COSTCO], ["Bloomberg: CIBC takes Costco card, Sep 2021 ⚠", COSTCOBB], ["CIBC: CARDS II amendment, Apr 2024", CARDSII]]),
            P("adapta", "CIBC Adapta Mastercard", "A no-fee card launched on 1 May 2025 that pays 1.5 points per dollar in each cardholder's top three of 12 categories every month. It was the first card in Canada with Mastercard's Touch Card notch; Mastercard Canada's Diane Miquelon spoke at launch. A student version exists.", short="Adapta (Mastercard)",
              s=["card"], lc="borrow", st="new", ay="May 2025", o="P", at="Mastercard", neo=[2, "Mastercard, with Touch Card."],
              mc="The first CIBC-designed Mastercard card.", src=[["CIBC: Adapta launch, May 2025", ADAPTA]]),
        ]},
        {"id": "2.3", "ic": "briefcase-business", "name": "Business cards", "blurb": "Visa, plus Costco Business.", "div": "canada", "rev": "cpbb", "products": [
            P("bizvisa", "Business & corporate Visa cards", "Aventura and Aeroplan Visa cards for business, bizline Visa and Corporate Classic Plus Visa, with Visa Spend Clarity reporting and Visa SavingsEdge. Large-corporate and purchasing-card programmes were not checked ⚠.", short="Business cards (Visa)",
              s=["sme"], lc="borrow", o="B", neo=[0, "Visa."], src=[["CIBC: business credit cards", BIZCARDS]]),
            P("costcobiz", "CIBC Costco Business Mastercard", "The business version of the Costco card, CIBC's only business card on Mastercard.", short="Costco Business (Mastercard)",
              s=["sme"], lc="borrow", ay="Mar 2022", o="A", at="Costco", neo=[2, "Mastercard."], src=[["CIBC: business credit cards", BIZCARDS]]),
        ]},
        {"id": "2.4", "ic": "wallet-cards", "name": "Debit cards", "blurb": "Interac with Visa Debit; Mastercard at Simplii.", "div": "canada", "rev": "cpbb", "products": [
            P("advdebit", "CIBC Advantage Debit Card", "Interac Debit in stores in Canada (tap up to C$250) and Visa Debit online, in apps, abroad and for recurring payments. The card shows up twice in mobile wallets, once per network.", short="Advantage Debit (Interac + Visa)",
              s=["con"], lc="everyday", o="B", neo=[0, "Interac and Visa Debit."], src=[["CIBC: Advantage Debit Card", DEBIT], ["CIBC: ways to pay", WAYSTOPAY]]),
            P("simpliidebit", "Simplii Financial Debit Mastercard", "Simplii's bank card works on Interac in stores in Canada and as a Debit Mastercard online and abroad, with Mastercard Zero Liability. Launch date not found ⚠.", short="Simplii Debit Mastercard",
              s=["con"], lc="everyday", o="B", neo=[1, "Interac in store; Debit Mastercard online and abroad."], src=[["Simplii: Debit Mastercard", SIMPLIIDM]]),
            P("usdebit", "CIBC Bank USA debit card", "CIBC Bank USA's consumer debit card runs on Mastercard, with Zero Liability and Apple Pay. Canadians can hold it through the CIBC Bank USA Smart Account (May 2018).", short="US debit (Mastercard)",
              s=["con", "inv"], lc="everyday", o="I", neo=[2, "Mastercard."], src=[["CIBC Bank USA: debit card", USDEBIT], ["CIBC: cross-border banking, May 2018", USCROSS]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Domestic transfers", "blurb": "Interac e-Transfer; RTR.", "div": "canada", "rev": "cpbb", "products": [
            P("etransfer", "Interac e-Transfer & bill payments", "Unlimited Interac e-Transfers in the Smart Account, bill payments and pre-authorised debits.",
              s=["con", "sme"], lc="move", o="P", at="Interac", neo=[0, "Interac."], src=[["CIBC: Smart Account, Aug 2025", SMART], ["CIBC: ways to pay", WAYSTOPAY]]),
            P("rtr", "Real-Time Rail", "Payments Canada's Real-Time Rail launches in Q4 2026, with participant testing under way. CIBC's role and the vendors behind it were not found ⚠.",
              s=["con", "corp"], lc="move", st="flux", ay="Q4 2026", neo=[None, "Vendors not public ⚠."], src=[["Payments Canada: Real-Time Rail", RTR]]),
        ]},
        {"id": "2.6", "ic": "earth", "name": "Cross-border & digital money", "blurb": "Visa Direct; Agorá.", "div": "cm", "rev": "cm", "products": [
            P("gmt", "CIBC Global Money Transfer", "No-fee transfers to more than 130 countries since 2015, run by Capital Markets' FX team: push to Visa cards through Visa Direct (December 2021), MoneyGram cash pick-up in 40+ countries (August 2022) and Alipay wallets through Citi WorldLink (March 2023).", short="Global Money Transfer",
              s=["new"], lc="move", o="P", at="Visa, MoneyGram, Citi", neo=[0, "Visa Direct, MoneyGram and Citi."],
              mc="A remittance engine with no Mastercard endpoint.", src=[["CIBC: Global Money Transfer", GMT], ["CIBC: Visa Direct, Dec 2021", VISADIRECT], ["CIBC: MoneyGram, Aug 2022", MONEYGRAM], ["CIBC: Alipay via Citi, Mar 2023", ALIPAY]]),
            P("prepaid", "Smart Prepaid Travel Visa", "Reloadable foreign-currency prepaid cards (US dollars, euros, pounds, pesos), launched in September 2016 with an Air Canada multi-currency card. Current status not checked ⚠.", short="Prepaid travel (Visa)",
              s=["card"], lc="move", o="B", neo=[0, "Visa."], src=[["CIBC: Smart Prepaid Visa, Sep 2016", PREPAID]]),
            P("dcc", "Dynamic Currency Conversion & payments", "Capital Markets runs a payments business, including Dynamic Currency Conversion that lets other banks offer foreign cardholders ATM withdrawals in their home currency.",
              s=["corp"], lc="move", o="B", neo=[None, "Networks not stated."], src=[["CIBC: Project Agorá, Sep 2026", AGORA]]),
            P("cadtoken", "CAD tokenised deposits", "One of six Canadian banks exploring a Canadian-dollar tokenised-deposit solution, first moving tokens between Canadian institutions (22 September 2026).",
              s=["corp"], lc="move", st="new", ay="Sep 2026", o="P", neo=[0, "Bank-led; no network named."], src=[["Six banks: CAD tokenised deposits, Sep 2026", CADTOK]]),
            P("agora", "Project Agorá", "Joined the BIS and IIF project testing tokenised commercial-bank deposits and central-bank reserves for wholesale cross-border payments (29 September 2026), led by Giorgia Anton, head of payments in Capital Markets.",
              s=["corp"], lc="move", st="new", ay="Sep 2026", o="P", at="BIS, IIF", neo=[0, ""], src=[["CIBC: Project Agorá, Sep 2026", AGORA]]),
        ]},
        {"id": "2.7", "ic": "store", "name": "Acquiring", "blurb": "Global Payments.", "div": "canada", "rev": "cpbb", "products": [
            P("globalpay", "Merchant services by Global Payments", "CIBC refers business clients to Global Payments for terminals, Genius cloud point of sale and online payments; it does not acquire itself. Global Payments bought CIBC's acquiring business in 2000 ⚠.", short="Global Payments",
              s=["sme"], lc="move", o="P", at="Global Payments", neo=[0, "Global Payments; accepts all networks."], src=[["CIBC: merchant services", MERCHANT]]),
            P("tyl", "Tyl by CIBC", "A digital acceptance and point-of-sale platform from Pollinate, announced in February 2022, with CIBC joining Mastercard, NatWest, NAB and Fiserv as Pollinate shareholders. Whether it is still offered was not found ⚠.",
              s=["sme"], lc="move", st="unconf", ay="Feb 2022", o="P", at="Pollinate", neo=[None, "Mastercard a Pollinate shareholder; status unknown ⚠."], src=[["CIBC and Pollinate, Feb 2022", TYL]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What rides on the rails: Aventura and Aeroplan rewards with Paymi and Skip offers, wallets and Click to Pay on both networks, instalments, digital identity and fraud work, and CRTeX personalisation with MX open-banking access.",
    "tiles": [
        {"id": "3.1", "ic": "gift", "name": "Rewards & offers", "blurb": "Aventura, Expedia, Paymi, Skip.", "div": "canada", "rev": "cpbb", "products": [
            P("rewards", "CIBC Rewards Centre & CIBC by Expedia", "Aventura points redeem for travel through CIBC by Expedia (October 2024: 900,000+ hotels and 500+ airlines); Aeroplan, Dividend cash back, Adapta points and Costco cash back run alongside.",
              s=["card"], lc="beyond", o="P", at="Expedia Group", neo=[0, "Mostly on Visa cards."], src=[["CIBC by Expedia, Oct 2024", EXPEDIA]]),
            P("offers", "Card-linked offers", "Paymi cash back on CIBC credit, debit and prepaid cards (November 2018) and free Skip+ delivery for linked CIBC credit or debit cards (2025).",
              s=["card", "con"], lc="beyond", o="P", at="Paymi, Skip", neo=[0, "Network-neutral partners."], src=[["CIBC: Paymi, Nov 2018", PAYMI], ["2025 Annual Report", AR25], ["CIBC: ways to pay", WAYSTOPAY]]),
        ]},
        {"id": "3.2", "ic": "smartphone", "name": "Wallets, checkout & instalments", "blurb": "Click to Pay from 21 October.", "div": "canada", "rev": "cpbb", "products": [
            P("clicktopay", "Click to Pay", "From 21 October 2026 CIBC enrols eligible credit cards in Click to Pay with each card's network when the card is activated, with opt-out in online and mobile banking. The change appears in both the Mastercard and the Visa cardholder notices.",
              s=["card"], lc="everyday", st="new", ay="Oct 2026", o="P", neo=[1, "Mastercard's on Costco and Adapta; Visa's on the rest."],
              mc="Issuer-led enrolment puts Mastercard's Click to Pay on every CIBC Mastercard.", src=[["CIBC: Mastercard cardholder notice, 2026", CTPMC], ["CIBC: Visa cardholder notice, 2026", CTPVISA]]),
            P("wallets", "Mobile wallets", "Credit and debit cards in Apple Pay, Google Pay and Samsung Pay (Android Pay from May 2017); a lost credit card can be replaced in the app and used in a wallet at once (October 2019). Token services are not named ⚠.",
              s=["con", "card"], lc="everyday", o="P", at="Apple, Google, Samsung", neo=[1, "Visa and Mastercard tokens ⚠."], src=[["CIBC: ways to pay", WAYSTOPAY], ["CIBC: Android Pay, May 2017", ANDROIDPAY], ["CIBC: instant card replacement, Oct 2019", REPLACE]]),
            P("instalments", "Pace It & Visa Installments", "CIBC Pace It turns purchases of C$100 or more into instalment plans after the fact (since September 2019); Visa Installments at online checkout was announced in June 2021 for early 2022 ⚠ launch not confirmed.",
              s=["card"], lc="borrow", o="P", at="Visa Canada", neo=[0, "In-house and Visa."], src=[["CIBC and Visa: instalments, Jun 2021", VISAINST]]),
        ]},
        {"id": "3.3", "ic": "shield-check", "name": "Identity & fraud", "blurb": "Digital ID; disputes automation.", "div": "canada", "rev": "cpbb", "products": [
            P("digitalid", "Digital identity & onboarding", "Machine-learning identity verification for online account opening (July 2021) and a bundled card-and-account application for newcomers (May 2024).",
              s=["new", "con"], lc="open", o="B", neo=[0, ""], src=[["CIBC: digital ID, Jul 2021", DIGID], ["CIBC: newcomer application, May 2024", NEWCOMER]]),
            P("fraud", "Fraud & disputes", "Card disputes automation (2025) cut call volumes; DocuMind supports fraud detection. Fraud vendors are not named ⚠.",
              s=["card"], lc="everyday", o="B", neo=[None, "Vendors not public."], src=[["2025 Annual Report", AR25], ["CIBC: AI awards, Oct 2026", AI26]]),
        ]},
        {"id": "3.4", "ic": "sparkles", "name": "Data, personalisation & open banking", "blurb": "CRTeX; MX.", "div": "canada", "rev": "cpbb", "products": [
            P("crtex", "CIBC CRTeX", "CIBC Real-Time Experience, a proprietary AI engine that personalises offers and advice across app, web, contact centres and branches in near real time; national launch October 2025.",
              s=["con", "card"], lc="everyday", st="new", ay="Oct 2025", o="B", neo=[0, ""], src=[["CIBC: CRTeX, Oct 2025", CRTEX]]),
            P("insights", "Insights, Smart Planner & GoalPlanner", "AI spending insights in the app (February 2021), Smart Planner (used by 894,000 clients in 2025) and GoalPlanner financial plans (430,000 households).",
              s=["con", "inv"], lc="grow", o="B", neo=[0, ""], src=[["CIBC: Insights, Feb 2021", INSIGHTS], ["2025 Annual Report", AR25]]),
            P("mx", "Open-banking data access", "API data sharing with MX under the FDX standard (August 2022), replacing screen-scraping for fintech apps. Canada's consumer-driven banking framework, overseen by the Bank of Canada, is legislated; payment initiation waits for a second phase.",
              s=["con"], lc="everyday", o="P", at="MX", neo=[0, ""], src=[["CIBC and MX, Aug 2022", MX], ["Finance Canada: consumer-driven banking", OPENBANK]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What CIBC sells: personal banking and Imperial Service, Simplii's direct bank, business and commercial banking, wealth, U.S. commercial banking and wealth, and Capital Markets.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Personal banking", "blurb": "Smart Account; Imperial Service.", "div": "canada", "rev": "cpbb", "products": [
            P("smartaccount", "CIBC Smart Account", "A tiered chequing account from 1 November 2025 that unlocks fee rebates and benefits as balances grow, with versions for newcomers (best retail product in Canada, 2026), students and skilled trades. Canadian Personal and Business Banking earned C$948 million in Q3 2026.",
              s=["con", "new"], lc="open", st="new", ay="Nov 2025", o="B", neo=[0, "Debit on Interac and Visa."], src=[["CIBC: Smart Account, Aug 2025", SMART], ["Q2 2026 results", Q2], ["Q3 2026 results", Q3]]),
            P("imperial", "Imperial Service", "Advice for mass-affluent clients; their number grew 4% and money-in balances 12% in the year to Q3 2026.",
              s=["inv"], lc="grow", o="B", neo=[0, ""], src=[["Q3 2026 presentation", Q3PRES], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "4.2", "ic": "rocket", "name": "Simplii Financial", "blurb": "No-fee direct bank.", "div": "simplii", "rev": "cpbb", "products": [
            P("simplii", "Simplii Financial", "CIBC's no-fee direct bank since 2017, first among no-fee chequing providers by balances and accounts (2025). A new app, brand and Simplii Account with folders began piloting on 13 October 2026. Debit Mastercard; Cash Back Visa.",
              s=["con"], lc="everyday", st="new", ay="Aug 2017", o="B", neo=[1, "Debit Mastercard; credit card on Visa."], src=[["CIBC: Simplii launch, Aug 2017", SIMPLII17], ["CIBC: Simplii relaunch, Oct 2026", SIMPLII26], ["Simplii: credit cards", SIMPLIICARDS], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Business & commercial banking", "blurb": "Skilled trades; defence.", "div": "canada", "rev": "ccbwm", "products": [
            P("business", "Business banking", "Accounts and lending for small businesses, a skilled-trades programme (2025) and a commitment of C$12 billion in new SME credit over 2025–27.",
              s=["sme"], lc="borrow", o="B", neo=[0, ""], src=[["2025 Annual Report", AR25]]),
            P("commercial", "Commercial banking & cash management", "Middle-market banking and cash management (Global Finance's best overall cash management bank in Canada, 2026), a C$2 billion commitment to defence and dual-use businesses (September 2026) and partner-bank status for the Defence, Security and Resilience Bank. Commercial banking revenue C$752 million in Q3 2026.",
              s=["corp"], lc="borrow", st="new", o="B", neo=[0, ""], src=[["Q3 2026 Report to Shareholders", Q3RPT], ["CIBC: defence commitment, Sep 2026", DEFENCE], ["CIBC: DSRB, Feb 2026", DSRB]]),
        ]},
        {"id": "4.4", "ic": "trending-up", "name": "Wealth management", "blurb": "Wood Gundy, Investor's Edge.", "div": "wealth", "rev": "ccbwm", "products": [
            P("wealth", "Canadian wealth", "Private Wealth, CIBC Wood Gundy, Investor's Edge (new accounts up 34% in the year to Q3 2026) and CIBC Global Asset Management. Assets under administration C$4.3 trillion and under management C$479 billion, bank-wide.",
              s=["inv"], lc="grow", o="B", neo=[0, ""], src=[["Q3 2026 Report to Shareholders", Q3RPT], ["Q3 2026 presentation", Q3PRES]]),
        ]},
        {"id": "4.5", "ic": "flag", "name": "U.S. commercial & wealth", "blurb": "CIBC Bank USA; &Partners.", "div": "usa", "rev": "us", "products": [
            P("usbank", "CIBC Bank USA & U.S. Private Wealth", "Middle-market commercial banking from the former PrivateBancorp, private and small-business banking in chosen US markets, U.S. Private Wealth and a 19.15% stake in &Partners. Net income US$228 million in Q3 2026.",
              s=["corp", "inv"], lc="borrow", o="A", neo=[1, "Debit on Mastercard; other cards not checked ⚠."], src=[["Q3 2026 Report to Shareholders", Q3RPT], ["CIBC Bank USA: debit card", USDEBIT]]),
        ]},
        {"id": "4.6", "ic": "chart-candlestick", "name": "Capital markets", "blurb": "Best investment bank in Canada.", "div": "cm", "rev": "cm", "products": [
            P("capmkts", "CIBC Capital Markets", "Global markets, corporate and investment banking, research and payments; net income C$722 million in Q3 2026 (up 34%). Global Finance's best investment bank in Canada for 2026.",
              s=["corp"], lc="grow", o="B", neo=[0, ""], src=[["Q3 2026 results", Q3], ["Q2 2026 results", Q2]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How clients reach CIBC: the mobile app and online banking, 10 million of them registered; banking centres including Toronto Pearson; and partners such as Costco and Air Canada.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Digital banking", "blurb": "J.D. Power first among Big Five.", "div": "canada", "rev": "cpbb", "products": [
            P("app", "CIBC Mobile & Online Banking", "10 million digitally registered clients (2025). Highest customer satisfaction for online and mobile banking among the Big Five in J.D. Power's 2025 studies, and for online banking again in 2026; a Virtual Assistant handles routine requests.",
              s=["con", "card"], lc="everyday", o="B", neo=[0, ""], src=[["2025 Annual Report", AR25], ["Q3 2026 results", Q3]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Banking centres & ATMs", "blurb": "Including Toronto Pearson.", "div": "canada", "rev": "cpbb", "products": [
            P("branches", "Banking centres & ATMs", "Banking centres across Canada (count not found ⚠), new centres at Toronto Pearson for travellers and newcomers (December 2024), and 800+ US-dollar ATMs in Canada.",
              s=["con", "new"], lc="open", o="B", neo=[0, ""], src=[["CIBC: Toronto Pearson, Dec 2024", PEARSON], ["CIBC: Global Money Transfer", GMT]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "Costco, Air Canada.", "div": "canada", "rev": "cpbb", "products": [
            P("costcooffer", "Costco Banking Offer & kiosks", "Since 2025, a banking offer for Costco members opening their first CIBC account, sold through CIBC kiosks rotating through Costco warehouses.",
              s=["con", "card"], lc="open", st="new", o="P", at="Costco", neo=[1, "Leads into the Costco Mastercard."], src=[["2025 Annual Report", AR25]]),
            P("travel", "Air Canada & Expedia", "Aeroplan Visa cards with Air Canada and Aventura travel booked through Expedia.",
              s=["card"], lc="beyond", o="P", at="Air Canada, Expedia", neo=[0, "Visa."], src=[["CIBC: Aeroplan Visa suite, Nov 2020", AEROPLAN20], ["CIBC by Expedia, Oct 2024", EXPEDIA]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at CIBC", "blurb": "Costco, Adapta, Simplii and US debit.", "products": [
        P("mcatcibc", "Mastercard at CIBC", "Visa carries almost all of CIBC's own-brand credit cards, every CIBC debit card (with Interac), most business cards, prepaid and Global Money Transfer. Mastercard carries the Costco cards (since March 2022), Adapta (May 2025), Simplii debit and CIBC Bank USA debit, and its Click to Pay goes live on those cards on 21 October 2026. No public network agreement or renewal date was found.",
          s=["card"], div="group", rev="corp", mc="The relationship this map is drawn for.",
          src=[["CIBC: Adapta launch, May 2025", ADAPTA], ["CIBC: all credit cards", CARDS], ["CIBC: Mastercard cardholder notice, 2026", CTPMC]]),
    ]},
    {"id": "pillar-market", "name": "Canadian banking", "blurb": "RTR, open banking, tokens.", "products": [
        P("market", "The Canadian market", "Payments Canada's Real-Time Rail launches in Q4 2026. Consumer-driven banking is legislated, with the Bank of Canada as overseer and payment initiation left to a second phase. Six large banks, CIBC among them, are exploring a CAD deposit token. Interac runs domestic debit.",
          s=["con"], div="group", rev="corp", src=[["Payments Canada: Real-Time Rail", RTR], ["Finance Canada: consumer-driven banking", OPENBANK], ["Six banks: CAD tokenised deposits, Sep 2026", CADTOK]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
