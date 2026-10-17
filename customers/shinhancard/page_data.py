"""Shinhan Card, as a platform: the data behind ``Shinhan_Card_Platform.html``.

``python customers/build_page.py shinhancard`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Shinhan_Card_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from shinhancard_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from shinhancard_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Shinhan Card'
PAGE = 'Shinhan_Card_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Shinhan Card Platform"
KICKER = f"Shinhan Card Co. (Shinhan Financial Group) · as at {AS_OF}"
H1 = '<h1>Shinhan Card <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Shinhan Card's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Shinhan Card's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Shinhan Card's colours"

PIN = (37.566, 126.986, 'Seoul')
PIN_FACING = 'Korea and Asia-Pacific'

ALLOWED_MENTIONS: tuple[str, ...] = ('CLASSIC NEO',)

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'card': 'Card business', 'finance': 'Card loans & consumer finance', 'auto': 'Lease & instalment finance', 'other': 'Overseas & other'}
DIV = {'shc': 'Shinhan Card', 'sfg': 'Shinhan Financial Group', 'solpay': 'SOL Pay', 'mycar': 'Shinhan MyCar', 'data': 'Data Bada & GranData', 'overseas': 'Overseas subsidiaries'}
DEFAULT_DIV = 'shc'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F4F6", "panel-2": "#E7ECF0", "ink": "#0C1420", "ink-2": "#2A3544",
    "muted": "#767D92", "faint": "#9498A2", "line": "#D5D8E0", "line-2": "#C4C8D1", "focus": "#0040F8",
    "accent": "#0040F8", "link": "#0022AA", "gold": "#0040F8", "gold-deep": "#001B89", "gold-ink": "#0022AA",
    "l1": "#001155", "l2": "#001B89", "l3": "#1433C5", "l4": "#5173C8", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#122D9A", "l2f": "#0040F8", "l3f": "#4669DC", "l4f": "#98AED6",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0C1420", "shadow": "rgba(8,23,52,.22)", "wash-a": "rgba(0,64,248,.14)",
    "wash-b": "rgba(152,174,214,.10)", "gb2": "#122D9A", "gb3": "#0040F8", "gb4": "#B1C5E4", "brand-grad": "linear-gradient(90deg,#001B89,#0040F8 55%,#B1C5E4)",
    "gold-grad": "linear-gradient(135deg,#B1C5E4 0%,#0040F8 45%,#001B89 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0C0F", "panel": "#161A20", "panel-2": "#212731", "ink": "#F3F5F7", "ink-2": "#DCE1E5",
    "muted": "#BFC2CB", "faint": "#A8AAB2", "line": "#454A5A", "line-2": "#71788C", "focus": "#8FABE0",
    "accent": "#829ED8", "link": "#B1C5E4", "gold": "#829ED8", "gold-deep": "#8FABE0", "gold-ink": "#B1C5E4",
    "l1": "#B1C5E4", "l2": "#9AB3DE", "l3": "#A6B4E7", "l4": "#C0D1EB", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#122D9A", "l2f": "#0040F8", "l3f": "#4669DC", "l4f": "#98AED6",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050709", "wash-a": "rgba(0,64,248,.12)", "wash-b": "rgba(152,174,214,.06)",
    "gb2": "#122D9A", "gb3": "#0040F8", "gb4": "#B1C5E4", "gold-grad": "linear-gradient(135deg,#CBDBF3 0%,#829ED8 45%,#0040F8 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
