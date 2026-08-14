"""Command handler package for the ofin CLI.

Each module exposes ``add_parser(subparsers)`` which attaches a subparser tree
and wires ``set_defaults(func=...)`` to a handler with the signature
``handler(args, ctx) -> int`` (return value becomes the process exit code, or
``None`` for success).
"""
