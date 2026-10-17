"""Scotiabank, as a platform: the data behind ``Scotiabank_Platform.html``.

``python customers/build_page.py scotiabank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Scotiabank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from scotiabank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from scotiabank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Scotiabank'
PAGE = 'Scotiabank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Scotiabank Platform"
KICKER = f"The Bank of Nova Scotia · as at {AS_OF}"
H1 = '<h1>Scotiabank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Scotiabank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Scotiabank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Scotiabank's colours"

PIN = (43.65, -79.38, 'Toronto')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'canada': 'Canadian Banking', 'intl': 'International Banking', 'gwm': 'Global Wealth Management', 'gbm': 'Global Banking and Markets', 'other': 'Other'}
DIV = {'bns': 'Scotiabank group', 'scotiaca': 'Scotiabank Canada', 'tangerine': 'Tangerine', 'mexico': 'Scotiabank Mexico', 'andean': 'Scotiabank Peru & Chile', 'caribbean': 'Scotiabank Caribbean', 'gtb': 'Global Transaction Banking', 'stakes': 'KeyCorp & Davivienda stakes'}
DEFAULT_DIV = 'bns'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F3", "panel-2": "#EFE8EA", "ink": "#1F0E10", "ink-2": "#442C31",
    "muted": "#7A6465", "faint": "#908181", "line": "#E0D6D7", "line-2": "#D1C6C7", "focus": "#EC111A",
    "accent": "#EC111A", "link": "#A20E0C", "gold": "#EC111A", "gold-deep": "#820B09", "gold-ink": "#A20E0C",
    "l1": "#510706", "l2": "#820B09", "l3": "#BD2720", "l4": "#C15C63", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#941F1C", "l2f": "#EC111A", "l3f": "#D25355", "l4f": "#D39EA6",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#1F0E10", "shadow": "rgba(50,11,16,.22)", "wash-a": "rgba(236,17,26,.14)",
    "wash-b": "rgba(211,158,166,.10)", "gb2": "#941F1C", "gb3": "#EC111A", "gb4": "#E2B6BE", "brand-grad": "linear-gradient(90deg,#820B09,#EC111A 55%,#E2B6BE)",
    "gold-grad": "linear-gradient(135deg,#E2B6BE 0%,#EC111A 45%,#820B09 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0B0B", "panel": "#201718", "panel-2": "#302325", "ink": "#F7F3F4", "ink-2": "#E5DDDF",
    "muted": "#CBC1C2", "faint": "#B3AAAA", "line": "#5A4748", "line-2": "#8C7576", "focus": "#DC97A0",
    "accent": "#D38A92", "link": "#E2B6BE", "gold": "#D38A92", "gold-deep": "#DC97A0", "gold-ink": "#E2B6BE",
    "l1": "#E2B6BE", "l2": "#DAA1A9", "l3": "#E3ACAC", "l4": "#E8C4CA", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#941F1C", "l2f": "#EC111A", "l3f": "#D25355", "l4f": "#D39EA6",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080607", "wash-a": "rgba(236,17,26,.12)", "wash-b": "rgba(211,158,166,.06)",
    "gb2": "#941F1C", "gb3": "#EC111A", "gb4": "#E2B6BE", "gold-grad": "linear-gradient(135deg,#F0CED5 0%,#D38A92 45%,#EC111A 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
