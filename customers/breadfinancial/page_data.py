"""Bread Financial, as a platform: the data behind ``Bread_Financial_Platform.html``.

``python customers/build_page.py breadfinancial`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Bread_Financial_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from breadfinancial_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from breadfinancial_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Bread Financial'
PAGE = 'Bread_Financial_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Bread Financial Platform"
KICKER = f"Bread Financial Holdings · as at {AS_OF}"
H1 = '<h1>Bread Financial <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Bread Financial's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Bread Financial's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Bread Financial's colours"

PIN = (39.96, -83.0, 'Columbus')
PIN_FACING = 'the Americas'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'grp': 'Group', 'cobrand': 'Co-brand cards', 'pl': 'Private label', 'dtc': 'Direct to consumer', 'pay': 'Bread Pay'}
DIV = {'grp': 'Bread Financial', 'ccb': 'Comenity Capital Bank', 'cb': 'Comenity Bank', 'breadpay': 'Bread Pay', 'savings': 'Bread Savings', 'cashback': 'Bread Cashback'}
DEFAULT_DIV = 'grp'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F4F5", "panel-2": "#E5E9EB", "ink": "#0C1015", "ink-2": "#1A1F23",
    "muted": "#383B40", "faint": "#5C5F64", "line": "#C8CBD1", "line-2": "#A6ABB2", "focus": "#13294B",
    "accent": "#13294B", "link": "#101F3E", "gold": "#13294B", "gold-deep": "#0E1C37", "gold-ink": "#101F3E",
    "l1": "#0B152A", "l2": "#0E1C37", "l3": "#162340", "l4": "#334660", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#152139", "l2f": "#13294B", "l3f": "#2F4770", "l4f": "#708CAA",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0C1015", "shadow": "rgba(11,20,29,.22)", "wash-a": "rgba(19,41,75,.14)",
    "wash-b": "rgba(112,140,170,.10)", "gb2": "#152139", "gb3": "#13294B", "gb4": "#93ADC4", "brand-grad": "linear-gradient(90deg,#0E1C37,#13294B 55%,#93ADC4)",
    "gold-grad": "linear-gradient(135deg,#93ADC4 0%,#13294B 45%,#0E1C37 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090B0C", "panel": "#111315", "panel-2": "#17191C", "ink": "#F3F5F6", "ink-2": "#D4D9DB",
    "muted": "#9EA2A8", "faint": "#787C81", "line": "#222528", "line-2": "#34373B", "focus": "#688CB4",
    "accent": "#587CA7", "link": "#93ADC4", "gold": "#587CA7", "gold-deep": "#688CB4", "gold-ink": "#93ADC4",
    "l1": "#93ADC4", "l2": "#7595B5", "l3": "#869CC3", "l4": "#ADC1D3", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#152139", "l2f": "#13294B", "l3f": "#2F4770", "l4f": "#708CAA",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050707", "wash-a": "rgba(19,41,75,.12)", "wash-b": "rgba(112,140,170,.06)",
    "gb2": "#152139", "gb3": "#13294B", "gb4": "#93ADC4", "gold-grad": "linear-gradient(135deg,#C5D6E4 0%,#567AA4 45%,#13294B 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
