"""International Development Bank, as a platform: the data behind ``International_Development_Bank_Platform.html``.

``python customers/build_page.py idb`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``International_Development_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from idb_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from idb_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'IDB'
PAGE = 'International_Development_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "IDB Platform"
KICKER = f"International Development Bank · as at {AS_OF}"
H1 = '<h1>IDB <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: IDB's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in IDB's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in IDB's colours"

PIN = (33.31, 44.37, 'Baghdad')
PIN_FACING = 'Iraq and the Gulf'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail banking', 'corporate': 'Corporate banking', 'invest': 'Treasury & investment banking', 'group': 'Group & central'}
DIV = {'idb': 'International Development Bank', 'iraq': 'IDB Iraq', 'uae': 'IDB UAE (Dubai)', 'cards': 'IDB Cards & acquiring', 'eidb': 'e-IDB'}
DEFAULT_DIV = 'idb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F4", "panel-2": "#F0E6EA", "ink": "#1F0C11", "ink-2": "#412830",
    "muted": "#7A6065", "faint": "#917F83", "line": "#DFD3D5", "line-2": "#CEC1C3", "focus": "#E80028",
    "accent": "#E80028", "link": "#A10012", "gold": "#E80028", "gold-deep": "#82000F", "gold-ink": "#A10012",
    "l1": "#52000A", "l2": "#82000F", "l3": "#B91322", "l4": "#C44760", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#911120", "l2f": "#E80028", "l3f": "#DA3A52", "l4f": "#D392A4",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1F0C11", "shadow": "rgba(50,8,18,.22)", "wash-a": "rgba(232,0,40,.14)",
    "wash-b": "rgba(211,146,164,.10)", "gb2": "#911120", "gb3": "#E80028", "gb4": "#E3ACBD", "brand-grad": "linear-gradient(90deg,#82000F,#E80028 55%,#E3ACBD)",
    "gold-grad": "linear-gradient(135deg,#E3ACBD 0%,#E80028 45%,#82000F 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0A0C", "panel": "#1F1518", "panel-2": "#2F2024", "ink": "#F7F3F5", "ink-2": "#E5DADF",
    "muted": "#C7BCBE", "faint": "#ADA2A4", "line": "#554144", "line-2": "#836A6E", "focus": "#DE889F",
    "accent": "#D57A91", "link": "#E3ACBD", "gold": "#D57A91", "gold-deep": "#DE889F", "gold-ink": "#E3ACBD",
    "l1": "#E3ACBD", "l2": "#DC94A8", "l3": "#E5A0AA", "l4": "#E9BDCA", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#911120", "l2f": "#E80028", "l3f": "#DA3A52", "l4f": "#D392A4",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090507", "wash-a": "rgba(232,0,40,.12)", "wash-b": "rgba(211,146,164,.06)",
    "gb2": "#911120", "gb3": "#E80028", "gb4": "#E3ACBD", "gold-grad": "linear-gradient(135deg,#F2C9D7 0%,#D57A91 45%,#E80028 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
