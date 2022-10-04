#!/usr/bin/env python3
""" Tests for utils.py """
from typing import Sequence
from parameterized import parameterized
import unittest
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """ Test
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), ({"b": 2}, 2))
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expect: Any):
        """ Test for correct functioning"""
        self.assertEqual(access_nested_map(nested_map, path), expect)

if __name__ == '__main__':
    unittest.main()
