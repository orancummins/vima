"""HDFC Bank, as a platform: the data behind ``HDFC_Bank_Platform.html``.

``python customers/build_page.py hdfc`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``HDFC_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from hdfc_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from hdfc_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'HDFC Bank'
PAGE = 'HDFC_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "HDFC Bank Platform"
KICKER = f"HDFC Bank Limited · as at {AS_OF}"
H1 = '<h1>HDFC Bank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: HDFC Bank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in HDFC Bank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in HDFC Bank's colours"

PIN = (19.0, 72.83, 'Mumbai')
PIN_FACING = 'South Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail Banking', 'wholesale': 'Wholesale Banking', 'treasury': 'Treasury', 'other': 'Other Banking Business'}
DIV = {'bank': 'HDFC Bank', 'cards': 'HDFC Bank Cards', 'payzapp': 'PayZapp', 'vyapar': 'SmartHub Vyapar', 'hdb': 'HDB Financial Services', 'life': 'HDFC Life & ERGO', 'amc': 'HDFC AMC & Securities'}
DEFAULT_DIV = 'bank'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F5F6", "panel-2": "#E4ECEE", "ink": "#0A151A", "ink-2": "#1D2A30",
    "muted": "#49535C", "faint": "#6B747B", "line": "#CAD1D8", "line-2": "#ADB6BE", "focus": "#004C8F",
    "accent": "#004C8F", "link": "#00326B", "gold": "#004C8F", "gold-deep": "#002B5B", "gold-ink": "#00326B",
    "l1": "#001E3F", "l2": "#002B5B", "l3": "#0C3B74", "l4": "#2E648F", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0C3360", "l2f": "#004C8F", "l3f": "#2066A9", "l4f": "#6FA5C5",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0A151A", "shadow": "rgba(6,27,41,.22)", "wash-a": "rgba(0,76,143,.14)",
    "wash-b": "rgba(111,165,197,.10)", "gb2": "#0C3360", "gb3": "#004C8F", "gb4": "#91C2DA", "brand-grad": "linear-gradient(90deg,#002B5B,#004C8F 55%,#91C2DA)",
    "gold-grad": "linear-gradient(135deg,#91C2DA 0%,#004C8F 45%,#002B5B 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090C0D", "panel": "#111719", "panel-2": "#192024", "ink": "#F2F6F7", "ink-2": "#D5DEE0",
    "muted": "#A6AEB6", "faint": "#858C93", "line": "#2C3339", "line-2": "#434B52", "focus": "#62A9D4",
    "accent": "#5099C8", "link": "#91C2DA", "gold": "#5099C8", "gold-deep": "#62A9D4", "gold-ink": "#91C2DA",
    "l1": "#91C2DA", "l2": "#72AED1", "l3": "#82AFDD", "l4": "#ABD0E4", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0C3360", "l2f": "#004C8F", "l3f": "#2066A9", "l4f": "#6FA5C5",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,76,143,.12)", "wash-b": "rgba(111,165,197,.06)",
    "gb2": "#0C3360", "gb3": "#004C8F", "gb4": "#91C2DA", "gold-grad": "linear-gradient(135deg,#C0E1F0 0%,#5099C8 45%,#004C8F 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
