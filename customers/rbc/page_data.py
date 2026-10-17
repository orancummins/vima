"""Royal Bank of Canada, as a platform: the data behind ``RBC_Platform.html``.

``python customers/build_page.py rbc`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``RBC_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from rbc_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from rbc_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'RBC'
PAGE = 'RBC_Platform.html'
AS_OF = "17 October 2026"
TITLE = "RBC Platform"
KICKER = f"Royal Bank of Canada · as at {AS_OF}"
H1 = '<h1>RBC <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: RBC's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in RBC's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in RBC's colours"

PIN = (43.65, -79.38, 'Toronto')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'pb': 'Personal Banking', 'cb': 'Commercial Banking', 'wm': 'Wealth Management', 'ins': 'Insurance', 'cm': 'Capital Markets'}
DIV = {'group': 'Royal Bank of Canada', 'royal': 'RBC Royal Bank', 'avion': 'Avion Rewards', 'gtb': 'Global Transaction Banking', 'wealth': 'RBC Wealth Management', 'us': 'RBC Bank & City National', 'cm': 'RBC Capital Markets', 'moneris': 'Moneris'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F5F6", "panel-2": "#E5ECEF", "ink": "#0B151C", "ink-2": "#213037",
    "muted": "#58646F", "faint": "#78818A", "line": "#CED4DA", "line-2": "#B5BDC5", "focus": "#0059B3",
    "accent": "#0059B3", "link": "#003881", "gold": "#0059B3", "gold-deep": "#002F6A", "gold-ink": "#003881",
    "l1": "#001F47", "l2": "#002F6A", "l3": "#0E4490", "l4": "#3571A7", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0E3A74", "l2f": "#0059B3", "l3f": "#2570C2", "l4f": "#7DACCB",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0B151C", "shadow": "rgba(7,29,45,.22)", "wash-a": "rgba(0,89,179,.14)",
    "wash-b": "rgba(125,172,203,.10)", "gb2": "#0E3A74", "gb3": "#0059B3", "gb4": "#9CC6DD", "brand-grad": "linear-gradient(90deg,#002F6A,#0059B3 55%,#9CC6DD)",
    "gold-grad": "linear-gradient(135deg,#9CC6DD 0%,#0059B3 45%,#002F6A 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0C0E", "panel": "#13191C", "panel-2": "#1C2328", "ink": "#F2F6F7", "ink-2": "#D7DFE2",
    "muted": "#AFB6BD", "faint": "#91979E", "line": "#343C45", "line-2": "#525C66", "focus": "#72AED8",
    "accent": "#619FCE", "link": "#9CC6DD", "gold": "#619FCE", "gold-deep": "#72AED8", "gold-ink": "#9CC6DD",
    "l1": "#9CC6DD", "l2": "#80B3D6", "l3": "#8EB4E0", "l4": "#B2D3E6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0E3A74", "l2f": "#0059B3", "l3f": "#2570C2", "l4f": "#7DACCB",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,89,179,.12)", "wash-b": "rgba(125,172,203,.06)",
    "gb2": "#0E3A74", "gb3": "#0059B3", "gb4": "#9CC6DD", "gold-grad": "linear-gradient(135deg,#C4E1F1 0%,#619FCE 45%,#0059B3 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
