"""Samsung, as a platform: the data behind ``Samsung_Platform.html``.

``python customers/build_page.py samsung`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Samsung_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from samsung_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from samsung_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Samsung'
PAGE = 'Samsung_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Samsung Platform"
KICKER = f"Samsung Electronics, read through Samsung Wallet · as at {AS_OF}"
H1 = '<h1>Samsung <span class="os">Platform</span></h1>'
SERVES = 'who Samsung Wallet serves'

PALETTE_NOTE = ("Palette: Samsung's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Samsung's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Samsung's colours"

PIN = (37.26, 127.03, 'Suwon')
PIN_FACING = 'Korea and Asia-Pacific'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'mx': 'MX & Networks', 'ds': 'Device Solutions (chips)', 'ce': 'TVs & appliances', 'grp': 'Corporate'}
DIV = {'wallet': 'Samsung Wallet', 'kr': 'Samsung Wallet Korea', 'us': 'Samsung Electronics America', 'eu': 'Samsung Europe', 'asia': 'Samsung Asia entities', 'knox': 'Samsung Knox', 'grp': 'Samsung Electronics Co., Ltd.'}
DEFAULT_DIV = 'wallet'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F3F6", "panel-2": "#E6E9EE", "ink": "#0D101B", "ink-2": "#242935",
    "muted": "#5B5E6D", "faint": "#7A7C88", "line": "#CFD1D9", "line-2": "#B7B9C3", "focus": "#1428A0",
    "accent": "#1428A0", "link": "#0E1773", "gold": "#1428A0", "gold-deep": "#0C135F", "gold-ink": "#0E1773",
    "l1": "#080D3F", "l2": "#0C135F", "l3": "#1D2382", "l4": "#42519B", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#192069", "l2f": "#1428A0", "l3f": "#3745B1", "l4f": "#8695C2",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0D101B", "shadow": "rgba(11,18,41,.22)", "wash-a": "rgba(20,40,160,.14)",
    "wash-b": "rgba(134,149,194,.10)", "gb2": "#192069", "gb3": "#1428A0", "gb4": "#A4B2D6", "brand-grad": "linear-gradient(90deg,#0C135F,#1428A0 55%,#A4B2D6)",
    "gold-grad": "linear-gradient(135deg,#A4B2D6 0%,#1428A0 45%,#0C135F 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0B0D", "panel": "#14161B", "panel-2": "#1D2027", "ink": "#F3F4F7", "ink-2": "#D8DCE1",
    "muted": "#B0B2BB", "faint": "#92949D", "line": "#363843", "line-2": "#555764", "focus": "#7E90CD",
    "accent": "#6E80C2", "link": "#A4B2D6", "gold": "#6E80C2", "gold-deep": "#7E90CD", "gold-ink": "#A4B2D6",
    "l1": "#A4B2D6", "l2": "#8A9ACC", "l3": "#979ED7", "l4": "#B8C3E0", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#192069", "l2f": "#1428A0", "l3f": "#3745B1", "l4f": "#8695C2",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060708", "wash-a": "rgba(20,40,160,.12)", "wash-b": "rgba(134,149,194,.06)",
    "gb2": "#192069", "gb3": "#1428A0", "gb4": "#A4B2D6", "gold-grad": "linear-gradient(135deg,#C9D3EC 0%,#6E80C2 45%,#1428A0 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
