import unittest
from unittest.mock import patch, Mock
import logging

from logging_wrapper.decorators import auditlog

class AuditLogTests(unittest.TestCase):

    @patch("logging_wrapper.decorators.auditlog.logging")
    def test_auditlog_basic_logging(self, mock_logging):
        @auditlog("Basic audit log message")
        def sample_function():
            pass

        sample_function()
        mock_logging.info.assert_called_once_with("Basic audit log message", extra={})

    @patch("logging_wrapper.decorators.auditlog.logging")
    def test_auditlog_with_context(self, mock_logging):
        context = {"auditKey1": "value1", "auditKey2": "value2"}

        @auditlog("Contextual audit log message", context)
        def sample_function():
            pass

        sample_function()
        mock_logging.info.assert_called_once_with("Contextual audit log message", extra=context)

    @patch("logging_wrapper.decorators.auditlog.logging")
    def test_auditlog_update_context_inside_function(self, mock_logging):
        initial_context = {"auditKey1": "value1"}
        updated_context = {"auditKey1": "value1", "auditKey2": "updatedValue"}

        @auditlog("Updating context inside audit function", initial_context)
        def sample_function():
            initial_context["auditKey2"] = "updatedValue"

        sample_function()
        mock_logging.info.assert_called_once_with("Updating context inside audit function", extra=updated_context)

    # Add more tests as required to cover edge cases or specific audit-related scenarios.

if __name__ == "__main__":
    unittest.main()
