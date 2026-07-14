#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from runtime_bootstrap.bootstrap import bootstrap_path, load_bootstrap_record


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Inspect the local bootstrap record."
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only report success via exit status.",
    )
    args = parser.parse_args()

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


if __name__ == "__main__":
    raise SystemExit(main())
