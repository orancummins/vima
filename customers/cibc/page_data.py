"""Canadian Imperial Bank of Commerce, as a platform: the data behind ``CIBC_Platform.html``.

``python customers/build_page.py cibc`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``CIBC_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from cibc_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from cibc_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'CIBC'
PAGE = 'CIBC_Platform.html'
AS_OF = "17 October 2026"
TITLE = "CIBC Platform"
KICKER = f"Canadian Imperial Bank of Commerce · as at {AS_OF}"
H1 = '<h1>CIBC <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: CIBC's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in CIBC's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in CIBC's colours"

PIN = (43.65, -79.38, 'Toronto')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'cpbb': 'Canadian Personal & Business Banking', 'ccbwm': 'Canadian Commercial Banking & Wealth', 'us': 'U.S. Commercial Banking & Wealth', 'cm': 'Capital Markets', 'corp': 'Corporate & Other'}
DIV = {'group': 'CIBC', 'canada': 'CIBC (Canada)', 'simplii': 'Simplii Financial', 'usa': 'CIBC Bank USA', 'wealth': 'CIBC Wealth', 'cm': 'CIBC Capital Markets', 'caribbean': 'CIBC Caribbean'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F4", "panel-2": "#EEE8EB", "ink": "#1C0F13", "ink-2": "#3D2B31",
    "muted": "#766468", "faint": "#8F8286", "line": "#DDD4D6", "line-2": "#CBC1C3", "focus": "#C41F3E",
    "accent": "#C41F3E", "link": "#881624", "gold": "#C41F3E", "gold-deep": "#6E111D", "gold-ink": "#881624",
    "l1": "#460B13", "l2": "#6E111D", "l3": "#9F2835", "l4": "#B25569", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#7D222E", "l2f": "#C41F3E", "l3f": "#C34D60", "l4f": "#C999A7",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1C0F13", "shadow": "rgba(44,13,21,.22)", "wash-a": "rgba(196,31,62,.14)",
    "wash-b": "rgba(201,153,167,.10)", "gb2": "#7D222E", "gb3": "#C41F3E", "gb4": "#DBB2BF", "brand-grad": "linear-gradient(90deg,#6E111D,#C41F3E 55%,#DBB2BF)",
    "gold-grad": "linear-gradient(135deg,#DBB2BF 0%,#C41F3E 45%,#6E111D 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0E0B0C", "panel": "#1D1619", "panel-2": "#2C2225", "ink": "#F7F3F5", "ink-2": "#E3DCDF",
    "muted": "#C5BCBE", "faint": "#AAA2A4", "line": "#514245", "line-2": "#7D6B6E", "focus": "#D292A4",
    "accent": "#C88596", "link": "#DBB2BF", "gold": "#C88596", "gold-deep": "#D292A4", "gold-ink": "#DBB2BF",
    "l1": "#DBB2BF", "l2": "#D29CAC", "l3": "#DBA8B0", "l4": "#E3C2CD", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#7D222E", "l2f": "#C41F3E", "l3f": "#C34D60", "l4f": "#C999A7",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080607", "wash-a": "rgba(196,31,62,.12)", "wash-b": "rgba(201,153,167,.06)",
    "gb2": "#7D222E", "gb3": "#C41F3E", "gb4": "#DBB2BF", "gold-grad": "linear-gradient(135deg,#EDCED9 0%,#C88596 45%,#C41F3E 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
