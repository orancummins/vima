# Agent API Onboarding

Purpose: deterministic instructions for autonomously wiring a new Mastercard Developers API into Solution Studio.

## Execution Order

1. Read this file.
2. Validate [api-onboarding-spec.yaml](api-onboarding-spec.yaml) against [api-onboarding-spec.schema.json](api-onboarding-spec.schema.json).
3. Follow [new-api-playbook.md](new-api-playbook.md).
4. Use [provisioning-workflows.md](provisioning-workflows.md) for key setup automation behavior.
5. Enforce UI behavior with [ui-integration-contract.md](ui-integration-contract.md).
6. Execute [testing-matrix.md](testing-matrix.md).
7. Resolve failures using [troubleshooting.md](troubleshooting.md).

## Inputs Required

- Repository checkout with dependencies installed.
- Access to Mastercard Developers account for manual login + MFA.
- API metadata entry in [api-onboarding-spec.yaml](api-onboarding-spec.yaml).

## Outputs Produced

- Implemented API module and wiring.
- Provisioning mapping for key automation.
- Updated UI visibility and docs/how-to content.
- Passing contract validation and smoke checks.

## Happy Path (Agent Sequence)

1. Parse onboarding spec row for target API.
2. Confirm catalog parity using `./.venv/bin/python tools/validate_api_contract.py`.
3. Implement code changes per playbook.
4. Provision keys (or reuse-existing mode), import config, and confirm configured status.
5. Run testing matrix checks and record results.

## Failure Path (Agent Sequence)

1. Stop at first failed contract check.
2. Capture artifact: log line, screenshot, and failing command.
3. Apply troubleshooting recipe.
4. Retry up to configured threshold.
5. Escalate when failure remains unresolved.

## Definition of Done

- Contract validator passes.
- API appears in catalog/manifests/provision UI.
- Docs and how-to are present.
- Required tests in the matrix pass.

## Escalation Rules

Escalate if any of these are true:

- Portal workflow changed and selectors cannot recover.
- Provisioning artifacts are missing after retries.
- Auth mode requirements are unclear in Mastercard docs.
