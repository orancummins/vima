#!/usr/bin/env python3
"""Recolour a customer's page and Studio theme from its primary brand colour.

Citizens' palette is the hand-tuned base: deep foundation to bright access,
graphite for the people, Mastercard's colours for the lens. Its primary,
Citizens green ``#00875A``, is the anchor. Every colour in the base is moved
so the anchor lands exactly on the customer's ``CUSTOMER["accent"]``: the
hue turns by the same angle, saturation scales by the same ratio, and
lightness is stretched so the anchor's lightness becomes the primary's, less
and less towards black and white, so grounds and panels keep their depth. Greys and Mastercard's lens colours
are left alone, and so are the graphite greys of the people and the access
layer.

A light primary (Barclays blue, Synchrony gold) would leave pale text on
white, so text colours are then darkened (light theme) or lightened (dark
theme) until they read at 4.5:1, and the label on each slice turns white or
ink, whichever reads better on it.

Writes the ``PALETTE_LIGHT`` / ``PALETTE_DARK`` blocks at the end of
``customers/<id>/page_data.py`` and the whole ``studio-theme.css``; then
rebuild the page with ``customers/build_page.py``::

    python customers/brand_colours.py natwest && python customers/build_page.py natwest

Citizens (the base) and SNB (whose page is the template, built in the snb
project) are not recoloured here.
"""
from __future__ import annotations

import colorsys
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "citizens"
ANCHOR = "#00875A"
LENS = {"neo", "neof", "neo-on", "neo-grad"}        # Mastercard's colours, never moved
GRAPHITE = {"l5", "lu", "l5f", "luf", "l5t"}         # the people and the access layer stay graphite
SLATE = {"#1f2937", "#374151", "#6b7280", "#8b93a1", "#9ca3af", "#d1d5db"}   # the base's graphite greys
KEEP = {"#ffb070", "#b84a00"} | SLATE                # and Studio's orange, in the theme
INK_LIGHT, INK_DARK = "#FFFFFF", "#0B0F14"


# ---------------------------------------------------------------------------
# colour arithmetic
# ---------------------------------------------------------------------------

def rgb(h: str) -> tuple[float, float, float]:
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def hexc(r: float, g: float, b: float) -> str:
    return "#" + "".join(f"{round(max(0, min(1, v)) * 255):02X}" for v in (r, g, b))


def luminance(h: str) -> float:
    def lin(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a: str, b: str) -> float:
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


class Shift:
    """Moves colours so that ANCHOR lands on the customer's primary."""

    def __init__(self, primary: str):
        self.h0, self.l0, self.s0 = colorsys.rgb_to_hls(*rgb(ANCHOR))
        self.h1, self.l1, self.s1 = colorsys.rgb_to_hls(*rgb(primary))

    def __call__(self, h: str) -> str:
        hh, ll, ss = colorsys.rgb_to_hls(*rgb(h))
        if ss < 0.03:                                   # a true grey stays a grey
            return h.upper() if h.startswith("#") else h
        # A faintly tinted grey takes the brand's hue; a colour keeps its offset from the anchor's.
        hh = self.h1 if ss < 0.15 else (hh + self.h1 - self.h0) % 1
        ss = min(1.0, ss * self.s1 / self.s0)
        to = ll * self.l1 / self.l0 if ll <= self.l0 else 1 - (1 - ll) * (1 - self.l1) / (1 - self.l0)
        w = min(1.0, ll / 0.25, (1 - ll) / 0.25)        # near-black grounds and near-white panels keep their lightness
        ll = ll + (to - ll) * w
        return hexc(*colorsys.hls_to_rgb(hh, ll, ss))


def toward(h: str, against: str, target: float, darker: bool) -> str:
    """Darken (or lighten) ``h`` until it reads at ``target``:1 on ``against``."""
    hh, ll, ss = colorsys.rgb_to_hls(*rgb(h))
    out = h
    while contrast(out, against) < target and 0 < ll < 1:
        ll = max(0.0, ll - 0.01) if darker else min(1.0, ll + 0.01)
        out = hexc(*colorsys.hls_to_rgb(hh, ll, ss))
    return out


