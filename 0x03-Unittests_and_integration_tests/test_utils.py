#!/usr/bin/env python3
""" Unittests and Integration Tests"""


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, param
from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """ test get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ Create a mock response object with a .json() method """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get', return_value=mock_response) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """3. Parameterize and patch"""
    def test_memoize(self):
        """ Define a test class with a method to be memoized """
        class TestClass:
            """ Define a test class with a method to be memoized """
            def a_method(self):
                """ a_method """
                return 42

            @memoize
            def a_property(self):
                """ memoize """
                return self.a_method()

        test_instance = TestClass()

        with patch.object(test_instance, 'a_method', return_value=42) \
                as mock_method:
            result1 = test_instance.a_property
            result2 = test_instance.a_property
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
