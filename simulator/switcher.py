"""Simulator switcher — controls whether each API uses the real sandbox or the local simulator."""
import os

RUNTIME_OVERRIDES: dict[str, bool] = {}


def is_simulated(api_slug: str) -> bool:
    slug = api_slug.lower()
    if slug in RUNTIME_OVERRIDES:
        return RUNTIME_OVERRIDES[slug]
    if os.environ.get("SIMULATED_SANDBOX", "").strip() == "1":
        return True
    return os.environ.get(f"{slug.upper()}_SIMULATED", "").strip() == "1"


def sim_base_url(api_slug: str, real_base_url: str) -> str:
    if not is_simulated(api_slug):
        return real_base_url
    port = int(os.environ.get("PORT", 9021))
    return f"http://localhost:{port}/api-sim/{api_slug}"
