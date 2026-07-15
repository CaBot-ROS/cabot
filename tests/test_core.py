from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile
import unittest
from io import StringIO
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from runtime_bootstrap.cli import check_bootstrap_main
from runtime_bootstrap.bootstrap import bootstrap_path, load_bootstrap_record
from runtime_bootstrap.core import add, banner, bootstrap_helper_name, bootstrap_status


class CoreTests(unittest.TestCase):
    def helper_root(self) -> Path:
        temp_root = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, temp_root, True)
        return temp_root

    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_banner(self) -> None:
        self.assertEqual(banner(), "runtime-bootstrap")

    def test_bootstrap_helper_name(self) -> None:
        self.assertEqual(bootstrap_helper_name(), "downloader")

    def test_bootstrap_path(self) -> None:
        self.assertEqual(bootstrap_path(), ROOT / "artifacts" / "bootstrap.json")

    def test_missing_bootstrap_status(self) -> None:
        temp_root = self.helper_root()
        with patch.dict(os.environ, {"RUNTIME_BOOTSTRAP_ROOT": str(temp_root)}):
            self.assertEqual(
                bootstrap_status(),
                "bootstrap-missing:bootstrap.json",
            )

    def test_load_bootstrap_record_missing(self) -> None:
        temp_root = self.helper_root()
        with patch.dict(os.environ, {"RUNTIME_BOOTSTRAP_ROOT": str(temp_root)}):
            self.assertIsNone(load_bootstrap_record())

    def test_load_bootstrap_record_payload(self) -> None:
        temp_root = self.helper_root()
        bootstrap_file = temp_root / "artifacts" / "bootstrap.json"
        bootstrap_file.parent.mkdir(parents=True, exist_ok=True)
        bootstrap_file.write_text(
            json.dumps({"event": "downloader_executed", "safe": True}),
            encoding="utf-8",
        )

        with patch.dict(os.environ, {"RUNTIME_BOOTSTRAP_ROOT": str(temp_root)}):
            self.assertEqual(
                load_bootstrap_record(),
                {"event": "downloader_executed", "safe": True},
            )

    def test_check_bootstrap_main_quiet_missing(self) -> None:
        temp_root = self.helper_root()
        with patch.dict(os.environ, {"RUNTIME_BOOTSTRAP_ROOT": str(temp_root)}):
            self.assertEqual(check_bootstrap_main(["--quiet"]), 1)

    def test_check_bootstrap_main_prints_payload(self) -> None:
        temp_root = self.helper_root()
        bootstrap_file = temp_root / "artifacts" / "bootstrap.json"
        bootstrap_file.parent.mkdir(parents=True, exist_ok=True)
        bootstrap_file.write_text(
            json.dumps({"event": "downloader_executed", "safe": True}),
            encoding="utf-8",
        )
        output = StringIO()

        with patch.dict(os.environ, {"RUNTIME_BOOTSTRAP_ROOT": str(temp_root)}):
            with patch("sys.stdout", output):
                self.assertEqual(check_bootstrap_main([]), 0)

        self.assertIn("Bootstrap record found", output.getvalue())


if __name__ == "__main__":
    unittest.main()
