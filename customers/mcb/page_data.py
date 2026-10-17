"""Mauritius Commercial Bank (MCB), as a platform: the data behind ``Mauritius_Commercial_Bank_Platform.html``.

``python customers/build_page.py mcb`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Mauritius_Commercial_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from mcb_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from mcb_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'MCB'
PAGE = 'Mauritius_Commercial_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "MCB Platform"
KICKER = f"MCB Group · The Mauritius Commercial Bank · as at {AS_OF}"
H1 = '<h1>MCB <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: MCB's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in MCB's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in MCB's colours"

PIN = (-20.16, 57.5, 'Port Louis')
PIN_FACING = 'Mauritius, the Indian Ocean and Africa'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail & Business Banking', 'corporate': 'Mauritian & Regional Corporates', 'overseas': 'Overseas Banking Subsidiaries', 'cibpb': 'African CIB & Private Banking', 'group': 'Group & non-banking'}
DIV = {'group': 'MCB Group', 'mcb': 'MCB Ltd (Mauritius)', 'juice': 'MCB Juice', 'mg': 'MCB Madagascar', 'sc': 'MCB Seychelles', 'mv': 'MCB Maldives', 'capm': 'MCB Capital Markets', 'nbf': 'Leasing, Factors & Microfinance'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F4", "panel-2": "#EEE7EA", "ink": "#1D0D11", "ink-2": "#3C282E",
    "muted": "#776266", "faint": "#908285", "line": "#DCD2D4", "line-2": "#CABEC0", "focus": "#C41230",
    "accent": "#C41230", "link": "#890D1A", "gold": "#C41230", "gold-deep": "#6F0A15", "gold-ink": "#890D1A",
    "l1": "#48070E", "l2": "#6F0A15", "l3": "#9E1E29", "l4": "#B3485D", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#7D1A25", "l2f": "#C41230", "l3f": "#C93C50", "l4f": "#CB91A0",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1D0D11", "shadow": "rgba(45,11,19,.22)", "wash-a": "rgba(196,18,48,.14)",
    "wash-b": "rgba(203,145,160,.10)", "gb2": "#7D1A25", "gb3": "#C41230", "gb4": "#DCACBA", "brand-grad": "linear-gradient(90deg,#6F0A15,#C41230 55%,#DCACBA)",
    "gold-grad": "linear-gradient(135deg,#DCACBA 0%,#C41230 45%,#6F0A15 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0E0A0C", "panel": "#1D1518", "panel-2": "#2B2023", "ink": "#F7F3F5", "ink-2": "#E3DADE",
    "muted": "#C3B8BA", "faint": "#A79D9F", "line": "#4E3E41", "line-2": "#776467", "focus": "#D5889C",
    "accent": "#CB7A8D", "link": "#DCACBA", "gold": "#CB7A8D", "gold-deep": "#D5889C", "gold-ink": "#DCACBA",
    "l1": "#DCACBA", "l2": "#D394A5", "l3": "#DDA0A8", "l4": "#E4BDC9", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#7D1A25", "l2f": "#C41230", "l3f": "#C93C50", "l4f": "#CB91A0",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080607", "wash-a": "rgba(196,18,48,.12)", "wash-b": "rgba(203,145,160,.06)",
    "gb2": "#7D1A25", "gb3": "#C41230", "gb4": "#DCACBA", "gold-grad": "linear-gradient(135deg,#EECBD6 0%,#CB7A8D 45%,#C41230 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
