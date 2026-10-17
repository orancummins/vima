"""Citi's Foundation layer, and the Data & AI and Ventures areas, as at 17 October 2026."""
# ruff: noqa: E501

SEC = "https://www.sec.gov/Archives/edgar/data/"
Q3R = SEC + "0000831001/000110465926115323/c-ex99d1.htm"
Q3S = "https://www.citigroup.com/rcs/citigpa/storage/public/Earnings/Q32026/2026psqtr3rslt.pdf"
FY25 = SEC + "831001/000110465926003604/c-20260114xex99d1.htm"
K10 = SEC + "831001/000083100126000011/c-20251231.htm"
Q10 = SEC + "0000831001/000083100126000045/c-20260630.htm"
IDCEO = "https://www.citigroup.com/rcs/citigpa/storage/public/investor-day/citi-ID26-ceo-presentation-transcript.pdf"
LEAD = "https://www.citigroup.com/global/about-us/leadership"
PR = "https://www.citigroup.com/global/news/press-release/"


def P(i, n, d, **x):
    return {"id": i, "n": n, "d": d, **x}


FOUNDATION = {
    "id": "L1", "name": "Foundation", "analogy": "balance sheet · charter · brand", "color": "--l1", "kind": "plate", "dark": True,
    "desc": "What everything else stands on: a $2.9 trillion balance sheet, a board and regulators still working through the 2020 consent orders, a 1812 charter and one brand, the technology being rebuilt underneath, and a strategy to earn 14 to 15% on tangible equity.",
    "tiles": [
        {"id": "1.1", "ic": "landmark", "name": "Balance sheet & capital", "blurb": "$2.9 trillion, CET1 12.8%.", "div": "grp", "rev": "grp", "products": [
            P("balance", "Balance sheet", "Total assets of $2.94 trillion, deposits of $1.5 trillion and loans of $820 billion at 30 September 2026, up from $2.66 trillion of assets at the end of 2025.",
              s=["inst", "gov"], neo=[0, ""], src=[["3Q26 earnings release", Q3R]]),
            P("earnings", "Earnings", "Revenue of $85.2 billion and net income of $14.3 billion in 2025; $23.8 billion and $5.2 billion in 3Q26 (return on tangible common equity 11.5%), and $73.2 billion and $16.9 billion over the first nine months of 2026.",
              s=["inst"], neo=[0, ""], src=[["3Q26 earnings release", Q3R], ["FY2025 earnings release", FY25]]),
            P("capital", "Capital & ratings", "CET1 ratio of 12.8%. Citigroup Inc. is rated A by Fitch (outlook positive), A3 by Moody's and BBB+ by S&P; Citibank, N.A. is AA-, Aa3 and A+. A $30 billion multi-year buyback was announced in May 2026; $16.5 billion was returned to shareholders in the first nine months of 2026.",
              s=["inst"], neo=[0, ""], src=[["Q2 2026 10-Q: ratings", Q10], ["3Q26 presentation", Q3S]]),
        ]},
        {"id": "1.2", "ic": "scale", "name": "Governance & regulators", "blurb": "Working out of the 2020 orders.", "div": "grp", "rev": "grp", "products": [
            P("leadership", "Board & leadership", "Jane Fraser has been CEO since March 2021 and chair since October 2025. CFO Gonzalo Luchetti (from March 2026); segment heads Shahmir Khaliq (Services), Andy Morton (Markets), Vis Raghavan (Banking), Andy Sieg (Wealth) and Pam Habner (U.S. Consumer Cards); Tim Ryan runs technology and Anand Selvakesari is COO.",
              s=["inst"], neo=[0, ""], src=[["Citi leadership", LEAD], ["Jane Fraser elected chair, Oct 2025", PR + "2025/jane-fraser-elected-chair-of-citi-board-of-directors"]]),
            P("consent", "The 2020 consent orders", "The Fed and OCC orders of October 2020 on risk management, data and controls are still in force. Penalties of about $136 million followed in July 2024; the OCC lifted that year's amendment in December 2025. About 90% of transformation programmes are at or near target, and Citi aims to give regulators its audit by early 2027.", short="2020 consent orders",
              s=["gov"], st="flux", neo=[0, ""], src=[["FY2025 10-K", K10], ["Investor Day 2026: CEO transcript", IDCEO], ["PYMNTS: Citi readies its audit, Oct 2026", "https://www.pymnts.com/news/banking/2026/citi-readies-audit-to-seek-end-of-federal-oversight-and-speed-growth/"]]),
        ]},
        {"id": "1.3", "ic": "badge-check", "name": "Brand & heritage", "blurb": "Since 1812.", "div": "grp", "rev": "grp", "products": [
            P("brand", "The Citi brand", "One brand and the red arc across every business; listed on the New York Stock Exchange as C, with a market value of about $206 billion in mid-October 2026.",
              s=["con", "corp"], neo=[0, ""], src=[["FY2025 10-K", K10]]),
            P("heritage", "City Bank to Citigroup", "Founded as the City Bank of New York in 1812; Citigroup formed in October 1998 when Citicorp merged with Travelers Group; bought Banamex in 2001; took $45 billion of TARP capital in 2008, which the Treasury fully exited in December 2010.",
              s=["inst"], o="I", neo=[0, ""], src=[["FY2025 10-K", K10], ["Citi: US Treasury exits Citigroup common shares, Dec 2010", "https://blog.citigroup.com/2010/12/us-treasury-exits-citigroup-common-shares"]]),
        ]},
        {"id": "1.4", "ic": "database", "name": "Technology & data core", "blurb": "Rebuilt under the orders.", "div": "grp", "rev": "grp", "products": [
            P("transform", "Transformation & modernisation", "About $3.3 billion of transformation spending in 2025, 548 applications retired, data consolidated into one institutional and one consumer store, a hybrid cloud, and North American corporate loans moved onto one platform. Services alone invests more than $2 billion a year in technology.",
              s=["corp", "inst"], neo=[0, ""], src=[["FY2025 10-K", K10], ["Investor Day 2026: CEO transcript", IDCEO]]),
        ]},
        {"id": "1.5", "ic": "target", "name": "Strategy", "blurb": "14–15% returns by 2031.", "div": "grp", "rev": "grp", "products": [
            P("strategy", "Investor Day 2026 targets", "Set on 7 May 2026: a return on tangible common equity above 11% in 2026, 11–13% in 2027–28 and 14–15% over 2029–31, an efficiency ratio below 60% now and below 55% later, and $5 billion of business investment through 2028.",
              s=["inst"], st="new", ay="May 2026", neo=[0, ""], src=[["Investor Day 2026: CEO transcript", IDCEO], ["3Q26 presentation", Q3S]]),
            P("simplify", "Simplification", "The 2023–24 reorganisation ('Project Bora Bora') into five businesses with eight management layers instead of 13 and 20,000 fewer roles; the exit from consumer banking in 14 markets outside the US; and, from 2026, U.S. Consumer Cards as its own segment with retail banking inside Wealth.",
              s=["inst"], neo=[0, ""], src=[["FY2025 10-K", K10], ["CNBC: Project Bora Bora, Nov 2023", "https://www.cnbc.com/2023/11/06/citigroup-considers-deep-job-cuts-project-bora-bora.html"], ["Citi: CFO transition and changes to U.S. Personal Banking, Nov 2025", PR + "2025/citi-cfo-transition-plans-changes-united-states-personal-banking-business"]]),
        ]},
    ],
}

