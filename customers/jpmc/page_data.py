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
    "ground": "#FFFFFF", "panel": "#F1F5F6", "panel-2": "#E5ECEF", "ink": "#0B141D", "ink-2": "#23303A",
    "muted": "#5F6877", "faint": "#7E858F", "line": "#CFD4DC", "line-2": "#B8BEC7", "focus": "#004FC2",
    "accent": "#004FC2", "link": "#00308A", "gold": "#004FC2", "gold-deep": "#002871", "gold-ink": "#00308A",
    "l1": "#001A4A", "l2": "#002871", "l3": "#103D9C", "l4": "#386DB1", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0F357C", "l2f": "#004FC2", "l3f": "#2767CD", "l4f": "#83A9CD",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0B141D", "shadow": "rgba(7,26,46,.22)", "wash-a": "rgba(0,79,194,.14)",
    "wash-b": "rgba(131,169,205,.10)", "gb2": "#0F357C", "gb3": "#004FC2", "gb4": "#A1C3DF", "brand-grad": "linear-gradient(90deg,#002871,#004FC2 55%,#A1C3DF)",
    "gold-grad": "linear-gradient(135deg,#A1C3DF 0%,#004FC2 45%,#002871 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0C0E", "panel": "#13191D", "panel-2": "#1D242A", "ink": "#F2F6F7", "ink-2": "#D8DFE3",
    "muted": "#B2B8C0", "faint": "#969BA2", "line": "#383F49", "line-2": "#59626E", "focus": "#78A9DA",
    "accent": "#689AD0", "link": "#A1C3DF", "gold": "#689AD0", "gold-deep": "#78A9DA", "gold-ink": "#A1C3DF",
    "l1": "#A1C3DF", "l2": "#86AFD7", "l3": "#93B1E2", "l4": "#B5D0E7", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0F357C", "l2f": "#004FC2", "l3f": "#2767CD", "l4f": "#83A9CD",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,79,194,.12)", "wash-b": "rgba(131,169,205,.06)",
    "gb2": "#0F357C", "gb3": "#004FC2", "gb4": "#A1C3DF", "gold-grad": "linear-gradient(135deg,#C5DEF1 0%,#689AD0 45%,#004FC2 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
