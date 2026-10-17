"""ICICI Bank, as a platform: the data behind ``ICICI_Bank_Platform.html``.

``python customers/build_page.py icici`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``ICICI_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from icici_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from icici_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'ICICI Bank'
PAGE = 'ICICI_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "ICICI Bank Platform"
KICKER = f"ICICI Bank Limited · as at {AS_OF}"
H1 = '<h1>ICICI Bank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: ICICI Bank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in ICICI Bank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in ICICI Bank's colours"

PIN = (19.07, 72.87, 'Mumbai')
PIN_FACING = 'South Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail Banking', 'wholesale': 'Wholesale Banking', 'treasury': 'Treasury', 'other': 'Other Banking'}
DIV = {'bank': 'ICICI Bank', 'cards': 'ICICI Bank Cards', 'biz': 'Business & Commercial Banking', 'intl': 'International & GIFT City', 'life': 'ICICI Prudential Life & ICICI Lombard', 'amc': 'ICICI Prudential AMC & ICICI Securities', 'hfc': 'ICICI Home Finance'}
DEFAULT_DIV = 'bank'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F3", "panel-2": "#EEE7E9", "ink": "#1B0E10", "ink-2": "#38282B",
    "muted": "#756565", "faint": "#8E8282", "line": "#DBD2D2", "line-2": "#C7BDBD", "focus": "#AD1F24",
    "accent": "#AD1F24", "link": "#7A1816", "gold": "#AD1F24", "gold-deep": "#641412", "gold-ink": "#7A1816",
    "l1": "#400D0C", "l2": "#641412", "l3": "#8D2B27", "l4": "#A54E53", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#712321", "l2f": "#AD1F24", "l3f": "#BA4244", "l4f": "#C49299",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1B0E10", "shadow": "rgba(41,13,16,.22)", "wash-a": "rgba(173,31,36,.14)",
    "wash-b": "rgba(196,146,153,.10)", "gb2": "#712321", "gb3": "#AD1F24", "gb4": "#D7ADB4", "brand-grad": "linear-gradient(90deg,#641412,#AD1F24 55%,#D7ADB4)",
    "gold-grad": "linear-gradient(135deg,#D7ADB4 0%,#AD1F24 45%,#641412 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0D0A0B", "panel": "#1C1517", "panel-2": "#292021", "ink": "#F7F3F4", "ink-2": "#E2DADC",
    "muted": "#C0B7B7", "faint": "#A39B9B", "line": "#4A3D3E", "line-2": "#706161", "focus": "#CD8B93",
    "accent": "#C27C84", "link": "#D7ADB4", "gold": "#C27C84", "gold-deep": "#CD8B93", "gold-ink": "#D7ADB4",
    "l1": "#D7ADB4", "l2": "#CD969D", "l3": "#D7A2A2", "l4": "#E0BFC4", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#712321", "l2f": "#AD1F24", "l3f": "#BA4244", "l4f": "#C49299",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080607", "wash-a": "rgba(173,31,36,.12)", "wash-b": "rgba(196,146,153,.06)",
    "gb2": "#712321", "gb3": "#AD1F24", "gb4": "#D7ADB4", "gold-grad": "linear-gradient(135deg,#EBCDD3 0%,#C27C84 45%,#AD1F24 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
