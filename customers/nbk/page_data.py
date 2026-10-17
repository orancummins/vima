"""National Bank of Kuwait (NBK), as a platform: the data behind ``National_Bank_of_Kuwait_Platform.html``.

``python customers/build_page.py nbk`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``National_Bank_of_Kuwait_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from nbk_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from nbk_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'NBK'
PAGE = 'National_Bank_of_Kuwait_Platform.html'
AS_OF = "17 October 2026"
TITLE = "NBK Platform"
KICKER = f"National Bank of Kuwait · as at {AS_OF}"
H1 = '<h1>NBK <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: NBK's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in NBK's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in NBK's colours"

PIN = (29.37, 47.98, 'Kuwait City')
PIN_FACING = 'Kuwait and the Gulf'

ALLOWED_MENTIONS: tuple[str, ...] = ('Saudi',)

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'consumer': 'Consumer Banking', 'corporate': 'Corporate Banking', 'islamic': 'Islamic Banking (Boubyan)', 'wealth': 'NBK Wealth', 'intl': 'International Banking'}
DIV = {'group': 'NBK Group', 'nbk': 'NBK Kuwait', 'weyay': 'Weyay Bank', 'boubyan': 'Boubyan Bank', 'wealth': 'NBK Wealth', 'upay': 'UPayments', 'intl': 'NBK International'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F4F5", "panel-2": "#E6E9EC", "ink": "#0E1116", "ink-2": "#21252B",
    "muted": "#4C4F56", "faint": "#6E7076", "line": "#CDCFD4", "line-2": "#B0B3BA", "focus": "#21376B",
    "accent": "#21376B", "link": "#192650", "gold": "#21376B", "gold-deep": "#152044", "gold-ink": "#192650",
    "l1": "#0F172F", "l2": "#152044", "l3": "#242F5A", "l4": "#445477", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#1F294B", "l2f": "#21376B", "l3f": "#3F5387", "l4f": "#8295B0",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0E1116", "shadow": "rgba(14,21,32,.22)", "wash-a": "rgba(33,55,107,.14)",
    "wash-b": "rgba(130,149,176,.10)", "gb2": "#1F294B", "gb3": "#21376B", "gb4": "#A2B3C8", "brand-grad": "linear-gradient(90deg,#152044,#21376B 55%,#A2B3C8)",
    "gold-grad": "linear-gradient(135deg,#A2B3C8 0%,#21376B 45%,#152044 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0B0C", "panel": "#131517", "panel-2": "#1B1E21", "ink": "#F3F5F6", "ink-2": "#D7DBDD",
    "muted": "#A9ABB1", "faint": "#87898F", "line": "#2E3035", "line-2": "#45474D", "focus": "#7C93B9",
    "accent": "#6B83AB", "link": "#A2B3C8", "gold": "#6B83AB", "gold-deep": "#7C93B9", "gold-ink": "#A2B3C8",
    "l1": "#A2B3C8", "l2": "#879CBA", "l3": "#96A3C7", "l4": "#B8C5D6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#1F294B", "l2f": "#21376B", "l3f": "#3F5387", "l4f": "#8295B0",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060707", "wash-a": "rgba(33,55,107,.12)", "wash-b": "rgba(130,149,176,.06)",
    "gb2": "#1F294B", "gb3": "#21376B", "gb4": "#A2B3C8", "gold-grad": "linear-gradient(135deg,#CBD7E5 0%,#6B83AB 45%,#21376B 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
