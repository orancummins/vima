"""Unit tests for the deterministic provisioning pipeline.

Covers the parts of the key-acquisition flow that can be verified without a
live browser or network connection:

  - _find_artifact  : direct p12 match, zip-fallback extraction, cross-API isolation
  - Project name    : 50-char truncation invariant
  - Playbook loading: schema validation, variable completeness check
  - Variable subst  : single/multi var, undefined raises, non-string passthrough
  - Package builder : deduplication, required bundle entries, missing-file raises
  - api_config      : every catalog entry maps to a valid ProvisionType
  - Playbook files  : every .json in playbooks/mastercard/ loads clean
"""
from __future__ import annotations

import hashlib
import json
import sys
import zipfile
from pathlib import Path

import pytest

# Ensure the tool root is on sys.path for all imports below.
TOOL_ROOT = Path(__file__).resolve().parent.parent
if str(TOOL_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOL_ROOT))

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_zip(path: Path, *, member: str = "signing.p12", content: bytes = b"FAKEP12") -> None:
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr(member, content)


# ---------------------------------------------------------------------------
# _find_artifact
# ---------------------------------------------------------------------------

import importlib
_main = importlib.import_module("app.main")
_find_artifact = _main._find_artifact


class TestFindArtifact:
    def test_direct_p12_match(self, tmp_path):
        p12 = tmp_path / "mastercard-sbx-my-project-bin-lookup-signing-v1.p12"
        p12.write_bytes(b"data")
        assert _find_artifact(tmp_path, "my-project", "bin_lookup", ("p12",)) == p12

    def test_direct_json_match(self, tmp_path):
        creds = tmp_path / "mastercard-sbx-my-project-bin-lookup-signing-v1-credentials.json"
        creds.write_text('{"consumer_key":"abc"}')
        assert _find_artifact(tmp_path, "my-project", "bin_lookup", ("json",)) == creds

    def test_no_match_returns_none(self, tmp_path):
        (tmp_path / "unrelated.p12").write_bytes(b"x")
        assert _find_artifact(tmp_path, "my-project", "bin_lookup", ("p12",)) is None

    def test_zip_fallback_extracts_p12(self, tmp_path):
        zip_path = tmp_path / "mastercard-sbx-my-project-bin-lookup-signing-v1.zip"
        _make_zip(zip_path, member="mastercard_signing_key.p12", content=b"P12BYTES")
        result = _find_artifact(tmp_path, "my-project", "bin_lookup", ("p12",))
        assert result is not None
        assert result.suffix == ".p12"
        assert result.read_bytes() == b"P12BYTES"

    def test_zip_fallback_not_triggered_for_non_p12_exts(self, tmp_path):
        zip_path = tmp_path / "mastercard-sbx-my-project-bin-lookup-signing-v1.zip"
        _make_zip(zip_path)
        assert _find_artifact(tmp_path, "my-project", "bin_lookup", ("json",)) is None

    def test_zip_fallback_respects_slug_filter(self, tmp_path):
        zip_path = tmp_path / "mastercard-sbx-other-project-other-api-signing-v1.zip"
        _make_zip(zip_path)
        assert _find_artifact(tmp_path, "my-project", "bin_lookup", ("p12",)) is None

    def test_zip_without_p12_member_returns_none(self, tmp_path):
        zip_path = tmp_path / "mastercard-sbx-my-project-bin-lookup-signing-v1.zip"
        with zipfile.ZipFile(zip_path, "w") as zf:
            zf.writestr("readme.txt", "no keys here")
        assert _find_artifact(tmp_path, "my-project", "bin_lookup", ("p12",)) is None

    def test_direct_p12_preferred_over_zip(self, tmp_path):
        p12 = tmp_path / "mastercard-sbx-my-project-bin-lookup-signing-v1.p12"
        p12.write_bytes(b"direct")
        zip_path = tmp_path / "mastercard-sbx-my-project-bin-lookup-signing-v1.zip"
        _make_zip(zip_path, content=b"fromzip")
        result = _find_artifact(tmp_path, "my-project", "bin_lookup", ("p12",))
        assert result == p12
        assert result.read_bytes() == b"direct"

    def test_snake_case_api_name_normalised(self, tmp_path):
        p12 = tmp_path / "mastercard-sbx-my-project-bin-lookup-signing-v1.p12"
        p12.write_bytes(b"data")
        # Pass snake_case — must still find the kebab filename.
        assert _find_artifact(tmp_path, "my-project", "bin_lookup", ("p12",)) == p12

    def test_cross_api_isolation(self, tmp_path):
        """An artifact for api-a must not be returned when searching for api-b."""
        p12_a = tmp_path / "mastercard-sbx-proj-api-a-signing-v1.p12"
        p12_a.write_bytes(b"a")
        assert _find_artifact(tmp_path, "proj", "api_b", ("p12",)) is None

    def test_most_recent_returned_when_multiple(self, tmp_path):
        import time
        old = tmp_path / "mastercard-sbx-my-project-bin-lookup-signing-v1-a.p12"
        old.write_bytes(b"old")
        time.sleep(0.05)
        new = tmp_path / "mastercard-sbx-my-project-bin-lookup-signing-v1-b.p12"
        new.write_bytes(b"new")
        assert _find_artifact(tmp_path, "my-project", "bin_lookup", ("p12",)) == new


