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

    def test_public_repos_url(self):
        """ test_public_repos_url """
        org_name = "google"
        expected_repos_url = "https://api.github.com/orgs/google/repos"
        # Mock payload for the org method
        payload = {
            "repos_url": expected_repos_url
        }

        # Use patch as a context manager to mock the org property
        with patch.object(GithubOrgClient, 'org', return_value=payload):
            client = GithubOrgClient(org_name)
            # Access the _public_repos_url property
            repos_url = client._public_repos_url
            # Test that the result is as expected
            self.assertEqual(repos_url, expected_repos_url)

    def test_public_repos(self, mock_get_json):
        """ test_public_repos """
        org_name = "google"
        expected_repos = ["repo1", "repo2", "repo3"]

        # Mock payload for the get_json return value
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        # Use patch as a context manager to mock _public_repos_url
        re = "https://api.github.com/orgs/google/repos"
        repo = '_public_repos_url'
        with patch.object(GithubOrgClient, repo, return_value=re):
            client = GithubOrgClient(org_name)
            repos = client.public_repos()  # Call the public_repos method

            # Test that the repos list is what we expect
            self.assertEqual(repos, expected_repos)

            # Ensure that the mocked get_json was called once
            test_api = "https://api.github.com/orgs/google/repos"
            mock_get_json.assert_called_once_with(test_api)


if __name__ == '__main__':
    unittest.main()
