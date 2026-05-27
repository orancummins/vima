#!/usr/bin/env python3
"""Validate API onboarding contract parity across core wiring surfaces.

Checks:
1. Catalog IDs match API manifest IDs.
2. Provision catalog payload has required keys for each API.
3. Provisioning API_CONFIG covers every catalog API (canonical or legacy key).
4. API_CONFIG provision_type values are supported by workflow dispatch.
"""

from __future__ import annotations

import importlib
import importlib.util
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL_ROOT = ROOT / "tools" / "mcd-key-automation"


def _load_root_app_module():
    app_path = ROOT / "app.py"
    spec = importlib.util.spec_from_file_location("vima_root_app", app_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load app module from {app_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _supported_provision_types(workflow_file: Path) -> set[str]:
    text = workflow_file.read_text(encoding="utf-8")
    return set(re.findall(r'if\s+ptype\s*==\s*"([a-z0-9_]+)"', text))


def main() -> int:
    errors: list[str] = []

    # Validate docs/agent-onboarding spec against its JSON schema.
    schema_path = ROOT / "docs" / "agent-onboarding" / "api-onboarding-spec.schema.json"
    spec_path = ROOT / "docs" / "agent-onboarding" / "api-onboarding-spec.yaml"
    if not schema_path.is_file():
        errors.append(f"Missing schema file: {schema_path}")
    if not spec_path.is_file():
        errors.append(f"Missing spec file: {spec_path}")

    if schema_path.is_file() and spec_path.is_file():
        try:
            import yaml  # type: ignore
            import jsonschema  # type: ignore
        except Exception as exc:
            errors.append(
                "Spec/schema validation dependencies missing. Install PyYAML and jsonschema. "
                f"Import error: {exc}"
            )
        else:
            try:
                schema = json.loads(schema_path.read_text(encoding="utf-8"))
                spec_doc = yaml.safe_load(spec_path.read_text(encoding="utf-8"))
                jsonschema.validate(instance=spec_doc, schema=schema)
            except Exception as exc:
                errors.append(f"Onboarding spec failed schema validation: {exc}")

    # Load core catalog + registry from repository root.
    sys.path.insert(0, str(ROOT))
    from apis.catalog import iter_ordered
    from apis import registry as api_registry

    catalog_entries = list(iter_ordered())
    catalog_ids = {e.id for e in catalog_entries}
    legacy_to_id = {e.legacy_id: e.id for e in catalog_entries if e.legacy_id}

    manifests = api_registry.manifests()
    manifest_ids = {m.get("id") for m in manifests if m.get("id")}

    missing_in_manifests = sorted(catalog_ids - manifest_ids)
    extra_in_manifests = sorted(manifest_ids - catalog_ids)
    if missing_in_manifests:
        errors.append(f"Missing APIs in manifests: {missing_in_manifests}")
    if extra_in_manifests:
        errors.append(f"Unexpected APIs in manifests: {extra_in_manifests}")

    for m in manifests:
        if not m.get("docs_url"):
            errors.append(f"API {m.get('id')} has empty docs_url")

    # Validate provision catalog shape from backend helper.
    root_app = _load_root_app_module()
    if not hasattr(root_app, "_build_provision_catalog"):
        errors.append("app.py missing _build_provision_catalog helper")
        provision_rows = []
    else:
        provision_rows = root_app._build_provision_catalog()

    required_keys = {
        "id",
        "legacy_id",
        "name",
        "configured",
        "docs_url",
        "requires_owner_approval",
        "provision_note",
    }
    provision_ids = set()
    for row in provision_rows:
        row_keys = set(row.keys())
        missing_keys = sorted(required_keys - row_keys)
        if missing_keys:
            errors.append(f"Provision catalog row missing keys {missing_keys}: {row}")
        row_id = row.get("id")
        if row_id:
            provision_ids.add(row_id)

    if provision_ids and provision_ids != catalog_ids:
        errors.append(
            f"Provision catalog IDs mismatch. expected={sorted(catalog_ids)} actual={sorted(provision_ids)}"
        )

    # Validate mcd key-automation mapping against catalog.
    sys.path.insert(0, str(TOOL_ROOT))
    api_config_mod = importlib.import_module("providers.mastercard.api_config")
    workflow_file = TOOL_ROOT / "providers" / "mastercard" / "workflows" / "project_workflow.py"

    api_config = getattr(api_config_mod, "API_CONFIG", {})
    supported_types = _supported_provision_types(workflow_file)

    for api_id in sorted(catalog_ids):
        legacy_id = next((k for k, v in legacy_to_id.items() if v == api_id), None)
        has_mapping = api_id in api_config or (legacy_id in api_config if legacy_id else False)
        if not has_mapping:
            errors.append(f"API {api_id} missing in mcd API_CONFIG")

    for key, setup in api_config.items():
        ptype = getattr(setup, "provision_type", None)
        if ptype and ptype not in supported_types:
            errors.append(
                f"API_CONFIG entry {key} uses unsupported provision_type {ptype}. "
                f"Supported: {sorted(supported_types)}"
            )

    if errors:
        print("API contract validation FAILED:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("API contract validation PASSED")
    print(f"- Catalog APIs: {len(catalog_ids)}")
    print(f"- Manifest APIs: {len(manifest_ids)}")
    print(f"- Provision catalog APIs: {len(provision_rows)}")
    print(f"- Supported provision types: {sorted(supported_types)}")
    print("- Onboarding spec/schema: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
