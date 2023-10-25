import unittest
from django.http import HttpRequest
import logging

from logging_wrapper.decorators import cyberlog

class DjangoCyberLogTests(unittest.TestCase):
    def setUp(self):
        self.mock_request = HttpRequest()
        self.mock_request.method = "GET"
        self.mock_request.META = {
            "SERVER_PROTOCOL": "HTTP/1.1",
            "HTTP_USER_AGENT": "test-agent"
        }
        self.mock_request._body = b"mock data"

    def test_django_request_url(self):
        @cyberlog("Test URL enrichment", enrich_http_context=True)
        def mock_view(request):
            pass

        mock_view(self.mock_request)

        self.assertIn("protocol.url", logged_data)
        # Note: You'll likely need more mocking for Django to get the full URL
        # This is just a basic test for illustrative purposes.

    def test_django_request_headers(self):
        @cyberlog("Test headers enrichment", enrich_http_context=True)
        def mock_view(request):
            pass

        mock_view(self.mock_request)

        self.assertIn("protocol.headers", logged_data)
        self.assertIn("User-Agent", logged_data["protocol.headers"])
        self.assertEqual(logged_data["protocol.headers"]["User-Agent"], "test-agent")

    # Add more tests as needed

if __name__ == "__main__":
    unittest.main()
