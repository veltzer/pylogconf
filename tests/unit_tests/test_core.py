"""Behavioural tests for pylogconf's pure helpers."""

import logging
import unittest

from pylogconf import core


class Str2BoolTests(unittest.TestCase):
    def test_recognised_true_tokens(self):
        for token in ("True", "T", "true", "t", "yes", "y", "1"):
            self.assertTrue(core._str2bool(token), token)  # pylint: disable=protected-access

    def test_false_tokens(self):
        for token in ("False", "F", "false", "no", "0", "", "maybe"):
            self.assertFalse(core._str2bool(token), token)  # pylint: disable=protected-access

    def test_is_case_sensitive(self):
        # only the exact tokens count; "YES" is not in the accepted set
        self.assertFalse(core._str2bool("YES"))  # pylint: disable=protected-access


class RemoveAllRootHandlersTests(unittest.TestCase):
    def setUp(self):
        self._root = logging.getLogger()
        self._saved = list(self._root.handlers)

    def tearDown(self):
        self._root.handlers = self._saved

    def test_removes_single_handler(self):
        self._root.handlers = []
        self._root.addHandler(logging.NullHandler())
        core.remove_all_root_handlers()
        self.assertEqual(self._root.handlers, [])

    def test_noop_when_no_handlers(self):
        self._root.handlers = []
        core.remove_all_root_handlers()
        self.assertEqual(self._root.handlers, [])


if __name__ == "__main__":
    unittest.main()
