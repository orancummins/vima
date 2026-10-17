"""Garanti BBVA, as a platform: the data behind ``Garanti_BBVA_Platform.html``.

``python customers/build_page.py garanti`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Garanti_BBVA_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from garanti_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from garanti_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Garanti BBVA'
PAGE = 'Garanti_BBVA_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Garanti BBVA Platform"
KICKER = f"Türkiye Garanti Bankası A.Ş. (Garanti BBVA) · as at {AS_OF}"
H1 = '<h1>Garanti BBVA <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Garanti BBVA's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Garanti BBVA's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Garanti BBVA's colours"

PIN = (41.08, 29.01, 'Istanbul')
PIN_FACING = 'Turkey and Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail banking', 'sme': 'SME & commercial banking', 'cib': 'Corporate & investment banking', 'pay': 'Payment systems', 'central': 'Finance, treasury & subsidiaries'}
DIV = {'gbbva': 'Garanti BBVA', 'gosas': 'Garanti BBVA Payment Systems (Bonus)', 'tami': 'TAMİ', 'kripto': 'Garanti BBVA Kripto', 'subs': 'Pensions, leasing, factoring & securities', 'gbi': 'Garanti BBVA International', 'romania': 'Garanti BBVA Romania (being sold)'}
DEFAULT_DIV = 'gbbva'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F5F2", "panel-2": "#E7ECE7", "ink": "#0E170F", "ink-2": "#222D23",
    "muted": "#515C53", "faint": "#717A73", "line": "#CED5CF", "line-2": "#B2BCB5", "focus": "#217536",
    "accent": "#217536", "link": "#18572C", "gold": "#217536", "gold-deep": "#154925", "gold-ink": "#18572C",
    "l1": "#0E3219", "l2": "#154925", "l3": "#246239", "l4": "#457E52", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#1F512F", "l2f": "#217536", "l3f": "#408F55", "l4f": "#84B48C",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0E170F", "shadow": "rgba(14,34,17,.22)", "wash-a": "rgba(33,117,54,.14)",
    "wash-b": "rgba(132,180,140,.10)", "gb2": "#1F512F", "gb3": "#217536", "gb4": "#A3CBA7", "brand-grad": "linear-gradient(90deg,#154925,#217536 55%,#A3CBA7)",
    "gold-grad": "linear-gradient(135deg,#A3CBA7 0%,#217536 45%,#154925 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0C0A", "panel": "#131814", "panel-2": "#1C221D", "ink": "#F3F6F3", "ink-2": "#D8DED8",
    "muted": "#ABB4AD", "faint": "#8A928C", "line": "#313933", "line-2": "#49534C", "focus": "#7EBC88",
    "accent": "#6DAF79", "link": "#A3CBA7", "gold": "#6DAF79", "gold-deep": "#7EBC88", "gold-ink": "#A3CBA7",
    "l1": "#A3CBA7", "l2": "#89BD91", "l3": "#98CAA6", "l4": "#B8D8BC", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#1F512F", "l2f": "#217536", "l3f": "#408F55", "l4f": "#84B48C",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060706", "wash-a": "rgba(33,117,54,.12)", "wash-b": "rgba(132,180,140,.06)",
    "gb2": "#1F512F", "gb3": "#217536", "gb4": "#A3CBA7", "gold-grad": "linear-gradient(135deg,#CBE6CE 0%,#6DAF79 45%,#217536 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
