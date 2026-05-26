"""Deterministic alias and filename generation.

Format:  <org>-<env>-<project>-<api>-<purpose>-v<version>
Example: mastercard-sbx-binlookup-signing-v1
"""
from __future__ import annotations

import re

_ENV_SHORT = {"sandbox": "sbx", "production": "prd"}
_SLUG_RE = re.compile(r"[^a-z0-9]+")


def _slug(value: str) -> str:
    return _SLUG_RE.sub("-", value.lower()).strip("-")


def make_alias(
    *,
    organization: str,
    environment: str,
    project: str,
    api: str,
    purpose: str = "signing",
    version: str = "1",
) -> str:
    env = _ENV_SHORT.get(environment, _slug(environment))
    parts = [_slug(organization), env, _slug(project), _slug(api), _slug(purpose), f"v{version}"]
    return "-".join(p for p in parts if p)


def make_filename(alias: str, extension: str) -> str:
    ext = extension.lstrip(".").lower()
    return f"{alias}.{ext}"
