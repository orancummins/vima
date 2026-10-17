"""National Bank of Egypt, as a platform: the data behind ``National_Bank_of_Egypt_Platform.html``.

``python customers/build_page.py nbe`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``National_Bank_of_Egypt_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from nbe_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from nbe_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'NBE'
PAGE = 'National_Bank_of_Egypt_Platform.html'
AS_OF = "17 October 2026"
TITLE = "NBE Platform"
KICKER = f"National Bank of Egypt · as at {AS_OF}"
H1 = '<h1>NBE <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: NBE's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in NBE's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in NBE's colours"

PIN = (30.04, 31.24, 'Cairo')
PIN_FACING = 'Egypt, the Gulf and Africa'

ALLOWED_MENTIONS: tuple[str, ...] = ('Saudi',)

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'corp': 'Corporate & investment banking', 'retail': 'Retail & consumer banking', 'sme': 'SME & microfinance', 'treasury': 'Treasury & financial institutions', 'intl': 'International'}
DIV = {'nbe': 'National Bank of Egypt', 'nbeuk': 'NBE (UK)', 'intl': 'NBE international branches', 'alcap': 'Al Ahly Capital Holding', 'momkn': 'Al Ahly Momkn'}
DEFAULT_DIV = 'nbe'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F5F2", "panel-2": "#E7EDE5", "ink": "#0D180C", "ink-2": "#202C1E",
    "muted": "#485548", "faint": "#6A766A", "line": "#CBD5CB", "line-2": "#ADBBAD", "focus": "#107614",
    "accent": "#107614", "link": "#0C5914", "gold": "#107614", "gold-deep": "#0A4C11", "gold-ink": "#0C5914",
    "l1": "#07360C", "l2": "#0A4C11", "l3": "#176120", "l4": "#377E38", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#15521B", "l2f": "#107614", "l3f": "#2F9335", "l4f": "#7AB976",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0D180C", "shadow": "rgba(11,36,10,.22)", "wash-a": "rgba(16,118,20,.14)",
    "wash-b": "rgba(122,185,118,.10)", "gb2": "#15521B", "gb3": "#107614", "gb4": "#9DD098", "brand-grad": "linear-gradient(90deg,#0A4C11,#107614 55%,#9DD098)",
    "gold-grad": "linear-gradient(135deg,#9DD098 0%,#107614 45%,#0A4C11 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0D09", "panel": "#131812", "panel-2": "#1A2219", "ink": "#F3F6F3", "ink-2": "#D7DFD5",
    "muted": "#A6B2A6", "faint": "#838F84", "line": "#2B352C", "line-2": "#404C41", "focus": "#71C56C",
    "accent": "#5DB85A", "link": "#9DD098", "gold": "#5DB85A", "gold-deep": "#71C56C", "gold-ink": "#9DD098",
    "l1": "#9DD098", "l2": "#7FC47A", "l3": "#8AD18F", "l4": "#B4DCB0", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#15521B", "l2f": "#107614", "l3f": "#2F9335", "l4f": "#7AB976",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060805", "wash-a": "rgba(16,118,20,.12)", "wash-b": "rgba(122,185,118,.06)",
    "gb2": "#15521B", "gb3": "#107614", "gb4": "#9DD098", "gold-grad": "linear-gradient(135deg,#C9EAC5 0%,#5DB85A 45%,#107614 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
