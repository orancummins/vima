"""Typer CLI entrypoint."""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

import typer
from loguru import logger

from app import orchestrator

app = typer.Typer(add_completion=False, help="Mastercard Developers key automation.")


def _configure_logging(verbose: bool) -> None:
    logger.remove()
    level = "DEBUG" if verbose else "INFO"
    logger.add(sys.stderr, level=level)
    log_dir = Path(__file__).parent.parent / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    logger.add(log_dir / "execution.log", level="DEBUG", rotation="10 MB")


@app.command()
def run(
    config: Path = typer.Option(..., "--config", "-c", exists=True, help="Path to YAML config."),
    dry_run: bool = typer.Option(False, "--dry-run", help="Stop after login; do not provision."),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Run the end-to-end automation."""
    _configure_logging(verbose)
    bundle = asyncio.run(orchestrator.run(config, dry_run=dry_run))
    if bundle:
        typer.echo(f"Bundle: {bundle}")
    else:
        typer.echo("No bundle produced.")


@app.command()
def login(
    config: Path = typer.Option(..., "--config", "-c", exists=True, help="Path to YAML config."),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Launch the browser and stop after authentication (handy for DOM discovery)."""
    _configure_logging(verbose)
    asyncio.run(orchestrator.run(config, dry_run=True))


if __name__ == "__main__":
    app()
