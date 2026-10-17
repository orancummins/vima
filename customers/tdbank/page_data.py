"""TD Bank Group, as a platform: the data behind ``TD_Bank_Group_Platform.html``.

``python customers/build_page.py tdbank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``TD_Bank_Group_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from tdbank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from tdbank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'TD'
PAGE = 'TD_Bank_Group_Platform.html'
AS_OF = "17 October 2026"
TITLE = "TD Platform"
KICKER = f"TD Bank Group · as at {AS_OF}"
H1 = '<h1>TD <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: TD's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in TD's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in TD's colours"

PIN = (43.65, -79.38, 'Toronto')
PIN_FACING = 'Canada and the US'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'cpcb': 'Canadian Personal & Commercial Banking', 'usb': 'U.S. Banking', 'wmi': 'Wealth Management & Insurance', 'wholesale': 'Wholesale Banking', 'corp': 'Corporate'}
DIV = {'td': 'TD Bank Group', 'tdct': 'TD Canada Trust', 'mbna': 'MBNA', 'tdus': 'TD Bank (US)', 'partner': 'TD Bank USA partner cards', 'tdms': 'TD Merchant Solutions', 'wealth': 'TD Wealth & TD Insurance', 'tds': 'TD Securities & TD Cowen'}
DEFAULT_DIV = 'td'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F4F5F3", "panel-2": "#EBEDE9", "ink": "#141B12", "ink-2": "#363F32",
    "muted": "#636C62", "faint": "#828981", "line": "#D9DED9", "line-2": "#C7CDC7", "focus": "#4BA740",
    "accent": "#4BA740", "link": "#31782E", "gold": "#4BA740", "gold-deep": "#2A6627", "gold-ink": "#31782E",
    "l1": "#1A3F18", "l2": "#2A6627", "l3": "#499947", "l4": "#7EAA77", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#3D783A", "l2f": "#54B948", "l3f": "#79B574", "l4f": "#B2C7AC",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#141B12", "shadow": "rgba(24,41,20,.22)", "wash-a": "rgba(84,185,72,.14)",
    "wash-b": "rgba(178,199,172,.10)", "gb2": "#3D783A", "gb3": "#54B948", "gb4": "#C7D8C1", "brand-grad": "linear-gradient(90deg,#2A6627,#54B948 55%,#C7D8C1)",
    "gold-grad": "linear-gradient(135deg,#C7D8C1 0%,#54B948 45%,#2A6627 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0C0E0C", "panel": "#1A1E19", "panel-2": "#282D26", "ink": "#F5F6F4", "ink-2": "#E0E3DF",
    "muted": "#C5C9C5", "faint": "#AEB2AD", "line": "#4E574D", "line-2": "#7E887D", "focus": "#54B948",
    "accent": "#54B948", "link": "#C7D8C1", "gold": "#54B948", "gold-deep": "#B0CCA9", "gold-ink": "#C7D8C1",
    "l1": "#C7D8C1", "l2": "#B6CDB0", "l3": "#BCD6BA", "l4": "#D2E0CD", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#3D783A", "l2f": "#54B948", "l3f": "#79B574", "l4f": "#B2C7AC",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#070806", "wash-a": "rgba(84,185,72,.12)", "wash-b": "rgba(178,199,172,.06)",
    "gb2": "#3D783A", "gb3": "#54B948", "gb4": "#C7D8C1", "gold-grad": "linear-gradient(135deg,#DBE8D7 0%,#A4C29D 45%,#54B948 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
