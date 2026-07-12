#!/usr/bin/env python3
"""Run all standard-library unittest suites."""
import sys
import unittest
from pathlib import Path

root = Path(__file__).resolve().parents[1]
suite = unittest.TestSuite()
loader = unittest.TestLoader()
for relative in ("tests", "tools/tests"):
    suite.addTests(loader.discover(str(root / relative), pattern="test_*.py"))
result = unittest.TextTestRunner(verbosity=2).run(suite)
sys.exit(0 if result.wasSuccessful() else 1)
