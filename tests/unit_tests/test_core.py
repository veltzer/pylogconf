"""Behavioural tests for pylogconf's pure helpers."""

import logging
import os
import sys
import unittest
from typing import override
from unittest import mock

from pylogconf import core


def _drills_to_root_cause(token: str) -> bool:
    """Install the excepthook with PYLOGCONF_DRILL=token; True if it logs the root cause.

    The environment token is parsed as a boolean by setup_exceptions, so this
    exercises that parsing through the public API.
    """
    with mock.patch.dict(os.environ, {"PYLOGCONF_DRILL": token}):
        core.setup_exceptions()
    try:
        try:
            raise ValueError("root cause")
        except ValueError as root:
            raise RuntimeError("outer failure") from root
    except RuntimeError as outer:
        with unittest.TestCase().assertLogs("pylogconf.core", level="ERROR") as captured:
            sys.excepthook(type(outer), outer, None)
    return "root cause" in captured.output[0]


class Str2BoolTests(unittest.TestCase):
    @override
    def setUp(self) -> None:
        self._saved_hook = sys.excepthook

    @override
    def tearDown(self) -> None:
        # restore the defaults: drill on, traceback printing off
        with mock.patch.dict(os.environ, {"PYLOGCONF_DRILL": "1", "PYLOGCONF_PRINT_TRACEBACK": "0"}):
            core.setup_exceptions()
        sys.excepthook = self._saved_hook

    def test_recognised_true_tokens(self) -> None:
        for token in ("True", "T", "true", "t", "yes", "y", "1"):
            assert _drills_to_root_cause(token), token

    def test_false_tokens(self) -> None:
        for token in ("False", "F", "false", "no", "0", "", "maybe"):
            assert not _drills_to_root_cause(token), token

    def test_is_case_sensitive(self) -> None:
        # only the exact tokens count; "YES" is not in the accepted set
        assert not _drills_to_root_cause("YES")


class RemoveAllRootHandlersTests(unittest.TestCase):
    @override
    def setUp(self) -> None:
        self._root = logging.getLogger()
        self._saved = list(self._root.handlers)

    @override
    def tearDown(self) -> None:
        self._root.handlers = self._saved

    def test_removes_single_handler(self) -> None:
        self._root.handlers = []
        self._root.addHandler(logging.NullHandler())
        core.remove_all_root_handlers()
        assert self._root.handlers == []

    def test_removes_multiple_handlers(self) -> None:
        self._root.handlers = []
        for _ in range(3):
            self._root.addHandler(logging.NullHandler())
        core.remove_all_root_handlers()
        assert self._root.handlers == []

    def test_noop_when_no_handlers(self) -> None:
        self._root.handlers = []
        core.remove_all_root_handlers()
        assert self._root.handlers == []


if __name__ == "__main__":
    unittest.main()
