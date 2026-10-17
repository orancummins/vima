"""BAC, as a platform: the data behind ``BAC_Platform.html``.

``python customers/build_page.py bac`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``BAC_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bac_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bac_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BAC'
PAGE = 'BAC_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BAC Platform"
KICKER = f"BAC International Bank · as at {AS_OF}"
H1 = '<h1>BAC <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BAC's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BAC's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BAC's colours"

PIN = (9.93, -84.08, 'San José')
PIN_FACING = 'Central America'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'consumer': 'Consumer & cards', 'corporate': 'Corporate & SME', 'mortgage': 'Mortgages', 'central': 'Treasury & central'}
DIV = {'bac': 'BAC regional', 'cr': 'BAC Costa Rica', 'pa': 'BAC Panamá (with Multibank)', 'gt': 'BAC Guatemala', 'hn': 'BAC Honduras', 'sv': 'BAC El Salvador', 'ni': 'BAC Nicaragua'}
DEFAULT_DIV = 'bac'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F4", "panel-2": "#EFE6EA", "ink": "#1F0C12", "ink-2": "#402730",
    "muted": "#7B6266", "faint": "#928184", "line": "#DED3D5", "line-2": "#CDC0C2", "focus": "#E4002B",
    "accent": "#E4002B", "link": "#9E0015", "gold": "#E4002B", "gold-deep": "#800011", "gold-ink": "#9E0015",
    "l1": "#51000B", "l2": "#800011", "l3": "#B61224", "l4": "#C34460", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#8F1121", "l2f": "#E4002B", "l3f": "#D93752", "l4f": "#D390A3",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1F0C12", "shadow": "rgba(50,7,19,.22)", "wash-a": "rgba(228,0,43,.14)",
    "wash-b": "rgba(211,144,163,.10)", "gb2": "#8F1121", "gb3": "#E4002B", "gb4": "#E2ABBD", "brand-grad": "linear-gradient(90deg,#800011,#E4002B 55%,#E2ABBD)",
    "gold-grad": "linear-gradient(135deg,#E2ABBD 0%,#E4002B 45%,#800011 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0A0C", "panel": "#1F1518", "panel-2": "#2E2024", "ink": "#F7F3F5", "ink-2": "#E4DADF",
    "muted": "#C7BBBD", "faint": "#ACA1A3", "line": "#544044", "line-2": "#81686D", "focus": "#DE879F",
    "accent": "#D57891", "link": "#E2ABBD", "gold": "#D57891", "gold-deep": "#DE879F", "gold-ink": "#E2ABBD",
    "l1": "#E2ABBD", "l2": "#DC93A8", "l3": "#E59FAA", "l4": "#E9BCCB", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#8F1121", "l2f": "#E4002B", "l3f": "#D93752", "l4f": "#D390A3",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090507", "wash-a": "rgba(228,0,43,.12)", "wash-b": "rgba(211,144,163,.06)",
    "gb2": "#8F1121", "gb3": "#E4002B", "gb4": "#E2ABBD", "gold-grad": "linear-gradient(135deg,#F2C9D7 0%,#D57891 45%,#E4002B 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
