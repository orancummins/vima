# Mastercard Developers Automation Platform
## Implementation Plan

Version: 1.0  
Owner: Platform Engineering  
Primary Language: Python 3.12+  
Automation Framework: Playwright  
Execution Model: Human-assisted authentication + deterministic automation

---

# 1. Objective

Build a Python-based automation platform that:

1. Launches Mastercard Developers portal
2. Waits for user authentication
3. Creates projects
4. Adds APIs to projects
5. Downloads keys/certificates
6. Normalizes aliases and filenames
7. Generates metadata manifests
8. Packages all artifacts into a deterministic ZIP bundle
9. Produces output consumable by downstream onboarding/configuration tooling

---

# 2. Primary Goals

The automation MUST:

- Be deterministic
- Be configuration-driven
- Support multiple projects
- Support multiple APIs per project
- Normalize naming conventions
- Produce reproducible outputs
- Support MFA/CAPTCHA via manual user interaction
- Be maintainable and modular
- Support future provider expansion

---

# 3. Non-Goals

The platform MUST NOT:

- Bypass MFA
- Automate CAPTCHA
- Store user passwords
- Use browser hacks to evade security
- Hardcode selectors into orchestration logic
- Depend on undocumented Mastercard APIs
- Require CI execution initially
- Implement Vault integration in MVP

---

# 4. High-Level Workflow

```text
Load Config
    ↓
Validate Config
    ↓
Launch Browser (Headful)
    ↓
Navigate to Mastercard Developers Login
    ↓
WAIT FOR USER LOGIN
    ↓
Detect Authenticated Session
    ↓
Create/Verify Projects
    ↓
Attach APIs
    ↓
Generate/Download Keys
    ↓
Normalize Files
    ↓
Generate Metadata
    ↓
Build ZIP Package
    ↓
Output Artifact
```

---

# 5. Technical Stack

## Required

| Component | Technology |
|---|---|
| Language | Python 3.12+ |
| Browser Automation | Playwright |
| Config Validation | Pydantic |
| YAML Parsing | PyYAML |
| CLI | Typer |
| Logging | Loguru |
| Packaging | zipfile |
| Crypto Validation | cryptography |

---

# 6. Repository Structure

```text
mcd-key-automation/

├── pyproject.toml
├── README.md
├── IMPLEMENTATION_PLAN.md
├── CONFIG_SCHEMA.md
├── PACKAGE_SPEC.md
├── ALIASES.md

├── configs/
│   ├── sandbox.yaml
│   └── production.yaml

├── app/
│   ├── main.py
│   ├── orchestrator.py
│   ├── models.py
│   ├── config_loader.py
│   ├── alias_engine.py
│   ├── package_builder.py
│   ├── manifest_builder.py
│   ├── validators.py
│   └── exceptions.py

├── providers/
│   ├── base.py
│   └── mastercard/
│       ├── provider.py
│       ├── selectors.py
│       ├── pages/
│       │   ├── login_page.py
│       │   ├── dashboard_page.py
│       │   ├── project_page.py
│       │   └── api_page.py
│       └── workflows/
│           ├── project_workflow.py
│           ├── api_workflow.py
│           └── download_workflow.py

├── browser/
│   ├── session.py
│   ├── downloads.py
│   ├── waits.py
│   └── screenshots.py

├── output/
├── temp/
├── logs/
└── tests/
```

---

# 7. Authentication Model

## Authentication MUST Be Manual

The automation MUST:

- launch browser in headful mode
- open Mastercard Developers login page
- pause for user interaction
- allow MFA/CAPTCHA
- resume only after authenticated state detected

The automation MUST NOT:

- inject credentials
- automate MFA
- automate CAPTCHA
- persist passwords

---

# 8. Login Workflow

## Required Flow

```text
Launch Browser
    ↓
Open Login Page
    ↓
Wait For User Authentication
    ↓
Detect Logged-In State
    ↓
Persist Session State
    ↓
Continue Automation
```

---

# 9. Browser Requirements

## Playwright Requirements

Browser MUST:

- run headful
- support downloads
- support persistent sessions
- support screenshots on failure
- support session state export

## Example Requirements

```python
playwright.chromium.launch(
    headless=False
)
```

---

# 10. Configuration Model

The system MUST be fully configuration-driven.

## Example Configuration

```yaml
environment: sandbox

organization: mastercard

projects:

  - name: BINLookup
    description: Mastercard BIN Lookup API

    apis:
      - binlookup

  - name: USOpenFinance

    apis:
      - ofin
```

---

# 11. Configuration Validation

The system MUST validate:

- required fields
- duplicate project names
- duplicate aliases
- invalid characters
- reserved words
- API uniqueness

Validation failures MUST stop execution.

---

# 12. Alias Naming Convention

## Required Alias Format

```text
<org>-<env>-<project>-<api>-<purpose>-v<version>
```

## Example

```text
mastercard-sbx-binlookup-signing-v1
```

---

# 13. File Naming Convention

## Required File Format

```text
<alias>.<extension>
```

## Examples

```text
mastercard-sbx-binlookup-signing-v1.p12
mastercard-sbx-binlookup-signing-v1.pem
```

---

# 14. Project Automation Requirements
cd tools/mcd-key-automation && .venv/bin/python tests/smoke_test.py
The automation MUST:

- detect existing projects
- create projects if missing
- avoid duplicates where possible
- support retries
- support multiple projects per execution
- Standardize passwords as 'foobar!!' for sandbox

