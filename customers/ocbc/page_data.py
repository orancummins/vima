"""OCBC, as a platform: the data behind ``OCBC_Platform.html``.

``python customers/build_page.py ocbc`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``OCBC_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from ocbc_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from ocbc_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'OCBC'
PAGE = 'OCBC_Platform.html'
AS_OF = "17 October 2026"
TITLE = "OCBC Platform"
KICKER = f"Oversea-Chinese Banking Corporation · as at {AS_OF}"
H1 = '<h1>OCBC <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: OCBC's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in OCBC's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in OCBC's colours"

PIN = (1.28, 103.85, 'Singapore')
PIN_FACING = 'Southeast Asia and Greater China'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'consumer': 'Global Consumer/Private Banking', 'wholesale': 'Global Wholesale Banking', 'markets': 'Global Markets', 'insurance': 'Insurance', 'others': 'Others'}
DIV = {'group': 'OCBC Group', 'sg': 'OCBC Singapore', 'my': 'OCBC Malaysia', 'id': 'OCBC Indonesia', 'hk': 'OCBC Hong Kong & China', 'bos': 'Bank of Singapore', 'ge': 'Great Eastern'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F3", "panel-2": "#EFE8EA", "ink": "#200E11", "ink-2": "#462E33",
    "muted": "#786364", "faint": "#8F8181", "line": "#E0D8D8", "line-2": "#D3C9C9", "focus": "#ED1C24",
    "accent": "#ED1C24", "link": "#A7100D", "gold": "#ED1C24", "gold-deep": "#860D0B", "gold-ink": "#A7100D",
    "l1": "#530807", "l2": "#860D0B", "l3": "#C52A23", "l4": "#C3656B", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#99211E", "l2f": "#ED1C24", "l3f": "#D45C5E", "l4f": "#D4A3AA",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#200E11", "shadow": "rgba(51,11,16,.22)", "wash-a": "rgba(237,28,36,.14)",
    "wash-b": "rgba(212,163,170,.10)", "gb2": "#99211E", "gb3": "#ED1C24", "gb4": "#E3B9C1", "brand-grad": "linear-gradient(90deg,#860D0B,#ED1C24 55%,#E3B9C1)",
    "gold-grad": "linear-gradient(135deg,#E3B9C1 0%,#ED1C24 45%,#860D0B 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0B0C", "panel": "#201719", "panel-2": "#312426", "ink": "#F7F3F4", "ink-2": "#E6DDE0",
    "muted": "#CDC4C5", "faint": "#B6AEAE", "line": "#5E4A4B", "line-2": "#917C7C", "focus": "#DD9CA4",
    "accent": "#D59098", "link": "#E3B9C1", "gold": "#D59098", "gold-deep": "#DD9CA4", "gold-ink": "#E3B9C1",
    "l1": "#E3B9C1", "l2": "#DCA6AD", "l3": "#E4B0B0", "l4": "#E9C7CC", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#99211E", "l2f": "#ED1C24", "l3f": "#D45C5E", "l4f": "#D4A3AA",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090607", "wash-a": "rgba(237,28,36,.12)", "wash-b": "rgba(212,163,170,.06)",
    "gb2": "#99211E", "gb3": "#ED1C24", "gb4": "#E3B9C1", "gold-grad": "linear-gradient(135deg,#F0D0D6 0%,#D59098 45%,#ED1C24 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
