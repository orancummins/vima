"""Banque de Développement Local (BDL), as a platform: the data behind ``Banque_de_Developpement_Local_BDL_Platform.html``.

``python customers/build_page.py bdl`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Banque_de_Developpement_Local_BDL_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bdl_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bdl_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BDL'
PAGE = 'Banque_de_Developpement_Local_BDL_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BDL Platform"
KICKER = f"Banque de Développement Local · as at {AS_OF}"
H1 = '<h1>BDL <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BDL's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BDL's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BDL's colours"

PIN = (36.75, 2.89, 'Algiers')
PIN_FACING = 'Algeria and North Africa'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'menages': 'Households', 'prive': 'Private sector', 'public': 'Public sector', 'central': 'Treasury & central items'}
DIV = {'bdl': 'BDL', 'islamic': 'BDL Finance Islamique', 'digit': 'DigitBDL', 'wimpay': 'WIMPAY BDL', 'snl': 'Société Nationale de Leasing (50%)', 'finalep': 'FINALEP (66%)', 'satim': 'SATIM (14.7%)'}
DEFAULT_DIV = 'bdl'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F4F2F5", "panel-2": "#EAE6ED", "ink": "#150E18", "ink-2": "#2B232F",
    "muted": "#5E5360", "faint": "#7C737E", "line": "#D5CED6", "line-2": "#BCB3BE", "focus": "#711E80",
    "accent": "#711E80", "link": "#57165E", "gold": "#711E80", "gold-deep": "#49124F", "gold-ink": "#57165E",
    "l1": "#310D35", "l2": "#49124F", "l3": "#65236A", "l4": "#7A4585", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#521E57", "l2f": "#711E80", "l3f": "#8C3E98", "l4f": "#AB85B8",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#150E18", "shadow": "rgba(30,13,36,.22)", "wash-a": "rgba(113,30,128,.14)",
    "wash-b": "rgba(171,133,184,.10)", "gb2": "#521E57", "gb3": "#711E80", "gb4": "#C2A3CE", "brand-grad": "linear-gradient(90deg,#49124F,#711E80 55%,#C2A3CE)",
    "gold-grad": "linear-gradient(135deg,#C2A3CE 0%,#711E80 45%,#49124F 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0C0A0D", "panel": "#171419", "panel-2": "#211C24", "ink": "#F5F3F6", "ink-2": "#DCD8DF",
    "muted": "#B4ACB6", "faint": "#948C95", "line": "#3A323B", "line-2": "#564C57", "focus": "#B17DC1",
    "accent": "#A46DB5", "link": "#C2A3CE", "gold": "#A46DB5", "gold-deep": "#B17DC1", "gold-ink": "#C2A3CE",
    "l1": "#C2A3CE", "l2": "#B389C2", "l3": "#C797CE", "l4": "#D0B8DA", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#521E57", "l2f": "#711E80", "l3f": "#8C3E98", "l4f": "#AB85B8",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#070608", "wash-a": "rgba(113,30,128,.12)", "wash-b": "rgba(171,133,184,.06)",
    "gb2": "#521E57", "gb3": "#711E80", "gb4": "#C2A3CE", "gold-grad": "linear-gradient(135deg,#DFCAE8 0%,#A46DB5 45%,#711E80 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
