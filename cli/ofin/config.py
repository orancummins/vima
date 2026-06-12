"""Credential resolution for the ofin CLI/SDK.

Resolution order (highest precedence first):

1. Explicit values passed in code / CLI flags.
2. OS environment variables.
3. An ``--env-file`` provided on the command line.
4. The repo's ``config/.env`` (auto-discovered by walking up from CWD and from
   the package location — dev convenience).
5. A config file bundled inside the artifact (``ofin/_bundled_config.env``),
   written by ``cli/build.py`` from the repo's single source of truth.

Env files are parsed with a tiny ``KEY=VALUE`` reader (no python-dotenv
dependency, so the CLI stays stdlib-only). Existing OS env vars are never
overwritten by file values, preserving the precedence above.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Dict, List, Optional


# ---------------------------------------------------------------------------
# .env parsing + discovery
# ---------------------------------------------------------------------------
def parse_env_file(path: str) -> Dict[str, str]:
    """Parse a ``KEY=VALUE`` file. Ignores blanks/comments; strips quotes."""
    out: Dict[str, str] = {}
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for raw in fh:
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                if line.lower().startswith("export "):
                    line = line[7:].strip()
                if "=" not in line:
                    continue
                key, _, val = line.partition("=")
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if key:
                    out[key] = val
    except OSError:
        return {}
    return out


def _candidate_repo_envs() -> List[str]:
    """Return plausible repo ``config/.env`` paths, nearest first."""
    candidates: List[str] = []
    # Walk up from the current working directory.
    cwd = os.path.abspath(os.getcwd())
    node = cwd
    while True:
        candidates.append(os.path.join(node, "config", ".env"))
        parent = os.path.dirname(node)
        if parent == node:
            break
        node = parent
    # Walk up from this file's location (cli/ofin/config.py -> repo root).
    here = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(here, "..", ".."))
    candidates.append(os.path.join(repo_root, "config", ".env"))
    # Dedupe, preserve order.
    seen = set()
    uniq = []
    for c in candidates:
        if c not in seen:
            seen.add(c)
            uniq.append(c)
    return uniq


def _bundled_config_path() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "_bundled_config.env")


def config_sources(env_file: Optional[str] = None) -> List[str]:
    """Return the human-readable list of config files actually in effect.

    Useful for the no-args welcome / ``config show`` so users can see exactly
    where credentials are being read from, in precedence order (highest first).
    """
    sources: List[str] = []
    if any(k.startswith("OPEN_FINANCE") for k in os.environ):
        sources.append("OS environment variables")
    if env_file and os.path.isfile(env_file):
        sources.append(f"--env-file: {os.path.abspath(env_file)}")
    for cand in _candidate_repo_envs():
        if os.path.isfile(cand):
            sources.append(f"repo config: {cand}")
            break
    bundled = _bundled_config_path()
    if os.path.isfile(bundled):
        sources.append(f"bundled: {bundled}")
    return sources


def build_env(env_file: Optional[str] = None) -> Dict[str, str]:
    """Build the effective environment mapping per the documented precedence.

    OS environment wins; then ``env_file``; then the nearest repo ``config/.env``;
    then the bundled config. Returns a plain dict (a snapshot, not ``os.environ``).
    """
    merged: Dict[str, str] = {}

    # Lowest precedence: bundled config.
    bundled = _bundled_config_path()
    if os.path.isfile(bundled):
        merged.update(parse_env_file(bundled))

    # Then nearest repo config/.env (first existing candidate only).
    for cand in _candidate_repo_envs():
        if os.path.isfile(cand):
            merged.update(parse_env_file(cand))
            break

    # Then an explicit --env-file.
    if env_file:
        if not os.path.isfile(env_file):
            raise FileNotFoundError(f"--env-file not found: {env_file}")
        merged.update(parse_env_file(env_file))

    # Highest precedence: real OS environment.
    for k, v in os.environ.items():
        merged[k] = v

    return merged


# ---------------------------------------------------------------------------
# Per-region credential views
# ---------------------------------------------------------------------------
_PLACEHOLDERS = {"", "your_partner_id_here", "your_client_id_here", "changeme"}


def _resolve_key_path(path: str, env_file: Optional[str] = None) -> str:
    """Resolve an EU key/cert path to an on-disk location.

    Absolute paths that exist pass through. Relative paths are resolved against
    a series of base directories, in priority order:

    1. The directory of an explicit ``--env-file`` (so a portable ``dist/``
       folder with ``ofin.env`` + ``keys/`` works when copied anywhere).
    2. The repo root (dev convenience for ``config/keys/...`` paths).
    3. The package directory (alongside any bundled config).

    The keys must be real files — the EU client opens them with ``open()`` —
    so they are never stored inside the ``.pyz`` zip.
    """
    if not path:
        return path
    if os.path.isabs(path) and os.path.exists(path):
        return path
    bases: List[str] = []
    if env_file:
        bases.append(os.path.dirname(os.path.abspath(env_file)))
    for cand in _candidate_repo_envs():
        if os.path.isfile(cand):
            bases.append(os.path.dirname(os.path.dirname(cand)))  # repo root
            break
    bases.append(os.path.dirname(_bundled_config_path()))
    for base in bases:
        candidate = os.path.normpath(os.path.join(base, path))
        if os.path.exists(candidate):
            return candidate
    return path  # return as-is; the client will raise a clear error if missing


@dataclass
class USConfig:
    partner_id: str = ""
    partner_secret: str = ""
    app_key: str = ""
    base_url: str = "https://api.finicity.com"

    @property
    def configured(self) -> bool:
        return all(v not in _PLACEHOLDERS for v in (self.partner_id, self.partner_secret, self.app_key))

    def missing_message(self) -> str:
        return (
            "Open Finance US is not configured. Set OPEN_FINANCE_PARTNER_ID, "
            "OPEN_FINANCE_PARTNER_SECRET and OPEN_FINANCE_APP_KEY (env, --env-file, "
            "or config/.env)."
        )


@dataclass
class AUConfig:
    partner_id: str = ""
    partner_secret: str = ""
    app_key: str = ""
    base_url: str = "https://api.openbanking.mastercard.com.au"

    @property
    def configured(self) -> bool:
        return all(v not in _PLACEHOLDERS for v in (self.partner_id, self.partner_secret, self.app_key))

    def missing_message(self) -> str:
        return (
            "Open Finance AU is not configured. Set OPEN_FINANCE_AU_PARTNER_ID, "
            "OPEN_FINANCE_AU_PARTNER_SECRET and OPEN_FINANCE_AU_APP_KEY."
        )


@dataclass
class EUConfig:
    client_id: str = ""
    private_key_path: str = ""
    public_cert_path: str = ""
    application_id: str = ""
    auth_base_url: str = ""
    api_base_url: str = ""
    use_case_id: str = ""

    @property
    def configured(self) -> bool:
        return (
            self.client_id not in _PLACEHOLDERS
            and bool(self.private_key_path)
            and bool(self.public_cert_path)
        )

    def missing_message(self) -> str:
        return (
            "Open Finance EU is not configured. Set OPEN_FINANCE_EU_CLIENT_ID, "
            "OPEN_FINANCE_EU_PRIVATE_KEY_PATH and OPEN_FINANCE_EU_PUBLIC_CERT_PATH."
        )


@dataclass
class Config:
    us: USConfig
    au: AUConfig
    eu: EUConfig
    source_env: Dict[str, str]

    @classmethod
    def resolve(cls, env_file: Optional[str] = None) -> "Config":
        env = build_env(env_file)
        us = USConfig(
            partner_id=env.get("OPEN_FINANCE_PARTNER_ID", ""),
            partner_secret=env.get("OPEN_FINANCE_PARTNER_SECRET", ""),
            app_key=env.get("OPEN_FINANCE_APP_KEY", ""),
            base_url=env.get("OPEN_FINANCE_API_BASE_URL", "https://api.finicity.com"),
        )
        au = AUConfig(
            partner_id=env.get("OPEN_FINANCE_AU_PARTNER_ID", ""),
            partner_secret=env.get("OPEN_FINANCE_AU_PARTNER_SECRET", ""),
            app_key=env.get("OPEN_FINANCE_AU_APP_KEY", ""),
            base_url=env.get("OPEN_FINANCE_AU_API_BASE_URL", "https://api.openbanking.mastercard.com.au"),
        )
        eu = EUConfig(
            client_id=env.get("OPEN_FINANCE_EU_CLIENT_ID", ""),
            private_key_path=_resolve_key_path(env.get("OPEN_FINANCE_EU_PRIVATE_KEY_PATH", ""), env_file),
            public_cert_path=_resolve_key_path(env.get("OPEN_FINANCE_EU_PUBLIC_CERT_PATH", ""), env_file),
            application_id=env.get("OPEN_FINANCE_EU_APPLICATION_ID", ""),
            auth_base_url=env.get("OPEN_FINANCE_EU_AUTH_BASE_URL", ""),
            api_base_url=env.get("OPEN_FINANCE_EU_API_BASE_URL", ""),
            use_case_id=env.get("OPEN_FINANCE_EU_USE_CASE_ID", ""),
        )
        return cls(us=us, au=au, eu=eu, source_env=env)