# ---------------------------------------------------------------------------
# Project name truncation (50-char portal limit)
# ---------------------------------------------------------------------------

def _portal_name(project_name: str, ts: str = "20260528103531", prefix: str = "SS") -> str:
    """Mirror of the truncation logic in project_workflow.py:ensure_project_with_api."""
    portal_name = f"{prefix}-{project_name}-{ts}"
    _MAX = 50
    if len(portal_name) > _MAX:
        overflow = len(portal_name) - _MAX
        trimmed = project_name[: max(1, len(project_name) - overflow)]
        portal_name = f"{prefix}-{trimmed}-{ts}"
    return portal_name


class TestPortalNameTruncation:
    def test_short_name_unchanged(self):
        result = _portal_name("bin-lookup")
        assert result == "SS-bin-lookup-20260528103531"
        assert len(result) <= 50

    def test_long_name_truncated_to_50(self):
        result = _portal_name("enhanced-currency-conversion-calculator")
        assert len(result) == 50
        assert result.startswith("SS-")
        assert result.endswith("-20260528103531")

    def test_prefix_and_suffix_always_present(self):
        result = _portal_name("a-very-long-api-slug-that-clearly-overflows-the-limit")
        assert result.startswith("SS-")
        assert result.endswith("-20260528103531")
        assert len(result) <= 50

    def test_extreme_slug_preserves_at_least_one_char(self):
        result = _portal_name("x" * 100)
        assert result.startswith("SS-x")
        assert len(result) <= 50

    def test_exactly_50_chars_unchanged(self):
        ts = "20260528103531"  # 14 chars; "SS-" (3) + name + "-" (1) + ts (14) = 50 → name = 32
        name = "a" * 32
        result = _portal_name(name, ts)
        assert result == f"SS-{name}-{ts}"
        assert len(result) == 50

    def test_sst_prefix_for_tests(self):
        result = _portal_name("bin-lookup", prefix="SST")
        assert result == "SST-bin-lookup-20260528103531"
        assert len(result) <= 50

    def test_sst_long_name_truncated_to_50(self):
        result = _portal_name("enhanced-currency-conversion-calculator", prefix="SST")
        assert len(result) == 50
        assert result.startswith("SST-")
        assert result.endswith("-20260528103531")


# ---------------------------------------------------------------------------
# Playbook loading & variable completeness
# ---------------------------------------------------------------------------

from providers.mastercard.playbook_runner import load_playbook, substitute


