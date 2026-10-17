"""PrivatBank, as a platform: the data behind ``PrivatBank_Platform.html``.

``python customers/build_page.py privatbank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``PrivatBank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from privatbank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from privatbank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'PrivatBank'
PAGE = 'PrivatBank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "PrivatBank Platform"
KICKER = f"JSC CB PrivatBank · as at {AS_OF}"
H1 = '<h1>PrivatBank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: PrivatBank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in PrivatBank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in PrivatBank's colours"

PIN = (50.45, 30.52, 'Kyiv')
PIN_FACING = 'Ukraine and Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail banking', 'corporate': 'Corporate banking business', 'markets': 'Capital markets', 'legacy': 'Separate portfolio (former owners)', 'central': 'Capital management & central'}
DIV = {'pb': 'PrivatBank', 'p24': 'Privat24', 'p24b': 'Privat24 for Business', 'liqpay': 'LiqPay & Terminal', 'pmoney': 'PrivatMoney', 'pryvit': 'Pryvit & Subscriptions'}
DEFAULT_DIV = 'pb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F4F5F2", "panel-2": "#EBEDE7", "ink": "#141A0F", "ink-2": "#2F3728",
    "muted": "#646E5F", "faint": "#828A7F", "line": "#D5DAD2", "line-2": "#C0C6BC", "focus": "#4EA524",
    "accent": "#4EA524", "link": "#327419", "gold": "#4EA524", "gold-deep": "#295F15", "gold-ink": "#327419",
    "l1": "#1B3E0D", "l2": "#295F15", "l3": "#41872A", "l4": "#6CA050", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#376C24", "l2f": "#4EA524", "l3f": "#67B346", "l4f": "#A7C193",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#141A0F", "shadow": "rgba(25,40,14,.22)", "wash-a": "rgba(78,165,36,.14)",
    "wash-b": "rgba(167,193,147,.10)", "gb2": "#376C24", "gb3": "#4EA524", "gb4": "#C0D5AE", "brand-grad": "linear-gradient(90deg,#295F15,#4EA524 55%,#C0D5AE)",
    "gold-grad": "linear-gradient(135deg,#C0D5AE 0%,#4EA524 45%,#295F15 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0C0D0B", "panel": "#181B15", "panel-2": "#242920", "ink": "#F5F6F3", "ink-2": "#DEE1DA",
    "muted": "#B9BFB6", "faint": "#9DA29A", "line": "#41483D", "line-2": "#656E60", "focus": "#4EA524",
    "accent": "#4EA524", "link": "#C0D5AE", "gold": "#4EA524", "gold-deep": "#A6CA8C", "gold-ink": "#C0D5AE",
    "l1": "#C0D5AE", "l2": "#ACCA97", "l3": "#B2D4A3", "l4": "#CEDFBF", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#376C24", "l2f": "#4EA524", "l3f": "#67B346", "l4f": "#A7C193",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#070806", "wash-a": "rgba(78,165,36,.12)", "wash-b": "rgba(167,193,147,.06)",
    "gb2": "#376C24", "gb3": "#4EA524", "gb4": "#C0D5AE", "gold-grad": "linear-gradient(135deg,#DBEACE 0%,#98BF7E 45%,#4EA524 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
