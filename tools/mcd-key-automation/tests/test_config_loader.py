import pytest

from app.config_loader import load_config
from app.exceptions import ConfigError


def test_load_sandbox(tmp_path):
    p = tmp_path / "c.yaml"
    p.write_text(
        """
environment: sandbox
organization: mastercard
projects:
  - name: A
    apis: [binlookup]
"""
    )
    cfg = load_config(p)
    assert cfg.environment == "sandbox"
    assert cfg.projects[0].name == "A"


def test_duplicate_projects(tmp_path):
    p = tmp_path / "c.yaml"
    p.write_text(
        """
environment: sandbox
projects:
  - name: A
    apis: [x]
  - name: a
    apis: [y]
"""
    )
    with pytest.raises(ConfigError):
        load_config(p)
