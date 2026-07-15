from __future__ import annotations

import argparse
import json

from .bootstrap import bootstrap_path, load_bootstrap_record


def check_bootstrap_main(argv: list[str] | None = None) -> int:
    """Inspect the local bootstrap record and print its contents if present."""
    parser = argparse.ArgumentParser(
        description="Inspect the local bootstrap record."
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only report success via exit status.",
    )
    args = parser.parse_args(argv)

    payload = load_bootstrap_record()
    path = bootstrap_path()
    if payload is None:
        if not args.quiet:
            print(f"No bootstrap record found at {path}.")
        return 1

    if args.quiet:
        return 0

    print(f"Bootstrap record found at {path}.")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0
