"""BBVA, as a platform: the data behind ``BBVA_Platform.html``.

``python customers/build_page.py bbva`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``BBVA_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bbva_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bbva_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BBVA'
PAGE = 'BBVA_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BBVA Platform"
KICKER = f"Banco Bilbao Vizcaya Argentaria · as at {AS_OF}"
H1 = '<h1>BBVA <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BBVA's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BBVA's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BBVA's colours"

PIN = (40.51, -3.66, 'Madrid')
PIN_FACING = 'Spain and Mexico'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'spain': 'Spain', 'mexico': 'Mexico', 'samerica': 'South America', 'rest': 'Rest of Business', 'cc': 'Corporate Center'}
DIV = {'group': 'BBVA Group', 'spain': 'BBVA Spain', 'mexico': 'BBVA México', 'digital': 'Digital banks (Italy, Germany)', 'cib': 'Corporate & Investment Banking', 'consumer': 'BBVA Consumer Finance', 'samerica': 'BBVA South America'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F3F6", "panel-2": "#E4E8EE", "ink": "#0A0E1B", "ink-2": "#1D2330",
    "muted": "#4A4D5D", "faint": "#6C6E7C", "line": "#CACCD8", "line-2": "#ADB0BF", "focus": "#001391",
    "accent": "#001391", "link": "#00086C", "gold": "#001391", "gold-deep": "#00075B", "gold-ink": "#00086C",
    "l1": "#00053F", "l2": "#00075B", "l3": "#0C1176", "l4": "#2E3E91", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0C1262", "l2f": "#001391", "l3f": "#202FAA", "l4f": "#7084C6",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A0E1B", "shadow": "rgba(6,13,41,.22)", "wash-a": "rgba(0,19,145,.14)",
    "wash-b": "rgba(112,132,198,.10)", "gb2": "#0C1262", "gb3": "#001391", "gb4": "#92A5DA", "brand-grad": "linear-gradient(90deg,#00075B,#001391 55%,#92A5DA)",
    "gold-grad": "linear-gradient(135deg,#92A5DA 0%,#001391 45%,#00075B 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090A0D", "panel": "#11141A", "panel-2": "#191C24", "ink": "#F2F4F7", "ink-2": "#D5D9E0",
    "muted": "#A6A8B6", "faint": "#858794", "line": "#2C2E3A", "line-2": "#434553", "focus": "#637CD4",
    "accent": "#5D73CC", "link": "#92A5DA", "gold": "#5D73CC", "gold-deep": "#637CD4", "gold-ink": "#92A5DA",
    "l1": "#92A5DA", "l2": "#7389D1", "l3": "#828BDD", "l4": "#ABBAE4", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0C1262", "l2f": "#001391", "l3f": "#202FAA", "l4f": "#7084C6",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050608", "wash-a": "rgba(0,19,145,.12)", "wash-b": "rgba(112,132,198,.06)",
    "gb2": "#0C1262", "gb3": "#001391", "gb4": "#92A5DA", "gold-grad": "linear-gradient(135deg,#C0CEF0 0%,#5169C8 45%,#001391 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
