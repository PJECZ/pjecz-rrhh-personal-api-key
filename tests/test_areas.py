"""
Unit tests for areas category
"""
import os
import unittest

import requests
from dotenv import load_dotenv

load_dotenv()


class TestAreas(unittest.TestCase):
    """Tests for areas category"""

    def setUp(self) -> None:
        """Initialize the test case"""
        # Load environment variables
        self.api_key = os.getenv("API_KEY", "")
        self.host = os.getenv("HOST", "")
        self.timeout = int(os.getenv("TIMEOUT", "20"))
        # If any of the environment variables is empty, raise an error
        if not self.api_key:
            raise ValueError("API_KEY environment variable is empty")
        if not self.host:
            raise ValueError("HOST environment variable is empty")
        if not self.timeout:
            raise ValueError("TIMEOUT environment variable is empty")
        # Return super
        return super().setUp()

    def test_get_centros_trabajos(self):
        """Test GET method for centros_trabajos"""
        response = requests.get(f"{self.host}/v3/centros_trabajos", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)

    def test_get_areas(self):
        """Test GET method for areas"""
        response = requests.get(f"{self.host}/v3/areas", headers={"X-Api-Key": self.api_key}, timeout=self.timeout)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
