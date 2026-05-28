"""Typer CLI entrypoint."""
from __future__ import annotations

import asyncio
import json
import os
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlparse

import typer
import yaml
from loguru import logger

from app import orchestrator
from app._vima_catalog import encryption_env_var, env_prefix_for
from app.config_loader import load_config
from app.models import AppConfig, ProjectSpec

app = typer.Typer(add_completion=False, help="Mastercard Developers key automation.")

HERE = Path(__file__).parent.parent
WORKSPACE = HERE / "temp"
VIMA_ROOT = HERE.parent.parent  # /Users/.../vima
VIMA_CONFIG = VIMA_ROOT / "config"
VIMA_KEYS = VIMA_CONFIG / "keys"
SESSION_FILE = HERE / "session_state.json"
SESSION_MAX_AGE_HOURS = 8.0


def _session_is_fresh(max_age_hours: float = SESSION_MAX_AGE_HOURS) -> bool:
    """True if session_state.json exists and was written within max_age_hours."""
    if not SESSION_FILE.exists():
        return False
    import time
    return (time.time() - SESSION_FILE.stat().st_mtime) / 3600 < max_age_hours


def _session_age_str() -> str:
    if not SESSION_FILE.exists():
        return "no session"
    import time
    age_m = int((time.time() - SESSION_FILE.stat().st_mtime) / 60)
    return f"{age_m}m old"


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
    headless: bool = typer.Option(False, "--headless/--no-headless", help="Run without browser window."),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Run the end-to-end automation."""
    _configure_logging(verbose)
    bundle = asyncio.run(orchestrator.run(config, dry_run=dry_run, headless=headless))
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


@app.command("init-session")
def init_session(verbose: bool = typer.Option(False, "--verbose", "-v")) -> None:
    """Establish an authenticated portal session.

    \b
    Run this once to log in and cache the session in session_state.json.
    Subsequent 'provision-api' calls will reuse the session automatically
    (headless, no browser window) until the session expires (~8 hours).

    Reads MCD_PORTAL_EMAIL / MCD_PORTAL_PASSWORD from config/.env to
    pre-fill the login form.  You still complete MFA/CAPTCHA when prompted.
    """
    _configure_logging(verbose)
    _load_dotenv(VIMA_CONFIG / ".env")

    typer.echo("Opening browser to establish portal session...")
    email = os.environ.get("MCD_PORTAL_EMAIL", "")
    if email:
        typer.echo(f"  Credentials found for {email}")
    else:
        typer.echo("  MCD_PORTAL_EMAIL not set — you will need to type your email manually.")

    raw_cfg = {
        "environment": "sandbox",
        "organization": "mastercard",
        "key_password": "foobar!!",
        "projects": [],
    }
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as fh:
        yaml.dump(raw_cfg, fh)
        tmp_path = Path(fh.name)

    try:
        asyncio.run(orchestrator.run(tmp_path, dry_run=True, headless=False))
    finally:
        tmp_path.unlink(missing_ok=True)

    if SESSION_FILE.exists():
        typer.echo(f"Session saved: {SESSION_FILE}")
        typer.echo(
            f"provision-api will now run headless for ~{int(SESSION_MAX_AGE_HOURS)}h. "
            "Re-run init-session when it expires."
        )
    else:
        typer.echo("Warning: session file not written — check logs/execution.log", err=True)


def _find_artifact(normalized_dir: Path, project: str, api: str, exts: tuple[str, ...]) -> Path | None:
    """Find the most recent artifact for a given project/api/extension combo."""
    candidates: list[Path] = []
    project_slug = project.lower().replace(" ", "-")
    api_slug = api.lower()
    for f in normalized_dir.glob("*"):
        if f.suffix.lstrip(".").lower() not in exts:
            continue
        name = f.name.lower()
        if project_slug in name and api_slug in name:
            candidates.append(f)
    if not candidates:
        return None
    return max(candidates, key=lambda p: p.stat().st_mtime)


def _load_dotenv(path: Path) -> None:
    """Load a .env file into os.environ without overriding already-set variables."""
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


def _slug_from_url(url: str) -> str | None:
    """Extract the API portal slug from a Mastercard Developers URL.

    https://developer.mastercard.com/merchant-identifier/documentation/ → 'merchant-identifier'
    """
    path = urlparse(url).path.strip("/")
    if not path:
        return None
    segment = path.split("/")[0]
    return segment or None


def _resolve_api_name(slug: str) -> str:
    """Return the canonical catalog id for a portal slug, or the slug itself for unwired APIs.

    If the slug is not yet in the catalog or API_CONFIG, registers a temporary
    oauth1_standard entry so the portal workflow can run before code wiring is complete.
    """
    from app._vima_catalog import iter_ordered
    from providers.mastercard.api_config import API_CONFIG, ApiSetup

    for entry in iter_ordered():
        if entry.portal_slug == slug:
            return entry.id

    if slug not in API_CONFIG:
        API_CONFIG[slug] = ApiSetup(slug=slug, provision_type="oauth1_standard")
        logger.warning(
            "Slug {!r} not found in catalog — registering with oauth1_standard for this session. "
            "Add to api_config.py once the API module is wired.",
            slug,
        )
    return slug


def _run_deploy(
    cfg: AppConfig,
    normalized: Path,
    env_out: Path,
    keys_dir: Path,
) -> dict[str, dict]:
    """Copy normalized artifacts to keys_dir and write env vars to env_out.

    Returns a dict of deployed api → info for reporting.
    """
    keys_dir.mkdir(parents=True, exist_ok=True)
    lines: list[str] = ["# Generated by mcd-key-automation", ""]
    deployed: dict[str, dict] = {}

    for project in cfg.projects:
        for api_spec in project.normalised_apis():
            api = api_spec.name
            prefix = env_prefix_for(api)

            # OAuth 2.0 (Open Finance / ofin)
            if api in ("ofin", "open_finance"):
                creds_file = _find_artifact(normalized, project.name, api, ("json",))
                pem_file = _find_artifact(normalized, project.name, api, ("pem", "zip"))
                if not creds_file:
                    typer.echo(f"No credentials.json for {project.name}/{api}", err=True)
                    continue
                creds = json.loads(creds_file.read_text())
                lines.append(f"# Mastercard Open Finance — project {project.name}")
                lines.append(f"{prefix}_PARTNER_ID={creds.get('partner_id', '')}")
                lines.append(f"{prefix}_PARTNER_SECRET={creds.get('secret', '')}")
                lines.append(f"{prefix}_APP_KEY={creds.get('app_key', '')}")
                if pem_file:
                    deployed_pem = keys_dir / f"{api}-sig.pem"
                    deployed_pem.write_bytes(pem_file.read_bytes())
                    lines.append(f"{prefix}_SIG_KEY_PATH=config/keys/{deployed_pem.name}")
                lines.append("")
                deployed[api] = {"creds": str(creds_file)}
                continue

            # OAuth 1.0a
            p12 = _find_artifact(normalized, project.name, api, ("p12",))
            creds_file = _find_artifact(normalized, project.name, api, ("json",))
            if not p12:
                typer.echo(f"No p12 found for {project.name}/{api}", err=True)
                continue
            consumer_key = ""
            key_alias = api
            if creds_file:
                try:
                    j = json.loads(creds_file.read_text())
                    consumer_key = j.get("consumer_key", "") or ""
                    key_alias = j.get("key_alias") or api
                except Exception as e:
                    logger.warning("Failed to parse {}: {}", creds_file, e)

            target_p12 = keys_dir / f"{api}.p12"
            target_p12.write_bytes(p12.read_bytes())
            lines.append(f"# {api} (project {project.name})")
            lines.append(f"{prefix}_CONSUMER_KEY={consumer_key}")
            lines.append(f"{prefix}_SIGNING_KEY_PATH=config/keys/{target_p12.name}")
            lines.append(f"{prefix}_SIGNING_KEY_ALIAS={key_alias}")
            lines.append(f"{prefix}_SIGNING_KEY_PASSWORD={cfg.key_password}")
            lines.append(f"{prefix}_ENV=sandbox")
            enc_var = encryption_env_var(api)
            if enc_var:
                lines.append(
                    f"# TODO: {enc_var}=config/keys/{api}-enc.pem  "
                    f"(download manually from portal — not yet automated)"
                )
            lines.append("")
            deployed[api] = {"p12": str(target_p12), "consumer_key_present": bool(consumer_key)}

    env_out.parent.mkdir(parents=True, exist_ok=True)
    env_out.write_text("\n".join(lines))
    return deployed


@app.command()
def deploy(
    config: Path = typer.Option(..., "--config", "-c", exists=True, help="Path to YAML config."),
    env_out: Path = typer.Option(
        VIMA_CONFIG / ".env.generated",
        "--env-out",
        help="Where to write the generated .env file.",
    ),
    keys_dir: Path = typer.Option(
        VIMA_KEYS,
        "--keys-dir",
        help="Where to copy key files (.p12, .pem).",
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Copy downloaded keys to config/keys/ and emit a generated .env."""
    _configure_logging(verbose)
    cfg = load_config(config)
    normalized = WORKSPACE / "normalized"
    if not normalized.is_dir():
        typer.echo(f"No normalized artifacts at {normalized}. Run `mcd-key-automation run` first.", err=True)
        raise typer.Exit(2)
    deployed = _run_deploy(cfg, normalized, env_out, keys_dir)
    typer.echo(f"✅ Wrote {env_out}")
    typer.echo(f"✅ Copied keys to {keys_dir}")
    typer.echo("Deployed:")
    for api, info in deployed.items():
        typer.echo(f"  {api}: {info}")


