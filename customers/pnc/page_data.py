"""PNC Financial Services Group, as a platform: the data behind ``PNC_Platform.html``.

``python customers/build_page.py pnc`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``PNC_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from pnc_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from pnc_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'PNC'
PAGE = 'PNC_Platform.html'
AS_OF = "17 October 2026"
TITLE = "PNC Platform"
KICKER = f"PNC Financial Services Group · as at {AS_OF}"
H1 = '<h1>PNC <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: PNC's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in PNC's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in PNC's colours"

PIN = (40.44, -80.0, 'Pittsburgh')
PIN_FACING = 'the United States'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail Banking', 'cib': 'Corporate & Institutional Banking', 'amg': 'Asset Management Group', 'other': 'Other'}
DIV = {'pnc': 'PNC Financial Services Group', 'bank': 'PNC Bank', 'firstbank': 'FirstBank (now PNC)', 'tm': 'PNC Treasury Management', 'merchant': 'PNC Merchant Services', 'wealth': 'PNC Wealth Management & Private Bank', 'hw': 'Harris Williams'}
DEFAULT_DIV = 'pnc'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F3F2", "panel-2": "#F0E9E8", "ink": "#21140E", "ink-2": "#4A362F",
    "muted": "#73685E", "faint": "#8F857F", "line": "#E2DDD9", "line-2": "#CFC9C4", "focus": "#F06F0B",
    "accent": "#F06F0B", "link": "#A25507", "gold": "#F06F0B", "gold-deep": "#914B07", "gold-ink": "#A25507",
    "l1": "#592E04", "l2": "#914B07", "l3": "#D77E1F", "l4": "#CA936C", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#A6611B", "l2f": "#F58025", "l3f": "#DB9A63", "l4f": "#D9B9A8",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#21140E", "shadow": "rgba(54,26,10,.22)", "wash-a": "rgba(245,128,37,.14)",
    "wash-b": "rgba(217,185,168,.10)", "gb2": "#A6611B", "gb3": "#F58025", "gb4": "#E6C9BD", "brand-grad": "linear-gradient(90deg,#914B07,#F58025 55%,#E6C9BD)",
    "gold-grad": "linear-gradient(135deg,#E6C9BD 0%,#F58025 45%,#914B07 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0C0B", "panel": "#211A18", "panel-2": "#342A25", "ink": "#F7F4F3", "ink-2": "#E7E0DE",
    "muted": "#D1CCC8", "faint": "#BCB7B3", "line": "#64574E", "line-2": "#9A8D84", "focus": "#F58025",
    "accent": "#F58025", "link": "#E6C9BD", "gold": "#F58025", "gold-deep": "#E1B7A1", "gold-ink": "#E6C9BD",
    "l1": "#E6C9BD", "l2": "#E0BCAA", "l3": "#E7CCB4", "l4": "#EBD3C9", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#A6611B", "l2f": "#F58025", "l3f": "#DB9A63", "l4f": "#D9B9A8",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090606", "wash-a": "rgba(245,128,37,.12)", "wash-b": "rgba(217,185,168,.06)",
    "gb2": "#A6611B", "gb3": "#F58025", "gb4": "#E6C9BD", "gold-grad": "linear-gradient(135deg,#F2DAD0 0%,#DAAE95 45%,#F58025 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
