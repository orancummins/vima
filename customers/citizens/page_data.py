"""Citizens, as a platform: the data behind ``Citizens_Platform.html``.

``python customers/build_page.py citizens`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Citizens_research_notes.md``.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from citizens_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from citizens_story import LENS, OUTCOMES, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = "Citizens"
PAGE = "Citizens_Platform.html"
AS_OF = "17 October 2026"
TITLE = "Citizens Platform"
KICKER = f"Citizens Financial Group · as at {AS_OF}"
H1 = '<h1>Citizens <span class="os">Platform</span></h1>'
SUB = ("A $234 billion regional bank as five discs that stack into one platform, from the balance sheet and the cloud at "
       "the bottom to the app, about 1,000 branches and the Private Bank's offices at the top. Click the stack to open it. "
       "Choose who you are and what you want to do, and the areas that deliver it light up across the layers, joined in "
       "the order they act. Switch to the Mastercard lens to see how deep Mastercard goes in every area.")

PALETTE_NOTE = ("Palette: Citizens' greens for the bank, from the deep forest foundation to the bright access layer, graphite for the\n"
                "   people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = ("the five slices: foundation (deep forest), rails (Citizens green), services (jade), lines (fresh green), "
               "access (graphite); graphite for the people")
GLOBE_NOTE = "the globe: Citizens' forest, green and mint"

PIN = (41.82, -71.41, "Providence")
PIN_FACING = "New England"

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Open & onboard", "everyday": "Everyday banking", "move": "Pay & move money",
      "borrow": "Borrow & finance", "grow": "Save, invest & grow", "beyond": "Beyond banking"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
# Citizens reports two segments, Consumer Banking and Commercial Banking, plus Other (treasury and the
# run-off book, folded in from 4Q25).
REV = {"con": "Consumer Banking segment", "com": "Commercial Banking segment", "oth": "Other (treasury, run-off)"}
DIV = {"cfg": "Citizens Financial Group", "con": "Consumer Banking", "pay": "Citizens Pay", "pb": "Citizens Private Bank",
       "com": "Commercial Banking", "jmp": "Citizens Capital Markets & Advisory"}
DEFAULT_DIV = "cfg"

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F1F6F3", "panel-2": "#E4EEE8", "ink": "#0A1A13", "ink-2": "#1C2E25",
    "muted": "#46584F", "faint": "#68786F", "line": "#C9D7CF", "line-2": "#ABBDB3",
    "focus": "#00875A", "accent": "#00875A", "link": "#00664A",
    "gold": "#00875A", "gold-deep": "#00573F", "gold-ink": "#00664A",
    "l1": "#003D2C", "l2": "#00573F", "l3": "#0B6E55", "l4": "#2C8A68", "l5": "#1F2937", "lu": "#6B7280",
    "l1f": "#0B5C46", "l2f": "#00875A", "l3f": "#1FA37A", "l4f": "#6CC49E", "l5f": "#374151", "luf": "#9CA3AF",
    "l1t": "#E8FFF5", "l2t": "#FFFFFF", "l3t": "#FFFFFF", "l4t": "#062A1D", "l5t": "#FFFFFF",
    "slot": "#0A1A13", "shadow": "rgba(6,40,26,.22)",
    "wash-a": "rgba(0,135,90,.14)", "wash-b": "rgba(108,196,158,.10)",
    "gb2": "#0B5C46", "gb3": "#00875A", "gb4": "#8FD9B6",
    "brand-grad": "linear-gradient(90deg,#00573F,#00875A 55%,#8FD9B6)",
    "gold-grad": "linear-gradient(135deg,#8FD9B6 0%,#00875A 45%,#00573F 100%)",
    "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00",
    "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#090D0B", "panel": "#111915", "panel-2": "#18231E", "ink": "#F2F7F4", "ink-2": "#D4E0D9",
    "muted": "#A4B4AB", "faint": "#82918A", "line": "#2A3731", "line-2": "#3F4E47",
    "focus": "#5FD3A2", "accent": "#4CC795", "link": "#8FD9B6",
    "gold": "#4CC795", "gold-deep": "#5FD3A2", "gold-ink": "#8FD9B6",
    "l1": "#8FD9B6", "l2": "#6FD0A6", "l3": "#7FDCC0", "l4": "#A9E3C8", "l5": "#D1D5DB", "lu": "#8B93A1",
    "l1f": "#0B5C46", "l2f": "#00875A", "l3f": "#1FA37A", "l4f": "#6CC49E", "l5f": "#6B7280", "luf": "#6B7280",
    "slot": "#050806",
    "wash-a": "rgba(0,135,90,.12)", "wash-b": "rgba(108,196,158,.06)",
    "gb2": "#0B5C46", "gb3": "#00875A", "gb4": "#8FD9B6",
    "gold-grad": "linear-gradient(135deg,#BFF0D8 0%,#4CC795 45%,#00875A 100%)",
    "neo": "#FFB070", "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
