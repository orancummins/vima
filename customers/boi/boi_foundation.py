"""Bank of Ireland's Foundation layer, as at 17 October 2026 (see page_data.py for the format)."""
# ruff: noqa: E501

IR = "https://investorrelations.bankofireland.com/"
UP = IR + "app/uploads/"
H1 = UP + "2026-H1-RNS-FINAL-N-P.pdf"
INTERIM = UP + "BoIG-Interim-Report-2026-web.pdf"
FY25 = UP + "D15699-BOI-FY-2025-Annual-Results-Announcement-Web-Feb26-FINAL-np.pdf"
FY25RNS = UP + "2026.03.02-RNS-Bank-of-Ireland-Annual-Results-31-December-2025-vFF.pdf"
HISTORY = "https://www.bankofireland.com/about-bank-of-ireland/about-the-group/bank-of-ireland-history/"
GEC = "https://www.bankofireland.com/about-bank-of-ireland/about-the-group/management-structure/"
PR = "https://www.bankofireland.com/about-bank-of-ireland/press-releases/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · charter · brand", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a €169 billion balance sheet rated A+ at the bank, a royal charter from 1783 and a State rescue it has fully repaid, a core rebuilt on Temenos, and Strategy 2028's target of more than 16% on tangible equity.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & capital", "blurb": "€169 billion, CET1 15.5%.", "div": "grp", "rev": "grp", "products": [
            P("balance", "Balance sheet", "Total assets of €168.6 billion, customer deposits of €108.5 billion and loans of €84.0 billion at 30 June 2026; Wealth assets under management a record €65.5 billion.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 results, Jul 2026", H1]]),
            P("earnings", "Earnings", "Underlying profit before tax of €1.8 billion in 2025 (€1.39 billion statutory, after a UK motor-finance provision); €960 million in the first half of 2026, up 33%, with a 14.4% statutory return on tangible equity and a net interest margin of 2.68%.",
              s=["corp"], neo=[0, ""], src=[["H1 2026 results, Jul 2026", H1], ["FY2025 results, Mar 2026", FY25RNS]]),
            P("capital", "Capital, ratings & distributions", "CET1 of 15.5% pro forma. The bank is rated Aa3 by Moody's (outlook positive, August 2026) and A+ by Fitch; the holding company A2 and A-. A 39c interim dividend and a €530 million buyback in 2026, and €4.4 billion returned since 2022. Listed on Euronext Dublin only since the London listing ended in June 2026; market value about €18 billion.",
              s=["corp"], neo=[0, ""], src=[["Bank of Ireland: credit ratings", IR + "debt-investors/credit-ratings/"], ["Bank of Ireland: completion of delisting, Jun 2026", UP + "2026.06.29-BOIG-RNS-Completion-of-Delisting.pdf"]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Governance & leadership", "blurb": "CEO Myles O'Grady since 2022.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Board & leadership", "Group CEO Myles O'Grady (November 2022), Chair (and Governor) Akshaya Bhargava (January 2025), CFO Mark Spain; Susan Russell runs Retail Ireland, Gavin Kelly Davy and Wealth, John Feeney Corporate & Commercial, Gail Goldie the UK bank, and Ciarán Coyle, as group COO, technology, data and payments. Prag Sharma joined from Citi as Chief AI Officer in October 2026.",
              s=["corp"], neo=[0, ""], src=[["Bank of Ireland: Group Executive Committee", GEC], ["Bank of Ireland: Chief AI Officer appointed, Jul 2026", PR + "2026/bank-of-ireland-appoints-prag-sharma-as-chief-artificial-intelligence-officer/"]]),
            P("regulation", "Regulators & conduct", "Supervised by the Central Bank of Ireland and the ECB. The Central Bank fined the bank €100.5 million over tracker mortgages in 2022, and an IT fault in August 2023 let customers draw money they did not have; the UK bank was fined £3.8 million in 2025 for a late Confirmation of Payee rollout. The Irish bank levy costs about €200 million a year across the banks.",
              s=["corp", "con"], neo=[0, ""], src=[["Central Bank of Ireland: tracker mortgage fine, Sep 2022", "https://edit.centralbank.ie/news/article/enforcement-action-the-governor-and-company-of-the-bank-of-ireland-reprimanded-and-fined-100-520-000-by-the-central-bank-of-ireland-for-regulatory-breaches-affecting-tracker-mortgage-customers-29-september-2022"], ["Finextra: Bank of Ireland UK fined for late Confirmation of Payee", "https://www.finextra.com/newsarticle/47326/bank-of-ireland-uk-fined-37-million-for-implementing-anti-fraud-tool-14-months-too-late"]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Charter & heritage", "blurb": "College Green, 1783.", "div": "grp", "rev": "grp", "products": [
            P("heritage", "From 1783 to the State's exit", "Opened under royal charter in 1783 and at the old Parliament House on College Green from 1808; banker to the Irish Government from 1922. Rescued in 2009–11 (€4.7 billion of State capital), it repaid the State in full: the last shares were sold on 23 September 2022, about €6.7 billion recovered in all.", short="1783 to the State's exit",
              s=["corp", "con"], o="I", neo=[0, ""], src=[["Bank of Ireland: history", HISTORY], ["ISIF: State exit, Sep 2022", UP + "2022.09.23-RNS-ISIF-.pdf"]]),
            P("market", "The three-bank market", "Since Ulster Bank and KBC left Ireland, the market has three main banks (AIB, Bank of Ireland and PTSB), with Revolut reaching more than 80% of adults; Bank of Ireland took KBC's €7.6 billion of performing mortgages and 150,000 customers in February 2023.",
              s=["con", "home"], o="A", ay="Feb 2023", neo=[0, ""], src=[["KBC: sale to Bank of Ireland closes, Feb 2023", "https://newsroom.kbc.com/kbc-bank-ireland-closes-sale-of-substantially-all-of-its-assets-and-liabilities-to-bank-of-ireland"], ["Irish Times: lessons from Ireland's Revolut revolution, Jun 2026", "https://www.irishtimes.com/business/economy/2026/06/20/lessons-from-irelands-revolut-revolution/"]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & data core", "blurb": "Temenos underneath, AI on top.", "div": "grp", "rev": "grp", "products": [
            P("core", "Core banking & AI platform", "A Temenos core chosen in 2016 ('Project Omega', with Accenture and Capgemini); an enterprise AI platform and an AI Academy (more than 1,000 colleagues) in 2026, with GenAI used by 99% of contact-centre staff and AI expected to deliver about a fifth of targeted savings.",
              s=["corp"], o="P", at="Temenos, Accenture", neo=[0, ""], src=[["FinTech Futures: Temenos for core banking, 2016", "https://www.fintechfutures.com/core-banking-technology/bank-of-ireland-chooses-temenos-for-core-banking-revamp"], ["H1 2026 interim report", INTERIM]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy 2028", "blurb": "More than 16% on tangible equity.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "Strategy 2028", "Set on 2 March 2026: a statutory return on tangible equity above 16% by 2028, income above €4.75 billion, costs flat at about €2.2 billion with about €250 million of efficiencies, CET1 around 14.5%, about €1.5 billion of investment and a 50% payout. Guidance was raised in July 2026.",
              s=["corp"], st="new", ay="Mar 2026", neo=[0, ""], src=[["FY2025 results and Strategy 2028, Mar 2026", FY25RNS], ["H1 2026 results, Jul 2026", H1]]),
            P("exits", "Portfolio exits", "Out of US leveraged acquisition finance (February 2026, a €1.2 billion book running off), running down GB corporate lending; earlier, UK credit cards went to Jaja (2019) and UK personal lending stopped (2023).",
              s=["corp"], st="retired", neo=[0, ""], src=[["FY2025 results, Mar 2026", FY25RNS]]),
        ]},
    ],
}
