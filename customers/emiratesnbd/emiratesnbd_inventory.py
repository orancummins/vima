"""Emirates NBD's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 results (23 July 2026), the FY 2025
results (26 January 2026) and the RBL Bank completion filing (18 June 2026). Card networks are read from the
bank's own card listings. ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product
runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://www.emiratesnbd.com/en/media-center/emirates-nbd-h1-2026-results-announcement"
FY25 = "https://www.emiratesnbd.com/en/media-center/emirates-nbd-announces-fy-2025-financial-results"
AGBI = "https://www.agbi.com/banking-finance/2026/07/loan-growth-lifts-emirates-nbd-profit-to-3-5bn/"
RBL = "https://feeds.dfm.ae/documents/2026/Jun/18/2044cc79-ac5d-4372-ad6c-1b19798072e5/Emirates%20NBD%20And%20RBL%20Bank%20Announce%20The%20Successful%20.pdf"
ABOUT = "https://www.emiratesnbd.com/en/about-emirates-nbd"
JOURNEY = "https://www.emiratesnbd.com/en/about-emirates-nbd/our-journey"
MGMT = "https://www.emiratesnbd.com/en/about-emirates-nbd/corporate-governance/management-team"
CC = "https://www.emiratesnbd.com/en/cards/credit-cards"
DC = "https://www.emiratesnbd.com/en/cards/debit-cards"
COMM = "https://www.emiratesnbd.com/en/cards/commercial-cards"
PREPAID = "https://www.emiratesnbd.com/en/cards/prepaid-cards/globalcash-card"
VOYAGER = "https://www.emiratesnbd.com/en/campaigns/voyager-credit-cards"
VOYLAUNCH = "https://techafricanews.com/2025/12/09/voyager-mastercard-launches-with-digital-travel-portal-and-integrated-services/"
MARRIOTT = "https://news.marriott.com/news/2024/03/28/emirates-nbd-marriott-bonvoy-and-mastercard-unveil-two-new-co-brand-credit-cards-in-the-united-arab-emirates"
DPW = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2024/september/emirates-nbd-and-dp-world-launch-new-co-branded-mastercard-corporate-card-in-the-uae-advancing-the-dubai-economic-agenda-2033"
MCGW = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2025-1/february/mastercard-collaborates-with-emirates-nbd-to-accelerate-digital-payment-adoption-through-innovative-acceptance-solutions"
MCEG = "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2024/january/mastercard-and-emirates-nbd-egypt-partner-to-advance-egypt-s-digital-banking-experience"
TMG = "https://www.egypttoday.com/Article/3/142317/Emirates-NBD-Egypt-Talaat-Mostafa-Group-collaborate-to-launch-exclusive"
VISA20 = "https://www.electronicpaymentsinternational.com/?p=49395"
VISAPLUS = "https://fintech.global/2025/04/17/visa-and-emirates-nbd-join-forces-to-drive-digital-remittance-innovation-in-the-uae/"
NNSS = "https://www.emiratesnbd.com/en/media-center/visa-appoints-emirates-nbd-as-its-official-national-net-settlement-service-agent-in-the-uae"
AITRAVEL = "https://www.emiratesnbd.com/en/media-center/emirates-nbd-elevates-customer-travel-experience-in-collaboration-with-visa-and-tripadvisor"
SMEVIP = "https://www.emiratesnbd.com/en/media-center/emirates-nbd-business-banking-launches-vip-privilege-program-for-smes"
DBOND = "https://www.emiratesnbd.com/en/media-center/emirates-nbd-issues-middle-easts-first-aed-denominated-digital-bond-on-euroclears-dfmi"
LIV = "https://www.liv.me/en"
LIVCC = "https://www.liv.me/en/liv-credit-card"
LIVTAM = "https://www.liv.me/en/liv-tamayaz-credit-card"
JAYNI = "https://gulfnews.com/business/banking/emirates-nbd-rolls-out-uaes-jaywan-debit-cards-signs-deal-with-network-international-1.500023445"
JAYID = "https://www.idemia.com/news/idemia-and-emirates-nbd-unveil-first-jaywan-prepaid-card-uae-2025-06-02/"
JAYKT = "https://www.khaleejtimes.com/business/finance/uae-jaywan-card-benefits-banks-travel-perks-how-to-apply?amp=1"
AANI = "https://www.centralbank.ae/media/eccjvuib/al-etihad-payments-launches-aani-a-instant-payments-platform-for-digital-transactions-in-the-uae-en.pdf"
NIIPO = "https://gulfnews.com/amp/story/business%2Fbanking%2Fthe-network-ipo-gets-10-times-oversubscription-1.63266480"
NIBROOK = "https://enterpriseam.com/uae/2024/09/19/fab-brookfield-take-over-network/"
NIMAG = "https://enterpriseam.com/uae/2025/10/02/network-international-magnati-finalize-merger/"
KSA21 = "https://www.emiratesnbd.com/en/media-center/emirates-nbd-expands-its-presence-in-the-saudi-market-with-the-official-opening-of-2-new-branches-in"
TOKEN16 = "https://www.fintechfutures.com/contactless-payments/emirates-nbd-launches-mobile-contactless-payments-solution"
AGENTPAY = "https://gulfnews.com/business/banking/now-use-ai-to-shop-in-dubai-after-new-mastercard-majid-al-futtaim-deal-1.500352104"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · Dubai · reach", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a balance sheet above AED 1.3 trillion, record profits, the Government of Dubai as majority owner, banks dating from 1963, a top-ranked AI programme, and RBL Bank in India bought in 2026.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "AED 1.3 trillion, record H1.", "div": "group", "rev": "rbwm", "products": [
            P("balance", "Balance sheet & earnings", "Profit before tax of AED 16.2 billion in H1 2026 (up 5%) and net profit of about AED 12.9 billion; total income AED 27.9 billion; total assets above AED 1.3 trillion, loans AED 771 billion and deposits AED 892 billion at 30 June 2026; cost of risk 42bp and impaired loans 2.1%. FY 2025 profit before tax AED 29.8 billion and net profit about USD 6.5 billion.",
              s=["con"], neo=[0, ""], src=[["H1 2026 results", H1], ["AGBI: H1 net profit, Jul 2026", AGBI], ["FY 2025 results", FY25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "Dubai owns 56%.", "div": "group", "rev": "rbwm", "products": [
            P("leadership", "Board & executive team", "Chairman Sheikh Ahmed bin Saeed Al Maktoum, Vice Chairman and MD Hesham Abdulla Al Qassim, Group CEO Shayne Nelson, CFO Patrick Sullivan; Marwan Hadi runs retail and wealth, Ahmed Al Qassim wholesale, Miguel Rio-Tinto digital and IT, Farid Al Mulla Emirates Islamic.",
              s=["corp"], neo=[0, ""], src=[["Emirates NBD: management team", MGMT], ["H1 2026 results", H1]]),
            P("heritage", "Heritage & ownership", "National Bank of Dubai (1963) and Emirates Bank International merged on 6 March 2007. Listed on the Dubai Financial Market at about USD 52 billion (June 2026), 56% owned by the Government of Dubai through ICD and Dubai Holding; more than 30,000 staff.",
              s=["con"], o="I", neo=[0, ""], src=[["Emirates NBD: about us", ABOUT], ["RBL completion filing, Jun 2026", RBL]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology & AI", "blurb": "Evident AI number one.", "div": "group", "rev": "rbwm", "products": [
            P("tech", "Cloud, APIs & AI", "Cloud-native platforms, 187 APIs, more than 50 AI initiatives and the region's first AI-powered contact centre (2025); ranked first in the inaugural Evident AI Index for Middle East and Africa banks (H1 2026).",
              s=["corp"], neo=[0, ""], src=[["FY 2025 results", FY25], ["H1 2026 results", H1]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Strategy & deals", "blurb": "RBL Bank, 60%.", "div": "group", "rev": "intl", "products": [
            P("strategy", "Strategy", "A \"data-first, digital-focused\" regional group: international operations give about 35% of income, Saudi lending grew 48% in 2025, and USD 30 billion of sustainable finance is targeted by 2030 (91% reached).",
              s=["corp"], neo=[0, ""], src=[["FY 2025 results", FY25], ["H1 2026 results", H1]]),
            P("rbldeal", "RBL Bank acquisition", "60% of India's RBL Bank for about USD 2.75 billion, announced 18 October 2025 and completed 18 June 2026: the largest foreign direct investment in Indian banking. It added AED 74 billion of assets.",
              s=["con", "corp"], st="new", ay="Jun 2026", o="A", neo=[None, "RBL card networks not checked."], src=[["RBL completion filing, Jun 2026", RBL], ["H1 2026 results", H1]]),
            P("network", "Network International (sold)", "Emirates NBD built Network International, the region's card processor, and cut its stake from 51% to 22.4% at the 2019 London listing, then sold more. Brookfield and First Abu Dhabi Bank took Network private in September 2024 and merged it with Magnati in 2025. When Emirates NBD fully exited is not confirmed ⚠.",
              s=["corp"], st="retired", o="I", neo=[0, ""],
              mc="The bank's old processor now belongs to a rival bank's group.",
              src=[["Gulf News: Network IPO, 2019", NIIPO], ["Enterprise AM: FAB and Brookfield take over Network, Sep 2024", NIBROOK], ["Enterprise AM: Network–Magnati merger, Oct 2025", NIMAG]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Eight ways money moves: Visa debit for every account, the UAE's largest credit-card book split between Visa and Mastercard, Mastercard travel cards, corporate and prepaid cards, the new Jaywan scheme, Emirates NBD Pay on Mastercard Gateway, Aani and Visa+ transfers, and digital bonds.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "All 16 cards on Visa.", "div": "enbd", "rev": "rbwm", "products": [
            P("debit", "Emirates NBD debit cards", "All 16 debit cards listed, from Visa Classic to Visa Infinite, Emirati, business and Manchester United cards, are Visa; a five-year Visa renewal in June 2020 gave Visa the bank's debit cards. Whether it was renewed again in 2025 is not public ⚠.",
              short="Debit (Visa)", s=["con", "prem", "sme"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              src=[["Emirates NBD: debit cards", DC], ["EPI: Visa five-year renewal, Jun 2020", VISA20]]),
            P("livdebit", "Liv debit & Multicurrency card", "Liv's debit card runs on Visa; the Multicurrency Visa card (H1 2026) holds five currencies and falls back to AED automatically.",
              s=["dig"], lc="everyday", st="new", o="P", at="Visa", neo=[0, "Visa."],
              src=[["H1 2026 results", H1], ["Liv", LIV]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "36% of UAE card spend.", "div": "enbd", "rev": "rbwm", "products": [
            P("visacc", "Visa credit & co-brands", "About 21 of 35 listed credit cards are Visa, including the flagship co-brands: Emirates Skywards, SHARE with Majid Al Futtaim (100,000 primary cards in its first year), U By Emaar, Aldar's Darna, Etihad Guest, noon One and Visa Infinite. Emirates NBD has 36% of UAE credit-card spend.",
              short="Credit co-brands (Visa)", s=["con", "prem"], lc="borrow", o="P", at="Visa", neo=[0, "Visa."],
              src=[["Emirates NBD: credit cards", CC], ["H1 2026 results", H1]]),
            P("mccc", "Mastercard credit cards", "About 12 listed credit cards are Mastercard: dnata World and Platinum, LuLu 247 Platinum and Titanium, Webshopper, Manchester United, Mastercard Platinum and Titanium, plus the Voyager and Marriott Bonvoy cards.",
              short="Credit (Mastercard)", s=["con", "prem"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="About a third of the UAE's largest card book.",
              src=[["Emirates NBD: credit cards", CC]]),
            P("diners", "Diners Club & Duo", "A Diners Club card, and Duo, which pairs a Diners Club card with a Mastercard Platinum card in one package.",
              s=["prem"], lc="borrow", o="P", at="Diners Club, Mastercard", neo=[1, "Duo includes a Mastercard."],
              src=[["Emirates NBD: credit cards", CC]]),
            P("livcc", "Liv credit cards", "Liv's Cashback card and the Tamayaz World and Platinum cards with Union Coop (10% back at Union Coop). Liv's pages show the World tier and Mastercard offers, so the cards look to be Mastercard ⚠.",
              s=["dig"], lc="borrow", st="new", o="P", at="Union Coop", neo=[2, "Mastercard ⚠ inferred."],
              src=[["Liv: credit card", LIVCC], ["Liv: Tamayaz", LIVTAM]]),
        ]},
        {"id": "2.3", "ic": "plane", "name": "Travel cards", "blurb": "Voyager and Marriott.", "div": "enbd", "rev": "rbwm", "products": [
            P("voyager", "Voyager Mastercard", "A travel card the bank owns itself (December 2025) on World Elite and World Mastercard: up to 12 Voyager Miles per AED on its own travel portal in the app, visa services from OneVasco, and Mastercard Travel Pass lounges.",
              short="Voyager (Mastercard)", s=["prem", "con"], lc="borrow", st="new", ay="Dec 2025", o="P", at="Mastercard", neo=[2, "World Elite and World Mastercard."],
              mc="The bank chose Mastercard for its own travel programme.",
              src=[["Emirates NBD: Voyager cards", VOYAGER], ["TechAfrica News: Voyager launch, Dec 2025", VOYLAUNCH]]),
            P("marriott", "Marriott Bonvoy Mastercard", "The existing Marriott card upgraded to World Elite Mastercard and a new World Mastercard added (March 2024), with up to 200,000 bonus points at launch.",
              s=["prem"], lc="borrow", ay="Mar 2024", o="P", at="Marriott, Mastercard", neo=[2, "World Elite and World Mastercard."],
              src=[["Marriott: co-brand cards, Mar 2024", MARRIOTT]]),
        ]},
        {"id": "2.4", "ic": "briefcase-business", "name": "Commercial & prepaid", "blurb": "Corporate, virtual, GlobalCash.", "div": "enbd", "rev": "cib", "products": [
            P("corpcards", "Corporate & virtual cards", "A Mastercard Corporate Card and a Visa Corporate Card, the Wholesale Travel Solution virtual card and Corporate Virtual Mobile Card (Mastercard ⚠ from card images), a DMCC corporate card and business credit cards (network not stated ⚠).",
              s=["sme", "corp"], lc="move", o="P", at="Mastercard, Visa", neo=[1, "Mastercard and Visa."],
              src=[["Emirates NBD: commercial cards", COMM]]),
            P("dpworld", "DP World corporate card", "A co-branded Mastercard corporate card with DP World for trade and logistics businesses (September 2024), with revolving credit and uncapped cashback.",
              s=["corp"], lc="move", ay="Sep 2024", o="P", at="DP World, Mastercard", neo=[2, "Mastercard."],
              src=[["Mastercard: DP World corporate card, Sep 2024", DPW]]),
            P("globalcash", "GlobalCash prepaid card", "A Mastercard prepaid travel card that holds up to 15 currencies.",
              s=["con"], lc="move", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["Emirates NBD: GlobalCash card", PREPAID]]),
        ]},
        {"id": "2.5", "ic": "flag", "name": "Jaywan", "blurb": "First Jaywan issuer.", "div": "enbd", "rev": "rbwm", "products": [
            P("jaywan", "Jaywan cards", "Emirates NBD issued the UAE's first Jaywan debit cards (January 2025), with Network International taking them at its 60,000 merchants, and the first Jaywan prepaid card with IDEMIA (June 2025). The national scheme launched in July 2026 with 11 issuers; banks must issue it, on its own or co-badged with a global network.",
              short="Jaywan (domestic)", s=["con", "dig"], lc="everyday", st="new", ay="Jan 2025", o="P", at="Al Etihad Payments, Network International", neo=[0, "Domestic scheme."],
              mc="Co-badging with Jaywan is the next network choice the bank makes.",
              src=[["Gulf News: first Jaywan cards, Jan 2025", JAYNI], ["IDEMIA: Jaywan prepaid, Jun 2025", JAYID], ["Khaleej Times: Jaywan, Jul 2026", JAYKT]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Acceptance", "blurb": "Emirates NBD Pay.", "div": "enbd", "rev": "cib", "products": [
            P("enbdpay", "Emirates NBD Pay", "Merchant payments platform on Mastercard Gateway (February 2025); the first acquirer in the world to offer Mastercard's Brighterion AI through that integration, for retail, hospitality and real-estate merchants. A broker went live on it in 2026 using Visa's Account Funding Transactions.",
              short="ENBD Pay (Mastercard Gateway)", s=["sme", "corp"], lc="move", st="new", ay="Feb 2025", o="P", at="Mastercard", neo=[3, "Mastercard Gateway and Brighterion."],
              mc="Mastercard runs the bank's acquiring gateway and its merchant risk model.",
              src=[["Mastercard: Gateway and Brighterion, Feb 2025", MCGW], ["H1 2026 results", H1]]),
        ]},
        {"id": "2.7", "ic": "zap", "name": "Instant & cross-border", "blurb": "Aani, Visa+, settlement.", "div": "enbd", "rev": "rbwm", "products": [
            P("aani", "Aani instant payments", "Emirates NBD was one of eight institutions live at the launch of Aani, the central bank's instant-payments platform, on 16 October 2023: transfers by mobile number, request-to-pay and QR payments.",
              s=["con", "dig", "sme"], lc="move", ay="Oct 2023", o="P", at="Al Etihad Payments", neo=[0, "Central bank rail."],
              src=[["CBUAE: Aani launch, Oct 2023", AANI]]),
            P("visaplus", "Visa+ transfers", "The first UAE bank on Visa+ (April 2025): send money to Visa cardholders across the GCC with a mobile or card number. DirectRemit covers other corridors.",
              s=["con"], lc="move", ay="Apr 2025", o="P", at="Visa", neo=[0, "Visa."],
              src=[["FinTech Global: Visa+, Apr 2025", VISAPLUS]]),
            P("nnss", "Visa settlement agent", "Visa's National Net Settlement Service agent in the UAE from 30 April 2026, settling domestic Visa transactions locally in AED.",
              s=["corp"], lc="move", st="new", ay="Apr 2026", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa now settles its UAE domestic volume through Emirates NBD.",
              src=[["Emirates NBD: Visa NNSS, Apr 2026", NNSS]]),
        ]},
        {"id": "2.8", "ic": "coins", "name": "Digital money", "blurb": "First AED digital bond.", "div": "group", "rev": "gmt", "products": [
            P("digitalbond", "AED digital bond", "AED 1 billion of three-year Digitally Native Notes on Euroclear's D-FMI ledger, listed on Nasdaq Dubai (19 January 2026): the first AED digital bond.",
              s=["corp"], lc="grow", st="new", ay="Jan 2026", o="P", at="Euroclear", neo=[0, ""],
              src=[["Emirates NBD: digital bond, Jan 2026", DBOND]]),
            P("crypto", "Liv crypto", "Crypto trading in the Liv X app with zero trading fees, and card rewards that can be redeemed for crypto.",
              s=["dig"], lc="grow", o="P", neo=[0, ""],
              src=[["Liv", LIV], ["Liv: credit card", LIVCC]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: fraud controls, AI from the contact centre to a travel assistant built with Visa, rewards and instalments on the UAE's biggest card book, and 187 APIs.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & risk", "blurb": "In-house, plus Brighterion.", "div": "enbd", "rev": "rbwm", "products": [
            P("fraud", "Fraud & security", "Card and account fraud controls, with Brighterion scoring for merchants on Emirates NBD Pay. The bank's own issuer fraud tools are not public ⚠.",
              s=["con", "sme"], lc="everyday", neo=[None, "Issuer tools not public."],
              mc="Issuer-side scam and fraud scoring is untested ground.",
              src=[["Mastercard: Gateway and Brighterion, Feb 2025", MCGW]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI for customers", "blurb": "Contact centre, travel.", "div": "enbd", "rev": "rbwm", "products": [
            P("aicontact", "AI contact centre", "The region's first AI-powered contact-centre platform (2025), with 24/7 support, among more than 50 AI initiatives.",
              s=["con"], lc="everyday", st="new", neo=[0, ""],
              src=[["FY 2025 results", FY25]]),
            P("aitravel", "AI Travel Assistant", "Billed as the UAE's first bank-led AI travel assistant (5 October 2026), built with Visa and Tripadvisor: itineraries from conversation, with Visa cardholder offers, open to anyone without a login.",
              s=["con", "prem"], lc="beyond", st="new", ay="Oct 2026", o="P", at="Visa, Tripadvisor", neo=[0, "Visa."],
              mc="Mastercard took the UAE's first Agent Pay transaction in 2025, but this went to Visa.",
              src=[["Emirates NBD: AI Travel Assistant, Oct 2026", AITRAVEL], ["Gulf News: Agent Pay in the UAE, Nov 2025", AGENTPAY]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Rewards & instalments", "blurb": "Plus Points, Skywards, 0%.", "div": "enbd", "rev": "rbwm", "products": [
            P("rewards", "Rewards & offers", "Plus Points, Skywards Miles, Darna and SHARE points, Voyager Miles, a Rewards Hub in ENBD X (H1 2026) and dining, travel and 0% offers.",
              s=["con", "prem"], lc="grow", neo=[1, "Rewards on both networks."],
              src=[["Emirates NBD: credit cards", CC], ["H1 2026 results", H1]]),
            P("instalments", "Instalments & card credit", "Instalment plans on purchases, balance conversion and transfer, and loans within and beyond the card limit.",
              s=["con"], lc="borrow", neo=[1, "On Visa and Mastercard cards."],
              src=[["Emirates NBD: credit cards", CC]]),
        ]},
        {"id": "3.4", "ic": "code-xml", "name": "APIs & data", "blurb": "187 APIs.", "div": "group", "rev": "cib", "products": [
            P("apis", "APIs & API banking", "187 APIs integrated by 2025, and API banking for corporate clients.",
              s=["corp", "sme"], lc="open", neo=[0, ""],
              src=[["FY 2025 results", FY25]]),
            P("carbon", "Carbon Calculator", "A carbon calculator linking spending to its environmental impact (H1 2026). The provider is not named.",
              s=["con"], lc="beyond", st="new", neo=[None, "Provider not named."],
              src=[["H1 2026 results", H1]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: retail loans and USD 105 billion of wealth, business banking, corporate and investment banking, Emirates Islamic, and banks in Türkiye, Egypt, Saudi Arabia and India.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Retail & wealth", "blurb": "USD 105bn AUM.", "div": "enbd", "rev": "rbwm", "products": [
            P("retail", "Retail banking", "Accounts, loans and cards for UAE residents, with retail loans up 9% in H1 2026, record retail CASA growth of AED 44 billion in 2025 and a Net Promoter Score of 58.",
              s=["con"], lc="everyday", neo=[0, "Visa debit."], src=[["H1 2026 results", H1], ["FY 2025 results", FY25]]),
            P("wealth", "Priority, private & digital wealth", "USD 105 billion of assets under management and administration, Digital Wealth trading above AED 40 billion in 2025, and Emirates NBD Gold.",
              s=["prem"], lc="grow", neo=[0, ""], src=[["H1 2026 results", H1], ["FY 2025 results", FY25]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "Business banking", "blurb": "VIP Privilege for SMEs.", "div": "enbd", "rev": "rbwm", "products": [
            P("sme", "Business Banking", "Accounts, cards and finance for SMEs; the VIP Privilege Program (7 October 2026) is built around a Visa Infinite Business Debit Card.",
              s=["sme"], lc="everyday", st="new", neo=[0, "Visa Infinite Business Debit."], src=[["Emirates NBD: SME VIP Privilege, Oct 2026", SMEVIP]]),
        ]},
        {"id": "4.3", "ic": "building-2", "name": "Corporate & institutional", "blurb": "Loans up 12%.", "div": "enbd", "rev": "cib", "products": [
            P("cib", "Corporate, institutional & investment banking", "Corporate loans up 12% in H1 2026; Emirates NBD Capital led more than 55 debt deals; transaction banking and trade.",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["H1 2026 results", H1]]),
        ]},
        {"id": "4.4", "ic": "gem", "name": "Islamic banking", "blurb": "AED 250bn Islamic assets.", "div": "ei", "rev": "islamic", "products": [
            P("islamic", "Emirates Islamic", "Record profit before tax of AED 3.9 billion in 2025; with the group's Islamic window, Islamic assets above AED 250 billion. Card networks not checked ⚠.",
              s=["isl"], lc="everyday", neo=[None, "Card networks not checked."], src=[["FY 2025 results", FY25], ["H1 2026 results", H1]]),
        ]},
        {"id": "4.5", "ic": "globe", "name": "International", "blurb": "Türkiye, Egypt, India, Saudi.", "div": "group", "rev": "intl", "products": [
            P("deniz", "DenizBank", "The group's Turkish bank, bought in 2019, where income recovered as inflation eased in 2025.",
              s=["con", "corp"], o="A", neo=[None, "Card networks not checked."], src=[["FY 2025 results", FY25], ["Emirates NBD: our journey", JOURNEY]]),
            P("egypt", "Emirates NBD Egypt", "A partnership with Mastercard (January 2024), co-branded Talaat Mostafa Group Mastercard cards (2025) and ENBD X launched in Egypt (2026).",
              s=["con"], lc="everyday", st="new", o="P", at="Mastercard", neo=[1, "Mastercard partner and co-brands."],
              src=[["Mastercard: Emirates NBD-Egypt, Jan 2024", MCEG], ["Egypt Today: TMG cards, 2025", TMG], ["H1 2026 results", H1]]),
            P("ksa", "Emirates NBD KSA", "Branches across the Kingdom of Saudi Arabia, 24 planned by early 2026, with lending up 48% in 2025, and Emirates NBD Capital KSA.",
              s=["con", "corp"], neo=[None, "Card networks not checked."], src=[["FY 2025 results", FY25], ["Emirates NBD: Saudi branches, Apr 2021", KSA21]]),
            P("rbl", "RBL Bank", "India's RBL Bank, 60% owned since June 2026, adding AED 44 billion of loans and AED 43 billion of deposits.",
              s=["con", "sme"], st="new", ay="Jun 2026", o="A", neo=[None, "Card networks not checked."], src=[["RBL completion filing, Jun 2026", RBL], ["H1 2026 results", H1]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the ENBD X app, Liv for digital natives, 1,425 branches and almost 5,000 ATMs, businessONLINE, and the brands whose cards it issues.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "ENBD X & businessONLINE", "blurb": "2.5 million active users.", "div": "enbd", "rev": "rbwm", "products": [
            P("app", "ENBD X app", "Mobile platforms with more than 2.5 million active users across the UAE and Saudi Arabia (2025), launched in Egypt in 2026; 97% of transactions happen outside branches.",
              s=["con", "prem"], lc="everyday", neo=[0, ""], src=[["FY 2025 results", FY25], ["Emirates NBD: our journey", JOURNEY]]),
            P("bizonline", "businessONLINE", "The digital channel for business and corporate clients, with real-time service for VIP Privilege members.",
              s=["sme", "corp"], lc="everyday", neo=[0, ""], src=[["Emirates NBD: SME VIP Privilege, Oct 2026", SMEVIP]]),
        ]},
        {"id": "5.2", "ic": "rocket", "name": "Liv", "blurb": "Half a million customers.", "div": "liv", "rev": "rbwm", "products": [
            P("liv", "Liv digital bank", "The UAE's first digital bank (2017), with more than half a million customers, accounts opened in under three minutes, the Liv X and Liv Lite family apps, savings, gold and crypto.",
              s=["dig"], lc="open", o="B", neo=[1, "Visa debit, Mastercard credit ⚠."], src=[["Liv", LIV], ["Emirates NBD: our journey", JOURNEY]]),
        ]},
        {"id": "5.3", "ic": "building", "name": "Branches & partners", "blurb": "1,425 branches.", "div": "group", "rev": "rbwm", "products": [
            P("branches", "Branches & ATMs", "1,425 branches and 4,948 ATMs and deposit machines across the group, including DenizBank and RBL.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["Emirates NBD: our journey", JOURNEY]]),
            P("partners", "Co-brand partners", "Emirates, Etihad, Majid Al Futtaim, Emaar, Aldar, noon, Amazon, Marriott, dnata, LuLu, DP World and Manchester United, among others; Emaar, Aldar, Majid Al Futtaim and Amazon cards came in 2025.",
              s=["con", "prem"], lc="beyond", o="P", neo=[1, "Most big co-brands on Visa; travel and retail ones on Mastercard."],
              src=[["Emirates NBD: credit cards", CC], ["FY 2025 results", FY25]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Emirates NBD", "blurb": "A Visa bank with a real second network.", "products": [
        P("mcatenbd", "Mastercard at Emirates NBD", "Visa carries every debit card, the biggest co-brands, domestic settlement and the new AI travel assistant. Mastercard carries about a third of the credit cards (Voyager, Marriott Bonvoy, dnata, LuLu), Liv's credit cards ⚠, GlobalCash, corporate cards and Egypt's co-brands, and runs Emirates NBD Pay's gateway and Brighterion merchant risk.",
          s=["con"], div="group", rev="rbwm", mc="The relationship this map is drawn for.",
          src=[["Emirates NBD: credit cards", CC], ["Mastercard: Gateway and Brighterion, Feb 2025", MCGW], ["Emirates NBD: Visa NNSS, Apr 2026", NNSS]]),
    ]},
    {"id": "pillar-market", "name": "UAE payments", "blurb": "Jaywan, Aani, Visa onshore.", "products": [
        P("market", "The UAE market", "The central bank's programme has added Aani instant payments (2023) and the Jaywan card scheme (2025–26), which every bank must issue. Network International, which Emirates NBD built, now belongs to Brookfield and First Abu Dhabi Bank.",
          s=["con"], div="group", rev="rbwm", src=[["CBUAE: Aani launch, Oct 2023", AANI], ["Khaleej Times: Jaywan, Jul 2026", JAYKT], ["Enterprise AM: FAB and Brookfield take over Network, Sep 2024", NIBROOK]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