class TestLoadPlaybook:
    def _write(self, tmp_path: Path, data: dict) -> Path:
        p = tmp_path / "test.json"
        p.write_text(json.dumps(data))
        return p

    def test_valid_playbook_loads(self, tmp_path):
        p = self._write(tmp_path, {
            "schema": 1,
            "variables": ["project_name"],
            "steps": [{"action": "sleep", "ms": 100}],
        })
        pb = load_playbook(p)
        assert pb["schema"] == 1

    def test_wrong_schema_raises(self, tmp_path):
        p = self._write(tmp_path, {"schema": 2, "steps": []})
        with pytest.raises(ValueError, match="Unsupported playbook schema"):
            load_playbook(p)

    def test_missing_steps_raises(self, tmp_path):
        p = self._write(tmp_path, {"schema": 1})
        with pytest.raises(ValueError, match="missing 'steps'"):
            load_playbook(p)

    def test_undeclared_variable_raises(self, tmp_path):
        p = self._write(tmp_path, {
            "schema": 1,
            "variables": ["project_name"],
            "steps": [{"action": "fill", "selector": "input", "value": "{{undeclared}}"}],
        })
        with pytest.raises(ValueError, match="undeclared variable"):
            load_playbook(p)

    def test_variable_in_defaults_is_valid(self, tmp_path):
        """Variables declared only in 'defaults' must not raise."""
        p = self._write(tmp_path, {
            "schema": 1,
            "variables": [],
            "defaults": {"ica": "123"},
            "steps": [{"action": "fill", "selector": "input", "value": "{{ica}}"}],
        })
        load_playbook(p)  # must not raise

    def test_no_variables_key_still_validates(self, tmp_path):
        """A playbook with no 'variables' key and no {{tokens}} should load fine."""
        p = self._write(tmp_path, {
            "schema": 1,
            "steps": [{"action": "sleep", "ms": 100}],
        })
        load_playbook(p)  # must not raise

    def test_match_playbook_loads_clean(self):
        match_path = TOOL_ROOT / "playbooks" / "mastercard" / "match.json"
        if not match_path.exists():
            pytest.skip("match.json not present")
        load_playbook(match_path)  # must not raise


# ---------------------------------------------------------------------------
# Variable substitution
# ---------------------------------------------------------------------------

class TestSubstitute:
    def test_single_variable(self):
        assert substitute("Hello {{name}}!", {"name": "world"}) == "Hello world!"

    def test_multiple_variables(self):
        assert substitute("{{a}}-{{b}}", {"a": "foo", "b": "bar"}) == "foo-bar"

    def test_undefined_variable_raises(self):
        with pytest.raises(KeyError, match="missing"):
            substitute("{{missing}}", {})

    def test_non_string_passthrough(self):
        assert substitute(42, {"x": "y"}) == 42
        assert substitute(None, {}) is None

    def test_spaces_around_variable_name(self):
        assert substitute("{{ name }}", {"name": "val"}) == "val"


# ---------------------------------------------------------------------------
# Package builder
# ---------------------------------------------------------------------------

from app.package_builder import _dedupe_artifacts_by_filename, build_bundle
from app.exceptions import PackagingError
from app.models import AppConfig, DownloadedArtifact, ProjectSpec


def _artifact(filename: str, tmp_path: Path, api: str = "test-api") -> DownloadedArtifact:
    p = tmp_path / filename
    p.write_bytes(b"cert-data")
    sha = hashlib.sha256(b"cert-data").hexdigest()
    return DownloadedArtifact(
        alias=f"alias-{filename}",
        filename=filename,
        path=str(p),
        sha256=sha,
        kind="p12",
        project="test-project",
        api=api,
    )


def _config() -> AppConfig:
    return AppConfig(
        environment="sandbox",
        organization="mastercard",
        key_password="foobar!!",
        projects=[ProjectSpec(name="P", apis=["bin_lookup"])],
    )


class TestDedupeArtifacts:
    def test_unique_filenames_kept(self, tmp_path):
        arts = [_artifact("a.p12", tmp_path), _artifact("b.p12", tmp_path)]
        assert len(_dedupe_artifacts_by_filename(arts)) == 2

    def test_duplicate_filename_keeps_last(self, tmp_path):
        a1 = _artifact("a.p12", tmp_path)
        a2 = _artifact("a.p12", tmp_path)
        result = _dedupe_artifacts_by_filename([a1, a2])
        assert len(result) == 1
        assert result[0] is a2

    def test_empty_input(self):
        assert _dedupe_artifacts_by_filename([]) == []


