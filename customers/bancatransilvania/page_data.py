"""Banca Transilvania, as a platform: the data behind ``Banca_Transilvania_Platform.html``.

``python customers/build_page.py bancatransilvania`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Banca_Transilvania_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bancatransilvania_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bancatransilvania_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BT'
PAGE = 'Banca_Transilvania_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BT Platform"
KICKER = f"Banca Transilvania · as at {AS_OF}"
H1 = '<h1>BT <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BT's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BT's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BT's colours"

PIN = (46.77, 23.6, 'Cluj-Napoca')
PIN_FACING = 'Romania and Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail', 'sme': 'Micro & SME', 'corp': 'Mid & Large Corporate', 'treasury': 'Treasury & group', 'nbfi': 'Leasing & consumer finance'}
DIV = {'group': 'BT Financial Group', 'bt': 'Banca Transilvania', 'salt': 'Salt Bank', 'victoriabank': 'Victoriabank', 'leasing': 'BT Leasing, BT Direct & BT Mic', 'invest': 'BT Asset Management & BT Capital Partners', 'pensii': 'BT Pensii'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F7F4F2", "panel-2": "#F0ECE7", "ink": "#211A0D", "ink-2": "#493D2D",
    "muted": "#9D9684", "faint": "#ABA89F", "line": "#E2DFD8", "line-2": "#D5D3CA", "focus": "#BB8B01",
    "accent": "#BB8B01", "link": "#816801", "gold": "#BB8B01", "gold-deep": "#937601", "gold-ink": "#816801",
    "l1": "#5B4800", "l2": "#937601", "l3": "#D9B717", "l4": "#CDAF63", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#A88B15", "l2f": "#FEC214", "l3f": "#DFBF58", "l4f": "#DAC6A3",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#0B0F14", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#211A0D", "shadow": "rgba(55,39,8,.22)", "wash-a": "rgba(254,194,20,.14)",
    "wash-b": "rgba(218,198,163,.10)", "gb2": "#A88B15", "gb3": "#FEC214", "gb4": "#E7D5B9", "brand-grad": "linear-gradient(90deg,#937601,#FEC214 55%,#E7D5B9)",
    "gold-grad": "linear-gradient(135deg,#E7D5B9 0%,#FEC214 45%,#937601 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0D0B", "panel": "#211D17", "panel-2": "#342E24", "ink": "#F7F5F3", "ink-2": "#E7E2DD",
    "muted": "#D0CDC6", "faint": "#BAB7B0", "line": "#625C4B", "line-2": "#97917F", "focus": "#FEC214",
    "accent": "#FEC214", "link": "#E7D5B9", "gold": "#FEC214", "gold-deep": "#E3CA9B", "gold-ink": "#E7D5B9",
    "l1": "#E7D5B9", "l2": "#E1CCA5", "l3": "#E9DCAF", "l4": "#ECDDC6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#A88B15", "l2f": "#FEC214", "l3f": "#DFBF58", "l4f": "#DAC6A3",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090706", "wash-a": "rgba(254,194,20,.12)", "wash-b": "rgba(218,198,163,.06)",
    "gb2": "#A88B15", "gb3": "#FEC214", "gb4": "#E7D5B9", "gold-grad": "linear-gradient(135deg,#F3E4CE 0%,#DBC28F 45%,#FEC214 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
