"""Capital One, as a platform: the data behind ``Capital_One_Platform.html``.

``python customers/build_page.py capitalone`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Capital_One_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from capitalone_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from capitalone_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Capital One'
PAGE = 'Capital_One_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Capital One Platform"
KICKER = f"Capital One Financial · as at {AS_OF}"
H1 = '<h1>Capital One <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Capital One's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Capital One's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Capital One's colours"

PIN = (38.92, -77.22, 'McLean')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'card': 'Credit Card segment', 'consumer': 'Consumer Banking segment', 'commercial': 'Commercial Banking segment', 'network': 'Discover Global Network & PULSE', 'grp': 'Group'}
DIV = {'cof': 'Capital One', 'card': 'Capital One Card', 'consumer': 'Consumer Banking', 'commercial': 'Commercial Banking', 'network': 'Discover Global Network', 'grp': 'Capital One Financial'}
DEFAULT_DIV = 'cof'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F5F6", "panel-2": "#E4EDEE", "ink": "#0A1519", "ink-2": "#1A272B",
    "muted": "#3F4950", "faint": "#626C71", "line": "#C7D0D6", "line-2": "#A7B3BA", "focus": "#004977",
    "accent": "#004977", "link": "#00335C", "gold": "#004977", "gold-deep": "#002C50", "gold-ink": "#00335C",
    "l1": "#00203A", "l2": "#002C50", "l3": "#0A3962", "l4": "#29607F", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0A3253", "l2f": "#004977", "l3f": "#1D6598", "l4f": "#66A7C1",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A1519", "shadow": "rgba(6,28,38,.22)", "wash-a": "rgba(0,73,119,.14)",
    "wash-b": "rgba(102,167,193,.10)", "gb2": "#0A3253", "gb3": "#004977", "gb4": "#8AC4D7", "brand-grad": "linear-gradient(90deg,#002C50,#004977 55%,#8AC4D7)",
    "gold-grad": "linear-gradient(135deg,#8AC4D7 0%,#004977 45%,#002C50 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090C0D", "panel": "#101618", "panel-2": "#171E21", "ink": "#F2F6F7", "ink-2": "#D3DEDF",
    "muted": "#A0AAB1", "faint": "#7D868C", "line": "#262D32", "line-2": "#384045", "focus": "#58ADD1",
    "accent": "#449CC5", "link": "#8AC4D7", "gold": "#449CC5", "gold-deep": "#58ADD1", "gold-ink": "#8AC4D7",
    "l1": "#8AC4D7", "l2": "#69B1CE", "l3": "#7AB2DB", "l4": "#A6D3E2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0A3253", "l2f": "#004977", "l3f": "#1D6598", "l4f": "#66A7C1",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,73,119,.12)", "wash-b": "rgba(102,167,193,.06)",
    "gb2": "#0A3253", "gb3": "#004977", "gb4": "#8AC4D7", "gold-grad": "linear-gradient(135deg,#BDE4F0 0%,#449CC5 45%,#004977 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
