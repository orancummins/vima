"""Banco Angolano de Investimentos (BAI), as a platform: the data behind ``Banco_Angolano_de_Investimentos_Platform.html``.

``python customers/build_page.py bai`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Banco_Angolano_de_Investimentos_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bai_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bai_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BAI'
PAGE = 'Banco_Angolano_de_Investimentos_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BAI Platform"
KICKER = f"Banco Angolano de Investimentos · as at {AS_OF}"
H1 = '<h1>BAI <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BAI's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BAI's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BAI's colours"

PIN = (-8.81, 13.23, 'Luanda')
PIN_FACING = 'Angola and Lusophone Africa'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail banking', 'commercial': 'Commercial banking', 'private': 'Private banking', 'markets': 'Investment & correspondent banking', 'insurance': 'Insurance & pensions'}
DIV = {'group': 'Grupo BAI', 'bai': 'BAI (Angola)', 'europa': 'BAI Europa', 'cv': 'BAI Cabo Verde', 'nossa': 'NOSSA Seguros', 'aurea': 'ÁUREA', 'pay4all': 'Pay4all (é-Kwanza)'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F4F6", "panel-2": "#E4EAEE", "ink": "#0A1119", "ink-2": "#1A232A",
    "muted": "#3E444E", "faint": "#616770", "line": "#C7CDD6", "line-2": "#A7AEBA", "focus": "#002D74",
    "accent": "#002D74", "link": "#001E5B", "gold": "#002D74", "gold-deep": "#001A4F", "gold-ink": "#001E5B",
    "l1": "#001339", "l2": "#001A4F", "l3": "#0A245F", "l4": "#284C7D", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0A2152", "l2f": "#002D74", "l3f": "#1C4996", "l4f": "#6592C1",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A1119", "shadow": "rgba(6,21,38,.22)", "wash-a": "rgba(0,45,116,.14)",
    "wash-b": "rgba(101,146,193,.10)", "gb2": "#0A2152", "gb3": "#002D74", "gb4": "#89B2D7", "brand-grad": "linear-gradient(90deg,#001A4F,#002D74 55%,#89B2D7)",
    "gold-grad": "linear-gradient(135deg,#89B2D7 0%,#002D74 45%,#001A4F 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090B0D", "panel": "#101418", "panel-2": "#161C21", "ink": "#F2F5F7", "ink-2": "#D3DBDF",
    "muted": "#9FA6B0", "faint": "#7C828B", "line": "#262A31", "line-2": "#373C44", "focus": "#5791D1",
    "accent": "#437FC4", "link": "#89B2D7", "gold": "#437FC4", "gold-deep": "#5791D1", "gold-ink": "#89B2D7",
    "l1": "#89B2D7", "l2": "#6899CE", "l3": "#799BDA", "l4": "#A5C5E2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0A2152", "l2f": "#002D74", "l3f": "#1C4996", "l4f": "#6592C1",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050708", "wash-a": "rgba(0,45,116,.12)", "wash-b": "rgba(101,146,193,.06)",
    "gb2": "#0A2152", "gb3": "#002D74", "gb4": "#89B2D7", "gold-grad": "linear-gradient(135deg,#BDD9F0 0%,#437FC4 45%,#002D74 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