def label_on(fill: str) -> str:
    return INK_LIGHT if contrast(INK_LIGHT, fill) >= contrast(INK_DARK, fill) else INK_DARK


def shift_text(text: str, shift: Shift, keep=frozenset()) -> str:
    """Shift every #rrggbb and rgb()/rgba() in ``text``."""
    def hx(m):                                          # keeps the source's letter case
        v = m.group(0)
        if v.lower() in keep:
            return v
        out = shift(v)
        return out.lower() if any(c.islower() for c in v[1:]) else out

    def rgba(m):
        fn, r, g, b, rest = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)), m.group(5) or ""
        out = rgb(shift(f"#{r:02X}{g:02X}{b:02X}"))
        sep = ", " if ", " in m.group(0) else ","
        return f"{fn}({sep.join(str(round(c * 255)) for c in out)}{rest})"

    text = re.sub(r"#[0-9A-Fa-f]{6}\b", hx, text)
    return re.sub(r"(rgba?)\((\d+),\s*(\d+),\s*(\d+)(,\s*[\d.]+)?\)", rgba, text)


# ---------------------------------------------------------------------------
# page palette (page_data.py)
# ---------------------------------------------------------------------------

def base_palettes() -> tuple[dict, dict]:
    src = open(os.path.join(HERE, BASE, "page_data.py"), encoding="utf-8").read()
    i = src.index("PALETTE_LIGHT = ")
    ns: dict = {}
    exec(src[i:], ns)                                   # two dict literals, our own file
    return ns["PALETTE_LIGHT"], ns["PALETTE_DARK"]


def page_palettes(primary: str) -> tuple[dict, dict]:
    shift = Shift(primary)
    light, dark = base_palettes()
    L = {k: v if k in LENS | GRAPHITE else shift_text(v, shift, keep=SLATE) for k, v in light.items()}
    D = {k: v if k in LENS | GRAPHITE else shift_text(v, shift, keep=SLATE) for k, v in dark.items()}
    # Body text keeps its contrast however light or dark the brand is (a pale pink must not wash out the greys).
    for k, target in (("ink", 7.0), ("ink-2", 7.0), ("muted", 4.5), ("faint", 3.0)):
        L[k] = toward(L[k], L["panel-2"], target, darker=True)
        D[k] = toward(D[k], D["panel-2"], target, darker=False)
    for k, target in (("line", 1.25), ("line-2", 1.6)):  # hairlines and borders stay visible
        L[k] = toward(L[k], L["ground"], target, darker=True)
        D[k] = toward(D[k], D["ground"], target, darker=False)
    for k in ("link", "gold-ink"):                      # text on white and on the panels
        L[k] = toward(L[k], L["panel-2"], 4.5, darker=True)
        D[k] = toward(D[k], D["panel-2"], 4.5, darker=False)
    for k in ("focus", "accent", "gold"):               # rings, strokes, badges: the brand colour itself where it reads
        L[k] = toward(L[k], L["ground"], 3.0, darker=True)
        D[k] = primary.upper() if contrast(primary, D["ground"]) >= 4.5 else toward(D[k], D["ground"], 4.5, darker=False)
    D["gold-deep"] = toward(D["gold-deep"], D["ground"], 4.5, darker=False)
    for n in "1234":                                    # dark theme: slice names are text on the ground
        D[f"l{n}"] = toward(D[f"l{n}"], D["ground"], 4.5, darker=False)
    for n in "12345":                                   # light theme: labels on the slices
        L[f"l{n}t"] = label_on(L[f"l{n}"])
    return L, D


def palette_block(name: str, d: dict) -> str:
    items = list(d.items())
    out = [f"{name} = {{"]
    for i in range(0, len(items), 5):
        out.append("    " + " ".join(f'"{k}": "{v}",' for k, v in items[i:i + 5]))
    return "\n".join(out + ["}"])


