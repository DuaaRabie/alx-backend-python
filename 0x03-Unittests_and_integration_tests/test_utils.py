#!/usr/bin/env python3
""" 0. Parameterize a unit test, 1. Parameterize a unit test"""


import unittest
from unittest.mock import patch
from parameterized import parameterized, param
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ test access_nested_map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ method to test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


    """ @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'")
    ])
    def test_access_nested_map_exception(nested_map, path, expected_message):
        test error
        with pytest.raises(KeyError, match=expected_message):
            access_nested_map(nested_map, path)
"""

if __name__ == '__main__':
    unittest.main()
