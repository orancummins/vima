"""Citi's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Citi's own unless a source says otherwise: the 3Q26 results (13 October 2026) and the
Investor Day decks and transcripts (7 May 2026). ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product or network runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not
Mastercard, None = nothing public.
"""
# ruff: noqa: E501

from citi_foundation import DATA_AI, FOUNDATION, VENTURES

_CG = "https://www.citigroup.com/rcs/citigpa/storage/public/"
Q3 = _CG + "Earnings/Q32026/2026prqtr3rslt.pdf"
Q3S = _CG + "Earnings/Q32026/2026psqtr3rslt.pdf"
IDS = _CG + "investor-day/citi-ID26-services-presentation.pdf"
IDST = _CG + "investor-day/citi-ID26-services-presentation-transcript.pdf"
IDC = _CG + "investor-day/citi-ID26-us-consumer-cards-presentation.pdf"
IDCT = _CG + "investor-day/citi-ID26-us-consumer-cards-presentation-transcript.pdf"
IDW = _CG + "investor-day/citi-ID26-wealth-presentation.pdf"
IDM = _CG + "investor-day/citi-ID26-markets-presentation.pdf"
IDB = _CG + "investor-day/citi-ID26-banking-presentation.pdf"
PR = "https://www.citigroup.com/global/news/press-release/"
MCPR = "https://www.mastercard.com/us/en/news-and-trends/press/"
CARDS = "https://www.citi.com/credit-cards/compare/view-all-credit-cards"
MC_ISSUER = "https://www.mastercard.com/us/en/personal/find-a-card/credit-card/issuers/citi.html"
MC2015 = "https://www.pymnts.com/news/2015/citi-and-mastercard-sign-new-ten-year-deal/"
AA2024 = "https://citigroup.com/global/news/press-release/2024/american-airlines-and-citi-extend-and-expand-co-branded-card-partnership-paving-the-way-for-more-customer-benefits"
COSTCO = "https://investor.visa.com/news/news-details/2015/Costco-Enters-Into-a-Long-Term-Co-Brand-Credit-Card-Agreement-With-Citi-and-an-Acceptance-and-Co-Brand-Agreement-With-Visa/default.aspx"
MOVE = PR + "2024/citi-mastercard-global-cross-border-payments-join-forces"
INSTALL = MCPR + "2025/october/mastercard-and-citi-bring-citi-flex-pay-installments-to-more-ret.html"
INCONTROL = MCPR + "2026/july/Mastercard-expands-virtual-card-platform.html"
CTS26 = PR + "2026/citi-token-services-expands-global-footprint-japan-united-arab-emirates"
CTS25 = PR + "2025/citi-integrates-citi-token-services-with-24-7-usd-clearing-real-time-cross-border-payments-liquidity-management"
STRATA_ELITE = PR + "2025/citi-launches-citi-strata-elite-credit-card"
AAEXEC = PR + "2026/american-airlines-citi-elevate-premium-travel-enhanced-citi-aadvantage-executive-world-legend-mastercard"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves through Citi: consumer cards on Mastercard (and Costco on Visa), commercial and virtual cards, about $6 trillion a day of institutional payments and clearing, WorldLink cross-border, tokenised deposits that settle around the clock, and Spring by Citi for merchants.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Consumer cards & wallets", "blurb": "Mastercard for Citi's own cards, Visa for Costco.", "div": "uscc", "rev": "uscc", "products": [
            P("mcdeal", "Citi–Mastercard network agreement", "In March 2015 Citi and Mastercard signed a new and expanded ten-year agreement that moved Citi's proprietary US consumer credit and debit cards to Mastercard; co-brand and commercial cards stayed multi-network. A ten-year Middle East agreement followed in 2018, and Citi is still moving its remaining Visa cards in Asia: the Citi Rewards Visa in Singapore was discontinued on 15 October 2026. No renewal of the 2015 deal has been reported.", short="Mastercard network agreement",
              s=["con", "aff"], lc="move", o="P", at="Mastercard", ay="Mar 2015", neo=[3, "The agreement that puts Citi's own cards on Mastercard."],
              mc="The installed base: every Citi-branded credit and debit card in the US. Its ten-year term from 2015 makes the renewal, which nobody has reported, the most important open question in the relationship.",
              rel=["brandedcards", "aacards", "debit"], src=[["PYMNTS: Citi and Mastercard sign new ten-year deal, Mar 2015", MC2015], ["EPI: ten-year Middle East agreement, Aug 2018", "https://www.electronicpaymentsinternational.com/news/citi-mastercard-ink-10-year-agreement-to-extend-relationship-in-middle-east-180815-4648777"], ["MileLion: Citi Rewards Visa discontinued in Singapore, Jul 2026", "https://milelion.com/2026/07/12/citi-rewards-visa-to-be-discontinued-on-15-october-2026/"]]),
            P("debit", "Citibank debit cards", "US Citibank debit cards carry the Mastercard logo; Mastercard was also chosen for the Citi Plex account with Google Pay in 2020.",
              s=["con", "aff"], lc="everyday", o="P", at="Mastercard", neo=[2, "Debit Mastercard."],
              src=[["Citi: debit card", "https://www.citi.com/online-services/debit-card"], ["Mastercard: network partner for Citi Plex, Nov 2020", "https://newsroom.mastercard.com/news/press/2020/november/citi-selects-mastercard-as-network-partner-for-the-citi-plex-account-by-google-pay/"]]),
            P("wallets", "Apple Pay, Google Pay, Samsung Pay & Paze", "Citi cards are in all three phone wallets, and Citi Flex Pay installments now work inside them through Mastercard Installments. In March 2026 Citi became the first bank outside the owner group to join Paze, Early Warning's bank-run checkout wallet.", short="Wallets & Paze",
              s=["con"], lc="move", o="P", at="Apple, Google, Samsung, Early Warning", st="new", ay="Mar 2026", neo=[1, "Mastercard tokens behind Citi's Mastercard cards; Paze is a rival checkout."],
              mc="Tokens (MDES) and Click to Pay sit under every Mastercard-badged Citi card in a wallet; Paze is the bank-owned alternative Citi has just joined, which makes passkeys and Click to Pay the argument to win.",
              src=[["Payments Dive: EWS pairs with Citi to offer Paze, Mar 2026", "https://www.paymentsdive.com/news/ews-pairs-with-citi-to-offer-paze/815023/"], ["Mastercard and Citi: Flex Pay in wallets, Oct 2025", INSTALL]]),
            P("costcovisa", "Costco Anywhere Visa", "Citi has been Costco's exclusive card issuer since the June 2016 conversion from American Express, on Visa. Costco exercised its three-year extension, so the term runs to 19 June 2029; new accounts grew 19% in 2025.", short="Costco Anywhere Visa",
              s=["con", "sme"], lc="move", o="P", at="Costco, Visa", neo=[0, "Visa."],
              mc="The largest Citi programme not on Mastercard, with its term ending in June 2029.",
              src=[["Visa and Costco, Mar 2015", COSTCO], ["YMMV: the future of the Costco Anywhere card, Aug 2025", "https://yourmileagemayvary.com/2025/08/08/the-future-of-the-costco-anywhere-card/"], ["Investor Day 2026: U.S. Consumer Cards", IDC]]),
        ]},
        {"id": "2.2", "ic": "wallet-cards", "name": "Commercial & virtual cards", "blurb": "$20bn a quarter of business spend.", "div": "svc", "rev": "svc", "products": [
            P("commcards", "Citi Commercial Cards", "Corporate travel and expense, purchasing, fleet and virtual cards for companies and governments; global commercial card spend was $20 billion in 3Q26, up 10%. A mix of Visa and Mastercard; Citi withdrew commercial cards in Singapore on 30 June 2026.",
              s=["corp", "sme", "gov"], lc="move", o="B", neo=[1, "Visa and Mastercard; no public programme-level split."],
              mc="Mastercard's commercial products (In Control, Commercial Connect, Smart Data) already run the virtual side; the physical T&E and purchasing book is shared with Visa.",
              src=[["3Q26 results", Q3], ["Visa: travel card providers", "https://usa.visa.com/supporting-info/travel-card-provider.html"]]),
            P("vca", "Citi Virtual Card Account", "Single-use and multi-use virtual card numbers for B2B payments, in local currency in about 50 countries, built on Mastercard In Control since 2009. In July 2026 Citi went live on Mastercard's upgraded In Control (issuer-enforced and clearing controls, the Commercial Connect API) and will be first to roll it out globally.", short="Virtual Card Account",
              s=["corp", "sme"], lc="move", o="P", at="Mastercard", ay="2009", st="new", neo=[3, "Runs on Mastercard In Control."],
              mc="Mastercard In Control is the engine; Citi is its launch issuer for the 2026 upgrade.",
              src=[["Mastercard expands its virtual card platform, Jul 2026", INCONTROL], ["The Global Treasurer: Citi launches multicurrency virtual card platform, Aug 2009", "https://www.theglobaltreasurer.com/2009/08/27/citi-launches-multicurrency-virtual-card-platform-for-institutions/"]]),
            P("smartpay", "GSA SmartPay 3", "One of two banks (with U.S. Bank) on the US federal government's purchase, travel and fleet card master contract, 2018 to 2031.",
              s=["gov"], lc="move", o="P", at="U.S. General Services Administration", neo=[None, "Visa lists Citibank as a SmartPay bank; the split is not public."],
              src=[["GSA SmartPay master contract", "https://smartpay.gsa.gov/about/master-contract/"], ["Citi: GSA SmartPay", "https://www.citi.com/tts/sa/federal-government-benefits/gsa.html"]]),
        ]},
        {"id": "2.3", "ic": "arrow-left-right", "name": "Payments & clearing", "blurb": "About $6 trillion a day.", "div": "svc", "rev": "svc", "products": [
            P("payflows", "Citi payments", "Citi's institutional payments franchise processes about $6 trillion a day to more than 180 countries for about 17,000 clients, including about 80% of the Fortune 500; Coalition Greenwich ranks Treasury and Trade Solutions first in payments with an 11.6% share.", short="$6tn a day of payments",
              s=["corp", "inst", "gov", "sme"], lc="move", neo=[0, "Citi's own rails and the clearing systems."],
              src=[["Investor Day 2026: Services", IDS], ["Citi Perspectives: payments, 2026", "https://www.citigroup.com/global/news/perspectives/2026/big-small-everything-in-between-debo-sen-citi-industry-leading-payments-business"]]),
            P("cpe", "Citi Payments Express", "Citi's instant and low-value payments engine, live in 22 markets, processing up to about 10 million payments a day (December 2025), around 40% of Citi's payment count, at 99.9% availability. Built for e-commerce, fintechs, payroll and gig platforms.",
              s=["corp", "fin"], lc="move", neo=[0, "Account-to-account."],
              src=[["Investor Day 2026: Services", IDS]]),
            P("usd247", "Citi 24/7 USD Clearing", "Always-on US dollar clearing for banks, with more than 300 live by December 2025; Citi clears for about 1,500 financial institutions and processed 47 million USD clearing instructions in 3Q26.",
              s=["inst"], lc="move", neo=[0, ""],
              src=[["Investor Day 2026: Services", IDS], ["3Q26 results", Q3]]),
            P("zelle", "Zelle", "Person-to-person payments in the Citi Mobile app. Citi participates in Zelle but is not one of Early Warning's owner banks.",
              s=["con"], lc="move", o="P", at="Early Warning Services", neo=[0, ""],
              src=[["Payments Dive: EWS and Citi, Mar 2026", "https://www.paymentsdive.com/news/ews-pairs-with-citi-to-offer-paze/815023/"]]),
        ]},
        {"id": "2.4", "ic": "globe", "name": "Cross-border & FX", "blurb": "WorldLink, 135-plus currencies.", "div": "svc", "rev": "svc", "products": [
            P("worldlink", "WorldLink cross-border payments", "Cross-border payments in more than 135 currencies and 4,500 currency pairs, to more than 150 digital destinations including bank accounts, wallets and cards. Cross-border transaction value was $116 billion in 3Q26, up 10%. Since October 2024 WorldLink pays out to Mastercard debit cards through Mastercard Move, first in 14 markets.", short="WorldLink",
              s=["corp", "inst", "gov"], lc="move", o="B", neo=[1, "Card payouts through Mastercard Move; the rest on bank rails."],
              mc="Mastercard Move already carries WorldLink's card payouts; more corridors and wallet endpoints are the obvious next step.",
              rel=["payex"], src=[["Citi and Mastercard join forces on cross-border payments, Oct 2024", MOVE], ["3Q26 results", Q3]]),
            P("swiftinstant", "Swift instant cross-border payments", "In September 2026 Citi became the first bank live with several markets (AUD, GBP, INR and USD) on Swift's new instant cross-border payments scheme.",
              s=["corp", "inst"], lc="move", st="new", ay="Sep 2026", o="P", at="Swift", neo=[0, ""],
              src=[["Citi: first bank on Swift's multi-market instant payments", PR + "2026/citi-first-bank-launch-multi-market-instant-payments-swift-payments-scheme"]]),
            P("payex", "Citi Payment Exchange", "Business-to-consumer payouts where the payee chooses how to be paid (account, wallet or card), aimed at gig, creator and marketplace platforms; wallet payouts to the Philippines, Indonesia, Bangladesh and Colombia through Dandelion (a Euronet company) since September 2025.",
              s=["fin", "corp", "gov"], lc="move", o="P", at="Dandelion", neo=[1, "Card endpoints through Mastercard Move."],
              mc="A payee-choice payout is exactly what Move's card, account and wallet reach is for.",
              src=[["Citi: reimagining payouts", "https://www.citigroup.com/global/insights/reimagining-payouts-simplifying-the-payment-experience-while-providing-impactful-optionality"]]),
        ]},
        {"id": "2.5", "ic": "network", "name": "Tokenised & digital money", "blurb": "Deposits that move at 3 a.m.", "div": "svc", "rev": "svc", "products": [
            P("cts", "Citi Token Services", "Tokenised deposits on a private permissioned blockchain that Citi runs, for 24/7 cross-border treasury and liquidity. Announced September 2023, commercial from 2024 in the US, UK, Singapore and Hong Kong, then the euro (November 2025), Japan and the UAE (28 September 2026), seven markets in all; joined to 24/7 USD Clearing in September 2025. Citi cites close to $1 billion a day.",
              s=["corp", "inst"], lc="move", st="new", ay="2024", neo=[0, "No public link to Mastercard's Multi-Token Network."],
              mc="Mastercard's Multi-Token Network and card-funded stablecoin flows are the bridge nobody has announced.",
              src=[["Citi Token Services expands to Japan and the UAE, Sep 2026", CTS26], ["Citi Token Services joins 24/7 USD Clearing, Sep 2025", CTS25], ["Investor Day 2026: Services transcript", IDST]]),
            P("digassets", "Stablecoins & crypto custody", "A Coinbase collaboration (October 2025) for stablecoin on- and off-ramps for clients, native crypto custody being launched in 2026, and a tokenised money-market fund under evaluation. Citi says its token infrastructure would let it issue a Citi stablecoin but remains 'open-minded' after the GENIUS Act (July 2025).",
              s=["inst", "corp"], lc="move", st="flux", ay="Oct 2025", o="P", at="Coinbase", neo=[0, ""],
              src=[["CoinDesk: Citi and Coinbase, Oct 2025", "https://www.coindesk.com/business/2025/10/27/wall-street-bank-citi-coinbase-partner-to-expand-digital-asset-payments"], ["Investor Day 2026: Services transcript", IDST]]),
        ]},
        {"id": "2.6", "ic": "store", "name": "Merchant acceptance", "blurb": "Spring by Citi.", "div": "svc", "rev": "svc", "products": [
            P("spring", "Spring by Citi", "E-commerce acceptance for Citi's corporate clients: cards, local payment methods, direct debit and QR or instant payments, settled straight into Citi accounts, in about two dozen markets. Launched 2019 with Global Processing (now Thredd) and PPRO.",
              s=["corp", "sme"], lc="move", o="P", at="Thredd, PPRO", ay="2019", neo=[1, "Accepts Mastercard among many methods."],
              mc="A corporate acquirer that sees its clients' sales: merchant identification, Gateway-style reporting and Click to Pay acceptance fit.",
              src=[["Citi Services: payments", "https://www.citigroup.com/global/businesses/services/payments"]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account and payment: decide the risk, keep money safe, let other software in, learn from the data, reward the customer, find merchant-funded value, and answer when they call.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Risk, fraud & controls", "blurb": "The transformation's core.", "div": "citi", "rev": "grp", "products": [
            P("cardrisk", "Card fraud & servicing AI", "Machine-learning fraud and servicing across U.S. Consumer Cards, with gen-AI for collections, complaint detection and agent assist (cutting about 60 seconds off a call).",
              s=["con"], lc="everyday", neo=[None, "Nothing public on Decision Intelligence or Brighterion at Citi."],
              mc="Decision Intelligence and Brighterion score the same transactions Citi's models do; there is no public sign Citi uses them.",
              src=[["Investor Day 2026: U.S. Consumer Cards", IDC]]),
            P("kyc", "Client onboarding & KYC", "Institutional onboarding and know-your-customer for about 17,000 Services clients in 90-plus countries, one of the areas the 2020 consent orders required Citi to rebuild.",
              s=["corp", "inst", "gov"], lc="open", neo=[0, ""],
              src=[["Investor Day 2026: Services", IDS]]),
        ]},
        {"id": "3.2", "ic": "gauge", "name": "Credit decisioning", "blurb": "+100bp approvals, same risk.", "div": "uscc", "rev": "uscc", "products": [
            P("underwrite", "AI underwriting", "New machine-learning models aim to lift card approval rates by about 100 basis points within the same risk appetite; 85% of US card loans are to borrowers with FICO scores of 660 or more.",
              s=["con"], lc="borrow", st="new", neo=[0, ""],
              src=[["Investor Day 2026: U.S. Consumer Cards", IDC]]),
            P("flexdecide", "Installment decisioning", "Instant eligibility for Flex Pay and Flex Loan against an existing card line, in the app, online and at checkout.",
              s=["con"], lc="borrow", neo=[1, "Exposed at checkout through Mastercard Installments."],
              rel=["flexpay", "flexloan"], src=[["Mastercard and Citi: Flex Pay at checkout, Oct 2025", INSTALL]]),
        ]},
        {"id": "3.3", "ic": "webhook", "name": "APIs & open finance", "blurb": "10 billion API calls since 2022.", "div": "svc", "rev": "svc", "products": [
            P("citiconnect", "CitiConnect & Citi APIs", "Host-to-host files, APIs, an ERP Integrator and the developer portal at developer.citi.com: more than 10 billion API calls from 2022 to 2025.",
              s=["corp", "fin"], lc="beyond", neo=[0, ""],
              src=[["Investor Day 2026: Services", IDS], ["Treasury Management International: Citi launches treasury APIs", "https://treasury-management.com/news/citi-launches-apis-for-treasury-services"]]),
            P("openfin", "Open finance & Section 1033", "The CFPB's 2024 personal financial data rule is enjoined and being rewritten (a reconsideration went to OIRA in August 2026), reopening whether banks may charge aggregators. Citi has published no stance of its own; JPMorgan began charging and signed Plaid in 2025. Citi's 2020 open-banking marketplace named Finicity among its first data partners.",
              s=["fin", "con"], lc="beyond", st="flux", neo=[None, "A 2020 Finicity link; nothing since."],
              mc="Whatever the rewritten 1033 rule allows, Citi will need data-access agreements and a consent layer: Mastercard Open Finance (Finicity) is where that lands.",
              src=[["Consumer Finance Monitor: new 1033 proposal to OIRA, Aug 2026", "https://www.consumerfinancemonitor.com/2026/08/06/cfpb-sends-new-section-1033-open-banking-proposal-to-oira-for-review/"], ["FinTech Global: Citi's open-banking marketplace, Dec 2020", "https://fintech.global/2020/12/21/citi-builds-fintech-open-banking-marketplace-for-fintechs/"]]),
        ]},
        {"id": "3.4", "ic": "brain", "name": "Data & AI", "blurb": "Agents for clients, bankers and coders.", "div": "citi", "rev": "grp", "products": DATA_AI},
        {"id": "3.5", "ic": "gift", "name": "Loyalty & rewards", "blurb": "ThankYou points, AAdvantage miles.", "div": "uscc", "rev": "uscc", "products": [
            P("thankyou", "Citi ThankYou Rewards", "Citi's points currency, with more than 14 million eligible customers, 19 transfer partners (American AAdvantage since July 2025, the only major transferable currency that moves into it), 18 Shop with Points partners and more than 175 gift cards.", short="ThankYou Rewards",
              s=["con", "aff"], lc="grow", neo=[0, "Citi's own currency."],
              mc="Points are Citi's most expensive benefit: rewards and partner costs pushed U.S. Consumer Cards' non-interest revenue down 62% in 3Q26, which is the case for merchant-funded value.",
              src=[["Investor Day 2026: U.S. Consumer Cards", IDC], ["Frequent Miler: ThankYou transfer partners", "https://frequentmiler.com/citi-thankyou-rewards-airline-and-hotel-transfer-partners/"]]),
            P("cititravel", "Citi Travel with Booking.com", "Citi's travel portal since March 2023, run by Rocket Travel by Agoda (Booking Holdings): more than 600 travel partners and The Reserve hotel collection; programme spend grew 32% from 2022 to 2025. Strata Elite earns 12x on hotels and cars booked here.",
              s=["con", "aff"], lc="beyond", o="P", at="Booking Holdings", ay="Mar 2023", neo=[0, ""],
              src=[["NerdWallet: Citi's Booking.com travel portal", "https://www.nerdwallet.com/article/travel/citi-booking-com-new-travel-portal"], ["Investor Day 2026: U.S. Consumer Cards", IDC]]),
            P("priceless", "Priceless, World Legend & The Curated Table", "Mastercard's premium layer on Citi's top cards: Strata Elite was the first World Legend card (July 2025) and the AAdvantage Executive became one in August 2026, with the Mastercard Collection and Priceless; The Curated Table dining series for Strata Elite runs with Mastercard (fall 2026: New York, Austin with McLaren, Miami).", short="Priceless & World Legend",
              s=["aff", "con"], lc="beyond", o="P", at="Mastercard", st="new", ay="Jul 2025", neo=[3, "Mastercard's own benefits."],
              src=[["Citi launches Strata Elite, Jul 2025", STRATA_ELITE], ["AAdvantage Executive World Legend, Aug 2026", AAEXEC], ["Citi and Mastercard: The Curated Table, fall 2026", PR + "2026/citi-mastercard-expand-the-curated-table-series-fall-2026-premium-dining-experiences"]]),
            P("citient", "Citi Entertainment", "Presale and preferred tickets for Live Nation and Ticketmaster events, unlocked by card or account linking.",
              s=["con", "aff"], lc="beyond", o="P", at="Live Nation, Ticketmaster", neo=[0, ""],
              src=[["Citi Entertainment: account linking", "https://citientertainment.com/landing/accountlinking_faq"]]),
        ]},
        {"id": "3.6", "ic": "sparkles", "name": "Commerce & offers", "blurb": "Merchant-funded value.", "div": "uscc", "rev": "uscc", "products": [
            P("offers", "Citi Merchant Offers & commerce media", "Card-linked offers since 2022 and a commerce-media pilot. Citi's cards head wants merchant-funded benefits 'to reduce our dependency on expensive, points-based rewards'; Citi was named a partner in Mastercard Commerce Media in October 2025.", short="Merchant Offers & commerce media",
              s=["con", "fin"], lc="beyond", st="new", o="P", at="Mastercard Commerce Media", neo=[2, "A Mastercard Commerce Media partner."],
              mc="Mastercard Commerce Media and card-linked offers are the merchant-funded layer Citi says it wants.",
              src=[["Marketing Dive: Mastercard's commerce media network, Oct 2025", "https://www.marketingdive.com/news/mastercard-bigger-grab-commerce-media-dollars-new-network/761568/"], ["Investor Day 2026: U.S. Consumer Cards transcript", IDCT]]),
            P("kard", "Kard acquisition", "Citi agreed in August 2026 to buy Kard, a merchant-funded rewards and commerce-media platform, terms undisclosed; not yet reported as closed.",
              s=["con", "fin"], lc="beyond", st="new", ay="Aug 2026", o="A", neo=[0, "Citi's own."],
              mc="Buying its own offers engine is a signal of how much Citi wants this layer; Mastercard's merchant reach and data are the complement, or the competitor.",
              src=[["American Banker: what Citi gets from Kard", "https://www.americanbanker.com/payments/news/what-citi-gets-from-its-kard-acquisition"]]),
            P("agentpay", "Mastercard Agent Pay", "Citi and U.S. Bank Mastercard holders were first to get Mastercard Agent Pay (September 2025), so AI agents can pay with tokenised Citi cards. Citi's cards head says the aim is to keep Citi cards top-of-wallet when agents shop.",
              s=["con"], lc="move", st="new", ay="Sep 2025", o="P", at="Mastercard", neo=[3, "Mastercard's own."],
              src=[["Banking Exchange: Citi and U.S. Bank to pilot Agent Pay, Sep 2025", "https://www.bankingexchange.com/news-feed/item/10413-citi-u-s-bank-to-pilot-mastercard-s-ai-payments-service"], ["Investor Day 2026: U.S. Consumer Cards transcript", IDCT]]),
        ]},
        {"id": "3.7", "ic": "headset", "name": "Operations & service", "blurb": "Answer, resolve, run.", "div": "citi", "rev": "grp", "products": [
            P("service", "Contact centres & disputes", "Card servicing, disputes and subscriptions. Mastercard's Ethoca Smart Subscriptions went live in the Citi app in the UAE in September 2026, Citi's first deployment anywhere; nothing equivalent is live in the US.",
              s=["con", "aff"], lc="everyday", neo=[1, "Smart Subscriptions in the UAE only."],
              mc="Consumer Clarity and Smart Subscriptions in the US: fewer 'what is this charge?' calls and disputes on 70 million customers' cards.",
              src=[["Mastercard: Citi and Mastercard launch Smart Subscriptions in the UAE, Sep 2026", "https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2026/september/citi-and-mastercard-launch-smart-subscriptions-in-the-uae/"]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "The five segments Citi has reported since 1Q26, Services, Markets, Banking, Wealth and U.S. Consumer Cards, opened out into what clients buy.",
    "tiles": [
        {"id": "4.1", "ic": "building-2", "name": "Treasury & Trade Solutions", "blurb": "#1 in payments, liquidity and trade.", "div": "svc", "rev": "svc", "products": [
            P("tts", "Treasury and Trade Solutions", "Cash management, payments, liquidity, trade and commercial cards for multinationals, banks and governments: 3Q26 revenue $4.9 billion (up 16%) on average deposits of $867 billion. Services as a whole earned $6.6 billion with a 31% return on tangible common equity.", short="TTS",
              s=["corp", "inst", "gov"], lc="everyday", neo=[1, "Commercial and virtual cards; the rest is bank rails."],
              src=[["3Q26 results", Q3], ["Investor Day 2026: Services", IDS]]),
            P("liquidity", "Liquidity management", "Pooling in more than 80 countries, with over $24 trillion a year swept through Citi liquidity structures; about half of Citi's Fortune 500 clients use them.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["Investor Day 2026: Services", IDS]]),
            P("trade", "Trade & working capital", "Supply-chain finance, letters of credit and guarantees: about $1 trillion of trade throughput in 2025 and about 440,000 buyer–supplier relationships in Citi Supplier Finance.",
              s=["corp", "sme"], lc="borrow", neo=[0, ""], src=[["Investor Day 2026: Services", IDS]]),
        ]},
        {"id": "4.2", "ic": "landmark", "name": "Securities Services", "blurb": "$35 trillion under custody.", "div": "svc", "rev": "svc", "products": [
            P("custody", "Custody & fund services", "Direct custody in more than 100 markets, fund administration and ETF servicing: assets under custody and administration of $35 trillion at 3Q26, up 16%, and 3Q26 revenue of $1.7 billion. Euromoney's best bank for securities services in 2026.",
              s=["inst"], lc="grow", neo=[0, ""], src=[["3Q26 results", Q3], ["Euromoney: world's best for securities services 2026", "https://www.euromoney.com/article/8yzqabdhfw0scgc8s8s8ss0o4/investment-banking/the-worlds-best-for-securities-services-2026-citi/"]]),
            P("issuer", "Issuer services & depositary receipts", "Depositary receipts, agency and trust, and digitally native notes: Global Depositary Notes are live in 14 markets.",
              s=["inst", "corp"], lc="grow", neo=[0, ""], src=[["Investor Day 2026: Services", IDS]]),
        ]},
        {"id": "4.3", "ic": "chart-candlestick", "name": "Markets", "blurb": "#1 in FX.", "div": "mkt", "rev": "mkt", "products": [
            P("ficc", "Fixed income, currencies & commodities", "Ranked first in FX and second in fixed income: 3Q26 FICC revenue $4.4 billion, rates and currencies $3.0 billion and spread products $1.4 billion. Markets earned $22.4 billion in 2025.", short="FICC",
              s=["inst", "corp", "gov"], lc="grow", neo=[0, ""], src=[["3Q26 results", Q3], ["Investor Day 2026: Markets", IDM]]),
            P("equities", "Equities & prime services", "3Q26 equities revenue $1.7 billion, up 14%, with record prime balances, up more than 40% on a year earlier.",
              s=["inst"], lc="grow", neo=[0, ""], src=[["3Q26 results", Q3]]),
        ]},
        {"id": "4.4", "ic": "briefcase-business", "name": "Banking", "blurb": "Deals, lending and the middle market.", "div": "bnk", "rev": "bnk", "products": [
            P("ib", "Investment banking", "M&A advice and equity and debt underwriting: $4.6 billion of fees in 2025, fifth globally, top three in debt capital markets. 3Q26 fees $1.35 billion, up 9%, led by equity capital markets (up 77%).",
              s=["corp", "inst", "gov"], lc="grow", neo=[0, ""], src=[["3Q26 results", Q3], ["Investor Day 2026: Banking", IDB]]),
            P("corplending", "Corporate banking & lending", "Second globally and first outside the US, with $415 billion of committed exposure (2025).",
              s=["corp"], lc="borrow", neo=[0, ""], src=[["Investor Day 2026: Banking", IDB]]),
            P("commercial", "Citi Commercial Bank", "Coverage for companies with $10 million to $3 billion of revenue, an addressable wallet Citi puts at about $100 billion; expanded into Germany, Switzerland and Canada (2022), France and Ireland (2023) and Japan (2024). Its revenue lands in Services, Markets and Banking.",
              s=["sme"], lc="everyday", neo=[1, "Commercial cards."], src=[["Investor Day 2026: Banking", IDB]]),
        ]},
        {"id": "4.5", "ic": "gem", "name": "Wealth", "blurb": "$759 billion of client investments.", "div": "wlt", "rev": "wlt", "products": [
            P("privatebank", "Citi Private Bank", "About 14,000 ultra-high-net-worth clients served by about 620 advisers from ten booking centres, including about a quarter of the world's billionaires and about 2,000 family offices. 3Q26 revenue $766 million.",
              s=["pvt"], lc="grow", neo=[1, "Premium Mastercard benefits on the top cards."], src=[["Investor Day 2026: Wealth", IDW], ["3Q26 results", Q3]]),
            P("citigold", "Citigold & Citi Priority", "Citi's affluent tiers: Citi Priority, Citigold and Citigold Private Client, with about 400,000 US and 200,000 international Citigold clients; about 325,000 have upgraded since 2022. Citigold and Retail Banking earned $2.3 billion in 3Q26.",
              s=["aff"], lc="grow", neo=[2, "Debit and the Strata cards are Mastercard."], src=[["Investor Day 2026: Wealth", IDW], ["3Q26 results", Q3]]),
            P("wealthatwork", "Wealth at Work", "Banking and investment for partners at law firms and professional-services firms: about 50,000 clients and 3Q26 revenue of $228 million.",
              s=["aff", "pvt"], lc="grow", neo=[0, ""], src=[["3Q26 results", Q3]]),
            P("blackrock", "Citi Portfolio Solutions with BlackRock", "BlackRock manages about $80 billion of Citi's investment-management assets, and Citi uses BlackRock's Aladdin Wealth platform (September 2025).",
              s=["aff", "pvt"], lc="grow", st="new", ay="Sep 2025", o="P", at="BlackRock", neo=[0, ""],
              src=[["BusinessWire: Citi and BlackRock, Sep 2025", "https://www.businesswire.com/news/home/20250904755362/en/"]]),
        ]},
        {"id": "4.6", "ic": "credit-card", "name": "Branded & co-brand cards", "blurb": "70 million US customers.", "div": "uscc", "rev": "uscc", "products": [
            P("brandedcards", "Citi-branded cards", "Double Cash (2% back), Simplicity and Diamond Preferred, and the Strata family: Strata (no fee, replaced Rewards+ in July 2025), Strata Premier ($95, World Elite) and Strata Elite ($595, July 2025). Custom Cash closed to new applicants on 28 May 2026. U.S. Consumer Cards: about 70 million customers, the third-largest US card lender with 14% of loans, $182 billion of loans and $175 billion of spend in 3Q26.", short="Double Cash, Strata",
              s=["con", "aff"], lc="borrow", neo=[2, "Mastercard since the 2015 agreement."],
              rel=["mcdeal", "stratae"], src=[["Citi: all credit cards", CARDS], ["Mastercard: Citi cards", MC_ISSUER], ["3Q26 results", Q3], ["NerdWallet: Custom Cash closed to new applications", "https://www.nerdwallet.com/credit-cards/news/citi-custom-cash-closed-to-new-applications"]]),
            P("stratae", "Citi Strata Elite", "Citi's premium card, launched 28 July 2025 at $595 a year: the first card on Mastercard's World Legend tier, 12x points on hotels and cars through Citi Travel, Admirals Club passes and The Curated Table dining series.", short="Strata Elite",
              s=["aff"], lc="borrow", st="new", ay="Jul 2025", neo=[3, "World Legend Mastercard, the first issued."],
              src=[["Citi launches Strata Elite, Jul 2025", STRATA_ELITE]]),
            P("aacards", "Citi / AAdvantage cards", "Platinum Select, Executive (World Legend from August 2026, $695), Globe (October 2025), MileUp and Business, all Mastercard. Under a ten-year extension signed in December 2024, Citi has been American's only US card issuer from 2026; Barclays' portfolio (about $6.6 billion of loans) converted on 24 April 2026. New AA accounts grew 38% in 2025.", short="AAdvantage cards",
              s=["con", "aff", "sme"], lc="borrow", o="P", at="American Airlines", neo=[2, "Every AAdvantage card is Mastercard."],
              mc="The single biggest co-brand on Mastercard in the US, now with the Barclays book on Citi's paper and on Mastercard.",
              src=[["American Airlines and Citi extend their partnership, Dec 2024", AA2024], ["AAdvantage Executive World Legend, Aug 2026", AAEXEC], ["Doctor of Credit: Barclays AA cards become Citi cards on 24 Apr 2026", "https://www.doctorofcredit.com/barclays-american-airlines-cards-to-become-citi-cards-on-4-24-26/"]]),
        ]},
        {"id": "4.7", "ic": "hand-coins", "name": "Retail Services & installments", "blurb": "Store cards, Flex Pay, Flex Loan.", "div": "uscc", "rev": "uscc", "products": [
            P("retailsvcs", "Retail Services partner cards", "Private-label and co-brand cards for 12 key partners, eight of them among the top 50 US retailers: The Home Depot, My Best Buy (store card and Visa), Macy's and Bloomingdale's (store cards and American Express), Exxon Mobil, Tractor Supply, Wayfair and Dillard's (Mastercard), L.L.Bean Mastercard and others. Citi has exited 12 programmes since 2022; private-label loans were $27.6 billion in 3Q26.", short="Home Depot, Best Buy, Macy's",
              s=["con", "fin"], lc="borrow", o="P", at="The Home Depot, Best Buy, Macy's", neo=[1, "Store cards are closed-loop; co-brands split across Mastercard, Visa and Amex."],
              src=[["Citi: retail store credit cards", "https://www.citi.com/credit-cards/compare/retail-store-credit-cards"], ["3Q26 results", Q3]]),
            P("flexpay", "Citi Flex Pay", "Split a card purchase of $75 or more into fixed monthly payments for a set fee. Since October 2025 Citi is the first US issuer on Mastercard Installments, so Flex Pay appears at checkout and in wallets; earlier partners included Apple Pay, Amazon and Costco.",
              s=["con"], lc="borrow", o="P", at="Mastercard", st="new", ay="Oct 2025", neo=[3, "Mastercard Installments carries it to merchants."],
              src=[["Mastercard and Citi: Flex Pay at more retailers, Oct 2025", INSTALL], ["Payments Dive: Citi Flex Pay partnerships, Mar 2025", "https://www.paymentsdive.com/news/citi-flex-pay-apple-partnerships-installment-lending-bnpl/742494/"]]),
            P("flexloan", "Citi Flex Loan", "A fixed-rate loan drawn against the card's credit line: from $500, up to 60 months, no origination fee. Installment balances have grown 13% a year since 2022.",
              s=["con"], lc="borrow", neo=[0, "Funded to a bank account."],
              src=[["MyBankTracker: Citi Flex Loan review", "https://www.mybanktracker.com/credit-cards/expert-reviews/citi-flex-loan-review-300878"], ["Investor Day 2026: U.S. Consumer Cards", IDC]]),
            P("citipay", "Citi Pay credit at checkout", "Digital-only credit and installment loans embedded in retailers' checkouts through FreedomPay (May 2023); current scale not disclosed.",
              s=["con", "fin"], lc="borrow", o="P", at="FreedomPay", ay="May 2023", st="unconf", neo=[0, ""],
              src=[["Citi Retail Services expands embedded payments with Citi Pay, 2023", PR + "2023/citi-retail-services-expands-embedded-payment-capabilities-with-citi-pay-"]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How clients reach Citi: the Citi Mobile app and citi.com, about 650 US branches and four international wealth hubs, CitiDirect and Citi Velocity for institutions, and the partners' own stores, lounges and checkouts.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Citi Mobile & citi.com", "blurb": "Digital actives up 18% since 2022.", "div": "uscc", "rev": "uscc", "products": [
            P("mobile", "Citi Mobile app", "Accounts, cards, Flex Pay and Flex Loan, Citi Travel and offers in one US app; 90-day digital actives are up 18% since 2022 and Citi expects mobile sales of those products to rise 25% in 2026. Citi publishes no current user count.",
              s=["con", "aff"], lc="everyday", neo=[0, ""], src=[["Investor Day 2026: U.S. Consumer Cards", IDC]]),
            P("citisky", "Citi Sky", "An AI wealth assistant built with Google Cloud and Google DeepMind, unveiled in April 2026 and rolling out to US Citigold clients from the summer.",
              s=["aff"], lc="grow", st="new", ay="Apr 2026", o="P", at="Google", neo=[0, ""],
              src=[["Constellation Research: Citi Sky, 2026", "https://www.constellationr.com/insights/news/citigroups-wealth-unit-launches-citi-sky-google-powered-wealth-advisor"]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches & wealth centres", "blurb": "650 branches in six cities.", "div": "wlt", "rev": "wlt", "products": [
            P("branches", "US branches", "About 650 branches in six affluent metros (New York, Los Angeles, San Francisco, Chicago, Miami and Washington), first in deposits per branch at about $255 million, with more than 400 advisers and bankers and 200 small-business advisers being added. Fee-free ATMs through Allpoint.",
              s=["con", "aff", "sme"], lc="everyday", neo=[0, ""], src=[["Investor Day 2026: Wealth", IDW]]),
            P("hubs", "International wealth hubs", "Singapore, Hong Kong, the UAE and London, where Citi books its international wealth; Hong Kong's Global Wealth Centre opened in 2022 and Singapore closed its last branch for wealth hubs in October 2024. About 30% of Wealth revenue is from Asia.",
              s=["aff", "pvt"], lc="grow", neo=[0, ""], src=[["finews.asia: Citi's Hong Kong wealth centre", "https://www.finews.asia/finance/37958-citi-launches-new-wealth-center-in-hong-kong"], ["Investor Day 2026: Wealth", IDW]]),
        ]},
        {"id": "5.3", "ic": "monitor", "name": "Institutional platforms", "blurb": "CitiDirect and Citi Velocity.", "div": "svc", "rev": "svc", "products": [
            P("citidirect", "CitiDirect", "Treasury and Trade Solutions' online and mobile portal (also CitiDirect BE), ranked joint first for global capabilities by Coalition Greenwich in 2025, now with a CitiDirect AI assistant.",
              s=["corp", "inst", "gov", "sme"], lc="everyday", neo=[0, ""], src=[["Investor Day 2026: Services", IDS]]),
            P("velocity", "Citi Velocity", "Markets' e-trading, research and analytics platform across FX, rates, credit, equities, commodities and prime; FX volumes rose 43% year on year in April 2025.",
              s=["inst", "corp"], lc="grow", neo=[0, ""], src=[["Citi Velocity", "https://www.citivelocity.com"]]),
        ]},
        {"id": "5.4", "ic": "plane", "name": "Partner channels", "blurb": "Stores, lounges, in flight.", "div": "uscc", "rev": "uscc", "products": [
            P("partneracq", "Partner acquisition", "About 90% of partner cards are acquired in the partner's own channels (stores, apps, Admirals Clubs and, since the AA deal, in flight), reaching more than 200 million loyalty-programme members.",
              s=["con", "fin"], lc="open", o="P", at="American Airlines, The Home Depot, Costco", neo=[1, "AA on Mastercard, Costco on Visa."],
              src=[["Investor Day 2026: U.S. Consumer Cards", IDC]]),
        ]},
        {"id": "5.5", "ic": "rocket", "name": "Ventures & developers", "blurb": "Where Citi invests and plugs in.", "div": "ven", "rev": "grp", "products": VENTURES},
    ],
}

PILLARS = [
    {"id": "pillar-banamex", "name": "Banamex & the exits", "blurb": "What Citi sold to become simpler.", "products": [
        P("banamex", "Banamex", "Mexico's consumer and small-business bank, being separated: Fernando Chico Pardo bought 25% (about $2.3 billion, closed December 2025) and became chair, and a group including General Atlantic, Afore SURA, BTG Pactual, Chubb, Blackstone funds, Liberty Strategic Capital and the Qatar Investment Authority took 24% by August 2026, leaving Citi with 51% ahead of a planned IPO. Reported in Legacy Franchises: 3Q26 revenue $1.8 billion.",
          s=["con", "sme"], div="banamex", rev="oth", st="flux", neo=[1, "Banamex issues Mastercard and Visa."],
          src=[["Citi: investors commit to 24% of Banamex, 2026", PR + "2026/citi-announces-agreements-with-investors-for-commitments-to-purchase-an-aggregate-24-equity-stake-in-banamex"], ["3Q26 results", Q3]]),
        P("exits", "International consumer exits", "The 2021 plan to leave consumer banking in 13 markets outside the US and Mexico is done: sold in Australia, Bahrain, India, Indonesia, Malaysia, the Philippines, Taiwan, Thailand, Vietnam and Poland (VeloBank, June 2026); wound down in Korea and China; and the Russian bank sold to Renaissance Capital around February 2026.",
          s=["con"], div="citi", rev="oth", st="retired", neo=[0, ""],
          src=[["Citi Handlowy completes the sale of its Polish consumer business, 2026", PR + "2026/citi-handlowy-completes-sale-consumer-banking-business-poland-velobank-sa"]]),
    ]},
    {"id": "pillar-market", "name": "The US card market", "blurb": "The water Citi swims in.", "products": [
        P("cardmarket", "US cards after Capital One–Discover", "Capital One closed Discover in May 2025 and became the largest US card lender (about $270 billion of loans), moving debit and testing credit on its own network; JPMorgan is next and Citi third, with 14% of loans. The revised Visa and Mastercard merchant settlement (about $38 billion; preliminary approval June 2026) would cut interchange and cap standard credit at 1.25%, squeezing rewards economics.",
          s=["fin", "con"], div="grp", rev="grp",
          src=[["PYMNTS: judge signals approval of the swipe-fee settlement, 2026", "https://www.pymnts.com/credit-cards/2026/judge-signals-approval-for-visa-and-mastercard-swipe-fee-settlement/"], ["PaymentsJournal: Capital One's credit migration, Jul 2026", "https://www.paymentsjournal.com/after-moving-debit-cards-to-discover-capital-one-turns-to-credit-card-migration/"]]),
    ]},
    {"id": "pillar-mastercard", "name": "Mastercard at Citi", "blurb": "The relationship, end to end.", "products": [
        P("mcatciti", "Mastercard at Citi", "From the 2009 virtual-card platform and the 2015 network agreement to the 2024–26 run of 'first issuer' launches: Move payouts through WorldLink, Strata Elite on World Legend, Agent Pay, Installments with Flex Pay, Commerce Media, the In Control upgrade and Smart Subscriptions in the UAE. Mastercard's US issuer business is led by co-president John Levitsky; Global Account Management (Jason Lane, Victor Nordenson) appears on the Citi launches.",
          s=["fin"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Citi and Mastercard: cross-border payments, Oct 2024", MOVE], ["Mastercard and Citi: Flex Pay installments, Oct 2025", INSTALL], ["Mastercard: In Control with Citi, Jul 2026", INCONTROL]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
