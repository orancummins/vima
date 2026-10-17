"""Banco Nacional de Bolivia, as a platform: the data behind ``Banco_Nacional_de_Bolivia_Platform.html``.

``python customers/build_page.py bnb`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Banco_Nacional_de_Bolivia_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bnb_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bnb_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BNB'
PAGE = 'Banco_Nacional_de_Bolivia_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BNB Platform"
KICKER = f"Banco Nacional de Bolivia · as at {AS_OF}"
H1 = '<h1>BNB <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BNB's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BNB's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BNB's colours"

PIN = (-19.05, -65.26, 'Sucre')
PIN_FACING = 'Bolivia and South America'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'corp': 'Corporate & Business Banking', 'mass': 'Mass Banking', 'micro': 'SME & Microcredit', 'fin': 'Finance & International'}
DIV = {'bnb': 'Banco Nacional de Bolivia', 'group': 'Grupo Financiero BNB', 'leasing': 'BNB Leasing', 'valores': 'BNB Valores', 'safi': 'BNB SAFI', 'bille': 'Bille'}
DEFAULT_DIV = 'bnb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F3F5F3", "panel-2": "#E8EEE9", "ink": "#0F1B13", "ink-2": "#2B3B2F",
    "muted": "#5F6E65", "faint": "#808A84", "line": "#D5DCD7", "line-2": "#C1CAC5", "focus": "#28A85A",
    "accent": "#28A85A", "link": "#1D7947", "gold": "#28A85A", "gold-deep": "#18653B", "gold-ink": "#1D7947",
    "l1": "#0F4125", "l2": "#18653B", "l3": "#31935F", "l4": "#5AA977", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#29754B", "l2f": "#2BB461", "l3f": "#54B97E", "l4f": "#9BC5A8",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0F1B13", "shadow": "rgba(16,41,24,.22)", "wash-a": "rgba(43,180,97,.14)",
    "wash-b": "rgba(155,197,168,.10)", "gb2": "#29754B", "gb3": "#2BB461", "gb4": "#B4D7BD", "brand-grad": "linear-gradient(90deg,#18653B,#2BB461 55%,#B4D7BD)",
    "gold-grad": "linear-gradient(135deg,#B4D7BD 0%,#2BB461 45%,#18653B 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0B0E0B", "panel": "#171C18", "panel-2": "#222B24", "ink": "#F3F6F4", "ink-2": "#DCE2DD",
    "muted": "#BCC3BF", "faint": "#A2A9A4", "line": "#434F47", "line-2": "#6A7970", "focus": "#2BB461",
    "accent": "#2BB461", "link": "#B4D7BD", "gold": "#2BB461", "gold-deep": "#96CCA6", "gold-ink": "#B4D7BD",
    "l1": "#B4D7BD", "l2": "#9FCDAD", "l3": "#ABD6BD", "l4": "#C4E0CB", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#29754B", "l2f": "#2BB461", "l3f": "#54B97E", "l4f": "#9BC5A8",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060806", "wash-a": "rgba(43,180,97,.12)", "wash-b": "rgba(155,197,168,.06)",
    "gb2": "#29754B", "gb3": "#2BB461", "gb4": "#B4D7BD", "gold-grad": "linear-gradient(135deg,#D0EAD6 0%,#88C29B 45%,#2BB461 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
