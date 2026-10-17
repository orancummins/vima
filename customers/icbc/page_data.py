"""Industrial and Commercial Bank of China, as a platform: the data behind ``ICBC_Platform.html``.

``python customers/build_page.py icbc`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``ICBC_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from icbc_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from icbc_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'ICBC'
PAGE = 'ICBC_Platform.html'
AS_OF = "17 October 2026"
TITLE = "ICBC Platform"
KICKER = f"Industrial and Commercial Bank of China · as at {AS_OF}"
H1 = '<h1>ICBC <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: ICBC's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in ICBC's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in ICBC's colours"

PIN = (39.91, 116.36, 'Beijing')
PIN_FACING = 'China and Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'corporate': 'Corporate banking', 'personal': 'Personal banking', 'treasury': 'Treasury operations', 'other': 'Others'}
DIV = {'icbc': 'ICBC', 'cards': 'ICBC Card Centre (Peony)', 'subs': 'Domestic subsidiaries', 'asia': 'ICBC (Asia)', 'macau': 'ICBC (Macau)', 'argentina': 'ICBC (Argentina)', 'overseas': 'Other overseas & Standard Bank'}
DEFAULT_DIV = 'icbc'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F1F3", "panel-2": "#EFE6E9", "ink": "#1D0B0E", "ink-2": "#3B2429",
    "muted": "#796162", "faint": "#918081", "line": "#DCD0D0", "line-2": "#C8B9BA", "focus": "#C7000B",
    "accent": "#C7000B", "link": "#8D0000", "gold": "#C7000B", "gold-deep": "#730000", "gold-ink": "#8D0000",
    "l1": "#4B0000", "l2": "#730000", "l3": "#9F1410", "l4": "#B43A44", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#7F100F", "l2f": "#C7000B", "l3f": "#D0282D", "l4f": "#CE8590",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1D0B0E", "shadow": "rgba(47,7,12,.22)", "wash-a": "rgba(199,0,11,.14)",
    "wash-b": "rgba(206,133,144,.10)", "gb2": "#7F100F", "gb3": "#C7000B", "gb4": "#DFA2AE", "brand-grad": "linear-gradient(90deg,#730000,#C7000B 55%,#DFA2AE)",
    "gold-grad": "linear-gradient(135deg,#DFA2AE 0%,#C7000B 45%,#730000 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0E0A0B", "panel": "#1D1416", "panel-2": "#2B1D20", "ink": "#F7F2F4", "ink-2": "#E3D8DC",
    "muted": "#C1B4B4", "faint": "#A49798", "line": "#4B393A", "line-2": "#715B5C", "focus": "#DB7A88",
    "accent": "#D16B78", "link": "#DFA2AE", "gold": "#D16B78", "gold-deep": "#DB7A88", "gold-ink": "#DFA2AE",
    "l1": "#DFA2AE", "l2": "#D88894", "l3": "#E29597", "l4": "#E7B6BF", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#7F100F", "l2f": "#C7000B", "l3f": "#D0282D", "l4f": "#CE8590",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#080506", "wash-a": "rgba(199,0,11,.12)", "wash-b": "rgba(206,133,144,.06)",
    "gb2": "#7F100F", "gb3": "#C7000B", "gb4": "#DFA2AE", "gold-grad": "linear-gradient(135deg,#F2C6CF 0%,#D16B78 45%,#C7000B 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
