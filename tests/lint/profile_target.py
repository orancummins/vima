"""tests/lint/profile_target.py — Scalene profiling target.

Exercises Flask app initialisation and core request handling via the
built-in test client.  Does not start a network server — safe to run
standalone.

Run standalone::

    python tests/lint/profile_target.py
"""
from __future__ import annotations

import os
import sys
import warnings

warnings.filterwarnings("ignore")

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

import app as _vima  # noqa: E402 — imports and registers all routes + blueprints

with _vima.app.test_client() as _client:
    _client.get("/app")
    _client.get("/explorer/apis")
    _client.get("/explorer/usecases")
