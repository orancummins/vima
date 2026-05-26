"""File validation utilities — hashing and basic cert sniffing."""
from __future__ import annotations

import hashlib
from pathlib import Path


def sha256_file(path: str | Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def classify_extension(filename: str) -> str:
    ext = Path(filename).suffix.lstrip(".").lower()
    if ext in {"p12", "pem", "crt", "key", "json"}:
        return ext
    return "other"
