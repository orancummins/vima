"""ofin — a standalone CLI + SDK for Mastercard Open Finance (US, AU, EU).

The package wraps the three Open Finance API clients behind a single SDK
facade (:class:`ofin.sdk.OfinClient`) and a thin ``argparse``-based command
line interface (``python -m ofin`` / the ``ofin`` console script / the built
``ofin.pyz`` zipapp).

It is designed to run completely independently of the Flask web app and to be
buildable into a portable, no-binary artifact via ``cli/build.py``.
"""

__version__ = "0.1.0"

__all__ = ["__version__"]