DATA_AI = [
    P("aitools", "AI for 180,000 colleagues", "Core AI tools rolled out to more than 180,000 staff in 85 countries in 2025: Citi Assist for policy questions, Citi Stylus (agentic Workspaces since September 2025) and AI code review that frees about 100,000 hours a week. Arc, a platform for building agents, launched in April 2026.", short="Citi Stylus, Assist, Arc",
      s=["corp", "con"], st="new", neo=[0, ""], src=[["Citi Stylus Workspaces, Sep 2025", PR + "2025/citi-unveils-citi-stylus-workspaces-agentic-ai-turbocharging-productivity"], ["CIO Dive: Citi launches Arc, May 2026", "https://www.ciodive.com/news/citi-launches-arc-scale-ai-agents/819113/"], ["Investor Day 2026: CEO transcript", IDCEO]]),
    P("clientai", "AI in client channels", "A CitiDirect AI assistant for treasurers, Agent Assist in Services operations (March 2026), intelligent document processing for trade, and Citi Sky for Citigold clients.",
      s=["corp", "aff"], st="new", neo=[0, ""], rel=["citidirect", "citisky"], src=[["Investor Day 2026: Services", "https://www.citigroup.com/rcs/citigpa/storage/public/investor-day/citi-ID26-services-presentation.pdf"]]),
]

VENTURES = [
    P("ventures", "Citi Ventures", "Citi's venture arm, led by Arvind Purushotham: 26 investments in 2025 and more than 30 exits including DocuSign and Plaid; recent bets include BVNK (stablecoin infrastructure, October 2025), Wealth.com, Endowus and Clara.",
      s=["fin"], o="B", neo=[0, ""], src=[["Global Venturing: Citi Ventures, Jan 2026", "https://globalventuring.com/corporate/financial/citi-ventures-purushotham-corporate-investment/"], ["BusinessWire: BVNK, Oct 2025", "https://www.businesswire.com/news/home/20251009562874/en/"]]),
    P("devportal", "Developer portal", "developer.citi.com: Citi's API catalogue and sandbox for treasury, payments and trade integrations.",
      s=["fin", "corp"], neo=[0, ""], rel=["citiconnect"], src=[["Citi developer portal", "https://developer.citi.com"]]),
    P("stablejv", "Bank stablecoin venture", "One of 21 institutions that agreed on 1 September 2026 to form a joint company for a US-dollar stablecoin, targeted for the first half of 2027.",
      s=["inst", "fin"], st="unconf", ay="Sep 2026", o="P", neo=[0, ""], src=[["Blockhead: 21 banks commit to a joint stablecoin venture, Sep 2026", "https://blockhead.co/2026/09/02/21-banks-including-citi-goldman-sachs-bank-of-america-commit-to-joint-stablecoin-venture"]]),
]
