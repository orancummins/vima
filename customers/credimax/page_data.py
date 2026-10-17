"""CrediMax B.S.C. (c), as a platform: the data behind ``CrediMax_Platform.html``.

``python customers/build_page.py credimax`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``CrediMax_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from credimax_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from credimax_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'CrediMax'
PAGE = 'CrediMax_Platform.html'
AS_OF = "17 October 2026"
TITLE = "CrediMax Platform"
KICKER = f"CrediMax B.S.C. (c) · as at {AS_OF}"
H1 = '<h1>CrediMax <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: CrediMax's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in CrediMax's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in CrediMax's colours"

PIN = (26.23, 50.54, 'Manama')
PIN_FACING = 'Bahrain and the Gulf'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'issuing': 'Card issuing', 'acquiring': 'Merchant acquiring', 'corporate': 'Corporate cards', 'company': 'Company-wide'}
DIV = {'credimax': 'CrediMax', 'bbk': 'BBK Group', 'thameen': 'Thameen', 'tayseer': 'Tayseer', 'cobrand': 'Co-brands', 'gps': 'Global Payment Services'}
DEFAULT_DIV = 'credimax'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F3F5", "panel-2": "#E5E7EB", "ink": "#0C0D14", "ink-2": "#181A1F",
    "muted": "#303036", "faint": "#55565D", "line": "#C6C7CF", "line-2": "#A2A3AE", "focus": "#10143B",
    "accent": "#10143B", "link": "#0E0F34", "gold": "#10143B", "gold-deep": "#0D0E30", "gold-ink": "#0E0F34",
    "l1": "#0A0B26", "l2": "#0D0E30", "l3": "#131333", "l4": "#2E3254", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#121330", "l2f": "#10143B", "l3f": "#2C3064", "l4f": "#6A75A5",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0C0D14", "shadow": "rgba(11,14,27,.22)", "wash-a": "rgba(16,20,59,.14)",
    "wash-b": "rgba(106,117,165,.10)", "gb2": "#121330", "gb3": "#10143B", "gb4": "#8F9BC1", "brand-grad": "linear-gradient(90deg,#0D0E30,#10143B 55%,#8F9BC1)",
    "gold-grad": "linear-gradient(135deg,#8F9BC1 0%,#10143B 45%,#0D0E30 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090A0B", "panel": "#101114", "panel-2": "#15161A", "ink": "#F3F4F6", "ink-2": "#D3D5DA",
    "muted": "#999AA4", "faint": "#72737B", "line": "#232328", "line-2": "#34363B", "focus": "#6976B2",
    "accent": "#6B77AF", "link": "#8F9BC1", "gold": "#6B77AF", "gold-deep": "#6976B2", "gold-ink": "#8F9BC1",
    "l1": "#8F9BC1", "l2": "#707CB0", "l3": "#8285BF", "l4": "#ABB3D1", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#121330", "l2f": "#10143B", "l3f": "#2C3064", "l4f": "#6A75A5",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050607", "wash-a": "rgba(16,20,59,.12)", "wash-b": "rgba(106,117,165,.06)",
    "gb2": "#121330", "gb3": "#10143B", "gb4": "#8F9BC1", "gold-grad": "linear-gradient(135deg,#C4CCE3 0%,#535F9A 45%,#10143B 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
