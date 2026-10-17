"""First Abu Dhabi Bank, as a platform: the data behind ``First_Abu_Dhabi_Bank_Platform.html``.

``python customers/build_page.py fab`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``First_Abu_Dhabi_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from fab_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from fab_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'FAB'
PAGE = 'First_Abu_Dhabi_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "FAB Platform"
KICKER = f"First Abu Dhabi Bank · as at {AS_OF}"
H1 = '<h1>FAB <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: FAB's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in FAB's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in FAB's colours"

PIN = (24.45, 54.38, 'Abu Dhabi')
PIN_FACING = 'the Gulf, Egypt and global corridors'

ALLOWED_MENTIONS: tuple[str, ...] = ('Saudi',)

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'pbwpc': 'Personal, Business, Wealth & Privileged Client Banking', 'wb': 'Wholesale Banking', 'ibm': 'Investment Banking & Markets', 'intl': 'International'}
DIV = {'group': 'FAB Group', 'fab': 'FAB (UAE)', 'islamic': 'FAB Islamic', 'payit': 'Payit', 'dubaifirst': 'Dubai First', 'misr': 'FABMISR (Egypt)', 'ksa': 'FAB in Saudi Arabia', 'network': 'Network International (stake)'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F4F6", "panel-2": "#E5EBEE", "ink": "#0B131C", "ink-2": "#202B34",
    "muted": "#535B68", "faint": "#737985", "line": "#CCD1D9", "line-2": "#B2B8C2", "focus": "#003DA6",
    "accent": "#003DA6", "link": "#002579", "gold": "#003DA6", "gold-deep": "#001F65", "gold-ink": "#002579",
    "l1": "#001544", "l2": "#001F65", "l3": "#0D3086", "l4": "#335D9F", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0D2A6D", "l2f": "#003DA6", "l3f": "#2357B9", "l4f": "#789EC9",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0B131C", "shadow": "rgba(6,23,43,.22)", "wash-a": "rgba(0,61,166,.14)",
    "wash-b": "rgba(120,158,201,.10)", "gb2": "#0D2A6D", "gb3": "#003DA6", "gb4": "#98BBDC", "brand-grad": "linear-gradient(90deg,#001F65,#003DA6 55%,#98BBDC)",
    "gold-grad": "linear-gradient(135deg,#98BBDC 0%,#003DA6 45%,#001F65 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090C0E", "panel": "#12171B", "panel-2": "#1B2027", "ink": "#F2F5F7", "ink-2": "#D6DDE1",
    "muted": "#ACB1BA", "faint": "#8C919A", "line": "#313741", "line-2": "#4D535F", "focus": "#6C9DD7",
    "accent": "#5B8DCC", "link": "#98BBDC", "gold": "#5B8DCC", "gold-deep": "#6C9DD7", "gold-ink": "#98BBDC",
    "l1": "#98BBDC", "l2": "#7BA4D4", "l3": "#8AA6DF", "l4": "#AFCAE5", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0D2A6D", "l2f": "#003DA6", "l3f": "#2357B9", "l4f": "#789EC9",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050708", "wash-a": "rgba(0,61,166,.12)", "wash-b": "rgba(120,158,201,.06)",
    "gb2": "#0D2A6D", "gb3": "#003DA6", "gb4": "#98BBDC", "gold-grad": "linear-gradient(135deg,#C2DBF1 0%,#5B8DCC 45%,#003DA6 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
