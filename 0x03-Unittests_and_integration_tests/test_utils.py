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


    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ test error """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(path[-1]))


if __name__ == '__main__':
    unittest.main()
