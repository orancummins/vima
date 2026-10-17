"""Bank of Ireland, as a platform: the data behind ``Bank_of_Ireland_Platform.html``.

``python customers/build_page.py boi`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from boi_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from boi_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = "Bank of Ireland"
PAGE = "Bank_of_Ireland_Platform.html"
AS_OF = "17 October 2026"
TITLE = "Bank of Ireland Platform"
KICKER = f"Bank of Ireland Group · as at {AS_OF}"
H1 = '<h1>Bank of Ireland <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Bank of Ireland's royal blues for the bank, from the deep navy foundation to the bright access layer, graphite for\n"
                "   the people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = 'the five slices: foundation (deep navy), rails (royal blue), services (bright blue), lines (cornflower), access (graphite); graphite for the people'
GLOBE_NOTE = "the globe: Bank of Ireland's navy, royal blue and sky"

PIN = (53.34, -6.26, 'Dublin')
PIN_FACING = 'Ireland and Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
# The group reports Retail Ireland, Wealth and Insurance, Retail UK, Corporate and Commercial, and Group Centre.
REV = {"ri": "Retail Ireland segment", "wi": "Wealth and Insurance segment", "uk": "Retail UK segment",
       "cc": "Corporate and Commercial segment", "grp": "Group Centre"}
DIV = {"ri": "Bank of Ireland", "wi": "Davy & New Ireland", "uk": "Bank of Ireland UK", "cc": "Corporate & Commercial",
       "grp": "Bank of Ireland Group"}
DEFAULT_DIV = "grp"

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F5FB", "panel-2": "#E5EBF7", "ink": "#0A1530", "ink-2": "#1C2B4D",
    "muted": "#46536E", "faint": "#69758E", "line": "#CCD5E6", "line-2": "#AFBBD3", "focus": "#0047BB",
    "accent": "#0047BB", "link": "#003A99", "gold": "#0047BB", "gold-deep": "#0B1F4F", "gold-ink": "#003A99",
    "l1": "#0B1F4F", "l2": "#00349A", "l3": "#0047BB", "l4": "#2F6AD9", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#14306E", "l2f": "#0047BB", "l3f": "#2F6AD9", "l4f": "#79A0EA",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#EAF0FF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#08214F", "l5t": "#FFFFFF", "slot": "#0A1530", "shadow": "rgba(8,24,64,.22)", "wash-a": "rgba(0,71,187,.14)",
    "wash-b": "rgba(121,160,234,.10)", "gb2": "#14306E", "gb3": "#0047BB", "gb4": "#9CC0FF", "brand-grad": "linear-gradient(90deg,#0B1F4F,#0047BB 55%,#9CC0FF)",
    "gold-grad": "linear-gradient(135deg,#9CC0FF 0%,#0047BB 45%,#0B1F4F 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090C14", "panel": "#111727", "panel-2": "#18203A", "ink": "#F2F5FB", "ink-2": "#D5DCEC",
    "muted": "#A3AEC7", "faint": "#808BA6", "line": "#29324C", "line-2": "#3D4868", "focus": "#7FA6F5",
    "accent": "#6E99F2", "link": "#9CC0FF", "gold": "#6E99F2", "gold-deep": "#7FA6F5", "gold-ink": "#9CC0FF",
    "l1": "#9CC0FF", "l2": "#7FA6F5", "l3": "#8DB4FA", "l4": "#B4CCF7", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#14306E", "l2f": "#0047BB", "l3f": "#2F6AD9", "l4f": "#79A0EA",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#05070C", "wash-a": "rgba(0,71,187,.12)", "wash-b": "rgba(121,160,234,.06)",
    "gb2": "#14306E", "gb3": "#0047BB", "gb4": "#9CC0FF", "gold-grad": "linear-gradient(135deg,#CFE0FF 0%,#6E99F2 45%,#0047BB 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
