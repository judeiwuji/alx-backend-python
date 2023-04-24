#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import (GithubOrgClient)
from typing import Dict
from fixtures import (TEST_PAYLOAD)


class TestGithubOrgClient(unittest.TestCase):
    """Test Github org client"""

    @parameterized.expand([
        "google",
        "abc"
    ])
    @patch("client.get_json")
    def test_org(self, input: str, mock_get_json: Mock):
        """Test github org client"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        client = GithubOrgClient(input)
        client.org()
        mock_get_json.assert_called_once_with(client.ORG_URL.format(org=input))

    def test_public_repos_url(self):
        """Test public repos url"""
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            payload = "google"
            mock_public_repos_url.return_value = payload
            mock = GithubOrgClient("google")
            self.assertEqual(mock._public_repos_url, payload)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: Mock):
        """Test public repos method"""
        mock_get_json.return_value = [{'name': 'google'}]

        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            payload = {'name': 'google'}
            mock_public_repos_url.return_value = payload
            mock = GithubOrgClient("google")
            data = mock.public_repos()
            self.assertEqual(list(payload.values()), data)
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"repo": {"license": {"key": "my_license"}},
         "license_key": "my_license"}, True),
        ({"repo": {"license": {"key": "other_license"}},
         "license_key": "my_license"}, False)
    ])
    def test_has_license(self, input: Dict[str, Dict[str, str]], expected: bool):
        """Test has license method"""
        self.assertEqual(GithubOrgClient.has_license(**input), expected)


def get_side_effect():
    """get side effect method"""
    return TEST_PAYLOAD[1]


@parameterized_class(("org_payload", "repos_payload",
                      "expected_repos", "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test integration GithubOrgClient"""
    @classmethod
    def setUpClass(cls) -> None:
        """setup class method"""
        cls.mock_get = Mock("requests.get")
        cls.mock_get.json = MagicMock()
        cls.mock_get.json.side_effect = get_side_effect

        cls.get_patcher = patch("requests.get", spec=True)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """tear down class method"""
        cls.get_patcher.stop()
