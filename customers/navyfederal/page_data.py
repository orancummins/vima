"""Navy Federal Credit Union, as a platform: the data behind ``Navy_Federal_Credit_Union_Platform.html``.

``python customers/build_page.py navyfederal`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Navy_Federal_Credit_Union_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from navyfederal_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from navyfederal_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Navy Federal'
PAGE = 'Navy_Federal_Credit_Union_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Navy Federal Platform"
KICKER = f"Navy Federal Credit Union · as at {AS_OF}"
H1 = '<h1>Navy Federal <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Navy Federal's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Navy Federal's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Navy Federal's colours"

PIN = (38.9, -77.27, 'Vienna, Virginia')
PIN_FACING = 'the United States'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'consumer': 'Consumer lending', 'card': 'Credit cards', 'realestate': 'Real estate lending', 'deposits': 'Deposits & payments', 'cu': 'Credit union-wide'}
DIV = {'nfcu': 'Navy Federal Credit Union', 'cards': 'Navy Federal cards', 'mortgage': 'Navy Federal mortgages', 'business': 'Business Solutions', 'nfis': 'Navy Federal Investment Services', 'ombp': 'Overseas Military Banking Program'}
DEFAULT_DIV = 'nfcu'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F4F5", "panel-2": "#E5EBED", "ink": "#0C1318", "ink-2": "#1D262A",
    "muted": "#454B52", "faint": "#676D73", "line": "#CACFD5", "line-2": "#ABB2B9", "focus": "#0F3D70",
    "accent": "#0F3D70", "link": "#0B2A56", "gold": "#0F3D70", "gold-deep": "#0A244A", "gold-ink": "#0B2A56",
    "l1": "#071A34", "l2": "#0A244A", "l3": "#15315D", "l4": "#35587A", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#142C4E", "l2f": "#0F3D70", "l3f": "#2D598E", "l4f": "#739BB8",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0C1318", "shadow": "rgba(10,24,35,.22)", "wash-a": "rgba(15,61,112,.14)",
    "wash-b": "rgba(115,155,184,.10)", "gb2": "#142C4E", "gb3": "#0F3D70", "gb4": "#96B9CF", "brand-grad": "linear-gradient(90deg,#0A244A,#0F3D70 55%,#96B9CF)",
    "gold-grad": "linear-gradient(135deg,#96B9CF 0%,#0F3D70 45%,#0A244A 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090B0C", "panel": "#121518", "panel-2": "#191D21", "ink": "#F3F5F6", "ink-2": "#D5DCDE",
    "muted": "#A4AAB0", "faint": "#81878D", "line": "#2A2E33", "line-2": "#3D4248", "focus": "#6A9DC4",
    "accent": "#578CB7", "link": "#96B9CF", "gold": "#578CB7", "gold-deep": "#6A9DC4", "gold-ink": "#96B9CF",
    "l1": "#96B9CF", "l2": "#78A3C3", "l3": "#87A8D0", "l4": "#AECADB", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#142C4E", "l2f": "#0F3D70", "l3f": "#2D598E", "l4f": "#739BB8",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050708", "wash-a": "rgba(15,61,112,.12)", "wash-b": "rgba(115,155,184,.06)",
    "gb2": "#142C4E", "gb3": "#0F3D70", "gb4": "#96B9CF", "gold-grad": "linear-gradient(135deg,#C4DCEA 0%,#578CB7 45%,#0F3D70 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
