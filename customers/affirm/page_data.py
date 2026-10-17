"""Affirm Holdings, as a platform: the data behind ``Affirm_Platform.html``.

``python customers/build_page.py affirm`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Affirm_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from affirm_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from affirm_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Affirm'
PAGE = 'Affirm_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Affirm Platform"
KICKER = f"Affirm Holdings · as at {AS_OF}"
H1 = '<h1>Affirm <span class="os">Platform</span></h1>'
SERVES = 'who Affirm serves'

PALETTE_NOTE = ("Palette: Affirm's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Affirm's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Affirm's colours"

PIN = (37.79, -122.39, 'San Francisco')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'merchant': 'Merchant network revenue', 'card': 'Card network revenue', 'interest': 'Interest income', 'loans': 'Loan sales & servicing', 'grp': 'Corporate'}
DIV = {'affirm': 'Affirm, Inc.', 'payments': 'Affirm Payments', 'card': 'Affirm Card & Money', 'canada': 'Affirm Canada', 'intl': 'Affirm U.K. & Australia', 'bank': 'Affirm Bank (proposed)', 'grp': 'Affirm Holdings'}
DEFAULT_DIV = 'affirm'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F4F7", "panel-2": "#E9EBF0", "ink": "#0F1123", "ink-2": "#343950",
    "muted": "#67677D", "faint": "#868694", "line": "#DDDDE5", "line-2": "#CACAD4", "focus": "#4A4AF4",
    "accent": "#4A4AF4", "link": "#170CC8", "gold": "#4A4AF4", "gold-deep": "#120A9E", "gold-ink": "#170CC8",
    "l1": "#0B065F", "l2": "#120A9E", "l3": "#4336DF", "l4": "#8587D1", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#2A21B7", "l2f": "#4A4AF4", "l3f": "#807DDF", "l4f": "#B6BADE",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0F1123", "shadow": "rgba(12,15,57,.22)", "wash-a": "rgba(74,74,244,.14)",
    "wash-b": "rgba(182,186,222,.10)", "gb2": "#2A21B7", "gb3": "#4A4AF4", "gb4": "#C8CDE9", "brand-grad": "linear-gradient(90deg,#120A9E,#4A4AF4 55%,#C8CDE9)",
    "gold-grad": "linear-gradient(135deg,#C8CDE9 0%,#4A4AF4 45%,#120A9E 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0B0C10", "panel": "#191B24", "panel-2": "#282A38", "ink": "#F3F4F7", "ink-2": "#E1E3E8",
    "muted": "#D1D1D8", "faint": "#BFBFC6", "line": "#57576E", "line-2": "#9898A9", "focus": "#B0B5E5",
    "accent": "#A7ABDF", "link": "#C8CDE9", "gold": "#A7ABDF", "gold-deep": "#B0B5E5", "gold-ink": "#C8CDE9",
    "l1": "#C8CDE9", "l2": "#B8BCE4", "l3": "#C2C0EA", "l4": "#D0D4ED", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#2A21B7", "l2f": "#4A4AF4", "l3f": "#807DDF", "l4f": "#B6BADE",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060709", "wash-a": "rgba(74,74,244,.12)", "wash-b": "rgba(182,186,222,.06)",
    "gb2": "#2A21B7", "gb3": "#4A4AF4", "gb4": "#C8CDE9", "gold-grad": "linear-gradient(135deg,#D4D9F3 0%,#A7ABDF 45%,#4A4AF4 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
