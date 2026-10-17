"""The Mastercard lens for each area, read straight from a customer's inventory.

Each product in ``<id>_inventory.py`` carries ``neo = [depth, note]`` (3 Mastercard-run, 2 on
Mastercard, 1 partly, 0 not, None nothing public). The lens's per-area entries (``LENS["t"]``)
say the same thing area by area, so rather than write them twice a story can build them here::

    from customers.lens_tiles import area_lens
    LENS = {..., "t": area_lens(LAYERS)}

An area takes the deepest depth among its products (an area with Mastercard in one product and
not in another is still "partly"), or None when no product says anything; its list shows every
product with its note and whether Mastercard is in it.
"""
from __future__ import annotations


def _depth(products: list[dict]) -> int | None:
    known = [p["neo"][0] for p in products if p.get("neo") and p["neo"][0] is not None]
    if not known:
        return None
    best = max(known)
    # Mastercard in some products but not others reads as "partly", not as the best product's depth.
    return 1 if best >= 2 and min(known) == 0 else best


def area_lens(layers: list[dict], overrides: dict | None = None) -> dict:
    """``LENS["t"]`` for every area in ``layers``; ``overrides`` replaces entries by area id."""
    out = {}
    for layer in layers:
        for t in layer["tiles"]:
            rows, notes = [], []
            for p in t["products"]:
                d, note = (p.get("neo") or [None, ""])[:2]
                status = "u" if d is None else ("0" if d == 0 else "")
                rows.append([p.get("short", p["n"]), note or ("No Mastercard role." if d == 0 else "Not public."), status, ""])
                if note and note not in notes and d:
                    notes.append(note)
            d = _depth(t["products"])
            if d is None:
                why = "Nothing public says which network, if any, runs it."
            elif d == 0:
                why = "No Mastercard role in public sources."
            else:
                why = " ".join(notes) or "Mastercard is part of it."
            out[t["id"]] = {"d": d, "why": why, "v": rows}
    out.update(overrides or {})
    return out
