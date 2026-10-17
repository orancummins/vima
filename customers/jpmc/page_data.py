"""JPMorgan Chase, as a platform: the data behind ``JPMorgan_Chase_Platform.html``.

``python customers/build_page.py jpmc`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``JPMorgan_Chase_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from jpmc_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from jpmc_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'JPMorgan Chase'
PAGE = 'JPMorgan_Chase_Platform.html'
AS_OF = "17 October 2026"
TITLE = "JPMorgan Chase Platform"
KICKER = f"JPMorgan Chase & Co. · as at {AS_OF}"
H1 = '<h1>JPMorgan Chase <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: JPMorgan Chase's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in JPMorgan Chase's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in JPMorgan Chase's colours"

PIN = (40.76, -73.97, 'New York')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'ccb': 'Consumer & Community Banking', 'cib': 'Commercial & Investment Bank', 'awm': 'Asset & Wealth Management', 'corp': 'Corporate'}
DIV = {'jpmc': 'JPMorgan Chase', 'chase': 'Chase', 'cib': 'J.P. Morgan', 'pay': 'J.P. Morgan Payments', 'awm': 'J.P. Morgan Asset & Wealth Management', 'kinexys': 'Kinexys'}
DEFAULT_DIV = 'jpmc'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F5F6", "panel-2": "#E4ECEF", "ink": "#09151B", "ink-2": "#1B292F",
    "muted": "#455359", "faint": "#677579", "line": "#C8D4D8", "line-2": "#AAB9BE", "focus": "#004A87",
    "accent": "#004A87", "link": "#003266", "gold": "#004A87", "gold-deep": "#002B57", "gold-ink": "#003266",
    "l1": "#001E3D", "l2": "#002B57", "l3": "#063973", "l4": "#27638F", "l5": "#271E38",
    "lu": "#746A81", "l1f": "#073260", "l2f": "#004A87", "l3f": "#1865AA", "l4f": "#68A6C8",
    "l5f": "#413652", "luf": "#A49BB0", "l1t": "#E8F7FF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#041B2C", "l5t": "#FFFFFF", "slot": "#09151B", "shadow": "rgba(4,28,42,.22)", "wash-a": "rgba(0,74,135,.14)",
    "wash-b": "rgba(104,166,200,.10)", "gb2": "#073260", "gb3": "#004A87", "gb4": "#8BC3DD", "brand-grad": "linear-gradient(90deg,#073260,#117ACA 55%,#7FC4F5)",
    "gold-grad": "linear-gradient(135deg,#8BC3DD 0%,#004A87 45%,#002B57 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090C0D", "panel": "#111719", "panel-2": "#172024", "ink": "#F2F6F7", "ink-2": "#D3DEE1",
    "muted": "#A3B1B5", "faint": "#818D92", "line": "#293338", "line-2": "#3E4A4F", "focus": "#59ABD9",
    "accent": "#469ACD", "link": "#8BC3DD", "gold": "#469ACD", "gold-deep": "#59ABD9", "gold-ink": "#8BC3DD",
    "l1": "#8BC3DD", "l2": "#6AAFD5", "l3": "#7AAFE1", "l4": "#A6D2E6", "l5": "#D5D0DB",
    "lu": "#948AA2", "l1f": "#073260", "l2f": "#004A87", "l3f": "#1865AA", "l4f": "#68A6C8",
    "l5f": "#746A81", "luf": "#746A81", "slot": "#050808", "wash-a": "rgba(0,74,135,.12)", "wash-b": "rgba(104,166,200,.06)",
    "gb2": "#073260", "gb3": "#004A87", "gb4": "#8BC3DD", "gold-grad": "linear-gradient(135deg,#BDE3F2 0%,#469ACD 45%,#004A87 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
