"""Kapitalbank (JSCB Kapitalbank, Uzbekistan), as a platform: the data behind ``Kapitalbank_Platform.html``.

``python customers/build_page.py kapitalbankuz`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Kapitalbank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from kapitalbankuz_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from kapitalbankuz_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Kapitalbank'
PAGE = 'Kapitalbank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Kapitalbank Platform"
KICKER = f"JSCB Kapitalbank, Uzbekistan · as at {AS_OF}"
H1 = '<h1>Kapitalbank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Kapitalbank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Kapitalbank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Kapitalbank's colours"

PIN = (41.31, 69.28, 'Tashkent')
PIN_FACING = 'Uzbekistan and Central Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Retail banking', 'sme': 'Small business & entrepreneurs', 'corporate': 'Corporate & trade finance', 'treasury': 'Treasury & financial institutions'}
DIV = {'kb': 'Kapitalbank', 'online': 'KAPITALBANK.Online', 'premium': 'Kapital Premium & Privilege', 'uzbiz': 'Uzum Business Kapitalbank', 'uzum': 'Uzum group'}
DEFAULT_DIV = 'kb'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F7F4F2", "panel-2": "#F0EBE7", "ink": "#201A0C", "ink-2": "#453A2A",
    "muted": "#6F6B59", "faint": "#8B887A", "line": "#E0DED5", "line-2": "#CCCABF", "focus": "#B98F00",
    "accent": "#B98F00", "link": "#7E6900", "gold": "#B98F00", "gold-deep": "#8A7300", "gold-ink": "#7E6900",
    "l1": "#564700", "l2": "#8A7300", "l3": "#C8AD14", "l4": "#C8AA53", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#9C8513", "l2f": "#FBC200", "l3f": "#DCBE48", "l4f": "#D6C299",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#201A0C", "shadow": "rgba(52,39,8,.22)", "wash-a": "rgba(251,194,0,.14)",
    "wash-b": "rgba(214,194,153,.10)", "gb2": "#9C8513", "gb3": "#FBC200", "gb4": "#E5D2B2", "brand-grad": "linear-gradient(90deg,#8A7300,#FBC200 55%,#E5D2B2)",
    "gold-grad": "linear-gradient(135deg,#E5D2B2 0%,#FBC200 45%,#8A7300 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0D0A", "panel": "#201C16", "panel-2": "#312C22", "ink": "#F7F5F3", "ink-2": "#E6E1DC",
    "muted": "#CBC9C0", "faint": "#B3B1A9", "line": "#5B5645", "line-2": "#8D8772", "focus": "#FBC200",
    "accent": "#FBC200", "link": "#E5D2B2", "gold": "#FBC200", "gold-deep": "#E1C790", "gold-ink": "#E5D2B2",
    "l1": "#E5D2B2", "l2": "#DFC99C", "l3": "#E7DAA7", "l4": "#EBDCC1", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#9C8513", "l2f": "#FBC200", "l3f": "#DCBE48", "l4f": "#D6C299",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090705", "wash-a": "rgba(251,194,0,.12)", "wash-b": "rgba(214,194,153,.06)",
    "gb2": "#9C8513", "gb3": "#FBC200", "gb4": "#E5D2B2", "gold-grad": "linear-gradient(135deg,#F3E4CB 0%,#D8BF83 45%,#FBC200 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