@app.command("provision-api")
def provision_api(
    url: str = typer.Argument(
        help="Mastercard Developers URL for the API, e.g. "
             "https://developer.mastercard.com/merchant-identifier/documentation/",
    ),
    environment: str = typer.Option("sandbox", "--env", help="sandbox or production"),
    project_name: str | None = typer.Option(
        None, "--project-name", help="Portal project name (default: derived from URL slug)"
    ),
    headful: bool = typer.Option(
        False, "--headful",
        help="Force browser window open (useful when session has expired).",
    ),
    dry_run: bool = typer.Option(False, "--dry-run", help="Stop after login; do not provision."),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Provision keys for one Mastercard API from its documentation URL.

    \b
    Example:
      mcd-key-automation provision-api https://developer.mastercard.com/bin-lookup/documentation/

    Reads MCD_PORTAL_EMAIL / MCD_PORTAL_PASSWORD from config/.env.
    Auto-detects headless mode when a fresh session exists — no browser
    window or human interaction needed.  Run 'init-session' first to
    establish the session; subsequent calls run fully autonomously.
    Credentials are written to config/.env.generated on completion.
    """
    _configure_logging(verbose)
    _load_dotenv(VIMA_CONFIG / ".env")

    slug = _slug_from_url(url)
    if not slug:
        typer.echo(f"ERROR: Could not extract API slug from URL: {url!r}", err=True)
        raise typer.Exit(1)

    api_name = _resolve_api_name(slug)
    pname = project_name or slug

    # Auto-select headless mode when a fresh session exists; headful otherwise.
    headless = not headful and _session_is_fresh()
    mode = "headless" if headless else "headful"
    session_info = _session_age_str()
    typer.echo(
        f"Provisioning {api_name!r}  slug={slug!r}  env={environment}  "
        f"mode={mode}  session={session_info}"
    )
    if not headless and not headful:
        typer.echo(
            "  No fresh session found — browser will open for login.\n"
            "  Tip: run 'init-session' once to cache your session for autonomous re-runs."
        )

    raw_cfg = {
        "environment": environment,
        "organization": "mastercard",
        "key_password": "foobar!!",
        "projects": [{"name": pname, "apis": [api_name]}],
    }
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as fh:
        yaml.dump(raw_cfg, fh)
        tmp_path = Path(fh.name)

    try:
        bundle = asyncio.run(orchestrator.run(tmp_path, dry_run=dry_run, headless=headless))
    except RuntimeError as exc:
        # Headless session-expired error — give a clear recovery instruction.
        typer.echo(f"ERROR: {exc}", err=True)
        typer.echo(
            "\nTo fix: run 'mcd-key-automation init-session' to refresh your session, then retry.",
            err=True,
        )
        raise typer.Exit(1) from None
    finally:
        tmp_path.unlink(missing_ok=True)

    if dry_run:
        typer.echo("Dry run complete.")
        return

    if not bundle:
        typer.echo(
            f"No artifacts produced — check {HERE / 'logs' / 'execution.log'} for details.",
            err=True,
        )
        raise typer.Exit(1)

    typer.echo(f"Bundle: {bundle}")

    cfg = AppConfig(
        environment=environment,  # type: ignore[arg-type]
        projects=[ProjectSpec(name=pname, apis=[api_name])],
    )
    env_out = VIMA_CONFIG / ".env.generated"
    deployed = _run_deploy(cfg, WORKSPACE / "normalized", env_out, VIMA_KEYS)

    typer.echo(f"\n✅ Credentials written to: {env_out}")
    typer.echo("Deployed:")
    for api, info in deployed.items():
        typer.echo(f"  {api}: {info}")
    typer.echo(f"\nMerge into config/.env when ready:\n  cat {env_out} >> {VIMA_CONFIG / '.env'}")

    # Smoke-test the provisioned API
    from app.api_smoke import run_smoke
    typer.echo("\nRunning smoke test…")
    outcome = run_smoke(api_name, url, VIMA_ROOT)
    _print_smoke_outcome(outcome)
    if not outcome.success:
        typer.echo(
            "  Smoke test did not pass — credentials may need more time to activate.\n"
            f"  Re-run: mcd-key-automation test-api {url!r}",
            err=True,
        )


@app.command("test-api")
def test_api(
    url: str = typer.Argument(
        help="Mastercard Developers URL for the API.",
    ),
    api_id: str | None = typer.Option(
        None, "--api-id", help="Override the api_id (default: derived from URL slug)."
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Test a provisioned API: call its first operation and verify credentials work.

    \b
    Example:
      mcd-key-automation test-api https://developer.mastercard.com/bin-lookup/documentation/

    If the first call fails, the command searches the docs URL for sandbox test
    values, retries with those, and patches the MANIFEST if a good response is
    obtained.  Reads credentials from config/.env and config/.env.generated.
    """
    _configure_logging(verbose)
    _load_dotenv(VIMA_CONFIG / ".env")

    slug = _slug_from_url(url)
    if not slug:
        typer.echo(f"ERROR: Could not extract slug from URL: {url!r}", err=True)
        raise typer.Exit(1)

    resolved_id = api_id or _resolve_api_name(slug)

    typer.echo(f"Testing {resolved_id!r}  slug={slug!r}  url={url!r}")

    from app.api_smoke import run_smoke
    outcome = run_smoke(resolved_id, url, VIMA_ROOT)
    _print_smoke_outcome(outcome)

    if not outcome.success:
        raise typer.Exit(1)


def _print_smoke_outcome(outcome) -> None:
    status = "✅ PASS" if outcome.success else "❌ FAIL"
    typer.echo(
        f"  {status}  api={outcome.api_id}  op={outcome.op_id}  "
        f"attempts={outcome.attempts}  status={outcome.status_code}"
    )
    if outcome.sandbox_values_found:
        typer.echo(f"  Sandbox values used: {outcome.params_used}")
    if outcome.manifest_updated:
        typer.echo("  MANIFEST updated with sandbox test values and defaults.")
    if not outcome.success and outcome.error:
        typer.echo(f"  Error: {outcome.error}")


@app.command("export-vima-config")
def export_vima_config_cmd(
    normalized_dir: Path = typer.Option(
        None, "--normalized-dir",
        help="Path to temp/normalized directory (default: temp/normalized beside this tool)",
    ),
    password: str = typer.Option("foobar!!", "--password", help="Keystore password"),
    output: Path = typer.Option(None, "--output", help="Output zip path (default: output/vima-config.zip)"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Build a vima-config.zip from the latest provisioned keys, ready for /config/import."""
    _configure_logging(verbose)
    here = Path(__file__).parent.parent
    nd = normalized_dir or (here / "temp" / "normalized")
    out = output or (here / "output" / "vima-config.zip")

    if not nd.exists():
        typer.echo(f"ERROR: normalized dir not found: {nd}", err=True)
        raise typer.Exit(2)

    sys.path.insert(0, str(here))
    from export_vima_config import build_vima_config_zip
    result = build_vima_config_zip(nd, password, out)
    typer.echo(f"Built: {out.resolve()}")
    typer.echo(f"  APIs     : {', '.join(result['apis'])}")
    if result["skipped"]:
        typer.echo(f"  Skipped  : {', '.join(result['skipped'])}")
    typer.echo(f"\nImport into vima:")
    typer.echo(f"  curl -X POST http://localhost:5001/config/import -F file=@{out.resolve()}")



@app.command("smoke-test")
def smoke_test(
    env_file: Path = typer.Option(
        VIMA_CONFIG / ".env.generated",
        "--env-file",
        exists=True,
        help=".env file with the credentials to test.",
    ),
    only: list[str] = typer.Option(
        None,
        "--only",
        help="Only test these api ids (repeatable). Default: all.",
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Call the first operation on each API to verify the credentials work."""
    _configure_logging(verbose)

    # Load env file into os.environ
    for raw in env_file.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        os.environ[k.strip()] = v.strip()

    # Make sure vima root is importable
    sys.path.insert(0, str(VIMA_ROOT))

    from apis.registry import REGISTRY, ORDER  # noqa: E402

    targets = [a for a in ORDER if (not only or a in only)]
    results: list[tuple[str, str, str]] = []

    for api_id in targets:
        mod = REGISTRY[api_id]
        manifest = mod.MANIFEST
        ops = manifest.get("operations") or []
        if not ops:
            results.append((api_id, "SKIP", "no operations in manifest"))
            continue
        op = ops[0]
        params = {
            p["name"]: p.get("default")
            for p in op.get("params", [])
            if p.get("default") is not None
        }
        try:
            resp = mod.execute(op["id"], params)
            ok = bool(resp.get("success"))
            short = (resp.get("error") or "")[:120]
            results.append((api_id, "PASS" if ok else "FAIL", short or op["id"]))
        except Exception as e:
            results.append((api_id, "ERROR", f"{type(e).__name__}: {str(e)[:120]}"))

    typer.echo("")
    typer.echo(f"{'API':<14} {'STATUS':<7} DETAIL")
    typer.echo("-" * 70)
    for api_id, status, detail in results:
        marker = {"PASS": "✅", "FAIL": "❌", "ERROR": "💥", "SKIP": "⏭️"}.get(status, "?")
        typer.echo(f"{api_id:<14} {marker} {status:<5} {detail}")
    n_pass = sum(1 for _, s, _ in results if s == "PASS")
    typer.echo("")
    typer.echo(f"Summary: {n_pass}/{len(results)} passed")
    if n_pass != len(results):
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
