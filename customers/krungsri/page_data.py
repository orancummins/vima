"""Krungsri (Bank of Ayudhya), as a platform: the data behind ``Krungsri_Platform.html``.

``python customers/build_page.py krungsri`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Krungsri_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from krungsri_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from krungsri_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Krungsri'
PAGE = 'Krungsri_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Krungsri Platform"
KICKER = f"Krungsri (Bank of Ayudhya) · as at {AS_OF}"
H1 = '<h1>Krungsri <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Krungsri's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Krungsri's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Krungsri's colours"

PIN = (13.74, 100.55, 'Bangkok')
PIN_FACING = 'Thailand and ASEAN'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail & Consumer', 'corp': 'Corporate (Thai, MNC & Japanese)', 'sme': 'SME', 'asean': 'ASEAN', 'group': 'Group & Global Markets'}
DIV = {'bay': 'Krungsri', 'kcc': 'Krungsri Consumer', 'central': 'Central The 1 (General Card Services)', 'lotus': "Lotus's Money Services", 'auto': 'Krungsri Auto', 'tidlor': 'Ngern Tid Lor', 'asean': 'ASEAN subsidiaries', 'mufg': 'MUFG'}
DEFAULT_DIV = 'bay'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F7F4F2", "panel-2": "#F0ECE7", "ink": "#211B0D", "ink-2": "#463D2A",
    "muted": "#95907A", "faint": "#A5A297", "line": "#E0DFD6", "line-2": "#D2D0C6", "focus": "#AD9000",
    "accent": "#AD9000", "link": "#776900", "gold": "#AD9000", "gold-deep": "#8C7C00", "gold-ink": "#776900",
    "l1": "#574D00", "l2": "#8C7C00", "l3": "#CBBB14", "l4": "#C9B256", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#9E8F13", "l2f": "#FFD400", "l3f": "#DDC74A", "l4f": "#D7C79B",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#0B0F14", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#211B0D", "shadow": "rgba(53,42,8,.22)", "wash-a": "rgba(255,212,0,.14)",
    "wash-b": "rgba(215,199,155,.10)", "gb2": "#9E8F13", "gb3": "#FFD400", "gb4": "#E5D6B3", "brand-grad": "linear-gradient(90deg,#8C7C00,#FFD400 55%,#E5D6B3)",
    "gold-grad": "linear-gradient(135deg,#E5D6B3 0%,#FFD400 45%,#8C7C00 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0D0A", "panel": "#201D16", "panel-2": "#312D22", "ink": "#F7F5F3", "ink-2": "#E6E2DC",
    "muted": "#CCCAC1", "faint": "#B4B2AA", "line": "#5C5946", "line-2": "#8F8A74", "focus": "#FFD400",
    "accent": "#FFD400", "link": "#E5D6B3", "gold": "#FFD400", "gold-deep": "#E1CD92", "gold-ink": "#E5D6B3",
    "l1": "#E5D6B3", "l2": "#DFCD9D", "l3": "#E7DFA8", "l4": "#EBDFC2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#9E8F13", "l2f": "#FFD400", "l3f": "#DDC74A", "l4f": "#D7C79B",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090705", "wash-a": "rgba(255,212,0,.12)", "wash-b": "rgba(215,199,155,.06)",
    "gb2": "#9E8F13", "gb3": "#FFD400", "gb4": "#E5D6B3", "gold-grad": "linear-gradient(135deg,#F3E6CC 0%,#D9C585 45%,#FFD400 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