class TestBuildBundle:
    def test_required_entries_present(self, tmp_path):
        art = _artifact("mastercard-sbx-p-bin-lookup-signing-v1.p12", tmp_path)
        bundle = build_bundle(config=_config(), artifacts=[art], output_dir=tmp_path)
        with zipfile.ZipFile(bundle) as zf:
            names = zf.namelist()
        assert "manifest.json" in names
        assert "import_descriptor.json" in names
        assert "metadata/aliases.csv" in names
        assert "metadata/hashes.json" in names
        assert f"certs/{art.filename}" in names

    def test_manifest_artifact_count(self, tmp_path):
        arts = [
            _artifact("mastercard-sbx-p-api1-signing-v1.p12", tmp_path, api="api1"),
            _artifact("mastercard-sbx-p-api2-signing-v1.p12", tmp_path, api="api2"),
        ]
        bundle = build_bundle(config=_config(), artifacts=arts, output_dir=tmp_path)
        with zipfile.ZipFile(bundle) as zf:
            manifest = json.loads(zf.read("manifest.json"))
        assert len(manifest["artifacts"]) == 2

    def test_duplicate_artifacts_deduped(self, tmp_path):
        art = _artifact("dup.p12", tmp_path)
        bundle = build_bundle(config=_config(), artifacts=[art, art], output_dir=tmp_path)
        with zipfile.ZipFile(bundle) as zf:
            cert_entries = [n for n in zf.namelist() if n.startswith("certs/")]
        assert len(cert_entries) == 1

    def test_missing_artifact_file_raises(self, tmp_path):
        art = _artifact("gone.p12", tmp_path)
        (tmp_path / "gone.p12").unlink()
        with pytest.raises(PackagingError, match="Missing artifact file"):
            build_bundle(config=_config(), artifacts=[art], output_dir=tmp_path)


# ---------------------------------------------------------------------------
# api_config: every catalog entry has a valid ProvisionType
# ---------------------------------------------------------------------------

from providers.mastercard.api_config import API_CONFIG, ProvisionType
import typing

_VALID_TYPES: set[str] = set(typing.get_args(ProvisionType))


class TestApiConfig:
    def test_all_entries_have_valid_provision_type(self):
        for name, setup in API_CONFIG.items():
            assert setup.provision_type in _VALID_TYPES, (
                f"{name!r} has unknown provision_type {setup.provision_type!r}"
            )

    def test_all_entries_have_slug(self):
        for name, setup in API_CONFIG.items():
            assert setup.slug, f"{name!r} has empty slug"

    def test_oauth2_region_entries_have_region(self):
        for name, setup in API_CONFIG.items():
            if setup.provision_type == "oauth2_region":
                assert setup.region, f"{name!r} is oauth2_region but has no region set"

    def test_known_ids_present(self):
        for api_id in ("bin_lookup", "places", "easy_savings", "match", "open_finance"):
            assert api_id in API_CONFIG, f"Expected {api_id!r} in API_CONFIG"

    def test_match_uses_playbook(self):
        assert API_CONFIG["match"].provision_type == "playbook"

    def test_transaction_notifications_skips_step3(self):
        assert API_CONFIG["transaction_notifications"].provision_type == "oauth1_skip_step3"

    def test_open_finance_is_oauth2_region(self):
        assert API_CONFIG["open_finance"].provision_type == "oauth2_region"
        assert API_CONFIG["open_finance"].region is not None

    def test_no_duplicate_canonical_ids(self):
        """Each catalog entry's canonical id must map to exactly one ApiSetup."""
        from app._vima_catalog import iter_ordered
        canonical_ids = [e.id for e in iter_ordered()]
        assert len(canonical_ids) == len(set(canonical_ids)), "Duplicate canonical ids in catalog"


# ---------------------------------------------------------------------------
# Playbook files: every .json on disk loads cleanly
# ---------------------------------------------------------------------------

class TestPlaybookFiles:
    def _all_playbooks(self) -> list[Path]:
        pb_dir = TOOL_ROOT / "playbooks" / "mastercard"
        return [p for p in pb_dir.glob("*.json") if p.is_file()]

    def test_all_playbooks_load_without_error(self):
        playbooks = self._all_playbooks()
        if not playbooks:
            pytest.skip("No playbook files found — skipping")
        for pb_path in playbooks:
            load_playbook(pb_path)  # raises on any validation failure
