"""Danske Bank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 interim report (17 July 2026), the
Forward '28 update (30 April 2026) and the Annual Report 2025 (5 February 2026). ``neo`` is the Mastercard
lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly,
0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://danskebank.com/-/media/danske-bank-com/file-cloud/2026/7/danske-bank-interim-report---first-half-2026.pdf"
H1PR = "https://mfn.se/all/a/danske-bank/staerke-resultater-for-1-halvar-2026-pa-baggrund-af-god-kundeaktivitet-vaekst-i-udlanet-og-staerk-kreditkvalitet-resultat-efter-skat-pa-11-9-mia-kr-2026-forventningerne-til-resultat-efter-skat-opjusteret-til-23-25-mia-kr-fbdbb75c"
AR25 = "https://danskebank.com/-/media/danske-bank-com/file-cloud/2026/2/annual-report-2025.pdf?rev=16af459cfa094b8ab365a911a324f7f2&hash=EA2BEA20F11569C30A0396F6BF49065B"
FY25 = "https://danskebank.com/news-and-insights/news-archive/press-releases/2026/pr05022026"
F28 = "https://danskebank.com/news-and-insights/news-archive/company-announcements/2026/ca30042026"
STRAT = "https://danskebank.com/about-us/our-strategy"
LEAD = "https://danskebank.com/da/om-os/vores-ledelse"
ELT26 = "https://www.inderes.se/en/releases/changes-to-the-executive-leadership-team-of-danske-bank-as-and-the-organisation"
NIHEAD = "https://www.mortgagesolutions.co.uk/mortgage-news/2026/02/24/danske-bank-appoints-haines-as-ceo-to-succeed-davies/"
WIKI = "https://en.wikipedia.org/wiki/Danske_Bank"
DKCARDS = "https://danskebank.dk/privat/produkter/kort"
HVERDAG = "https://danskebank.dk/en/personal/products/cards/mastercard-hverdag-plus"
WE = "https://danskebank.dk/PDF/PRISER-VILKAAR-FAKTAARK/Kort/Kortbestemmelser-World-Elite-MC-PBE.pdf"
CASHBACK = "https://danskebank.dk/privat/produkter/kort/cashback"
BIZCARDS = "https://danskebank.dk/erhverv/loesninger/daglig-drift/kort"
FICARDS = "https://danskebank.fi/sinulle/paivittaispalvelut/kortit"
SECARDS = "https://danskebank.se/privat/produkter/kort"
UKDEBIT = "https://danskebank.co.uk/personal/products/credit-cards/debit-mastercard"
DANKORT19 = "https://danskebank.com/news-and-insights/news-archive/press-releases/2019/pr01022019a"
NETS19 = "https://www.nets.eu/Media-and-press/news/Pages/Danske-Bank-and-Nets-enter-long-term-Nordic-agreement.aspx"
AIIA = "https://danskebank.com/news-and-insights/news-archive/press-releases/2021/pr07092021"
MOBILEPAY = "https://mobilepay.dk/news/mobilepay-to-merge-with-norwegian-vipps-and-finnish-pivo"
NORWAY = "https://www.nordea.com/en/press/2024-11-18/nordea-completes-the-acquisition-of-danske-banks-personal-customer-and-private-banking-business-in-norway"
NBDK = "https://www.nationalbanken.dk/da/viden-og-nyheder/publikationer-og-taler/analyse/2026/danskerne-betaler-mere-med-mobilen"
TAENK = "https://taenk.dk/privatoekonomi/banker-og-kreditforeninger/overblik-vil-din-bank-tilbyde-dankort-i-apple-pay"
NETSMONO = "https://ing.dk/artikel/nationalbanken-nets-monopol-som-dankort-indloeser-oeger-omkostninger-til-kortbetalinger"
QIVALIS = "https://qivalis.eu/press/news/qivalis-joint-venture-of-a-european-banking-consortium-to-launch-euro-stablecoin-in-the-second-half-of-2026"
AGENT = "https://www.crowdfundinsider.com/2026/09/312003-danske-bank-completes-denmarks-ai-agent-payment-with-mastercard/"
DEV = "https://developers.danskebank.com/"
EUROMON = "https://www.euromonitor.com/debit-cards-in-denmark/report"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · governance · platform", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: Denmark's largest bank with DKK 1,794 billion of loans, ROE of 13.9% in the first half of 2026, a bank dating from 1871, the Estonia case now closed, one platform moving to AWS, and Forward '28.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "DKK 11.9bn profit in H1.", "div": "group", "rev": "other", "products": [
            P("balance", "Balance sheet & earnings", "Loans of DKK 1,794 billion and deposits of DKK 1,135 billion at 30 June 2026; net profit of DKK 11.9 billion in the half (ROE 13.9%) and DKK 23.0 billion in 2025; CET1 17.0%; 2026 profit guidance raised to DKK 23–25 billion. Rated AA-/Aa3/AA- (counterparty) at end-2025; market value about DKK 290 billion at 30 June 2026 ⚠ derived.",
              s=["con"], neo=[0, ""], src=[["H1 2026 interim report", H1], ["H1 2026 release", H1PR], ["Annual Report 2025", AR25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership & heritage", "blurb": "Egeriis and Blessing.", "div": "group", "rev": "other", "products": [
            P("leadership", "Board & executive team", "Chair Martin Blessing, CEO Carsten Egeriis, CFO Cecile Hillary, COO Frans Woelders, CRO Magnus Agustsson (Risk and Compliance merged June 2026); Christian Bornfeld runs Personal Customers, Johanna Norberg Business Customers and Joachim Alpen LC&I. Julie-Ann Haines leads Northern Ireland from 1 July 2026.",
              s=["corp"], neo=[0, ""], src=[["Danske Bank: leadership", LEAD], ["ELT changes, Jun 2026", ELT26], ["Mortgage Solutions: Haines, Feb 2026", NIHEAD]]),
            P("brands", "Heritage & brands", "Founded in 1871 as Den Danske Landmandsbank; bought Northern Bank (2004) and Sampo Bank (2007). Brands include Danske Bank, Realkredit Danmark, Danica, Danske Invest and Nordania; 21,429 staff at end-2025, nearly half outside Denmark.",
              s=["con"], o="I", neo=[0, ""], src=[["Wikipedia: Danske Bank", WIKI], ["Annual Report 2025", AR25]]),
            P("estonia", "Estonia case closed", "The US DOJ probation from the Estonian branch case (December 2022 plea, about USD 2 billion) ended on 13 December 2025; Danske says all formal processes with authorities are finalised.",
              s=["corp"], st="retired", neo=[0, ""], src=[["Annual Report 2025", AR25], ["Wikipedia: Danske Bank", WIKI]]),
        ]},
        {"id": "1.3", "ic": "database", "name": "Technology & AI", "blurb": "DKK 4.5bn a year.", "div": "group", "rev": "other", "products": [
            P("tech", "One platform on AWS", "Over 30% of applications moved to public cloud since 2023, migration to Amazon Web Services ahead of plan, mainframe use being cut; annual investment in technology, AI and advisory up from about DKK 4.0 billion to about DKK 4.5 billion.",
              s=["corp"], at="AWS", neo=[0, ""], src=[["Forward '28 update, Apr 2026", F28], ["Annual Report 2025", AR25]]),
            P("ai", "GenAI & agentic AI", "DanskeGPT, Danske Assist and Microsoft Copilot used by most staff; a first multi-agent GenAI pilot in credit; an 'AI city' infrastructure; AI to give about DKK 2 billion a year of productivity by 2028.",
              s=["corp"], st="new", neo=[0, ""], src=[["Annual Report 2025", AR25], ["H1 2026 interim report", H1], ["Forward '28 update, Apr 2026", F28]]),
        ]},
        {"id": "1.4", "ic": "target", "name": "Forward '28", "blurb": "ROE above 14.5% by 2028.", "div": "group", "rev": "other", "products": [
            P("strategy", "Forward '28", "A focused Nordic bank built on advisory, digital, sustainability and one simple platform. Updated 30 April 2026: ROE above 14.5%, cost/income at most 43%, CET1 about 16% and income about DKK 63 billion by 2028; payout 60–70%.",
              s=["corp"], st="new", neo=[0, ""], src=[["Forward '28 update, Apr 2026", F28], ["Danske Bank: strategy", STRAT]]),
            P("deals", "Deals", "Sold its Aiia stake to Mastercard (2021), merged MobilePay into Vipps MobilePay (2022), and sold Norwegian personal banking to Nordea (completed 18 November 2024, about 235,000 customers).",
              s=["con"], o="A", st="retired", neo=[0, ""], src=[["Danske: Aiia sale, Sep 2021", AIIA], ["MobilePay merger, Jun 2021", MOBILEPAY], ["Nordea: Norway completed, Nov 2024", NORWAY]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: Danish debit on Mastercard or Visa/Dankort, Mastercard credit and premium cards, Mastercard cards in Finland, Sweden and Northern Ireland, Mastercard business cards, wallets and MobilePay, and transaction banking with a bank stablecoin.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit in Denmark", "blurb": "Mastercard or Visa/Dankort.", "div": "dk", "rev": "personal", "products": [
            P("hverdag", "Mastercard Hverdag+", "A Mastercard debit card with a DKK 100,000 daily limit, Apple Pay, Google Pay, Garmin Pay and MobilePay; customers in the Hverdag+ package can swap their Visa/Dankort for it free ⚠ launch date not found.", short="Hverdag+ (Mastercard)",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard debit."],
              mc="Danske's own route off Visa/Dankort for everyday spending.",
              src=[["Danske: Mastercard Hverdag+", HVERDAG], ["Danske: cards", DKCARDS]]),
            P("visadankort", "Visa/Dankort", "The co-badged Danish debit card: Dankort at home, Visa abroad and online (Visa limit DKK 25,000 per 30 days). Danske was the first bank with Dankort in Apple Pay (November 2024) and is the top debit issuer in Denmark ⚠.", short="Visa/Dankort",
              s=["con"], lc="everyday", o="P", at="Visa, Nets", neo=[0, "Visa and Dankort."],
              src=[["Danske: cards", DKCARDS], ["Tænk: Dankort in Apple Pay, Nov 2024", TAENK], ["Euromonitor: debit cards in Denmark", EUROMON]]),
            P("nets", "Card processing & Dankort deals", "Nets (now Nexi) processes all of Danske's Nordic card transactions under a five-year deal of 13 February 2019, alongside a direct five-year Dankort deal of 1 February 2019 ⚠ renewal terms not public.",
              s=["con"], lc="move", ay="Feb 2019", o="P", at="Nets", neo=[0, "Nets processes."],
              src=[["Nets: Nordic agreement, Feb 2019", NETS19], ["Danske: Dankort agreement, Feb 2019", DANKORT19]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit & premium cards", "blurb": "All Mastercard.", "div": "dk", "rev": "personal", "products": [
            P("dkcredit", "Mastercard Basis, Guld & Platin", "Credit cards with a debit side ('2 cards in 1'), up to 45 days interest-free (40 days from 20 November 2026); Platin adds Priority Pass, concierge and worldwide travel insurance.", short="Credit (Mastercard)",
              s=["con", "priv"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard credit."],
              src=[["Danske: cards", DKCARDS]]),
            P("worldelite", "World Elite Mastercard", "The Private Banking card, with family cards, for Danske's wealthiest customers.", short="World Elite (Mastercard)",
              s=["priv"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard World Elite."],
              src=[["Danske: World Elite terms", WE]]),
        ]},
        {"id": "2.3", "ic": "earth", "name": "Finland, Sweden & UK cards", "blurb": "Mastercard in all three.", "div": "nordic", "rev": "personal", "products": [
            P("ficards", "Finland: Mastercard Debit, Gold & Platinum", "Mastercard Debit, MunRahat Mastercard Debit for ages 8–14, and Gold and Platinum combo cards; K-Plussa loyalty, Apple Pay, Google Pay, MobilePay and Click to Pay.", short="Finland (Mastercard)",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["Danske Finland: cards", FICARDS]]),
            P("secards", "Sweden: Mastercard Bankkort & Direkt", "Mastercard Bankkort and Bankkort Start debit, Mastercard Direkt, Direkt Ung, Guld and Platinum credit; Apple Pay, Google Pay and Click to Pay.", short="Sweden (Mastercard)",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["Danske Sweden: cards", SECARDS]]),
            P("ukcards", "Northern Ireland: Debit Mastercard", "Debit Mastercard with contactless to £100, Danske 3D Secure and Priceless Cities offers, plus a Mastercard credit card; a youth account with a contactless debit card from age 8.", short="UK (Mastercard)",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["Danske UK: Debit Mastercard", UKDEBIT], ["H1 2026 interim report", H1]]),
        ]},
        {"id": "2.4", "ic": "briefcase-business", "name": "Business cards", "blurb": "Mastercard Corporate.", "div": "dk", "rev": "business", "products": [
            P("corpcards", "Mastercard Corporate & Business Debit", "Mastercard Corporate Platinum, Gold and Classic credit cards and Mastercard Business Debit, managed in District's card module. No purchasing or virtual card is listed.", short="Corporate (Mastercard)",
              s=["sme", "corp"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard commercial."],
              mc="No virtual or purchasing card in the range.",
              src=[["Danske: business cards", BIZCARDS]]),
            P("travel", "Mastercard Corporate Travel Account", "Pools a company's travel-agency bookings on one account, with data flowing to accounting and expense systems.",
              s=["corp"], lc="move", o="P", at="Mastercard", neo=[2, "Mastercard."],
              src=[["Danske: business cards", BIZCARDS]]),
            P("gdr", "Mastercard card data feeds", "Corporate card transactions delivered as CDF3 files from Mastercard's Global Data Repository into SAP Concur, Oracle and Visma.",
              s=["corp"], lc="move", o="P", at="Mastercard", neo=[3, "Mastercard's own data service."],
              src=[["Danske: business cards", BIZCARDS]]),
        ]},
        {"id": "2.5", "ic": "smartphone", "name": "Wallets & MobilePay", "blurb": "Phones and a 28% stake.", "div": "mobilepay", "rev": "personal", "products": [
            P("mobilepay", "MobilePay (Vipps MobilePay)", "Danske built MobilePay and merged it with Vipps and Pivo (agreed June 2021; about 11 million users then); it holds about 28% ⚠. MobilePay carries about 8 in 10 Danish person-to-person payments; its in-store contactless (2025) runs on card rails.", short="MobilePay",
              s=["con"], lc="move", o="P", at="Vipps MobilePay", neo=[1, "Rides on the card beneath, any network."],
              src=[["MobilePay merger, Jun 2021", MOBILEPAY], ["Nationalbanken, Jun 2026", NBDK], ["Annual Report 2025", AR25]]),
            P("wallets", "Apple Pay, Google Pay & Garmin Pay", "Wallets on Danske cards in every market; nearly one in three Danish in-store payments was by wallet in 2025, and 51% of Danes had one.",
              s=["con"], lc="everyday", o="P", at="Apple, Google", neo=[1, "Mastercard tokens for Mastercard cards; Visa for Visa/Dankort."],
              src=[["Danske: Mastercard Hverdag+", HVERDAG], ["Nationalbanken, Jun 2026", NBDK]]),
        ]},
        {"id": "2.6", "ic": "coins", "name": "Transaction banking & digital money", "blurb": "FX, instant, stablecoin.", "div": "group", "rev": "lci", "products": [
            P("fx", "Cash management & FX", "Cash management, transaction services and FX lifted daily-banking fees about 9% a year across business segments; DanskeFX OneClick and DanskeFX Trader launched in 2025.",
              s=["sme", "corp"], lc="move", st="new", neo=[0, ""], src=[["Annual Report 2025", AR25], ["H1 2026 interim report", H1]]),
            P("scf", "Supply chain finance", "A funding bank on PrimeRevenue's supply chain finance platform since 2025.",
              s=["corp"], lc="borrow", st="new", o="P", at="PrimeRevenue", neo=[0, ""], src=[["Annual Report 2025", AR25]]),
            P("instant", "Instant transfers", "Danish instant account transfers since 2014; account-based payments are still only about 7% of digital retail payments (2025).",
              s=["con", "sme"], lc="move", neo=[0, "Account-to-account."], src=[["Nationalbanken, Jun 2026", NBDK]]),
            P("qivalis", "Qivalis euro stablecoin", "A founding member (25 September 2025) of Qivalis, a bank-owned euro stablecoin issuer seeking a Dutch e-money licence, with launch planned for H2 2026 ⚠.",
              s=["corp"], lc="move", st="new", ay="Sep 2025", o="P", at="Qivalis", neo=[0, "Bank-owned stablecoin."],
              mc="Danske is co-building the bank stablecoin rail itself.",
              src=[["Qivalis: launch H2 2026", QIVALIS], ["Annual Report 2025", AR25]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: card controls and Mastercard passkeys, Denmark's first agentic payment, cashback on Mastercard cards, Premium APIs and an MCP server, and AI that handles a fifth of enquiries.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & identity", "blurb": "Card controls, passkeys.", "div": "group", "rev": "personal", "products": [
            P("cardcontrols", "Card controls & 3D Secure", "Geographic control that keeps a card active on one continent at a time, online spending switched on and off in the app, and Danske 3D Secure; financial crime prevention sits with the head of Personal Customers.",
              s=["con"], lc="everyday", neo=[0, "Danske's own."], src=[["Danske: Mastercard Hverdag+", HVERDAG], ["Danske UK: Debit Mastercard", UKDEBIT]]),
            P("passkeys", "Mastercard Payment Passkeys", "Used to authenticate the agent payment in the September 2026 pilot ⚠ not yet a general customer service.",
              s=["con"], lc="everyday", st="new", ay="Sep 2026", o="P", at="Mastercard", neo=[3, "Mastercard's own ⚠ pilot."],
              src=[["Crowdfund Insider: Agent Pay, Sep 2026", AGENT]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "Agentic payments", "blurb": "Denmark's first.", "div": "dk", "rev": "personal", "products": [
            P("agentpay", "Mastercard Agent Pay pilot", "Denmark's first AI-agent payment (21 September 2026): an assistant booked a coffee tasting on Priceless.com and paid with a Danske Mastercard, using Agent Pay, agentic tokens and passkeys, with PayOS. Led by Mark Wraa-Hansen (Danske) and Erik Gutwasser (Mastercard).", short="Agent Pay (Mastercard)",
              s=["con"], lc="move", st="new", ay="Sep 2026", o="P", at="Mastercard, PayOS", neo=[3, "Mastercard Agent Pay."],
              mc="The newest joint work; the test is whether it reaches customers.",
              src=[["Crowdfund Insider: Agent Pay, Sep 2026", AGENT]]),
            P("mcp", "MCP server for corporates", "A pilot that lets corporate clients connect their own AI assistants to bank data through Premium APIs, built with Amazon Bedrock and AgentCore.",
              s=["corp"], lc="open", st="new", at="AWS", neo=[0, ""],
              src=[["Crowdfund Insider: Agent Pay, Sep 2026", AGENT], ["Danske: developer portal", DEV]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Loyalty & offers", "blurb": "Cashback on Mastercard.", "div": "dk", "rev": "personal", "products": [
            P("cashback", "Cashback til Mastercard", "Card-linked cashback at more than 2,000 Danish shops, restaurants and webshops, paid as cash from DKK 100; private Mastercards only, run by Loyalty Key A/S.",
              s=["con", "priv"], lc="grow", o="P", at="Loyalty Key", neo=[1, "Mastercard cards only; run by Loyalty Key."],
              mc="A reason to hold a Mastercard over Visa/Dankort.",
              src=[["Danske: Cashback", CASHBACK]]),
            P("priceless", "Priceless Cities", "Priceless offers on Northern Ireland Debit Mastercard; Priceless.com hosted the 2026 agent pilot.",
              s=["con"], lc="beyond", o="P", at="Mastercard", neo=[3, "Mastercard's own."],
              src=[["Danske UK: Debit Mastercard", UKDEBIT], ["Crowdfund Insider: Agent Pay, Sep 2026", AGENT]]),
        ]},
        {"id": "3.4", "ic": "code-xml", "name": "APIs & open banking", "blurb": "Premium APIs, Aiia.", "div": "group", "rev": "lci", "products": [
            P("apis", "Premium APIs", "Account Transaction & Balance, Payment Initiation and Payment Collection APIs for corporate systems, regulatory (PSD2) APIs and an MCP service.",
              s=["corp", "sme"], lc="open", neo=[0, ""], src=[["Danske: developer portal", DEV]]),
            P("aiia", "Account aggregation (Aiia)", "Danske co-owned Aiia from 2018 and built multibank views in its app with it; sold its stake to Mastercard in September 2021 and promised continued collaboration ⚠ current use not confirmed.",
              s=["con"], lc="everyday", ay="Sep 2021", o="P", at="Mastercard", neo=[3, "Mastercard Open Banking ⚠."],
              src=[["Danske: Aiia sale, Sep 2021", AIIA]]),
        ]},
        {"id": "3.5", "ic": "brain", "name": "AI & advice tools", "blurb": "A fifth of enquiries.", "div": "dk", "rev": "personal", "products": [
            P("assistant", "AI Assistant", "24/7 help in Danske Mobile Banking in Denmark (2025), handling about 20% of enquiries and cutting human-chat waits below two minutes.",
              s=["con"], lc="everyday", st="new", neo=[0, ""], src=[["Annual Report 2025", AR25]]),
            P("panorama", "Panorama", "An advisory tool giving customers a full financial overview; about 600 advisers trained and adviser efficiency up about 50%.",
              s=["priv", "home"], lc="grow", st="new", neo=[0, ""], src=[["H1 2026 interim report", H1]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: personal banking in Denmark, Finland and Sweden, Realkredit Danmark mortgages, Private Banking, Danske Invest and Danica, business banking and Nordania, corporate and institutional banking, and Northern Ireland.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Personal banking", "blurb": "Pre-tax DKK 5.2bn in H1.", "div": "dk", "rev": "personal", "products": [
            P("personal", "Personal Customers", "Everyday banking in Denmark, Finland and Sweden: pre-tax profit DKK 5.2 billion in H1 2026 (up 24%); gaining share in Finland. About 5 million retail customers ⚠ secondary.",
              s=["con"], lc="everyday", neo=[1, "Mastercard and Visa/Dankort cards."], src=[["H1 2026 interim report", H1], ["Wikipedia: Danske Bank", WIKI]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Home finance", "blurb": "Realkredit Danmark.", "div": "rd", "rev": "personal", "products": [
            P("mortgages", "Realkredit Danmark", "Danish mortgage lending funded by DKK 730 billion of covered bonds at 30 June 2026, rated AAA; home finance assessments within 24 hours.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["H1 2026 interim report", H1], ["Annual Report 2025", AR25]]),
            P("boligstart", "Danske BoligStart", "Advice and the lowest variable rate in Danske's spread for first-time buyers aged 18–38.",
              s=["home"], lc="borrow", st="new", neo=[0, ""], src=[["H1 2026 interim report", H1]]),
        ]},
        {"id": "4.3", "ic": "gem", "name": "Wealth & pensions", "blurb": "Danske Invest, Danica.", "div": "invest", "rev": "danica", "products": [
            P("privatebanking", "Private Banking & Premium", "Private Banking customers up 8% net since 2023, a new Premium offering and a family-office team in Denmark.",
              s=["priv"], lc="grow", st="new", neo=[1, "World Elite Mastercard."], src=[["H1 2026 interim report", H1], ["Annual Report 2025", AR25]]),
            P("invest", "Danske Invest", "Danish retail fund leader again with a 21.7% share (2025); retail and institutional assets under management up 30% since 2023.",
              s=["priv", "saver"], lc="grow", neo=[0, ""], src=[["Annual Report 2025", AR25], ["H1 2026 interim report", H1]]),
            P("danica", "Danica Pension", "Pensions and health insurance with DKK 551 billion under management; insurance result DKK 851 million in H1 2026; pension sales through the bank doubled in three years.",
              s=["saver"], lc="grow", neo=[0, ""], src=[["H1 2026 interim report", H1], ["H1 2026 release", H1PR]]),
        ]},
        {"id": "4.4", "ic": "briefcase", "name": "Business banking", "blurb": "The Nordic Business Bank.", "div": "group", "rev": "business", "products": [
            P("business", "Business Customers", "SMEs and mid-corporates across the Nordics: pre-tax profit DKK 5.1 billion in H1 2026, lending up about 7% since 2023 and green lending of DKK 76 billion (May 2026).",
              s=["sme"], lc="borrow", neo=[1, "Business cards on Mastercard."], src=[["H1 2026 interim report", H1], ["Annual Report 2025", AR25]]),
            P("nordania", "Nordania Leasing", "Vehicle leasing and low-priced EV loans, plus charging stations.",
              s=["sme", "con"], lc="borrow", neo=[0, ""],
              mc="Fleet and fuel cards are untested ground.",
              src=[["H1 2026 interim report", H1]]),
        ]},
        {"id": "4.5", "ic": "factory", "name": "Corporates & institutions", "blurb": "Pre-tax DKK 4.6bn.", "div": "group", "rev": "lci", "products": [
            P("lci", "Large Corporates & Institutions", "Markets, debt capital markets (Nordic high-yield share 8.7% in 2025), transaction banking and asset management; about 90 new customers outside Denmark and 45 house-bank mandates since 2023; pre-tax DKK 4.6 billion in H1 2026.",
              s=["corp"], lc="move", neo=[0, ""], src=[["H1 2026 interim report", H1], ["Annual Report 2025", AR25]]),
        ]},
        {"id": "4.6", "ic": "flag", "name": "Northern Ireland", "blurb": "Danske Bank UK.", "div": "uk", "rev": "other", "products": [
            P("ni", "Danske Bank UK", "The former Northern Bank: pre-tax DKK 1.2 billion in H1 2026, about 6,800 new current accounts and 900 new small businesses in the half, and about 100 million digital logins a year.",
              s=["con", "sme"], lc="everyday", neo=[1, "Cards on Mastercard."], src=[["H1 2026 interim report", H1], ["Annual Report 2025", AR25]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Danske: Danske Mobile Banking, District for businesses, and branches, advisers and partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Danske Mobile Banking", "blurb": "AI, homes, investing.", "div": "dk", "rev": "personal", "products": [
            P("app", "Danske Mobile Banking", "The personal app with the AI Assistant, a 'housing universe', a digital investment hub and card controls.",
              s=["con", "priv"], lc="everyday", neo=[0, ""], src=[["Annual Report 2025", AR25]]),
        ]},
        {"id": "5.2", "ic": "monitor", "name": "District", "blurb": "New platform, 71,000 moved.", "div": "group", "rev": "business", "products": [
            P("district", "District & District Mobile", "The business platform, rebuilt in Denmark in 2025 with about 71,000 customers moved; District Mobile live in Denmark and Norway, Sweden and Finland to follow; District Marketplace.",
              s=["sme", "corp"], lc="open", st="new", neo=[0, ""], src=[["Annual Report 2025", AR25]]),
        ]},
        {"id": "5.3", "ic": "users-round", "name": "Branches & partners", "blurb": "Advisers and alliances.", "div": "group", "rev": "personal", "products": [
            P("branches", "Branches & advisers", "Advisory meetings scoring above 9 out of 10 in Denmark, Sweden and Finland; more than 1,000 business advisers retrained.",
              s=["con", "sme"], lc="open", neo=[0, ""], src=[["Annual Report 2025", AR25]]),
            P("partners", "Partnerships", "Fennia and AKAVA in Finland, SPP in Sweden, NRGi in Denmark (energy tool), and Tryg for card insurance.",
              s=["con"], lc="open", o="P", at="Fennia, AKAVA, SPP, NRGi", neo=[0, ""], src=[["Annual Report 2025", AR25], ["H1 2026 interim report", H1]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Danske", "blurb": "Most cards, and the first agent payment.", "products": [
        P("mcatdanske", "Mastercard at Danske", "Mastercard carries Danske's Danish credit and premium cards, Hverdag+ debit and all business cards, and every card in Finland, Sweden and Northern Ireland. Visa shares only the co-badged Visa/Dankort. Mastercard bought Aiia from Danske in 2021, and the two ran Denmark's first agent payment in September 2026. No master agreement is public ⚠.",
          s=["con"], div="group", rev="other", mc="The relationship this map is drawn for.",
          src=[["Danske: cards", DKCARDS], ["Crowdfund Insider: Agent Pay, Sep 2026", AGENT], ["Danske: Aiia sale, Sep 2021", AIIA]]),
    ]},
    {"id": "pillar-market", "name": "Danish payments", "blurb": "Dankort fading, wallets rising.", "products": [
        P("market", "The Danish market", "International cards reached about 1.5 billion transactions in 2025 while Dankort fell to just over 0.8 billion; wallets take nearly a third of in-store payments; Nets is the only Dankort processor, and a 2025 law opens access ⚠.",
          s=["con"], div="group", rev="other", src=[["Nationalbanken, Jun 2026", NBDK], ["Ing.dk: Nets and Dankort, Feb 2025", NETSMONO]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
