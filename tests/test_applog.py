import logging
import pytest
from unittest.mock import patch
from logging_wrapper.decorators import applog
from datetime import datetime

# Mocking the logger
class MockLogger:
    logged_data = []

    @staticmethod
    def info(message, extra=None):
        MockLogger.logged_data.append({"level": "INFO", "message": message, "extra": extra})

    @staticmethod
    def error(message, extra=None):
        MockLogger.logged_data.append({"level": "ERROR", "message": message, "extra": extra})

# Mocking datetime to control timestamps
class MockDateTime(datetime):
    @classmethod
    def now(cls):
        return datetime(2023, 1, 1, 12, 0, 0)

@pytest.fixture
def mock_logger():
    with patch("logging_wrapper.decorators.applog.logger", MockLogger):
        yield MockLogger

@pytest.fixture
def mock_datetime():
    with patch("datetime.datetime", MockDateTime):
        yield MockDateTime

def test_applog_decorator_logs_with_context(mock_logger, mock_datetime):
    # Decorate a function with applog and additional context
    @applog(message="Test Message", additional_context={"key": "value"})
    def example_function():
        pass

    # Run the decorated function
    example_function()

    # Check that the log contains the expected data
    assert len(mock_logger.logged_data) == 1
    log_data = mock_logger.logged_data[0]

    assert log_data['level'] == "INFO"
    assert "Test Message" in log_data['message']
    assert "key: 'value'" in str(log_data['extra'])

def test_applog_decorator_logs_without_context(mock_logger, mock_datetime):
    # Decorate a function with applog without additional context
    @applog(message="Test Message")
    def example_function():
        pass

    # Run the decorated function
    example_function()

    # Check that the log contains the expected data
    assert len(mock_logger.logged_data) == 1
    log_data = mock_logger.logged_data[0]

    assert log_data['level'] == "INFO"
    assert "Test Message" in log_data['message']
    assert "key" not in str(log_data['extra'])
