"""ANZ Group, as a platform: the data behind ``ANZ_Platform.html``.

``python customers/build_page.py anz`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``ANZ_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from anz_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from anz_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'ANZ'
PAGE = 'ANZ_Platform.html'
AS_OF = "17 October 2026"
TITLE = "ANZ Platform"
KICKER = f"ANZ Group Holdings · as at {AS_OF}"
H1 = '<h1>ANZ <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: ANZ's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in ANZ's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in ANZ's colours"

PIN = (-37.82, 144.95, 'Melbourne')
PIN_FACING = 'Australia, New Zealand and the Pacific'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Australia Retail', 'bpb': 'Business & Private Bank', 'inst': 'Institutional', 'nz': 'New Zealand', 'suncorp': 'Suncorp Bank', 'centre': 'Pacific & Group Centre'}
DIV = {'group': 'ANZ Group', 'anz': 'ANZ', 'plus': 'ANZ Plus', 'suncorp': 'Suncorp Bank', 'anznz': 'ANZ New Zealand', 'worldline': 'ANZ Worldline', 'inst': 'ANZ Institutional'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F6", "panel-2": "#E5EEEF", "ink": "#0B191D", "ink-2": "#223538",
    "muted": "#5B6B73", "faint": "#7B868C", "line": "#CED7DB", "line-2": "#B6C1C6", "focus": "#007DBA",
    "accent": "#007DBA", "link": "#005185", "gold": "#007DBA", "gold-deep": "#00436D", "gold-ink": "#005185",
    "l1": "#002C48", "l2": "#00436D", "l3": "#0F5E95", "l4": "#3789AC", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0E4F78", "l2f": "#007DBA", "l3f": "#268FC7", "l4f": "#80BBCC",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0B191D", "shadow": "rgba(7,36,45,.22)", "wash-a": "rgba(0,125,186,.14)",
    "wash-b": "rgba(128,187,204,.10)", "gb2": "#0E4F78", "gb3": "#007DBA", "gb4": "#9ED2DE", "brand-grad": "linear-gradient(90deg,#00436D,#007DBA 55%,#9ED2DE)",
    "gold-grad": "linear-gradient(135deg,#9ED2DE 0%,#007DBA 45%,#00436D 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0D0E", "panel": "#131B1C", "panel-2": "#1C2629", "ink": "#F2F7F7", "ink-2": "#D7E2E2",
    "muted": "#B0BABE", "faint": "#939CA0", "line": "#364147", "line-2": "#55636A", "focus": "#75C1D9",
    "accent": "#64B4CF", "link": "#9ED2DE", "gold": "#64B4CF", "gold-deep": "#75C1D9", "gold-ink": "#9ED2DE",
    "l1": "#9ED2DE", "l2": "#83C3D6", "l3": "#90C4E1", "l4": "#B3DCE6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0E4F78", "l2f": "#007DBA", "l3f": "#268FC7", "l4f": "#80BBCC",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,125,186,.12)", "wash-b": "rgba(128,187,204,.06)",
    "gb2": "#0E4F78", "gb3": "#007DBA", "gb4": "#9ED2DE", "gold-grad": "linear-gradient(135deg,#C4EAF1 0%,#64B4CF 45%,#007DBA 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
