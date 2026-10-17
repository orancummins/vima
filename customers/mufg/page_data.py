"""Mitsubishi UFJ Financial Group, as a platform: the data behind ``MUFG_Platform.html``.

``python customers/build_page.py mufg`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``MUFG_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from mufg_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from mufg_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'MUFG'
PAGE = 'MUFG_Platform.html'
AS_OF = "17 October 2026"
TITLE = "MUFG Platform"
KICKER = f"Mitsubishi UFJ Financial Group · as at {AS_OF}"
H1 = '<h1>MUFG <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: MUFG's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in MUFG's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in MUFG's colours"

PIN = (35.68, 139.76, 'Tokyo')
PIN_FACING = 'Japan and Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'rd': 'Retail & Digital', 'cwm': 'Commercial Banking & Wealth Management', 'jcib': 'Japanese Corporate & Investment Banking', 'gcb': 'Global Commercial Banking', 'global': 'Global CIB, Markets & AM/IS'}
DIV = {'mufg': 'MUFG', 'bank': 'MUFG Bank', 'nicos': 'Mitsubishi UFJ NICOS', 'acom': 'ACOM', 'emut': 'Emut & MUFG Emut Bank', 'trust': 'Mitsubishi UFJ Trust & Securities', 'asia': 'Asian partner banks & investees'}
DEFAULT_DIV = 'mufg'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F2F3", "panel-2": "#EFE6E9", "ink": "#1F0C0E", "ink-2": "#41272C",
    "muted": "#796060", "faint": "#907F7F", "line": "#DED3D3", "line-2": "#CEC0C0", "focus": "#E60000",
    "accent": "#E60000", "link": "#9F0900", "gold": "#E60000", "gold-deep": "#810700", "gold-ink": "#9F0900",
    "l1": "#520400", "l2": "#810700", "l3": "#B72012", "l4": "#C44549", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#901911", "l2f": "#E60000", "l3f": "#D93C39", "l4f": "#D39198",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#FFFFFF", "l5t": "#FFFFFF", "slot": "#1F0C0E", "shadow": "rgba(50,8,11,.22)", "wash-a": "rgba(230,0,0,.14)",
    "wash-b": "rgba(211,145,152,.10)", "gb2": "#901911", "gb3": "#E60000", "gb4": "#E3ABB3", "brand-grad": "linear-gradient(90deg,#810700,#E60000 55%,#E3ABB3)",
    "gold-grad": "linear-gradient(135deg,#E3ABB3 0%,#E60000 45%,#810700 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0A0B", "panel": "#1F1517", "panel-2": "#2E2022", "ink": "#F7F3F4", "ink-2": "#E5DADD",
    "muted": "#C7BBBB", "faint": "#ADA2A2", "line": "#544040", "line-2": "#826969", "focus": "#DE888F",
    "accent": "#D57980", "link": "#E3ABB3", "gold": "#D57980", "gold-deep": "#DE888F", "gold-ink": "#E3ABB3",
    "l1": "#E3ABB3", "l2": "#DC939B", "l3": "#E5A29F", "l4": "#E9BCC2", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#901911", "l2f": "#E60000", "l3f": "#D93C39", "l4f": "#D39198",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090506", "wash-a": "rgba(230,0,0,.12)", "wash-b": "rgba(211,145,152,.06)",
    "gb2": "#901911", "gb3": "#E60000", "gb4": "#E3ABB3", "gold-grad": "linear-gradient(135deg,#F2C9D0 0%,#D57980 45%,#E60000 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
