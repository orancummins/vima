"""Builds manifest.json and import_descriptor.json for the upload bundle."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from app.models import AppConfig, DownloadedArtifact


def build_manifest(config: AppConfig, artifacts: Iterable[DownloadedArtifact]) -> dict:
    arts = list(artifacts)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "environment": config.environment,
        "organization": config.organization,
        "projects": [
            {
                "name": p.name,
                "apis": [a if isinstance(a, str) else a.name for a in p.apis],
            }
            for p in config.projects
        ],
        "artifacts": [a.model_dump() for a in arts],
        "checksums": {a.filename: a.sha256 for a in arts},
    }


def build_import_descriptor(artifacts: Iterable[DownloadedArtifact]) -> dict:
    return {
        "version": "1.0",
        "entries": [
            {
                "alias": a.alias,
                "file": f"certs/{a.filename}",
                "type": a.kind,
                "keystore_type": "PKCS12" if a.kind == "p12" else "PEM",
                "project": a.project,
                "api": a.api,
            }
            for a in artifacts
        ],
    }


def write_json(path: str | Path, data: dict) -> None:
    Path(path).write_text(json.dumps(data, indent=2, sort_keys=True))
