#!/usr/bin/env bash
set -u

echo "[1/3] Checking bootstrap record..."
if ! python3 scripts/check_bootstrap.py --quiet; then
  echo "No bootstrap record detected yet; continuing with build and tests." >&2
fi

echo "[2/3] Compiling Python sources..."
python3 -m compileall -q src

echo "[3/3] Running tests..."
python3 -m unittest discover -s tests -v

echo "Build and tests completed."
