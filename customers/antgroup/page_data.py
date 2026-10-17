"""Ant International, as a platform: the data behind ``Ant_International_Platform.html``.

``python customers/build_page.py antgroup`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Ant_International_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from antgroup_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from antgroup_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Ant International'
PAGE = 'Ant_International_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Ant International Platform"
KICKER = f"Ant International · as at {AS_OF}"
H1 = '<h1>Ant International <span class="os">Platform</span></h1>'
SERVES = 'who Ant International serves'

PALETTE_NOTE = ("Palette: Ant International's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Ant International's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Ant International's colours"

PIN = (1.28, 103.85, 'Singapore')
PIN_FACING = 'Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'wallet': 'Alipay+', 'merchant': 'Antom', 'account': 'WorldFirst', 'credit': 'Bettr', 'grp': 'Group'}
DIV = {'ai': 'Ant International', 'aplus': 'Alipay+', 'antom': 'Antom', 'c2p': '2C2P', 'msp': 'MultiSafepay', 'wf': 'WorldFirst', 'bettr': 'Bettr & ANEXT Bank', 'grp': 'Ant Group (context)'}
DEFAULT_DIV = 'ai'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F5F7", "panel-2": "#E7EDF0", "ink": "#0D1721", "ink-2": "#2A3A46",
    "muted": "#626C7A", "faint": "#818792", "line": "#D6DAE0", "line-2": "#C6CBD2", "focus": "#0066FF",
    "accent": "#0066FF", "link": "#003CAF", "gold": "#0066FF", "gold-deep": "#00308C", "gold-ink": "#003CAF",
    "l1": "#001E57", "l2": "#00308C", "l3": "#144FCB", "l4": "#5687C9", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#13429E", "l2f": "#0066FF", "l3f": "#4A82DD", "l4f": "#9BB9D7",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0D1721", "shadow": "rgba(8,29,53,.22)", "wash-a": "rgba(0,102,255,.14)",
    "wash-b": "rgba(155,185,215,.10)", "gb2": "#13429E", "gb3": "#0066FF", "gb4": "#B3CEE5", "brand-grad": "linear-gradient(90deg,#00308C,#0066FF 55%,#B3CEE5)",
    "gold-grad": "linear-gradient(135deg,#B3CEE5 0%,#0066FF 45%,#00308C 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0D0F", "panel": "#161C20", "panel-2": "#222A31", "ink": "#F3F6F7", "ink-2": "#DCE2E6",
    "muted": "#C1C5CC", "faint": "#AAAEB4", "line": "#464F5C", "line-2": "#747F8F", "focus": "#92B9E1",
    "accent": "#85ADD9", "link": "#B3CEE5", "gold": "#85ADD9", "gold-deep": "#92B9E1", "gold-ink": "#B3CEE5",
    "l1": "#B3CEE5", "l2": "#9DBEDF", "l3": "#A8BFE7", "l4": "#C2D8EB", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#13429E", "l2f": "#0066FF", "l3f": "#4A82DD", "l4f": "#9BB9D7",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050809", "wash-a": "rgba(0,102,255,.12)", "wash-b": "rgba(155,185,215,.06)",
    "gb2": "#13429E", "gb3": "#0066FF", "gb4": "#B3CEE5", "gold-grad": "linear-gradient(135deg,#CCE2F3 0%,#85ADD9 45%,#0066FF 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
