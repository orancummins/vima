"""Shared command helpers used by every region handler."""
from __future__ import annotations

from typing import Optional

from ..errors import UsageError
from ..output import open_in_browser
from ..sdk.base import Result


def resolve_arg(args, attr: str, ctx, region: str, state_key: str,
                label: Optional[str] = None, required: bool = True) -> Optional[str]:
    """Return an arg value, falling back to saved state for the region.

    Looks first at the parsed CLI value (``getattr(args, attr)``), then at the
    persisted state ``ctx.state.get(region, state_key)``. Raises
    :class:`UsageError` when ``required`` and nothing is found.
    """
    val = getattr(args, attr, None)
    if not val:
        val = ctx.state.get(region, state_key)
    if not val and required:
        nice = label or attr.replace("_", "-")
        raise UsageError(
            f"--{nice} is required (none supplied and no saved value in state). "
            f"Pass it explicitly or run a command that produces it first."
        )
    return val


def emit(res: Result, ctx, region: str, *, open_link: bool = False) -> int:
    """Persist state updates, optionally open a link, render, and return code."""
    if res.state_updates:
        ctx.state.update(region, res.state_updates)
        ctx.state.save()
    if open_link and res.hints.get("open_link"):
        ok = open_in_browser(res.hints["open_link"])
        if not ok:
            ctx.printer.warn("Could not open a browser automatically; copy the URL above.")
    ctx.printer.result(res)
    return 0 if res.ok else 3


def parse_account_ids(value: Optional[str]):
    """Split a comma-separated --account-ids value into a list (or None)."""
    if not value:
        return None
    ids = [p.strip() for p in value.split(",") if p.strip()]
    return ids or None
