import unittest
from unittest.mock import patch, Mock
import logging

from logging_wrapper.decorators import cyberlog

class FlaskCyberLogTests(unittest.TestCase):
    def setUp(self):
        self.mock_flask_request = Mock(url="http://example.com",
                                       method="GET",
                                       environ={"SERVER_PROTOCOL": "HTTP/1.1", "wsgi.url_scheme": "http"},
                                       headers={"User-Agent": "test-agent"},
                                       data=b"mock data")

    @patch("logging_wrapper.decorators.cyberlog.flask_request", new_callable=lambda: self.mock_flask_request)
    def test_flask_request_url(self):
        @cyberlog("Test URL enrichment", enrich_http_context=True)
        def mock_endpoint():
            pass

        mock_endpoint()

        # Assuming you're logging to a dictionary named `logged_data`
        self.assertIn("protocol.url", logged_data)
        self.assertEqual(logged_data["protocol.url"], "http://example.com")

    @patch("logging_wrapper.decorators.cyberlog.flask_request", new_callable=lambda: self.mock_flask_request)
    def test_flask_request_headers(self):
        @cyberlog("Test headers enrichment", enrich_http_context=True)
        def mock_endpoint():
            pass

        mock_endpoint()

        self.assertIn("protocol.headers", logged_data)
        self.assertIn("User-Agent", logged_data["protocol.headers"])
        self.assertEqual(logged_data["protocol.headers"]["User-Agent"], "test-agent")

    # Add more tests as needed

if __name__ == "__main__":
    unittest.main()
