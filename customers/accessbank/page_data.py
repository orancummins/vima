"""Access Bank, as a platform: the data behind ``Access_Bank_Platform.html``.

``python customers/build_page.py accessbank`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Access_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from accessbank_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from accessbank_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'Access Bank'
PAGE = 'Access_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "Access Bank Platform"
KICKER = f"Access Bank Plc · as at {AS_OF}"
H1 = '<h1>Access Bank <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: Access Bank's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in Access Bank's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in Access Bank's colours"

PIN = (6.43, 3.42, 'Lagos')
PIN_FACING = 'Africa and Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'cib': 'Corporate & Investment Banking', 'commercial': 'Commercial Banking', 'retail': 'Retail Banking', 'africa': 'Rest of Africa', 'intl': 'International'}
DIV = {'abg': 'Access Bank Group', 'access': 'Access Bank Nigeria', 'more': 'AccessMore', 'closa': 'Access Closa', 'private': 'Access Private Bank', 'subs': 'African subsidiaries', 'uk': 'The Access Bank UK', 'holdings': 'Access Holdings & Hydrogen'}
DEFAULT_DIV = 'abg'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F3F2", "panel-2": "#F0E9E7", "ink": "#20140C", "ink-2": "#423229",
    "muted": "#8E8171", "faint": "#9F9890", "line": "#DFDAD4", "line-2": "#CFC9C2", "focus": "#DF7601",
    "accent": "#DF7601", "link": "#9A5B01", "gold": "#DF7601", "gold-deep": "#844E01", "gold-ink": "#9A5B01",
    "l1": "#533100", "l2": "#844E01", "l3": "#BE7B14", "l4": "#C5884C", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#955F12", "l2f": "#EE7E01", "l3f": "#DA9540", "l4f": "#D4B095",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#20140C", "shadow": "rgba(51,27,8,.22)", "wash-a": "rgba(238,126,1,.14)",
    "wash-b": "rgba(212,176,149,.10)", "gb2": "#955F12", "gb3": "#EE7E01", "gb4": "#E3C3AE", "brand-grad": "linear-gradient(90deg,#844E01,#EE7E01 55%,#E3C3AE)",
    "gold-grad": "linear-gradient(135deg,#E3C3AE 0%,#EE7E01 45%,#844E01 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0F0C0A", "panel": "#1F1915", "panel-2": "#2F2721", "ink": "#F7F4F3", "ink-2": "#E5DEDB",
    "muted": "#C9C3BD", "faint": "#AFAAA5", "line": "#574D43", "line-2": "#877A6D", "focus": "#EE7E01",
    "accent": "#EE7E01", "link": "#E3C3AE", "gold": "#EE7E01", "gold-deep": "#DFB08C", "gold-ink": "#E3C3AE",
    "l1": "#E3C3AE", "l2": "#DDB597", "l3": "#E5C8A3", "l4": "#EAD0BF", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#955F12", "l2f": "#EE7E01", "l3f": "#DA9540", "l4f": "#D4B095",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#090605", "wash-a": "rgba(238,126,1,.12)", "wash-b": "rgba(212,176,149,.06)",
    "gb2": "#955F12", "gb3": "#EE7E01", "gb4": "#E3C3AE", "gold-grad": "linear-gradient(135deg,#F2D9CA 0%,#D6A67E 45%,#EE7E01 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
