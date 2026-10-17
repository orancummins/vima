"""CTBC Bank, as a platform: the data behind ``CTBC_Bank_Platform.html``.

``python customers/build_page.py ctbc`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``CTBC_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from ctbc_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from ctbc_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'CTBC'
PAGE = 'CTBC_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "CTBC Platform"
KICKER = f"CTBC Bank · as at {AS_OF}"
H1 = '<h1>CTBC <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: CTBC's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in CTBC's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in CTBC's colours"

PIN = (25.06, 121.61, 'Taipei')
PIN_FACING = 'Taiwan and Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'consumer': 'Consumer banking & cards', 'wealth': 'Wealth management', 'corporate': 'Corporate banking', 'overseas': 'Overseas subsidiaries', 'group': 'Group & central'}
DIV = {'holding': 'CTBC Financial Holding', 'bank': 'CTBC Bank', 'cards': 'CTBC cards', 'tokyostar': 'Tokyo Star Bank', 'lhfg': 'LH Financial Group', 'life': 'Taiwan Life', 'lottery': 'Taiwan Lottery'}
DEFAULT_DIV = 'bank'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F5", "panel-2": "#E4EEEB", "ink": "#0A1918", "ink-2": "#1A2B28",
    "muted": "#405151", "faint": "#637272", "line": "#C8D6D6", "line-2": "#A8BBBB", "focus": "#007979",
    "accent": "#007979", "link": "#00585E", "gold": "#007979", "gold-deep": "#004C51", "gold-ink": "#00585E",
    "l1": "#00373A", "l2": "#004C51", "l3": "#0A5C63", "l4": "#29817E", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0A5054", "l2f": "#007979", "l3f": "#1D9699", "l4f": "#67C2B9",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A1918", "shadow": "rgba(6,39,36,.22)", "wash-a": "rgba(0,121,121,.14)",
    "wash-b": "rgba(103,194,185,.10)", "gb2": "#0A5054", "gb3": "#007979", "gb4": "#8BD8CD", "brand-grad": "linear-gradient(90deg,#004C51,#007979 55%,#8BD8CD)",
    "gold-grad": "linear-gradient(135deg,#8BD8CD 0%,#007979 45%,#004C51 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090D0C", "panel": "#101817", "panel-2": "#172120", "ink": "#F2F7F6", "ink-2": "#D3DFDC",
    "muted": "#A1B1B1", "faint": "#7D8D8D", "line": "#273333", "line-2": "#394646", "focus": "#59D1C7",
    "accent": "#45C5BC", "link": "#8BD8CD", "gold": "#45C5BC", "gold-deep": "#59D1C7", "gold-ink": "#8BD8CD",
    "l1": "#8BD8CD", "l2": "#6ACEC4", "l3": "#7AD8DB", "l4": "#A6E2DA", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0A5054", "l2f": "#007979", "l3f": "#1D9699", "l4f": "#67C2B9",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050807", "wash-a": "rgba(0,121,121,.12)", "wash-b": "rgba(103,194,185,.06)",
    "gb2": "#0A5054", "gb3": "#007979", "gb4": "#8BD8CD", "gold-grad": "linear-gradient(135deg,#BEF0E8 0%,#45C5BC 45%,#007979 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
