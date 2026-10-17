"""GCB Bank, as a platform: the data behind ``GCB_Bank_Platform.html``.

``python customers/build_page.py gcb`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``GCB_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from gcb_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from gcb_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'GCB'
PAGE = 'GCB_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "GCB Platform"
KICKER = f"GCB Bank PLC · as at {AS_OF}"
H1 = '<h1>GCB <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: GCB's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in GCB's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in GCB's colours"

PIN = (5.55, -0.2, 'Accra')
PIN_FACING = 'Ghana and West Africa'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Personal banking', 'business': 'SME & commercial banking', 'corporate': 'Corporate, SOE & government', 'treasury': 'Treasury & trade'}
DIV = {'gcb': 'GCB Bank PLC', 'personal': 'Personal banking', 'business': 'Business banking', 'private': 'Amber Club & private banking', 'gmoney': 'G-Money Financial Services', 'capital': 'GCB Capital', 'afro': 'Afro-Asia banking'}
DEFAULT_DIV = 'gcb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F7F4F2", "panel-2": "#F1ECE8", "ink": "#231B0D", "ink-2": "#4E4130",
    "muted": "#716B5A", "faint": "#8C8779", "line": "#E4E1DA", "line-2": "#CFCBC1", "focus": "#BE8C00",
    "accent": "#BE8C00", "link": "#816600", "gold": "#BE8C00", "gold-deep": "#9E7E00", "gold-ink": "#816600",
    "l1": "#604C00", "l2": "#9E7E00", "l3": "#E8C31B", "l4": "#D2B672", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#B59516", "l2f": "#FFC72A", "l3f": "#E2C568", "l4f": "#DDCBAC",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#0B0F14", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#231B0D", "shadow": "rgba(57,41,9,.22)", "wash-a": "rgba(255,199,42,.14)",
    "wash-b": "rgba(221,203,172,.10)", "gb2": "#B59516", "gb3": "#FFC72A", "gb4": "#E9D8BF", "brand-grad": "linear-gradient(90deg,#9E7E00,#FFC72A 55%,#E9D8BF)",
    "gold-grad": "linear-gradient(135deg,#E9D8BF 0%,#FFC72A 45%,#9E7E00 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#100E0B", "panel": "#231E18", "panel-2": "#363025", "ink": "#F8F5F3", "ink-2": "#E8E3DF",
    "muted": "#D4D2CB", "faint": "#C1BEB8", "line": "#696350", "line-2": "#A19B8B", "focus": "#FFC72A",
    "accent": "#FFC72A", "link": "#E9D8BF", "gold": "#FFC72A", "gold-deep": "#E6CFA4", "gold-ink": "#E9D8BF",
    "l1": "#E9D8BF", "l2": "#E4D0AD", "l3": "#EBDFB6", "l4": "#EEE0CA", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#B59516", "l2f": "#FFC72A", "l3f": "#E2C568", "l4f": "#DDCBAC",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090706", "wash-a": "rgba(255,199,42,.12)", "wash-b": "rgba(221,203,172,.06)",
    "gb2": "#B59516", "gb3": "#FFC72A", "gb4": "#E9D8BF", "gold-grad": "linear-gradient(135deg,#F4E5D0 0%,#DFC899 45%,#FFC72A 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
