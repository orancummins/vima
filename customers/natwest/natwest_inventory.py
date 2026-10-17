"""NatWest Group's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 results (31 July 2026) and FY2025
results (13 February 2026). ``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own
product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

IR = "https://investors.natwestgroup.com/~/media/Files/R/RBS-IR-V2/results-center/"
H1 = IR + "31072026/nwg-h1-2026-results.pdf"
FB = IR + "31072026/nwg-h1-2026-investor-factbook.pdf"
FY25 = IR + "13022026/nwg-company-announcement.pdf"
NWG = "https://www.natwestgroup.com/"
TECH = NWG + "who-we-are/about-natwest-group/tech-data-and-AI.html"
H1W = NWG + "news-and-insights/latest-stories/financial-reporting/2026/jul/h1-2026-natwest-group-results.html"
DEBIT = "https://www.retailbankerinternational.com/news/natwest-switches-debit-cards-to-mastercard/"
NILSON = "https://nilsonreport.com/articles/natwest-cards-to-mastercard/"
CFR = "https://newsroom.mastercard.com/news/press/2024/april/mastercard-transforms-the-fight-against-scams-with-latest-ai-tech/"
VISA_TR = "https://corporate.visa.com/en/sites/visa-perspectives/company-news/natwest-and-visa-launch-new-credit-card-to-support-and-reward-uk-customers.html"
A2B = "https://www.pymnts.com/partnerships/2024/mastercard-natwest-launch-mobile-virtual-card-partnership/"
AGENTIC = NWG + "news-and-insights/news-room/press-releases/2026/global-banks-collaborate-on-principles-for-trusted-agentic-comme.html"
VISA_AGENT = "https://www.fstech.co.uk/fst/Visa_Partners_With_European_Banks_And_Merchants_For_Agentic_Commerce_Launch.php"
PSR = "https://www.psr.org.uk/media/b50p3mlm/psr-2024-app-scam-performance-data-february-2026.pdf"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · ownership · brands", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a £745 billion balance sheet returning nearly 20%, private again since the government sold its last shares in May 2025, Coutts and the Royal Bank of Scotland among its brands, £1.2 billion a year on technology and AI, and targets to 2028.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & capital", "blurb": "£745 billion, RoTE 19.7%.", "div": "nwg", "rev": "grp", "products": [
            P("balance", "Balance sheet", "Total assets of £745.4 billion, loans of £435.9 billion and deposits of £448.6 billion at 30 June 2026; more than 20 million customers and about 1.5 million businesses.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 results", H1]]),
            P("earnings", "Earnings", "Operating profit of £7.7 billion in 2025 (RoTE 19.2%) and £4.3 billion in the first half of 2026 (RoTE 19.7%), with income of £8.9 billion and a cost:income ratio of 46%; 2026 guidance raised to a RoTE above 19%.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 results", H1], ["FY2025 results", FY25]]),
            P("capital", "Capital & ratings", "CET1 of 13.2% after the Evelyn deal; the holding company rated A3, A- and A+, the ring-fenced banks A1, A+ and AA; market value about £53 billion in mid-October 2026.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 investor factbook", FB]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Ownership & leadership", "blurb": "Private again since May 2025.", "div": "nwg", "rev": "grp", "products": [
            P("govexit", "The end of state ownership", "The 2008 rescue (£45.5 billion, up to 84% owned) ended when the Treasury sold its last shares on 30 May 2025, about £35 billion having been returned.",
              s=["corp"], neo=[0, ""], src=[["HM Treasury: government completes exit from NatWest, May 2025", "https://www.gov.uk/government/news/government-completes-exit-from-natwest--2"]]),
            P("leadership", "Board & leadership", "CEO Paul Thwaite (since 2023), chair Rick Haythornthwaite (2024), CFO Katie Murray; Solange Chamberlain runs Retail Banking (July 2025), Robert Begbie Commercial & Institutional and Emma Crystal Private Banking & Wealth; Mark Brant is chief payments officer.",
              s=["corp"], neo=[0, ""], src=[["NatWest Group: board", NWG + "who-we-are/board-and-governance/group-board.html"]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brands", "blurb": "Coutts 1692, RBS 1727.", "div": "nwg", "rev": "grp", "products": [
            P("heritage", "From Coutts to NatWest Group", "Coutts (1692), the Royal Bank of Scotland (1727) and Ulster Bank (1836); NatWest from 1970; RBS took over NatWest in 2000 and the group became NatWest Group in 2020. Ulster Bank left the Republic of Ireland in 2023.",
              s=["con", "corp"], o="I", neo=[0, ""], src=[["NatWest Group: our history", NWG + "who-we-are/about-natwest-group/our-history.html"]]),
            P("brands", "Brands", "NatWest, Royal Bank of Scotland, Ulster Bank (Northern Ireland), Coutts, Evelyn Partners, Lombard, RBS International, Holt's, FreeAgent, Mettle, Tyl, Rooster Money and NatWest Boxed.",
              s=["con", "sme", "aff"], neo=[0, ""], src=[["NatWest Group: our brands", NWG + "who-we-are/our-brands.html"]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI core", "blurb": "OpenAI, AWS, Google.", "div": "nwg", "rev": "grp", "products": [
            P("tech", "Technology, data & AI", "£1.2 billion invested in technology, data and AI in 2025; partnerships with OpenAI (March 2025, the first UK bank to do so), AWS, Accenture and Google; an engineering hub in Bengaluru; AI tools for all 60,000 colleagues and AI coding tools for more than 12,000 engineers.",
              s=["corp"], o="P", at="OpenAI, AWS, Accenture, Google", neo=[0, ""], src=[["NatWest Group: tech, data and AI", TECH]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "RoTE above 18% to 2028.", "div": "nwg", "rev": "grp", "products": [
            P("strategy", "2028 targets", "Disciplined growth, simplification and active balance-sheet management: RoTE above 18%, cost:income below 45% and CET1 about 13% by 2028, with about half of profits paid out.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 results", H1]]),
            P("deals", "Acquisitions", "Metro Bank mortgages (2020, 2024), Sainsbury's Bank (2025, about a million customers and a £1.1 billion card book) and Evelyn Partners (completed 30 June 2026 for £2.2 billion, £71.7 billion of client assets); Cushon was sold to WTW in 2026.",
              s=["con", "aff"], o="A", neo=[0, ""], src=[["H1 2026 results", H1], ["FY2025 results", FY25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Five ways money moves: 16 million debit cards on Mastercard since 2021, credit cards mostly on Mastercard, Tyl for merchants, Payit for open-banking payments, and Bankline, FX and virtual cards for companies.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "16 million, to Mastercard in 2021.", "div": "natwest", "rev": "retail", "products": [
            P("mcdebit", "Mastercard debit", "In February 2021 the group agreed to move about 16 million personal and business debit cards across NatWest, RBS, Ulster Bank and Coutts from Visa to Mastercard; Nilson put 2019 debit spend at $148 billion, Europe's third-largest debit issuer. Mastercard said it then held one in three UK debit cards.", short="Mastercard debit (16m)",
              s=["con", "sme", "aff"], lc="everyday", o="P", at="Mastercard", ay="Feb 2021", neo=[2, "Mastercard, converted from Visa."],
              mc="The foundation of the relationship: the third-largest debit book in Europe, with a contract term that has not been made public.",
              src=[["Retail Banker International: NatWest switches debit to Mastercard, Feb 2021", DEBIT], ["Nilson Report: NatWest cards to Mastercard, Feb 2021", NILSON]]),
            P("rooster", "Rooster Card", "A prepaid card for 6–17-year-olds from NatWest Rooster Money, issued under licence from Visa.",
              s=["young"], lc="everyday", o="A", neo=[0, "Visa prepaid."], src=[["Rooster Money", "https://www.roostermoney.com/gb/"]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Mostly Mastercard.", "div": "natwest", "rev": "retail", "products": [
            P("credit", "NatWest & RBS credit cards", "Reward, Reward Black, The NatWest Credit Card and balance-transfer cards, mostly Mastercard, within about £20 billion of unsecured balances.",
              s=["con", "aff"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard for the core range."],
              src=[["NatWest: credit cards", "https://www.natwest.com/credit-cards.html"], ["H1 2026 investor factbook", FB]]),
            P("travelreward", "Travel Reward & Sainsbury's cards (Visa)", "The Travel Reward credit card launched on Visa in August 2024 alongside NatWest's Team GB sponsorship; the Sainsbury's Bank Nectar cards taken over in 2025 are reportedly moving from Mastercard to Visa.", short="Travel Reward (Visa)",
              s=["con"], lc="borrow", st="new", ay="Aug 2024", o="P", at="Visa", neo=[0, "Visa."],
              mc="Visa's foothold in a Mastercard bank: two credit portfolios in two years.",
              src=[["Visa: NatWest Travel Reward card, Aug 2024", VISA_TR]]),
        ]},
        {"id": "2.3", "ic": "store", "name": "Merchant acquiring", "blurb": "Tyl.", "div": "tyl", "rev": "ci", "products": [
            P("tyl", "Tyl by NatWest", "Card acceptance for small businesses since May 2019, built with Pollinate (in which RBS and Mastercard both invested) on First Data processing: card machines, online payments and Tap to Pay on phones, for NatWest, RBS and Ulster Bank business customers.",
              s=["sme"], lc="move", o="P", at="Pollinate, Fiserv", ay="May 2019", neo=[1, "Accepts Mastercard; Mastercard co-invested in Pollinate."],
              src=[["Tyl by NatWest", "https://tylbynatwest.com/time-for-tyl"], ["Scottish Financial News: RBS and Mastercard invest in Pollinate, Nov 2019", "https://www.scottishfinancialnews.com/articles/rbs-and-partners-invest-in-international-payments-business-pollinate"]]),
        ]},
        {"id": "2.4", "ic": "zap", "name": "Open banking payments", "blurb": "Payit and VRPs.", "div": "natwest", "rev": "ci", "products": [
            P("payit", "Payit", "NatWest's own open-banking payments: account-to-account over Faster Payments, recurring payments and account data for businesses, more than £1 billion processed by 2022 and variable recurring payments with TrueLayer, GoCardless, Token, Tink and Yapily. NatWest also joined Mastercard's Pay by Bank app in 2021.",
              s=["sme", "corp", "fin"], lc="move", ay="2020", neo=[0, "NatWest's own A2A."],
              mc="Payit is pitched as a replacement for card-on-file and Direct Debit, so it competes as much as it partners.",
              src=[["NatWest: Payit", "https://www.natwest.com/business/business-services/payit.html"], ["FStech: Mastercard Pay by Bank app, Aug 2021", "https://fstech.co.uk/fst/NatWest_Latest_Bank_To_Offer_Mastercard_Pay_By_Bank.php"]]),
        ]},
        {"id": "2.5", "ic": "arrow-left-right", "name": "Corporate payments & FX", "blurb": "Bankline, FX, virtual cards.", "div": "nwg", "rev": "ci", "products": [
            P("bankline", "Bankline & FX", "Bankline, the corporate payments channel, re-platformed in 2025 with generative-AI help from 2026; international payments in more than 130 currencies.",
              s=["corp", "sme"], lc="move", neo=[0, ""], src=[["FY2025 results", FY25], ["H1 2026 results", H1]]),
            P("approval2buy", "Approval2Buy", "Commercial virtual cards on Mastercard's mobile virtual card app (November 2024), the first such service in Europe.",
              s=["corp", "sme"], lc="move", st="new", ay="Nov 2024", o="P", at="Mastercard", neo=[3, "Mastercard's virtual card app."],
              src=[["PYMNTS: Mastercard and NatWest mobile virtual card, Nov 2024", A2B]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account and payment: scam scoring that makes NatWest the UK's best at not receiving scam money, Cora and its OpenAI-built successors, AI for colleagues, embedded finance and agentic principles, and Mastercard savings for business customers.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & scams", "blurb": "Best in the UK for scams received.", "div": "nwg", "rev": "grp", "products": [
            P("cfr", "Consumer Fraud Risk", "Mastercard's AI scam-scoring for account-to-account payments, used by NatWest since 2023 among the first banks anywhere. In the regulator's 2024 data NatWest ranked best of 20 for scam money received and fourth for refunds.", short="Consumer Fraud Risk",
              s=["con", "sme"], lc="everyday", o="P", at="Mastercard", ay="2023", neo=[3, "Mastercard's own product."],
              mc="Already live; the next steps are the receiving-side scores and the regulator's December 2026 review of the reimbursement cap and split.",
              src=[["Mastercard: AI against scams, Apr 2024", CFR], ["PSR: 2024 APP scam data, Feb 2026", PSR]]),
            P("cora_fraud", "Fraud help in Cora", "Report and resolve fraud by conversation with the Cora assistant, planned for 2026.",
              s=["con"], lc="everyday", st="new", neo=[0, ""], src=[["ResultSense: NatWest invests £1.2bn in AI, Feb 2026", "https://www.resultsense.com/news/2026-02-17-natwest-invests-1-2bn-in-ai-transformation/"]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "Cora & AI assistants", "blurb": "12.9 million conversations.", "div": "natwest", "rev": "retail", "products": [
            P("cora", "Cora & Cora+", "The digital assistant since about 2017: 12.9 million retail conversations in 2025 and 21 generative-AI journeys by the end of the year.",
              s=["con"], lc="everyday", neo=[0, ""], src=[["NatWest Group: tech, data and AI", TECH]]),
            P("spendingchat", "Cora Spending Chat & NatWest in ChatGPT", "An agentic assistant built on OpenAI models that answers questions about spending (25,000 customers by early 2026), and a mortgage app inside ChatGPT (April 2026), the first UK bank there.",
              s=["con", "home"], lc="everyday", st="new", ay="2026", o="P", at="OpenAI", neo=[0, ""],
              mc="Spending answers depend on clean merchant names and categories, which is what Mastercard's data enrichment provides.",
              src=[["FStech: agentic financial assistant, 2026", "https://fstech.co.uk/fst/Thousands_Of_NatWest_Customers_To_Soon_Have_Access_To_Agentic_Financial_Assistant.php"], ["NatWest Group: tech, data and AI", TECH]]),
        ]},
        {"id": "3.3", "ic": "brain", "name": "AI at work", "blurb": "Agents in onboarding and service.", "div": "nwg", "rev": "grp", "products": [
            P("colleagueai", "Colleague AI & C&I agents", "Copilot Chat and an internal model for every colleague, complaint and call summaries saving 70,000–90,000 hours a year in Retail, and five AI agents live in commercial onboarding, operations and servicing (2026).",
              s=["corp"], lc="beyond", st="new", neo=[0, ""], src=[["H1 2026 results", H1], ["NatWest Group: tech, data and AI", TECH]]),
        ]},
        {"id": "3.4", "ic": "webhook", "name": "Embedded & agentic", "blurb": "Principles, partners, Boxed.", "div": "nwg", "rev": "grp", "products": [
            P("agentic", "Agentic commerce", "NatWest co-published principles for trusted agentic commerce with Bank of America, Capital One, CBA, ING and ASB (22 September 2026), naming no network; it is among 30-plus European issuers live on Visa's agentic payments (July 2026). No Mastercard Agent Pay transaction with NatWest has been announced.",
              s=["con", "fin"], lc="move", st="new", ay="Sep 2026", neo=[0, "Visa first, on the public record."],
              mc="The clearest gap: Mastercard holds the debit book, Visa has the first agentic transactions.",
              src=[["NatWest Group: principles for trusted agentic commerce, Sep 2026", AGENTIC], ["FStech: Visa's agentic launch with European banks, Jul 2026", VISA_AGENT]]),
            P("boxed", "NatWest Boxed & FinTech Growth Programme", "Embedded banking for partners (moved into Retail Banking in 2026) and an accelerator for fintechs, with eight AI firms in the 2026 cohort.",
              s=["fin"], lc="beyond", neo=[0, ""], src=[["H1 2026 results", H1], ["NatWest Group: tech, data and AI", TECH]]),
        ]},
        {"id": "3.5", "ic": "gift", "name": "Loyalty & savings", "blurb": "Savings from Mastercard.", "div": "natwest", "rev": "retail", "products": [
            P("loyalty", "Business Savings from Mastercard & Reward", "Automatic merchant discounts for business debit-card holders (Business Savings from Mastercard), a Mastercard Business Bonus for Mettle, and the Reward account and cards for consumers.",
              s=["sme", "con"], lc="grow", o="P", at="Mastercard", neo=[2, "Mastercard's merchant-savings programme."],
              src=[["Mettle", "https://www.mettle.co.uk/"], ["Finextra: NatWest to convert debit cards to Mastercard", "https://www.finextra.com/newsarticle/37414/natwest-to-convert-all-debit-cards-to-mastercard"]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "Retail Banking, Private Banking & Wealth Management, and Commercial & Institutional, opened out into what more than 20 million customers buy: current accounts and mortgages, Coutts and Evelyn, and the UK's biggest bank for business.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "Everyday banking", "blurb": "19 million retail customers.", "div": "natwest", "rev": "retail", "products": [
            P("accounts", "Current accounts & Premier", "Current accounts for more than 19 million retail customers, with Premier for 529,000 affluent customers; 95% of retail customers bank digitally.",
              s=["con", "aff"], lc="everyday", neo=[2, "Mastercard debit."], src=[["FY2025 results", FY25], ["H1 2026 results web story", H1W]]),
            P("youth", "NatWest Rooster Money", "Pocket money and junior accounts for 2.4 million young customers (NPS +72), with Junior ISAs up about 50%.",
              s=["young"], lc="open", o="A", ay="2021", neo=[0, "Rooster Card on Visa."], src=[["FY2025 results", FY25]]),
        ]},
        {"id": "4.2", "ic": "house", "name": "Mortgages", "blurb": "£219 billion, third in the UK.", "div": "natwest", "rev": "retail", "products": [
            P("mortgages", "Home loans", "A £219 billion mortgage book, third-largest in the UK and first in digital mortgages; £8.2 billion to first-time buyers in the first half of 2026, Family-Backed Mortgages, and partnerships with Rightmove and Landbay.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["H1 2026 investor factbook", FB], ["H1 2026 results", H1]]),
        ]},
        {"id": "4.3", "ic": "coins", "name": "Savings & investing", "blurb": "ISAs up 20%.", "div": "natwest", "rev": "retail", "products": [
            P("savings", "Savings, ISAs & investing", "ISA openings up 20% and investing customers up 32% in the first half of 2026, with Bestinvest trialled for retail customers.",
              s=["con", "aff"], lc="grow", neo=[0, ""], src=[["H1 2026 results", H1]]),
        ]},
        {"id": "4.4", "ic": "gem", "name": "Private banking & wealth", "blurb": "£131 billion of client assets.", "div": "coutts", "rev": "pbwm", "products": [
            P("coutts", "Coutts", "Private banking for high and ultra-high-net-worth clients (NPS +64), with the Silk card, a Mastercard.",
              s=["aff"], lc="grow", neo=[1, "Silk card on Mastercard; debit Mastercard."], src=[["H1 2026 results", H1], ["Coutts: Silk card", "https://www.coutts.com/private-banking/banking/silk-credit-card.html"]]),
            P("evelyn", "Evelyn Partners & Bestinvest", "Investment management and financial planning bought for £2.2 billion (June 2026), taking client assets to £130.6 billion and making the group, by its own account, the UK's leading private bank and wealth manager.",
              s=["aff"], lc="grow", st="new", ay="Jun 2026", o="A", neo=[0, ""], src=[["H1 2026 results", H1]]),
        ]},
        {"id": "4.5", "ic": "store", "name": "Business banking", "blurb": "One in five UK start-ups.", "div": "natwest", "rev": "ci", "products": [
            P("smebank", "Business banking & Accelerator", "Banking for about 1.5 million businesses, including one in five UK start-ups, business debit cards on Mastercard, and 15 Accelerator programmes for 25,000 customers.",
              s=["sme"], lc="everyday", neo=[2, "Business debit on Mastercard."], src=[["H1 2026 results web story", H1W], ["FY2025 results", FY25]]),
        ]},
        {"id": "4.6", "ic": "building-2", "name": "Commercial & institutional", "blurb": "Mid-market to infrastructure.", "div": "nwg", "rev": "ci", "products": [
            P("midmarket", "Mid-market & corporates", "£78 billion of mid-market and £83 billion of corporate and institutional loans; the UK's leading infrastructure and project-finance lender, IP-backed and venture lending, and Lombard asset finance.",
              s=["corp"], lc="borrow", neo=[1, "Commercial virtual cards on Mastercard."], src=[["H1 2026 investor factbook", FB], ["H1 2026 results", H1]]),
            P("climatefin", "Climate & social-housing finance", "£20.2 billion of climate and transition finance in the first half of 2026 towards £200 billion by 2030, and £10 billion for social housing by 2028.",
              s=["corp"], lc="borrow", neo=[0, ""],
              mc="A carbon footprint on business card spend would sit alongside the bank's transition-finance targets.",
              src=[["H1 2026 results", H1]]),
        ]},
        {"id": "4.7", "ic": "chart-candlestick", "name": "Markets & offshore", "blurb": "NatWest Markets, RBS International.", "div": "nwg", "rev": "ci", "products": [
            P("markets", "NatWest Markets & RBS International", "FX, rates and debt capital markets for corporates and institutions, and banking in Jersey, Guernsey, the Isle of Man and Gibraltar.",
              s=["corp"], lc="grow", neo=[0, ""], src=[["H1 2026 investor factbook", FB]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: apps used by 11.4 million people, 336 branches kept open to 2029, Mettle and FreeAgent for small firms, relationship managers for companies, and niche brands from Holt's to the Isle of Man Bank.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "11.4 million users.", "div": "natwest", "rev": "retail", "products": [
            P("apps", "NatWest, RBS & Ulster Bank apps", "11.4 million mobile users; 95% of retail customers and 85% of commercial customers are digital-first.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["NatWest Group: tech, data and AI", TECH]]),
        ]},
        {"id": "5.2", "ic": "building", "name": "Branches", "blurb": "336, open to 2029.", "div": "natwest", "rev": "retail", "products": [
            P("branches", "Branches", "336 branches, all kept open until at least 2029 with £50 million invested.",
              s=["con", "aff"], lc="everyday", neo=[0, ""], src=[["H1 2026 results web story", H1W]]),
        ]},
        {"id": "5.3", "ic": "briefcase-business", "name": "Mettle & FreeAgent", "blurb": "For sole traders.", "div": "mettle", "rev": "ci", "products": [
            P("mettle", "Mettle & FreeAgent", "A free business account for sole traders and small companies with a Mastercard card and FreeAgent accounting software included.",
              s=["sme"], lc="open", neo=[2, "Mastercard card."], src=[["Mettle", "https://www.mettle.co.uk/"]]),
        ]},
        {"id": "5.4", "ic": "headset", "name": "Relationship managers", "blurb": "About 1,000 for companies.", "div": "nwg", "rev": "ci", "products": [
            P("rms", "Relationship managers", "About 1,000 relationship managers for commercial customers, with Bankline and the Mid-Market Growth Council.",
              s=["corp"], lc="everyday", neo=[0, ""], src=[["H1 2026 results web story", H1W]]),
        ]},
        {"id": "5.5", "ic": "flag", "name": "Niche brands", "blurb": "Holt's, Drummonds, Isle of Man.", "div": "nwg", "rev": "grp", "products": [
            P("niche", "Holt's, Drummonds & Isle of Man Bank", "Banking for the armed forces, a London private bank, and the Isle of Man's own bank.",
              s=["aff", "con"], lc="everyday", o="I", neo=[0, ""], src=[["NatWest Group: our brands", NWG + "who-we-are/our-brands.html"]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at NatWest", "blurb": "Debit, credit and scam scoring.", "products": [
        P("mcatnw", "Mastercard at NatWest", "Mastercard carries the group's 16 million debit cards (from 2021) and most of its credit cards, scores its account-to-account payments for scams, powers Approval2Buy virtual cards and co-invested in Tyl's Pollinate; Visa has the Travel Reward card, reportedly the Nectar cards, and the first agentic transactions. Salim Secretary is the bank's head of scheme partnerships for both networks.",
          s=["fin"], div="nwg", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Retail Banker International: debit switch, Feb 2021", DEBIT], ["Mastercard: AI against scams, Apr 2024", CFR]]),
    ]},
    {"id": "pillar-market", "name": "UK payments", "blurb": "Scams, open banking, agents.", "products": [
        P("ukmarket", "The UK payments market", "Mandatory APP-scam reimbursement since October 2024 (88% of claimed losses repaid in the first year; the cap and the 50:50 split under review), the regulator being folded into the FCA, open-banking payments growing, and Visa first to live agentic transactions with UK banks.",
          s=["con"], div="nwg", rev="grp",
          src=[["PSR: one year of APP reimbursement, Oct 2025", "https://www.psr.org.uk/news-and-updates/latest-news/news/one-year-on-impact-of-app-reimbursement-on-victims/"]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
