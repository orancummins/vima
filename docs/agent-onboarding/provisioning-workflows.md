# Provisioning Workflows

This document defines deterministic behavior for each supported `provision_type`.

## Workflow Matrix

| provision_type | Auth | Key steps | Expected artifacts |
|---|---|---|---|
| oauth1_standard | OAuth 1.0a | Step1 -> Step2 creds -> download zip | credentials.json + signing zip |
| oauth1_skip_step3 | OAuth 1.0a | Step1 -> Step2 -> Skip step3 -> sandbox add signing key | credentials.json + signing zip (+ optional enc pem) |
| oauth1_enc_key | OAuth 1.0a + client encryption | Step1 -> Step2 -> download enc pem -> sandbox add signing key | encryption pem + credentials.json + signing zip |
| oauth2_region | OAuth 2.0 | Step1 with region -> open project -> sandbox OAuth2 creds + sig key | credentials.json + signature key pem |
| priceless | OAuth 1.0a | Step1 with api selection -> Step2 creds -> download zip | credentials.json + signing zip (may be pending approval) |

## Prerequisites

- Browser automation environment is functional.
- User can complete manual login/MFA.
- API is present in API_CONFIG mapping.

## Step-by-Step Rules Per Type

### oauth1_standard

1. Fill project name.
2. Proceed and fill key alias/password.
3. Create project and download signing key zip.
4. Capture consumer key from sandbox.

### oauth1_skip_step3

1. Follow oauth1_standard through step2.
2. On step3 additional credentials, click skip.
3. Use sandbox add-key flow for signing key.
4. Capture consumer key.

### oauth1_enc_key

1. Follow oauth1_standard through step2.
2. Download encryption key pem from wizard.
3. Navigate to sandbox and add OAuth signing key.
4. Capture consumer key.

### oauth2_region

1. Fill project name and mandatory region.
2. Create/open project.
3. Extract partner credentials and app key.
4. Download or create signature verification key.

### priceless

1. Select required sub-api card (Priceless Specials).
2. Complete step2 alias/password.
3. Download signing key and capture consumer key.
4. Mark as pending approval when applicable.

## Known Failure Modes

- Wizard lands on project page instead of download state.
- Key rows not visible immediately after creation.
- Optional step3 causes missing signing key.
- API approval lag for Priceless.

## Recovery Paths

1. Retry with bounded polling + page reload for delayed key rows.
2. Fall back to sandbox add-key flow when wizard path deviates.
3. Preserve artifacts and continue remaining APIs on per-API failures.
4. Surface explicit warning when API owner approval is required.
