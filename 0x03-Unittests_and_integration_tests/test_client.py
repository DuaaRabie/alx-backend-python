#!/usr/bin/env python3
""" test client """


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ test that GithubOrgClient.org returns the correct value """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Set up the mock return value for get_json"""
        mock_get_json.return_value = {"login": org_name}
        """Create an instance of GithubOrgClient"""
        client = GithubOrgClient(org_name)
        """Call the org method"""
        result = client.org()
        """ Ensure that get_json was called once with the correct URL """
        url = f'https://api.github.com/orgs/{org_name}'
        mock_get_json.assert_called_once_with(url)
        """Check that the returned value matches the expected result """
        self.assertEqual(result, {"login": org_name})


if __name__ == '__main__':
    unittest.main()
