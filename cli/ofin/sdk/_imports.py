"""Resolve the underlying Open Finance client classes.

Single source of truth, two delivery modes:

* **Development / in-repo** — import the battle-tested clients straight from
  the Flask app's ``apis.open_finance*`` packages. No duplication.
* **Bundled zipapp** — ``cli/build.py`` copies those same ``client.py`` files
  into ``ofin/sdk/_vendor/`` (rewriting their relative imports) so the
  artifact is fully self-contained. When the ``apis`` package is not on the
  path, we transparently fall back to the vendored copies.

Either way the rest of the SDK imports the three client classes from here and
never has to care which mode it is running in.
"""
from __future__ import annotations

import os
import sys


def _ensure_repo_on_path() -> None:
    """Best-effort: add the repo root to ``sys.path`` in dev mode.

    The repo root is the directory two levels above this file
    (``cli/ofin/sdk/_imports.py`` -> repo root). Adding it lets ``import apis``
    work even when the CLI is launched from an arbitrary working directory.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(here, "..", "..", ".."))
    apis_dir = os.path.join(repo_root, "apis")
    if os.path.isdir(apis_dir) and repo_root not in sys.path:
        sys.path.insert(0, repo_root)


def _load_clients():
    """Return ``(USClientCls, AUClientCls, EUClientCls)``.

    Tries the in-repo ``apis`` packages first, then the vendored copies.
    """
    # 1) In-repo clients (dev mode / running from the workspace).
    try:
        _ensure_repo_on_path()
        from apis.open_finance.client import OpenFinanceClient as _US  # type: ignore
        from apis.open_finance_au.client import OpenFinanceAUClient as _AU  # type: ignore
        from apis.open_finance_eu.client import OpenFinanceEUClient as _EU  # type: ignore
        return _US, _AU, _EU
    except Exception:  # noqa: BLE001 — fall through to vendored copies.
        pass

    # 2) Vendored clients (bundled .pyz). Created by cli/build.py.
    try:
        from ._vendor.open_finance_au_client import OpenFinanceAUClient as _AU  # type: ignore
        from ._vendor.open_finance_client import OpenFinanceClient as _US  # type: ignore
        from ._vendor.open_finance_eu_client import OpenFinanceEUClient as _EU  # type: ignore
        return _US, _AU, _EU
    except Exception as exc:  # noqa: BLE001
        raise ImportError(
            "Could not import the Open Finance client classes. In development "
            "run from the repo so 'apis' is importable; in a bundle, rebuild "
            "with cli/build.py so the vendored clients are present.\n"
            f"Underlying error: {exc}"
        ) from exc


USClientCls: type
AUClientCls: type
EUClientCls: type
USClientCls, AUClientCls, EUClientCls = _load_clients()

__all__ = ["USClientCls", "AUClientCls", "EUClientCls"]
