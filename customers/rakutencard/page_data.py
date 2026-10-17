"""Rakuten Card, as a platform: the data behind ``Rakuten_Card_Platform.html``.

``python customers/build_page.py rakutencard`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Rakuten_Card_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from rakutencard_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from rakutencard_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Rakuten Card'
PAGE = 'Rakuten_Card_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Rakuten Card Platform"
KICKER = f"Rakuten Card Co., Ltd. · as at {AS_OF}"
H1 = '<h1>Rakuten Card <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Rakuten Card's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Rakuten Card's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Rakuten Card's colours"

PIN = (35.66, 139.72, 'Tokyo')
PIN_FACING = 'Japan and Asia-Pacific'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'card': 'Rakuten Card', 'bank': 'Rakuten Bank', 'securities': 'Rakuten Securities', 'payment': 'Rakuten Payment', 'other': 'Others & group'}
DIV = {'rcard': 'Rakuten Card', 'rbank': 'Rakuten Bank', 'rgroup': 'Rakuten Group', 'mizuho': 'Mizuho partnership', 'rpay': 'Rakuten Payment', 'rsec': 'Rakuten Securities', 'taiwan': 'Taiwan Rakuten Card'}
DEFAULT_DIV = 'rcard'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F1F3", "panel-2": "#EFE5E8", "ink": "#1D0B0D", "ink-2": "#392326",
    "muted": "#755D5D", "faint": "#8E7D7D", "line": "#DBCFCF", "line-2": "#C7B8B8", "focus": "#BF0000",
    "accent": "#BF0000", "link": "#880800", "gold": "#BF0000", "gold-deep": "#700600", "gold-ink": "#880800",
    "l1": "#490400", "l2": "#700600", "l3": "#991A0F", "l4": "#AF383B", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#7B150F", "l2f": "#BF0000", "l3f": "#CB2A27", "l4f": "#CD8289",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1D0B0D", "shadow": "rgba(46,7,10,.22)", "wash-a": "rgba(191,0,0,.14)",
    "wash-b": "rgba(205,130,137,.10)", "gb2": "#7B150F", "gb3": "#BF0000", "gb4": "#DFA0A9", "brand-grad": "linear-gradient(90deg,#700600,#BF0000 55%,#DFA0A9)",
    "gold-grad": "linear-gradient(135deg,#DFA0A9 0%,#BF0000 45%,#700600 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0E0A0A", "panel": "#1C1315", "panel-2": "#2A1D1E", "ink": "#F7F2F4", "ink-2": "#E3D8DA",
    "muted": "#BFB2B2", "faint": "#A19595", "line": "#483737", "line-2": "#6C5858", "focus": "#DA7780",
    "accent": "#CF676E", "link": "#DFA0A9", "gold": "#CF676E", "gold-deep": "#DA7780", "gold-ink": "#DFA0A9",
    "l1": "#DFA0A9", "l2": "#D7858D", "l3": "#E19592", "l4": "#E7B4BB", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#7B150F", "l2f": "#BF0000", "l3f": "#CB2A27", "l4f": "#CD8289",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080506", "wash-a": "rgba(191,0,0,.12)", "wash-b": "rgba(205,130,137,.06)",
    "gb2": "#7B150F", "gb3": "#BF0000", "gb4": "#DFA0A9", "gold-grad": "linear-gradient(135deg,#F1C5CC 0%,#CF676E 45%,#BF0000 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
