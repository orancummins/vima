"""Intesa Sanpaolo, as a platform: the data behind ``Intesa_Sanpaolo_Platform.html``.

``python customers/build_page.py intesa`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Intesa_Sanpaolo_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from intesa_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from intesa_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Intesa Sanpaolo'
PAGE = 'Intesa_Sanpaolo_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Intesa Sanpaolo Platform"
KICKER = f"Intesa Sanpaolo · as at {AS_OF}"
H1 = '<h1>Intesa Sanpaolo <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Intesa Sanpaolo's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Intesa Sanpaolo's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Intesa Sanpaolo's colours"

PIN = (45.07, 7.69, 'Turin')
PIN_FACING = 'Italy and Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'bdt': 'Banca dei Territori', 'imi': 'IMI Corporate & Investment Banking', 'ibd': 'International Banks', 'wm': 'Private Banking, Asset Management & Insurance', 'cc': 'Corporate Centre'}
DIV = {'isp': 'Intesa Sanpaolo', 'isybank': 'Isybank', 'fideuram': 'Fideuram', 'eurizon': 'Eurizon', 'imi': 'IMI CIB', 'insurance': 'Intesa Sanpaolo Assicurazioni', 'intl': 'International subsidiary banks'}
DEFAULT_DIV = 'isp'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F4F6F1", "panel-2": "#E9EEE4", "ink": "#101A0A", "ink-2": "#242E1C",
    "muted": "#4C5947", "faint": "#6D7969", "line": "#CDD7C9", "line-2": "#B0BDAB", "focus": "#258900",
    "accent": "#258900", "link": "#166700", "gold": "#258900", "gold-deep": "#135800", "gold-ink": "#166700",
    "l1": "#0D3D00", "l2": "#135800", "l3": "#1E700B", "l4": "#498B2C", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#1C5D0B", "l2f": "#258900", "l3f": "#40A41F", "l4f": "#8DC46D",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#101A0A", "shadow": "rgba(18,40,6,.22)", "wash-a": "rgba(37,137,0,.14)",
    "wash-b": "rgba(141,196,109,.10)", "gb2": "#1C5D0B", "gb3": "#258900", "gb4": "#AED990", "brand-grad": "linear-gradient(90deg,#135800,#258900 55%,#AED990)",
    "gold-grad": "linear-gradient(135deg,#AED990 0%,#258900 45%,#135800 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0B0D09", "panel": "#151911", "panel-2": "#1C2318", "ink": "#F5F7F2", "ink-2": "#DAE0D4",
    "muted": "#A9B4A4", "faint": "#879283", "line": "#2E382A", "line-2": "#444F40", "focus": "#89D360",
    "accent": "#77C74D", "link": "#AED990", "gold": "#77C74D", "gold-deep": "#89D360", "gold-ink": "#AED990",
    "l1": "#AED990", "l2": "#93D070", "l3": "#96DC80", "l4": "#C1E3A9", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#1C5D0B", "l2f": "#258900", "l3f": "#40A41F", "l4f": "#8DC46D",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#070805", "wash-a": "rgba(37,137,0,.12)", "wash-b": "rgba(141,196,109,.06)",
    "gb2": "#1C5D0B", "gb3": "#258900", "gb4": "#AED990", "gold-grad": "linear-gradient(135deg,#D4F0BF 0%,#77C74D 45%,#258900 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
