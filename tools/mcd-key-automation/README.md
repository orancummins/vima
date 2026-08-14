# Mastercard Developers Key Automation

Python + Playwright automation that creates Mastercard Developer projects, enrolls APIs, downloads
keys/certificates, normalises filenames and packages everything into a deterministic ZIP bundle.

Spec: see `../mcd-key-automation.md`.

## Quick start

```bash
cd tools/mcd-key-automation
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
playwright install chromium

# Run against the sandbox config; opens browser headful and waits for you to log in.
mcd-key-automation run --config configs/sandbox.yaml
```

## Phase 1 status

This is the initial scaffold. Implemented:

- repository layout
- config loader + pydantic models
- CLI (`typer`)
- browser session manager (Playwright, headful)
- manual-login orchestration: opens login URL, waits for authenticated state
- alias engine
- placeholder workflows and provider hooks

Next phase will be to drive a real authenticated session and learn the portal DOM (selectors live
in `providers/mastercard/selectors.py`).

## Layout

See `../mcd-key-automation.md` § 6.
