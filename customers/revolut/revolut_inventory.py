"""Revolut's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Revolut is private: figures are from its 2025 annual report (24 March 2026), regulators and press.
``neo`` is the Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly
on Mastercard, 1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

AR25 = "https://www.fintechaustralia.org.au/community-news/revolut-reports-record-profit-of-usd23bn-for-2025-as-revenue-surges-to-usd6bn"
UKBANK = "https://itbrief.co.uk/story/revolut-wins-uk-bank-licence-plans-major-investment-push"
VAL = "https://tech.eu/2026/07/22/revolut-confirms-fresh-secondary-share-sale-at-reported-115bn-valuation/"
IPO = "https://thepaypers.com/fintech/news/revolut-ceo-targets-us-primary-listing-for-potential-ipo"
OCC = "https://theblock.co/news/regulation/2026-09-03-revolut-takes-important-step-toward-becoming-a-us-bank-with-conditional-occ-approval-413474"
MX = "https://www.retailbankerinternational.com/news/revolut-mexico-banking-licence/"
MAPPR = "https://www.mappr.co/revolut-countries-mapped/"
CTO = "https://thenextweb.com/news/revolut-cto-yatsenko-steps-down"
MC19 = "https://newsroom.mastercard.com/news/press/2019/october/revolut-to-launch-first-u-s-cards-with-mastercard-in-new-deal/"
VISA19 = "https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.16606.html"
VDIRECT = "https://www.financemagnates.com/fintech/revolut-and-visa-direct-sign-global-agreement/"
TERMINAL = "https://thepaypers.com/payments/news/revolut-launches-revolut-terminal-for-uk-businesses"
INDIA = "https://techcrunch.com/2025/10/07/revolut-aims-to-take-on-indian-banks-and-their-criminal-forex-fees"
EURR = "https://forkast.news/revolut-eurr-stablecoin-launch/"
LTFINE = "https://www.lrt.lt/en/news-in-english/19/2531818/revolut-bank-fined-eur3-5m-for-breaching-anti-money-laundering-rules"
ITFINE = "https://fintech.global/?p=237231"
WIKI = "https://en.wikipedia.org/wiki/Revolut"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "profit · licences · ownership", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: $6 billion of revenue and $2.3 billion of pre-tax profit in 2025, bank licences in more than 30 of 40 markets with the UK and Mexico new in 2026, a founder-led private company valued at a reported $115 billion, and a plan to reach 100 million customers by mid-2027.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & profit", "blurb": "68 million customers, $2.3bn profit.", "div": "grp", "rev": "grp", "products": [
            P("scale", "Scale", "68.3 million retail customers at the end of 2025 (+30%), 767,000 businesses, $1.7 trillion of transactions and $67.5 billion of customer balances; more than 80 million customers in 40 countries by September 2026 ⚠.",
              s=["con"], neo=[0, ""], src=[["Revolut 2025 annual report via Fintech Australia, Mar 2026", AR25], ["Wikipedia: Revolut", WIKI]]),
            P("earnings", "Earnings", "Revenue of $6.0 billion in 2025 (+46%) and profit before tax of $2.3 billion (38% margin), the fifth profitable year; card payments $1.3 billion, subscriptions $936 million, wealth $876 million, FX $800 million, interest $1.3 billion.",
              s=["con"], neo=[1, "Card revenue earned on Mastercard and Visa."], src=[["Revolut 2025 annual report via Fintech Australia, Mar 2026", AR25]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Licences", "blurb": "A bank in 30-plus markets.", "div": "grp", "rev": "grp", "products": [
            P("licences", "Bank licences", "Revolut Bank UAB (Lithuania, EEA-wide since 2021); the UK bank out of mobilisation in March 2026; Mexico (live January 2026); France (August 2026), Australia (July 2026 ⚠) and the UAE (June 2026); conditional OCC approval for a US bank (September 2026).",
              s=["con", "sme"], st="new", neo=[0, ""],
              src=[["IT Brief: UK bank licence, Mar 2026", UKBANK], ["Retail Banker International: Mexico licence, Oct 2025", MX], ["The Block: OCC conditional approval, Sep 2026", OCC]]),
            P("compliance", "Regulatory record", "A €3.5 million AML fine in Lithuania (April 2025), an €11.5 million Italian competition fine (April 2026, under appeal) and reported ECB curbs on new EU products ⚠.",
              s=["con"], neo=[0, ""], src=[["LRT: Revolut Bank fined, Apr 2025", LTFINE], ["FinTech Global, Apr 2026", ITFINE]]),
        ]},
        {"id": "1.3", "ic": "users-round", "name": "Ownership & leadership", "blurb": "Reported $115bn valuation.", "div": "grp", "rev": "grp", "products": [
            P("ownership", "Valuation & IPO", "Secondary sales at $75 billion (November 2025) and a reported $115 billion (July 2026); Nik Storonsky says a listing is at least two years away and prefers a US primary listing.",
              s=["aff"], neo=[0, ""], src=[["tech.eu: $115bn secondary, Jul 2026", VAL], ["The Paypers: US listing preferred, Oct 2026", IPO]]),
            P("leadership", "Leadership", "Co-founder and CEO Nik Storonsky; CFO Victor Stinga; Francesca Carlesi runs the UK bank; co-founder Vlad Yatsenko stepped down as CTO in July 2026, succeeded by Donato Lucia.",
              s=["aff"], neo=[0, ""], src=[["The Next Web: CTO steps down, Jun 2026", CTO], ["Revolut 2025 annual report via Fintech Australia", AR25]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Built in-house.", "div": "grp", "rev": "grp", "products": [
            P("tech", "Platform & Revolut Research", "One in-house stack across 40 markets, about 10,000 staff (3,500 in India), and an AI research division announced in August 2026 ⚠.",
              s=["con"], o="B", neo=[0, ""], src=[["TechCrunch: Revolut in India, Oct 2025", INDIA], ["Wikipedia: Revolut", WIKI]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy", "blurb": "100 million by mid-2027.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "100 million customers, 100 markets", "Targets of 100 million customers by mid-2027 and 30 new markets by 2030; £10 billion of investment over five years (£3 billion in the UK); the US and Western Europe as priorities; Banco Cetelem Argentina bought from BNP Paribas (approved September 2026 ⚠).",
              s=["con"], neo=[0, ""], src=[["IT Brief, Mar 2026", UKBANK], ["Revolut 2025 annual report via Fintech Australia", AR25]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: cards on both Mastercard and Visa, transfers and payouts on Visa Direct, FX in 36 currencies, Revolut Pay and its own acquiring, local rails from Wero to UPI, and crypto with a euro stablecoin.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Cards", "blurb": "Mastercard and Visa.", "div": "revolut", "rev": "retail", "products": [
            P("cards", "Debit cards in Europe & the UK", "Physical, virtual and disposable cards on both networks; under a 2019 deal Mastercard was to carry at least half of Revolut's existing and future European cards. The current split is not disclosed.", short="Debit cards (both networks)",
              s=["con", "travel"], lc="everyday", o="P", at="Mastercard, Visa", neo=[1, "Mastercard and Visa; split undisclosed."],
              mc="The 2019 agreement's term and renewal are not public.",
              src=[["Mastercard: Revolut deal, Oct 2019", MC19], ["Visa: Revolut global partnership, Sep 2019", VISA19]]),
            P("visamarkets", "Visa-led markets", "Since 2019 Visa has been the lead issuer for new markets: India's prepaid cards, Canada's prepaid card and the US credit card (issued by Cross River ⚠) are Visa.", short="Visa markets",
              s=["con"], lc="everyday", o="P", at="Visa", neo=[0, "Visa."],
              src=[["Visa: Revolut global partnership, Sep 2019", VISA19], ["TechCrunch: Revolut in India, Oct 2025", INDIA]]),
            P("premium", "Metal, Ultra & Titan", "Premium plan cards and Titan, an 'ultra-premium' corporate card with a 2025 waitlist; networks not disclosed.",
              s=["aff", "sme"], lc="everyday", st="new", neo=[None, "Network not disclosed."], src=[["Revolut 2025 annual report via Fintech Australia", AR25]]),
        ]},
        {"id": "2.2", "ic": "send", "name": "Transfers & payouts", "blurb": "Visa Direct.", "div": "revolut", "rev": "retail", "products": [
            P("payouts", "P2P & card payouts", "Push-to-card to about 90 countries on Visa Direct (2023) and a global Visa Direct agreement for Revolut Business card payouts (August 2024); Mastercard Send was promised in 2019 but nothing later is public.", short="Payouts (Visa Direct)",
              s=["con", "sme"], lc="move", o="P", at="Visa", neo=[0, "Visa Direct."],
              mc="Mastercard Move could contest Visa Direct's hold on payouts.",
              src=[["Finance Magnates: Revolut and Visa Direct, Aug 2024", VDIRECT], ["Mastercard: Revolut deal, Oct 2019", MC19]]),
        ]},
        {"id": "2.3", "ic": "arrow-left-right", "name": "FX & international", "blurb": "$800m of FX revenue.", "div": "revolut", "rev": "retail", "products": [
            P("fx", "Currency exchange & transfers", "Exchange and international transfers at interbank-style rates: $800 million of FX revenue in 2025 (+43%); India's launch is pitched against banks' forex fees.",
              s=["travel", "con"], lc="move", neo=[0, "Revolut's own FX."], src=[["Revolut 2025 annual report via Fintech Australia", AR25], ["TechCrunch: Revolut in India, Oct 2025", INDIA]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Revolut Pay & acquiring", "blurb": "Checkout and terminals.", "div": "business", "rev": "business", "products": [
            P("revpay", "Revolut Pay", "One-tap checkout from a Revolut balance, about 0.5% plus 2p for merchants and RevPoints for shoppers; Booking.com, Wizz Air and Harvey Norman among merchants.", short="Revolut Pay",
              s=["merch", "con"], lc="move", neo=[0, "Account-to-account, off the networks."],
              mc="Moves checkout volume off cards; Click to Pay is the network answer.",
              src=[["Wikipedia: Revolut", WIKI]]),
            P("acquiring", "Terminal, Reader & Gateway", "Card acceptance for businesses: Revolut Terminal (UK October 2024, then Ireland, Italy and Portugal), Reader, POS software, Gateway, Payment Links and Tap to Pay on iPhone; Amex accepted since 2024.",
              s=["merch", "sme"], lc="move", ay="Oct 2024", neo=[1, "Accepts every network."], src=[["The Paypers: Revolut Terminal, Oct 2024", TERMINAL]]),
        ]},
        {"id": "2.5", "ic": "zap", "name": "Local rails", "blurb": "Wero, UPI.", "div": "revolut", "rev": "retail", "products": [
            P("local", "Wero & UPI", "A member of the European Payments Initiative (Wero) from 2025 ⚠ and UPI handles in India's beta.",
              s=["con"], lc="move", st="new", neo=[0, "Account-to-account."], src=[["Wikipedia: Revolut", WIKI], ["TechCrunch: Revolut in India, Oct 2025", INDIA]]),
        ]},
        {"id": "2.6", "ic": "coins", "name": "Crypto & stablecoins", "blurb": "EURR, 16 million crypto users.", "div": "eu", "rev": "wealth", "products": [
            P("crypto", "Crypto & Revolut X", "Crypto trading and staking for 16 million users, and the Revolut X exchange ⚠.",
              s=["crypto"], lc="grow", neo=[0, ""], src=[["Forkast: EURR, Aug 2026", EURR]]),
            P("eurr", "EURR stablecoin", "A MiCA euro stablecoin issued by Bridge (Stripe), launched 26 August 2026 in Denmark, Poland and Portugal; a sterling coin is in the FCA sandbox ⚠.",
              s=["crypto", "con"], lc="move", st="new", ay="Aug 2026", o="P", at="Bridge (Stripe)", neo=[0, "No network involved."],
              mc="Stablecoin-linked cards and settlement are open ground.",
              src=[["Forkast: EURR, Aug 2026", EURR]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: AI fraud screening and Street Mode, the AIR assistant about to shop on its own, RevPoints and subscription plans, and insurance and mobile extras.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "10x fraud review.", "div": "revolut", "rev": "retail", "products": [
            P("protection", "Customer Protection Platform", "AI models that raised fraud-case review tenfold, Street Mode for transfers in public, verified in-app calls against impersonation, and Travel Mode (2025).",
              s=["con"], lc="everyday", neo=[0, "Revolut's own."],
              mc="A newly regulated UK bank with fraud-complaint exposure: Consumer Fraud Risk fits.",
              src=[["Revolut 2025 annual report via Fintech Australia", AR25]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI & agents", "blurb": "AIR, shopping from December.", "div": "revolut", "rev": "retail", "products": [
            P("air", "AIR (AI by Revolut)", "An in-app money assistant gaining autonomous shopping, with tests planned for December 2026 and the UK likely first; Revolut also helped develop Google's AP2 ⚠.",
              s=["con"], lc="move", st="new", ay="Dec 2026", neo=[0, "No network named yet."],
              mc="Agentic tokens and Agent Pay for AIR's shopping pilot.",
              src=[["The Paypers, Oct 2026", IPO]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Plans & RevPoints", "blurb": "17 million on RevPoints.", "div": "revolut", "rev": "retail", "products": [
            P("revpoints", "RevPoints & subscription plans", "RevPoints for 17 million users in 36 markets, earned on card spend and Revolut Pay; Plus, Premium, Metal and Ultra plans brought $936 million in 2025.",
              s=["con", "aff"], lc="grow", neo=[1, "Earned on network cards."], src=[["Revolut 2025 annual report via Fintech Australia", AR25]]),
        ]},
        {"id": "3.4", "ic": "smartphone", "name": "Extras", "blurb": "Mobile, insurance.", "div": "revolut", "rev": "retail", "products": [
            P("extras", "Revolut Mobile & insurance", "A mobile network in the UK and Poland (2025) and travel and device insurance ⚠.",
              s=["con", "travel"], lc="beyond", st="new", neo=[0, ""], src=[["Revolut 2025 annual report via Fintech Australia", AR25]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What 80 million customers buy: accounts that are now bank accounts in the UK, EEA and Mexico; Revolut Business for 767,000 firms; trading, ISAs and crypto; and credit from loans to mortgages.",
    "tiles": [
        {"id": "4.1", "ic": "wallet", "name": "Accounts", "blurb": "$67.5bn of balances.", "div": "uk", "rev": "retail", "products": [
            P("accounts", "Current accounts & savings", "Bank accounts in the UK (FSCS), the EEA (local IBANs) and Mexico, US accounts through partner banks, and savings that earned $1.3 billion of interest income in 2025.",
              s=["con"], lc="everyday", neo=[1, "Cards on both networks."], src=[["IT Brief, Mar 2026", UKBANK], ["mappr: Revolut countries, Jul 2026", MAPPR]]),
            P("kids", "Revolut <18", "Accounts for 6–17-year-olds with parental controls ⚠.",
              s=["young"], lc="open", neo=[None, "Network not verified."], src=[["Wikipedia: Revolut", WIKI]]),
        ]},
        {"id": "4.2", "ic": "briefcase", "name": "Revolut Business", "blurb": "767,000 businesses.", "div": "business", "rev": "business", "products": [
            P("business", "Business accounts & cards", "Accounts, cards, expenses and payouts for 767,000 businesses moving $365 billion in 2025, 16% of income.",
              s=["sme"], lc="everyday", neo=[None, "Network not disclosed."], src=[["Revolut 2025 annual report via Fintech Australia", AR25]]),
        ]},
        {"id": "4.3", "ic": "chart-candlestick", "name": "Wealth", "blurb": "$876m of revenue.", "div": "eu", "rev": "wealth", "products": [
            P("trading", "Stocks, ETFs, CFDs & ISA", "Commission-free ETF plans in the EEA and Switzerland, CFDs in 29 countries and a UK Stocks and Shares ISA (2025); wealth revenue of $876 million.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["Revolut 2025 annual report via Fintech Australia", AR25]]),
        ]},
        {"id": "4.4", "ic": "hand-coins", "name": "Credit", "blurb": "$2.9bn of loans.", "div": "eu", "rev": "credit", "products": [
            P("credit", "Loans, credit cards & mortgages", "Customer lending of $2.9 billion (+120%): personal loans, credit cards in the EEA and US (Visa ⚠), and mortgages in Lithuania and France; US credit cards to follow the bank charter.",
              s=["con", "aff"], lc="borrow", st="new", neo=[None, "Mixed and undisclosed."],
              mc="US credit cards from 2027 put a network choice in play.",
              src=[["Revolut 2025 annual report via Fintech Australia", AR25], ["The Paypers, Oct 2026", IPO]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Revolut: one app localised for 40 markets, a referral engine that brings in most new customers, merchant checkouts, and sponsorships from Manchester City to Formula 1.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "The app", "blurb": "40 markets.", "div": "revolut", "rev": "retail", "products": [
            P("app", "Revolut app", "One app localised by market, with India in controlled beta from June 2026 and the US, Mexico and Australia growing.",
              s=["con", "travel"], lc="open", neo=[0, ""], src=[["mappr: Revolut countries, Jul 2026", MAPPR]]),
        ]},
        {"id": "5.2", "ic": "users-round", "name": "Referrals & partners", "blurb": "63% by word of mouth.", "div": "revolut", "rev": "retail", "products": [
            P("growth", "Referrals, merchants & sponsorships", "More than 63% of new customers join by referral or word of mouth; merchant checkouts carry Revolut Pay; sponsorships include Manchester City and Audi's Formula 1 team ⚠.",
              s=["con", "merch"], lc="open", neo=[0, ""], src=[["Revolut 2025 annual report via Fintech Australia", AR25], ["Wikipedia: Revolut", WIKI]]),
        ]},
        {"id": "5.3", "ic": "earth", "name": "New markets", "blurb": "India, UAE, Argentina, US.", "div": "us", "rev": "grp", "products": [
            P("markets", "New markets", "India (PPI licence, beta), the UAE (licensed June 2026), Argentina (Cetelem), Peru (applied), and a US bank to open in 2027.",
              s=["con"], lc="open", st="new", neo=[None, "Network choices open."],
              mc="New-market issuing where the network is still to be chosen.",
              src=[["mappr: Revolut countries, Jul 2026", MAPPR], ["The Block, Sep 2026", OCC]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Revolut", "blurb": "Launch partner, half of Europe.", "products": [
        P("mcatrevolut", "Mastercard at Revolut", "Mastercard was Revolut's launch partner in 2015, and a 2019 deal (signed by Michael Miebach) gave it at least half of Revolut's European cards, the first US cards and Mastercard Send first. Visa became lead issuer for new markets the same year and carries Revolut's payouts on Visa Direct. Nothing joint with Mastercard has been announced since 2019.",
          s=["con"], div="grp", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Mastercard: Revolut deal, Oct 2019", MC19], ["Visa: Revolut global partnership, Sep 2019", VISA19]]),
    ]},
    {"id": "pillar-market", "name": "Neobanks", "blurb": "Licences, scams, agents.", "products": [
        P("market", "The neobank market", "Revolut, Monzo, Wise, N26 and Nubank turning into licensed banks; UK APP-scam reimbursement; the OCC chartering fintechs; stablecoins under MiCA.",
          s=["con"], div="grp", rev="grp", src=[["The Block, Sep 2026", OCC]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
