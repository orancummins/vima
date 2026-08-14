"""Meta commands: ``config``, ``state``, ``ops``, ``version``."""
from __future__ import annotations

from .. import __version__


def _mask(value: str) -> str:
    if not value:
        return ""
    if len(value) <= 8:
        return "•" * len(value)
    return value[:4] + "…" + value[-4:]


# ---------------------------------------------------------------------------
# config show
# ---------------------------------------------------------------------------
def _config_show(args, ctx) -> int:
    cfg = ctx.config
    payload = {
        "us": {
            "configured": cfg.us.configured,
            "partner_id": _mask(cfg.us.partner_id),
            "app_key": _mask(cfg.us.app_key),
            "base_url": cfg.us.base_url,
        },
        "au": {
            "configured": cfg.au.configured,
            "partner_id": _mask(cfg.au.partner_id),
            "app_key": _mask(cfg.au.app_key),
            "base_url": cfg.au.base_url,
        },
        "eu": {
            "configured": cfg.eu.configured,
            "client_id": _mask(cfg.eu.client_id),
            "private_key_path": cfg.eu.private_key_path,
            "public_cert_path": cfg.eu.public_cert_path,
            "application_id": _mask(cfg.eu.application_id),
            "auth_base_url": cfg.eu.auth_base_url or "(default)",
            "api_base_url": cfg.eu.api_base_url or "(default)",
        },
    }
    if ctx.printer.as_json:
        ctx.printer.data(payload)
        return 0
    p = ctx.printer
    for region in ("us", "au", "eu"):
        block = payload[region]
        ok = block["configured"]
        head = p.green("configured") if ok else p.red("not configured")
        p.info(p.bold(region.upper()) + "  " + head)
        for k, v in block.items():
            if k == "configured":
                continue
            p.info(f"  {k}: {v}")
    return 0


# ---------------------------------------------------------------------------
# state show / clear
# ---------------------------------------------------------------------------
def _state_show(args, ctx) -> int:
    data = ctx.state.as_dict()
    if ctx.printer.as_json:
        ctx.printer.data({"path": ctx.state.path, "state": data})
        return 0
    ctx.printer.info(ctx.printer.dim(f"state file: {ctx.state.path}"))
    if not data:
        ctx.printer.info("(empty)")
        return 0
    for region, vals in data.items():
        ctx.printer.info(ctx.printer.bold(region.upper()))
        for k, v in vals.items():
            ctx.printer.info(f"  {k}: {v}")
    return 0


def _state_clear(args, ctx) -> int:
    region = getattr(args, "region", None)
    ctx.state.clear(region)
    ctx.state.save()
    ctx.printer.info(f"cleared state for {region or 'all regions'}.")
    return 0


# ---------------------------------------------------------------------------
# ops — list curated commands per region
# ---------------------------------------------------------------------------
_OPS = {
    "us": [
        "auth token", "customers add-testing", "customers list", "customers get",
        "customers use", "connect generate", "accounts list", "accounts refresh",
        "balance", "transactions list", "reports voa", "reports voi",
    ],
    "au": [
        "auth token", "customers add-testing", "customers list", "institutions list",
        "connect generate", "consents list", "accounts list",
    ],
    "eu": [
        "auth token", "providers list", "consent create", "consent get",
        "consent revoke", "flow create", "accounts list", "account get",
        "transactions list", "balance", "verify-ownership",
    ],
}


def _ops(args, ctx) -> int:
    region = getattr(args, "region", None)
    regions = [region] if region else ["us", "au", "eu"]
    if ctx.printer.as_json:
        ctx.printer.data({r: _OPS[r] for r in regions})
        return 0
    for r in regions:
        ctx.printer.info(ctx.printer.bold(r.upper()))
        for op in _OPS[r]:
            ctx.printer.info(f"  ofin {r} {op}")
    return 0


def _version(args, ctx) -> int:
    if ctx.printer.as_json:
        ctx.printer.data({"version": __version__})
    else:
        ctx.printer.info(f"ofin {__version__}")
    return 0


# ---------------------------------------------------------------------------
# parser registration
# ---------------------------------------------------------------------------
def add_parser(subparsers) -> None:
    # config
    cfg = subparsers.add_parser("config", help="Show resolved credentials (masked).")
    cfg_sub = cfg.add_subparsers(dest="config_cmd", required=True)
    cfg_show = cfg_sub.add_parser("show", help="Show which regions are configured.")
    cfg_show.set_defaults(func=_config_show)

    # state
    st = subparsers.add_parser("state", help="Inspect or clear saved flow state.")
    st_sub = st.add_subparsers(dest="state_cmd", required=True)
    st_show = st_sub.add_parser("show", help="Show saved active ids.")
    st_show.set_defaults(func=_state_show)
    st_clear = st_sub.add_parser("clear", help="Clear saved state.")
    st_clear.add_argument("region", nargs="?", choices=["us", "au", "eu"],
                          help="Region to clear (default: all).")
    st_clear.set_defaults(func=_state_clear)

    # ops
    ops = subparsers.add_parser("ops", help="List available commands per region.")
    ops.add_argument("region", nargs="?", choices=["us", "au", "eu"])
    ops.set_defaults(func=_ops)

    # version
    ver = subparsers.add_parser("version", help="Print the ofin version.")
    ver.set_defaults(func=_version)