---

# 15. API Enrollment Requirements

The automation MUST:

- add configured APIs to projects
- verify API attachment
- support retry handling
- support delayed provisioning states

---

# 16. Download Requirements

The automation MUST support downloading:

- certificates
- signing keys
- encryption keys
- .pem files
- .p12 files
- certificate chains

Downloaded files MUST:

- be normalized
- be renamed immediately
- be validated before packaging

---

# 17. Download Processing

Downloaded files MUST be:

1. moved into temp workspace and ignored by git
2. renamed according to alias rules
3. validated
4. hashed
5. registered in manifest

---

# 18. Packaging Requirements

The automation MUST produce:

```text
upload_bundle_YYYYMMDD.zip
```

---

# 19. ZIP Structure

```text
upload_bundle_20260526.zip

├── manifest.json
├── import_descriptor.json
├── certs/
│   ├── *.pem
│   ├── *.p12
│   └── *.crt
├── metadata/
│   ├── aliases.csv
│   └── hashes.json
└── logs/
    └── execution.log
```

---

# 20. Manifest Requirements

## manifest.json MUST include:

- generation timestamp
- environment
- projects
- APIs
- aliases
- filenames
- checksums
- metadata references

---

# 21. Import Descriptor Requirements

## import_descriptor.json MUST include:

- alias
- file path
- certificate type
- keystore type
- downstream import metadata

---

# 22. Logging Requirements

## Structured Logging Required

All actions MUST emit structured logs.

## Example

```json
{
  "project": "payments-core",
  "api": "mastercard-send",
  "action": "download_cert",
  "status": "success"
}
```

---

# 23. Error Handling Requirements

## Retries Required For

- navigation failures
- download failures
- stale browser states
- modal interruptions
- delayed API provisioning

## Hard Failures Required For

- invalid login
- missing downloads
- invalid cert files
- duplicate aliases
- malformed manifests

---

# 24. Screenshot Requirements

The system MUST capture screenshots on failure.

## Screenshot Locations

```text
logs/screenshots/
```

---

# 25. Selector Requirements

Selectors MUST:

- exist only in page object modules
- not exist in orchestration logic
- use stable selectors where possible

Preferred:

- data-testid
- accessible roles
- stable text labels

Avoid:

- brittle XPath
- nested CSS chains

---

# 26. Provider Abstraction

All provider-specific logic MUST be isolated.

## Required Interface

```python
class DeveloperPortalProvider:

    async def login():
        pass

    async def create_project():
        pass

    async def attach_api():
        pass

    async def download_keys():
        pass
```

---

# 27. Mastercard Provider

Mastercard-specific implementation MUST exist under:

```text
providers/mastercard/
```

---

# 28. Orchestration Requirements

The orchestrator MUST:

- load config
- coordinate workflows
- manage retries
- manage output lifecycle
- terminate cleanly on failure

---

# 29. Session Persistence

The platform SHOULD support:

- Playwright session state persistence
- optional reuse between executions

Session state MUST NOT contain passwords.

---

# 30. Temporary File Handling

Temporary files MUST:

- exist only during execution
- be deleted after packaging
- never be committed
- never persist unexpectedly

---

# 31. Security Requirements

## The platform MUST NOT:

- log secrets
- store passwords
- commit certificates
- expose private keys in logs

## The platform SHOULD:

- support future Vault integration
- support encrypted temp storage
- support secure deletion

---

# 32. CLI Requirements

## Required CLI

```bash
python main.py --config configs/sandbox.yaml
```

---

# 33. CLI Features

CLI SHOULD support:

- dry-run mode
- verbose logging
- output directory override
- environment override

---

# 34. Required Deliverables

## MVP Deliverables

- repository scaffolding
- config loader
- Playwright browser layer
- manual login orchestration
- project automation
- API enrollment
- download handling
- alias normalization
- packaging engine
- structured logs

---

# 35. Development Phases

## Phase 1

Repository scaffolding

## Phase 2

Configuration models and validation

## Phase 3

Browser/session management

## Phase 4

Manual login orchestration

## Phase 5

Project creation workflows

## Phase 6

API enrollment workflows

## Phase 7

Download handling

## Phase 8

Packaging and manifests

## Phase 9

Hardening and retries

---

# 36. Testing Requirements

## Unit Tests Required For

- alias generation
- config validation
- manifest generation
- packaging logic

## Integration Tests Required For

- browser workflows
- download handling
- ZIP generation

---

# 37. Operational Requirements

The system MUST support:

- deterministic outputs
- repeatable execution
- operational troubleshooting
- artifact traceability

---

# 38. Future Enhancements

## Future Scope

- Vault integration
- CI/CD integration
- parallel provisioning
- browserless execution
- provider expansion
- certificate expiration monitoring

---

# 39. Acceptance Criteria

The implementation is complete when:

- user can login manually
- projects are created automatically
- APIs are attached automatically
- certs/keys are downloaded automatically
- aliases are deterministic
- ZIP package is deterministic
- manifests are valid
- logs are structured
- reruns are stable

---

# 40. Final Architectural Principle

Downloaded key material MUST be treated as managed inventory.

This means:

- deterministic naming
- immutable manifests
- reproducible packaging
- traceable metadata
- operational consistency

The platform is not merely browser automation.

It is a deterministic certificate provisioning and packaging system.