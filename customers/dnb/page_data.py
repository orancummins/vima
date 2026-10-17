"""DNB, as a platform: the data behind ``DNB_Platform.html``.

``python customers/build_page.py dnb`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``DNB_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from dnb_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from dnb_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'DNB'
PAGE = 'DNB_Platform.html'
AS_OF = "17 October 2026"
TITLE = "DNB Platform"
KICKER = f"DNB Bank ASA · as at {AS_OF}"
H1 = '<h1>DNB <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: DNB's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in DNB's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in DNB's colours"

PIN = (59.91, 10.76, 'Oslo')
PIN_FACING = 'Norway and the Nordics'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'pm': 'Personal customers', 'bmn': 'Corporate customers Norway', 'lci': 'Large corporates & international', 'other': 'Other operations'}
DIV = {'group': 'DNB Group', 'dnb': 'DNB', 'sbanken': 'Sbanken', 'carnegie': 'DNB Carnegie', 'wm': 'Wealth Management & DNB Livsforsikring', 'finans': 'DNB Finans', 'eiendom': 'DNB Eiendom', 'vipps': 'Vipps MobilePay (associate)'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F5", "panel-2": "#E3EEEB", "ink": "#0A1917", "ink-2": "#192A27",
    "muted": "#3D4D4D", "faint": "#616F6F", "line": "#C7D5D5", "line-2": "#A6B9B9", "focus": "#007272",
    "accent": "#007272", "link": "#005459", "gold": "#007272", "gold-deep": "#00494E", "gold-ink": "#005459",
    "l1": "#003538", "l2": "#00494E", "l3": "#09575E", "l4": "#287C7A", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0A4C50", "l2f": "#007272", "l3f": "#1C9194", "l4f": "#64C1B8",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A1917", "shadow": "rgba(6,38,35,.22)", "wash-a": "rgba(0,114,114,.14)",
    "wash-b": "rgba(100,193,184,.10)", "gb2": "#0A4C50", "gb3": "#007272", "gb4": "#89D7CC", "brand-grad": "linear-gradient(90deg,#00494E,#007272 55%,#89D7CC)",
    "gold-grad": "linear-gradient(135deg,#89D7CC 0%,#007272 45%,#00494E 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090D0C", "panel": "#101816", "panel-2": "#16201F", "ink": "#F2F7F6", "ink-2": "#D3DFDC",
    "muted": "#9FB0B0", "faint": "#7B8B8B", "line": "#253030", "line-2": "#364343", "focus": "#56D1C6",
    "accent": "#42C4BA", "link": "#89D7CC", "gold": "#42C4BA", "gold-deep": "#56D1C6", "gold-ink": "#89D7CC",
    "l1": "#89D7CC", "l2": "#67CDC3", "l3": "#78D7DA", "l4": "#A5E2DA", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0A4C50", "l2f": "#007272", "l3f": "#1C9194", "l4f": "#64C1B8",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050807", "wash-a": "rgba(0,114,114,.12)", "wash-b": "rgba(100,193,184,.06)",
    "gb2": "#0A4C50", "gb3": "#007272", "gb4": "#89D7CC", "gold-grad": "linear-gradient(135deg,#BDEFE8 0%,#42C4BA 45%,#007272 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