def write_page_data(cid: str, primary: str) -> None:
    path = os.path.join(HERE, cid, "page_data.py")
    src = open(path, encoding="utf-8").read()
    L, D = page_palettes(primary)
    i = src.index("PALETTE_LIGHT = ")
    src = src[:i] + palette_block("PALETTE_LIGHT", L) + "\n" + palette_block("PALETTE_DARK", D) + "\n"
    open(path, "w", encoding="utf-8").write(src)


# ---------------------------------------------------------------------------
# Studio theme (studio-theme.css)
# ---------------------------------------------------------------------------

def set_css(block: str, var: str, value: str) -> str:
    return re.sub(rf"(--{re.escape(var)}:\s*)#[0-9a-fA-F]{{6}}", lambda m: m.group(1) + value.lower(), block, count=1)


def get_css(block: str, var: str) -> str | None:
    m = re.search(rf"--{re.escape(var)}:\s*(#[0-9a-fA-F]{{6}})", block)
    return m.group(1) if m else None


def studio_theme(cid: str, name: str, primary: str) -> str:
    css = open(os.path.join(HERE, BASE, "studio-theme.css"), encoding="utf-8").read()
    css = shift_text(css, Shift(primary), keep=KEEP)
    css = css.replace("/* Citizens inside Solution Studio.", f"/* {name} inside Solution Studio.")
    css = css.replace("Citizens' greens back", f"{name}'s colours back")
    css = css.replace("/* The Citizens / Mastercard lens switch", f"/* The {name} / Mastercard lens switch")
    dark_at = css.index('html:root:not([data-theme="light"])')
    light_at = css.index('html:root[data-theme="light"]')
    end = css.index("/* ---------- page ---------- */")
    dark, light = css[dark_at:light_at], css[light_at:end]
    ground_d = get_css(dark, "ground") or "#0d0b0f"
    panel_l = get_css(light, "panel-2") or "#e8e4ee"
    for v in ("link", "gold-ink", "gold-deep", "l1t", "l2t", "l3t", "l4t"):
        c = get_css(dark, v)
        if c:
            dark = set_css(dark, v, toward(c, ground_d, 4.5, darker=False))
    for v in ("focus", "accent", "gold"):
        c = get_css(dark, v)
        if c:
            dark = set_css(dark, v, primary if contrast(primary, ground_d) >= 4.5 else toward(c, ground_d, 4.5, darker=False))
    for v in ("link", "gold-ink"):
        c = get_css(light, v)
        if c:
            light = set_css(light, v, toward(c, panel_l, 4.5, darker=True))
    for v in ("focus", "accent", "gold"):
        c = get_css(light, v)
        if c:
            light = set_css(light, v, toward(c, "#ffffff", 3.0, darker=True))
    for v in ("l1t", "l2t", "l3t", "l4t"):              # light: slice text on white-ish discs reads as ink
        c = get_css(light, v)
        if c:
            light = set_css(light, v, toward(c, "#ffffff", 4.5, darker=True))
    return css[:dark_at] + dark + light + css[end:]


def customer(cid: str) -> dict:
    spec = importlib.util.spec_from_file_location(f"_c_{cid}", os.path.join(HERE, cid, "__init__.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CUSTOMER


def main(cid: str) -> None:
    if cid in (BASE, "snb"):
        raise SystemExit(f"{cid} is not recoloured here (see the module docstring)")
    c = customer(cid)
    primary = c.get("accent")
    if not primary:
        raise SystemExit(f"customers/{cid}/__init__.py has no CUSTOMER['accent']")
    write_page_data(cid, primary)
    with open(os.path.join(HERE, cid, "studio-theme.css"), "w", encoding="utf-8") as f:
        f.write(studio_theme(cid, c.get("short") or c["name"], primary))
    print(f"✓ {cid}: palette and Studio theme from {primary}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python customers/brand_colours.py <customer id>")
    main(sys.argv[1])
