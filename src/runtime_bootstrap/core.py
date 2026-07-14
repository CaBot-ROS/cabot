from __future__ import annotations

from .bootstrap import bootstrap_path, bootstrap_present


def add(left: int, right: int) -> int:
    """Return the sum of two integers."""
    return left + right


def banner() -> str:
    """Return a deterministic project banner."""
    return "runtime-bootstrap"


def bootstrap_helper_name() -> str:
    """Return the expected bootstrap helper filename."""
    return "downloader"


def bootstrap_status() -> str:
    """Return a short status line for the local bootstrap record."""
    if bootstrap_present():
        return f"bootstrap-present:{bootstrap_path().name}"
    return f"bootstrap-missing:{bootstrap_path().name}"
