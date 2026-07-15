#!/usr/bin/env bash
set -u

echo "[1/3] Checking Arduino board preparation record..."
if ! python3 scripts/check_bootstrap.py --quiet; then
  echo "No Arduino board preparation record detected; continuing with firmware validation." >&2
fi

echo "[2/3] Compiling Arduino firmware support sources..."
python3 -m compileall -q src

echo "[3/3] Running Arduino firmware build tests..."
python3 -m unittest discover -s tests -v

echo "Arduino firmware build validation completed."