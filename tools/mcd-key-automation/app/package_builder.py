"""Builds the deterministic ZIP bundle."""
from __future__ import annotations

import csv
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Iterable

from loguru import logger

from app.exceptions import PackagingError
from app.manifest_builder import build_import_descriptor, build_manifest, write_json
from app.models import AppConfig, DownloadedArtifact


def build_bundle(
    *,
    config: AppConfig,
    artifacts: Iterable[DownloadedArtifact],
    output_dir: str | Path,
    log_file: str | Path | None = None,
) -> Path:
    arts = _dedupe_artifacts_by_filename(list(artifacts))
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.utcnow().strftime("%Y%m%d")
    bundle_path = output_dir / f"upload_bundle_{stamp}.zip"

    manifest = build_manifest(config, arts)
    descriptor = build_import_descriptor(arts)

    try:
        with zipfile.ZipFile(bundle_path, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("manifest.json", _json_text(manifest))
            z.writestr("import_descriptor.json", _json_text(descriptor))
            for a in arts:
                p = Path(a.path)
                if not p.exists():
                    raise PackagingError(f"Missing artifact file: {p}")
                z.write(p, arcname=f"certs/{a.filename}")
            z.writestr("metadata/aliases.csv", _aliases_csv(arts))
            z.writestr("metadata/hashes.json", _json_text({a.filename: a.sha256 for a in arts}))
            if log_file and Path(log_file).exists():
                z.write(log_file, arcname="logs/execution.log")
    except OSError as e:
        raise PackagingError(f"Failed to build bundle: {e}") from e

    logger.info("Built bundle {}", bundle_path)
    return bundle_path


def _dedupe_artifacts_by_filename(arts: list[DownloadedArtifact]) -> list[DownloadedArtifact]:
    """Keep the latest artifact per output filename to avoid duplicate zip entries."""
    seen: set[str] = set()
    deduped_rev: list[DownloadedArtifact] = []
    dropped = 0
    for a in reversed(arts):
        if a.filename in seen:
            dropped += 1
            continue
        seen.add(a.filename)
        deduped_rev.append(a)
    deduped = list(reversed(deduped_rev))
    if dropped:
        logger.warning("Dropped {} duplicate artifact(s) by filename during bundle build", dropped)
    return deduped


def _json_text(obj: dict) -> str:
    import json
    return json.dumps(obj, indent=2, sort_keys=True)


def _aliases_csv(arts: list[DownloadedArtifact]) -> str:
    import io
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["alias", "filename", "kind", "project", "api", "sha256"])
    for a in arts:
        w.writerow([a.alias, a.filename, a.kind, a.project, a.api, a.sha256])
    return buf.getvalue()
