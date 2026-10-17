"""Synchrony, as a platform: the data behind ``Synchrony_Platform.html``.

``python customers/build_page.py synchrony`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Synchrony_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from synchrony_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from synchrony_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Synchrony'
PAGE = 'Synchrony_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Synchrony Platform"
KICKER = f"Synchrony Financial · as at {AS_OF}"
H1 = '<h1>Synchrony <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Synchrony's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Synchrony's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Synchrony's colours"

PIN = (41.05, -73.54, 'Stamford')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'home': 'Home & Auto', 'digital': 'Digital', 'dv': 'Diversified & Value', 'health': 'Health & Wellness', 'life': 'Lifestyle', 'grp': 'Corporate'}
DIV = {'syf': 'Synchrony', 'carecredit': 'CareCredit', 'bank': 'Synchrony Bank', 'grp': 'Synchrony Financial'}
DEFAULT_DIV = 'syf'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F7F5F2", "panel-2": "#F1EDE9", "ink": "#241D0E", "ink-2": "#544733",
    "muted": "#706B59", "faint": "#8D887C", "line": "#E6E4DD", "line-2": "#CFCCC2", "focus": "#B98E00",
    "accent": "#B98E00", "link": "#7F6900", "gold": "#B98E00", "gold-deep": "#AC8E00", "gold-ink": "#7F6900",
    "l1": "#675500", "l2": "#AC8E00", "l3": "#EBCF33", "l4": "#D9C386", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#C6A918", "l2f": "#FFD549", "l3f": "#E6D17E", "l4f": "#E2D4B8",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#0B0F14", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#241D0E", "shadow": "rgba(61,45,9,.22)", "wash-a": "rgba(255,213,73,.14)",
    "wash-b": "rgba(226,212,184,.10)", "gb2": "#C6A918", "gb3": "#FFD549", "gb4": "#EDDFC9", "brand-grad": "linear-gradient(90deg,#AC8E00,#FFD549 55%,#EDDFC9)",
    "gold-grad": "linear-gradient(135deg,#EDDFC9 0%,#FFD549 45%,#AC8E00 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#100E0B", "panel": "#252019", "panel-2": "#3A3428", "ink": "#F8F5F3", "ink-2": "#E9E5E1",
    "muted": "#DBD9D3", "faint": "#CAC8C2", "line": "#736D58", "line-2": "#AFAB9C", "focus": "#FFD549",
    "accent": "#FFD549", "link": "#EDDFC9", "gold": "#FFD549", "gold-deep": "#EAD8B1", "gold-ink": "#EDDFC9",
    "l1": "#EDDFC9", "l2": "#E8D9B9", "l3": "#EEE5C1", "l4": "#F0E5D1", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#C6A918", "l2f": "#FFD549", "l3f": "#E6D17E", "l4f": "#E2D4B8",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090706", "wash-a": "rgba(255,213,73,.12)", "wash-b": "rgba(226,212,184,.06)",
    "gb2": "#C6A918", "gb3": "#FFD549", "gb4": "#EDDFC9", "gold-grad": "linear-gradient(135deg,#F5E8D3 0%,#E4D2A8 45%,#FFD549 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
