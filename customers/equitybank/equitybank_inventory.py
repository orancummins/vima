"""Equity Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Equity Bank Kenya is the local bank; Equity Group Holdings Plc and its five other banking subsidiaries are the
group context. Figures are the group's own unless a source says otherwise: the HY 2026 investor booklet
(19 August 2026), the FY2025 results (18 March 2026) and Equity Bank Kenya's products and services handbook
(July 2025). ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it,
2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

HY26 = "https://equitygroupholdings.com/wp-content/uploads/2026/08/Equity-Group-Holdings-PLC-HY-2026-Investor-Booklet.pdf"
IR = "https://equitygroupholdings.com/investor-relations/"
HB = "https://equitygroupholdings.com/ke/media/fjoemylb/equity-group-products-and-services-handbook.pdf"
KEHOME = "https://equitygroupholdings.com/ke/"
TECHISH = "https://tech-ish.com/2026/08/20/equity-group-half-year-profit-rises-32-to-kes-45-5-billion-as-more-than-half-the-business-moves-outside-kenya/"
CITH1 = "https://citizen.digital/article/equity-group-half-year-profit-hits-ksh45b-as-digital-regional-expansion-drive-record-growth-n388586"
CITFY = "https://citizen.digital/article/equity-profit-surges-to-ksh755b-as-regional-units-contribute-nearly-half-of-earnings-n379221"
KHUSOKO = "https://khusoko.com/2026/03/18/equity-group-posts-record-ksh75-5bn-profit-raises-dividend-35/"
MC23 = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2023/september/equity-bank-and-mastercard-sign-a-ten-year-agreement-to-scale-consumers-payment-experience-in-the-region"
HAPA23 = "https://hapakenya.com/2023/09/19/equity-bank-partners-with-mastercard-to-introduce-card-payment-solutions"
MC13 = "https://capitalfm.africa/equity-mastercard-in-joint-venture/"
MC15 = "https://nextbillion.net/news/financial-inclusion-equity-bank-master-card-launch-new-prepaid-card-in-kenya"
MCXB = "https://www.findevgateway.org/news/mastercard-and-equity-bank-join-forces-to-enhance-cross-border-money-transfers-in-kenya"
AMEX14 = "https://www.businessdailyafrica.com/bd/corporate/companies/equity-signs-up-as-american-express-card-issuer-2063638"
AMEX18 = "https://standardmedia.co.ke/business/article/2001286039/cards-firm-extends-deal-with-equity"
VISARW = "https://www.newtimes.co.rw/article/186882/Events/featured-equity-bank-rwanda-in-digital-payment-push/amp"
PAYPAL = "https://equitygroupholdings.com/ke/pay-send-money/personal/payment-services/paypal/"
WIKI = "https://en.wikipedia.org/wiki/Equity_Group_Holdings"
WIKIEQ = "https://en.wikipedia.org/wiki/Equitel"
CA = "https://citizen.digital/article/safaricom-gains-55-million-subscribers-as-kenyas-mobile-market-hits-841-million-n384964"
SAFCOM = "https://hapakenya.com/2026/05/07/safaricom-hits-historic-ksh-118-4b-net-profit-as-kenya-core-business-surges/"
PL24 = "https://techafricanews.com/2025/08/05/pesalink-partnership-with-sbm-bank-delivers-24-7-low-cost-interbank-transfers/"
MPPL = "https://techcabal.com/2025/09/05/m-pesa-raises-bank-transfer-limit-via-pesalink/"
FPS = "https://www.businessdailyafrica.com/bd/economy/ruto-entangled-in-battle-for-new-payments-platform-4976374"
KCB = "https://ke.kcbgroup.com/kcb-and-mastercard-unveil-world-elite-credit-cards"
NYAB = "https://citizen.digital/article/equity-bank-appoints-moses-okoth-nyabanda-as-acting-managing-director-n347896"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · six banks · technology group", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: KES 2.16 trillion of assets and a record KES 75.5 billion profit in 2025, banks in six countries that now earn 42% of banking profit, a technology group that calls Equity 'a technology company that does banking', and a 2030 plan for 15 countries and 100 million customers.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "KES 2.16tn, ROE 26.5%.", "div": "egh", "rev": "kenya", "products": [
            P("balance", "H1 2026 results", "Profit after tax of KES 45.5 billion in the six months to June 2026 (up 32%), total income KES 124.9 billion with non-funded income 44.5% of it, assets KES 2.16 trillion, deposits KES 1.59 trillion, net loans KES 981 billion, ROE 26.5%, cost-to-income 48.6% and NPLs down to 9.5%.",
              s=["con"], neo=[0, ""], src=[["HY 2026 investor booklet", HY26], ["Tech-ish: H1 2026, Aug 2026", TECHISH]]),
            P("fy2025", "FY2025 results & dividend", "Record profit after tax of KES 75.5 billion in 2025 (up 55%), total income KES 217.7 billion, 22.4 million customer accounts, Equity Bank Kenya PAT KES 39.2 billion (up 63%), and a dividend of KES 5.75 a share (KES 21.7 billion).",
              s=["con"], neo=[0, ""], src=[["Citizen Digital: FY2025, Mar 2026", CITFY], ["Khusoko: FY2025 dividend, Mar 2026", KHUSOKO]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & ownership", "blurb": "Mwangi since the building society.", "div": "egh", "rev": "kenya", "products": [
            P("leadership", "Board & executives", "Chair Prof Isaac Macharia; Group MD and CEO Dr James Mwangi; COO Samuel Kirubi, strategy chief Brent Malahay, finance and transformation chief Anthony Murage, product chief Rene Kalonji; Moses Nyabanda runs Equity Bank Kenya (acting from August 2024).",
              s=["corp"], neo=[0, ""], src=[["HY 2026 investor booklet", HY26], ["Citizen Digital: Nyabanda, Aug 2024", NYAB]]),
            P("owners", "Listing, ownership & heritage", "Founded in October 1984 as Equity Building Society; listed in Nairobi (EQTY) and cross-listed in Uganda (2009); largest holder Arise BV with 12.76% (March 2023 ⚠ dated); 14,265 staff. Market capitalisation at October 2026 not found ⚠.",
              s=["corp"], o="I", neo=[0, ""], src=[["Wikipedia: Equity Group Holdings", WIKI], ["HY 2026 investor booklet", HY26]]),
        ]},
        {"id": "1.3", "ic": "earth", "name": "Six-country footprint", "blurb": "Kenya plus five, 23.3m accounts.", "div": "region", "rev": "regional", "products": [
            P("footprint", "Banks in six countries", "Kenya 14.3 million accounts, DRC 4.2 million, Uganda 2.2 million, Rwanda 1.9 million, Tanzania 455,000 and South Sudan 250,000, with a representative office in Ethiopia; outside Kenya the banks hold 54% of loans and earn 42% of banking profit (H1 2026). Second by assets in Kenya (12.4%), DRC and Rwanda.",
              s=["con", "sme"], neo=[0, ""], src=[["HY 2026 investor booklet", HY26]]),
            P("deals", "Acquisitions", "ProCredit Bank Congo (79%, 2015), Banque Commerciale du Congo (66.5% for US$95 million, August 2020, merged into Equity BCDC) and Cogebanque in Rwanda (91.93% term sheet June 2023, merged from January 2024).",
              s=["corp"], o="A", neo=[0, ""], src=[["Wikipedia: Equity Group Holdings", WIKI]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology Group & AI", "blurb": "A technology company that does banking.", "div": "finserve", "rev": "nonbank", "products": [
            P("techgroup", "Equity Technology Group", "Six capability lines (payment solutions, the Equitel MVNO, IT services, AI, digital currencies and trading platforms) on microservices, hybrid cloud, an enterprise data fabric, AI decision engines and API-first banking; Finserve's revenue grew 84% to KES 1.77 billion in H1 2026.",
              s=["corp"], neo=[0, ""], src=[["HY 2026 investor booklet", HY26]]),
            P("aiskills", "AI skills programme", "82% of staff (12,882) have taken a business generative-AI course, 5,743 hold Huawei certifications and 406 are on WorldQuant University master's programmes: about 120,000 hours of AI instruction.",
              s=["corp"], st="new", o="P", at="Huawei ICT Academy, WorldQuant University", neo=[0, ""], src=[["HY 2026 investor booklet", HY26]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "2030 strategy & foundation", "blurb": "15 countries, 100m customers.", "div": "egh", "rev": "kenya", "products": [
            P("strategy2030", "2030 strategy", "Anchored on the Africa Recovery and Resilience Plan: operate in 15 countries, serve 100 million customers and build next-generation digital and AI systems, sharing KYC, wallet rails, AI models and APIs across the group ('One Equity').",
              s=["corp"], st="new", neo=[0, ""],
              mc="A 15-country, 100-million-customer plan is the scale case for the 2023 regional agreement.",
              src=[["HY 2026 investor booklet", HY26]]),
            P("egf", "Equity Group Foundation", "60,009 Wings to Fly and Elimu scholars, more than a million entrepreneurs trained, and the USD 25 million SASTAIN programme with the Mastercard Foundation for 60,000 smallholder farmers in Tanzania and DRC.",
              s=["farm"], o="P", at="Mastercard Foundation", neo=[0, "The Mastercard Foundation is independent of Mastercard."], src=[["HY 2026 investor booklet", HY26]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: debit on Visa and Mastercard side by side, credit on Visa and Amex with Mastercard for corporates, acquiring for every network, Pay With Equity tills, Equitel and the M-Pesa and PesaLink links, cross-border send and FX, and a digital-asset platform in the making.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit & prepaid", "blurb": "Visa and Mastercard side by side.", "div": "ebkl", "rev": "kenya", "products": [
            P("debit", "Classic debit cards", "Visa and Mastercard classic debit cards offered side by side, contactless, 3-D Secure and printed at the branch (KES 600 to issue, KES 200 a year); an 'instant Mastercard or Visa card' comes with retail accounts.", short="Classic debit (Visa & Mastercard)",
              s=["con", "sme"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Visa and Mastercard side by side."],
              mc="Customers choose the network at the counter; share of issuance is not published.",
              src=[["Equity products handbook, Jul 2025", HB]]),
            P("premiumdebit", "Premium debit: Platinum, World & World Elite", "Premium Visa and Mastercard debit cards in shillings and dollars; in the Fanikisha tiers the bank names Mastercard Platinum, Mastercard World and Mastercard World Elite debit, the last with JKIA lounge access and travel insurance.", short="Premium debit (Mastercard World Elite)",
              s=["con", "sme"], lc="everyday", st="new", o="P", at="Mastercard, Visa", neo=[1, "Mastercard World and World Elite at the top; Visa premium too."],
              src=[["Equity products handbook, Jul 2025", HB], ["Mastercard: ten-year agreement, Sep 2023", MC23]]),
            P("propcard", "Equity proprietary debit", "An Equity-only debit card (KES 400), accepted in Kenya and across Equity's subsidiaries at ATMs, agents and POS.",
              s=["con"], lc="everyday", o="B", neo=[0, "Equity's own brand."], src=[["Equity products handbook, Jul 2025", HB]]),
            P("usdgold", "USD Gold debit", "A Visa debit card on a dollar account ($8 to issue); Equity Bank Rwanda launched USD Visa Gold debit and Visa Infinite cards in June 2021.",
              s=["con", "dia"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Equity products handbook, Jul 2025", HB], ["New Times: Equity Rwanda Visa cards, Jun 2021", VISARW]]),
            P("prepaid", "Prepaid cards", "Top-up cards for Equity and non-Equity customers, loaded at branches and agents; launched on Mastercard with contactless in February 2015 ⚠ current network not stated.",
              s=["con"], lc="everyday", ay="Feb 2015", o="P", at="Mastercard", neo=[2, "Mastercard at launch ⚠ current network not stated."], src=[["NextBillion: Mastercard prepaid, Feb 2015", MC15], ["Equity products handbook, Jul 2025", HB]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit & commercial cards", "blurb": "Visa, Amex, Mastercard corporate.", "div": "ebkl", "rev": "kenya", "products": [
            P("visacredit", "Visa credit cards", "Visa Classic and Gold credit cards (KES 2,500 and KES 4,500 a year, 3.5% a month), and a Visa credit card up to KES 300,000 in Fanikisha Dhahabu.", short="Consumer credit (Visa)",
              s=["con"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Equity products handbook, Jul 2025", HB]]),
            P("amexcredit", "American Express Green & Gold", "Equity is the exclusive issuer of American Express cards in Kenya (from 2013–14, also Uganda and Tanzania); Green and Gold credit cards for limits of KES 301,000 to KES 3 million.", short="Premium credit (Amex)",
              s=["con", "sme"], lc="borrow", o="P", at="American Express", neo=[0, "American Express."], src=[["Business Daily: Amex issuer, Jul 2014", AMEX14], ["Equity products handbook, Jul 2025", HB]]),
            P("corpcard", "Corporate credit cards", "Mastercard credit cards for corporates and SMEs banked with Equity for at least a year (KES 4,000 a year, 13% a year).", short="Corporate cards (Mastercard)",
              s=["corp", "sme"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Mastercard's clearest hold on Equity's credit book.",
              src=[["Equity products handbook, Jul 2025", HB]]),
            P("virtual", "Virtual cards", "Named in the scope of the 2023 Mastercard agreement alongside corporate cards ⚠ no launch found.",
              s=["corp"], lc="move", st="unconf", o="P", at="Mastercard", neo=[None, "In the 2023 Mastercard scope ⚠ not seen live."], src=[["Mastercard: ten-year agreement, Sep 2023", MC23]]),
        ]},
        {"id": "2.3", "ic": "store", "name": "Card acceptance", "blurb": "Every network; Amex exclusive.", "div": "ebkl", "rev": "kenya", "products": [
            P("posacq", "POS acquiring", "Terminals accepting Amex, UnionPay, Diners, Discover, JCB, Mastercard and Visa with next-day settlement; exclusive Amex acquirer in Kenya (extended June 2018) and Visa acquiring awards (2021). Card merchant payments were 9.1 million transactions worth KES 67.7 billion in H1 2026 ⚠ read from a chart.",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts every network."], src=[["Equity products handbook, Jul 2025", HB], ["The Standard: Amex acquiring, Jun 2018", AMEX18], ["HY 2026 investor booklet", HY26]]),
            P("jenga", "Jenga payment gateway", "An e-commerce payment gateway and APIs for business customers to collect payments online.",
              s=["sme", "corp"], lc="move", o="B", at="Finserve", neo=[None, ""], src=[["Equity products handbook, Jul 2025", HB]]),
        ]},
        {"id": "2.4", "ic": "receipt-text", "name": "Pay With Equity tills", "blurb": "213.6m payments in a half.", "div": "ebkl", "rev": "kenya", "products": [
            P("pwe", "Pay With Equity", "One merchant till that takes Equitel, Equity Mobile, M-Pesa (paybill 247247) and PesaLink payments with no merchant commission and real-time settlement: 213.6 million transactions worth KES 1.08 trillion in H1 2026 ⚠ read from a chart; 1.3 million merchants in Kenya.",
              s=["sme", "con"], lc="move", o="B", neo=[0, "Mobile money and PesaLink, not cards."],
              mc="QR and tap on phone from the 2023 agreement would land here.",
              src=[["Equity products handbook, Jul 2025", HB], ["HY 2026 investor booklet", HY26]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Equitel & mobile money", "blurb": "Its own MVNO; M-Pesa next door.", "div": "finserve", "rev": "nonbank", "products": [
            P("equitel", "Equitel", "Finserve's mobile network on Airtel Kenya (licence April 2014, SIMs from October 2014): 1.51 million subscribers (1.8%, Jan–Mar 2026); once 22% of Kenya's mobile-money value (2018); 195.7 million transactions worth KES 651 billion in H1 2026 ⚠ read from a chart.",
              s=["con"], lc="move", ay="Oct 2014", o="B", at="Airtel Kenya", neo=[0, "Equity's own rail."], src=[["Wikipedia: Equitel", WIKIEQ], ["Citizen Digital: CA mobile data, Jun 2026", CA], ["HY 2026 investor booklet", HY26]]),
            P("pesalink", "PesaLink & M-Pesa links", "Bank-to-bank transfers on PesaLink (about KES 1.1 trillion across the industry in 2024) and M-Pesa in and out of Equity accounts; M-Pesa users can send up to KES 500,000 to banks through PesaLink (September 2025). The CBK plans its own fast payment system ⚠ status unknown.",
              s=["con", "sme"], lc="move", o="P", at="IPSL, Safaricom", neo=[0, ""], src=[["TechAfrica News: PesaLink 2024", PL24], ["TechCabal: M-Pesa via PesaLink, Sep 2025", MPPL], ["Business Daily: CBK fast payments", FPS]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Cross-border & FX", "blurb": "Mastercard from the branch.", "div": "ebkl", "rev": "kenya", "products": [
            P("mccbs", "Mastercard Cross-Border Services", "Send money from any Equity branch in Kenya to 30 countries (April 2024).", short="Cross-border send (Mastercard)",
              s=["dia", "con"], lc="move", ay="Apr 2024", o="P", at="Mastercard", neo=[3, "Mastercard Cross-Border Services."],
              mc="Branch-only today; the app and Equitel are the obvious next step.",
              src=[["FinDev Gateway: Mastercard cross-border, Apr 2024", MCXB]]),
            P("remit", "Western Union, remittance partners & PayPal", "Western Union inside Equity Mobile and Equity Online; Small World, Transfast and Remitly paying into Equity accounts or M-Pesa and Airtel wallets; PayPal withdrawals and card linking in the app.",
              s=["dia"], lc="move", o="P", at="Western Union, Small World, Remitly, PayPal", neo=[0, ""], src=[["Equity products handbook, Jul 2025", HB], ["Equity: PayPal", PAYPAL]]),
            P("eazzyfx", "Eazzy FX", "An online FX dealing platform for business clients; KES 77.6 billion of transactions in H1 2026, up 44% ⚠ read from a chart.",
              s=["corp", "sme"], lc="move", o="B", neo=[0, ""], src=[["Equity products handbook, Jul 2025", HB], ["HY 2026 investor booklet", HY26]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Digital assets", "blurb": "A settlement platform in the plan.", "div": "finserve", "rev": "nonbank", "products": [
            P("digitalasset", "Digital asset settlement platform", "Listed as the 'digital currencies' line of the Equity Technology Group ⚠ no product or partner public.",
              s=["corp"], lc="move", st="unconf", neo=[None, ""], src=[["HY 2026 investor booklet", HY26]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: one KYC across six countries and Community Pass in the Mastercard contract, cyber defence agreed with Mastercard, AI decision engines, the Eva chatbot and Jenga APIs, and card deals.",
    "tiles": [
        {"id": "3.1", "ic": "fingerprint", "name": "Identity & KYC", "blurb": "One KYC for six countries.", "div": "egh", "rev": "regional", "products": [
            P("kyc", "Unified KYC", "One KYC across all subsidiaries under the 'One Equity' plan, to cut onboarding friction and compliance cost.",
              s=["con"], lc="open", st="new", o="B", neo=[0, ""], src=[["HY 2026 investor booklet", HY26]]),
            P("communitypass", "Community Pass", "In the 2023 Mastercard agreement: access to services for farmers and traders by QR, biometric or facial identification ⚠ no live deployment found.",
              s=["farm", "sme"], lc="open", st="unconf", o="P", at="Mastercard", neo=[None, "Mastercard's, contracted in 2023 ⚠ not seen live."],
              mc="Fits Equity's agri ecosystems and agents; the most specific unused clause in the deal.",
              src=[["Mastercard: ten-year agreement, Sep 2023", MC23], ["HapaKenya: Mastercard deal, Sep 2023", HAPA23]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud & cyber", "blurb": "Joint strategy with Mastercard.", "div": "egh", "rev": "kenya", "products": [
            P("cyber", "Risk analytics & cyber defence", "Risk analytics being modernised group-wide; the 2023 Mastercard agreement commits both sides to joint strategies against cybercrime ⚠ no named fraud product public.",
              s=["con", "sme"], lc="everyday", o="B", neo=[None, "Joint anti-cybercrime work agreed ⚠."], src=[["HY 2026 investor booklet", HY26], ["Mastercard: ten-year agreement, Sep 2023", MC23]]),
        ]},
        {"id": "3.3", "ic": "brain", "name": "Data, AI & APIs", "blurb": "Decision engines, Eva, Jenga.", "div": "finserve", "rev": "nonbank", "products": [
            P("aidata", "AI decision engines & Eva", "Centrally trained AI models for risk scoring and personalisation on a group data fabric, faster credit decisions, and the Eva chatbot in the app.",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, ""],
              mc="An AI-first plan with no agentic-payments partner yet.",
              src=[["HY 2026 investor booklet", HY26], ["Equity products handbook, Jul 2025", HB]]),
            P("apis", "Jenga APIs & open API layer", "An open API layer for third-party integrations and partner growth, with Jenga APIs offered to business customers.",
              s=["sme", "corp"], lc="open", o="B", at="Finserve", neo=[0, ""], src=[["HY 2026 investor booklet", HY26], ["Equity products handbook, Jul 2025", HB]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Card deals", "blurb": "Discounts on Equity cards.", "div": "ebkl", "rev": "kenya", "products": [
            P("carddeals", "Equity Deals", "Card discounts and property deals on the Kenyan website, for customers paying with an Equity card.",
              s=["con"], lc="everyday", o="B", neo=[1, "Offers on Equity's Visa and Mastercard cards ⚠."], src=[["Equity Bank Kenya website", KEHOME]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: accounts and mobile loans for 23 million, MSME and women-in-business banking, farm and supply-chain finance, corporate, trade and investment banking, and insurance and clinics.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Accounts & mobile loans", "blurb": "23.3m accounts, Eazzy loans.", "div": "ebkl", "rev": "kenya", "products": [
            P("accounts", "Retail accounts", "23.3 million customer accounts across six countries, 14.3 million of them in Kenya, each with a Visa or Mastercard debit card on request and access by app, USSD, Equitel and agents.",
              s=["con"], lc="open", neo=[1, "Visa or Mastercard debit."], src=[["HY 2026 investor booklet", HY26], ["Equity products handbook, Jul 2025", HB]]),
            P("eazzyloan", "Eazzy Loan", "Mobile loans of up to KES 3 million through Equitel, the app and *247#; KES 86.8 billion lent across 3.0 million loans group-wide in H1 2026.",
              s=["con", "sme"], lc="borrow", o="B", neo=[0, ""], src=[["Equity products handbook, Jul 2025", HB], ["HY 2026 investor booklet", HY26]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "MSME & women in business", "blurb": "36% of Kenya's MSME lending.", "div": "ebkl", "rev": "kenya", "products": [
            P("msme", "MSME banking", "Equity Bank Kenya made 36% of Kenya's KES 101 billion of MSME loan disbursements in Q1 2026; business accounts, working capital, LPO finance and Mastercard corporate cards.",
              s=["sme"], lc="borrow", neo=[1, "Mastercard corporate cards."], src=[["Tech-ish: H1 2026, Aug 2026", TECHISH], ["Equity products handbook, Jul 2025", HB]]),
            P("fanikisha", "Fanikisha", "Four tiers for women-run businesses (Shaba to Platini, turnover up to and above KES 800 million), each bundling loans, health cover and a card: Visa or Mastercard classic, Mastercard Platinum, Mastercard World or World Elite debit, Visa credit or Amex.",
              s=["sme"], lc="borrow", neo=[1, "Mastercard premium debit; Visa and Amex credit."], src=[["Equity products handbook, Jul 2025", HB]]),
        ]},
        {"id": "4.3", "ic": "target", "name": "Agriculture & ecosystems", "blurb": "Tea, water, motorbikes.", "div": "ebkl", "rev": "kenya", "products": [
            P("agri", "Ecosystem & agri finance", "Loans run through value chains, such as KTDA tea farmers, Maji water loans and Eco Moto motorbike loans, plus supplier and distributor credit lines (Eazzy Stock).",
              s=["farm", "sme"], lc="borrow", o="P", at="KTDA", neo=[0, ""],
              mc="Community Pass was written into the 2023 deal for exactly these customers.",
              src=[["Equity products handbook, Jul 2025", HB]]),
        ]},
        {"id": "4.4", "ic": "building-2", "name": "Corporate, trade & investment", "blurb": "Trade finance, EIB.", "div": "eib", "rev": "nonbank", "products": [
            P("corporate", "Corporate & trade banking", "Trade finance, supply-chain finance up to KES 250 million, a China desk and Equity Online for Business, which moved KES 2.74 trillion in H1 2026 (up 27%) ⚠ read from a chart.",
              s=["corp"], lc="move", neo=[1, "Mastercard corporate cards."], src=[["Equity products handbook, Jul 2025", HB], ["HY 2026 investor booklet", HY26]]),
            P("eib", "Equity Investment Bank", "Brokerage, asset management and advisory, building access to African capital markets; revenue KES 0.34 billion in H1 2026 (up 41%).",
              s=["corp", "con"], lc="grow", neo=[0, ""], src=[["HY 2026 investor booklet", HY26]]),
        ]},
        {"id": "4.5", "ic": "users-round", "name": "Insurance & health", "blurb": "22.6m life policies.", "div": "insure", "rev": "insurance", "products": [
            P("insurance", "Equity Insurance Group", "Life, general and health insurance: gross written premiums KES 6.4 billion in H1 2026 (up 24%), PBT KES 1.25 billion, 22.6 million life policies issued to date, 79% sold digitally.",
              s=["ins", "con"], lc="beyond", neo=[0, ""], src=[["HY 2026 investor booklet", HY26]]),
            P("afya", "Equity Afya", "156 medical centres with 5.3 million patient visits, and a first community pharmacy in a planned network of 1,000.",
              s=["ins"], lc="beyond", st="new", neo=[0, ""], src=[["HY 2026 investor booklet", HY26]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Equity: 89.7% of transactions are digital, through the Equity Mobile app, *247#, Equitel and Equity Online, backed by 410 branches, 886 ATMs and 92,572 agents.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Equity Mobile & *247#", "blurb": "KES 2.56tn in a half.", "div": "ebkl", "rev": "kenya", "products": [
            P("app", "Equity Mobile app & USSD", "The app and *247# carried 90.8 million transactions worth KES 2.56 trillion in H1 2026 (value up 29%) ⚠ read from a chart; 89.7% of all transactions are digital.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, ""], src=[["HY 2026 investor booklet", HY26]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Equity Online", "blurb": "For individuals and business.", "div": "ebkl", "rev": "kenya", "products": [
            P("online", "Equity Online & EazzyBiz", "Online banking for individuals and for corporates, public bodies and SMEs, with payments to banks and mobile wallets, liquidity management and reconciliation.",
              s=["corp", "sme"], lc="everyday", o="B", neo=[0, ""], src=[["Equity products handbook, Jul 2025", HB], ["Equity Bank Kenya website", KEHOME]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches, agents & diaspora", "blurb": "410 branches, 92,572 agents.", "div": "egh", "rev": "regional", "products": [
            P("branches", "Branches & ATMs", "410 branches and 886 ATMs and deposit machines in six countries; the machines take Visa, Mastercard, Amex and Equity cards and M-Pesa and Equitel wallets.",
              s=["con"], lc="everyday", neo=[1, "Accepts every card network."], src=[["HY 2026 investor booklet", HY26], ["Equity products handbook, Jul 2025", HB]]),
            P("agents", "Agency banking", "92,572 agency outlets (41,632 in Kenya, 30,827 in DRC) for deposits, withdrawals and account opening.",
              s=["con", "farm"], lc="open", o="P", neo=[0, ""], src=[["HY 2026 investor booklet", HY26]]),
            P("diaspora", "Diaspora banking", "Accounts, investment loans for diaspora groups and referral agents for Kenyans abroad.",
              s=["dia"], lc="grow", neo=[0, ""], src=[["Equity products handbook, Jul 2025", HB], ["Equity Bank Kenya website", KEHOME]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Equity", "blurb": "A ten-year deal, half-activated.", "products": [
        P("mcatequity", "Mastercard at Equity", "Equity has issued Mastercard since 2013 and signed a ten-year agreement in September 2023 covering World and World Elite, corporate and virtual cards, QR, tap on phone, cross-border and Community Pass in six countries. Mastercard holds corporate credit, top-tier debit and branch remittances; Visa shares debit and holds consumer credit; Amex holds premium credit and exclusive Kenyan acquiring.",
          s=["con"], div="egh", rev="kenya", mc="The relationship this map is drawn for.",
          src=[["Mastercard: ten-year agreement, Sep 2023", MC23], ["Capital FM: Equity and Mastercard, Jan 2013", MC13], ["Equity products handbook, Jul 2025", HB]]),
    ]},
    {"id": "pillar-market", "name": "Kenyan payments", "blurb": "M-Pesa, PesaLink, fast payments.", "products": [
        P("market", "The Kenyan market", "M-Pesa holds 89.1% of mobile-money subscriptions and earned KES 182.7 billion in FY2026; PesaLink links banks and, since 2025, M-Pesa; the CBK plans a national fast payment system ⚠; KCB issues Mastercard World Elite credit cards (2023).",
          s=["con"], div="ebkl", rev="kenya", src=[["Citizen Digital: CA mobile data, Jun 2026", CA], ["HapaKenya: Safaricom FY2026, May 2026", SAFCOM], ["Business Daily: CBK fast payments", FPS], ["KCB: World Elite with Mastercard, Oct 2023", KCB]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
