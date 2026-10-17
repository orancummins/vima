"""UniCredit, as a platform: the data behind ``UniCredit_Platform.html``.

``python customers/build_page.py unicredit`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``UniCredit_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from unicredit_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from unicredit_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'UniCredit'
PAGE = 'UniCredit_Platform.html'
AS_OF = "17 October 2026"
TITLE = "UniCredit Platform"
KICKER = f"UniCredit S.p.A. · as at {AS_OF}"
H1 = '<h1>UniCredit <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: UniCredit's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in UniCredit's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in UniCredit's colours"

PIN = (45.48, 9.19, 'Milan')
PIN_FACING = 'Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'italy': 'Italy', 'germany': 'Germany', 'austria': 'Austria', 'cee': 'Central & Eastern Europe', 'group': 'Group functions & centre'}
DIV = {'ucg': 'UniCredit Group', 'italy': 'UniCredit (Italy)', 'hvb': 'HypoVereinsbank', 'ba': 'Bank Austria', 'cee': 'UniCredit CEE banks', 'buddy': 'buddy', 'onemarkets': 'onemarkets', 'vodeno': 'Vodeno & UniCredit NV/SA'}
DEFAULT_DIV = 'ucg'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F3", "panel-2": "#EFE8EA", "ink": "#1E0E10", "ink-2": "#422D30",
    "muted": "#917A7A", "faint": "#A29797", "line": "#DFD6D6", "line-2": "#D0C6C6", "focus": "#E31818",
    "accent": "#E31818", "link": "#9C1910", "gold": "#E31818", "gold-deep": "#7D140D", "gold-ink": "#9C1910",
    "l1": "#4E0C08", "l2": "#7D140D", "l3": "#B73125", "l4": "#BD5E61", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#8F2720", "l2f": "#E31818", "l3f": "#CE5956", "l4f": "#D09FA4",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#1E0E10", "shadow": "rgba(48,12,15,.22)", "wash-a": "rgba(227,24,24,.14)",
    "wash-b": "rgba(208,159,164,.10)", "gb2": "#8F2720", "gb3": "#E31818", "gb4": "#E0B7BC", "brand-grad": "linear-gradient(90deg,#7D140D,#E31818 55%,#E0B7BC)",
    "gold-grad": "linear-gradient(135deg,#E0B7BC 0%,#E31818 45%,#7D140D 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0E0B0B", "panel": "#1F1718", "panel-2": "#2F2325", "ink": "#F7F3F4", "ink-2": "#E5DDDF",
    "muted": "#CAC1C1", "faint": "#B2AAAA", "line": "#594848", "line-2": "#8B7575", "focus": "#D9989E",
    "accent": "#D08B91", "link": "#E0B7BC", "gold": "#D08B91", "gold-deep": "#D9989E", "gold-ink": "#E0B7BC",
    "l1": "#E0B7BC", "l2": "#D8A2A7", "l3": "#E1AEAD", "l4": "#E7C5C9", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#8F2720", "l2f": "#E31818", "l3f": "#CE5956", "l4f": "#D09FA4",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080607", "wash-a": "rgba(227,24,24,.12)", "wash-b": "rgba(208,159,164,.06)",
    "gb2": "#8F2720", "gb3": "#E31818", "gb4": "#E0B7BC", "gold-grad": "linear-gradient(135deg,#EFCFD4 0%,#D08B91 45%,#E31818 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
