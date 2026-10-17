"""Walmart Inc., as a platform: the data behind ``Walmart_Platform.html``.

``python customers/build_page.py walmart`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Walmart_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from walmart_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from walmart_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Walmart'
PAGE = 'Walmart_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Walmart Platform"
KICKER = f"Walmart Inc., read through payments · as at {AS_OF}"
H1 = '<h1>Walmart <span class="os">Platform</span></h1>'
SERVES = 'who Walmart serves'

PALETTE_NOTE = ("Palette: Walmart's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Walmart's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Walmart's colours"

PIN = (36.37, -94.21, 'Bentonville')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'us': 'Walmart U.S.', 'intl': 'Walmart International', 'sams': "Sam's Club U.S.", 'grp': 'Corporate'}
DIV = {'walmart': 'Walmart', 'onepay': 'OnePay', 'sams': "Sam's Club", 'india': 'Flipkart & PhonePe', 'walmex': 'Walmex', 'intl': 'Other markets', 'grp': 'Walmart Inc.'}
DEFAULT_DIV = 'walmart'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F5F6", "panel-2": "#E6ECEF", "ink": "#0C151F", "ink-2": "#273440",
    "muted": "#616A7A", "faint": "#808791", "line": "#D3D7DE", "line-2": "#BFC4CD", "focus": "#0053E2",
    "accent": "#0053E2", "link": "#00309D", "gold": "#0053E2", "gold-deep": "#00277F", "gold-ink": "#00309D",
    "l1": "#001951", "l2": "#00277F", "l3": "#1241B4", "l4": "#4375C3", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#11378E", "l2f": "#0053E2", "l3f": "#366ED9", "l4f": "#90AFD2",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0C151F", "shadow": "rgba(7,26,50,.22)", "wash-a": "rgba(0,83,226,.14)",
    "wash-b": "rgba(144,175,210,.10)", "gb2": "#11378E", "gb3": "#0053E2", "gb4": "#AAC7E2", "brand-grad": "linear-gradient(90deg,#00277F,#0053E2 55%,#AAC7E2)",
    "gold-grad": "linear-gradient(135deg,#AAC7E2 0%,#0053E2 45%,#00277F 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0C0F", "panel": "#151A1F", "panel-2": "#1F272E", "ink": "#F3F6F7", "ink-2": "#DAE0E4",
    "muted": "#BABFC6", "faint": "#A0A5AC", "line": "#404753", "line-2": "#677080", "focus": "#86AEDE",
    "accent": "#77A0D5", "link": "#AAC7E2", "gold": "#77A0D5", "gold-deep": "#86AEDE", "gold-ink": "#AAC7E2",
    "l1": "#AAC7E2", "l2": "#92B4DB", "l3": "#9EB6E4", "l4": "#BCD2E9", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#11378E", "l2f": "#0053E2", "l3f": "#366ED9", "l4f": "#90AFD2",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050809", "wash-a": "rgba(0,83,226,.12)", "wash-b": "rgba(144,175,210,.06)",
    "gb2": "#11378E", "gb3": "#0053E2", "gb4": "#AAC7E2", "gold-grad": "linear-gradient(135deg,#C9DEF2 0%,#77A0D5 45%,#0053E2 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
