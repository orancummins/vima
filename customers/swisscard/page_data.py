"""Swisscard AECS, as a platform: the data behind ``Swisscard_Platform.html``.

``python customers/build_page.py swisscard`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Swisscard_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from swisscard_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from swisscard_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Swisscard'
PAGE = 'Swisscard_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Swisscard Platform"
KICKER = f"Swisscard AECS GmbH · as at {AS_OF}"
H1 = '<h1>Swisscard <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Swisscard's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Swisscard's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Swisscard's colours"

PIN = (47.26, 8.6, 'Horgen')
PIN_FACING = 'Switzerland and Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'private': 'Private customers', 'business': 'Business customers', 'banks': 'Private banks', 'merchants': 'Merchants', 'company': 'Company-wide'}
DIV = {'swisscard': 'Swisscard AECS', 'amex': 'American Express', 'swiss': 'SWISS Miles & More', 'cashback': 'Cashback Cards', 'poinz': 'poinz Cards', 'free': 'swisscard card'}
DEFAULT_DIV = 'swisscard'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F4F4", "panel-2": "#E7EAEB", "ink": "#0F1214", "ink-2": "#202426",
    "muted": "#45484B", "faint": "#686B6D", "line": "#CCCFD1", "line-2": "#AEB1B5", "focus": "#263C53",
    "accent": "#263C53", "link": "#1D2C40", "gold": "#263C53", "gold-deep": "#192637", "gold-ink": "#1D2C40",
    "l1": "#121C28", "l2": "#192637", "l3": "#263347", "l4": "#455565", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#212D3D", "l2f": "#263C53", "l3f": "#445A72", "l4f": "#8397A5",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0F1214", "shadow": "rgba(16,23,28,.22)", "wash-a": "rgba(38,60,83,.14)",
    "wash-b": "rgba(131,151,165,.10)", "gb2": "#212D3D", "gb3": "#263C53", "gb4": "#A3B5BF", "brand-grad": "linear-gradient(90deg,#192637,#263C53 55%,#A3B5BF)",
    "gold-grad": "linear-gradient(135deg,#A3B5BF 0%,#263C53 45%,#192637 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0B0C", "panel": "#131516", "panel-2": "#1A1D1E", "ink": "#F3F5F5", "ink-2": "#D7DADB",
    "muted": "#A6A9AC", "faint": "#828588", "line": "#2A2D2F", "line-2": "#3D4042", "focus": "#7F99AC",
    "accent": "#6D889D", "link": "#A3B5BF", "gold": "#6D889D", "gold-deep": "#7F99AC", "gold-ink": "#A3B5BF",
    "l1": "#A3B5BF", "l2": "#899FAF", "l3": "#99A9BC", "l4": "#B9C7CF", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#212D3D", "l2f": "#263C53", "l3f": "#445A72", "l4f": "#8397A5",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060707", "wash-a": "rgba(38,60,83,.12)", "wash-b": "rgba(131,151,165,.06)",
    "gb2": "#212D3D", "gb3": "#263C53", "gb4": "#A3B5BF", "gold-grad": "linear-gradient(135deg,#CDD9E0 0%,#6D889D 45%,#263C53 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
