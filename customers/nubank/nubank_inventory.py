"""Nu Holdings' layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are Nu's own unless a source says otherwise: the Q2 2026 results (13 August 2026), the FY2025 results
and 20-F, Nu's newsroom and its NuHeadlines newsletters. ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

NEWS = "https://nu.com/en/newsroom/company/"
NH = "https://cdn.nubank.com.br/newsletter/nuheadlines-editions/"
Q226 = NEWS + "nu-holdings-ltd-reports-second-quarter-2026-financial-results"
Q126 = NEWS + "nu-holdings-ltd-reports-first-quarter-2026-financial-results"
FY25 = NEWS + "nu-holdings-ltd-reports-fourth-quarter-and-full-year-2025-financial-results"
F20 = "https://www.sec.gov/Archives/edgar/data/1691493/000129281426002166/nuform20f_2025.htm"
US = NEWS + "nu-united-states-nu-global"
OCC = NEWS + "nu-secures-approval-to-establish-us-national-bank"
MXBANK = NEWS + "nu-mexico-receives-authorization-to-begin-operations-as-a-bank"
MXINV = NEWS + "nu-mexicos-total-investments-expected-to-reach-us4-2-billion-by-2030-as-banking-launch-approaches"
BRLIC = NEWS + "nubank-strengthens-its-brazil-operation-with-a-new-banking-license"
LATAMCEO = NEWS + "nubank-names-livia-chanes-ceo-for-latin-america"
CFO = NEWS + "nubank-appoints-rob-livingston-as-chief-financial-officer"
CFOVC = NEWS + "new-cfo-signals-disciplined-ambition-for-nubanks-next-phase-of-growth"
CROMA = NEWS + "nubank-announces-nubank-croma-featuring-a-platinum-card-0-8-cashback-on-all-purchases-5-on-streaming-subscriptions-a-caixinha-turbo-yielding-120-and-a-special-nucel-plan"
TAP = "https://nu.com/en/newsroom/consumers/nubank-evolves-contactless-payments-and-integrates-pix-debit-and-credit-in-a-single-tap-on-the-phone"
CRYPTO = NEWS + "nubank-launches-cryptocurrency-rewards-feature"
NUCEL = "https://nu.com/en/newsroom/consumers/nucel-reaches-1-million-customers-and-consolidates-nubank-as-a-platform-beyond-finance"
PPRO = "https://www.ppro.com/news/ppro-partners-with-nubank-to-enable-nupay-unlocking-access-to-brazils-digital-banking-ecosystem/"
NH43 = NH + "43/nuheadlines-43-en.html"
NH44 = NH + "44/nuheadlines-44-en.html"
NH45 = NH + "45/nuheadlines-45-en.html"
NH46 = NH + "46/nuheadlines-46-en.html"
NH47 = NH + "47/nuheadlines-47-en.html"
NH48 = NH + "48/nuheadlines-48-en.html"
NH49 = NH + "49/nuheadlines-49-en.html"
NH51 = NH + "51/nuheadlines-51-en.html"
UV = "https://nubank.com.br/ultravioleta/"
PIX = "https://nubank.com.br/pix/"
USSITE = "https://nu.com/us/"
RATINGS = "https://nu.com/en/investors/ratings/"
MCAP = "https://stockanalysis.com/stocks/nu/market-cap/"
WIKI = "https://en.wikipedia.org/wiki/Nubank"
NUCO = "https://nu.com.co/cuenta/"
MXDEBIT = "https://dplnews.com/?p=191826"
OF = "https://finsidersbrasil.com.br/economia-open/brasil-lidera-open-finance-no-mundo-com-100-milhoes-de-clientes/"
FEED = "https://neofeed.com.br/blog/home/de-inimigas-as-fintechs-viraram-as-grandes-parceiras-da-mastercard/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "scale · licences · AI", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: 139 million customers and a first billion-dollar quarter, banking licences arriving in Mexico, Brazil and the US, a founder-led company worth about $70 billion that started with a Mastercard card in 2014, and its own AI models.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Scale & returns", "blurb": "139m customers, ROE 33%.", "div": "nu", "rev": "grp", "products": [
            P("scale", "Customers & earnings", "139 million customers at 30 June 2026 (about 118 million in Brazil, 15.8 million in Mexico, more than 5 million in Colombia); Q2 2026 revenue about $5.9 billion and net income of $1.06 billion, the first quarter above $1 billion, at a 33% ROE; FY2025 revenue $16.3 billion and net income $2.9 billion.",
              s=["con"], neo=[0, ""], src=[["Nu: Q2 2026 results", Q226], ["Nu: FY2025 results", FY25]]),
            P("balance", "Credit book & deposits", "A $39.4 billion credit portfolio (+37%), of which cards $26.0 billion, unsecured $10.3 billion and secured $3.1 billion; deposits of $45.3 billion; 90-day NPLs of 6.9%; gross profit 41% from credit, 25% fees and 34% float (Q2 2026).",
              s=["con", "saver"], neo=[0, ""], src=[["Nu: Q2 2026 results", Q226]]),
        ]},
        {"id": "1.2", "ic": "badge-check", "name": "Licences", "blurb": "Banks in Mexico, Brazil, US.", "div": "nu", "rev": "grp", "products": [
            P("licences", "Licences by country", "Nu Mexico has operated as a bank since 6 August 2026; in Brazil Nu is buying Banco Porto Real for a full banking licence (July 2026, pending central-bank approval); Colombia has a financing-company licence (2024); in the US the OCC conditionally approved Nubank, N.A. (January 2026), with Lead Bank as partner meanwhile. An Argentina Mastercard licence of 2019 has gone from the 2025 20-F ⚠ exit date unknown.",
              s=["con"], st="flux", neo=[0, ""], src=[["Nu: Brazil banking licence, Jul 2026", BRLIC], ["Nu: Mexico bank authorisation, Jul 2026", MXBANK], ["Nu: OCC approval, Jan 2026", OCC], ["Nu 20-F 2025", F20]]),
        ]},
        {"id": "1.3", "ic": "users-round", "name": "Leadership & market", "blurb": "Vélez; a CFO from Visa.", "div": "nu", "rev": "grp", "products": [
            P("leadership", "Leadership, ratings & market value", "Founder and CEO David Vélez; Cristina Junqueira runs Nu US and Livia Chanes Latin America (July 2026); CFO Rob Livingston since 13 July 2026, after more than 12 years at Visa ending as CFO North America. NYSE: NU, worth $70.3 billion at $14.56 (16 October 2026); S&P BB- and Moody's Ba2 at holding level.",
              s=["con"], st="new", neo=[0, ""],
              mc="A CFO from Visa is a relationship to watch, though nothing points to a network review.",
              src=[["Nu: CFO appointment, Jun 2026", CFO], ["Nu: Latin America CEO, Jul 2026", LATAMCEO], ["Stockanalysis: NU market cap", MCAP], ["Nu: ratings", RATINGS]]),
        ]},
        {"id": "1.4", "ic": "rocket", "name": "Heritage", "blurb": "A Mastercard card in 2014.", "div": "br", "rev": "grp", "products": [
            P("heritage", "Founding & deals", "Founded in São Paulo in May 2013 by David Vélez, Cristina Junqueira and Edward Wible; Mastercard was the only network willing to work with the start-up and the first card shipped in about six months (first transaction 1 April 2014). IPO December 2021; Easynvest (2021), Hyperplane (2024) and a stake in Tyme (2024).",
              s=["con"], o="B", neo=[2, "Built on a Mastercard card from day one."],
              src=[["NeoFeed: fintechs and Mastercard, Jun 2019", FEED], ["Nu 20-F 2025", F20], ["Wikipedia: Nubank", WIKI]]),
        ]},
        {"id": "1.5", "ic": "brain", "name": "Technology & AI", "blurb": "nuFormer, AI agents.", "div": "nu", "rev": "grp", "products": [
            P("nuformer", "nuFormer models", "Nu's own foundation models make credit decisions for cards in Brazil and Mexico and for unsecured loans in Brazil, with SME and Colombian cards in testing; model development has fallen from about three months to about seven days.",
              s=["con"], o="B", neo=[0, ""], src=[["Nu: Q2 2026 results", Q226], ["Nu: CFO interview, Aug 2026", CFOVC]]),
            P("aiagents", "AI Private Banker & AI agents", "An AI Private Banker with more than 15 million monthly users (Q1 2026), AI agents in more than 60% of Brazilian support chats, Pix by chat with more than 10 million users, and a partnership with OpenAI.",
              s=["con"], st="new", neo=[0, ""],
              mc="Agent Pay is not yet in Nu's assistants, though nearly all Latin American issuers use Mastercard tokens.",
              src=[["Nu: Q1 2026 results", Q126], ["Nu: Q2 2026 results", Q226], ["NuHeadlines 44, Feb 2026", NH44]]),
        ]},
        {"id": "1.6", "ic": "target", "name": "Strategy", "blurb": "Brazil first, then the US.", "div": "nu", "rev": "grp", "products": [
            P("strategy", "Strategy & brand", "Brazil stays the main focus, with R$45 billion invested there in 2026 and a push into mid- and high-income customers; US spending capped at 100 basis points of the efficiency ratio in 2026 and 2027; a $1 billion buyback (June 2026); first Investor Day on 8 December 2026. Sponsorships: Inter Miami's Nu Stadium, Mercedes-AMG F1 and Palmeiras' Nubank Parque.",
              s=["con", "affl"], neo=[0, ""],
              mc="Nu's sports deals suit Priceless experiences.",
              src=[["NuHeadlines 46, Apr 2026", NH46], ["Nu: Q1 2026 results", Q126], ["NuHeadlines 45, Mar 2026", NH45]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Six ways money moves: credit cards worth $26 billion, all Mastercard where the network is named, Black and Platinum premium cards, Mastercard debit in three countries, Pix and its credit in up to 12 instalments, one tap and NuPay at the checkout, and Nu Global's stablecoin account and crypto.",
    "tiles": [
        {"id": "2.1", "ic": "credit-card", "name": "Credit cards", "blurb": "$26bn, Mastercard.", "div": "br", "rev": "credit", "products": [
            P("ccbr", "Nu credit card, Brazil", "The no-fee, app-first card that started Nu in 2014 and is still its biggest asset: $26.0 billion of the $39.4 billion credit book (Q2 2026), with credit decided by nuFormer.", short="Credit card (Mastercard)",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="The core of the relationship: Nu's largest asset rides on Mastercard.",
              src=[["Nu 20-F 2025", F20], ["Nu: Q2 2026 results", Q226]]),
            P("othercards", "Nubank+, under-18 & SME cards", "A mid-tier subscription card (2024), an under-18 credit card (2025) and the Nu Empresas card (2021) ⚠ network not stated.",
              s=["con", "sme"], lc="borrow", neo=[None, "Network not stated ⚠."], src=[["Nu 20-F 2025", F20], ["Nu: FY2025 results", FY25]]),
            P("ccmx", "Nu credit card, Mexico", "Launched 2020 on Mastercard; Nu Mexico is the third-largest card issuer there and 54% of its customers got their first credit card from Nu, with interest-free instalments and secured cards.",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Nu: Mexico bank authorisation, Jul 2026", MXBANK], ["Nu: Mexico investment, Feb 2026", MXINV]]),
            P("ccco", "Nu credit card, Colombia", "Mastercard Gold and Black cards under a licence dated April 2020, with about 1.2 million card clients and a subscription card from 2025.",
              s=["con"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard ⚠ from the 20-F and exhibit list."], src=[["Nu 20-F 2025", F20]]),
        ]},
        {"id": "2.2", "ic": "gem", "name": "Premium cards", "blurb": "Black and Platinum.", "div": "br", "rev": "credit", "products": [
            P("ultravioleta", "Nubank Ultravioleta", "A Mastercard Black metal card (2021) at R$89 a month, waived above R$8,000 of monthly spend: 1.25% cashback or points, no IOF on foreign spend, a LATAM Pass mode (March 2026), a lounge at Guarulhos and Priority Pass visits.", short="Ultravioleta (Mastercard Black)",
              s=["affl"], lc="borrow", o="P", at="Mastercard", neo=[2, "Mastercard Black."], src=[["Nubank: Ultravioleta", UV], ["Nu 20-F 2025", F20]]),
            P("croma", "Nubank Croma", "A Mastercard Platinum card launched 28 July 2026 for the tier between mass market and high income: R$39 a month, 0.8% cashback or points transferable to LATAM Pass, Azul and Smiles, and 5% back on 28 subscriptions.", short="Croma (Mastercard Platinum)",
              s=["affl"], lc="borrow", st="new", ay="Jul 2026", o="P", at="Mastercard", neo=[2, "Mastercard Platinum."],
              mc="Nu is moving up-market on Mastercard tiers; World and World Elite benefits could follow in Brazil.",
              src=[["Nu: Croma launch, Jul 2026", CROMA]]),
        ]},
        {"id": "2.3", "ic": "wallet-cards", "name": "Debit", "blurb": "Mastercard in three countries.", "div": "br", "rev": "fees", "products": [
            P("debitbr", "Debit card, Brazil", "A Mastercard-branded international debit and prepaid card since 2018.",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "Mastercard."], src=[["Nu 20-F 2025", F20]]),
            P("debitmx", "Cuenta Nu debit card, Mexico", "Launched 4 May 2023 'in association with Mastercard'; Nu Mexico has 16 million customers, about 22% of whom used only cash before Nu.",
              s=["con"], lc="everyday", ay="May 2023", o="P", at="Mastercard", neo=[2, "Mastercard."],
              mc="Moving Mexican spend from cash to card is the growth case.",
              src=[["DPL News: Nu Mexico debit, May 2023", MXDEBIT], ["Nu: Mexico investment, Feb 2026", MXINV]]),
            P("debitco", "Account card, Colombia", "One free cash withdrawal a month 'on the Mastercard network' ⚠ the page does not say the card is Mastercard-branded.",
              s=["con"], lc="everyday", neo=[1, "Mastercard ATM network; brand not stated ⚠."], src=[["Nu Colombia: account", NUCO]]),
        ]},
        {"id": "2.4", "ic": "zap", "name": "Pix & instant", "blurb": "Pix, SPEI, Bre-B.", "div": "br", "rev": "float", "products": [
            P("pix", "Pix", "Free Pix transfers with scheduling, Pix by chat or voice, trusted lists and night limits; Nu originates about 20% of Pix transfers ⚠ search summary, out of 179.7 million Pix users in 2025.",
              s=["con", "sme"], lc="move", neo=[0, "Pix, the central bank's rail."], src=[["Nubank: Pix", PIX], ["Nu 20-F 2025", F20]]),
            P("pixcredit", "Pix financing", "Pay a Pix from the credit-card limit in up to 12 instalments, the payee paid instantly (2022), and boletos financed on the card limit.",
              s=["con"], lc="borrow", neo=[0, "Runs on Pix, off the card rails."],
              mc="Every Pix-financed purchase is card credit that earns no interchange.",
              src=[["Nubank: Pix", PIX], ["Nu 20-F 2025", F20]]),
            P("instantlatam", "SPEI & Bre-B", "SPEI transfers in Mexico (those under $5 grew more than 60% in H1 2026) and Bre-B in Colombia, where about 75% of Nu customers have registered keys.",
              s=["con"], lc="move", neo=[0, ""], src=[["Nu: Q2 2026 results", Q226], ["NuHeadlines 44, Feb 2026", NH44]]),
        ]},
        {"id": "2.5", "ic": "wallet", "name": "Tap & NuPay", "blurb": "One tap, one click.", "div": "br", "rev": "fees", "products": [
            P("paybytap", "Pay by Tap", "One NFC tap pays by Pix (one-off or up to 12 instalments), debit or credit, by creating and tokenising a virtual card (April 2026, Android only) ⚠ no network or token service named.",
              s=["con"], lc="move", st="new", ay="Apr 2026", neo=[None, "Token service not named ⚠."],
              mc="Making Mastercard tokens the default under Pay by Tap would keep the tap on the card.",
              src=[["Nu: Pay by Tap, Apr 2026", TAP]]),
            P("nupay", "NuPay", "A checkout button for Nubank customers only, with one-click or biometric approval and no card details shared (2022), reached through EBANX, Uber and PPRO (May 2026, 115 million customers); NuPay for Business came from Spin Pay ⚠.",
              s=["con", "merch"], lc="move", neo=[0, "Account-based; does what Click to Pay does."],
              src=[["PPRO: NuPay, May 2026", PPRO], ["Nu 20-F 2025", F20]]),
        ]},
        {"id": "2.6", "ic": "globe", "name": "Cross-border & crypto", "blurb": "Nu Global, stablecoins.", "div": "us", "rev": "fees", "products": [
            P("nuglobal", "Nu Global", "A cross-border account launched 10 September 2026 with balances held as USDC (3.50%) or EURC (2.20%), spent through a virtual Mastercard, with transfers to 35+ countries and bitcoin and ether.",
              s=["xb"], lc="move", st="new", ay="Sep 2026", o="P", at="Mastercard", neo=[1, "Virtual Mastercard over stablecoin balances."],
              mc="Stablecoin-linked card settlement and Move for payouts outside the stablecoin corridors.",
              src=[["Nu: US and Nu Global, Sep 2026", US]]),
            P("contaglobal", "Conta Global", "A multi-currency account in Brazil (2024), with zero spread for Ultravioleta members.",
              s=["xb", "affl"], lc="move", neo=[None, ""], src=[["Nu 20-F 2025", F20], ["Nubank: Ultravioleta", UV]]),
            P("remit", "US-to-LatAm transfers", "Free transfers from the US to Pix, CLABE and Bre-B keys.",
              s=["xb"], lc="move", st="new", neo=[0, "Pix, SPEI and Bre-B."], src=[["Nu US", USSITE]]),
            P("crypto", "Nubank Crypto", "Buying, selling and custody through Fireblocks for more than 7 million clients, USDC rewards (2025) and Solana staking (March 2026).",
              s=["saver"], lc="grow", o="P", at="Fireblocks", neo=[0, ""], src=[["Nu: crypto rewards, Mar 2026", CRYPTO], ["Nu 20-F 2025", F20]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: Street Mode and scam alerts, Brazil's leading open-finance payment initiator, digital onboarding and credit scores, and points, cashback and Vantagens Nu offers.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Street Mode, 5m users.", "div": "nu", "rev": "grp", "products": [
            P("security", "Street Mode & scam alerts", "Modo Rua (Street Mode) with more than 5 million users, Pix limits and trusted lists, a Scam Alert in Mexico, and a new CISO (2026); Vélez says criminals will use AI, so Nu must too.",
              s=["con"], lc="everyday", neo=[0, "Nu's own."],
              mc="Account-to-account scam scoring for Pix, SPEI and Bre-B is an open slot.",
              src=[["NuHeadlines 44, Feb 2026", NH44], ["NuHeadlines 51, Sep 2026", NH51], ["Nu: Mexico bank authorisation, Jul 2026", MXBANK]]),
        ]},
        {"id": "3.2", "ic": "plug", "name": "Open finance", "blurb": "Top Pix initiator.", "div": "br", "rev": "fees", "products": [
            P("openfinance", "Open-finance payment initiation", "Brazil's number one payment initiator over 2025, ahead of Google Pay, in a market of 64.5 million initiated payments and more than 100 million open-finance users ⚠ ranking varies by quarter; open finance is coming in Colombia and Mexico.",
              s=["con"], lc="move", neo=[0, ""], src=[["Finsiders: open finance, Feb 2026", OF], ["NuHeadlines 46, Apr 2026", NH46]]),
        ]},
        {"id": "3.3", "ic": "fingerprint", "name": "Onboarding & credit health", "blurb": "Digital KYC, NuScore.", "div": "nu", "rev": "grp", "products": [
            P("kyc", "Digital onboarding", "Fully digital identity checks in every market ⚠ no vendor or product disclosed.",
              s=["con"], lc="open", neo=[None, "Vendor not disclosed."], src=[["Nu 20-F 2025", F20]]),
            P("nuscore", "NuScore & CPF monitoring", "Credit scores and CPF monitoring built with Acordo Certo.",
              s=["con"], lc="open", o="P", at="Acordo Certo", neo=[0, ""], src=[["NuHeadlines 48, Jun 2026", NH48]]),
        ]},
        {"id": "3.4", "ic": "gift", "name": "Rewards & offers", "blurb": "Points, Vantagens Nu.", "div": "br", "rev": "fees", "products": [
            P("points", "Points & cashback", "Cashback and points on Ultravioleta and Croma, transferable to LATAM, Azul, Gol and Smiles, and experiences such as the Ultravioleta lounge and IRONMAN sponsorship.",
              s=["affl"], lc="grow", neo=[1, "Earned on Mastercard cards; Nu's own scheme."],
              mc="Priceless experiences and travel benefits fit the premium push.",
              src=[["Nubank: Ultravioleta", UV], ["Nu: Croma launch, Jul 2026", CROMA], ["NuHeadlines 43, Jan 2026", NH43]]),
            P("vantagens", "Vantagens Nu", "An offers programme launched in April 2026 with Shopee.",
              s=["con"], lc="grow", st="new", ay="Apr 2026", o="P", at="Shopee", neo=[0, ""], src=[["NuHeadlines 46, Apr 2026", NH46]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy beyond cards: loans priced in under a second, $45 billion of deposits and investments, Nu Empresas for 6 million small businesses, a mobile network and insurance, and a new US bank.",
    "tiles": [
        {"id": "4.1", "ic": "hand-coins", "name": "Lending", "blurb": "Priced in under a second.", "div": "br", "rev": "credit", "products": [
            P("loans", "Personal & payroll loans", "Personal loans (2019), payroll-deducted, FGTS-backed and public-sector loans, each priced and approved by AI in under a second, and the Novo Desenrola renegotiation programme.",
              s=["con"], lc="borrow", neo=[0, ""], src=[["Nu 20-F 2025", F20], ["Nu: Q1 2026 results", Q126], ["NuHeadlines 47, May 2026", NH47]]),
        ]},
        {"id": "4.2", "ic": "coins", "name": "Deposits & investments", "blurb": "$45bn of deposits.", "div": "invest", "rev": "float", "products": [
            P("nuconta", "NuConta & Caixinhas", "NuConta (2017) and Caixinhas savings pots, Caixinha Turbo paying 120% of CDI with NuCel or Croma, Cuenta Nu and Cajitas in Mexico, and Cajitas and CDTs in Colombia: $45.3 billion of deposits at 88% of the interbank rate.",
              s=["saver", "con"], lc="grow", neo=[0, ""], src=[["Nu: Q2 2026 results", Q226], ["Nu: Croma launch, Jul 2026", CROMA]]),
            P("investments", "Nu Investimentos & Nu Asset", "Investments from the Easynvest purchase, CDBs paying up to 130% of CDI and the NLFA11 private-credit ETF (January 2026).",
              s=["saver"], lc="grow", o="A", neo=[0, ""], src=[["NuHeadlines 43, Jan 2026", NH43], ["Nu 20-F 2025", F20]]),
        ]},
        {"id": "4.3", "ic": "briefcase", "name": "Nu Empresas", "blurb": "6m small businesses.", "div": "empresas", "rev": "credit", "products": [
            P("empresas", "Nu Empresas", "Six million business customers, more than a fifth of Brazil's active companies, with working capital, receivables anticipation and BNDES-backed loans.",
              s=["sme"], lc="borrow", neo=[None, "Card network not stated ⚠."], src=[["NuHeadlines 47, May 2026", NH47], ["NuHeadlines 49, Jul 2026", NH49]]),
            P("smeaccept", "Tap to Pay & Payment Link", "Card acceptance for small merchants on a phone or by link ⚠ processor and network not disclosed.",
              s=["sme", "merch"], lc="move", neo=[None, "Processor not disclosed."],
              mc="Tap on Phone and small-business cards could serve 6 million firms.",
              src=[["NuHeadlines 43, Jan 2026", NH43]]),
        ]},
        {"id": "4.4", "ic": "sparkles", "name": "Beyond banking", "blurb": "NuCel, insurance, travel.", "div": "br", "rev": "fees", "products": [
            P("nucel", "NuCel", "A mobile network on Claro (January 2025) with 1 million customers by June 2026, Brazil's largest MVNO.",
              s=["con"], lc="beyond", o="P", at="Claro", neo=[0, ""], src=[["Nu: NuCel 1 million, Jun 2026", NUCEL]]),
            P("beyond", "Insurance, NuTravel & NuTag", "Life insurance with Chubb (2020), NuTravel bookings paid through NuPay (2024) and the NuTag toll tag.",
              s=["con"], lc="beyond", o="P", at="Chubb", neo=[0, ""], src=[["Nu 20-F 2025", F20], ["Nu: Croma launch, Jul 2026", CROMA]]),
        ]},
        {"id": "4.5", "ic": "flag", "name": "Nu US", "blurb": "World Elite, exclusive.", "div": "us", "rev": "credit", "products": [
            P("uscard", "Nu Credit Card, US", "A Mastercard World Elite card from an 'exclusive relationship with Mastercard', launched 10 September 2026 and issued by Lead Bank: no annual fee, 1.5% cashback rising to 2%.", short="US card (World Elite)",
              s=["con", "xb"], lc="borrow", st="new", ay="Sep 2026", o="P", at="Mastercard, Lead Bank", neo=[2, "Mastercard World Elite, exclusive."],
              mc="The most significant recent joint step.",
              src=[["Nu: US and Nu Global, Sep 2026", US]]),
            P("usaccount", "Nu Account & metal debit card", "A US account with a metal debit card (September 2026) ⚠ network not stated.",
              s=["con", "xb"], lc="everyday", st="new", neo=[None, "Network not stated ⚠."], src=[["Nu US", USSITE]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach Nu: one app in four countries, cash points in Mexico and Colombian shops, and partners from Lead Bank to Claro.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Nu app", "blurb": "83.5% active monthly.", "div": "nu", "rev": "grp", "products": [
            P("app", "Nu app", "The Nu app in Brazil, Mexico, Colombia and the US, with 83.5% of customers active monthly (above 86% in Brazil).",
              s=["con", "affl", "saver"], lc="everyday", neo=[0, ""], src=[["Nu: Q2 2026 results", Q226]]),
        ]},
        {"id": "5.2", "ic": "store", "name": "Cash points", "blurb": "30,000 in Mexico.", "div": "mx", "rev": "float", "products": [
            P("cashpoints", "Cash-in & cash-out", "More than 30,000 cash points in Mexico and cash withdrawals by QR code at 2,800 D1 stores in Colombia.",
              s=["con"], lc="open", neo=[0, ""], src=[["Nu: Mexico bank authorisation, Jul 2026", MXBANK], ["NuHeadlines 51, Sep 2026", NH51]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Partners", "blurb": "Lead Bank, PPRO, Claro.", "div": "nu", "rev": "grp", "products": [
            P("partners", "Partners", "Mastercard for cards, Lead Bank in the US, PPRO, EBANX and Uber for NuPay, Claro, Chubb, Fireblocks, Shopee and OpenAI.",
              s=["con", "merch"], lc="open", neo=[1, "Mastercard is the card partner."], src=[["Nu: US and Nu Global, Sep 2026", US], ["PPRO: NuPay, May 2026", PPRO]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Nubank", "blurb": "Every card, while Pix takes spend.", "products": [
        P("mcatnu", "Mastercard at Nubank", "Mastercard is the only network named on any Nu card: credit, debit, Black and Platinum in Brazil, credit and debit in Mexico, Colombia's cards, the US World Elite card under an 'exclusive relationship', and Nu Global's virtual card. The agreements found are trademark licences; commercial terms are not public. Nu also moves spend off cards through Pix, Pix financing, Pay by Tap and NuPay, and its new CFO came from Visa.",
          s=["con"], div="nu", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Nu 20-F 2025", F20], ["Nu: US and Nu Global, Sep 2026", US], ["NeoFeed: fintechs and Mastercard, Jun 2019", FEED]]),
    ]},
    {"id": "pillar-market", "name": "Latin American banking", "blurb": "Pix, licences, rivals.", "products": [
        P("market", "The market", "Pix with 179.7 million users, Brazil's rules on how institutions name themselves, Mexico's digital banks (Klar, Stori, Revolut) and incumbents, Bre-B new in Colombia, and Mercado Pago and Nubank making 36% of Brazil's card-credit growth.",
          s=["con"], div="nu", rev="grp", src=[["Nu 20-F 2025", F20], ["NuHeadlines 45, Mar 2026", NH45], ["NuHeadlines 51, Sep 2026", NH51]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
