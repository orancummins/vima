"""Deutsche Bank, as a platform: the data behind ``Deutsche_Bank_Platform.html``.

``python customers/build_page.py deutschebank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Deutsche_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from deutschebank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from deutschebank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Deutsche Bank'
PAGE = 'Deutsche_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Deutsche Bank Platform"
KICKER = f"Deutsche Bank AG · as at {AS_OF}"
H1 = '<h1>Deutsche Bank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Deutsche Bank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Deutsche Bank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Deutsche Bank's colours"

PIN = (50.11, 8.67, 'Frankfurt')
PIN_FACING = 'Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'pb': 'Private Bank', 'cb': 'Corporate Bank', 'ib': 'Investment Bank', 'am': 'Asset Management (DWS)', 'group': 'Group, Corporate & Other'}
DIV = {'dbg': 'Deutsche Bank Group', 'db': 'Deutsche Bank', 'postbank': 'Postbank', 'mm': 'Miles & More card', 'ms': 'Merchant Solutions', 'vert': 'Vert (with Fiserv)', 'dws': 'DWS'}
DEFAULT_DIV = 'dbg'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F3F6", "panel-2": "#E5E9EF", "ink": "#0B0F1C", "ink-2": "#202635",
    "muted": "#545769", "faint": "#747685", "line": "#CDCEDA", "line-2": "#B2B5C3", "focus": "#0018A8",
    "accent": "#0018A8", "link": "#000A7A", "gold": "#0018A8", "gold-deep": "#000966", "gold-ink": "#000A7A",
    "l1": "#000644", "l2": "#000966", "l3": "#0E1588", "l4": "#3346A0", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0D156E", "l2f": "#0018A8", "l3f": "#2336BA", "l4f": "#798CC9",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0B0F1C", "shadow": "rgba(7,15,44,.22)", "wash-a": "rgba(0,24,168,.14)",
    "wash-b": "rgba(121,140,201,.10)", "gb2": "#0D156E", "gb3": "#0018A8", "gb4": "#99ACDC", "brand-grad": "linear-gradient(90deg,#000966,#0018A8 55%,#99ACDC)",
    "gold-grad": "linear-gradient(135deg,#99ACDC 0%,#0018A8 45%,#000966 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090B0E", "panel": "#12151B", "panel-2": "#1B1E27", "ink": "#F2F4F7", "ink-2": "#D6DBE2",
    "muted": "#ACAEBB", "faint": "#8D8F9B", "line": "#323441", "line-2": "#4E5060", "focus": "#6D86D7",
    "accent": "#5C74CC", "link": "#99ACDC", "gold": "#5C74CC", "gold-deep": "#6D86D7", "gold-ink": "#99ACDC",
    "l1": "#99ACDC", "l2": "#7C91D4", "l3": "#8A94DF", "l4": "#B0BEE5", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0D156E", "l2f": "#0018A8", "l3f": "#2336BA", "l4f": "#798CC9",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050708", "wash-a": "rgba(0,24,168,.12)", "wash-b": "rgba(121,140,201,.06)",
    "gb2": "#0D156E", "gb3": "#0018A8", "gb4": "#99ACDC", "gold-grad": "linear-gradient(135deg,#C2D0F1 0%,#5C74CC 45%,#0018A8 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
