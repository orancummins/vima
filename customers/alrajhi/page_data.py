"""Al Rajhi Bank, as a platform: the data behind ``Al_Rajhi_Bank_Platform.html``.

``python customers/build_page.py alrajhi`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Al_Rajhi_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from alrajhi_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from alrajhi_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Al Rajhi'
PAGE = 'Al_Rajhi_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Al Rajhi Platform"
KICKER = f"Al Rajhi Bank · as at {AS_OF}"
H1 = '<h1>Al Rajhi <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Al Rajhi's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Al Rajhi's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Al Rajhi's colours"

PIN = (24.71, 46.68, 'Riyadh')
PIN_FACING = 'the Kingdom and the Gulf'

ALLOWED_MENTIONS: tuple[str, ...] = ('Saudi', 'Riyadh')

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail', 'corporate': 'Corporate & SME', 'treasury': 'Treasury', 'invest': 'Investment services & brokerage', 'other': 'Group & other'}
DIV = {'arb': 'Al Rajhi group', 'bank': 'alrajhi bank', 'neoleap': 'neoleap & urpay', 'emkan': 'Emkan Finance', 'capital': 'Al Rajhi Capital', 'neotek': 'neotek & Drahim', 'intl': 'Malaysia, Jordan & Kuwait'}
DEFAULT_DIV = 'arb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F3F6", "panel-2": "#E7E9EF", "ink": "#0D0F1E", "ink-2": "#2A2D41",
    "muted": "#68677E", "faint": "#858392", "line": "#D5D5DE", "line-2": "#C3C3CE", "focus": "#150FE0",
    "accent": "#150FE0", "link": "#170A9B", "gold": "#150FE0", "gold-deep": "#12087C", "gold-ink": "#170A9B",
    "l1": "#0B054E", "l2": "#12087C", "l3": "#2E1EB4", "l4": "#5353BE", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#241A8D", "l2f": "#150FE0", "l3f": "#5049D1", "l4f": "#999DD0",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0D0F1E", "shadow": "rgba(10,12,48,.22)", "wash-a": "rgba(21,15,224,.14)",
    "wash-b": "rgba(153,157,208,.10)", "gb2": "#241A8D", "gb3": "#150FE0", "gb4": "#B1B7E0", "brand-grad": "linear-gradient(90deg,#12087C,#150FE0 55%,#B1B7E0)",
    "gold-grad": "linear-gradient(135deg,#B1B7E0 0%,#150FE0 45%,#12087C 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0B0E", "panel": "#16171F", "panel-2": "#21232F", "ink": "#F3F4F7", "ink-2": "#DCDEE4",
    "muted": "#BEBEC8", "faint": "#A6A5AF", "line": "#444456", "line-2": "#6F6E85", "focus": "#9195DA",
    "accent": "#8387D1", "link": "#B1B7E0", "gold": "#8387D1", "gold-deep": "#9195DA", "gold-ink": "#B1B7E0",
    "l1": "#B1B7E0", "l2": "#9BA0D9", "l3": "#AAA7E1", "l4": "#C1C5E7", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#241A8D", "l2f": "#150FE0", "l3f": "#5049D1", "l4f": "#999DD0",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060608", "wash-a": "rgba(21,15,224,.12)", "wash-b": "rgba(153,157,208,.06)",
    "gb2": "#241A8D", "gb3": "#150FE0", "gb4": "#B1B7E0", "gold-grad": "linear-gradient(135deg,#CDD1F0 0%,#8387D1 45%,#150FE0 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
