"""Arab Bank, as a platform: the data behind ``Arab_Bank_Platform.html``.

``python customers/build_page.py arabbank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Arab_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from arabbank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from arabbank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Arab Bank'
PAGE = 'Arab_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Arab Bank Platform"
KICKER = f"Arab Bank plc · as at {AS_OF}"
H1 = '<h1>Arab Bank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Arab Bank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Arab Bank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Arab Bank's colours"

PIN = (31.95, 35.91, 'Amman')
PIN_FACING = 'Jordan, the Levant and the Gulf'

ALLOWED_MENTIONS: tuple[str, ...] = ('Saudi',)

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'consumer': 'Consumer Banking & Wealth Management', 'cib': 'Corporate & Institutional Banking', 'treasury': 'Treasury', 'group': 'Group & other'}
DIV = {'abg': 'Arab Bank Group', 'jordan': 'Arab Bank (Jordan)', 'reflect': 'Reflect', 'acabes': 'Acabes', 'regional': 'Regional branches & subsidiaries', 'swiss': 'Arab Bank Switzerland'}
DEFAULT_DIV = 'abg'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F2F3F7", "panel-2": "#E7E9F0", "ink": "#0D0D21", "ink-2": "#2B2D46",
    "muted": "#686680", "faint": "#858494", "line": "#D7D6E1", "line-2": "#C7C6D2", "focus": "#1501FF",
    "accent": "#1501FF", "link": "#1800AF", "gold": "#1501FF", "gold-deep": "#13008C", "gold-ink": "#1800AF",
    "l1": "#0C0057", "l2": "#13008C", "l3": "#3214CC", "l4": "#5C57C9", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#27139F", "l2f": "#1501FF", "l3f": "#5A4BDD", "l4f": "#9B9DD7",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#0D0D21", "shadow": "rgba(8,8,53,.22)", "wash-a": "rgba(21,1,255,.14)",
    "wash-b": "rgba(155,157,215,.10)", "gb2": "#27139F", "gb3": "#1501FF", "gb4": "#B3B6E5", "brand-grad": "linear-gradient(90deg,#13008C,#1501FF 55%,#B3B6E5)",
    "gold-grad": "linear-gradient(135deg,#B3B6E5 0%,#1501FF 45%,#13008C 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0B0F", "panel": "#161720", "panel-2": "#222332", "ink": "#F3F4F7", "ink-2": "#DCDEE6",
    "muted": "#C2C1CC", "faint": "#ABAAB4", "line": "#48475D", "line-2": "#77758F", "focus": "#9393E1",
    "accent": "#8686D9", "link": "#B3B6E5", "gold": "#8686D9", "gold-deep": "#9393E1", "gold-ink": "#B3B6E5",
    "l1": "#B3B6E5", "l2": "#9D9FDF", "l3": "#AFA8E7", "l4": "#C2C4EB", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#27139F", "l2f": "#1501FF", "l3f": "#5A4BDD", "l4f": "#9B9DD7",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050609", "wash-a": "rgba(21,1,255,.12)", "wash-b": "rgba(155,157,215,.06)",
    "gb2": "#27139F", "gb3": "#1501FF", "gb4": "#B3B6E5", "gold-grad": "linear-gradient(135deg,#CCCFF3 0%,#8686D9 45%,#1501FF 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
