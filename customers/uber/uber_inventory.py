"""Uber's layers, areas and products, read through payments, as at 17 October 2026 (see page_data.py for the format).

Figures are Uber's own unless a source says otherwise: the Q2 2026 results (5 August 2026), the Q1 2026 results
(6 May 2026), the FY2025 results and 10-K (February 2026), the Q2 2026 10-Q and 8-Ks to September 2026, with
Uber's product pages, Mastercard's July 2025 release (read through trade coverage) and press for the card
programmes. Q3 2026 results are due in early November. ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm"
Q1 = "https://www.sec.gov/Archives/edgar/data/1543151/000154315126000019/uberq126earningspressrelea.htm"
Q4 = "https://www.sec.gov/Archives/edgar/data/1543151/000154315126000011/uberq425earningspressrelea.htm"
TENK = "https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm"
TENQ = "https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000032/uber-20260630.htm"
CFO = "https://www.sec.gov/Archives/edgar/data/1543151/000154315126000011/uber-20260130.htm"
PRES = "https://www.sec.gov/Archives/edgar/data/1543151/000155278126000320/e26247_uber-8k.htm"
DH = "https://www.sec.gov/Archives/edgar/data/1543151/000155278126000382/e26302_uber-8k.htm"
GETIR = "https://www.sec.gov/Archives/edgar/data/1543151/000155278126000043/e26049_uber-8k.htm"
NOTES = "https://www.sec.gov/Archives/edgar/data/1543151/000155278126000486/e26383_uber-8k.htm"
MC = "https://www.mastercard.com/us/en/news-and-trends/press/2025/july/mastercard-expands-global-relationship-with-uber.html"
PAYPERS = "https://thepaypers.com/payments/news/uber-expands-mastercard-partnership-to-improve-payments"
ALTEX = "https://www.altexsoft.com/travel-industry-news/mastercard-and-uber-add-instant-payouts-for-drivers/"
PROUS = "https://www.uber.com/us/en/drive/uber-pro/debit-card/"
PROUK = "https://www.uber.com/gb/en/drive/uber-pro/debit-card/"
PROBLOG = "https://www.uber.com/us/en/blog/uber-pro-card-cash-back/"
BRANCH = "https://branchapp.com/upc/rewards"
ADYEN = "https://www.travolution.com/news/adyen-and-uber-expand-partnership-into-new-markets/"
EBANX = "https://www.electronicpaymentsinternational.com/news/uber-taps-ebanx-for-instant-payments-processing-in-brazil"
UPI = "https://embed.wionews.com/business-economy/uber-expands-its-payment-mode-with-upi-based-payment-facility-19368"
AMEX = "https://www.uber.com/us/en/u/amex/"
U4B = "https://www.uber.com/us/en/business/"
MONEY = "https://siliconangle.com/?p=495122"
CASH = "https://www.uber.com/newsroom/introducing-uber-money"
BLOOMBERG = "https://www.bloomberg.com/news/articles/2017-10-25/uber-hails-barclays-visa-for-its-no-fee-co-brand-credit-card"
UPGRADED = "https://upgradedpoints.com/new-uber-visa-credit-card"
CAPONE = "https://www.bankrate.com/finance/credit-cards/capital-one-and-uber-partnership/"
PAYPAL = "https://techcrunch.com/2015/06/24/uber-paypal"
METHODS = "https://getridewise.com/blog/uber-payment-methods-cash-options"
VISAAF = "https://cioafrica.co/visa-uber-partner-offer-seamless-payment-experience/"
AGENTIC = "https://letsdatascience.com/news/visa-partners-with-openai-for-agentic-commerce-41fdfbb2"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "bookings · people · payments entities", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $193.5 billion of Gross Bookings in 2025 and $58.0 billion in Q2 2026, a San Francisco leadership under Dara Khosrowshahi with a new CFO, e-money licences in the EEA, UK and Mexico, and a takeover offer for Delivery Hero.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & results", "blurb": "$193.5bn of bookings in 2025.", "div": "grp", "rev": "grp", "products": [
            P("results", "Bookings & results", "Gross Bookings of $193.5 billion in 2025 (+19%) on revenue of $52.0 billion and 13.6 billion trips; free cash flow $9.8 billion. Q2 2026: Gross Bookings $58.0 billion (+24%), revenue $14.2 billion, GAAP net income $2.4 billion, trailing free cash flow above $10 billion for the first time. About 34,000 staff in more than 70 countries.",
              s=["rider", "eater"], neo=[0, ""], src=[["Uber: Q2 2026 results", Q2], ["Uber: Q4 and FY2025 results", Q4], ["Uber 10-K FY2025", TENK]]),
            P("platform", "Platform reach", "208 million monthly active platform consumers in Q2 2026 (+16%) and 3.9 billion trips in the quarter; more than 8.5 million drivers and couriers (July 2025); more than 15,000 cities.",
              s=["rider", "earner"], neo=[0, ""], src=[["Uber: Q2 2026 results", Q2], ["Altexsoft: Mastercard and Uber, Jul 2025", ALTEX], ["Uber 10-K FY2025", TENK]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Khosrowshahi, Krishnamurthy.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Executive officers", "Dara Khosrowshahi (CEO); Balaji Krishnamurthy (CFO from 16 February 2026, replacing Prashanth Mahendra-Rajah); Jill Hazelbaker (President & Chief Corporate Affairs Officer from May 2026). Karl Hébert, VP Global Commerce, speaks for payments. Andrew Macdonald as President & COO is from prior knowledge ⚠.",
              s=["rider"], neo=[0, ""], src=[["Uber 8-K: CFO, Feb 2026", CFO], ["Uber 8-K: Hazelbaker, May 2026", PRES], ["Travolution: Adyen and Uber, Feb 2026", ADYEN]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Payments entities", "blurb": "E-money in the EEA, UK, Mexico.", "div": "pay", "rev": "grp", "products": [
            P("uberpaybv", "Uber Payments B.V. & licences", "Uber Payments B.V. is registered as an electronic money institution in the EEA, with similar licences in the UK and Mexico; Uber says it is evaluating licences elsewhere.",
              s=["rider", "earner"], neo=[0, ""], src=[["Uber 10-K FY2025", TENK]]),
        ]},
        {"id": "1.4", "ic": "briefcase-business", "name": "Deals & capital", "blurb": "Delivery Hero, Getir, Blacklane.", "div": "grp", "rev": "del", "products": [
            P("deliveryhero", "Delivery Hero takeover offer", "Agreement of 16 July 2026 for a cash offer at €41.50 a share, backed by a €14.2 billion bridge loan; completion expected in the second half of 2027, subject to approvals. Uber already held Delivery Hero exposure through $1.6 billion of total return swaps.",
              s=["eater", "mer"], st="new", ay="Jul 2026", o="A", neo=[0, ""],
              mc="Delivery Hero's payments, payouts and merchant acquiring would come into Uber's estate.",
              src=[["Uber 8-K: Delivery Hero, Jul 2026", DH], ["Uber 10-Q Q2 2026", TENQ]]),
            P("deals", "Other deals 2021–26", "Drizly and Transplace (2021), Trendyol Go (June 2025; about $700 million ⚠), Getir's food delivery in Türkiye for $335 million plus 15% of its grocery business for $100 million (February 2026), Blacklane for about $550 million (March 2026), and a Lime stake that listed in June 2026.",
              s=["eater"], o="A", neo=[0, ""], src=[["Uber 8-K: Getir, Feb 2026", GETIR], ["Uber 10-Q Q2 2026", TENQ], ["Uber 10-K FY2025", TENK]]),
            P("funding", "Funding & buybacks", "€4.5 billion of senior notes in five series, 2029 to 2046 (September 2026); $6.5 billion of buybacks in 2025 and $3.5 billion in the first half of 2026.",
              s=["rider"], neo=[0, ""], src=[["Uber 8-K: euro notes, Sep 2026", NOTES], ["Uber: Q4 and FY2025 results", Q4], ["Uber 10-Q Q2 2026", TENQ]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy", "blurb": "Cross-platform, autonomous.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "Platform & autonomous strategy", "Users of both rides and delivery book over three times as much as single-product users; Uber aims to be 'the largest facilitator of AV trips in the world', with Waymo's fleet already on the platform. Other AV partners are from prior knowledge ⚠.",
              s=["rider", "eater"], neo=[0, ""], src=[["Uber 10-K FY2025", TENK], ["Uber: Q4 and FY2025 results", Q4]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: card and wallet acceptance (three quarters of bookings), processing on Adyen with Mastercard Gateway, Pix, UPI and cash, payouts to 8.5 million earners on Mastercard Move, the Mastercard Uber Pro Card, consumer card tie-ins led by American Express, and Uber Cash.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Acceptance", "blurb": "75%+ on cards and wallets.", "div": "pay", "rev": "mob", "products": [
            P("accept", "Card & wallet acceptance", "More than 75% of 2025 Gross Bookings were paid by credit card, debit card or digital wallet, on every network. The 10-K names card-network rules, PCI DSS and 'poor network relationships' as risks to incentives and costs.",
              s=["rider", "eater"], lc="move", neo=[1, "Accepts every network."], src=[["Uber 10-K FY2025", TENK]]),
            P("wallets", "Wallets & alternatives", "In the US: bank account through Link, PayPal, Venmo, Apple Pay, Google Pay, Klarna, gift cards and Uber Cash ⚠ secondary guide. PayPal has been offered since 2013–15.",
              s=["rider", "eater"], lc="move", o="P", at="PayPal, Apple, Google, Klarna", neo=[0, "Wallets carry cards on every network."],
              src=[["RideWise: Uber payment methods", METHODS], ["TechCrunch: Uber and PayPal, Jun 2015", PAYPAL]]),
            P("cash", "Cash", "About 6% of global Gross Bookings in 2025 were cash-paid trips, in markets such as Mexico, India and Egypt; Uber flags cash collection and anti-money-laundering risk.",
              s=["rider"], lc="move", neo=[0, "Cash."],
              mc="Cash markets are where card and account-to-account conversion pays.",
              src=[["Uber 10-K FY2025", TENK]]),
        ]},
        {"id": "2.2", "ic": "network", "name": "Processing", "blurb": "Adyen since 2012; Gateway.", "div": "pay", "rev": "mob", "products": [
            P("adyen", "Adyen", "Uber's processor since 2012, with growth in 40 key markets; from February 2026 local acquiring in Japan, Mexico, New Zealand and Australia, new markets in the UAE, Hong Kong and the Caribbean, and Pix, Afterpay and WeChat Pay through Adyen's Checkout API.",
              s=["rider", "eater"], lc="move", o="P", at="Adyen", ay="2012", neo=[1, "Processor for every network."],
              src=[["Travolution: Adyen and Uber, Feb 2026", ADYEN]]),
            P("mcgateway", "Mastercard Gateway", "Mastercard Gateway capabilities for collections, under the July 2025 agreement. Markets and share of volume were not disclosed ⚠.",
              s=["rider", "eater"], lc="move", st="new", ay="Jul 2025", o="P", at="Mastercard", neo=[3, "Mastercard Gateway."],
              src=[["Mastercard: Uber relationship, Jul 2025", MC], ["The Paypers: Uber and Mastercard, Jul 2025", PAYPERS]]),
        ]},
        {"id": "2.3", "ic": "zap", "name": "Local methods", "blurb": "Pix, UPI, WeChat Pay.", "div": "pay", "rev": "mob", "products": [
            P("pix", "Pix in Brazil", "An exclusive deal with EBANX from 17 November 2020 to take Pix for rides, Uber Eats and Uber Cash top-ups, to reach customers without cards.",
              s=["rider", "eater"], lc="move", ay="Nov 2020", o="P", at="EBANX", neo=[0, "Pix."],
              src=[["EPI: Uber and EBANX, Nov 2020", EBANX], ["Travolution: Adyen and Uber, Feb 2026", ADYEN]]),
            P("localpay", "UPI, Afterpay & WeChat Pay", "UPI in India (date unclear ⚠), Afterpay in Australia and WeChat Pay in Uber's WeChat mini-program, the last two through Adyen from February 2026.",
              s=["rider"], lc="move", o="P", at="Adyen", neo=[0, "UPI, BNPL and wallet."],
              src=[["WION: Uber and UPI", UPI], ["Travolution: Adyen and Uber, Feb 2026", ADYEN]]),
        ]},
        {"id": "2.4", "ic": "send", "name": "Earner payouts", "blurb": "Instant Pay, Mastercard Move.", "div": "pro", "rev": "mob", "products": [
            P("instantpay", "Instant Pay", "Earnings cashed out to a debit card at any time; already about 70% of driver payouts in 2019. Open to Mastercard, Visa and Discover debit cards in the US ⚠ secondary.",
              s=["earner"], lc="move", neo=[1, "Mastercard and Visa debit cards."], src=[["SiliconANGLE: Uber Money, Oct 2019", MONEY]]),
            P("mcmove", "Mastercard Move payouts", "Real-time disbursements to drivers and couriers on Mastercard Move, under the July 2025 agreement covering more than 8.5 million earners. The share of payouts it carries was not disclosed ⚠.",
              s=["earner"], lc="move", st="new", ay="Jul 2025", o="P", at="Mastercard", neo=[3, "Mastercard Move."],
              mc="Payouts to millions of earners in 70+ countries are Move's showcase.",
              src=[["Mastercard: Uber relationship, Jul 2025", MC], ["Altexsoft: Mastercard and Uber, Jul 2025", ALTEX]]),
        ]},
        {"id": "2.5", "ic": "wallet-cards", "name": "Uber Pro Card", "blurb": "Mastercard in US, Canada, UK.", "div": "pro", "rev": "mob", "products": [
            P("procardus", "Uber Pro Card (US)", "A Mastercard business debit card issued by Evolve Bank & Trust and run by Branch: free cash-out after every trip in 1–5 seconds, 2–6% back at the pump by Uber Pro tier (up to 10% at ExxonMobil Easy Savings stations), up to 12% on EV charging, refuelling cash back capped at $100 a month. In market by December 2022.", short="Pro Card US (Mastercard)",
              s=["earner"], lc="everyday", o="P", at="Branch, Evolve Bank & Trust", neo=[2, "Mastercard, issued by Evolve."],
              mc="Mastercard's anchor at Uber: the card earners are paid onto.",
              src=[["Uber: Uber Pro Card (US)", PROUS], ["Uber: Pro Card cash back, Dec 2022", PROBLOG], ["Branch: Uber Pro Card rewards", BRANCH]]),
            P("procardca", "Uber Pro Card (Canada)", "Live before July 2025 and renewed in the Mastercard agreement; the Canadian issuer was not verified ⚠.", short="Pro Card Canada (Mastercard)",
              s=["earner"], lc="everyday", o="P", neo=[2, "Mastercard."], src=[["Mastercard: Uber relationship, Jul 2025", MC]]),
            P("procarduk", "Uber Pro Card (UK)", "A Mastercard debit card issued by Transact Payments Limited, with a current account and savings from Griffin Bank: up to 3% back on fuel, EV charging and car washes (£25 a category a month), savings up to 3.30% AER, transfers within 10 seconds. Announced July 2025.", short="Pro Card UK (Mastercard)",
              s=["earner"], lc="everyday", st="new", ay="Jul 2025", o="P", at="Transact Payments, Griffin Bank", neo=[2, "Mastercard, issued by Transact Payments."],
              src=[["Uber: Uber Pro Card (UK)", PROUK], ["Mastercard: Uber relationship, Jul 2025", MC]]),
            P("onecred", "Mastercard One Credential", "The Uber Pro Card moving to One Credential, giving drivers and couriers more ways to pay from one card (July 2025).",
              s=["earner"], lc="everyday", st="new", ay="Jul 2025", o="P", at="Mastercard", neo=[3, "Mastercard One Credential."],
              src=[["The Paypers: Uber and Mastercard, Jul 2025", PAYPERS], ["Mastercard: Uber relationship, Jul 2025", MC]]),
            P("greendot", "Uber Debit by Green Dot", "Uber Money's Visa debit card from Green Dot (28 October 2019), with 3–6% back on gas; replaced by the Branch and Evolve Mastercard by 2022 ⚠ exact date.", short="Uber Debit 2019 (Visa)",
              s=["earner"], lc="everyday", st="retired", ay="Oct 2019", o="P", at="Green Dot", neo=[0, "Visa."],
              mc="The earner card moved from Visa to Mastercard.",
              src=[["SiliconANGLE: Uber Money, Oct 2019", MONEY]]),
        ]},
        {"id": "2.6", "ic": "gem", "name": "Consumer cards", "blurb": "Amex Uber Cash; no co-brand.", "div": "uber", "rev": "mob", "products": [
            P("amex", "American Express Uber Cash", "Platinum: up to $200 a year in Uber Cash and up to $120 a year of Uber One credits; Gold: up to $120 a year in Uber Cash; a dedicated Amex support line in the apps. US only; the card must be added directly, not through Apple Pay or PayPal.", short="Amex benefits (Amex)",
              s=["rider", "eater", "member"], lc="grow", o="P", at="American Express", neo=[0, "American Express."],
              mc="The richest card tie-in at Uber is Amex's.",
              src=[["Uber: American Express benefits", AMEX]]),
            P("ubervisa", "Uber Visa Card (Barclays)", "A no-fee co-brand with Barclays and Visa from October 2017, relaunched in October 2019 with 5% back in Uber Cash; reported discontinued (2021 ⚠).", short="Uber Visa (Visa)",
              s=["rider"], lc="borrow", st="retired", ay="Oct 2017", o="P", at="Barclays, Visa", neo=[0, "Visa."],
              src=[["Bloomberg: Uber picks Barclays and Visa, Oct 2017", BLOOMBERG], ["UpgradedPoints: Uber cards, Sep 2026", UPGRADED]]),
            P("capone", "Capital One Savor offer", "10% back on Uber and Uber Eats and Uber One for Savor and SavorOne holders from 2022 ⚠; reported ended in 2024 ⚠.", short="Capital One Savor (Mastercard ⚠)",
              s=["rider", "eater"], lc="grow", st="retired", o="P", at="Capital One", neo=[1, "Savor cards are Mastercard ⚠."],
              src=[["Bankrate: Capital One and Uber", CAPONE]]),
            P("onecard", "Uber One card", "No Uber One co-branded credit card was found in October 2026 ⚠; 50 million Uber One members have no Uber card of their own.",
              s=["member"], lc="borrow", st="unconf", neo=[None, "No card found ⚠."],
              mc="An open co-brand for 50 million members."),
        ]},
        {"id": "2.7", "ic": "wallet", "name": "Uber Cash", "blurb": "Stored value, gift cards.", "div": "uber", "rev": "mob", "products": [
            P("ubercash", "Uber Cash", "Stored value for rides, Uber Eats, groceries and packages; funds added never expire, promotional credits may. Topped up by card, gift card or, in Brazil, Pix.",
              s=["rider", "eater"], lc="everyday", neo=[1, "Topped up by card on any network."], src=[["Uber: Uber Cash", CASH], ["EPI: Uber and EBANX, Nov 2020", EBANX]]),
            P("giftcards", "Gift cards", "Uber gift cards sold at retailers and to businesses for staff and customers.",
              s=["rider", "biz"], lc="grow", neo=[0, ""], src=[["Uber for Business", U4B]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every trip: Uber One with 50 million members, Mastercard Offers and Easy Savings, Uber Pro's earner tiers and the money tools behind the Pro Card, payments risk and compliance, and advertising.",
    "tiles": [
        {"id": "3.1", "ic": "gift", "name": "Uber One & offers", "blurb": "50m members; Mastercard Offers.", "div": "uber", "rev": "mob", "products": [
            P("uberone", "Uber One", "46 million members at the end of 2025 in over 30 countries and 50 million in Q1 2026, driving half of Mobility and Delivery Gross Bookings; $9.99 a month in the US.",
              s=["member"], lc="grow", neo=[0, ""],
              mc="Recurring billing at this scale is what Automatic Billing Updater protects.",
              src=[["Uber: Q1 2026 results", Q1], ["Uber 10-K FY2025", TENK], ["UpgradedPoints: Uber cards, Sep 2026", UPGRADED]]),
            P("mcoffers", "Mastercard Offers Platform", "Benefits for Mastercard cardholders on Uber's rides and delivery worldwide, under the July 2025 agreement. Live offers were not verified ⚠.",
              s=["rider", "eater"], lc="grow", st="new", ay="Jul 2025", o="P", at="Mastercard", neo=[3, "Mastercard Offers."],
              src=[["Mastercard: Uber relationship, Jul 2025", MC], ["The Paypers: Uber and Mastercard, Jul 2025", PAYPERS]]),
        ]},
        {"id": "3.2", "ic": "hand-coins", "name": "Uber Pro & earner money", "blurb": "Tiers, Easy Savings, Backup Balance.", "div": "pro", "rev": "mob", "products": [
            P("uberpro", "Uber Pro tiers", "Blue or Green, Gold, Platinum and Diamond tiers for drivers and couriers, which set Pro Card cash back and Backup Balance limits.",
              s=["earner"], lc="grow", neo=[1, "Rewards paid on the Mastercard Pro Card."], src=[["Uber: Uber Pro Card (US)", PROUS]]),
            P("easysavings", "Mastercard Easy Savings", "An extra 1% back on the Uber Pro Card at participating fuel stations, outside the monthly cap.",
              s=["earner"], lc="grow", o="P", at="Mastercard", neo=[3, "Mastercard Easy Savings."],
              src=[["Uber: Uber Pro Card (US)", PROUS]]),
            P("backup", "Backup Balance & Branch wallet", "Up to $150 of Backup Balance with no fee (by tier), free transfers into the Branch wallet and 2% (minimum $2.99) to move money out instantly; free ACH.",
              s=["earner"], lc="borrow", o="P", at="Branch", neo=[2, "On the Mastercard Pro Card."], src=[["Uber: Uber Pro Card (US)", PROUS]]),
            P("savings", "Driver savings (UK)", "An easy-access savings account from Griffin Bank paying up to 3.30% AER, beside the UK Pro Card.",
              s=["earner"], lc="grow", st="new", o="P", at="Griffin Bank", neo=[1, "Beside the Mastercard Pro Card."], src=[["Uber: Uber Pro Card (UK)", PROUK]]),
        ]},
        {"id": "3.3", "ic": "shield-check", "name": "Risk & compliance", "blurb": "PCI, fraud, cash AML.", "div": "pay", "rev": "grp", "products": [
            P("risk", "Payments risk & compliance", "PCI DSS and network rules through Uber's processors, 'higher levels of credit risk and payment fraud' abroad, and anti-money-laundering risk on cash trips. No fraud-tool partner is named ⚠.",
              s=["rider", "earner"], lc="everyday", neo=[None, "No fraud partner named."],
              mc="Fraud and identity tools for riders and earner onboarding.",
              src=[["Uber 10-K FY2025", TENK]]),
        ]},
        {"id": "3.4", "ic": "presentation", "name": "Advertising", "blurb": "Since October 2022.", "div": "eats", "rev": "del", "products": [
            P("ads", "Uber Advertising", "Ads in the Uber and Uber Eats apps, launched in October 2022; the current run rate was not re-verified ⚠.",
              s=["mer"], lc="grow", neo=[0, ""], src=[["Uber 10-K FY2025", TENK]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What Uber sells: rides at $29.0 billion of bookings a quarter, Uber Eats delivery at $27.5 billion, Uber Freight, Uber for Business for more than 300,000 companies, Uber Health and autonomous rides with Waymo.",
    "tiles": [
        {"id": "4.1", "ic": "earth", "name": "Mobility", "blurb": "$29.0bn in Q2 2026.", "div": "uber", "rev": "mob", "products": [
            P("mobility", "Mobility", "Gross Bookings of $29.0 billion in Q2 2026 (+22%) and revenue of $7.4 billion; 15% of 2025 Mobility bookings started or ended at an airport. Blacklane's chauffeur service is being added.",
              s=["rider", "earner"], lc="everyday", neo=[1, "Accepts every network."], src=[["Uber: Q2 2026 results", Q2], ["Uber 10-K FY2025", TENK]]),
        ]},
        {"id": "4.2", "ic": "store", "name": "Delivery", "blurb": "$27.5bn in Q2 2026.", "div": "eats", "rev": "del", "products": [
            P("delivery", "Uber Eats & grocery", "Gross Bookings of $27.5 billion in Q2 2026 (+26%) and revenue of $5.2 billion; about 58% of first-time Delivery consumers in Q4 2025 were new to Uber.",
              s=["eater", "mer", "earner"], lc="everyday", neo=[1, "Accepts every network."], src=[["Uber: Q2 2026 results", Q2], ["Uber 10-K FY2025", TENK]]),
            P("merchants", "Restaurant & merchant payouts", "Uber collects from eaters and settles to restaurants and stores; payout rails and schedules were not found ⚠.",
              s=["mer"], lc="move", st="unconf", neo=[None, "Payout rails not public."],
              mc="Merchant payouts are a second Move use case."),
        ]},
        {"id": "4.3", "ic": "factory", "name": "Freight", "blurb": "$1.6bn in Q2 2026.", "div": "freight", "rev": "frt", "products": [
            P("freight", "Uber Freight", "Gross Bookings and revenue of $1.6 billion in Q2 2026 (+25%), principally in North America and Europe; Transplace added in 2021.",
              s=["shipper"], lc="beyond", neo=[0, ""], src=[["Uber: Q2 2026 results", Q2], ["Uber 10-K FY2025", TENK]]),
        ]},
        {"id": "4.4", "ic": "briefcase", "name": "Uber for Business", "blurb": "300,000+ businesses.", "div": "biz", "rev": "mob", "products": [
            P("u4b", "Uber for Business", "Travel and meal programmes for more than 300,000 businesses, including more than half of the Fortune 500: business profiles, delegate booking, vouchers, Central, gift cards and corporate Uber One, paid per trip or by monthly invoice.",
              s=["biz"], lc="everyday", neo=[1, "Corporate cards on any network."],
              mc="Virtual and commercial cards for monthly billing are untested ground.",
              src=[["Uber for Business", U4B]]),
            P("health", "Uber Health", "Rides and deliveries arranged by healthcare organisations, sold through Uber for Business.",
              s=["biz"], lc="beyond", neo=[0, ""], src=[["Uber for Business", U4B]]),
        ]},
        {"id": "4.5", "ic": "rocket", "name": "Autonomous", "blurb": "Waymo on the platform.", "div": "uber", "rev": "mob", "products": [
            P("av", "Autonomous rides", "Waymo's fleet is available through Uber; Uber names Waymo, Zoox and Tesla as competitors as well. Other AV partners are from prior knowledge ⚠.",
              s=["rider"], lc="beyond", st="new", o="P", at="Waymo", neo=[0, ""], src=[["Uber 10-K FY2025", TENK], ["Uber: Q4 and FY2025 results", Q4]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How people reach Uber: the Uber and Uber Eats apps for 208 million monthly users, the driver app, airport kiosks, a WeChat mini-program, and the expense and card partners that carry Uber into other products.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "208m monthly users.", "div": "uber", "rev": "mob", "products": [
            P("app", "Uber & Uber Eats apps", "Where riders and eaters book and pay, with Uber Cash, Uber One and saved cards in one wallet; 208 million monthly active platform consumers in Q2 2026.",
              s=["rider", "eater", "member"], lc="open", neo=[0, ""], src=[["Uber: Q2 2026 results", Q2]]),
            P("driverapp", "Driver app", "Where earners see Uber Pro status, cash out with Instant Pay and manage the Pro Card.",
              s=["earner"], lc="open", neo=[0, ""], src=[["Uber: Uber Pro Card (US)", PROUS]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "Kiosks & mini-programs", "blurb": "LaGuardia, WeChat.", "div": "uber", "rev": "mob", "products": [
            P("kiosk", "Uber kiosks", "Booking without a smartphone on Adyen terminals, first at LaGuardia Terminal C in December 2025, with more airports, hotels and ports planned.",
              s=["rider"], lc="open", st="new", ay="Dec 2025", o="P", at="Adyen", neo=[1, "Card-present, any network."], src=[["Travolution: Adyen and Uber, Feb 2026", ADYEN]]),
            P("wechat", "WeChat mini-program", "Uber inside WeChat for travellers, paid with WeChat Pay through Adyen.",
              s=["rider"], lc="open", o="P", at="Tencent, Adyen", neo=[0, "WeChat Pay."], src=[["Travolution: Adyen and Uber, Feb 2026", ADYEN]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Partners", "blurb": "Expense tools, card partners.", "div": "biz", "rev": "mob", "products": [
            P("integrations", "Expense & card partners", "Receipts sync to Navan, Ramp, SAP Concur and Expensify; Amex and Delta tie-ins bring cardholders in; double Delta SkyMiles on eligible business rides.",
              s=["biz", "member"], lc="open", o="P", at="Navan, Ramp, SAP Concur, Expensify, Delta", neo=[0, ""], src=[["Uber for Business", U4B], ["Uber: American Express benefits", AMEX]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Uber", "blurb": "Earner cards, Move, Gateway.", "products": [
        P("mcatuber", "Mastercard at Uber", "Mastercard carries Uber's earner money: the Uber Pro Card is a Mastercard in the US, Canada and the UK, and the July 2025 agreement added Mastercard Move for payouts, One Credential, Gateway for collections and the Offers Platform for cardholders; Easy Savings sits in Pro Card rewards. Sherri Haymond, co-president, Global Partnerships, led it for Mastercard. On the consumer side every network is accepted, American Express holds the richest US tie-in, and the old Visa co-brand has lapsed.",
          s=["earner"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Mastercard: Uber relationship, Jul 2025", MC], ["Uber: Uber Pro Card (US)", PROUS], ["Uber: American Express benefits", AMEX]]),
    ]},
    {"id": "pillar-market", "name": "The market", "blurb": "Amex, Visa, Pix, agents.", "products": [
        P("market", "The market", "Visa was Uber's first co-brand and driver-card network and pushed card payments with Uber in Africa in 2017; Amex owns the premium US benefit; Pix, UPI and cash take a share in Brazil, India and Mexico. Visa said in June 2026 it would embed its network in ChatGPT, and Mastercard launched Agent Pay for Machines the same day ⚠ secondary; no Uber agentic-payments partner is named.",
          s=["rider"], div="grp", rev="grp", src=[["CIO Africa: Visa and Uber, Oct 2017", VISAAF], ["Let's Data Science: Visa and OpenAI, Jun 2026", AGENTIC]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
