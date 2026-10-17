"""Isracard, as a platform: the data behind ``Isracard_Platform.html``.

``python customers/build_page.py isracard`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Isracard_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from isracard_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from isracard_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Isracard'
PAGE = 'Isracard_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Isracard Platform"
KICKER = f"Isracard Ltd · as at {AS_OF}"
H1 = '<h1>Isracard <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Isracard's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Isracard's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Isracard's colours"

PIN = (32.08, 34.83, 'Bnei Brak')
PIN_FACING = 'Israel'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'private': 'Private customers', 'business': 'Business customers', 'group': 'Group & other'}
DIV = {'isracard': 'Isracard', 'amex': 'American Express Israel', 'europay': 'Europay (Eurocard) Israel', 'finance': 'Isracard Finance', 'insurance': 'Isracard Insurance Agency', 'flycard': 'FLY CARD (El Al club)', 'delek': 'Delek Group'}
DEFAULT_DIV = 'isracard'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F3F4", "panel-2": "#E5E8E9", "ink": "#0D0F11", "ink-2": "#151819",
    "muted": "#252628", "faint": "#4D4F51", "line": "#C5C8CB", "line-2": "#9FA3A6", "focus": "#101820",
    "accent": "#101820", "link": "#101821", "gold": "#101820", "gold-deep": "#101720", "gold-ink": "#101821",
    "l1": "#0E141C", "l2": "#101720", "l3": "#11161E", "l4": "#2C353E", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#12181F", "l2f": "#101820", "l3f": "#2F3C4A", "l4f": "#6E8492",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0D0F11", "shadow": "rgba(13,18,22,.22)", "wash-a": "rgba(16,24,32,.14)",
    "wash-b": "rgba(110,132,146,.10)", "gb2": "#12181F", "gb3": "#101820", "gb4": "#93A7B2", "brand-grad": "linear-gradient(90deg,#101720,#101820 55%,#93A7B2)",
    "gold-grad": "linear-gradient(135deg,#93A7B2 0%,#101820 45%,#101720 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090A0A", "panel": "#0F1112", "panel-2": "#131516", "ink": "#F3F5F5", "ink-2": "#D3D6D7",
    "muted": "#95999C", "faint": "#6C6E71", "line": "#222325", "line-2": "#343637", "focus": "#6A8699",
    "accent": "#667E90", "link": "#93A7B2", "gold": "#667E90", "gold-deep": "#6A8699", "gold-ink": "#93A7B2",
    "l1": "#93A7B2", "l2": "#758D9D", "l3": "#8799AE", "l4": "#AFBDC6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#12181F", "l2f": "#101820", "l3f": "#2F3C4A", "l4f": "#6E8492",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#060607", "wash-a": "rgba(16,24,32,.12)", "wash-b": "rgba(110,132,146,.06)",
    "gb2": "#12181F", "gb3": "#101820", "gb4": "#93A7B2", "gold-grad": "linear-gradient(135deg,#C8D5DB 0%,#5B7181 45%,#101820 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
