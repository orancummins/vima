"""Standard Chartered, as a platform: the data behind ``Standard_Chartered_Platform.html``.

``python customers/build_page.py stanchart`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Standard_Chartered_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from stanchart_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from stanchart_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'StanChart'
PAGE = 'Standard_Chartered_Platform.html'
AS_OF = "17 October 2026"
TITLE = "StanChart Platform"
KICKER = f"Standard Chartered PLC · as at {AS_OF}"
H1 = '<h1>StanChart <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: StanChart's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in StanChart's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in StanChart's colours"

PIN = (51.515, -0.089, 'London')
PIN_FACING = 'Asia, Africa and the Middle East'

ALLOWED_MENTIONS: tuple[str, ...] = ('Saudi',)

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'cib': 'Corporate & Investment Banking', 'wrb': 'Wealth & Retail Banking', 'co': 'Central & other items'}
DIV = {'group': 'Standard Chartered PLC', 'hk': 'Standard Chartered Hong Kong', 'sg': 'Standard Chartered Singapore', 'asia': 'South Asia & ASEAN markets', 'ame': 'Africa & Middle East', 'mox': 'Mox Bank', 'trust': 'Trust Bank', 'scv': 'SC Ventures'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F5F6", "panel-2": "#E7EDEF", "ink": "#0C181F", "ink-2": "#293942",
    "muted": "#5F6B76", "faint": "#808890", "line": "#D4D9DF", "line-2": "#C2C8CF", "focus": "#0473EA",
    "accent": "#0473EA", "link": "#0346A1", "gold": "#0473EA", "gold-deep": "#023982", "gold-ink": "#0346A1",
    "l1": "#012452", "l2": "#023982", "l3": "#1658BB", "l4": "#4D89C3", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#144993", "l2f": "#0473EA", "l3f": "#4186D8", "l4f": "#95B9D3",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0C181F", "shadow": "rgba(8,32,50,.22)", "wash-a": "rgba(4,115,234,.14)",
    "wash-b": "rgba(149,185,211,.10)", "gb2": "#144993", "gb3": "#0473EA", "gb4": "#AFCFE3", "brand-grad": "linear-gradient(90deg,#023982,#0473EA 55%,#AFCFE3)",
    "gold-grad": "linear-gradient(135deg,#AFCFE3 0%,#0473EA 45%,#023982 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0D0F", "panel": "#151C1F", "panel-2": "#21292F", "ink": "#F3F6F7", "ink-2": "#DBE2E5",
    "muted": "#BDC3C8", "faint": "#A5AAAF", "line": "#434C57", "line-2": "#6D7986", "focus": "#8CBBDE",
    "accent": "#7FAFD5", "link": "#AFCFE3", "gold": "#7FAFD5", "gold-deep": "#8CBBDE", "gold-ink": "#AFCFE3",
    "l1": "#AFCFE3", "l2": "#98BFDC", "l3": "#A3C1E4", "l4": "#BFD9E9", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#144993", "l2f": "#0473EA", "l3f": "#4186D8", "l4f": "#95B9D3",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050809", "wash-a": "rgba(4,115,234,.12)", "wash-b": "rgba(149,185,211,.06)",
    "gb2": "#144993", "gb3": "#0473EA", "gb4": "#AFCFE3", "gold-grad": "linear-gradient(135deg,#CBE4F2 0%,#7FAFD5 45%,#0473EA 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
