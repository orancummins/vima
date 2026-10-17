"""Commercial Bank of Ceylon, as a platform: the data behind ``Commercial_Bank_of_Ceylon_Platform.html``.

``python customers/build_page.py combank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Commercial_Bank_of_Ceylon_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from combank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from combank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'ComBank'
PAGE = 'Commercial_Bank_of_Ceylon_Platform.html'
AS_OF = "17 October 2026"
TITLE = "ComBank Platform"
KICKER = f"Commercial Bank of Ceylon · as at {AS_OF}"
H1 = '<h1>ComBank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: ComBank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in ComBank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in ComBank's colours"

PIN = (6.93, 79.85, 'Colombo')
PIN_FACING = 'Sri Lanka and South Asia'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'personal': 'Personal Banking', 'corporate': 'Corporate Banking', 'intl': 'International Operations', 'treasury': 'Dealing/Treasury', 'nbfi': 'NBFI, real estate & services'}
DIV = {'group': 'ComBank Group', 'bank': 'Commercial Bank of Ceylon', 'cards': 'Card Centre', 'bd': 'CBC Bangladesh', 'cbm': 'Commercial Bank of Maldives', 'cbcf': 'CBC Finance', 'orysys': 'Orysys', 'myanmar': 'CBC Myanmar Microfinance'}
DEFAULT_DIV = 'group'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F6", "panel-2": "#E5EDEF", "ink": "#0B171D", "ink-2": "#223338",
    "muted": "#5B6973", "faint": "#7B858C", "line": "#CED6DB", "line-2": "#B6C0C6", "focus": "#006FBA",
    "accent": "#006FBA", "link": "#004785", "gold": "#006FBA", "gold-deep": "#003B6D", "gold-ink": "#004785",
    "l1": "#002748", "l2": "#003B6D", "l3": "#0F5495", "l4": "#3780AC", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#0E4778", "l2f": "#006FBA", "l3f": "#2682C7", "l4f": "#80B5CC",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#FFFFFF",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#0B171D", "shadow": "rgba(7,33,45,.22)", "wash-a": "rgba(0,111,186,.14)",
    "wash-b": "rgba(128,181,204,.10)", "gb2": "#0E4778", "gb3": "#006FBA", "gb4": "#9ECDDE", "brand-grad": "linear-gradient(90deg,#003B6D,#006FBA 55%,#9ECDDE)",
    "gold-grad": "linear-gradient(135deg,#9ECDDE 0%,#006FBA 45%,#003B6D 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0D0E", "panel": "#131A1C", "panel-2": "#1C2529", "ink": "#F2F7F7", "ink-2": "#D7E1E2",
    "muted": "#B0B9BE", "faint": "#939BA0", "line": "#364047", "line-2": "#55626A", "focus": "#75B9D9",
    "accent": "#64ACCF", "link": "#9ECDDE", "gold": "#64ACCF", "gold-deep": "#75B9D9", "gold-ink": "#9ECDDE",
    "l1": "#9ECDDE", "l2": "#83BDD6", "l3": "#90BEE1", "l4": "#B3D9E6", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#0E4778", "l2f": "#006FBA", "l3f": "#2682C7", "l4f": "#80B5CC",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#050808", "wash-a": "rgba(0,111,186,.12)", "wash-b": "rgba(128,181,204,.06)",
    "gb2": "#0E4778", "gb3": "#006FBA", "gb4": "#9ECDDE", "gold-grad": "linear-gradient(135deg,#C4E6F1 0%,#64ACCF 45%,#006FBA 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
