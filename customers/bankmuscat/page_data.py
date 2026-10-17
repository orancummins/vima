"""Bank Muscat, as a platform: the data behind ``Bank_Muscat_Platform.html``.

``python customers/build_page.py bankmuscat`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Bank_Muscat_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from bankmuscat_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from bankmuscat_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Bank Muscat'
PAGE = 'Bank_Muscat_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Bank Muscat Platform"
KICKER = f"Bank Muscat SAOG · as at {AS_OF}"
H1 = '<h1>Bank Muscat <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Bank Muscat's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Bank Muscat's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Bank Muscat's colours"

PIN = (23.59, 58.41, 'Muscat')
PIN_FACING = 'Oman and the Gulf'

ALLOWED_MENTIONS: tuple[str, ...] = ('Saudi',)

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'corporate': 'Corporate Banking', 'personal': 'Personal Banking', 'wholesale': 'Wholesale Banking', 'intl': 'International Banking', 'islamic': 'Islamic Banking (Meethaq)'}
DIV = {'bm': 'Bank Muscat', 'meethaq': 'Meethaq Islamic Banking', 'premier': 'Al Jawhar, Asalah & Private Banking', 'hisaby': 'Hisaby', 'intl': 'Saudi branch & representative offices'}
DEFAULT_DIV = 'bm'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F3F4", "panel-2": "#F0E9EB", "ink": "#200F12", "ink-2": "#493237",
    "muted": "#A08D8E", "faint": "#AFA6A6", "line": "#E2DADB", "line-2": "#D7CECF", "focus": "#E83840",
    "accent": "#E83840", "link": "#AE1614", "gold": "#E83840", "gold-deep": "#8A1110", "gold-ink": "#AE1614",
    "l1": "#540A0A", "l2": "#8A1110", "l3": "#CF322C", "l4": "#C6767C", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#A02725", "l2f": "#E83840", "l3f": "#D46F71", "l4f": "#D7ADB3",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#200F12", "shadow": "rgba(51,13,18,.22)", "wash-a": "rgba(232,56,64,.14)",
    "wash-b": "rgba(215,173,179,.10)", "gb2": "#A02725", "gb3": "#E83840", "gb4": "#E4C1C8", "brand-grad": "linear-gradient(90deg,#8A1110,#E83840 55%,#E4C1C8)",
    "gold-grad": "linear-gradient(135deg,#E4C1C8 0%,#E83840 45%,#8A1110 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0B0C", "panel": "#21181A", "panel-2": "#342629", "ink": "#F7F3F5", "ink-2": "#E6DFE1",
    "muted": "#D2CACA", "faint": "#BDB6B6", "line": "#645152", "line-2": "#9B8989", "focus": "#E83840",
    "accent": "#E83840", "link": "#E4C1C8", "gold": "#E83840", "gold-deep": "#DEA7AF", "gold-ink": "#E4C1C8",
    "l1": "#E4C1C8", "l2": "#DDB0B6", "l3": "#E5B9BA", "l4": "#E9CCD1", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#A02725", "l2f": "#E83840", "l3f": "#D46F71", "l4f": "#D7ADB3",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090607", "wash-a": "rgba(232,56,64,.12)", "wash-b": "rgba(215,173,179,.06)",
    "gb2": "#A02725", "gb3": "#E83840", "gb4": "#E4C1C8", "gold-grad": "linear-gradient(135deg,#F0D3D9 0%,#D69DA3 45%,#E83840 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
