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


def _find_artifact(normalized_dir: Path, project: str, api: str, exts: tuple[str, ...], purpose: str | None = None) -> Path | None:
    """Find the most recent artifact for a given project/api/extension combo.

    If ``purpose`` is given (e.g. 'signing' or 'enc'), only files whose name
    contains ``-{purpose}-`` are considered.  This prevents enc P12s from
    being returned when the caller wants the signing P12.
    """
    candidates: list[Path] = []
    project_slug = project.lower().replace(" ", "-").replace("_", "-")
    # make_alias() slug-ifies '_' → '-' in filenames, so always search by the
    # kebab form regardless of whether api_name uses snake or kebab.
    api_slug = api.lower().replace("_", "-")
    for f in normalized_dir.glob("*"):
        if f.suffix.lstrip(".").lower() not in exts:
            continue
        name = f.name.lower()
        if project_slug in name and api_slug in name:
            if purpose and f"-{purpose}-" not in name:
                continue
            candidates.append(f)
    if candidates:
        return max(candidates, key=lambda p: p.stat().st_mtime)

    # Fallback for .p12 lookups: the portal delivers the signing key inside a
    # password-protected zip, and the orchestrator leaves it that way. If a
    # matching zip exists, extract the first .p12 entry next to it so the
    # caller can read it via its returned Path.
    if "p12" in exts:
        for f in normalized_dir.glob("*.zip"):
            name = f.name.lower()
            if project_slug not in name or api_slug not in name:
                continue
            if purpose and f"-{purpose}-" not in name:
                continue
            try:
                import zipfile
                with zipfile.ZipFile(f) as zf:
                    p12_members = [n for n in zf.namelist() if n.lower().endswith(".p12")]
                    if not p12_members:
                        continue
                    member = p12_members[0]
                    extracted = normalized_dir / f"{f.stem}.p12"
                    extracted.write_bytes(zf.read(member))
                    return extracted
            except Exception as exc:
                logger.warning("Failed to extract .p12 from {}: {}", f, exc)
    return None


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
    """Return the canonical catalog id for a portal slug, or a snake_case id for unwired APIs.

    Existing catalog entries are returned as-is (already snake_case, e.g.
    'consumer_clarity', 'bin_lookup'). For a brand-new portal slug like
    'enhanced-currency-conversion-calculator', we register it under its
    snake_case form ('enhanced_currency_conversion_calculator') so the signing
    key alias, ``.env`` prefix, and key file basename all follow the same
    convention used by every other API in ``config/.env``.

    If a recorded playbook exists for the portal slug, registers with
    ``provision_type=playbook`` (record-once-replay-forever). Otherwise falls
    back to ``oauth1_standard`` with a clear warning.
    """
    from app._vima_catalog import iter_ordered
    from providers.mastercard.api_config import API_CONFIG, ApiSetup

    for entry in iter_ordered():
        if entry.portal_slug == slug:
            return entry.id

    # Normalise kebab → snake to match existing alias/env-var conventions.
    api_name = slug.replace("-", "_")

    if api_name not in API_CONFIG:
        playbook_file = HERE / "playbooks" / "mastercard" / f"{slug}.json"
        if playbook_file.is_file():
            API_CONFIG[api_name] = ApiSetup(slug=slug, provision_type="playbook")
            logger.info(
                "Slug {!r} not in catalog — using recorded playbook at {} "
                "(api_name={!r})",
                slug, playbook_file, api_name,
            )
        else:
            API_CONFIG[api_name] = ApiSetup(slug=slug, provision_type="oauth1_standard")
            logger.warning(
                "Slug {!r} not found in catalog and no playbook recorded — "
                "falling back to oauth1_standard (api_name={!r}). If the portal "
                "wizard for this API has more than project-name + alias/password "
                "fields (extra dropdowns, radios, etc.), the Proceed button will "
                "stay disabled and provisioning will time out. Record the flow with:"
                "\n  ./addapi.sh --record https://developer.mastercard.com/{}/documentation/",
                slug, api_name, slug,
            )
    return api_name


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
            p12 = _find_artifact(normalized, project.name, api, ("p12",), purpose="signing")
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
                enc_artifact = _find_artifact(normalized, project.name, api, ("pem", "p12"), purpose="enc")
                if enc_artifact:
                    target_enc = keys_dir / f"{api}-clientenc.pem"
                    if enc_artifact.suffix.lower() == ".p12":
                        # Extract Mastercard's certificate from the enc P12 and save as PEM.
                        try:
                            from cryptography.hazmat.primitives.serialization import pkcs12 as _pkcs12
                            from cryptography.hazmat.primitives.serialization import Encoding
                            _, cert, _ = _pkcs12.load_key_and_certificates(
                                enc_artifact.read_bytes(), cfg.key_password.encode()
                            )
                            target_enc.write_bytes(cert.public_bytes(Encoding.PEM))
                            logger.info("Extracted enc cert from P12 → {}", target_enc)
                        except Exception as exc:
                            logger.warning("Failed to extract cert from enc P12 for {}: {}", api, exc)
                            lines.append(f"# TODO: {enc_var}=config/keys/{api}-clientenc.pem  (enc P12 extraction failed: {exc})")
                            enc_artifact = None  # fall through
                    else:
                        target_enc.write_bytes(enc_artifact.read_bytes())
                    if enc_artifact:  # write env var only if deployment succeeded
                        lines.append(f"{enc_var}=config/keys/{target_enc.name}")
                else:
                    lines.append(
                        f"# TODO: {enc_var}=config/keys/{api}-clientenc.pem  "
                        f"(not found in provisioning run — re-run addapi)"
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

    # If this API has a portal flow that needs to be recorded (no playbook
    # found yet) print a clear hint before attempting to provision.
    _hint_missing_playbook(api_name, slug)

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


# ---------------------------------------------------------------------------
# Playbook record / replay support
# ---------------------------------------------------------------------------

PLAYBOOK_DIR = HERE / "playbooks" / "mastercard"


def _playbook_path_for(api_slug: str) -> Path:
    return PLAYBOOK_DIR / f"{api_slug}.json"


def _hint_missing_playbook(api_name: str, slug: str) -> None:
    """If MATCH-style (provision_type == playbook) and no JSON recorded, hint."""
    try:
        from providers.mastercard.api_config import API_CONFIG
        cfg = API_CONFIG.get(api_name)
    except Exception:
        return
    if cfg is None:
        return
    pb = _playbook_path_for(cfg.slug)

    if cfg.provision_type == "playbook":
        if pb.is_file():
            return
        typer.echo(
            f"\nERROR: API {api_name!r} uses the playbook driver but no playbook "
            f"was found at {pb}.\n"
            f"Record one first with:\n"
            f"  ./addapi.sh --record https://developer.mastercard.com/{cfg.slug}/documentation/\n",
            err=True,
        )
        raise typer.Exit(1)

    # Slug is using the default oauth1_standard fallback because it wasn't in the
    # catalog. If a playbook exists, the resolver should have picked it up; if
    # not, warn the operator before we burn ~45s waiting on a possibly-hung wizard.
    is_uncatalogued = api_name == slug and cfg.provision_type == "oauth1_standard"
    if is_uncatalogued and not pb.is_file():
        typer.echo(
            f"\nNOTE: {slug!r} is not in the catalog and no playbook was recorded.\n"
            f"  Falling back to the standard oauth1 wizard. If that wizard has\n"
            f"  extra required fields (radios, dropdowns, etc.), Proceed will\n"
            f"  stay disabled and this will fail after ~45s.\n"
            f"  If it fails, record the flow once with:\n"
            f"    ./addapi.sh --record https://developer.mastercard.com/{slug}/documentation/\n",
            err=True,
        )


@app.command("record-api")
def record_api(
    api_slug: str = typer.Option(
        ..., "--api-slug",
        help="Portal API slug (e.g. 'match', 'bin-lookup').",
    ),
    start_url: str | None = typer.Option(
        None, "--start-url",
        help="Portal create-project URL. Defaults to the standard create-project page for this slug.",
    ),
    organization: str = typer.Option("mastercard", "--organization"),
    no_prompt: bool = typer.Option(
        False, "--no-prompt",
        help="Skip interactive variable mapping at the end (keep literal values).",
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Record a portal create-project flow into a replayable playbook.

    Opens a headful browser. Drive the flow manually end-to-end (create
    project, download key file). When done, return to this terminal and
    press Enter — the recorded steps are compressed into
    ``playbooks/<organization>/<api-slug>.json`` which the regular
    ``provision-api`` command will replay autonomously thereafter.
    """
    _configure_logging(verbose)
    _load_dotenv(VIMA_CONFIG / ".env")

    if start_url is None:
        start_url = f"https://developer.mastercard.com/create-project?services={api_slug}"

    from app.playbook_record import _record_async  # local import; heavy deps
    asyncio.run(_record_async(api_slug, start_url, organization, headed=True, no_prompt=no_prompt))


if __name__ == "__main__":
    app()
