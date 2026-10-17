"""Scotiabank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the bank's own unless a source says otherwise: the Q3 2026 results, investor presentations and
fact sheet (25 August 2026) and the 2025 Annual Report (December 2025); fiscal years end 31 October. ``neo``
is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on
Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

Q3 = "https://www.scotiabank.com/content/dam/scotiabank/corporate/quarterly-reports/2026/q3/Q326_Quarterly_Press_Release-EN.pdf"
FACT = "https://www.scotiabank.com/content/dam/scotiabank/corporate/quarterly-reports/2026/q3/Q326_Scotiabank_Investor_Factsheet.pdf"
PRES = "https://www.scotiabank.com/content/dam/scotiabank/corporate/quarterly-reports/2026/q3/Q326_Investor_Presentation.pdf"
MKT = "https://www.scotiabank.com/content/dam/scotiabank/corporate/quarterly-reports/2026/q3/Q326_Investor_Marketing_Presentation.pdf"
QR = "https://www.scotiabank.com/content/dam/scotiabank/corporate/quarterly-reports/2026/q3/Q326_Shareholders_Report-EN.pdf"
AR25 = "https://www.scotiabank.com/content/dam/scotiabank/corporate/quarterly-reports/2025/q4/Annual_Report_2025_EN.pdf"
FY25 = "https://www.newswire.ca/news-releases/scotiabank-reports-fourth-quarter-and-2025-results-806914704.html"
EXEC = "https://www.scotiabank.com/ca/en/about/our-company/executive-management.html"
APPTS = "https://www.newswire.ca/news-releases/scotiabank-announces-executive-leadership-appointments-879299029.html"
HAMERS = "https://www.newswire.ca/news-releases/scotiabank-welcomes-ralph-hamers-to-its-board-of-directors-820560711.html"
KEY = "https://www.newswire.ca/news-releases/scotiabank-completes-additional-investment-in-keycorp-882830070.html"
DAVI25 = "https://www.newswire.ca/news-releases/scotiabank-enters-into-an-agreement-to-transfer-banking-operations-in-colombia-costa-rica-and-panama-to-davivienda-in-exchange-for-an-approximate-20-ownership-stake-in-the-combined-banking-operations-881068145.html"
DAVI = "https://www.newswire.ca/news-releases/scotiabank-and-davivienda-close-previously-announced-transaction-to-transfer-scotiabank-s-banking-operations-in-colombia-costa-rica-and-panama-889770837.html"
MAPLE = "https://www.newswire.ca/news-releases/scotiabank-to-acquire-maplemark-bank-to-support-strategic-growth-in-global-banking-and-markets-business-803346764.html"
JAM = "https://www.newswire.ca/news-releases/scotiabank-announces-plans-to-fully-acquire-scotia-group-jamaica-limited-811213061.html"
AGORA = "https://www.newswire.ca/news-releases/scotiabank-joins-project-agora-to-help-explore-the-future-of-wholesale-cross-border-payments-845735531.html"
CADTOK = "https://www.newswire.ca/news-releases/six-canadian-banks-explore-development-of-a-secure-cad-tokenized-deposit-solution-807746405.html"
BIZVISA = "https://www.newswire.ca/news-releases/scotiabank-launches-new-no-fee-visa-credit-card-for-canadian-business-owners-with-1-cash-back-on-every-purchase-818893878.html"
DIG0726 = "https://www.newswire.ca/news-releases/scotiabank-digital-banking-update-new-tools-to-make-everyday-banking-faster-simpler-and-more-secure-872686013.html"
DIG0426 = "https://www.newswire.ca/news-releases/scotiabank-digital-banking-update-latest-enhancements-include-more-ai-powered-personalization-and-fraud-prevention-features-830317233.html"
SHELL = "https://www.newswire.ca/news-releases/scotiabank-offers-clients-more-ways-to-earn-through-scene-with-shell-canada-838614790.html"
HISA = "https://www.newswire.ca/news-releases/scotiabank-launches-one-of-canada-s-first-relationship-based-high-interest-savings-accounts-859885999.html"
SI = "https://www.newswire.ca/news-releases/scotiabank-launches-scotia-intelligence-empowering-employees-and-accelerating-enterprise-ai-adoption-854931680.html"
SI2 = "https://www.newswire.ca/news-releases/scotiabank-accelerates-enterprise-adoption-of-ai-with-new-scotia-intelligence-capabilities-828555229.html"
LIGHT = "https://www.newswire.ca/news-releases/lightworks-scotiabank-sun-life-and-telus-launch-ai-consortium-to-jointly-build-critical-ai-control-infrastructure-in-canada-850767880.html"
CASA = "https://www.newswire.ca/news-releases/casa-and-scotiabank-team-up-to-offer-the-first-credit-card-in-canada-with-no-transaction-fees1-on-rent-payments-826481574.html"
USCM = "https://www.newswire.ca/news-releases/scotiabank-launches-modern-u-s-cash-management-platform-strengthening-north-american-corridor-capabilities-873992799.html"
EURO = "https://www.newswire.ca/news-releases/scotiabank-named-canada-s-best-transaction-bank-by-euromoney-853662840.html"
PRIV = "https://www.newswire.ca/news-releases/embark-on-a-world-of-luxury-scotiabank-introduces-the-scotiabank-passport-r-visa-infinite-privilege-card-856551746.html"
GROWTH = "https://www.newswire.ca/news-releases/scotiabank-launches-scotia-growth-institute-and-commits-over-100-billion-in-financing-to-support-canada-s-growth-agenda-875847121.html"
CC = "https://www.scotiabank.com/ca/en/personal/credit-cards.html"
SCENECARDS = "https://www.scotiabank.com/ca/en/personal/programs-services/sceneplus-rewards/cards.html"
BIZCC = "https://www.scotiabank.com/ca/en/business-banking/banking-solutions/credit-cards.html"
C2P = "https://www.scotiabank.com/ca/en/personal/ways-to-bank/debit-credit-card-purchases/click-to-pay.html"
TWE = "https://www.tangerine.ca/en/personal/spend/credit-cards/world-elite-mastercard"
TVD = "https://www.tangerine.ca/en/personal/spend/chequing-account/visa-debit-card"
TSHELL = "https://www.tangerine.ca/en/personal/spend/credit-cards/shell-benefits"
TSCENE = "https://dmn.ca/tangerine-joins-forces-with-scene-to-accelerate-everyday-rewards/"
TDH = "https://dailyhive.com/canada/new-tangerine-mastercard"
TWIKI = "https://en.wikipedia.org/wiki/Tangerine_Bank"
CHASE = "https://www.electronicpaymentsinternational.com/news/scotiabank-to-buy-jpmorgan-chases-canada-credit-card-portfolio-161015-4695010/"
MPASS = "https://finchannel.com/mastercard-and-scotiabank-team-up-to-bring-customers-scotiabank-masterpass/69439/american-business-trends/banks/2017/11/"
CARIBMC = "https://jamaicaobserver.com/2020/03/09/scotiabank-announces-strategic-initiative-with-mastercard-in-four-caribbean-markets"
VISA19 = "https://pa.scotiabank.com/content/dam/scotiabank/international/panama/spanish/Comunicado%20de%20Prensa%20Visa%20Scotiabank%20Alianza%20Centroam%C3%A9rica%20y%20el%20Caribe%20-%2020.12.2019.pdf"
JMDEBIT = "https://jm.scotiabank.com/personal/chequing-and-savings/debit-card.html"
JMAERO = "https://jm.scotiabank.com/personal/credit-cards/aero-platinum-mastercard.html"
FIFA = "https://jm.scotiabank.com/personal/credit-cards/terms-and-conditions/welcome-to-the-game-fifa-world-cup-2026.html"
PECC = "https://www.scotiabank.com.pe/Personas/tarjetas/credito"
PEDEB = "https://www.scotiabank.com.pe/Personas/tarjetas/debito"
PLIN = "https://www.scotiabank.com.pe/Personas/Canales-digitales/pagos/transferencias-interbancarias-plin"
MXCC = "https://www.scotiabank.com.mx/personas/tarjetas-de-credito.aspx"
MXAPPLE = "https://www.scotiabank.com.mx/servicios-bancarios/scotiamovil/apple-pay.aspx"
MXDIG = "https://www.scotiabank.com.mx/servicios-bancarios/scotiamovil/tarjeta-debito-digital.aspx"
CLCC = "https://www.scotiabankchile.cl/Personas/Tarjetas-de-Credito/Tarjetas-Scotiabank/tarjeta-mastercard-black"
CLDEB = "https://www.scotiabankchile.cl/Personas/tarjeta-debito"
RTR = "https://www.payments.ca/systems-services/payment-systems/real-time-rail-payment-system"
OPENBANK = "https://www.canada.ca/en/department-finance/programs/financial-sector-policy/open-banking-implementation/budget-2025-canadas-framework-for-consumer-driven-banking.html"
INTERAC = "https://www.interac.ca/en/about/our-company/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · charter · stakes", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: C$1.55 trillion of assets and a record Q3 with ROE back above 14%, a bank founded in Halifax in 1832, Scotia Intelligence for AI, a plan that moves capital to the North American corridor, and stakes in KeyCorp and Davivienda.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "C$1.55tn, ROE 14.1%.", "div": "bns", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Total assets of C$1,548 billion, loans of C$771 billion and deposits of C$1,006 billion at 31 July 2026; Q3 2026 revenue of C$10.5 billion and record net income of C$2,953 million (ROE 14.1%); CET1 13.1%; market value about C$150 billion; 81,734 staff. Fiscal 2025 net income was C$7,758 million reported, C$9,510 million adjusted.",
              s=["corp"], neo=[0, ""], src=[["Q3 2026 results", Q3], ["Q3 2026 fact sheet", FACT], ["2025 results", FY25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Charter & leadership", "blurb": "Thomson and Regent.", "div": "bns", "rev": "other", "products": [
            P("leadership", "Board & executive team", "Chair Aaron Regent, CEO Scott Thomson, CFO Raj Viswanathan; Aris Bogdaneris runs Canadian Banking, Francisco Aristeguieta International and Global Transaction Banking, Travis Machen Global Banking and Markets, Tim Clark technology and Phil Thomas strategy and operations (from December 2025). Former ING and UBS chief Ralph Hamers joined the board in September 2026.",
              s=["corp"], neo=[0, ""], src=[["Scotiabank: executive management", EXEC], ["Executive appointments, Nov 2025", APPTS], ["Ralph Hamers joins board, Sep 2026", HAMERS]]),
            P("brands", "Charter & brands", "The Bank of Nova Scotia, founded in Halifax in 1832, listed in Toronto and New York (BNS). Brands include Scotiabank, Tangerine (ING Direct Canada, bought in 2012 for C$3.1 billion), Scotia Wealth Management, Scotia iTRADE, Roynat and ScotiaConnect, and it runs Scene+ with its partners.",
              s=["con", "tang"], o="I", neo=[0, ""], src=[["Q3 2026 results", Q3], ["Wikipedia: Tangerine Bank", TWIKI]]),
        ]},
        {"id": "1.3", "ic": "brain", "name": "Technology & AI", "blurb": "Scotia Intelligence.", "div": "bns", "rev": "other", "products": [
            P("scotiaintel", "Scotia Intelligence & Navigator", "The bank's unified data and AI platform, launched April 2026: assistive AI for more than 71,000 staff, 5,500 engineers coding with AI, AI handling about 40% of contact-centre queries and routing about 90% of commercial emails, and AI-led credit-card pre-approval.",
              s=["corp"], st="new", ay="Apr 2026", neo=[0, ""], src=[["Scotia Intelligence launch, Apr 2026", SI], ["Scotia Intelligence expansion, Jun 2026", SI2], ["Q3 2026 presentation", PRES]]),
            P("aiconsortium", "AI Consortium with Lightworks", "A founding member, with Sun Life and TELUS, of an AI consortium building shared controls for agentic AI, starting with an 'Agentic Control Plane' already in production (July 2026).",
              s=["corp"], st="new", ay="Jul 2026", o="P", at="Lightworks, Sun Life, TELUS", neo=[0, ""],
              mc="Agentic AI is on the agenda; Agent Pay is untouched ground.",
              src=[["AI Consortium, Jul 2026", LIGHT]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & deals", "blurb": "The North American corridor.", "div": "bns", "rev": "other", "products": [
            P("strategy", "Investor Day plan", "Four pillars from the December 2023 Investor Day: grow in priority markets, earn primary clients, make it easy to bank, and win as one team. Targets are EPS growth of 7%+ and ROE of 14%+; Canadian Banking aims for about 24% ROE by 2028. ROE passed 14% in Q3 2026.",
              s=["corp"], neo=[0, ""], src=[["2025 results", FY25], ["Q3 2026 investor deck", MKT]]),
            P("deals", "Deals & disposals", "CrediScotia (Peru) sold to Santander (February 2025); MapleMark Bank in Dallas agreed (May 2026) ⚠ pending approval; a buy-out of Scotia Group Jamaica's minorities for about C$0.5 billion (June 2026) ⚠ due in Q4 2026; and Tangerine moving to Engine by Starling's cloud platform ⚠ no date.",
              s=["corp"], st="flux", o="A", neo=[0, ""], src=[["Q3 2026 results", Q3], ["MapleMark Bank, May 2026", MAPLE], ["Scotia Group Jamaica, Jun 2026", JAM], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "1.5", "ic": "network", "name": "Strategic stakes", "blurb": "KeyCorp 14.9%, Davivienda 20.3%.", "div": "stakes", "rev": "other", "products": [
            P("keycorp", "KeyCorp stake", "About 14.9% of KeyCorp for about US$2.8 billion, agreed August 2024 and completed 27 December 2024, with a board seat; worth C$4,987 million at 31 July 2026 and adding about C$82 million of earnings a quarter.",
              s=["corp"], ay="Dec 2024", o="A", at="KeyCorp", neo=[None, "KeyCorp's own card choices not researched."],
              src=[["KeyCorp investment completed, Dec 2024", KEY], ["Q3 2026 report", QR], ["Q3 2026 presentation", PRES]]),
            P("davivienda", "Davivienda Group stake", "Scotiabank's banks in Colombia, Costa Rica and Panama went to Davivienda on 1 December 2025 for a 20.3% stake (14.99% voting) and two board seats. The old operations trade as DAVIbank and Davivienda, and a referral deal keeps Scotiabank's corporate, wealth and markets clients.",
              s=["corp", "latam"], st="new", ay="Dec 2025", o="A", at="Davivienda", neo=[None, "Davivienda's networks not researched."],
              src=[["Davivienda deal agreed, Jan 2025", DAVI25], ["Davivienda deal closed, Dec 2025", DAVI], ["Q3 2026 report", QR]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: Scotiabank's Canadian credit cards on Visa and Amex, debit on Interac and Visa Debit, Tangerine's cards on Mastercard, Visa-led cards in Mexico and Chile, both networks in Peru and the Caribbean, Interac and PLIN for instant payments, and ScotiaConnect and tokenised deposits for business.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Scotiabank credit cards", "blurb": "Visa and Amex.", "div": "scotiaca", "rev": "canada", "products": [
            P("visacredit", "Scotiabank Visa cards", "Scene+ Visa, Passport Visa Infinite+, Passport Visa Infinite Privilege (launched with Visa Canada in March 2025), ScotiaGold Passport, Momentum and Value. Premium cards made 45% of new card sales in Q3 2026; cards are about 2% of Canadian Banking's C$475 billion of loans ⚠ derived.", short="Credit (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              mc="The main Scotiabank brand issues no Mastercard; Visa won the premium launch.",
              src=[["Scotiabank: credit cards", CC], ["Passport Visa Infinite Privilege, Mar 2025", PRIV], ["Q3 2026 presentation", PRES]]),
            P("amex", "Scotiabank American Express cards", "Scotiabank Gold American Express (Scene+), Platinum American Express and a no-fee Scotiabank American Express: one of few Canadian banks issuing Amex.",
              s=["con"], lc="borrow", o="P", at="American Express", neo=[0, "American Express."], src=[["Scotiabank: Scene+ cards", SCENECARDS]]),
            P("bizvisa", "Business Visa cards", "Scotia Momentum for business Visa, a new No Fee version with 1% cash back, Visa Spend Clarity and Visa SavingsEdge (24 August 2026), Passport Visa Infinite Business, ScotiaLine for business and Scotia Home Hardware PRO Visa. No commercial card programme is public ⚠.", short="Business (Visa)",
              s=["sme"], lc="borrow", st="new", ay="Aug 2026", o="P", at="Visa", neo=[0, "Visa."],
              mc="Commercial, virtual and purchasing cards are a visible gap.",
              src=[["No-fee business Visa, Aug 2026", BIZVISA], ["Scotiabank: business credit cards", BIZCC]]),
            P("legacymc", "Legacy Mastercard portfolio", "Bought from JPMorgan Chase Canada in October 2015: about C$1.7 billion of Mastercard and private-label receivables and 2 million accounts. A 'Credit agreement (Mastercard)' still appears on Scotiabank's site ⚠ how much remains is unknown.", short="Legacy Mastercard ⚠",
              s=["con"], lc="borrow", st="unconf", ay="Oct 2015", o="A", at="JPMorgan Chase", neo=[2, "Mastercard ⚠ size today."],
              src=[["EPI: JPMorgan Chase portfolio, Oct 2015", CHASE], ["Scotiabank: credit cards", CC]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Debit in Canada", "blurb": "Interac and Visa Debit.", "div": "scotiaca", "rev": "canada", "products": [
            P("debitca", "Scene+ ScotiaCard debit", "Debit cards on Interac with Visa Debit, earning 1 Scene+ point per C$5 spent, for more than 11 million Canadian Banking customers. Interac carries about 18.6 million transactions a day nationally.",
              s=["con"], lc="everyday", o="P", at="Interac, Visa", neo=[0, "Interac and Visa Debit."],
              src=[["Scotiabank: Scene+ cards", SCENECARDS], ["Interac: our company", INTERAC]]),
        ]},
        {"id": "2.3", "ic": "wallet", "name": "Tangerine cards", "blurb": "Mastercard's foothold.", "div": "tangerine", "rev": "canada", "products": [
            P("tangworldelite", "Tangerine Rewards World Elite Mastercard", "Tangerine's first paid card (C$120): Scene+ points with 1.5x in three chosen categories, DragonPass lounges and Mastercard Priceless, revealed on 22 April 2026 after Tangerine joined Scene+ (February 2026).", short="World Elite (Mastercard)",
              s=["tang"], lc="borrow", st="new", ay="Apr 2026", o="P", at="Mastercard, Scene+", neo=[2, "Mastercard World Elite."],
              mc="The first World Elite Mastercard in the group's Canadian range.",
              src=[["Tangerine: World Elite Mastercard", TWE], ["Daily Hive: new Tangerine Mastercard, Apr 2026", TDH], ["DMN: Tangerine joins Scene+, Feb 2026", TSCENE]]),
            P("tangmoneyback", "Tangerine Money-Back Mastercard", "No-fee cash-back cards (2% in up to three categories) on Mastercard since 2016, with a World Mastercard version, and up to 8 cents a litre at Shell.", short="Money-Back (Mastercard)",
              s=["tang"], lc="borrow", ay="2016", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["Tangerine: Shell benefits", TSHELL], ["Wikipedia: Tangerine Bank", TWIKI]]),
            P("tangdebit", "Tangerine Client Card with Visa Debit", "Debit for the No-Fee Daily Chequing Account, on Interac and Visa Debit, with Apple Pay, Google Pay and Samsung Pay and access to 3,500+ Scotiabank ABMs.",
              s=["tang"], lc="everyday", o="P", at="Interac, Visa", neo=[0, "Interac and Visa Debit."], src=[["Tangerine: Visa Debit", TVD]]),
        ]},
        {"id": "2.4", "ic": "globe", "name": "Cards in Mexico", "blurb": "Visa-led, World Elite on top.", "div": "mexico", "rev": "intl", "products": [
            P("mexicocards", "Scotiabank Mexico cards", "Singular Infinite and Signature, Scotia Travel, IDEAL and Scotia Básica credit cards and Débito Visa Signature debit, all on Visa. Scotia Travel, Singular and AAdvantage World Elite cards sit on Mastercard's World Elite tier ⚠ inferred. A virtual debit card has a dynamic CVV.", short="Mexico (Visa-led)",
              s=["latam"], lc="borrow", o="P", at="Visa, Mastercard ⚠", neo=[1, "Visa-led; World Elite tier ⚠."],
              mc="Mexico is Scotiabank's fourth-ranked market and the core of the corridor.",
              src=[["Scotiabank Mexico: credit cards", MXCC], ["Scotiabank Mexico: Apple Pay", MXAPPLE], ["Scotiabank Mexico: digital debit", MXDIG]]),
        ]},
        {"id": "2.5", "ic": "earth", "name": "Cards in Peru & Chile", "blurb": "Peru dual, Chile Visa.", "div": "andean", "rev": "intl", "products": [
            P("perucards", "Scotiabank Peru cards", "Full Visa and Mastercard ranges in credit, from Clásica to Infinite and Black, including AAdvantage co-brands on both networks, and Mastercard and Visa debit.", short="Peru (Visa & Mastercard)",
              s=["latam"], lc="borrow", o="P", at="Visa, Mastercard, American Airlines", neo=[1, "Visa and Mastercard."],
              src=[["Scotiabank Peru: credit cards", PECC], ["Scotiabank Peru: debit", PEDEB]]),
            P("chilecards", "Scotiabank Chile cards", "Visa Singular Infinite and Signature, Visa Signature, Visa Gold and Visa Wealth Management, and Visa debit. The Mastercard Black page now shows the Visa range ⚠.", short="Chile (Visa)",
              s=["latam"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Scotiabank Chile: credit cards", CLCC], ["Scotiabank Chile: debit", CLDEB]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Cards in the Caribbean", "blurb": "Mastercard debit since 2020.", "div": "caribbean", "rev": "intl", "products": [
            P("caribdebit", "ScotiaCard Mastercard Debit", "A seven-year deal of March 2020 put debit cards in the Bahamas, Barbados, the Dominican Republic and Jamaica on Mastercard, with e-commerce, wallets, a rewards platform and lifecycle management. It runs to about March 2027 ⚠.", short="Debit (Mastercard)",
              s=["latam"], lc="everyday", ay="Mar 2020", o="P", at="Mastercard", neo=[2, "Mastercard Debit."],
              mc="The term is up around 2027, with Scotiabank taking full control of Scotia Group Jamaica.",
              src=[["Jamaica Observer: Mastercard deal, Mar 2020", CARIBMC], ["Scotiabank Jamaica: debit", JMDEBIT]]),
            P("caribcredit", "Caribbean credit cards", "Visa (a seven-year Central America and Caribbean deal from December 2019, and FIFA World Cup 2026 promotions) alongside Mastercard ranges in Jamaica such as AERO Platinum, Gold and Magna Mastercard.", short="Credit (Visa & Mastercard)",
              s=["latam"], lc="borrow", ay="Dec 2019", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard."],
              src=[["Visa–Scotiabank deal, Dec 2019", VISA19], ["Scotiabank Jamaica: AERO Platinum Mastercard", JMAERO], ["Scotiabank Jamaica: FIFA 2026 promotion", FIFA]]),
        ]},
        {"id": "2.7", "ic": "zap", "name": "Real-time & wallets", "blurb": "Interac, PLIN, tokens.", "div": "scotiaca", "rev": "canada", "products": [
            P("interac", "Interac e-Transfer & the Real-Time Rail", "Interac e-Transfer and debit in Canada, with AI prompts for routine transfers; Canada's Real-Time Rail is due in Q4 2026 and consumer-driven banking is legislated.",
              s=["con", "sme"], lc="move", o="P", at="Interac, Payments Canada", neo=[0, "Interac."],
              mc="Real-time account payments bring scam risk that Mastercard's tools address.",
              src=[["Digital update, Jul 2026", DIG0726], ["Payments Canada: Real-Time Rail", RTR], ["Finance Canada: consumer-driven banking", OPENBANK]]),
            P("plin", "PLIN (Peru)", "Scotiabank Peru's instant wallet: up to S/500 a transfer, interoperable with Yape and other banks, and QR payments at Niubiz and Izipay terminals.",
              s=["latam"], lc="move", o="P", at="PLIN", neo=[0, "Bank-run A2A."], src=[["Scotiabank Peru: PLIN", PLIN]]),
            P("wallets", "Mobile wallets & Click to Pay", "Apple Pay, Google Pay and Samsung Pay; new Visa credit cards pushed straight into wallets (April and July 2026); a wallets ecosystem across International Banking (2025); Click to Pay explained for Visa and Amex. Masterpass was launched with Mastercard in November 2017.",
              s=["con", "tang", "latam"], lc="everyday", st="new", o="P", at="Apple, Google, Visa", neo=[1, "Tokens on each network ⚠."],
              src=[["Digital update, Apr 2026", DIG0426], ["Digital update, Jul 2026", DIG0726], ["Scotiabank: Click to Pay", C2P], ["FinChannel: Scotiabank Masterpass, Nov 2017", MPASS]]),
        ]},
        {"id": "2.8", "ic": "arrow-left-right", "name": "Treasury & digital money", "blurb": "ScotiaConnect, tokens.", "div": "gtb", "rev": "gbm", "products": [
            P("scotiaconnect", "ScotiaConnect & Global Transaction Banking", "A cloud treasury platform with US cash management launched in October 2025 (ACH, wires, host-to-host), live in Mexico, Scotia TranXact APIs and ERP links; Euromoney's best transaction bank in Canada (2025).",
              s=["sme", "corp"], lc="move", st="new", ay="Oct 2025", neo=[0, ""],
              mc="B2B card and virtual-card flows are absent from the corridor offer.",
              src=[["US cash management, Oct 2025", USCM], ["Euromoney award, Nov 2025", EURO]]),
            P("digitalmoney", "Tokenised deposits & Project Agorá", "One of six Canadian banks exploring a CAD tokenised deposit (September 2026), and a member of the BIS–IIF Project Agorá after live testing in July 2026.",
              s=["corp"], lc="move", st="new", ay="Sep 2026", o="P", at="Canadian banks, BIS, IIF", neo=[0, "Bank-led tokens."],
              src=[["CAD tokenised deposits, Sep 2026", CADTOK], ["Project Agorá, Sep 2026", AGORA]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: in-app scam alerts and real-time fraud flags, newcomer onboarding with Nova Credit, AI payment prompts, and Scene+, a 15-million-member loyalty programme now joined by Tangerine and Shell.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "Scam alerts in the app.", "div": "scotiaca", "rev": "canada", "products": [
            P("fraud", "Fraud & scam protection", "In-app warnings during phone calls, real-time flags on unusual transactions, in-app fraud reporting with merchant names and locations, behavioural biometrics across International Banking, and AI-assisted AML.",
              s=["con", "latam"], lc="everyday", st="new", neo=[0, "Scotiabank's own."],
              mc="Real-time payment fraud scoring fits the Real-Time Rail launch.",
              src=[["Digital update, Apr 2026", DIG0426], ["Digital update, Jul 2026", DIG0726], ["2025 Annual Report", AR25]]),
            P("onboarding", "Digital onboarding", "The first Canadian bank to fully integrate Nova Credit into digital onboarding for newcomers (2025), and digital-first account opening in Mexico.",
              s=["con", "latam"], lc="open", o="P", at="Nova Credit", neo=[0, ""], src=[["2025 Annual Report", AR25], ["Q3 2026 presentation", PRES]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI for clients", "blurb": "Predictive prompts.", "div": "scotiaca", "rev": "canada", "products": [
            P("predictive", "Predictive UX & AI chatbots", "Patented AI prompts for upcoming bills, routine e-Transfers and transfers, AI chatbots and personalised offers, and digital bill-payment receipts (about 30 million issued).",
              s=["con"], lc="everyday", st="new", neo=[0, ""],
              mc="Agent Pay could give these prompts a way to pay.",
              src=[["Digital update, Apr 2026", DIG0426], ["Q3 2026 presentation", PRES]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Scene+", "blurb": "15 million members.", "div": "scotiaca", "rev": "canada", "products": [
            P("sceneplus", "Scene+", "A loyalty programme with more than 15 million members: Sobeys, Safeway, IGA and FreshCo, Cineplex, Home Hardware, Scene+ Travel by Expedia, and Tangerine from 2026. It lifted Scotia payment products to 26% of members in 2025, and the bank aims to 'harness the full potential of Scene+'.",
              s=["con", "tang"], lc="grow", o="P", at="Empire, Cineplex", neo=[1, "Network-neutral; earned on Visa, Amex and Mastercard."],
              mc="Card-linked offers and merchant data could deepen Scene+.",
              src=[["Scotiabank: Scene+ cards", SCENECARDS], ["Casa partnership, Mar 2026", CASA], ["2025 Annual Report", AR25]]),
            P("shell", "Scene+ at Shell", "Up to 10 cents a litre in value at more than 1,400 Shell stations by linking a Scotiabank or Tangerine debit or credit card to Shell Go+ (26 May 2026).",
              s=["con", "tang", "sme"], lc="grow", st="new", ay="May 2026", o="P", at="Shell Canada", neo=[1, "All networks, including Tangerine Mastercard."],
              src=[["Scene+ with Shell, May 2026", SHELL], ["Tangerine: Shell benefits", TSHELL]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What clients buy: mortgages and savings in Canada, business banking, International Banking in Mexico, Peru, Chile and the Caribbean, wealth management with C$474 billion of assets, and corporate and investment banking across the Americas.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Mortgages & savings", "blurb": "Mortgage+ and the HISA.", "div": "scotiaca", "rev": "canada", "products": [
            P("mortgages", "Mortgages & Mortgage+", "Mortgages are 62% of Canadian Banking's C$475 billion of loans; the Mortgage+ bundle (rate, day-to-day account, card) is on 90% of new originations, and 30% of new Mortgage+ clients open a Scotiabank credit card.",
              s=["con"], lc="borrow", neo=[0, "Visa cards in the bundle."], src=[["2025 Annual Report", AR25], ["Q3 2026 investor deck", MKT]]),
            P("hisa", "Scotia HISA", "One of Canada's first relationship-priced savings accounts (1 May 2026), with five tiers from 0.75% to 2.20% based on total balances.",
              s=["con"], lc="grow", st="new", ay="May 2026", neo=[0, ""], src=[["Scotia HISA, May 2026", HISA]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Business banking", "blurb": "27% of Canadian revenue.", "div": "scotiaca", "rev": "canada", "products": [
            P("bizbanking", "Small business & commercial banking", "Small business, commercial and Roynat, 27% of Canadian Banking revenue, with cash management, payroll and a service for accountants (February 2026).",
              s=["sme"], lc="everyday", neo=[0, "Visa business cards."],
              mc="Commercial and virtual cards for mid-market clients are an open lane.",
              src=[["Q3 2026 investor deck", MKT], ["Scotiabank: business credit cards", BIZCC]]),
        ]},
        {"id": "4.3", "ic": "earth", "name": "International Banking", "blurb": "Fourth in Mexico, Peru, Chile.", "div": "bns", "rev": "intl", "products": [
            P("intl", "International Banking", "More than 8 million clients in over 12 countries, including Mexico, Peru, Chile, Uruguay, Brazil and the Caribbean; fourth by share in Mexico, Peru and Chile; Q3 2026 earnings C$725 million (ROE 15.7%); primary clients up 10%.",
              s=["latam"], lc="everyday", neo=[1, "Peru and the Caribbean issue Mastercard."],
              src=[["Q3 2026 fact sheet", FACT], ["Q3 2026 investor deck", MKT], ["Q3 2026 presentation", PRES]]),
        ]},
        {"id": "4.4", "ic": "gem", "name": "Wealth", "blurb": "C$474bn AUM.", "div": "bns", "rev": "gwm", "products": [
            P("wealth", "Global Wealth Management", "Scotia Wealth Management, Scotia iTRADE and 1832 Asset Management for more than 2 million clients in nine countries: assets under management of C$474 billion, record Q3 2026 earnings of C$515 million.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["Q3 2026 results", Q3], ["Q3 2026 fact sheet", FACT]]),
        ]},
        {"id": "4.5", "ic": "chart-candlestick", "name": "Global Banking & Markets", "blurb": "Record Q3.", "div": "bns", "rev": "gbm", "products": [
            P("gbm", "Global Banking and Markets", "Corporate and investment banking across the Americas: record Q3 2026 earnings of C$647 million, up 37%, and ninth-largest foreign bank in the US.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Q3 2026 results", Q3], ["Q3 2026 investor deck", MKT]]),
            P("maplemark", "MapleMark Bank", "A Dallas commercial bank being bought (agreed 29 May 2026) to offer FDIC-insured deposits for Mortgage Capital Markets and US deposit growth ⚠ closing pending.",
              s=["corp"], lc="grow", st="new", ay="May 2026", o="A", at="Maple Financial Holdings", neo=[0, ""], src=[["MapleMark Bank, May 2026", MAPLE]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How clients reach the bank: the Scotia app and international apps with about 9 million active mobile users, 1,984 branches and offices, and partners such as Casa and Scene+ merchants.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Digital banking", "blurb": "40% of Canadian sales.", "div": "scotiaca", "rev": "canada", "products": [
            P("app", "Scotia app (Canada)", "4.8 million active mobile users and 5.3 million active digital users; digital channels made 40% of Canadian retail sales in Q3 2026.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["Q3 2026 presentation", PRES]]),
            P("intlapp", "International apps", "ScotiaMóvil and the Peru, Chile and Caribbean apps: 4.0 million active mobile users and 49.5% digital sales, with 23% of clients acquired digitally in 2025.",
              s=["latam"], lc="open", neo=[0, ""], src=[["Q3 2026 presentation", PRES], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & ABMs", "blurb": "871 in Canada.", "div": "scotiaca", "rev": "canada", "products": [
            P("branches", "Branches & ABMs", "871 branches and 3,493 ABMs in Canada; 1,984 branches and offices and 7,478 ABMs in all; 44,000 ABMs through the Global ATM Alliance.",
              s=["con", "latam"], lc="open", neo=[0, ""], src=[["Q3 2026 fact sheet", FACT], ["Q3 2026 investor deck", MKT], ["Tangerine: Visa Debit", TVD]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Partners", "blurb": "Casa, Scene+, dealers.", "div": "scotiaca", "rev": "canada", "products": [
            P("partners", "Partners & platforms", "Casa for rent and condo-fee payments on ScotiaGold Passport Visa with no fee (March 2026; more than 500,000 units), Scene+ merchants, auto dealers and mortgage brokers.",
              s=["con"], lc="beyond", st="new", o="P", at="Casa", neo=[0, "Casa takes Visa and Mastercard; the no-fee card is Visa."],
              src=[["Casa partnership, Mar 2026", CASA]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Scotiabank", "blurb": "Tangerine and the Caribbean.", "products": [
        P("mcatbns", "Mastercard at Scotiabank", "Scotiabank's Canadian brand runs on Visa and Amex, with debit on Interac and Visa Debit. Mastercard carries Tangerine's credit cards, including a new World Elite card (April 2026), Caribbean debit under a 2020 seven-year deal, half of Peru's range and a World Elite tier in Mexico ⚠. Visa took the 2019 Caribbean credit deal and the 2025 and 2026 Canadian launches.",
          s=["con"], div="bns", rev="other", mc="The relationship this map is drawn for.",
          src=[["Tangerine: World Elite Mastercard", TWE], ["Jamaica Observer: Mastercard deal, Mar 2020", CARIBMC], ["Scotiabank: credit cards", CC]]),
    ]},
    {"id": "pillar-market", "name": "Markets & regulation", "blurb": "RTR, open banking, tokens.", "products": [
        P("market", "Canada and the corridor", "Canada's Real-Time Rail (Q4 2026), consumer-driven banking under the Bank of Canada, a six-bank CAD tokenised deposit, Interac's hold on debit, and fourth-place franchises in Mexico, Peru and Chile.",
          s=["con"], div="bns", rev="other", src=[["Payments Canada: Real-Time Rail", RTR], ["Finance Canada: consumer-driven banking", OPENBANK], ["Q3 2026 investor deck", MKT]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
