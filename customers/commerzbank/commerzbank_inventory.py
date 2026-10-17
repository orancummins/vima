"""Commerzbank's layers, areas and products, as at 17 October 2026 (see page_data.py for the format).

Figures are the group's own unless a source says otherwise: the Q2 2026 results (6 August 2026) and the
FY2025 results (11 February 2026). ``neo`` is the Mastercard lens: [depth, note], where
3 = Mastercard's own product runs it, 2 = rides wholly on Mastercard, 1 = partly, 0 = not Mastercard,
None = nothing public.
"""
# ruff: noqa: E501

Q2 = "https://www.commerzbank.de/group/newsroom/press-releases/commerzbank-delivers-record-result.html"
Q2DE = "https://www.commerzbank.de/konzern/newsroom/pressemitteilungen/2026/20260806-pm-q2-2026.pdf"
FY25 = "https://www.commerzbank.de/group/newsroom/press-releases/annual-press-conference.html"
VISA = "https://www.commerzbank.de/group/newsroom/press-releases/partnership-visa.html"
PAYPERS = "https://thepaypers.com/payments/news/commerzbank-and-visa-form-partnership-in-card-business"
CARDS = "https://www.commerzbank.de/privatkunden/kreditkarten/"
MCDEBIT = "https://www.commerzbank.de/privatkunden/kreditkarten/mastercard-debit/"
CLASSIC = "https://www.commerzbank.de/privatkunden/kreditkarten/classic-kreditkarte/"
PREPAID = "https://www.commerzbank.de/privatkunden/kreditkarten/prepaid-karte/"
ACCOUNTS = "https://www.commerzbank.de/privatkunden/girokonten/girokonto-eroeffnen/"
BIZCARDS = "https://www.commerzbank.de/unternehmerkunden/firmenkreditkarten/"
PLIANT = "https://www.commerzbank.de/unternehmerkunden/partnerangebot/pliant/"
TERMINAL = "https://www.commerzbank.de/unternehmerkunden/zahlungsverkehr/kartenzahlungsterminal/"
GPJV = "https://www.commerzbank.de/group/newsroom/press-releases/joint-venture-global-payments.html"
FINANZTIP = "https://www.finanztip.de/daily/von-mastercard-zu-visa-was-commerzbank-kunden-beachten-muessen/"
FTRENDS = "https://www.finanztrends.de/news/commerzbank-aktie-kartentausch-von-mastercard-zu-visa/"
WERO = "https://www.commerzbank.de/service/kann-ich-den-zahlungsservice-wero-ueber-die-commerzbank-nutzen/"
WEROMF = "https://www.mobiflip.de/commerzbank-steigt-bei-wero-ein/"
TENDER = "https://www.commerzbank.de/group/newsroom/press-releases/result-tender-offer-unicredit.html"
UCOFFER = "https://www.unicreditgroup.eu/content/dam/unicreditgroup-eu/documents/en/investors/unicredit-unlimited-next-phase/PR_UniCredit-exchange-offer-Commerzbank-_16032026.pdf"
UCCOND = "https://www.unicreditgroup.eu/content/dam/unicreditgroup-eu/documents/en/investors/unicredit-unlimited-next-phase/Announcement-regarding-the-fulfilment-of-offer-conditions-dated-16-October-2026.pdf"
UCMC = "https://insurancenewsnet.com/oarticle/unicredit-and-mastercard-expand-payments-partnership-10"
HVBCARD = "https://www.hypovereinsbank.de/hvb/privatkunden/banking-im-alltag/karten/debitkarte-unicredit-card"
MGMT = "https://www.commerzbank.de/group/who-we-are/management/"
STRAT = "https://www.commerzbank.de/group/who-we-are/strategy-brand/"
WIKI = "https://en.wikipedia.org/wiki/Commerzbank"
JOBS = "https://www.commerzbank.de/konzern/newsroom/pressemitteilungen/abschluss-rahmenregelungen.html"
CUSTODY = "https://www.finextra.com/newsarticle/43297/commerzbank-granted-crypto-custody-licence"
CRYPTOFIN = "https://www.ledgerinsights.com/commerzbank-launches-corporate-crypto-service-in-alliance-with-deutsche-borses-crypto-finance/"
MBCARDS = "https://www.mbank.pl/indywidualny/karty/"
BLIK = "https://thepaypers.com/online-payments/blik-eyes-expansion-with-mastercard-partnership--776468"
GIROCARD = "https://tuenews.de/en/changes-to-ec-cards/"
MAESTRO21 = "https://www.it-finanzmagazin.de/maestro-girocard-banken-epi-127937/"
EPI = "https://www.epicompany.eu/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · heritage · owner", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a record €1.8 billion half-year profit, a bank founded in Hamburg in 1870, AI rolled out bank-wide, Momentum 2030, and UniCredit at about 49.65% with approvals arriving.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & returns", "blurb": "Record H1, RoTE 12.5%.", "div": "cbk", "rev": "oci", "products": [
            P("balance", "Balance sheet & earnings", "Q2 2026 revenues of €3.3 billion and a net result of €898 million (net RoTE 12.5%, CET1 14.4%); a record H1 net result of €1.81 billion. 2025: revenues €12.2 billion, record operating result €4.5 billion, net result €2.6 billion after €562 million of restructuring. Total assets about €603 billion (Q1 2026).",
              s=["corp"], neo=[0, ""], src=[["Q2 2026 results", Q2], ["FY2025 results", FY25], ["Wikipedia: Commerzbank", WIKI]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Leadership", "blurb": "Orlopp and Weidmann.", "div": "cbk", "rev": "oci", "products": [
            P("leadership", "Board & supervisory board", "CEO Bettina Orlopp, CFO Carsten Schmitt, Michael Kotzbauer (Corporate Clients), Thomas Schaufler (Private and Small-Business Customers), CRO Bernhard Spalt, COO Christiane Vorspel and Sabine Mlnarsky (HR); Jens Weidmann chairs the supervisory board.",
              s=["corp"], neo=[0, ""], src=[["Commerzbank: board of managing directors", MGMT], ["Commerzbank: tender result, Jul 2026", TENDER]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Heritage & brands", "blurb": "Hamburg, 1870.", "div": "cbk", "rev": "psbc", "products": [
            P("heritage", "Heritage & brands", "Founded in Hamburg in 1870; took over Dresdner Bank in 2009 with a state rescue; brands Commerzbank, comdirect (founded 1994), mBank and Commerz Real. The German state still holds about 12% (12.11%, May 2026).",
              s=["con"], o="I", neo=[0, ""], src=[["Wikipedia: Commerzbank", WIKI], ["Commerzbank: strategy and brand", STRAT]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & AI", "blurb": "Copilot and Gemini bank-wide.", "div": "cbk", "rev": "oci", "products": [
            P("tech", "IT simplification & AI", "Microsoft Copilot and Google Gemini rolled out across the bank, an internal AI Academy, cobaGPT used by more than 30,000 staff, and 10% of IT systems switched off in H1 2026; agentic-AI pilots planned.",
              s=["corp"], st="new", neo=[0, ""], src=[["Q2 2026 results", Q2], ["FY2025 results", FY25]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Momentum 2030", "blurb": "RoTE 15% by 2028.", "div": "cbk", "rev": "oci", "products": [
            P("strategy", "Momentum 2030", "Gain share in Germany, grow international business and use more securitisation; 2028 targets of 15% net RoTE, 50% cost-income and a €4.2 billion net result; about 3,900 full-time posts cut by 2028 ⚠.",
              s=["corp"], st="new", neo=[0, ""], src=[["FY2025 results", FY25], ["Commerzbank: strategy and brand", STRAT], ["Commerzbank: social plan, May 2025", JOBS]]),
            P("capital", "Capital return", "100% of net result after AT1 coupons paid out for 2026–2028; about €3.2 billion planned for 2026 including a buyback of up to €1.2 billion from 2 September 2026; dividend of €1.10 for 2025.",
              s=["corp"], neo=[0, ""], src=[["Q2 2026 results", Q2], ["FY2025 results", FY25]]),
        ]},
        {"id": "1.6", "ic": "building", "name": "UniCredit position", "blurb": "About 49.65%, approvals arriving.", "div": "ucg", "rev": "oci", "products": [
            P("unicredit", "UniCredit's stake", "UniCredit held 26.77% before its exchange offer of 16 March 2026; 17.60% was tendered by 3 July, for an overall position put at 49.65% with swaps ⚠. ECB and BaFin cleared entities including EURO Kartensysteme and Commerz Globalpay on 15–16 October 2026 ⚠. Commerzbank rejected the offer and says a majority cannot decide structural measures alone.",
              s=["corp"], st="flux", ay="Mar 2026", o="A", at="UniCredit", neo=[None, "UniCredit's card partner is Mastercard; Commerzbank's is Visa."],
              mc="The swing factor: UniCredit made Mastercard its issuing partner for 13 banks in 2023.",
              src=[["Commerzbank: tender result, Jul 2026", TENDER], ["UniCredit: exchange offer, Mar 2026", UCOFFER], ["UniCredit: offer conditions, Oct 2026", UCCOND], ["Q2 2026 results", Q2]]),
        ]},
    ],
}

RAILS = {
    "id": "L2", "name": "Rails", "analogy": "how money moves", "color": "--l2", "kind": "rail",
    "desc": "Seven ways money moves: girocards with Visa Debit and a standalone Mastercard Debit, credit moving from Mastercard to Visa, business cards and Pliant, Commerz Globalpay for acceptance, Wero still to launch, corporate payments and crypto custody, and mBank's cards and BLIK.",
    "tiles": [
        {"id": "2.1", "ic": "wallet-cards", "name": "Debit", "blurb": "girocard with Visa.", "div": "commerzbank", "rev": "psbc", "products": [
            P("girocard", "Commerzbank girocard", "Every current account comes with a 'Girocard (Debitkarte mit Visa-Funktion)': GiroKonto €4.90 a month, KlassikKonto €9.90 and PremiumKonto €12.90 with two cards; Apple Pay and Google Pay included. The Visa function was the first step of the February 2025 Visa deal and replaces Maestro.", short="girocard (girocard + Visa)",
              s=["con", "sme"], lc="everyday", st="new", ay="Feb 2025", o="P", at="girocard, Visa", neo=[0, "girocard and Visa."],
              mc="A 2021 plan to co-badge Mastercard Debit was overtaken by the Visa deal ⚠.",
              src=[["Commerzbank: accounts", ACCOUNTS], ["Commerzbank and Visa, Feb 2025", VISA], ["tünews: changes to EC cards", GIROCARD], ["IT Finanzmagazin: Maestro and girocard, Oct 2021", MAESTRO21]]),
            P("mcdebit", "Mastercard Debit", "A standalone Mastercard debit card at €3.50 a month, free with the KlassikKonto; Apple Pay, Google Pay, Garmin Pay and Swatch Pay; limits and country blocks in online banking; Mastercard Identity Check online. Launch date not found ⚠.", short="Mastercard Debit",
              s=["con"], lc="everyday", o="P", at="Mastercard", neo=[2, "A Mastercard debit card."],
              mc="Mastercard's main remaining consumer card at Commerzbank.",
              src=[["Commerzbank: Mastercard Debit", MCDEBIT]]),
        ]},
        {"id": "2.2", "ic": "credit-card", "name": "Credit cards", "blurb": "Mastercard to Visa.", "div": "commerzbank", "rev": "psbc", "products": [
            P("credit", "Classic, Gold & Premium credit cards", "Classic (€39.90 a year), Gold (with travel cover) and Premium cards, now 'von Visa', with a 3-Raten-Service from €200 and Visa extras (EVENTIM presales, Travelcentive). Since July 2026 Mastercard Classic holders are asked, in tranches, to switch early to Visa Classic; keeping a Mastercard reportedly needs the PremiumKonto ⚠.", short="Credit (Mastercard to Visa)",
              s=["con"], lc="borrow", st="flux", ay="Jul 2026", o="P", at="Visa", neo=[1, "Visa; Mastercard Classic in run-off."],
              mc="The defining loss: Commerzbank's Mastercard credit book is being moved to Visa.",
              src=[["Commerzbank: credit cards", CARDS], ["Commerzbank: ClassicKreditkarte", CLASSIC], ["Finanztrends: Mastercard to Visa, Jul 2026", FTRENDS], ["Finanztip: Mastercard to Visa, Aug 2026", FINANZTIP]]),
            P("prepaid", "Prepaid Kreditkarte & Young Visa", "A reloadable prepaid card usable wherever Mastercard or Visa is accepted (network per card not stated ⚠), and Young Visa for pupils and students.",
              s=["con"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Mastercard or Visa ⚠."], src=[["Commerzbank: prepaid card", PREPAID], ["Commerzbank: credit cards", CARDS]]),
            P("amex", "American Express Platinum", "A metal Amex Platinum Card offered by referral, with Priority Pass lounges and SIXT ride credit.",
              s=["con"], lc="everyday", o="P", at="American Express", neo=[0, "Amex."], src=[["Commerzbank: credit cards", CARDS]]),
        ]},
        {"id": "2.3", "ic": "briefcase", "name": "Business cards", "blurb": "Pliant on Visa.", "div": "commerzbank", "rev": "psbc", "products": [
            P("bizcards", "Business Card Classic, Premium & Premium Debit", "Business Card Classic (€34.90 a year), Premium (€79.90, free in the PremiumGeschäftskonto) and Premium Debit (€5.90 a month), pitched as the girocard's successor; network not stated ⚠, with tailored Visa products for business and corporate clients promised 'gradually'.",
              s=["sme"], lc="everyday", o="P", neo=[None, "Network not stated ⚠."],
              mc="Commercial cards are still open; the Visa deal names them as next.",
              src=[["Commerzbank: business cards", BIZCARDS], ["Commerzbank and Visa, Feb 2025", VISA]]),
            P("pliant", "Pliant corporate cards", "Physical and virtual Visa Platinum Business and Visa Infinite Business credit cards from Pliant for the Mittelstand, with limits, real-time reporting and receipt matching, linked to the Commerzbank business account.",
              s=["sme", "corp"], lc="everyday", st="new", o="P", at="Pliant", neo=[0, "Visa."], src=[["Commerzbank: Pliant", PLIANT]]),
        ]},
        {"id": "2.4", "ic": "store", "name": "Acceptance", "blurb": "Commerz Globalpay.", "div": "globalpay", "rev": "psbc", "products": [
            P("globalpay", "Commerz Globalpay", "Joint venture of Global Payments (51%) and Commerzbank (49%) in Frankfurt, announced January 2024; terminals, e-commerce and the GP tom tap-on-phone app for small and mid-sized merchants, taking Visa, Mastercard, Apple Pay and Google Pay with no monthly fee.",
              s=["sme"], lc="move", st="new", ay="Jan 2024", o="P", at="Global Payments", neo=[1, "Accepts every network."],
              mc="Acceptance and merchant-risk services through Global Payments.",
              src=[["Commerzbank and Global Payments JV, Jan 2024", GPJV], ["Commerzbank: card terminals", TERMINAL]]),
        ]},
        {"id": "2.5", "ic": "send", "name": "Wero & wallets", "blurb": "Wero decided, not live.", "div": "cbk", "rev": "psbc", "products": [
            P("wero", "Wero", "Commerzbank left the EPI project in early 2022; on 11 February 2026 Bettina Orlopp said 'Wir werden bei Wero mitmachen', most likely as a user rather than a shareholder. Launch at Commerzbank and comdirect is 'in planning'.",
              s=["con"], lc="move", st="unconf", ay="Feb 2026", o="P", at="EPI", neo=[0, "Wero, the European scheme."],
              mc="Wero competes with cards online and, later, in shops.",
              src=[["Commerzbank: Wero", WERO], ["mobiFlip: Commerzbank joins Wero, Feb 2026", WEROMF], ["EPI", EPI]]),
            P("wallets", "Apple Pay, Google Pay & wearables", "Apple Pay and Google Pay on the girocard and credit cards, plus Garmin Pay and Swatch Pay.",
              s=["con"], lc="everyday", o="P", at="Apple, Google", neo=[1, "Tokens on Visa and Mastercard cards."], src=[["Commerzbank: accounts", ACCOUNTS], ["Commerzbank: Mastercard Debit", MCDEBIT]]),
        ]},
        {"id": "2.6", "ic": "earth", "name": "Corporate payments & digital assets", "blurb": "30% of German trade.", "div": "commerzbank", "rev": "cc", "products": [
            P("cash", "Cash management & trade finance", "Payments, cash management and trade finance for about 24,000 corporate client groups, covering about 30% of German foreign trade, in more than 40 countries.",
              s=["corp"], lc="move", neo=[0, ""],
              mc="B2B virtual cards and cross-border flows are untested ground.",
              src=[["Q2 2026 results (German)", Q2DE]]),
            P("crypto", "Crypto custody & trading", "The first BaFin crypto custody licence for a German full-service bank (November 2023), and crypto trading and custody for corporates with Deutsche Börse's Crypto Finance ⚠; no stablecoin product found.",
              s=["corp"], lc="move", ay="Nov 2023", o="P", at="Crypto Finance", neo=[0, ""], src=[["Finextra: crypto custody licence, Nov 2023", CUSTODY], ["Ledger Insights: Crypto Finance", CRYPTOFIN]]),
        ]},
        {"id": "2.7", "ic": "wallet", "name": "mBank cards & BLIK", "blurb": "Visa debit, Mastercard credit.", "div": "mbank", "rev": "mbank", "products": [
            P("mbcards", "mBank cards", "Debit mostly Visa (Visa Foto, Visa Me, Visa Podróże) plus virtual eKarta cards; credit on Mastercard (Mastercard Me and World Elite Mastercard, limit PLN 20,000–500,000 with Priority Pass), and a basic credit card on Mastercard or Visa.", short="mBank (Visa debit, Mastercard credit)",
              s=["pl"], lc="everyday", o="P", at="Visa, Mastercard", neo=[1, "Visa debit, Mastercard credit."],
              mc="World Elite at mBank is Mastercard's top card in the group.",
              src=[["mBank: cards", MBCARDS]]),
            P("blik", "BLIK", "Poland's bank-owned mobile payment scheme, part-owned by mBank; contactless BLIK runs on Mastercard acceptance under a 2018 deal.",
              s=["pl"], lc="move", o="P", at="Polski Standard Płatności", neo=[1, "Contactless BLIK on Mastercard (2018)."], src=[["The Paypers: BLIK and Mastercard, 2018", BLIK]]),
        ]},
    ],
}

SERVICES = {
    "id": "L3", "name": "Services", "analogy": "the engine room", "color": "--l3", "kind": "cyl",
    "desc": "What runs around every account: an in-house Fraud AI and 3-D Secure on both networks, the Ava assistant and cobaGPT, and Visa-linked perks.",
    "tiles": [
        {"id": "3.1", "ic": "shield-check", "name": "Fraud & security", "blurb": "Fraud AI, built in-house.", "div": "cbk", "rev": "psbc", "products": [
            P("fraudai", "Fraud AI", "An in-house AI fraud tool (FY2025); the Visa partnership adds joint work on payment security.",
              s=["con", "sme"], lc="everyday", o="B", neo=[0, "Commerzbank's own; Visa security cooperation."],
              mc="Scam and identity scoring are open as instant payments and Wero grow.",
              src=[["FY2025 results", FY25], ["Commerzbank and Visa, Feb 2025", VISA]]),
            P("idcheck", "3-D Secure & card controls", "Mastercard Identity Check and Visa Secure for online card payments, confirmed with a PIN and TAN; online and cash limits and country blocks set in online banking.",
              s=["con"], lc="everyday", o="P", at="Mastercard, Visa", neo=[1, "Identity Check on Mastercard cards."], src=[["Commerzbank: Mastercard Debit", MCDEBIT], ["Commerzbank: ClassicKreditkarte", CLASSIC]]),
        ]},
        {"id": "3.2", "ic": "bot", "name": "AI for customers & staff", "blurb": "Ava, cobaGPT.", "div": "cbk", "rev": "psbc", "products": [
            P("ava", "Ava", "The virtual assistant in the Commerzbank banking app, with agentic-AI pilots planned.",
              s=["con"], lc="everyday", st="new", o="B", neo=[0, ""],
              mc="Agent Pay is untouched ground.",
              src=[["FY2025 results", FY25]]),
            P("staffai", "Agent Assist & cobaGPT", "Agent Assist for advisers and the cobaGPT chatbot used by more than 30,000 employees, alongside Copilot and Gemini.",
              s=["corp"], lc="everyday", st="new", o="B", neo=[0, ""], src=[["FY2025 results", FY25], ["Q2 2026 results", Q2]]),
        ]},
        {"id": "3.3", "ic": "gift", "name": "Offers & loyalty", "blurb": "Visa perks.", "div": "commerzbank", "rev": "psbc", "products": [
            P("offers", "Card perks & referrals", "EVENTIM concert presales for Visa cardholders and 7% off travel at Visa's Travelcentive; customer referral rewards. No card-linked-offers platform found.",
              s=["con"], lc="grow", o="P", at="Visa", neo=[0, "Visa perks."],
              mc="Card-linked offers have no owner yet.",
              src=[["Commerzbank: credit cards", CARDS]]),
        ]},
    ],
}

LINES = {
    "id": "L4", "name": "Business lines", "analogy": "what it sells", "color": "--l4", "kind": "app", "dark": True,
    "desc": "What customers buy: accounts, €96 billion of mortgages and €285 billion of securities for private and small-business customers, comdirect and wealth management, the leading bank for the Mittelstand, and mBank in Poland.",
    "tiles": [
        {"id": "4.1", "ic": "user-round", "name": "Private & small-business", "blurb": "Revenues up 12%.", "div": "commerzbank", "rev": "psbc", "products": [
            P("retail", "Private and Small-Business Customers", "Q2 2026 revenues of €1.26 billion (+12%) and an operating result of €438 million; more than €400 billion of assets under management; accounts come with a girocard with Visa Debit.",
              s=["con", "sme"], lc="everyday", neo=[0, "girocard with Visa Debit."], src=[["Q2 2026 results", Q2], ["Q2 2026 results (German)", Q2DE]]),
            P("mortgages", "Mortgages & loans", "€96 billion of mortgage loans and €125 billion of average loans in the segment (Q2 2026).",
              s=["home"], lc="borrow", neo=[0, ""], src=[["Q2 2026 results", Q2]]),
        ]},
        {"id": "4.2", "ic": "trending-up", "name": "comdirect & wealth", "blurb": "21m trades in H1.", "div": "comdirect", "rev": "psbc", "products": [
            P("comdirect", "comdirect", "The digital main bank and broker: about 21 million trades in H1 2026 (+5%); Visa its preferred card partner since 2020.",
              s=["inv"], lc="grow", o="B", neo=[0, "Visa."], src=[["Q2 2026 results", Q2], ["Commerzbank and Visa, Feb 2025", VISA]]),
            P("wealth", "Wealth & portfolio management", "Securities volume of €285 billion (+€39 billion) and about €25 billion in discretionary mandates (+20%), with more than 90% of new mandates onboarded digitally; Commerz Real for real-asset funds.",
              s=["inv"], lc="grow", neo=[0, ""], src=[["Q2 2026 results", Q2], ["Wikipedia: Commerzbank", WIKI]]),
        ]},
        {"id": "4.3", "ic": "factory", "name": "Corporate Clients", "blurb": "24,000 client groups.", "div": "commerzbank", "rev": "cc", "products": [
            P("corporates", "Corporate Clients", "Germany's leading bank for the Mittelstand: Q2 2026 revenues of €1.23 billion and an operating result of €490 million, average loans of €123 billion (+16%); about 24,000 client groups.",
              s=["corp"], lc="borrow", neo=[0, ""],
              mc="Commercial and virtual cards for the Mittelstand are open ground.",
              src=[["Q2 2026 results", Q2], ["Q2 2026 results (German)", Q2DE]]),
        ]},
        {"id": "4.4", "ic": "flag", "name": "mBank", "blurb": "6 million customers.", "div": "mbank", "rev": "mbank", "products": [
            P("mbank", "mBank", "A digital universal bank with about 6 million customers in Poland, the Czech Republic and Slovakia: Q2 2026 revenues of €672 million (+15%) and an operating result of €365 million, with Swiss-franc loan provisions down to €29 million.",
              s=["pl"], lc="everyday", neo=[1, "Visa debit, Mastercard credit."], src=[["Q2 2026 results", Q2], ["Q2 2026 results (German)", Q2DE]]),
        ]},
    ],
}

ACCESS = {
    "id": "L5", "name": "Access", "analogy": "front doors", "color": "--l5", "kind": "port",
    "desc": "How customers reach the group: the Commerzbank and comdirect apps, about 400 locations and an advice centre, corporate offices in more than 40 countries, and partners.",
    "tiles": [
        {"id": "5.1", "ic": "smartphone", "name": "Apps", "blurb": "Commerzbank, comdirect, mBank.", "div": "cbk", "rev": "psbc", "products": [
            P("app", "Banking apps", "The Commerzbank banking app (cards, limits, Ava), the comdirect app and the mBank app.",
              s=["con", "inv", "pl"], lc="everyday", neo=[0, ""], src=[["FY2025 results", FY25], ["Commerzbank: Mastercard Debit", MCDEBIT]]),
        ]},
        {"id": "5.2", "ic": "building-2", "name": "Branches & advice", "blurb": "About 400 locations.", "div": "commerzbank", "rev": "psbc", "products": [
            P("branches", "Branches & advice centre", "About 400 locations across Germany, plus phone and video advice in the advice centre.",
              s=["con", "home"], lc="open", neo=[0, ""], src=[["Q2 2026 results (German)", Q2DE]]),
        ]},
        {"id": "5.3", "ic": "globe", "name": "Corporate network & partners", "blurb": "40+ countries.", "div": "cbk", "rev": "cc", "products": [
            P("network", "International network", "Corporate presence in more than 40 countries for the Mittelstand, large corporates and institutions.",
              s=["corp"], lc="open", neo=[0, ""], src=[["Q2 2026 results (German)", Q2DE]]),
            P("partners", "Partners", "Visa (cards and perks), Global Payments (Commerz Globalpay), Pliant (corporate cards), American Express and Crypto Finance.",
              s=["sme", "con"], lc="open", o="P", neo=[1, "Global Payments accepts Mastercard."], src=[["Commerzbank and Visa, Feb 2025", VISA], ["Commerzbank: Pliant", PLIANT], ["Commerzbank: card terminals", TERMINAL]]),
        ]},
    ],
}

PILLARS = [
    {"id": "pillar-mastercard", "name": "Mastercard at Commerzbank", "blurb": "Visa's bank, UniCredit's question.", "products": [
        P("mcatcbk", "Mastercard at Commerzbank", "Visa became Commerzbank's preferred card partner on 13 February 2025: girocards carry Visa Debit, the credit range is Visa and the Mastercard Classic book is being switched from July 2026; comdirect has been Visa since 2020. Mastercard keeps a standalone Mastercard Debit, Identity Check on its cards, acceptance through Commerz Globalpay and mBank's credit cards including World Elite. UniCredit, Mastercard's group partner since 2023, holds about 49.65% ⚠.",
          s=["con"], div="cbk", rev="oci", mc="The relationship this map is drawn for.",
          src=[["Commerzbank and Visa, Feb 2025", VISA], ["Finanztrends: Mastercard to Visa, Jul 2026", FTRENDS], ["UniCredit and Mastercard, May 2023", UCMC]]),
    ]},
    {"id": "pillar-market", "name": "German & Polish banking", "blurb": "girocard, Wero, BLIK.", "products": [
        P("market", "The market", "Maestro leaving German girocards by 2027 at the latest, with banks choosing Visa Debit or Debit Mastercard (HVB is moving to Mastercard); Wero replacing giropay; instant payments with verification of payee; and BLIK in Poland.",
          s=["con"], div="cbk", rev="oci", src=[["tünews: changes to EC cards", GIROCARD], ["HVB: UniCredit debit card", HVBCARD], ["EPI", EPI], ["The Paypers: BLIK and Mastercard, 2018", BLIK]]),
    ]},
]

LAYERS = [FOUNDATION, RAILS, SERVICES, LINES, ACCESS]
