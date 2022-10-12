#!/usr/bin/env python3
""" Tests for utils.py """
from parameterized import parameterized
import requests
import unittest
from utils import access_nested_map, get_json
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """ This class will test all the function
        access_nested_map in utils.py
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"),  2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ Test for correct functioning 
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ 
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJason(unittest.TestCase):
    """ This class tests the url fetching methods
        using mock patch methods to patch the requst
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """use mock to test the http call and Json return
        """
        with patch('requests.get') as mock_request:
            mock_request().json.return_value = test_payload
            mock_request.assert_called_once()
            result = get_json(test_url)
            self.assertEqual(result, test_payload)



if __name__ == '__main__':
    unittest.main()
