"""BDO Unibank, as a platform: the data behind ``BDO_Unibank_Platform.html``.

``python customers/build_page.py bdo`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``BDO_Unibank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bdo_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bdo_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'BDO'
PAGE = 'BDO_Unibank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "BDO Platform"
KICKER = f"BDO Unibank · as at {AS_OF}"
H1 = '<h1>BDO <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: BDO's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in BDO's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in BDO's colours"

PIN = (14.55, 121.02, 'Makati')
PIN_FACING = 'the Philippines and South-East Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'corporate': 'Corporate Banking', 'commercial': 'Commercial & MSME Banking', 'consumer': 'Consumer Banking', 'wealth': 'Trust, Wealth & Insurance', 'group': 'Group & Treasury'}
DIV = {'bdo': 'BDO Unibank', 'pay': 'BDO Pay', 'cards': 'BDO Credit Cards', 'remit': 'BDO Remit', 'network': 'BDO Network Bank', 'private': 'BDO Private Bank', 'life': 'BDO Life', 'capital': 'BDO Capital & Securities'}
DEFAULT_DIV = 'bdo'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F4F6", "panel-2": "#E5E9ED", "ink": "#0B1018", "ink-2": "#1C232B",
    "muted": "#434751", "faint": "#666A73", "line": "#C9CDD5", "line-2": "#AAAFBA", "focus": "#0B2972",
    "accent": "#0B2972", "link": "#081B58", "gold": "#0B2972", "gold-deep": "#07174B", "gold-ink": "#081B58",
    "l1": "#051136", "l2": "#07174B", "l3": "#12225E", "l4": "#32497B", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#111F50", "l2f": "#0B2972", "l3f": "#294591", "l4f": "#708DBA",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0B1018", "shadow": "rgba(9,19,36,.22)", "wash-a": "rgba(11,41,114,.14)",
    "wash-b": "rgba(112,141,186,.10)", "gb2": "#111F50", "gb3": "#0B2972", "gb4": "#93AED1", "brand-grad": "linear-gradient(90deg,#07174B,#0B2972 55%,#93AED1)",
    "gold-grad": "linear-gradient(135deg,#93AED1 0%,#0B2972 45%,#07174B 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090B0C", "panel": "#111418", "panel-2": "#181C21", "ink": "#F2F5F7", "ink-2": "#D4DADE",
    "muted": "#A3A7B1", "faint": "#80848D", "line": "#292C33", "line-2": "#3C3F47", "focus": "#658BC7",
    "accent": "#567BBB", "link": "#93AED1", "gold": "#567BBB", "gold-deep": "#658BC7", "gold-ink": "#93AED1",
    "l1": "#93AED1", "l2": "#7494C6", "l3": "#8498D3", "l4": "#ACC1DD", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#111F50", "l2f": "#0B2972", "l3f": "#294591", "l4f": "#708DBA",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050708", "wash-a": "rgba(11,41,114,.12)", "wash-b": "rgba(112,141,186,.06)",
    "gb2": "#111F50", "gb3": "#0B2972", "gb4": "#93AED1", "gold-grad": "linear-gradient(135deg,#C2D5EB 0%,#5278BA 45%,#0B2972 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
