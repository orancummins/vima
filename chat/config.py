import os

# ─── Claude Model ──────────────────────────────────────────────────────────────
# See https://docs.anthropic.com/en/docs/about-claude/models for model names.
MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-4-6")

# ─── Selectable models (shown in the /simple UI dropdown) ─────────────────────
# Pricing is per 1 million tokens. Cache-read input is billed at ~10% of input.
# Update these as Anthropic publishes new models/prices.
MODELS = [
    {
        "id": "claude-haiku-4-5",
        "name": "Haiku 4.5",
        "tier": "Fast & cheap",
        "input_per_mtok": 1,
        "output_per_mtok": 5,
        "blurb": "Fastest, best for simple targeted edits.",
    },
    {
        "id": "claude-sonnet-4-6",
        "name": "Sonnet 4.6",
        "tier": "Balanced (default)",
        "input_per_mtok": 3,
        "output_per_mtok": 15,
        "blurb": "Best price/quality for everyday coding tasks.",
    },
    {
        "id": "claude-opus-4-7",
        "name": "Opus 4.7",
        "tier": "Highest quality",
        "input_per_mtok": 5,
        "output_per_mtok": 25,
        "blurb": "Most capable; best for complex multi-file reasoning and agentic coding.",
    },
]
DEFAULT_MODEL_ID = "claude-sonnet-4-6"

# ─── File Limits ───────────────────────────────────────────────────────────────
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
