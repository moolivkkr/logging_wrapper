import unittest
from unittest.mock import patch, Mock

from logging_wrapper.decorators import cyberlog

class FastAPICyberLogTests(unittest.TestCase):
    def setUp(self):
        self.mock_request = Mock(method="GET",
                                 headers={"User-Agent": "test-agent"},
                                 body=b"mock data")

    def test_fastapi_request_url(self):
        @cyberlog("Test URL enrichment", enrich_http_context=True)
        async def mock_endpoint(request):
            pass

        mock_endpoint(self.mock_request)

        self.assertIn("protocol.url", logged_data)
        # Adjust as needed for FastAPI's request object.

    def test_fastapi_request_headers(self):
        @cyberlog("Test headers enrichment", enrich_http_context=True)
        async def mock_endpoint(request):
            pass

        mock_endpoint(self.mock_request)

        self.assertIn("protocol.headers", logged_data)
        self.assertIn("User-Agent", logged_data["protocol.headers"])
        self.assertEqual(logged_data["protocol.headers"]["User-Agent"], "test-agent")

    # Add more tests as needed

if __name__ == "__main__":
    unittest.main()
