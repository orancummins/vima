"""Arab Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 results (1 August 2026), the 2025
results (2 February 2026) and the 2025 Annual Report, with the bank's media room for launches. ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

NEWS26 = "https://www.arabbank.com/mainmenu/home/media-room-news?year=2026"
NEWS25 = "https://www.arabbank.com/mainmenu/home/media-room-news?year=2025"
NEWS24 = "https://www.arabbank.com/mainmenu/home/media-room-news?year=2024"
NEWS23 = "https://www.arabbank.com/mainmenu/home/media-room-news?year=2023"
NEWS22 = "https://www.arabbank.com/mainmenu/home/media-room-news?year=2022"
NEWS21 = "https://www.arabbank.com/mainmenu/home/media-room-news?year=2021"
NEWS19 = "https://www.arabbank.com/mainmenu/home/media-room-news?year=2019"
AR25 = "https://www.arabbank.com/docs/default-source/annual-reports-sorted/arab-bank-annual-report-2025.pdf?sfvrsn=eabdaa9f_2"
HISTORY = "https://www.arabbank.com/mainmenu/home/about/our-history"
BOARD = "https://www.arabbank.com/mainmenu/home/about/board-of-directors"
PROFILE = "https://www.arabbank.com/mainmenu/home/about/our-profile"
CARDS_JO = "https://www.arabbank.jo/mainmenu/home/Consumer-Banking/cards/card-type"
WEMC = "https://www.arabbank.jo/mainmenu/home/Consumer-Banking/cards/card-type/Arab-Bank-World-Elite-MasterCard"
UEFA = "https://www.arabbank.jo/mainmenu/home/Consumer-Banking/cards/card-type/arab-bank-uefa-mastercard"
AMEX = "https://www.arabbank.jo/mainmenu/home/Consumer-Banking/cards/card-type/american-express-(amex)"
CLIQ_AB = "https://www.arabbank.jo/mainmenu/home/ways-to-bank/instant-payment-service-cliq"
GPAY = "https://www.arabbank.jo/mainmenu/home/ways-to-bank/google-pay"
POINTS = "https://www.arabbank.jo/mainmenu/home/Consumer-Banking/arabi-points-program"
VCS = "https://www.arabbank.jo/mainmenu/home/corporate-institutional-banking/visa-corporate-signature-card"
REFLECT = "https://reflectapp.com/"
CARDS_AE = "https://www.arabbank.ae/mainmenu/home/Consumer-Banking/cards/card-type"
CARDS_EG = "https://www.arabbank.com.eg/mainmenu/home/personal-banking/cards/card-type"
CARDS_PS = "https://www.arabbank.ps/mainmenu/home/personal-banking/cards/card-type"
MCREMIT = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2024/january/arab-bank-and-mastercard-launch-cross-border-payments-services-remitex-in-jordan/"
JOPACC = "https://www.jopacc.com/sites/default/files/2026-03/end_of_year_systems_report_2025_en.pdf"
OPENFIN = "https://www.openbankproject.com/blog/open-finance-in-jordan-a-dive-into-the-instructions/"
CIR = "https://www.ciratings.com/news/2025/07/01/4572"
PETRA_H1 = "https://www.petra.gov.jo/en/news/arab-bank-posts-5709-million-in-first-half-net-profit"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · network · owners", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: USD 80 billion of assets and a record USD 1.13 billion profit in 2025, a quarter of Jordan's banking, a network of more than 600 branches in 28 countries built since 1930, and a bank putting AI to work across 2,000 staff.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "USD 80bn assets, first in Jordan.", "div": "abg", "rev": "group", "products": [
            P("balance", "Balance sheet & earnings", "Net profit of USD 570.9 million in H1 2026 (+7%) and a record USD 1.13 billion in 2025; assets USD 80.3 billion, loans USD 42.1 billion and deposits USD 58.8 billion at 30 June 2026; capital adequacy 17.3%; first in Jordan with 25.7% of assets, 25.9% of deposits and 20.0% of credit. Capital Intelligence rates it BB- ⚠; big-three ratings not confirmed.",
              s=["con"], neo=[0, ""], src=[["H1 2026 results, Aug 2026", NEWS26], ["Petra: H1 2026 profit", PETRA_H1], ["2025 Annual Report", AR25], ["CI Ratings, Jul 2025 ⚠", CIR]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & owners", "blurb": "Masri chairs, Sadik runs.", "div": "abg", "rev": "group", "products": [
            P("leadership", "Board, executives & shareholders", "Chairman Sabih Masri (since 2012), CEO Randa Sadik (since 2022), Deputy CEOs Mohammed Masri (corporate), Naim Al-Hussaini (consumer and wealth) and Eric Modave (COO), CFO Firas Zayyad. Jordan's Social Security Corporation owns 17.2%, the Shoman Foundation 5.0% and the Saudi Ministry of Finance 4.5%; listed in Amman, worth about JOD 4.4 billion at end-2025 ⚠.",
              s=["corp"], neo=[0, ""], src=[["Board of directors", BOARD], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "1.3", "ic": "earth", "name": "Heritage & network", "blurb": "1930, 600+ branches.", "div": "regional", "rev": "group", "products": [
            P("heritage", "Heritage", "Registered in Jerusalem in May 1930 by Abdul Hameed Shoman; head office in Amman since 1948; never defaulted on a payment through nationalisations and wars; a refreshed brand, 'Beginnings never end', in February 2025.",
              s=["con"], o="I", neo=[0, ""], src=[["Our history", HISTORY], ["Brand refresh, Feb 2025", NEWS25]]),
            P("network", "Branches, subsidiaries & affiliates", "More than 600 branches in 28 countries: Arab Bank plc's 187 branches (69 in Jordan), Oman Arab Bank (49%), Arab Tunisian Bank, Europe Arab Bank, Islamic International Arab Bank, Arab Bank Iraq (opened 2025) and Arab Bank – Syria; Arab National Bank (40%) in Saudi Arabia; 13,013 staff.",
              s=["corp"], o="I", neo=[0, ""], src=[["Our profile", PROFILE], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "1.4", "ic": "brain", "name": "Technology & AI", "blurb": "30 GenAI uses, Acabes.", "div": "acabes", "rev": "group", "products": [
            P("tech", "Acabes, cloud & AI", "Acabes, the fintech arm set up in 2021, runs the apps, a cloud marketplace and BPM platform and 70+ regulatory builds (CliQ, Aani, iBURAQ); 30 generative-AI uses reach about 2,000 staff and save about 7,000 working days a year, led by the Arabi GPT assistant.",
              s=["corp"], o="B", neo=[0, ""], src=[["2025 Annual Report", AR25], ["Acabes and Menaitech, Dec 2025", NEWS25]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & expansion", "blurb": "Iraq, Syria, Algeria, wealth.", "div": "abg", "rev": "group", "products": [
            P("strategy", "Strategy & deals", "Use the network, grow the core, add markets and digitise: Arab Bank Iraq opened in early 2025, Syria reactivated and an Islamic window opened in Algeria in 2026, and Arab Bank Switzerland's Gonet merged with Swiss One Bank (2025), lifting assets under management to CHF 18 billion.",
              s=["corp", "aff"], st="new", neo=[0, ""], src=[["H1 2026 results, Aug 2026", NEWS26], ["2025 Annual Report", AR25], ["Our history", HISTORY]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Visa debit for every account, a credit range that is mostly Visa with two Mastercard cards and Amex, wallets and Click to Pay, card acceptance for every network, CliQ instant transfers, and cross-border rails from Mastercard's RemitEx to Visa Direct, Citi, J.P. Morgan and crypto.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "Visa for every account.", "div": "jordan", "rev": "consumer", "products": [
            P("debit", "Visa Debit & Shabab Visa Debit", "Debit cards on Visa for Arab Bank accounts in Jordan, Palestine and Egypt; the Shabab debit card is issued instantly with no monthly fee, and debit spend earns Arabi Points.",
              s=["con", "youth"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."], src=[["Arab Bank Jordan: card types", CARDS_JO], ["Smart university card, Jan 2026", NEWS26]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "12 Visa, 2 Mastercard, Amex.", "div": "jordan", "rev": "consumer", "products": [
            P("visacredit", "Visa credit range", "Signature, Black, Platinum, Gold, Shabab, Travel Mate (eight currencies, no FX fees), Arabi Points, Together Platinum (0.5% to charity), Visa Arabi Switch (2023) and, for private clients, Visa Infinite Privilege (2025).",
              short="Visa credit", s=["con", "aff", "expat"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."], src=[["Arab Bank Jordan: card types", CARDS_JO], ["Visa Travel Mate, Aug 2025", NEWS25], ["2025 Annual Report", AR25]]),
            P("cobrand", "Co-branded cards", "Nashama Visa for Jordan's national team (World Cup 2026 campaign), the Arab Bank–LALIGA Visa card (May 2026, first in MENA) and the Royal Jordanian Visa Platinum.",
              short="Co-brands (Visa)", s=["con"], lc="borrow", st="new", ay="May 2026", o="P", at="Visa, LALIGA, Royal Jordanian", neo=[0, "Visa."],
              mc="Every sport and airline co-brand went to Visa.",
              src=[["LALIGA Visa card, May 2026", NEWS26], ["Arab Bank Jordan: card types", CARDS_JO]]),
            P("mccredit", "World Elite & UEFA Platinum Mastercard", "Two Mastercard cards in Jordan: World Elite for ultra-high-net-worth clients (1,200+ lounges, concierge, Cannes campaign 2023) and the UEFA Champions League Platinum co-brand (Travel Pass lounges, priceless.com, final-ticket campaigns in 2019 and 2025).",
              short="Mastercard credit", s=["aff", "con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard cards."],
              mc="Mastercard's foothold in Jordan: the top tier and football.",
              src=[["World Elite Mastercard", WEMC], ["UEFA Platinum Mastercard", UEFA], ["Mastercard UEFA campaign, Jun 2025", NEWS25]]),
            P("amex", "American Express Gold & Platinum", "Amex cards issued in Jordan from 2025, after Amex acceptance arrived on Arab Bank terminals in 2022.",
              short="Amex", s=["aff"], lc="borrow", st="new", ay="2025", o="P", at="American Express", neo=[0, "Amex."], src=[["Arab Bank Jordan: Amex", AMEX], ["2025 Annual Report", AR25]]),
            P("regionalcards", "Cards across the network", "Mastercard World Elite, Platinum and Titanium sit beside Visa ranges in the UAE and Egypt, and World Elite and Platinum in Palestine; Arab Bank joined the Jaywan (UAE) and Himyan (Qatar) domestic schemes in 2025.",
              short="Regional cards", s=["con", "expat"], lc="borrow", div="regional", o="P", at="Mastercard, Visa", neo=[1, "Mastercard and Visa."],
              src=[["Arab Bank UAE: cards", CARDS_AE], ["Arab Bank Egypt: cards", CARDS_EG], ["Arab Bank Palestine: cards", CARDS_PS], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "2.3", "ic": "smartphone", "name": "Wallets & checkout", "blurb": "Apple Pay, MobiCash, Click to Pay.", "div": "jordan", "rev": "consumer", "products": [
            P("wallets", "Apple Pay, Google Pay & Samsung Pay", "Apple Pay from February 2023, Google Pay in Jordan and Qatar and Samsung Pay in Qatar in 2025; tokens follow the card, so mostly Visa ⚠.",
              s=["con", "youth"], lc="everyday", o="P", at="Apple, Google, Samsung", neo=[1, "Tokens on each card's network ⚠."], src=[["Apple Pay, Feb 2023", NEWS23], ["Arab Bank Jordan: Google Pay", GPAY], ["2025 Annual Report", AR25]]),
            P("mobicash", "Arabi MobiCash & wearables", "Phone payments at more than 4,200 merchants (2024), with bracelets, stickers and rings for contactless.",
              s=["con"], lc="everyday", o="B", neo=[0, "Mostly Visa cards ⚠."], src=[["Winner Every Hour with Visa, Jul 2024", NEWS24]]),
            P("clicktopay", "Click to Pay", "First in Jordan, launched with Visa in September 2025 for all Arab Bank credit and debit cardholders.",
              s=["con"], lc="everyday", st="new", ay="Sep 2025", o="P", at="Visa", neo=[0, "Visa."],
              mc="Launched with Visa; Mastercard cards could join the same checkout.",
              src=[["Click to Pay with Visa, Sep 2025", NEWS25]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acceptance", "blurb": "Every network, state payments.", "div": "jordan", "rev": "cib", "products": [
            P("acquiring", "POS & merchant acquiring", "Terminals across Jordan taking Visa, Mastercard, Amex (2022) and JCB (2025), plus CliQ and MobiCash; SoftPOS; accredited acquirer for ministries and the payment gateway for consular services at 57 embassies (2025).",
              s=["sme"], lc="move", o="B", at="Visa, Mastercard, Amex, JCB", neo=[1, "Accepts every network."],
              src=[["Amex acceptance, Apr 2022", NEWS22], ["JCB acquiring, May 2025", NEWS25], ["2025 Annual Report", AR25]]),
            P("ecom", "E-commerce gateways", "HyperPay gateway partnership (January 2023), Arabi Shopix storefronts for SMEs (November 2023) and Arabi E-Mart; Visa CyberSource as the gateway in Egypt (2025).",
              s=["sme"], lc="move", o="P", at="HyperPay, Visa", neo=[1, "Accepts every network."], src=[["HyperPay, Jan 2023", NEWS23], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Instant payments", "blurb": "CliQ, 168m transfers.", "div": "jordan", "rev": "consumer", "products": [
            P("cliq", "CliQ & regional instant rails", "JoPACC's CliQ in Arabi Mobile and Reflect: alias transfers, request-to-pay and returns; CliQ carried 167.9 million payments worth JOD 20 billion in Jordan in 2025, double the year before. Aani (UAE) and iBURAQ also integrated.",
              s=["con", "youth", "sme"], lc="move", o="P", at="JoPACC", neo=[0, "National rail."],
              mc="Account-to-account volume doubled in 2025; fraud and identity tools are open ground.",
              src=[["Arab Bank: CliQ", CLIQ_AB], ["JoPACC: 2025 systems report", JOPACC], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "2.6", "ic": "send", "name": "Cross-border & digital money", "blurb": "RemitEx, Visa Direct, Kinexys.", "div": "abg", "rev": "treasury", "products": [
            P("remitex", "RemitEx", "Remittances to 28 countries on Mastercard Cross-Border Services, full value with no fee for the recipient; launched January 2024 with Mastercard's Levant team.",
              s=["expat", "con"], lc="move", ay="Jan 2024", o="P", at="Mastercard", neo=[3, "Mastercard Cross-Border Services."],
              mc="Mastercard's deepest product at the bank.",
              src=[["Mastercard: RemitEx, Jan 2024", MCREMIT], ["RemitEx launch, Jan 2024", NEWS24]]),
            P("visadirect", "Visa Direct", "Push-to-card transfers abroad from Arabi Mobile; first in Jordan, June 2023.",
              s=["expat"], lc="move", ay="Jun 2023", o="P", at="Visa", neo=[0, "Visa."], src=[["Visa Direct, Jun 2023", NEWS23]]),
            P("usd247", "Citi 24/7 USD & Kinexys", "Citi's 24/7 USD Clearing for corporate clients in selected branches (October 2026) and J.P. Morgan's Kinexys blockchain deposit network for round-the-clock settlement (April 2026).",
              s=["corp"], lc="move", st="new", ay="Oct 2026", o="P", at="Citi, J.P. Morgan", neo=[0, ""], div="abg", rev="cib",
              src=[["Citi 24/7 USD, Oct 2026", NEWS26], ["Kinexys, Apr 2026", NEWS26]]),
            P("crypto", "Crypto trading in Reflect", "Bitcoin, Ether and seven other coins traded in Reflect with Fuze from October 2026, the first Jordanian bank app to offer it, after a pilot in the central bank's JoRegBox sandbox.",
              s=["youth"], lc="grow", st="new", ay="Oct 2026", o="P", at="Fuze", div="reflect", rev="consumer", neo=[0, ""],
              mc="Crypto-linked cards and stablecoin links are untested ground.",
              src=[["Reflect crypto trading, Oct 2026", NEWS26], ["AB Xelerate and Fuze, Mar 2026", NEWS26]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: Sanad digital ID and in-house fraud models, Arabi GPT and the ReVA assistant, Omnify's banking APIs, Arabi Points and network campaigns, and an accelerator and venture arm.",
    "tiles": [
        {"id": "3.1", "ic": "fingerprint", "name": "Identity & fraud", "blurb": "Sanad ID, AI anomaly checks.", "div": "jordan", "rev": "consumer", "products": [
            P("sanad", "Sanad digital ID", "First bank to integrate Jordan's Sanad national digital ID: app activation (2022), verification (2024) and digital ID accepted in every branch (July 2025).",
              s=["con", "youth"], lc="open", o="P", at="Ministry of Digital Economy", neo=[0, ""], src=[["Sanad in branches, Jul 2025", NEWS25], ["Sanad verification, May 2024", NEWS24]]),
            P("fraud", "Fraud & security", "AI anomaly detection built by Acabes, staff fraud awareness, ISO 22301 continuity and Global Finance's 2026 award for information security and fraud management in Jordan.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, "Arab Bank's own."],
              mc="Instant-payment and card fraud tools have no public Mastercard role.",
              src=[["2025 Annual Report", AR25], ["Digital bank awards, Sep 2026", NEWS26]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI", "blurb": "Arabi GPT, ReVA.", "div": "reflect", "rev": "consumer", "products": [
            P("genai", "Arabi GPT & front-line assistant", "An internal assistant saving users five hours a week and a generative-AI assistant for branch and contact-centre staff in Jordan (2025); AI lead generation in trade finance.",
              s=["con", "corp"], lc="everyday", div="abg", rev="group", o="B", neo=[0, ""], src=[["2025 Annual Report", AR25]]),
            P("reva", "ReVA", "Reflect's Arabic and English conversational assistant (March 2026), by voice or chat, answering questions, showing balances and reviewing spending.",
              s=["youth"], lc="everyday", st="new", ay="Mar 2026", o="B", neo=[0, ""],
              mc="Spending insights and agentic payments are open ground.",
              src=[["ReVA launch, Mar 2026", NEWS26]]),
        ]},
        {"id": "3.3", "ic": "code-xml", "name": "APIs & fintech", "blurb": "Omnify BaaS, Xelerate.", "div": "acabes", "rev": "cib", "products": [
            P("omnify", "Omnify banking-as-a-service", "Acabes' API platform (October 2024): onboarding and ID, wallets, virtual IBANs, debit and prepaid cards, 'Cards as a Service' and payments; live with Menaitech in Jordan (December 2025) and universities and Octo in Egypt. Central-bank open-finance rules have required APIs since end-2023 ⚠.",
              s=["sme", "corp"], lc="open", st="new", ay="Oct 2024", o="B", neo=[None, "Card network not stated."],
              mc="Cards as a Service needs an issuing network; none is named.",
              src=[["Omnify launch, Oct 2024", NEWS24], ["Acabes and Menaitech, Dec 2025", NEWS25], ["Open Bank Project: Jordan open finance ⚠", OPENFIN]]),
            P("xelerate", "AB Xelerate, iHub & AB Ventures", "An accelerator with 50% more proofs of concept in 2025, an agentic-AI startup bootcamp, the iHub, and AB Ventures, the venture arm set up in 2018.",
              s=["corp"], lc="beyond", o="B", neo=[0, ""], src=[["2025 Annual Report", AR25]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Loyalty & campaigns", "blurb": "Arabi Points, network promos.", "div": "jordan", "rev": "consumer", "products": [
            P("points", "Arabi Points & Reflect rewards", "Relationship points for card spend, deposits and products, redeemable for cash or at merchants; Reflect's '1 Million Points' campaign and e-vouchers (May 2025); Royal Jordanian flights at 5% off in Arabi Mobile.",
              s=["con", "youth"], lc="everyday", o="B", neo=[0, ""], src=[["Arabi Points", POINTS], ["Reflect 1 Million Points, May 2025", NEWS25], ["RJ flight booking, Dec 2024", NEWS24]]),
            P("campaigns", "Network campaigns", "Mastercard: UEFA final trips (2019, 2025) and the World Elite Cannes campaign (2023). Visa: 'Winner Every Hour' (2024) and Nashama cashback (2026).",
              s=["con", "aff"], lc="everyday", o="P", at="Mastercard, Visa", neo=[1, "Both networks."],
              src=[["Mastercard UEFA campaign, Jun 2025", NEWS25], ["Cannes campaign, Jun 2023", NEWS23], ["Winner Every Hour, Jul 2024", NEWS24]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: banking programmes from Junior to Elite and a Cross Border account for expatriates, housing and green loans, private banking in Amman and Geneva, SME finance tied to card sales, and corporate, trade and treasury business across the region.",
    "tiles": [
        {"id": "4.1", "ic": "users-round", "name": "Personal banking", "blurb": "Junior to Elite, Cross Border.", "div": "jordan", "rev": "consumer", "products": [
            P("programmes", "Customer programmes", "Junior (under 18), Shabab (to 25), Extra (salaried), Premium, Elite (high net worth) and Tabeeb for doctors, each with its own cards and offers.",
              s=["con", "youth"], lc="everyday", o="B", neo=[0, "Visa debit."], src=[["2025 Annual Report", AR25]]),
            P("crossborder", "Cross Border account", "Accounts in Jordan and across the regional network from one app, instant 'Arabi Access' transfers between them, and non-resident mortgages for Jordanian expatriates (campaign July 2026).",
              s=["expat"], lc="move", o="B", neo=[0, ""],
              mc="Expatriate flows are where RemitEx and push payments matter most.",
              src=[["Cross Border campaign, Jul 2026", NEWS26]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Lending", "blurb": "Housing, solar, instalments.", "div": "jordan", "rev": "consumer", "products": [
            P("housing", "Housing, auto & green loans", "Housing-loan campaigns (2025, 2026), electric-vehicle loans and a solar-energy loan (April 2026).",
              s=["con"], lc="borrow", o="B", neo=[0, ""], src=[["Solar loan, Apr 2026", NEWS26], ["Housing loans, Jul 2026", NEWS26]]),
            P("instalments", "Instalments & Pay Later", "The Easy Payment Plan on credit cards, 0% green-product instalments (2025), instant instalments online with Amazon Payment Services (2021) and Reflect's Pay Later in four parts.",
              s=["con", "youth"], lc="borrow", o="P", at="Amazon Payment Services", neo=[0, "Mostly Visa cards ⚠."], src=[["Green card campaign, Jul 2025", NEWS25], ["Amazon Payment Services, Jun 2021", NEWS21], ["Reflect", REFLECT]]),
        ]},
        {"id": "4.3", "ic": "gem", "name": "Wealth & private banking", "blurb": "CHF 18bn in Switzerland.", "div": "swiss", "rev": "consumer", "products": [
            P("privatebank", "Private Banking Jordan", "Launched in 2025 with Visa Infinite Privilege, a REIT, capital-guaranteed USD deposits and a precious-metals account.",
              s=["aff"], lc="grow", st="new", ay="2025", div="jordan", o="B", neo=[0, "Visa Infinite."], src=[["2025 Annual Report", AR25]]),
            P("swiss", "Arab Bank Switzerland", "The sister bank in Geneva and Zurich since 1962; its Gonet unit merged with Swiss One Bank in mid-2025, taking client assets to CHF 18 billion.",
              s=["aff"], lc="grow", o="I", neo=[0, ""], src=[["2025 Annual Report", AR25], ["Our history", HISTORY]]),
        ]},
        {"id": "4.4", "ic": "briefcase", "name": "Small businesses", "blurb": "Loans repaid from card sales.", "div": "jordan", "rev": "consumer", "products": [
            P("sme", "SME banking", "Arabi SME and Arabi Next, SME credit cards (2025), a Dynamic POS Loan repaid daily from card sales (May 2025) and SME loyalty in Bahrain.",
              s=["sme"], lc="borrow", st="new", o="B", neo=[0, ""],
              mc="SME card and data products have no named network.",
              src=[["Dynamic POS loan, May 2025", NEWS25], ["2025 Annual Report", AR25]]),
        ]},
        {"id": "4.5", "ic": "building-2", "name": "Corporate & treasury", "blurb": "Syndications, trade, FX.", "div": "abg", "rev": "cib", "products": [
            P("cib", "Corporate & institutional banking", "Project and syndicated finance (lead on Royal Jordanian's USD 250 million loan, May 2025), trade finance, cash management, digital supply-chain finance in the UAE, and Treasury's FX, derivatives and sustainable-bond book.",
              s=["corp"], lc="borrow", o="B", neo=[0, ""], src=[["Royal Jordanian loan, May 2025", NEWS25], ["2025 Annual Report", AR25]]),
            P("corpcard", "Visa Corporate Signature", "A digital corporate credit card on Visa's payables-automation platform with single-use numbers and per-card limits (December 2021).",
              s=["corp"], lc="move", ay="Dec 2021", o="P", at="Visa", neo=[0, "Visa."],
              mc="Commercial and virtual cards are Visa's today.",
              src=[["Visa corporate card, Dec 2021", NEWS21], ["Visa Corporate Signature", VCS]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the bank: Arabi Mobile, Reflect, the Corporate Digital Gateway, and 69 branches in Jordan with campuses, clubs and Careem as partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Arabi Mobile", "blurb": "Redesigned 2025.", "div": "jordan", "rev": "consumer", "products": [
            P("arabimobile", "Arabi Mobile & Arabi Online", "A redesigned app in Jordan (2025) with digital onboarding, CliQ, cardless withdrawal, Royal Jordanian booking and credit reports; best mobile banking app in Jordan (Global Finance, 2026).",
              s=["con", "expat"], lc="everyday", o="B", neo=[0, ""], src=[["2025 Annual Report", AR25], ["Digital bank awards, Sep 2026", NEWS26]]),
        ]},
        {"id": "5.2", "ic": "rocket", "name": "Reflect", "blurb": "Jordan's first neobank.", "div": "reflect", "rev": "consumer", "products": [
            P("reflect", "Reflect", "A mobile-only bank launched in October 2021 for Jordan and Palestine: Visa debit and virtual cards, a free Visa Platinum credit card with 3% cashback, instant loans to JOD 6,000, Pay Later, ReVA and crypto. User numbers are not published ⚠.",
              s=["youth"], lc="open", o="B", at="Visa", neo=[0, "Visa cards."],
              mc="Jordan's most digital customers carry Visa.",
              src=[["Reflect launch, Oct 2021", NEWS21], ["Reflect", REFLECT], ["Reflect update, Jun 2024", NEWS24]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "Corporate digital", "blurb": "Gateway, ArabiConnect.", "div": "abg", "rev": "cib", "products": [
            P("cdg", "Corporate Digital Gateway & ArabiConnect", "A rebuilt corporate platform and mobile app (December 2025) with dashboards, basket payments and APIs for all payment types; digital collection accounts with CliQ (2024).",
              s=["corp", "sme"], lc="move", st="new", ay="Dec 2025", o="B", neo=[0, ""], src=[["Corporate Digital Gateway, Dec 2025", NEWS25], ["Digital collections, Jul 2024", NEWS24]]),
        ]},
        {"id": "5.4", "ic": "building", "name": "Branches & partners", "blurb": "69 branches, Careem, LALIGA.", "div": "jordan", "rev": "consumer", "products": [
            P("branches", "Branches & campuses", "69 branches and 3,645 staff in Jordan, video ITMs, a branch at King Hussein Medical City (January 2026) and smart university cards with campuses.",
              s=["con"], lc="everyday", o="B", neo=[0, ""], src=[["2025 Annual Report", AR25], ["Smart university card, Jan 2026", NEWS26]]),
            P("partners", "Partners", "Careem captain payouts in under five minutes (2024), the Jordan Football Association for 15 years, LALIGA across MENA (2025) and Yarmouk University with Reflect (2026).",
              s=["con", "sme"], lc="beyond", o="P", at="Careem, LALIGA, JFA", neo=[0, ""], src=[["Careem payouts, May 2024", NEWS24], ["LALIGA partnership, Aug 2025", NEWS25], ["Yarmouk University, Sep 2026", NEWS26]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Arab Bank", "blurb": "RemitEx and the top tier.", "products": [
        P("mcatarab", "Mastercard at Arab Bank", "Visa carries all debit, Reflect, the corporate card, every co-brand and 12 of 15 cards in Jordan, and launched Visa Direct and Click to Pay there first. Mastercard has World Elite and the UEFA Platinum card, ranges in the UAE, Egypt and Palestine, acceptance, campaigns, and RemitEx on Mastercard Cross-Border Services (2024). Amex issues from 2025.",
          s=["con"], div="abg", rev="group", mc="The relationship this map is drawn for.",
          src=[["Arab Bank Jordan: card types", CARDS_JO], ["Mastercard: RemitEx, Jan 2024", MCREMIT]]),
    ]},
    {"id": "pillar-market", "name": "Jordan's payments", "blurb": "CliQ, wallets, open finance.", "products": [
        P("market", "The Jordanian market", "JoPACC's systems carried 364 million payments worth JOD 93 billion in 2025 (+62% by volume): CliQ 168 million, JoMoPay wallets 102 million with 2.8 million wallet users, eFAWATEERcom bills; open-finance APIs mandated by the central bank ⚠ and a JoRegBox sandbox.",
          s=["con"], div="abg", rev="group", src=[["JoPACC: 2025 systems report", JOPACC], ["Open Bank Project: Jordan open finance ⚠", OPENFIN]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
