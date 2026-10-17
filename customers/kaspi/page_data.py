"""Kaspi.kz, as a platform: the data behind ``Kaspi_kz_Platform.html``.

``python customers/build_page.py kaspi`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Kaspi_kz_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from kaspi_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from kaspi_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Kaspi.kz'
PAGE = 'Kaspi_kz_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Kaspi.kz Platform"
KICKER = f"Kaspi.kz, Kazakhstan's payments, marketplace and fintech super-app · as at {AS_OF}"
H1 = '<h1>Kaspi.kz <span class="os">Platform</span></h1>'
SERVES = 'who Kaspi serves'

PALETTE_NOTE = ("Palette: Kaspi.kz's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Kaspi.kz's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Kaspi.kz's colours"

PIN = (43.24, 76.95, 'Almaty')
PIN_FACING = 'Central Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'pay': 'Payments', 'mkt': 'Marketplace', 'fin': 'Fintech', 'grp': 'Group'}
DIV = {'grp': 'Kaspi.kz JSC', 'bank': 'Kaspi Bank', 'pay': 'Kaspi Pay', 'travel': 'Kaspi Travel', 'kolesa': 'Kolesa Group & classifieds', 'hepsi': 'Hepsiburada (86.7%)', 'hbank': 'Hepsi Bank'}
DEFAULT_DIV = 'grp'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F3", "panel-2": "#F0E9EA", "ink": "#210F0F", "ink-2": "#4B3133",
    "muted": "#7A6564", "faint": "#908282", "line": "#E3DBDB", "line-2": "#D3CAC9", "focus": "#F14635",
    "accent": "#F14635", "link": "#B9270D", "gold": "#F14635", "gold-deep": "#931E0A", "gold-ink": "#B9270D",
    "l1": "#591206", "l2": "#931E0A", "l3": "#DA4526", "l4": "#CB7B76", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#A93520", "l2f": "#F14635", "l3f": "#DA7A6E", "l4f": "#DAAEAE",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#210F0F", "shadow": "rgba(54,12,12,.22)", "wash-a": "rgba(241,70,53,.14)",
    "wash-b": "rgba(218,174,174,.10)", "gb2": "#A93520", "gb3": "#F14635", "gb4": "#E6C1C3", "brand-grad": "linear-gradient(90deg,#931E0A,#F14635 55%,#E6C1C3)",
    "gold-grad": "linear-gradient(135deg,#E6C1C3 0%,#F14635 45%,#931E0A 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0B0B", "panel": "#221819", "panel-2": "#352627", "ink": "#F7F3F4", "ink-2": "#E7DFE0",
    "muted": "#D3CCCB", "faint": "#BFB8B8", "line": "#675351", "line-2": "#9F8D8B", "focus": "#F14635",
    "accent": "#F14635", "link": "#E6C1C3", "gold": "#F14635", "gold-deep": "#E1A7A7", "gold-ink": "#E6C1C3",
    "l1": "#E6C1C3", "l2": "#E0B0B0", "l3": "#E7BEB9", "l4": "#EBCCCD", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#A93520", "l2f": "#F14635", "l3f": "#DA7A6E", "l4f": "#DAAEAE",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090607", "wash-a": "rgba(241,70,53,.12)", "wash-b": "rgba(218,174,174,.06)",
    "gb2": "#A93520", "gb3": "#F14635", "gb4": "#E6C1C3", "gold-grad": "linear-gradient(135deg,#F2D2D4 0%,#DA9E9C 45%,#F14635 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
