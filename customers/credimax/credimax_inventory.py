"""CrediMax's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

CrediMax publishes no stand-alone accounts, so figures come from its own website, card pages and 2024
ESG report, BBK's 2025 annual report and results, Bahraini press and BENEFIT. ``neo`` is the Mastercard
lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

HOME = "https://credimax.com.bh/"
ABOUT = "https://credimax.com.bh/about-credimax/"
CREDIT = "https://credimax.com.bh/credit-cards/"
PREPAID = "https://credimax.com.bh/prepaid-cards/"
SHARIA = "https://credimax.com.bh/sharia-compliant-cards/"
YOUTH = "https://credimax.com.bh/youth-cards/"
CORP = "https://credimax.com.bh/corprate-cards/"
GATEWAY = "https://credimax.com.bh/payment-gateway/"
POS = "https://credimax.com.bh/pos-machines/"
THAMEEN = "https://credimax.com.bh/thameen-loyalty/"
HSBC = "https://credimax.com.bh/hsbc-transition/"
FEES = "https://credimax.com.bh/wp-content/uploads/2025/11/3888-CrediMax-Updated-Fees-Guide-A4-Credit-Cards-V30.pdf"
TAYSEER = "https://credimax.com.bh/wp-content/uploads/2026/08/4166-CrediMax-Tayseer-Terms-Conditions-Final-30.7.2026.pdf"
ESG = "https://credimax.com.bh/credimax-esg-sustainability-report-ye-2024/"
APPLEPAY = "https://credimax.com.bh/en/applepay"
MAXWALLET = "https://credimax.com.bh/en/MaxWallet"
MCRENEW = "https://credimax.com.bh/news/credimax-and-mastercard-sign-strategic-partnership-agreement-to-drive-digital-innovation-in-bahrain/"
C2P = "https://credimax.com.bh/news/credimax-and-mastercard-team-up-to-introduce-click-to-pay-in-bahrain/"
GCCC2P = "https://www.gccbusinessnews.com/credimax-mastercard-unite/"
AWARD = "https://credimax.com.bh/news/mastercard-leader-in-spend-on-premium-credit-cards-award/"
TALABAT = "https://techafricanews.com/2026/05/12/credimax-talabat-and-mastercard-strengthen-digital-payments-push-with-new-credit-card/"
VCP = "https://www.zawya.com/en/business/fintech/credimax-introduces-visa-commercial-pay-in-bahrain-b4j46262"
ONEAPP = "https://www.newsofbahrain.com/en/article/one-app-signs-strategic-partnership-with-credimax"
BNPLMOU = "https://credimax.com.bh/news/credimax-and-benefit-company-signs-memorandum-of-understanding-agreement-to-explore-bnpl-best-practice-framework/"
BAPCO = "https://credimax.com.bh/news/bapco-tazweed-x-credimax-strategic-partnership-agreement/"
BATELCO = "https://www.batelco.com/business/bbk-and-credimax-forge-strategic-partnership-with-batelco-to-elevate-customer-experience/"
FAWATEER = "https://credimax.com.bh/news/credimax-now-available-on-fawateer-offering-customers-one-more-channel-to-pay-their-bills/"
QATAR = "https://credimax.com.bh/news/credimax-partners-with-qatar-airways-to-offer-discounts-to-cardholders/"
BBKAR = "https://www.bbkonline.com/wp-content/uploads/2026/04/BBK-2025-Annual-Report-English-Spread.pdf"
BBKH1 = "https://www.bbkonline.com/bbk-discloses-its-financial-results-for-the-half-year-ended-30th-june-2026/"
BBKFY = "https://www.gdnonline.com/Details/1376977"
BBKSUBS = "https://www.bbkonline.com/subsidiaries/"
MERGER = "https://bahrainbourse.com/NewAttachments/21072026074510/21072026074510_File1.pdf"
MERGERAGBI = "https://agbi.com/banking-finance/2026/04/bahraini-banks-prepare-to-discuss-key-merger-terms"
BENEFITH1 = "https://www.gdnonline.com/Details/1405074/Digital-payments-hit-BD193bn-in-H1"
MCBENEFIT = "https://financialit.net/news/payments/mastercard-partners-benefit-company-drive-payment-innovation-and-financial-inclusion"
CBBOB = "https://www.cbb.gov.bh/open-banking/"
APPLEBH = "https://9to5mac.com/2021/10/05/apple-pay-arrives-in-bahrain-with-support-from-major-banks/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "owner · licence · heritage", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: wholly owned by BBK, a Central Bank of Bahrain financing-company licence, Bahrain's first credit card in 1991, 109 staff, its own processing arm, the HSBC card book and a parent in merger talks with NBB.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Ownership & heritage", "blurb": "100% BBK; first card 1991.", "div": "bbk", "rev": "company", "products": [
            P("owner", "BBK ownership & licence", "CrediMax B.S.C. (c) is 100% owned by BBK (10 million shares) and licensed by the Central Bank of Bahrain as a financing company; its total capital ratio was 62.2% at end-2025. It publishes no stand-alone accounts or rating ⚠.",
              s=["con"], o="I", neo=[0, ""], src=[["BBK annual report 2025", BBKAR], ["CrediMax: about", ABOUT]]),
            P("heritage", "Heritage", "Started in July 1991 as BBK's card unit, which issued Bahrain's first credit card; an independent subsidiary since April 1999, based in Seef with desks in BBK's Financial Malls.",
              s=["con"], o="I", ay="Jul 1991", neo=[0, ""], src=[["BBK: subsidiaries", BBKSUBS], ["CrediMax: about", ABOUT]]),
            P("bbkgroup", "BBK Group", "The parent made a record BD80 million net profit in 2025 and BD42.5 million in H1 2026 (+10.1%), with total assets of BD4.9 billion; card income sits in its Retail segment (segment result BD25.1 million in 2025).",
              s=["con"], neo=[0, ""], src=[["BBK H1 2026 results", BBKH1], ["GDN: BBK 2025 results, Feb 2026", BBKFY], ["BBK annual report 2025", BBKAR]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Alsharifi chairs; Seyadi runs it.", "div": "credimax", "rev": "company", "products": [
            P("leadership", "Board & management", "Chairman Yaser Alsharifi (also BBK Group Chief Executive); Chief Executive Ahmed A. Seyadi (named in May 2026; not listed on the About page ⚠); CFO Yasser Shaaban; Chief Technology and Transformation Officer Nada Mohamed A.Rahman. About 109 full-time staff at end-2024, 99.9% Bahraini.",
              s=["corp"], neo=[0, ""], src=[["CrediMax: about", ABOUT], ["CrediMax ESG report 2024", ESG], ["TechAfrica News: talabat card, May 2026", TALABAT]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Processing & technology", "blurb": "Global Payment Services, 973Labs.", "div": "gps", "rev": "company", "products": [
            P("gps", "Global Payment Services & 973Labs", "Global Payment Services W.L.L. (70% via CrediMax, since 2005) provides card processing and back-up services; 973Labs (60% CrediMax, 40% Invita, 2022) does computer consultancy. The app is built by Avanza.",
              s=["corp"], o="B", neo=[None, "Core card processor not named ⚠."], src=[["BBK annual report 2025", BBKAR], ["CrediMax: home", HOME]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & deals", "blurb": "HSBC cards in; NBB talks.", "div": "bbk", "rev": "company", "products": [
            P("strategy", "Strategy", "BBK says CrediMax 'reinforced its position as a leading payments platform' in 2025, with a new app and partnerships in telecoms, logistics and premium lifestyle; no public targets or AI plan ⚠.",
              s=["corp"], neo=[1, "Partners with both Mastercard and Visa."], src=[["BBK annual report 2025", BBKAR]]),
            P("hsbc", "HSBC card transition", "BBK bought HSBC Bahrain's retail business (about 75,000 customers); HSBC credit cards were replaced by CrediMax cards from 28 November 2025, with limits, balances and rewards carried over.",
              s=["con", "prem"], o="A", st="new", ay="Nov 2025", at="HSBC", neo=[None, "Networks of the replacement cards not stated ⚠."],
              mc="A one-off reissue of a premium expatriate book.",
              src=[["CrediMax: HSBC transition", HSBC], ["BBK annual report 2025", BBKAR]]),
            P("merger", "BBK–NBB merger talks", "BBK and National Bank of Bahrain signed a merger MoU in November 2025; NBB proposed key terms on 26 April 2026 and BBK said on 21 July 2026 that discussions continue. No completion date ⚠.",
              s=["corp"], st="flux", neo=[None, "Would bring NBB's cards alongside ⚠."],
              mc="A merged card book would likely reopen network choice.",
              src=[["Bahrain Bourse: BBK disclosure, 21 Jul 2026", MERGER], ["AGBI: merger terms, Apr 2026", MERGERAGBI]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: a credit range split almost evenly between Mastercard and Visa, Visa Islamic cards, prepaid and youth cards on both, corporate cards and Visa Commercial Pay, Bahrain's main acquiring business with Click to Pay on Mastercard Gateway, instalments and BNPL at the till, and Apple Pay.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Mastercard credit", "blurb": "World Elite to talabat.", "div": "credimax", "rev": "issuing", "products": [
            P("mccredit", "World Elite, World & Platinum Mastercard", "Seven of CrediMax's fourteen credit cards are Mastercard: World Elite (Careem airport rides, Royal Lounge), World and World Premier, Platinum and Platinum Advance. Mastercard named CrediMax 'Leader in spend on Premium Credit Cards' in May 2024.", short="Premium credit (Mastercard)",
              s=["con", "prem"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard cards."],
              src=[["CrediMax: credit cards", CREDIT], ["CrediMax: Mastercard award, May 2024", AWARD]]),
            P("talabat", "talabat Credit Card", "A co-brand with talabat launched in May 2026 on Mastercard with Platinum benefits: 30% cashback on talabat orders, up to 1% elsewhere, no annual fee while active, and a BD30 welcome bonus.", short="talabat (Mastercard)",
              s=["con"], lc="borrow", st="new", ay="May 2026", o="P", at="talabat, Mastercard", neo=[2, "Mastercard co-brand."],
              mc="The newest co-brand went to Mastercard.",
              src=[["TechAfrica News: talabat card, May 2026", TALABAT], ["CrediMax: credit cards", CREDIT]]),
            P("danat", "Danat Card", "A co-brand with LuLu Hypermarket on Mastercard, with LuLu cashback rewards and an extended grace period.",
              s=["con"], lc="borrow", o="P", at="LuLu Hypermarket", neo=[2, "Mastercard co-brand."], src=[["CrediMax: credit cards", CREDIT]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Visa & JCB credit", "blurb": "Infinite, Signature, JCB.", "div": "credimax", "rev": "issuing", "products": [
            P("visacredit", "Infinite, Signature & Platinum Visa", "Six of the fourteen credit cards are Visa: Infinite, Signature, Signature Premier, Platinum, Platinum Advance and Platinum Cashback. Interest runs 1.85–2.75% a month; foreign spend costs 2.75–3.3%.", short="Premium credit (Visa)",
              s=["con", "prem"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["CrediMax: credit cards", CREDIT], ["CrediMax: fees guide, Nov 2025", FEES]]),
            P("jcb", "JCB Card", "A JCB gold card with offers in Japan and Thameen points.",
              s=["con"], lc="borrow", o="P", at="JCB", neo=[0, "JCB."], src=[["CrediMax: credit cards", CREDIT]]),
        ]},
        {"id": "2.3", "ic": "scroll-text", "name": "Islamic cards", "blurb": "Tayseer on Visa.", "div": "tayseer", "rev": "issuing", "products": [
            P("tayseer", "Tayseer", "Sharia-compliant charge cards in Platinum, Signature and Infinite, shown on Visa, paid in full within a 25-day grace period for a fixed monthly service fee; terms revised on 30 July 2026 (they refer to both schemes ⚠).", short="Tayseer (Visa)",
              s=["con", "prem"], lc="borrow", st="new", o="B", at="Visa", neo=[0, "Visa."], src=[["CrediMax: Sharia-compliant cards", SHARIA], ["CrediMax: Tayseer terms, Jul 2026", TAYSEER]]),
        ]},
        {"id": "2.4", "ic": "graduation-cap", "name": "Prepaid & youth", "blurb": "Cardy, iLead, Student.", "div": "credimax", "rev": "issuing", "products": [
            P("cardy", "Cardy prepaid", "CrediMax's first reloadable prepaid card, on Mastercard, with dining and merchant offers.",
              s=["con", "young"], lc="everyday", o="B", at="Mastercard", neo=[2, "Mastercard prepaid."], src=[["CrediMax: prepaid cards", PREPAID]]),
            P("cardyex", "Cardy EX & Gift Card", "Cardy EX is a Visa multi-currency card holding dinars, dollars, sterling, euros, riyals and dirhams; the Visa Gift Card is sold in bulk to companies.",
              s=["con"], lc="move", o="B", at="Visa", neo=[0, "Visa."], src=[["CrediMax: prepaid cards", PREPAID]]),
            P("ilead", "iLead", "A Mastercard for children aged 7 and over, guaranteed by a parent, with a parent and child dashboard, goals and tasks in the app.",
              s=["young"], lc="open", o="B", at="Mastercard", neo=[2, "Mastercard card."], src=[["CrediMax: youth cards", YOUTH]]),
            P("student", "Student Card", "A Visa credit card for university students with no annual fee, zero interest and 5% monthly repayments.",
              s=["young"], lc="borrow", o="B", at="Visa", neo=[0, "Visa."], src=[["CrediMax: youth cards", YOUTH]]),
        ]},
        {"id": "2.5", "ic": "briefcase-business", "name": "Corporate cards", "blurb": "Both networks; Visa virtual.", "div": "credimax", "rev": "corporate", "products": [
            P("mccorp", "Mastercard Corporate & World Business", "Mastercard Corporate and World Business cards with hotel bookings, corporate liability waiver insurance and lounges; per-card limits and online statements.",
              s=["corp"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard cards."], src=[["CrediMax: corporate cards", CORP]]),
            P("visacorp", "Visa Corporate & Signature Business", "Visa Corporate (no annual fee, cashback) and Signature Business with Google Workspace and Zendesk offers.",
              s=["corp"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["CrediMax: corporate cards", CORP]]),
            P("vcp", "Visa Commercial Pay", "A virtual corporate-card platform with instant issuance and real-time tracking, which CrediMax says it was first in Bahrain to offer (2025 ⚠).",
              s=["corp"], lc="move", st="new", ay="2025 ⚠", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa took the virtual-card slot.",
              src=[["Zawya: Visa Commercial Pay", VCP]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acquiring", "blurb": "POS, gateway, Click to Pay.", "div": "credimax", "rev": "acquiring", "products": [
            P("pos", "POS terminals", "Smart, mobile and counter-top terminals and the Invo Pro cash register; 200 paperless MINI POS units and SMS receipts under 'GO Green'. No merchant or terminal count is published ⚠.",
              s=["merch"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["CrediMax: POS machines", POS], ["CrediMax ESG report 2024", ESG]]),
            P("gateway", "Payment gateway", "Online acceptance of Mastercard, Visa, Amex, Discover, Diners, JCB, BENEFIT debit and mada, with Apple Pay, Google Pay, Samsung Pay, tokenisation, recurring payments and DCC, integrated by Hosted Session or Hosted Checkout (Mastercard Gateway ⚠ inferred).",
              s=["merch"], lc="move", o="P", at="Mastercard Gateway ⚠", neo=[3, "Mastercard Gateway ⚠ inferred."], src=[["CrediMax: payment gateway", GATEWAY], ["CrediMax: Click to Pay, 2024", C2P]]),
            P("c2p", "Click to Pay", "First in Bahrain to offer Click to Pay, via Mastercard Gateway (April–May 2024), with tokenisation; announced by Ahmed Seyadi and Mastercard's Maria Medvedeva.",
              s=["con", "merch"], lc="move", ay="May 2024", o="P", at="Mastercard", neo=[3, "Mastercard's Click to Pay."],
              src=[["CrediMax: Click to Pay, 2024", C2P], ["GCC Business News, May 2024", GCCC2P]]),
            P("fuel", "Fuel-station acceptance", "Card and BENEFIT acceptance at every Bapco Tazweed petrol station (April 2023).",
              s=["merch", "con"], lc="move", ay="Apr 2023", o="P", at="Bapco Tazweed", neo=[1, "Every network and BENEFIT."], src=[["CrediMax: Bapco Tazweed, Apr 2023", BAPCO]]),
        ]},
        {"id": "2.7", "ic": "hand-coins", "name": "Instalments & BNPL", "blurb": "At the till; ONE App.", "div": "credimax", "rev": "acquiring", "products": [
            P("instal", "Easy instalments & Flexi plans", "Merchants let CrediMax cardholders split purchases into monthly payments on the POS; Flexi Instalment Plans on premium cards; instalments on Batelco products planned ⚠.",
              s=["con", "merch"], lc="borrow", o="B", neo=[1, "CrediMax's own, on both networks."],
              mc="Room for Mastercard Installments across issuers.",
              src=[["CrediMax: POS machines", POS], ["CrediMax: credit cards", CREDIT]]),
            P("bnpl", "BNPL with ONE App", "ONE App, powered by Al Salam Bank, offers buy now, pay later on CrediMax's POS and digital channels with no new integration (11 October 2026); CrediMax and BENEFIT studied a national BNPL framework in 2023.",
              s=["con", "merch"], lc="borrow", st="new", ay="Oct 2026", o="P", at="ONE App (Al Salam Bank)", neo=[0, "ONE App's own BNPL."],
              src=[["News of Bahrain: ONE App, Oct 2026", ONEAPP], ["CrediMax: BENEFIT BNPL MoU, Feb 2023", BNPLMOU]]),
        ]},
        {"id": "2.8", "ic": "wallet", "name": "Wallets", "blurb": "Apple Pay, MaxWallet.", "div": "credimax", "rev": "issuing", "products": [
            P("applepay", "Apple Pay", "Cards are added to Apple Wallet from the CrediMax app; Apple Pay arrived in Bahrain in October 2021. Google Pay and Samsung Pay for CrediMax cards are not confirmed ⚠.",
              s=["con"], lc="everyday", o="P", at="Apple", neo=[1, "Mastercard and Visa tokens."], src=[["CrediMax: Apple Pay", APPLEPAY], ["9to5Mac: Apple Pay in Bahrain, Oct 2021", APPLEBH]]),
            P("maxwallet", "MaxWallet", "CrediMax's own QR wallet for Visa and Mastercard credit cardholders (launch date unknown ⚠).",
              s=["con"], lc="everyday", o="B", neo=[1, "Visa and Mastercard cards."], src=[["CrediMax: MaxWallet", MAXWALLET]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every card: fraud and data-security controls with a Mastercard cyber workshop, automated scoring and digital onboarding, Thameen points convertible to about ten airline and hotel schemes, and partnerships with Batelco and BENEFIT's Fawateer.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Zero breaches in 2024.", "div": "credimax", "rev": "company", "products": [
            P("security", "Data security & fraud", "Zero data-security breaches in 2024, a data-protection supervisor under Bahrain's PDP law, and complaints down to 7 from 12. No fraud-scoring vendor is named ⚠.",
              s=["con", "merch"], lc="everyday", o="B", neo=[0, "CrediMax's own."], src=[["CrediMax ESG report 2024", ESG]]),
            P("mccyber", "Mastercard cyber work", "The 2023 Mastercard agreement set out to explore Mastercard's cyber-intelligence tools; staff took part in a Mastercard Cyber Crisis Simulation Workshop in May 2025. Deployment is not confirmed ⚠.",
              s=["corp"], lc="everyday", o="P", at="Mastercard", neo=[1, "Explored; not confirmed ⚠."],
              mc="An open door for fraud scoring in an A2A-heavy market.",
              src=[["CrediMax: Mastercard partnership, Jul 2023", MCRENEW], ["CrediMax ESG report 2024", ESG]]),
        ]},
        {"id": "3.2", "ic": "fingerprint", "name": "Onboarding & data", "blurb": "Instant scoring since 2023.", "div": "credimax", "rev": "issuing", "products": [
            P("onboarding", "Digital onboarding & scoring", "Paperless digital onboarding (2022), an automated scoring system and 'happy flow' instant approval without manual review (2023), and virtual cards (2024).",
              s=["con", "young"], lc="open", o="B", neo=[0, ""], src=[["CrediMax ESG report 2024", ESG]]),
            P("dataai", "Data & AI", "No public AI or data programme was found ⚠.",
              s=["corp"], lc="everyday", neo=[None, "Nothing public."], src=[["BBK annual report 2025", BBKAR]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Thameen & offers", "blurb": "Points to ten airline schemes.", "div": "thameen", "rev": "issuing", "products": [
            P("thameen", "Thameen loyalty", "Points at 0.75–2 per dinar locally and 1.5–2.5 abroad, redeemable for Gulf Air Falconflyer miles, cashback, gift cards and donations, or exchanged into AlFursan, Avios, Etihad Guest, Miles&Smiles, Accor and others; points last 36 months.",
              s=["con", "prem"], lc="grow", o="B", neo=[1, "Earned on both networks."], src=[["CrediMax: Thameen", THAMEEN]]),
            P("offers", "SAVUR offers & raffles", "SAVUR merchant offers in the app, annual raffles, Mastercard Buy 1 Get 1 on World cards and merchant deals such as Qatar Airways (January 2025).",
              s=["con", "prem"], lc="grow", o="P", neo=[1, "Some Mastercard benefits."],
              mc="Card-linked offers could feed SAVUR and Thameen.",
              src=[["CrediMax: Thameen", THAMEEN], ["CrediMax: Qatar Airways, Jan 2025", QATAR], ["CrediMax: credit cards", CREDIT]]),
        ]},
        {"id": "3.4", "ic": "network", "name": "Partnerships", "blurb": "Batelco, Fawateer.", "div": "bbk", "rev": "company", "products": [
            P("batelco", "Batelco by Beyon MoU", "BBK, CrediMax and Batelco agreed on 1 July 2025 to align loyalty schemes, market jointly and explore instalments on Batelco products with BBK and CrediMax cards.",
              s=["con", "partner"], lc="beyond", st="new", ay="Jul 2025", o="P", at="Batelco by Beyon", neo=[0, ""], src=[["Batelco: BBK and CrediMax MoU, Jul 2025", BATELCO]]),
            P("fawateer", "Bill payment via Fawateer", "CrediMax card bills can be paid through BENEFIT's Fawateer bill-payment service (September 2024).",
              s=["con"], lc="move", ay="Sep 2024", o="P", at="BENEFIT", neo=[0, "BENEFIT rail."], src=[["CrediMax: Fawateer, Sep 2024", FAWATEER]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What it sells: credit, Islamic, prepaid and youth cards to Bahraini and expatriate consumers, premium World Elite and Infinite cards, corporate cards and virtual cards, and card acceptance for Bahrain's merchants, with co-brands for talabat and LuLu.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Consumer cards", "blurb": "Fourteen credit cards.", "div": "credimax", "rev": "issuing", "products": [
            P("retail", "Consumer cardholders", "Credit, Islamic, prepaid and youth cards for Bahraini and expatriate consumers, with the HSBC book added in November 2025. No cardholder count is published ⚠.",
              s=["con", "young"], lc="borrow", neo=[1, "7 of 14 credit cards on Mastercard."], src=[["CrediMax: credit cards", CREDIT], ["CrediMax: HSBC transition", HSBC]]),
            P("premium", "Premium cardholders", "World Elite Mastercard and Infinite Visa at the top, with lounge access, Careem rides and travel insurance.",
              s=["prem"], lc="borrow", neo=[1, "World Elite on Mastercard; Infinite on Visa."], src=[["CrediMax: credit cards", CREDIT], ["CrediMax: Mastercard award, May 2024", AWARD]]),
        ]},
        {"id": "4.2", "ic": "building-2", "name": "Corporate & SME", "blurb": "Cards and virtual cards.", "div": "credimax", "rev": "corporate", "products": [
            P("business", "Business customers", "Corporate cards on both networks, Visa Commercial Pay virtual cards, and per-card limits with online reporting.",
              s=["corp"], lc="everyday", neo=[1, "Cards on both; virtual on Visa."], src=[["CrediMax: corporate cards", CORP], ["Zawya: Visa Commercial Pay", VCP]]),
        ]},
        {"id": "4.3", "ic": "store", "name": "Merchants", "blurb": "Bahrain's main acquirer.", "div": "credimax", "rev": "acquiring", "products": [
            P("merchants", "Merchant services", "POS, gateway, kiosk integration, instalments and BNPL for Bahraini merchants; CrediMax calls itself the kingdom's foremost acquirer (no share data ⚠).",
              s=["merch"], lc="move", neo=[1, "Accepts every network."], src=[["BBK: subsidiaries", BBKSUBS], ["CrediMax: payment gateway", GATEWAY]]),
        ]},
        {"id": "4.4", "ic": "users-round", "name": "Co-brands & partners", "blurb": "talabat, LuLu, Batelco.", "div": "cobrand", "rev": "issuing", "products": [
            P("partners", "Co-brand partners", "talabat (2026) and LuLu Hypermarket (Danat) on Mastercard, Bapco Tazweed for acceptance, Batelco for loyalty, and BBK's customers for distribution.",
              s=["partner"], lc="beyond", o="P", neo=[1, "Co-brands on Mastercard."], src=[["TechAfrica News: talabat card, May 2026", TALABAT], ["CrediMax: credit cards", CREDIT]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach it: the CrediMax Digital app and web portal, the Merchant Portal, Quick Pay and PIN change, and BBK's branches, Financial Malls and ATMs.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "CrediMax Digital", "blurb": "The cardholder app.", "div": "credimax", "rev": "issuing", "products": [
            P("app", "CrediMax Digital app", "The app and web portal for statements, payments, Thameen redemption, SAVUR codes, Apple Wallet provisioning and the iLead dashboard; a new app was introduced in 2025.",
              s=["con", "young"], lc="everyday", st="new", o="P", at="Avanza", neo=[0, ""], src=[["CrediMax: home", HOME], ["BBK annual report 2025", BBKAR]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Merchant Portal", "blurb": "For acquiring clients.", "div": "credimax", "rev": "acquiring", "products": [
            P("mportal", "Merchant Portal", "Online reporting for CrediMax's merchants, with online POS and gateway applications.",
              s=["merch"], lc="open", o="B", neo=[0, ""], src=[["CrediMax: home", HOME]]),
        ]},
        {"id": "5.3", "ic": "log-in", "name": "Quick Pay & PIN", "blurb": "Pay a card bill.", "div": "credimax", "rev": "issuing", "products": [
            P("qpay", "Quick Pay & PIN change", "Quick Pay for card bills and online PIN change, alongside Fawateer.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["CrediMax: home", HOME], ["CrediMax: Fawateer, Sep 2024", FAWATEER]]),
        ]},
        {"id": "5.4", "ic": "building", "name": "BBK branches", "blurb": "Financial Malls, ATMs.", "div": "bbk", "rev": "company", "products": [
            P("branches", "BBK branches & ATMs", "CrediMax desks in BBK's Riffa, Isa Town and Muharraq Financial Malls; BBK ATMs for PIN change.",
              s=["con"], lc="open", o="I", neo=[0, ""], src=[["BBK: subsidiaries", BBKSUBS], ["CrediMax: HSBC transition", HSBC]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at CrediMax", "blurb": "Half the cards, the gateway.", "products": [
        P("mcatcm", "Mastercard at CrediMax", "A strategic partner since a July 2023 renewal: half the credit range including World Elite, the talabat and LuLu co-brands, iLead and Cardy, Mastercard corporate cards, Bahrain's first Click to Pay and, it appears, Mastercard Gateway for e-commerce ⚠. Visa has the other half, the Islamic, student and multi-currency cards and Visa Commercial Pay.",
          s=["con"], div="credimax", rev="company", mc="The relationship this map is drawn for.",
          src=[["CrediMax: Mastercard partnership, Jul 2023", MCRENEW], ["CrediMax: credit cards", CREDIT]]),
    ]},
    {"id": "pillar-market", "name": "Bahrain payments", "blurb": "BENEFIT, Fawri+, mergers.", "products": [
        P("market", "The Bahraini market", "BENEFIT (22% BBK-owned) processed 261 million transfers worth BD19.3 billion in H1 2026, 246 million of them through BenefitPay, with Fawri+ at 248 million (+8%). Mastercard signed an MoU with BENEFIT in May 2024; the CBB is building open banking; BBK and NBB are in merger talks.",
          s=["con"], div="bbk", rev="company",
          src=[["GDN: BENEFIT H1 2026, Sep 2026", BENEFITH1], ["Financial IT: Mastercard and BENEFIT, May 2024", MCBENEFIT], ["CBB: open banking", CBBOB]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
