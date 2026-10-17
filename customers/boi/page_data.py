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
    "ground": "#FFFFFF", "panel": "#F2F3F7", "panel-2": "#E7E9F0", "ink": "#0D0F21", "ink-2": "#2A2F46",
    "muted": "#666680", "faint": "#848494", "line": "#D6D6E0", "line-2": "#C6C6D2", "focus": "#0000FF",
    "accent": "#0000FF", "link": "#0A00AF", "gold": "#0000FF", "gold-deep": "#08008C", "gold-ink": "#0A00AF",
    "l1": "#050057", "l2": "#08008C", "l3": "#2314CB", "l4": "#5659C9", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#1B139E", "l2f": "#0000FF", "l3f": "#4E4ADD", "l4f": "#9BA1D7",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0D0F21", "shadow": "rgba(8,11,53,.22)", "wash-a": "rgba(0,0,255,.14)",
    "wash-b": "rgba(155,161,215,.10)", "gb2": "#1B139E", "gb3": "#0000FF", "gb4": "#B3BAE5", "brand-grad": "linear-gradient(90deg,#08008C,#0000FF 55%,#B3BAE5)",
    "gold-grad": "linear-gradient(135deg,#B3BAE5 0%,#0000FF 45%,#08008C 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0B0F", "panel": "#161820", "panel-2": "#222431", "ink": "#F3F4F7", "ink-2": "#DCDEE6",
    "muted": "#C1C1CC", "faint": "#AAAAB4", "line": "#46465C", "line-2": "#74748F", "focus": "#9299E1",
    "accent": "#858BD9", "link": "#B3BAE5", "gold": "#858BD9", "gold-deep": "#9299E1", "gold-ink": "#B3BAE5",
    "l1": "#B3BAE5", "l2": "#9DA4DF", "l3": "#AAA8E7", "l4": "#C2C7EB", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#1B139E", "l2f": "#0000FF", "l3f": "#4E4ADD", "l4f": "#9BA1D7",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050709", "wash-a": "rgba(0,0,255,.12)", "wash-b": "rgba(155,161,215,.06)",
    "gb2": "#1B139E", "gb3": "#0000FF", "gb4": "#B3BAE5", "gold-grad": "linear-gradient(135deg,#CCD2F3 0%,#858BD9 45%,#0000FF 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
