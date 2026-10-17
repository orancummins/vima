"""Klarna Group, as a platform: the data behind ``Klarna_Platform.html``.

``python customers/build_page.py klarna`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Klarna_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from klarna_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from klarna_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Klarna'
PAGE = 'Klarna_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Klarna Platform"
KICKER = f"Klarna Group plc · as at {AS_OF}"
H1 = '<h1>Klarna <span class="os">Platform</span></h1>'
SERVES = 'who Klarna serves'

PALETTE_NOTE = ("Palette: Klarna's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Klarna's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Klarna's colours"

PIN = (59.33, 18.07, 'Stockholm')
PIN_FACING = 'Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'paynow': 'Pay Now', 'paylater': 'Pay Later', 'financing': 'Fair Financing', 'banking': 'Banking & memberships', 'grp': 'Group'}
DIV = {'klarna': 'Klarna', 'bank': 'Klarna Bank AB', 'us': 'Klarna Inc. (US)', 'uk': 'Klarna Financial Services UK', 'pricerunner': 'PriceRunner', 'grp': 'Klarna Group plc'}
DEFAULT_DIV = 'klarna'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F7F3F5", "panel-2": "#F3EBEF", "ink": "#2A101A", "ink-2": "#694052",
    "muted": "#7C636A", "faint": "#938387", "line": "#EBE3E4", "line-2": "#D5C8CC", "focus": "#FF5783",
    "accent": "#FF5783", "link": "#D9002C", "gold": "#FF5783", "gold-deep": "#DA002D", "gold-ink": "#D9002C",
    "l1": "#7E001A", "l2": "#DA002D", "l3": "#F38599", "l4": "#EFCDD7", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#E7385B", "l2f": "#FFB3C7", "l3f": "#F5C9D4", "l4f": "#F3E1E8",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#2A101A", "shadow": "rgba(72,11,32,.22)", "wash-a": "rgba(255,179,199,.14)",
    "wash-b": "rgba(243,225,232,.10)", "gb2": "#E7385B", "gb3": "#FFB3C7", "gb4": "#F7E8EE", "brand-grad": "linear-gradient(90deg,#DA002D,#FFB3C7 55%,#F7E8EE)",
    "gold-grad": "linear-gradient(135deg,#F7E8EE 0%,#FFB3C7 45%,#DA002D 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#120C0F", "panel": "#2B1D23", "panel-2": "#473139", "ink": "#F8F4F6", "ink-2": "#EEE8EB",
    "muted": "#F0EDED", "faint": "#E9E6E6", "line": "#93717A", "line-2": "#DED6D8", "focus": "#FFB3C7",
    "accent": "#FFB3C7", "link": "#F7E8EE", "gold": "#FFB3C7", "gold-deep": "#F6DFE7", "gold-ink": "#F7E8EE",
    "l1": "#F7E8EE", "l2": "#F5E2E9", "l3": "#F8E5E9", "l4": "#F7E6ED", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#E7385B", "l2f": "#FFB3C7", "l3f": "#F5C9D4", "l4f": "#F3E1E8",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#0A0608", "wash-a": "rgba(255,179,199,.12)", "wash-b": "rgba(243,225,232,.06)",
    "gb2": "#E7385B", "gb3": "#FFB3C7", "gb4": "#F7E8EE", "gold-grad": "linear-gradient(135deg,#F7DFE9 0%,#F4DBE3 45%,#FFB3C7 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
