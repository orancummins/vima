"""Worldline, as a platform: the data behind ``Worldline_Platform.html``.

``python customers/build_page.py worldline`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Worldline_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from worldline_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from worldline_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Worldline'
PAGE = 'Worldline_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Worldline Platform"
KICKER = f"Worldline SA · as at {AS_OF}"
H1 = '<h1>Worldline <span class="os">Platform</span></h1>'
SERVES = 'who Worldline serves'

PALETTE_NOTE = ("Palette: Worldline's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Worldline's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Worldline's colours"

PIN = (48.89, 2.24, 'Paris')
PIN_FACING = 'Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'ms': 'Merchant Services', 'fs': 'Financial Services', 'grp': 'Group & central'}
DIV = {'grp': 'Worldline SA', 'wl': 'Worldline', 'payone': 'PAYONE', 'gc': 'Global Collect', 'equens': 'equensWorldline', 'bambora': 'Bambora', 'axepta': 'Axepta Italy', 'greece': 'Worldline Greece'}
DEFAULT_DIV = 'grp'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F3F5F4", "panel-2": "#E9EEEC", "ink": "#121C19", "ink-2": "#32403B",
    "muted": "#636E6C", "faint": "#828A89", "line": "#D9DEDD", "line-2": "#C5CBCA", "focus": "#39A291",
    "accent": "#39A291", "link": "#29746C", "gold": "#39A291", "gold-deep": "#256962", "gold-ink": "#29746C",
    "l1": "#17413C", "l2": "#256962", "l3": "#459E97", "l4": "#77ADA2", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#387C75", "l2f": "#46BEAA", "l3f": "#73B8AE", "l4f": "#ACC8C1",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#121C19", "shadow": "rgba(20,42,36,.22)", "wash-a": "rgba(70,190,170,.14)",
    "wash-b": "rgba(172,200,193,.10)", "gb2": "#387C75", "gb3": "#46BEAA", "gb4": "#C1D9D2", "brand-grad": "linear-gradient(90deg,#256962,#46BEAA 55%,#C1D9D2)",
    "gold-grad": "linear-gradient(135deg,#C1D9D2 0%,#46BEAA 45%,#256962 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0C0E0D", "panel": "#191E1C", "panel-2": "#262E2C", "ink": "#F4F6F5", "ink-2": "#DFE3E2",
    "muted": "#C5CAC9", "faint": "#AEB3B2", "line": "#4D5856", "line-2": "#7E8A88", "focus": "#46BEAA",
    "accent": "#46BEAA", "link": "#C1D9D2", "gold": "#46BEAA", "gold-deep": "#A8CEC4", "gold-ink": "#C1D9D2",
    "l1": "#C1D9D2", "l2": "#B0CFC7", "l3": "#BAD8D4", "l4": "#CDE1DB", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#387C75", "l2f": "#46BEAA", "l3f": "#73B8AE", "l4f": "#ACC8C1",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060807", "wash-a": "rgba(70,190,170,.12)", "wash-b": "rgba(172,200,193,.06)",
    "gb2": "#387C75", "gb3": "#46BEAA", "gb4": "#C1D9D2", "gold-grad": "linear-gradient(135deg,#D6E9E3 0%,#9DC4BB 45%,#46BEAA 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
