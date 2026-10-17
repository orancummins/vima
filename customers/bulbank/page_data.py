"""UniCredit Bulbank, as a platform: the data behind ``UniCredit_Bulbank_Platform.html``.

``python customers/build_page.py bulbank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``UniCredit_Bulbank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bulbank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bulbank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Bulbank'
PAGE = 'UniCredit_Bulbank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Bulbank Platform"
KICKER = f"UniCredit Bulbank · as at {AS_OF}"
H1 = '<h1>Bulbank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Bulbank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Bulbank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Bulbank's colours"

PIN = (42.7, 23.32, 'Sofia')
PIN_FACING = 'Bulgaria and the euro area'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'corporate': 'Corporate Banking', 'retail': 'Retail Banking', 'private': 'Private Banking', 'subs': 'Consumer finance & leasing', 'centre': 'Treasury & centre'}
DIV = {'ucb': 'UniCredit Bulbank', 'ucg': 'UniCredit Group', 'ucfin': 'UniCredit Consumer Financing', 'leasing': 'UniCredit Leasing & Fleet Management', 'factoring': 'UniCredit Factoring', 'broker': 'UniCredit Insurance Broker'}
DEFAULT_DIV = 'ucb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F3", "panel-2": "#EFE8EA", "ink": "#1F0F11", "ink-2": "#442E32",
    "muted": "#776464", "faint": "#8F8282", "line": "#E0D7D8", "line-2": "#D2C8C8", "focus": "#E51E26",
    "accent": "#E51E26", "link": "#9F1512", "gold": "#E51E26", "gold-deep": "#7F110F", "gold-ink": "#9F1512",
    "l1": "#4F0A09", "l2": "#7F110F", "l3": "#BB2E28", "l4": "#BE646A", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#922422", "l2f": "#E51E26", "l3f": "#CE5C5E", "l4f": "#D1A3A9",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#1F0F11", "shadow": "rgba(49,13,17,.22)", "wash-a": "rgba(229,30,38,.14)",
    "wash-b": "rgba(209,163,169,.10)", "gb2": "#922422", "gb3": "#E51E26", "gb4": "#E0B9C0", "brand-grad": "linear-gradient(90deg,#7F110F,#E51E26 55%,#E0B9C0)",
    "gold-grad": "linear-gradient(135deg,#E0B9C0 0%,#E51E26 45%,#7F110F 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0B0C", "panel": "#1F1719", "panel-2": "#302426", "ink": "#F7F3F4", "ink-2": "#E5DDDF",
    "muted": "#CCC3C4", "faint": "#B4ACAD", "line": "#5B4A4A", "line-2": "#8E797A", "focus": "#DA9CA4",
    "accent": "#D19097", "link": "#E0B9C0", "gold": "#D19097", "gold-deep": "#DA9CA4", "gold-ink": "#E0B9C0",
    "l1": "#E0B9C0", "l2": "#D9A5AD", "l3": "#E1B0B0", "l4": "#E7C7CC", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#922422", "l2f": "#E51E26", "l3f": "#CE5C5E", "l4f": "#D1A3A9",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080607", "wash-a": "rgba(229,30,38,.12)", "wash-b": "rgba(209,163,169,.06)",
    "gb2": "#922422", "gb3": "#E51E26", "gb4": "#E0B9C0", "gold-grad": "linear-gradient(135deg,#EFD0D6 0%,#D19097 45%,#E51E26 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
