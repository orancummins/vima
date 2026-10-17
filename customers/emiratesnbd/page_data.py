"""Emirates NBD, as a platform: the data behind ``Emirates_NBD_Platform.html``.

``python customers/build_page.py emiratesnbd`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Emirates_NBD_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from emiratesnbd_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from emiratesnbd_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Emirates NBD'
PAGE = 'Emirates_NBD_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Emirates NBD Platform"
KICKER = f"Emirates NBD · as at {AS_OF}"
H1 = '<h1>Emirates NBD <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Emirates NBD's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Emirates NBD's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Emirates NBD's colours"

PIN = (25.27, 55.31, 'Dubai')
PIN_FACING = 'the Gulf, India and Turkiye'

ALLOWED_MENTIONS: tuple[str, ...] = ('Saudi',)

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'rbwm': 'Retail Banking & Wealth Management', 'cib': 'Corporate & Institutional Banking', 'gmt': 'Global Markets & Treasury', 'islamic': 'Islamic Banking', 'intl': 'International (DenizBank, Egypt, KSA, India)'}
DIV = {'group': 'Emirates NBD Group', 'enbd': 'Emirates NBD (UAE)', 'ei': 'Emirates Islamic', 'liv': 'Liv', 'deniz': 'DenizBank', 'egypt': 'Emirates NBD Egypt', 'ksa': 'Emirates NBD KSA', 'rbl': 'RBL Bank'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F4F5", "panel-2": "#E4EAEC", "ink": "#0A1116", "ink-2": "#161D22",
    "muted": "#2F3439", "faint": "#555A60", "line": "#C4CAD1", "line-2": "#A0A8B1", "focus": "#072447",
    "accent": "#072447", "link": "#061C3D", "gold": "#072447", "gold-deep": "#061A38", "gold-ink": "#061C3D",
    "l1": "#04142C", "l2": "#061A38", "l3": "#0C1E3D", "l4": "#26415E", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0C1D38", "l2f": "#072447", "l3f": "#204372", "l4f": "#5F8DB2",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A1116", "shadow": "rgba(8,20,31,.22)", "wash-a": "rgba(7,36,71,.14)",
    "wash-b": "rgba(95,141,178,.10)", "gb2": "#0C1D38", "gb3": "#072447", "gb4": "#86AFCC", "brand-grad": "linear-gradient(90deg,#061A38,#072447 55%,#86AFCC)",
    "gold-grad": "linear-gradient(135deg,#86AFCC 0%,#072447 45%,#061A38 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090B0C", "panel": "#0F1315", "panel-2": "#14181B", "ink": "#F2F5F6", "ink-2": "#D1D9DC",
    "muted": "#989FA7", "faint": "#71777E", "line": "#1F2428", "line-2": "#33373C", "focus": "#538EC0",
    "accent": "#457DAF", "link": "#86AFCC", "gold": "#457DAF", "gold-deep": "#538EC0", "gold-ink": "#86AFCC",
    "l1": "#86AFCC", "l2": "#6396BF", "l3": "#759ACD", "l4": "#A3C3D9", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0C1D38", "l2f": "#072447", "l3f": "#204372", "l4f": "#5F8DB2",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050707", "wash-a": "rgba(7,36,71,.12)", "wash-b": "rgba(95,141,178,.06)",
    "gb2": "#0C1D38", "gb3": "#072447", "gb4": "#86AFCC", "gold-grad": "linear-gradient(135deg,#BED9EA 0%,#447AAB 45%,#072447 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
