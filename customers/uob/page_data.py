"""UOB, as a platform: the data behind ``UOB_Platform.html``.

``python customers/build_page.py uob`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``UOB_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from uob_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from uob_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'UOB'
PAGE = 'UOB_Platform.html'
AS_OF = "17 October 2026"
TITLE = "UOB Platform"
KICKER = f"United Overseas Bank · as at {AS_OF}"
H1 = '<h1>UOB <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: UOB's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in UOB's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in UOB's colours"

PIN = (1.28, 103.85, 'Singapore')
PIN_FACING = 'Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'retail': 'Group Retail', 'gwb': 'Group Wholesale Banking', 'gm': 'Global Markets', 'oth': 'Others'}
DIV = {'uob': 'UOB Group', 'sg': 'UOB Singapore', 'my': 'UOB Malaysia', 'th': 'UOB Thailand', 'id': 'UOB Indonesia', 'vn': 'UOB Vietnam', 'tmrw': 'UOB TMRW', 'infinity': 'UOB Infinity'}
DEFAULT_DIV = 'uob'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F5F6", "panel-2": "#E5EDEF", "ink": "#0B161D", "ink-2": "#223138",
    "muted": "#5B6672", "faint": "#7A838C", "line": "#CED5DB", "line-2": "#B6BEC6", "focus": "#005CB9",
    "accent": "#005CB9", "link": "#003A84", "gold": "#005CB9", "gold-deep": "#00306D", "gold-ink": "#003A84",
    "l1": "#002048", "l2": "#00306D", "l3": "#0F4795", "l4": "#3774AB", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0E3C78", "l2f": "#005CB9", "l3f": "#2672C6", "l4f": "#80ADCC",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0B161D", "shadow": "rgba(7,29,45,.22)", "wash-a": "rgba(0,92,185,.14)",
    "wash-b": "rgba(128,173,204,.10)", "gb2": "#0E3C78", "gb3": "#005CB9", "gb4": "#9EC7DE", "brand-grad": "linear-gradient(90deg,#00306D,#005CB9 55%,#9EC7DE)",
    "gold-grad": "linear-gradient(135deg,#9EC7DE 0%,#005CB9 45%,#00306D 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0C0E", "panel": "#13191C", "panel-2": "#1C2429", "ink": "#F2F6F7", "ink-2": "#D7E0E2",
    "muted": "#B0B7BE", "faint": "#9399A0", "line": "#363E46", "line-2": "#555F69", "focus": "#74AFD9",
    "accent": "#64A1CE", "link": "#9EC7DE", "gold": "#64A1CE", "gold-deep": "#74AFD9", "gold-ink": "#9EC7DE",
    "l1": "#9EC7DE", "l2": "#82B4D6", "l3": "#90B6E1", "l4": "#B3D3E6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0E3C78", "l2f": "#005CB9", "l3f": "#2672C6", "l4f": "#80ADCC",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,92,185,.12)", "wash-b": "rgba(128,173,204,.06)",
    "gb2": "#0E3C78", "gb3": "#005CB9", "gb4": "#9EC7DE", "gold-grad": "linear-gradient(135deg,#C4E2F1 0%,#64A1CE 45%,#005CB9 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
