"""ofin command-line entry point (stdlib ``argparse``)."""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from typing import Optional

from . import __version__
from .config import Config, config_sources
from .errors import ConfigError, OfinError
from .output import Printer
from .sdk import OfinClient
from .state import State
from .commands import au_cmd, common_cmd, eu_cmd, us_cmd


@dataclass
class Context:
    """Shared services handed to every command handler."""

    config: Config
    state: State
    printer: Printer
    verbose: bool
    timeout: Optional[int]
    _client: Optional[OfinClient] = None

    @property
    def client(self) -> OfinClient:
        if self._client is None:
            self._client = OfinClient(self.config, timeout=self.timeout)
        return self._client


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ofin",
        description="Standalone CLI for Mastercard Open Finance (US, AU, EU).",
        epilog="Run 'ofin ops' to list available commands per region.",
    )
    parser.add_argument("--version", action="version", version=f"ofin {__version__}")
    parser.add_argument("--json", action="store_true", help="Emit full JSON envelopes.")
    parser.add_argument("--raw", action="store_true", help="Print only the response body.")
    parser.add_argument("--no-color", action="store_true", help="Disable ANSI colors.")
    parser.add_argument("--env-file", help="Path to a .env file with credentials.")
    parser.add_argument("--state-file", help="Path to the CLI state JSON file.")
    parser.add_argument("--timeout", type=int, help="Per-request timeout in seconds.")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Show tracebacks on unexpected errors.")

    subparsers = parser.add_subparsers(dest="command", required=False, metavar="<command>")
    common_cmd.add_parser(subparsers)
    us_cmd.add_parser(subparsers)
    au_cmd.add_parser(subparsers)
    eu_cmd.add_parser(subparsers)
    return parser


def _welcome(ctx: "Context", env_file: Optional[str]) -> None:
    """Print a friendly getting-started screen when no command is given."""
    p = ctx.printer
    b = p.bold
    p.info(b(f"ofin {__version__}") + " — Mastercard Open Finance CLI (US, AU, EU)")
    p.info("")

    # Where credentials are coming from.
    sources = config_sources(env_file)
    p.info(b("Configuration"))
    if sources:
        for src in sources:
            p.info(f"  • {src}")
    else:
        p.info("  • " + p.yellow("no credentials found"))
        p.info("    set env vars, pass --env-file PATH, or add config/.env")

    # Which regions are wired up.
    def _mark(ok: bool) -> str:
        return p.green("configured") if ok else p.yellow("not configured")

    p.info("  Regions: "
           f"US {_mark(ctx.config.us.configured)}, "
           f"AU {_mark(ctx.config.au.configured)}, "
           f"EU {_mark(ctx.config.eu.configured)}")
    p.info(f"  State file: {ctx.state.path}")
    p.info("")

    # Quickstart.
    p.info(b("Quickstart"))
    p.info("  ofin config show                 inspect resolved credentials")
    p.info("  ofin ops                         list every command per region")
    p.info("  ofin us auth token               verify US connectivity")
    p.info("  ofin eu providers list --country DK")
    p.info("  ofin <region> <group> --help     detailed help for any command")
    p.info("")
    p.info("Global flags: --json  --raw  --no-color  --env-file PATH  "
           "--state-file PATH  --timeout N  -v")


def main(argv: Optional[list] = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    parser = build_parser()
    args = parser.parse_args(argv)

    printer = Printer(as_json=args.json, raw=args.raw, no_color=args.no_color)

    # Resolve config + state. Config resolution can fail on a bad --env-file.
    try:
        config = Config.resolve(env_file=args.env_file)
    except FileNotFoundError as exc:
        printer.error(str(exc))
        return 2
    state = State(path=args.state_file)

    ctx = Context(config=config, state=state, printer=printer,
                  verbose=args.verbose, timeout=args.timeout)

    func = getattr(args, "func", None)
    if func is None:
        _welcome(ctx, args.env_file)
        return 0

    try:
        rc = func(args, ctx)
        return int(rc) if rc is not None else 0
    except ConfigError as exc:
        printer.error(str(exc))
        return exc.exit_code
    except OfinError as exc:
        printer.error(str(exc))
        return exc.exit_code
    except KeyboardInterrupt:  # pragma: no cover
        printer.error("interrupted")
        return 130
    except Exception as exc:  # noqa: BLE001
        if args.verbose:
            raise
        printer.error(f"{type(exc).__name__}: {exc}")
        return 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
