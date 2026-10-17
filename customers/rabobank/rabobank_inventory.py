"""Rabobank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the H1 2026 results (4 August 2026) and the
FY2025 results and appendix (10 February 2026). Rabobank's websites block direct fetches, so card and
payment facts come from its product pages read through a proxy and from Dutch trade press. ``neo`` is the
Mastercard lens: [depth, note], where 3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard,
1 = partly, 0 = not Mastercard, None = nothing public.
"""
# ruff: noqa: E501

H1 = "https://www.rabobank.nl/en/nieuws/011537973/rabobank-posts-a-net-result-of-eur-2-694-million-in-first-half-of-2026"
H1PDF = "https://media.rabobank.com/asset/8280e8bc-4430-4181-b2d8-92cafa2fc8d7/Press-Release-Interim-Results-2026.pdf"
FY25 = "https://www.rabobank.nl/en/nieuws/011514177/rabobank-posts-a-net-result-of-eur-4-957-million-in-2025"
FY25APP = "https://media.rabobank.com/m/35df032caa9f8236/original/Press-Release-Annual-Results-2025-Appendix.pdf"
NLTIMES = "https://nltimes.nl/2026/08/04/ai-push-prompts-eu2-billion-rabobank-investment-possible-future-job-cuts"
NOS = "https://nos.nl/l/2625458"
WIKI = "https://en.wikipedia.org/wiki/Rabobank"
INSHORT = "https://www.rabobank.com/about-us/in-short"
MOODYS = "https://www.rabobank.com/about-us/investor-relations/articles/011522972/moody-s-revises-rabobank-s-issuer-rating-to-aa3-outlook-stable"
FITCH = "https://www.rabobank.com/about-us/investor-relations/articles/011526401/fitch-ratings-upgrades-rabobank-s-issuer-rating-to-aa-outlook-remains-stable"
CEO22 = "https://www.banken.nl/nieuws/24010/rabobank-presenteert-nieuwe-bestuursvoorzitter-stefaan-decraene"
CEO26 = "https://www.banken.nl/nieuws/27472/stefaan-decraene-rabobank-zou-voor-iedereen-als-thuis-moeten-voelen"
IT2BN = "https://www.banken.nl/nieuws/27298/rabobank-pompt-2-miljard-in-it-fundament-voor-ai"
HUB = "https://www.banken.nl/nieuws/27233/rabobank-versnelt-inzet-van-ai-agents-met-nieuwe-agentic-hub"
ALFAM = "https://www.banken.nl/nieuws/26626/grote-slag-op-kredietmarkt-rabobank-neemt-alfam-over-van-abn-amro"
BELFIUS = "https://www.banken.nl/nieuws/27187/belgie-verkoopt-20-belang-in-belfius-rabobank-en-ing-genoemd-als-kanshebbers"
MCPAS = "https://www.rabobank.nl/over-ons/pers/persberichten/011332253/eerste-geslaagde-transactie-met-nieuwe-rabobank-betaalpas-van-mastercard"
VISADEBIT = "https://www.banken.nl/nieuws/23706/rabobank-introduceert-met-visa-debit-een-nieuwe-betaalmogelijkheid"
DMC24 = "https://www.banken.nl/nieuws/25308/rabobank-stapt-over-op-nieuwe-debit-mastercard-betaalpas"
DEBITPAGE = "https://www.rabobank.nl/particulieren/betalen/betaalpas/visa-debit-mastercard"
PASPAGE = "https://www.rabobank.nl/particulieren/betalen/betaalpas"
IAMEXPAT = "https://www.iamexpat.nl/expat-info/dutch-news/mastercard-and-visa-debit-replace-maestro-and-v-pay-netherlands"
ZELF = "https://www.rabobank.nl/bedrijven/betalen/zelf-betalingen-doen"
GOLD = "https://www.rabobank.nl/particulieren/betalen/creditcards/rabo-goldcard"
PAKKET = "https://www.rabobank.nl/particulieren/betalen/nieuwe-betaalpakketten"
RADAR20 = "https://radar.avrotros.nl/artikel/klanten-rabobank-geconfronteerd-met-onverwacht-omzetten-creditkaart-36131"
CC2020 = "https://www.banken.nl/nieuws/22637/rabobank-start-in-stilte-met-grootscheepse-vervanging-creditcards"
BIZCARD = "https://www.rabobank.nl/bedrijven/betalen/zelf-betalingen-doen/rabo-businesscard"
WERONEWS = "https://www.rabobank.nl/nieuws/011505875/ideal-vanaf-2026-stapsgewijs-over-naar-wero"
WEROBIZ = "https://www.rabobank.nl/bedrijven/service/betalen-en-ontvangen/idealnaarwero"
EPI = "https://epicompany.eu/media-insights/successful-first-phase-marks-major-next-steps-in-ideal-to-wero-migration/"
ACI = "https://cfotech.co.uk/story/rabobank-moves-ideal-to-wero-in-instant-payment-shift"
SMARTPAY = "https://www.rabobank.nl/bedrijven/betalen/klanten-laten-betalen/rabo-smart-pay"
KLANT = "https://www.rabobank.nl/bedrijven/betalen/klanten-laten-betalen"
AEVI = "https://aevi.com/newsroom/rabobank"
DEJA = "https://thepaypers.com/payments/news/rabobank-partners-with-dejamobile"
TAP = "https://docs.developer.rabobank.com/smartpay/reference/rabo-tap-to-pay"
BELAST = "https://www.banken.nl/nieuws/27069/rabobank-officieel-huisbankier-van-belastingdienst"
BELAST0 = "https://www.banken.nl/nieuws/25795/rabobank-wordt-huisbankier-van-belastingdienst"
QIVALIS = "https://www.banken.nl/nieuws/27119/europees-bankenconsortium-voor-euro-stablecoin-groeit-naar-37-leden-met-abn-amro-en-rabobank-erbij"
AGENT = "https://www.banken.nl/nieuws/27076/mastercard-en-rabobank-voeren-eerste-ai-agentbetaling-in-nederland-uit"
INFORM = "https://www.banken.nl/nieuws/27178/van-rule-based-naar-realtime-ai-rabobank-tilt-fraudepreventie-naar-een-hoger-niveau-met-inform"
RIS = "https://www.rabobank.nl/bedrijven/betalen/rabo-identity-services"
APP = "https://www.banken.nl/nieuws/27218/rabobank-vernieuwt-rabo-app-met-focus-op-hyperpersonalisatie"
CHALLENGE = "https://www.banken.nl/nieuws/27271/rabobank-wil-spaargedrag-stimuleren-met-money-challenges-in-rabo-app"
SIA = "https://www.banken.nl/nieuws/27486/rabobank-en-ing-in-wereldwijde-top-tien-van-bankapps"
LOVED = "https://www.banken.nl/nieuws/27186/rabobank-is-de-meest-geliefde-app-van-nederland-vier-financiele-apps-in-de-top-tien"
OBVION = "https://www.banken.nl/nieuws/27452/rabobank-en-dochter-obvion-scherpen-hypotheeknormen-vanaf-2027-aan"
MT1000 = "https://www.banken.nl/nieuws/27481/rabobank-private-banking-voert-mt1000-ranglijst-voor-private-banking-aan"
CENSE = "https://www.banken.nl/nieuws/27151/rabo-investments-en-gd-ventures-leiden-seed-ronde-van-65-miljoen-euro-in-cense"
RCOM = "https://www.rabobank.com/"
MSHARE = "https://www.banken.nl/bankensector/marktaandeel"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "cooperative · capital · strategy", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a cooperative with no shareholders, €639 billion of assets and a 20% CET1 ratio, roots in 1898 farmers' banks, up to €2 billion for data, IT and AI, and a push for scale.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "€2.7bn in H1, CET1 20%.", "div": "group", "rev": "grp", "products": [
            P("balance", "Balance sheet & earnings", "Net profit of €2,694 million in H1 2026 (RoE 9.5%, cost/income 50.2%, CET1 20.2%) after €562 million of impairments, mostly two South American wholesale cases; €4,957 million in 2025 on income of €16.4 billion; total assets €638.9 billion; Moody's Aa3 (April 2026) and Fitch AA- (May 2026).",
              s=["con", "corp"], neo=[0, ""], src=[["H1 2026 results", H1], ["H1 2026 press release (PDF)", H1PDF], ["FY2025 appendix", FY25APP], ["Moody's revision, Apr 2026", MOODYS], ["Fitch upgrade, May 2026", FITCH]]),
        ]},
        {"id": "1.2", "ic": "users-round", "name": "Cooperative & leadership", "blurb": "Members, not shareholders.", "div": "group", "rev": "grp", "products": [
            P("coop", "The cooperative", "A bank 'without shareholders, but with members', with 78 local banks in five Dutch regions and about €58 billion of equity built up over time; more than €1 billion given back through cooperative initiatives since 2023 ⚠ member count not published in 2026 releases.",
              s=["con", "sme"], o="I", neo=[0, ""], src=[["Rabobank: in short", INSHORT], ["FY2025 appendix", FY25APP], ["NL Times, Aug 2026", NLTIMES]]),
            P("leadership", "Managing board", "Chair Stefaan Decraene (from BNP Paribas and Dexia Bank Belgium, appointed 2022, second term from 2026), CFO Bas Brouwers, Retail Netherlands director Carlo van Kemenade; payments led by Suzan van Eeten (Tribe Lead Payments & Savings) ⚠ Supervisory Board chair not re-checked.",
              s=["corp"], neo=[0, ""], src=[["Banken.nl: Decraene appointed, Sep 2022", CEO22], ["Banken.nl: Decraene interview, Oct 2026", CEO26], ["NL Times, Aug 2026", NLTIMES]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage", "blurb": "Farmers' banks of 1898.", "div": "group", "rev": "grp", "products": [
            P("heritage", "Heritage", "Raiffeisen-Bank (Utrecht) and Boerenleenbank (Eindhoven), both founded in 1898, merged in 1972; the local banks became one legal entity on 1 January 2016; US retail was sold to Mechanics Bank in 2019 while farm lending stayed.",
              s=["con"], o="I", neo=[0, ""], src=[["Wikipedia: Rabobank", WIKI]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Up to €2bn over three years.", "div": "group", "rev": "grp", "products": [
            P("tech", "Data, IT & AI", "Up to €2 billion over three years for the data and IT foundation, customer experience and scaling AI (August 2026); an Agentic Hub for more than 1,100 software teams (July 2026); about 48,000 staff, 1,000 fewer in a year, with AI expected to shrink the workforce gradually.",
              s=["corp"], st="new", ay="Aug 2026", neo=[0, ""], src=[["H1 2026 results", H1], ["Banken.nl: €2bn for IT, Aug 2026", IT2BN], ["Banken.nl: Agentic Hub, Jul 2026", HUB], ["NL Times, Aug 2026", NLTIMES]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy & deals", "blurb": "Scale, simplicity, Alfam.", "div": "group", "rev": "grp", "products": [
            P("strategy", "Growing a better world together", "Serve customers, grow and gain scale, simplify and cut cost; Decraene says 'scale is only becoming more important' and is open to buying a bank; named as a possible bidder for Belgium's 20% Belfius stake ⚠ press speculation.",
              s=["corp"], neo=[0, ""], src=[["FY2025 results", FY25], ["NOS, Aug 2026", NOS], ["Banken.nl: Belfius stake, Jun 2026", BELFIUS]]),
            P("deals", "Deals", "Alfam (Defam) bought from ABN AMRO to merge with Freo into the Dutch consumer-credit leader (agreed November 2025, closing expected Q3 2026 ⚠ completion not confirmed); BPD bought BEMOG (2024); Belgian retail exited about 2021 ⚠.",
              s=["con"], o="A", st="flux", ay="Nov 2025", neo=[0, ""], src=[["Banken.nl: Alfam, Nov 2025", ALFAM], ["FY2025 appendix", FY25APP], ["Banken.nl: Belfius stake, Jun 2026", BELFIUS]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: Maestro replaced by Debit Mastercard and Visa Debit side by side, credit and business cards on either network, iDEAL becoming Wero, Rabo Smart Pay acceptance, the Tax Administration's payments, and a euro stablecoin.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit cards", "blurb": "Mastercard and Visa, side by side.", "div": "nl", "rev": "drb", "products": [
            P("debit", "Debit Mastercard & Visa Debit", "Since 2022 Rabobank issues both: a card shows 'either a Visa or a Mastercard logo', is replaced on expiry, pays online with a 16-digit number and carries Mastercard's sustainability badge; the Debit Mastercard rollout began in June 2024 ⚠ split between networks not disclosed.", short="Debit (Mastercard and Visa)",
              s=["con", "sme"], lc="everyday", st="flux", ay="Jun 2024", o="P", at="Mastercard, Visa", neo=[1, "Split between Debit Mastercard and Visa Debit ⚠ shares not disclosed."],
              mc="Every reissue is a share decision between the two networks.",
              src=[["Rabobank: Visa Debit & Debit Mastercard", DEBITPAGE], ["Banken.nl: Debit Mastercard rollout, Jun 2024", DMC24], ["Banken.nl: Visa Debit, Mar 2022", VISADEBIT]]),
            P("maestro", "Maestro", "The old Rabobank debit card, white or gold, still in circulation until replaced; Dutch banks stopped issuing Maestro replacements from 1 July 2023.", short="Maestro (being replaced)",
              s=["con"], lc="everyday", st="retired", o="P", at="Mastercard", neo=[2, "Maestro is Mastercard's."], src=[["Rabobank: debit card", PASPAGE], ["IamExpat: Maestro replaced, Jan 2023", IAMEXPAT]]),
            P("wallets", "Apple Pay, Google Pay & Garmin Pay", "Wallet tokens move to a new card automatically when it is activated; Garmin Pay must be added again; business debit cards also work with Apple Pay and Google Pay ⚠ launch date not found.",
              s=["con", "sme"], lc="everyday", o="P", at="Apple, Google, Garmin", neo=[1, "Tokens on whichever network the card carries."], src=[["Rabobank: Visa Debit & Debit Mastercard", DEBITPAGE], ["Rabobank: paying as a business", ZELF]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "GoldCard, Visa by default.", "div": "nl", "rev": "drb", "products": [
            P("credit", "Rabo GoldCard & RaboCard", "Sold with a payment package (€1.25 a month on Rabo Free, €2.00 on Rabo Standaard, included in Rabo Comfort): up to €10,000 a month, 360-day purchase insurance and a 2% FX mark-up; RaboCard holders got GoldCard benefits from 1 February 2026; since the 2020 reissue the GoldCard has been Visa by default with Mastercard on request ⚠ split not disclosed.", short="Credit (Visa or Mastercard)",
              s=["con"], lc="borrow", ay="Apr 2020", o="P", at="Visa, Mastercard", neo=[1, "Visa by default since 2020; Mastercard on request ⚠."],
              src=[["Rabobank: Rabo GoldCard", GOLD], ["Rabobank: new payment packages", PAKKET], ["Radar: credit cards switched, Apr 2020", RADAR20], ["Banken.nl: credit card reissue, Sep 2020", CC2020]]),
        ]},
        {"id": "2.3", "ic": "briefcase", "name": "Business cards", "blurb": "BusinessCard on either network.", "div": "nl", "rev": "drb", "products": [
            P("bizcard", "Rabo BusinessCard", "A business credit card accepted 'wherever you see the Visa or Mastercard logo', with cards for employees, 180-day purchase insurance and Visa Secure or Mastercard ID Check; a business debit card sits alongside ⚠ network split not disclosed.", short="Business cards (Visa or Mastercard)",
              s=["sme"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Visa or Mastercard ⚠ split not disclosed."],
              mc="Commercial-card controls could reach 800,000 SMEs.",
              src=[["Rabobank: Rabo BusinessCard", BIZCARD], ["Rabobank: paying as a business", ZELF]]),
        ]},
        {"id": "2.4", "ic": "zap", "name": "iDEAL to Wero", "blurb": "iDEAL ends in 2027.", "div": "nl", "rev": "drb", "products": [
            P("ideal", "iDEAL | Wero", "iDEAL, used for more than 70% of Dutch online payments, carries the iDEAL | Wero logo from 29 January 2026, moves onto Wero's platform from April 2026 and ends at the end of 2027; ACI Worldwide processes Rabobank's Wero payments on SEPA Instant (June 2026); Wero pricing stays close to iDEAL's until 2029.",
              s=["con", "sme"], lc="move", st="flux", ay="Jan 2026", o="P", at="EPI, ACI Worldwide", neo=[0, "EPI's own account-to-account rail."],
              mc="The main threat to card volume online, and later in shops.",
              src=[["Rabobank: iDEAL becomes Wero (business)", WEROBIZ], ["Rabobank: iDEAL to Wero, Nov 2025", WERONEWS], ["CFOtech: ACI and Rabobank, Jun 2026", ACI]]),
            P("wero", "Wero & EPI", "Rabobank is part of EPI; all Dutch issuing banks connect to Wero from October 2026, with purchase protection by 1 January 2028 and later subscriptions, contactless in shops and deferred payment; Wero has 56 million users in Belgium, France and Germany.",
              s=["con", "sme"], lc="move", st="new", o="P", at="EPI", neo=[0, "EPI's own."], src=[["EPI: first phase done, Jul 2026", EPI], ["Rabobank: iDEAL becomes Wero (business)", WEROBIZ]]),
        ]},
        {"id": "2.5", "ic": "store", "name": "Acceptance", "blurb": "Smart Pay, SmartPin, Tap to Pay.", "div": "nl", "rev": "drb", "products": [
            P("smartpay", "Rabo Smart Pay", "A free dashboard for terminals, online payments, payment requests, cash, direct debit and international payments, with next-day settlement and a partner network of tills and webshops ⚠ acquiring processor not identified.", short="Rabo Smart Pay (all schemes)",
              s=["sme"], lc="move", o="B", neo=[1, "Accepts Mastercard among all schemes."],
              mc="Merchant data and risk tools for a large SME base.",
              src=[["Rabobank: Rabo Smart Pay", SMARTPAY], ["Rabobank: letting customers pay", KLANT]]),
            P("smartpin", "Rabo SmartPin & PinBox", "Built with AEVI since 2016: more than 30,000 SmartPin set-ups and 10,000 PinBox terminals on Ingenico and Castles devices for markets, delivery, shops and bars.",
              s=["sme"], lc="move", o="P", at="AEVI", neo=[1, "Accepts all schemes."], src=[["AEVI: Rabobank, Apr 2026", AEVI]]),
            P("taptopay", "Rabo Tap to Pay", "An app that turns an iOS or Android phone into a contactless terminal linked to a partner till; SoftPOS from dejamobile (March 2024).",
              s=["sme"], lc="move", st="new", ay="Mar 2024", o="P", at="dejamobile", neo=[1, "Accepts contactless cards on all schemes."], src=[["Rabobank developer: Tap to Pay", TAP], ["The Paypers: dejamobile, Mar 2024", DEJA]]),
        ]},
        {"id": "2.6", "ic": "building", "name": "Payments for the state", "blurb": "The tax office's bank.", "div": "nl", "rev": "drb", "products": [
            P("belasting", "Belastingdienst house bank", "House bank to the Dutch Tax Administration from 1 May 2026, handling about 99% of its payments, some 275 million transactions a year, taken over from ING after a 2024 tender.",
              s=["corp"], lc="move", st="new", ay="May 2026", neo=[0, ""], src=[["Banken.nl: house bank, May 2026", BELAST], ["Banken.nl: tender won, Dec 2024", BELAST0]]),
        ]},
        {"id": "2.7", "ic": "coins", "name": "Digital money", "blurb": "Qivalis euro stablecoin.", "div": "wr", "rev": "wr", "products": [
            P("qivalis", "Qivalis", "Rabobank and ABN AMRO joined the euro-stablecoin consortium in May 2026, taking it to 37 banks; the coin is designed for MiCA, backed by bank deposits and aimed at cross-border payments, securities settlement and programmable payments ⚠ licence status not checked here.",
              s=["corp"], lc="move", st="new", ay="May 2026", o="P", at="Qivalis", neo=[0, "Mastercard's role unknown."],
              mc="Multi-token settlement could connect Qivalis to card rails.",
              src=[["Banken.nl: Qivalis grows to 37, May 2026", QIVALIS]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: the first Dutch AI-agent payment on Mastercard Agent Pay, INFORM fraud models, identity and payment APIs, and an app being rebuilt for personal tips.",
    "tiles": [
        {"id": "3.1", "ic": "bot", "name": "Agentic payments", "blurb": "First in the Netherlands.", "div": "nl", "rev": "drb", "products": [
            P("agentpay", "AI-agent payment pilot", "On 6 May 2026 an AI agent booked a coffee tasting from a single prompt, the first such payment in the Netherlands, on Mastercard Agent Pay with PayOS orchestration and Mastercard Payment Passkeys; the agent never saw card details.", short="Agent Pay pilot (Mastercard)",
              s=["con"], lc="everyday", st="new", ay="May 2026", o="P", at="Mastercard, PayOS", neo=[3, "Mastercard Agent Pay and Payment Passkeys."],
              mc="Mastercard's clearest first at Rabobank.",
              src=[["Banken.nl: first AI-agent payment, May 2026", AGENT]]),
        ]},
        {"id": "3.2", "ic": "shield-check", "name": "Fraud", "blurb": "INFORM RiskShield, 15 years.", "div": "nl", "rev": "drb", "products": [
            P("fraud", "Fraud detection", "INFORM RiskShield, in use for more than 15 years, mixes rules and machine learning across internet banking, card fraud and risk-based authentication, scoring millions of transactions a day in milliseconds; contactless fraud is refunded in full.",
              s=["con", "sme"], lc="everyday", o="P", at="INFORM", neo=[0, "INFORM and Rabobank's own."],
              mc="Instant payments and Wero need real-time scam and identity checks.",
              src=[["Banken.nl: INFORM, Jun 2026", INFORM], ["Rabobank: debit card", PASPAGE]]),
        ]},
        {"id": "3.3", "ic": "fingerprint", "name": "Identity & APIs", "blurb": "iDIN, itsme, eHerkenning.", "div": "nl", "rev": "drb", "products": [
            P("identity", "Rabo Identity Services", "iDIN, itsme, eHerkenning and identity-document scanning sold by API, also to companies that are not Rabobank customers.",
              s=["sme", "corp"], lc="open", o="P", at="iDIN, itsme", neo=[0, ""], src=[["Rabobank: Rabo Identity Services", RIS]]),
            P("apis", "Developer portal & Smart Pay APIs", "Smart Pay merchant APIs for transactions and refunds, and Tap to Pay deep links for partner tills.",
              s=["sme"], lc="move", o="B", neo=[0, ""], src=[["Rabobank developer: Tap to Pay", TAP], ["Rabobank: Rabo Smart Pay", SMARTPAY]]),
        ]},
        {"id": "3.4", "ic": "sparkles", "name": "Personal banking", "blurb": "Tips with 75% click-through.", "div": "nl", "rev": "drb", "products": [
            P("personal", "Hyper-personalisation & Money Challenges", "A new platform under the Rabo App (July 2026) tailors what each customer sees; tips in the transaction timeline get about 75% click-through; Money Challenges added for saving (July 2026).",
              s=["con"], lc="grow", st="new", ay="Jul 2026", neo=[0, ""],
              mc="Spend insights and card-linked offers could feed the tips.",
              src=[["Banken.nl: Rabo App platform, Jun 2026", APP], ["Banken.nl: Money Challenges, Jul 2026", CHALLENGE]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: the largest Dutch mortgage and savings books, SME and private banking, a global food & agri bank with rural lending in four regions, DLL leasing in more than 25 countries, and property and investments.",
    "tiles": [
        {"id": "4.1", "ic": "house", "name": "Homes & households", "blurb": "22% of new mortgages.", "div": "nl", "rev": "drb", "products": [
            P("mortgages", "Mortgages: Rabobank & Obvion", "Market leader with 22.4% of new production in 2025, a €203.7 billion book and about 58,000 customers helped to buy or improve a home; Obvion tightens lending norms from 2027; 170,000 sign-ups to the Vooruit met je Huis energy programme.",
              s=["home"], lc="borrow", neo=[0, ""], src=[["FY2025 appendix", FY25APP], ["Banken.nl: Obvion norms, Oct 2026", OBVION], ["H1 2026 press release (PDF)", H1PDF]]),
            P("packages", "Accounts, packages & savings", "Payment packages renamed Rabo Free, Standaard and Comfort in February 2026; €375.1 billion of Dutch retail deposits at June 2026 and more than 9 million private and business customers.",
              s=["con"], lc="everyday", st="new", ay="Feb 2026", neo=[1, "Debit on Mastercard or Visa."], src=[["Rabobank: new payment packages", PAKKET], ["H1 2026 results", H1], ["FY2025 results", FY25]]),
            P("consumercredit", "Freo & Alfam", "Online lender Freo merged with Alfam (Defam), bought from ABN AMRO, to form the Dutch consumer-credit leader; ABN AMRO keeps selling the loans through a partnership ⚠ completion not confirmed.", div="freo",
              s=["con"], lc="borrow", st="flux", ay="Nov 2025", o="A", neo=[0, ""], src=[["Banken.nl: Alfam, Nov 2025", ALFAM]]),
        ]},
        {"id": "4.2", "ic": "briefcase-business", "name": "SMEs & private banking", "blurb": "800,000 SMEs, €83bn AuM.", "div": "nl", "rev": "drb", "products": [
            P("sme", "SME & self-employed banking", "More than 800,000 SMEs and close to 350,000 self-employed customers; market leader in SME lending.",
              s=["sme"], lc="borrow", neo=[1, "Business cards on Visa or Mastercard."],
              mc="Payment controls and commercial cards for a very large SME base.",
              src=[["H1 2026 press release (PDF)", H1PDF]]),
            P("private", "Private Banking & insurance", "Private Banking assets of €83.1 billion, ranked first in the MT1000 survey (October 2026); insurance-intermediary commissions of €363 million in 2025.",
              s=["aff"], lc="grow", neo=[0, ""], src=[["H1 2026 results", H1], ["Banken.nl: MT1000, Oct 2026", MT1000], ["FY2025 appendix", FY25APP]]),
        ]},
        {"id": "4.3", "ic": "earth", "name": "Food & agri worldwide", "blurb": "W&R: €143bn of loans.", "div": "wr", "rev": "wr", "products": [
            P("wholesale", "Wholesale & food & agri", "'Rabobank's global Food & Agri bank and a selective leader in the Energy Transition': €142.7 billion of loans and more than 19,000 clients at June 2026, food & agri 59% of the book, sustainable energy lending €8.2 billion, and €1 billion with the EIB and DLL for sustainable farming in Europe.",
              s=["corp", "farm"], lc="borrow", neo=[0, ""],
              mc="Supply-chain and virtual cards for food and agri value chains are untouched ground.",
              src=[["Rabobank.com", RCOM], ["H1 2026 press release (PDF)", H1PDF], ["FY2025 appendix", FY25APP]]),
            P("rural", "Rural banking abroad", "Farm lending of €35.6 billion at end-2025: Australia €13.1 billion, North America €9.3 billion, New Zealand €6.9 billion and Brazil €5.3 billion; North America trimmed by portfolio optimisation ⚠ no card issuing found abroad.",
              s=["farm"], lc="borrow", neo=[None, "No card programme found."],
              mc="Purchasing cards for farm inputs would be new to these markets for Rabobank.",
              src=[["FY2025 appendix", FY25APP]]),
            P("onlinesavings", "Online savings in Australia & New Zealand", "About 186,000 online savers with €9.8 billion of deposits at end-2025.",
              s=["con"], lc="grow", neo=[0, ""], src=[["FY2025 appendix", FY25APP]]),
        ]},
        {"id": "4.4", "ic": "factory", "name": "DLL leasing", "blurb": "€47bn, 25+ countries.", "div": "dll", "rev": "lease", "products": [
            P("dll", "DLL vendor & asset finance", "Lease portfolio of €47.1 billion at June 2026 in more than 25 countries across agriculture, construction, healthcare, technology and transport; 2025 net profit €306 million after Brazil impairments; €417 million of circular assets financed in H1 2026.",
              s=["farm", "corp"], lc="borrow", neo=[0, ""],
              mc="Vendor programmes could carry commercial cards and carbon data.",
              src=[["H1 2026 press release (PDF)", H1PDF], ["FY2025 appendix", FY25APP]]),
        ]},
        {"id": "4.5", "ic": "building-2", "name": "Property & investments", "blurb": "BPD and Rabo Investments.", "div": "bpd", "rev": "bpd", "products": [
            P("bpd", "BPD property development", "6,256 homes sold in the Netherlands and Germany in 2025 and a rental fund of 2,194 homes; a net loss of €51 million after a one-off tax charge.",
              s=["home"], lc="beyond", neo=[0, ""], src=[["FY2025 appendix", FY25APP]]),
            P("raboinvest", "Rabo Investments", "Private equity and venture investing; co-led a €6.5 million seed round in crypto-compliance firm Cense (June 2026).", div="invest",
              s=["corp"], lc="grow", neo=[0, ""], src=[["Banken.nl: Cense seed round, Jun 2026", CENSE], ["FY2025 appendix", FY25APP]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the Rabo App, top in the Netherlands, 78 local banks run with members, and partners from ATMs to intermediaries and till makers.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Rabo App", "blurb": "Number one in the Netherlands.", "div": "nl", "rev": "drb", "products": [
            P("app", "Rabo App & online banking", "First in the Netherlands and in the global top ten of Sia's mobile banking benchmark (October 2026), named the country's most loved app (June 2026), with card controls, online card payments switched on or off, and Wero inside.",
              s=["con", "sme"], lc="everyday", neo=[0, ""], src=[["Banken.nl: Sia ranking, Oct 2026", SIA], ["Banken.nl: most loved app, Jun 2026", LOVED], ["Rabobank: Visa Debit & Debit Mastercard", DEBITPAGE]]),
        ]},
        {"id": "5.2", "ic": "users-round", "name": "Local banks", "blurb": "78 banks, five regions.", "div": "nl", "rev": "drb", "products": [
            P("localbanks", "Local banks & members", "78 local banks in five regions serve four customer segments, with members steering community funding such as Rabo ClubSupport.",
              s=["con", "sme", "farm"], lc="open", o="I", neo=[0, ""], src=[["FY2025 appendix", FY25APP], ["Rabobank: in short", INSHORT]]),
        ]},
        {"id": "5.3", "ic": "plug", "name": "Partners & portals", "blurb": "Intermediaries, tills, portal.", "div": "group", "rev": "grp", "products": [
            P("partners", "Partners, intermediaries & Rabo Business Banking", "Defam's intermediary network and ABN AMRO's loan partnership, Smart Pay software partners for tills and webshops, and the Rabo Business Banking portal for wholesale clients.",
              s=["sme", "corp"], lc="open", o="P", neo=[0, ""], src=[["Banken.nl: Alfam, Nov 2025", ALFAM], ["Rabobank: letting customers pay", KLANT], ["Rabobank.com", RCOM]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Rabobank", "blurb": "Shared debit, an agent first.", "products": [
        P("mcatrabo", "Mastercard at Rabobank", "Rabobank replaced Maestro with Debit Mastercard and Visa Debit side by side from 2022, in shares it does not disclose; its credit cards default to Visa since 2020 with Mastercard on request, and business cards come on either network. Mastercard ran the first Dutch AI-agent payment with Rabobank in May 2026 on Agent Pay. iDEAL, becoming Wero, carries most online payments, and Rabobank is part of EPI.",
          s=["con"], div="group", rev="grp", mc="The relationship this map is drawn for.",
          src=[["Banken.nl: first AI-agent payment, May 2026", AGENT], ["Rabobank: Visa Debit & Debit Mastercard", DEBITPAGE], ["Radar: credit cards switched, Apr 2020", RADAR20]]),
    ]},
    {"id": "pillar-market", "name": "Dutch banking", "blurb": "Wero, instant payments, scale.", "products": [
        P("market", "The market", "ING, Rabobank and ABN AMRO hold 85% of Dutch bank assets; Maestro and V PAY gave way to Debit Mastercard and Visa Debit from 2023; iDEAL becomes Wero by end-2027; the EU instant-payments rules, PSD3 and MiCA apply, and DNB dropped its mortgage risk-weight floor in 2026 ⚠.",
          s=["con"], div="group", rev="grp", src=[["Banken.nl: market share, Jun 2026", MSHARE], ["IamExpat: Maestro replaced, Jan 2023", IAMEXPAT], ["EPI: first phase done, Jul 2026", EPI]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
