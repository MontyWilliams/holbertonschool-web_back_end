#!/usr/bin/env python3
""" Tests for utils.py """
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Test
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), ({"b": 2}, 2))
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ Test for correct functioning"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

if __name__ == '__main__':
    unittest.main()
