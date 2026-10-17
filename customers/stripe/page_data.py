"""Stripe, as a platform: the data behind ``Stripe_Platform.html``.

``python customers/build_page.py stripe`` turns this into the page. Public
sources, as at the date in ``AS_OF``; every product carries its own sources,
and the research notes behind them are in ``Stripe_research_notes.md``.
Stripe is private, so many figures are its own claims (annual letters,
Sessions) or press estimates; the products say which.

The product format is the template's own (see ``customers/citi/page_data.py``):
id, n, d, short, s, lc, st, ay, o, at, div, rev, neo ([Mastercard depth 0–3 or
None, note] — the lens), mc, rel, src.
"""
# ruff: noqa: E501

from stripe_inventory import LAYERS, PILLARS  # noqa: F401  (the long lists live there)
from stripe_story import LENS, OUTCOMES, SUB, USERS, USERS_DESC, WHO  # noqa: F401

SHORT = "Stripe"
PAGE = "Stripe_Platform.html"
AS_OF = "17 October 2026"
TITLE = "Stripe Platform"
KICKER = f"Stripe · as at {AS_OF}"
H1 = '<h1>Stripe <span class="os">Platform</span></h1>'
SERVES = "who Stripe serves"

PALETTE_NOTE = ("Palette: Stripe's purples for the company, from the deep navy foundation to the bright access layer, graphite for\n"
                "   the people, and Mastercard's colours kept for the lens that reads the stack through Mastercard.")
SLICES_NOTE = ("the five slices: foundation (deep navy), rails (Stripe blurple), services (violet), lines (lavender), "
               "access (graphite); graphite for the people")
GLOBE_NOTE = "the globe: Stripe's navy, blurple and cyan"

PIN = (37.77, -122.42, "San Francisco")
PIN_FACING = "the Americas"

ALLOWED_MENTIONS: tuple[str, ...] = ()

LC = {"open": "Start & onboard", "everyday": "Run the business", "move": "Accept & move money",
      "borrow": "Finance", "grow": "Grow revenue", "beyond": "Beyond payments"}
ST = {"active": "Active", "new": "New in 2025–26", "flux": "In flux", "unconf": "Unconfirmed",
      "retired": "Retired / divested"}
OR = {"B": "Built in-house", "A": "Acquired", "P": "With a partner", "I": "Inherited from a predecessor"}
# Stripe reports no segments; products are grouped by Stripe's own suites.
REV = {"pay": "Payments suite", "rev": "Revenue & finance automation", "plat": "Connect & platforms",
       "money": "Money management", "crypto": "Stablecoins & crypto", "ai": "AI & agentic commerce",
       "grp": "Company-wide"}
DIV = {"stripe": "Stripe", "bridge": "Bridge", "privy": "Privy", "tempo": "Tempo (a separate company)",
       "openrouter": "OpenRouter"}
DEFAULT_DIV = "stripe"

PALETTE_LIGHT = {
    "ground": "#FFFFFF", "panel": "#F6F9FC", "panel-2": "#E9EEF7", "ink": "#0A2540", "ink-2": "#1F3556",
    "muted": "#425466", "faint": "#6B7C93", "line": "#D5DBE5", "line-2": "#B8C2D3",
    "focus": "#635BFF", "accent": "#635BFF", "link": "#4B45C6",
    "gold": "#635BFF", "gold-deep": "#0A2540", "gold-ink": "#4B45C6",
    "l1": "#0A2540", "l2": "#3A33B8", "l3": "#5148D9", "l4": "#7A73FF", "l5": "#1F2937", "lu": "#6B7280",
    "l1f": "#1A3A63", "l2f": "#635BFF", "l3f": "#7A73FF", "l4f": "#A39EFF", "l5f": "#374151", "luf": "#9CA3AF",
    "l1t": "#EEF2FF", "l2t": "#FFFFFF", "l3t": "#FFFFFF", "l4t": "#1B1660", "l5t": "#FFFFFF",
    "slot": "#0A2540", "shadow": "rgba(10,37,64,.22)",
    "wash-a": "rgba(99,91,255,.14)", "wash-b": "rgba(0,212,255,.08)",
    "gb2": "#1A3A63", "gb3": "#635BFF", "gb4": "#80E9FF",
    "brand-grad": "linear-gradient(90deg,#0A2540,#635BFF 55%,#80E9FF)",
    "gold-grad": "linear-gradient(135deg,#80E9FF 0%,#635BFF 45%,#0A2540 100%)",
    "neo": "#B23A00", "neof": "#FF5F00", "neo-on": "#1F0A00",
    "neo-grad": "linear-gradient(135deg,#F79E1B,#FF5F00 50%,#EB001B)",
}
PALETTE_DARK = {
    "ground": "#0A0E1A", "panel": "#121729", "panel-2": "#1A2035", "ink": "#F4F5FB", "ink-2": "#D9DCEB",
    "muted": "#A9AFC6", "faint": "#878DA6", "line": "#2B3149", "line-2": "#40476A",
    "focus": "#9D97FF", "accent": "#8F89FF", "link": "#B5B1FF",
    "gold": "#8F89FF", "gold-deep": "#9D97FF", "gold-ink": "#B5B1FF",
    "l1": "#B5B1FF", "l2": "#9D97FF", "l3": "#B0ABFF", "l4": "#C9C6FF", "l5": "#D1D5DB", "lu": "#8B93A1",
    "l1f": "#1A3A63", "l2f": "#635BFF", "l3f": "#7A73FF", "l4f": "#A39EFF", "l5f": "#6B7280", "luf": "#6B7280",
    "slot": "#05070D",
    "wash-a": "rgba(99,91,255,.12)", "wash-b": "rgba(0,212,255,.06)",
    "gb2": "#1A3A63", "gb3": "#635BFF", "gb4": "#80E9FF",
    "gold-grad": "linear-gradient(135deg,#D6D3FF 0%,#8F89FF 45%,#635BFF 100%)",
    "neo": "#FFB070", "neof": "#FF7A2E", "neo-on": "#1F0A00",
}
