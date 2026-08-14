"""YAML config loading + validation."""
from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import ValidationError

from app.exceptions import ConfigError
from app.models import AppConfig


def load_config(path: str | Path) -> AppConfig:
    p = Path(path)
    if not p.exists():
        raise ConfigError(f"Config file not found: {p}")
    try:
        raw = yaml.safe_load(p.read_text())
    except yaml.YAMLError as e:
        raise ConfigError(f"Invalid YAML in {p}: {e}") from e
    if not isinstance(raw, dict):
        raise ConfigError(f"Config root must be a mapping in {p}")
    try:
        return AppConfig.model_validate(raw)
    except ValidationError as e:
        raise ConfigError(f"Config validation failed: {e}") from e
