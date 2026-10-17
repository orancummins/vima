"""Truist Financial, as a platform: the data behind ``Truist_Platform.html``.

``python customers/build_page.py truist`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Truist_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from truist_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from truist_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Truist'
PAGE = 'Truist_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Truist Platform"
KICKER = f"Truist Financial Corporation · as at {AS_OF}"
H1 = '<h1>Truist <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Truist's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Truist's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Truist's colours"

PIN = (35.23, -80.84, 'Charlotte')
PIN_FACING = 'the United States'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'csbb': 'Consumer & Small Business Banking', 'wb': 'Wholesale Banking', 'otc': 'Other, Treasury & Corporate'}
DIV = {'tfc': 'Truist Financial', 'bank': 'Truist Bank', 'payments': 'Enterprise Payments', 'lending': 'National Consumer Lending', 'securities': 'Truist Securities', 'wealth': 'Truist Wealth'}
DEFAULT_DIV = 'tfc'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F3F2F4", "panel-2": "#E7E6EB", "ink": "#0F0D14", "ink-2": "#1D1B22",
    "muted": "#3D3A40", "faint": "#615E65", "line": "#CCC9D0", "line-2": "#ACA8B1", "focus": "#2E1A47",
    "accent": "#2E1A47", "link": "#28153A", "gold": "#2E1A47", "gold-deep": "#231333", "gold-ink": "#28153A",
    "l1": "#1A0E27", "l2": "#231333", "l3": "#2D1C3D", "l4": "#47395C", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#281936", "l2f": "#2E1A47", "l3f": "#4F376B", "l4f": "#8777A4",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0F0D14", "shadow": "rgba(19,14,28,.22)", "wash-a": "rgba(46,26,71,.14)",
    "wash-b": "rgba(135,119,164,.10)", "gb2": "#281936", "gb3": "#2E1A47", "gb4": "#A599BF", "brand-grad": "linear-gradient(90deg,#231333,#2E1A47 55%,#A599BF)",
    "gold-grad": "linear-gradient(135deg,#A599BF 0%,#2E1A47 45%,#231333 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0A0B", "panel": "#121115", "panel-2": "#19171C", "ink": "#F4F3F6", "ink-2": "#D6D5DB",
    "muted": "#A3A0A8", "faint": "#7D7A81", "line": "#262428", "line-2": "#39363B", "focus": "#8671AC",
    "accent": "#8671A9", "link": "#A599BF", "gold": "#8671A9", "gold-deep": "#8671AC", "gold-ink": "#A599BF",
    "l1": "#A599BF", "l2": "#8E7DAF", "l3": "#A48DBD", "l4": "#BBB2D0", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#281936", "l2f": "#2E1A47", "l3f": "#4F376B", "l4f": "#8777A4",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060607", "wash-a": "rgba(46,26,71,.12)", "wash-b": "rgba(135,119,164,.06)",
    "gb2": "#281936", "gb3": "#2E1A47", "gb4": "#A599BF", "gold-grad": "linear-gradient(135deg,#D0C9E1 0%,#765F9C 45%,#2E1A47 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
