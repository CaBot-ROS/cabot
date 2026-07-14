from __future__ import annotations

import json
import os
from pathlib import Path

BOOTSTRAP_FILE = "bootstrap.json"


def project_root() -> Path:
    """Return the repository root for this project."""
    override = os.environ.get("RUNTIME_BOOTSTRAP_ROOT")
    if override:
        return Path(override).resolve()
    return Path(__file__).resolve().parents[2]


def bootstrap_path() -> Path:
    """Return the repository-local bootstrap record path."""
    return project_root() / "artifacts" / BOOTSTRAP_FILE


def bootstrap_present() -> bool:
    """Return whether the bootstrap record exists."""
    return bootstrap_path().is_file()


def load_bootstrap_record() -> dict[str, object] | None:
    """Load the bootstrap record if the helper was executed."""
    path = bootstrap_path()
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))
