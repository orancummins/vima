"""Commonwealth Bank, as a platform: the data behind ``Commonwealth_Bank_Platform.html``.

``python customers/build_page.py cba`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Commonwealth_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from cba_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from cba_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'CommBank'
PAGE = 'Commonwealth_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "CommBank Platform"
KICKER = f"Commonwealth Bank of Australia · as at {AS_OF}"
H1 = '<h1>CommBank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: CommBank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in CommBank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in CommBank's colours"

PIN = (-33.87, 151.21, 'Sydney')
PIN_FACING = 'Australia and New Zealand'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'rbs': 'Retail Banking Services', 'bb': 'Business Banking', 'ibm': 'Institutional Banking and Markets', 'nz': 'New Zealand (ASB)', 'corp': 'Corporate Centre and Other'}
DIV = {'cba': 'Commonwealth Bank group', 'commbank': 'CommBank', 'bankwest': 'Bankwest', 'unloan': 'Unloan', 'commsec': 'CommSec', 'asb': 'ASB', 'merchant': 'CommBank merchant services'}
DEFAULT_DIV = 'cba'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F7F4F2", "panel-2": "#F0ECE7", "ink": "#211A0D", "ink-2": "#463C2A",
    "muted": "#6F6B59", "faint": "#8B8779", "line": "#E0DED6", "line-2": "#CDCBC0", "focus": "#B28F00",
    "accent": "#B28F00", "link": "#7C6A00", "gold": "#B28F00", "gold-deep": "#8C7800", "gold-ink": "#7C6A00",
    "l1": "#574A00", "l2": "#8C7800", "l3": "#CBB514", "l4": "#C9AF56", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#9E8B13", "l2f": "#FFCC00", "l3f": "#DDC34A", "l4f": "#D7C59B",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#0B0F14", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#211A0D", "shadow": "rgba(53,40,8,.22)", "wash-a": "rgba(255,204,0,.14)",
    "wash-b": "rgba(215,197,155,.10)", "gb2": "#9E8B13", "gb3": "#FFCC00", "gb4": "#E5D4B3", "brand-grad": "linear-gradient(90deg,#8C7800,#FFCC00 55%,#E5D4B3)",
    "gold-grad": "linear-gradient(135deg,#E5D4B3 0%,#FFCC00 45%,#8C7800 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0D0A", "panel": "#201D16", "panel-2": "#312C22", "ink": "#F7F5F3", "ink-2": "#E6E1DC",
    "muted": "#CCCAC1", "faint": "#B4B2AA", "line": "#5C5846", "line-2": "#8F8A74", "focus": "#FFCC00",
    "accent": "#FFCC00", "link": "#E5D4B3", "gold": "#FFCC00", "gold-deep": "#E1CA92", "gold-ink": "#E5D4B3",
    "l1": "#E5D4B3", "l2": "#DFCB9D", "l3": "#E7DDA8", "l4": "#EBDDC2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#9E8B13", "l2f": "#FFCC00", "l3f": "#DDC34A", "l4f": "#D7C59B",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090705", "wash-a": "rgba(255,204,0,.12)", "wash-b": "rgba(215,197,155,.06)",
    "gb2": "#9E8B13", "gb3": "#FFCC00", "gb4": "#E5D4B3", "gold-grad": "linear-gradient(135deg,#F3E5CC 0%,#D9C285 45%,#FFCC00 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
