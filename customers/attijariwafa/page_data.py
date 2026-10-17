"""Attijariwafa bank, as a platform: the data behind ``Attijariwafa_Bank_Platform.html``.

``python customers/build_page.py attijariwafa`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Attijariwafa_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from attijariwafa_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from attijariwafa_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Attijariwafa'
PAGE = 'Attijariwafa_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Attijariwafa Platform"
KICKER = f"Attijariwafa bank · as at {AS_OF}"
H1 = '<h1>Attijariwafa <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Attijariwafa's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Attijariwafa's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Attijariwafa's colours"

PIN = (33.59, -7.62, 'Casablanca')
PIN_FACING = 'Morocco and Africa'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'bmeo': 'Banking in Morocco, Europe & offshore', 'sfs': 'Specialised financial subsidiaries', 'irb': 'International retail banking', 'ins': 'Insurance & real estate'}
DIV = {'awb': 'Attijariwafa bank', 'simple': 'Simple', 'apay': 'Attijari Payment', 'wafacash': 'Wafacash', 'wafasalaf': 'Wafasalaf & specialised finance', 'wafaass': 'Wafa Assurance', 'africa': 'Africa subsidiaries'}
DEFAULT_DIV = 'awb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F3F3", "panel-2": "#EFE9EA", "ink": "#1F1010", "ink-2": "#473132",
    "muted": "#9C8D8A", "faint": "#ACA4A3", "line": "#E1DBDA", "line-2": "#D5CECD", "focus": "#E05038",
    "accent": "#E05038", "link": "#A4351A", "gold": "#E05038", "gold-deep": "#822A14", "gold-ink": "#A4351A",
    "l1": "#501A0C", "l2": "#822A14", "l3": "#C35231", "l4": "#C07D74", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#974029", "l2f": "#E05038", "l3f": "#CE7E6E", "l4f": "#D4AEAC",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#1F1010", "shadow": "rgba(49,17,15,.22)", "wash-a": "rgba(224,80,56,.14)",
    "wash-b": "rgba(212,174,172,.10)", "gb2": "#974029", "gb3": "#E05038", "gb4": "#E2C1C0", "brand-grad": "linear-gradient(90deg,#822A14,#E05038 55%,#E2C1C0)",
    "gold-grad": "linear-gradient(135deg,#E2C1C0 0%,#E05038 45%,#822A14 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0B0B", "panel": "#201819", "panel-2": "#322626", "ink": "#F7F3F4", "ink-2": "#E6DFE0",
    "muted": "#D0CAC9", "faint": "#BAB5B4", "line": "#615250", "line-2": "#978885", "focus": "#E05038",
    "accent": "#E05038", "link": "#E2C1C0", "gold": "#E05038", "gold-deep": "#DAA9A6", "gold-ink": "#E2C1C0",
    "l1": "#E2C1C0", "l2": "#DAB1AF", "l3": "#E2BFB8", "l4": "#E8CCCC", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#974029", "l2f": "#E05038", "l3f": "#CE7E6E", "l4f": "#D4AEAC",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080606", "wash-a": "rgba(224,80,56,.12)", "wash-b": "rgba(212,174,172,.06)",
    "gb2": "#974029", "gb3": "#E05038", "gb4": "#E2C1C0", "gold-grad": "linear-gradient(135deg,#EFD3D4 0%,#D29F9B 45%,#E05038 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
