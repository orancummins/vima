"""Capital One, as a platform: the data behind ``Capital_One_Platform.html``.

``python customers/build_page.py capitalone`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Capital_One_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from capitalone_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from capitalone_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Capital One'
PAGE = 'Capital_One_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Capital One Platform"
KICKER = f"Capital One Financial · as at {AS_OF}"
H1 = '<h1>Capital One <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Capital One's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Capital One's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Capital One's colours"

PIN = (38.92, -77.22, 'McLean')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'card': 'Credit Card segment', 'consumer': 'Consumer Banking segment', 'commercial': 'Commercial Banking segment', 'network': 'Discover Global Network & PULSE', 'grp': 'Group'}
DIV = {'cof': 'Capital One', 'card': 'Capital One Card', 'consumer': 'Consumer Banking', 'commercial': 'Commercial Banking', 'network': 'Discover Global Network', 'grp': 'Capital One Financial'}
DEFAULT_DIV = 'cof'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F5F6", "panel-2": "#E4EDEE", "ink": "#0A151A", "ink-2": "#1C2A2E",
    "muted": "#465458", "faint": "#687578", "line": "#C9D5D7", "line-2": "#ABBABD", "focus": "#004F87",
    "accent": "#004F87", "link": "#003666", "gold": "#004F87", "gold-deep": "#002E57", "gold-ink": "#003666",
    "l1": "#00203D", "l2": "#002E57", "l3": "#093D70", "l4": "#2A668C", "l5": "#271E38",
    "lu": "#746A81", "l1f": "#09355E", "l2f": "#004F87", "l3f": "#1C69A6", "l4f": "#6AA9C6",
    "l5f": "#403652", "luf": "#A39CAF", "l1t": "#E8F8FF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#051C2B", "l5t": "#FFFFFF", "slot": "#0A151A", "shadow": "rgba(5,29,41,.22)", "wash-a": "rgba(0,79,135,.14)",
    "wash-b": "rgba(106,169,198,.10)", "gb2": "#09355E", "gb3": "#004F87", "gb4": "#8DC5DB", "brand-grad": "linear-gradient(90deg,#09355E,#004879 55%,#D22E1E)",
    "gold-grad": "linear-gradient(135deg,#8DC5DB 0%,#004F87 45%,#002E57 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090C0D", "panel": "#111719", "panel-2": "#182023", "ink": "#F2F6F7", "ink-2": "#D4DEE0",
    "muted": "#A4B1B4", "faint": "#828D91", "line": "#2A3337", "line-2": "#3F4A4E", "focus": "#5CAED6",
    "accent": "#499ECA", "link": "#8DC5DB", "gold": "#499ECA", "gold-deep": "#5CAED6", "gold-ink": "#8DC5DB",
    "l1": "#8DC5DB", "l2": "#6DB2D2", "l3": "#7DB2DE", "l4": "#A8D3E4", "l5": "#D4D1DB",
    "lu": "#938AA2", "l1f": "#09355E", "l2f": "#004F87", "l3f": "#1C69A6", "l4f": "#6AA9C6",
    "l5f": "#746A81", "luf": "#746A81", "slot": "#050808", "wash-a": "rgba(0,79,135,.12)", "wash-b": "rgba(106,169,198,.06)",
    "gb2": "#09355E", "gb3": "#004F87", "gb4": "#8DC5DB", "gold-grad": "linear-gradient(135deg,#BEE4F1 0%,#499ECA 45%,#004F87 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
