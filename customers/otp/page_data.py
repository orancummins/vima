"""OTP Bank, as a platform: the data behind ``OTP_Bank_Platform.html``.

``python customers/build_page.py otp`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``OTP_Bank_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from otp_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from otp_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = 'OTP'
PAGE = 'OTP_Bank_Platform.html'
AS_OF = "17 October 2026"
TITLE = "OTP Platform"
KICKER = f"OTP Bank · OTP Group · as at {AS_OF}"
H1 = '<h1>OTP <span class="os">Platform</span></h1>'

PALETTE_NOTE = ("Palette: OTP's colours for the company, from the deep foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = "the five slices in OTP's colours, deep to bright, with graphite for access and the people"
GLOBE_NOTE = "the globe in OTP's colours"

PIN = (47.5, 19.05, 'Budapest')
PIN_FACING = 'Central and Eastern Europe'

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
REV = {'core': 'OTP Core (Hungary)', 'husubs': 'Other Hungarian subsidiaries', 'foreign': 'Foreign subsidiaries', 'group': 'Group'}
DIV = {'otpg': 'OTP Group', 'otp': 'OTP Bank (Hungary)', 'mobil': 'OTP Mobil (Simple, SimplePay)', 'dsk': 'DSK Bank (Bulgaria)', 'otpbanka': 'OTP banka (Slovenia)', 'ipoteka': 'Ipoteka Bank (Uzbekistan)', 'merkantil': 'Merkantil & OTP Fund Management', 'luminor': 'Luminor (pending)'}
DEFAULT_DIV = 'otpg'

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F4F5F3", "panel-2": "#EBEDE8", "ink": "#141B10", "ink-2": "#323A2C",
    "muted": "#636D5F", "faint": "#828A80", "line": "#D7DBD5", "line-2": "#C4C9C1", "focus": "#4EA62E",
    "accent": "#4EA62E", "link": "#347921", "gold": "#4EA62E", "gold-deep": "#2A621B", "gold-ink": "#347921",
    "l1": "#1B3F11", "l2": "#2A621B", "l3": "#458F34", "l4": "#72A65C", "l5": "#1F2937",
    "lu": "#6B7280", "l1f": "#3A712B", "l2f": "#52AE30", "l3f": "#6EB557", "l4f": "#ABC39D",
    "l5f": "#374151", "luf": "#9CA3AF", "l1t": "#FFFFFF", "l2t": "#FFFFFF", "l3t": "#0B0F14",
    "l4t": "#0B0F14", "l5t": "#FFFFFF", "slot": "#141B10", "shadow": "rgba(25,40,16,.22)", "wash-a": "rgba(82,174,48,.14)",
    "wash-b": "rgba(171,195,157,.10)", "gb2": "#3A712B", "gb3": "#52AE30", "gb4": "#C2D6B5", "brand-grad": "linear-gradient(90deg,#2A621B,#52AE30 55%,#C2D6B5)",
    "gold-grad": "linear-gradient(135deg,#C2D6B5 0%,#52AE30 45%,#2A621B 100%)", "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00", "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0C0D0B", "panel": "#191C17", "panel-2": "#252A22", "ink": "#F5F6F4", "ink-2": "#DFE2DC",
    "muted": "#BEC3BC", "faint": "#A3A8A1", "line": "#464E43", "line-2": "#6E786A", "focus": "#52AE30",
    "accent": "#52AE30", "link": "#C2D6B5", "gold": "#52AE30", "gold-deep": "#AACA97", "gold-ink": "#C2D6B5",
    "l1": "#C2D6B5", "l2": "#B0CBA1", "l3": "#B6D5AC", "l4": "#CFDFC5", "l5": "#D1D5DB",
    "lu": "#8B93A1", "l1f": "#3A712B", "l2f": "#52AE30", "l3f": "#6EB557", "l4f": "#ABC39D",
    "l5f": "#6B7280", "luf": "#6B7280", "slot": "#070806", "wash-a": "rgba(82,174,48,.12)", "wash-b": "rgba(171,195,157,.06)",
    "gb2": "#3A712B", "gb3": "#52AE30", "gb4": "#C2D6B5", "gold-grad": "linear-gradient(135deg,#DBE9D1 0%,#9CC08A 45%,#52AE30 100%)", "neo": "#FFB070",
    "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
