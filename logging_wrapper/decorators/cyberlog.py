import functools
from datetime import datetime
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
# Importing semantic conventions
from logging_wrapper.semconv.cyber import (
    event_name,
    event_action,
    event_outcome,
    event_severity,
    event_reason,
    event_details,
    event_duration_ms,
    event_overflow,
)

from logging_wrapper.semconv.common import (
    Timestamp,
    ObservedTimestamp,
    TraceId,
    SpanId,
    TraceFlags,
    SeverityText,
    SeverityNumber,
    Body,
    InstrumentationScope
)

def extract_http_context():
    """Detect the framework and extract HTTP context."""
    http_context = {}
    
    # Attempt Flask detection and extraction
    try:
        from flask import request
        http_context['protocol.url'] = request.url
        http_context['protocol.type'] = request.scheme
        http_context['protocol.version'] = request.environ.get('SERVER_PROTOCOL')
        http_context['protocol.headers'] = dict(request.headers)
        http_context['protocol.transport'] = request.environ.get('wsgi.url_scheme')
        http_context['protocol.request.detail'] = request.data[:2000]  # Limit to 2KB
        return http_context
    except ImportError:
        pass

    # Attempt FastAPI detection and extraction
    # For FastAPI, this is just a basic example, in a real-world situation you might need to adjust
    try:
        from starlette.requests import Request
        # The actual extraction might be a bit more complicated and might require changes based on your FastAPI setup
    except ImportError:
        pass

    # Attempt Django detection and extraction
    try:
        from django import http
        # Placeholder, as the actual extraction will depend on your Django setup
    except ImportError:
        pass

    return http_context


def cyberlog(message="", additional_context=None, enrich_http_context=False):
    """
    A decorator to automate cyber security logging.

    :param message: A default message to be logged.
    :param additional_context: Additional context to be logged in the form of a dictionary.
    :param enrich_http_context: Flag to decide if HTTP context should be enriched.
    """
    if additional_context is None:
        additional_context = {}

    def decorator_cyberlog(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            
            result = func(*args, **kwargs)

            end_time = datetime.now()

            # Generating the log
            log_data = {
                Timestamp: start_time.strftime('%Y-%m-%d %H:%M:%S'),
                ObservedTimestamp: end_time.strftime('%Y-%m-%d %H:%M:%S'),
                TraceFlags: "trace_flags_placeholder",
                event_name: "event_name_placeholder",
                event_action: "event_action_placeholder",
                event_outcome: "SUCCESS",  # This should be dynamic based on the function's outcome
                event_severity: "MEDIUM",  # This should be dynamic
                event_details: "details_placeholder",
                event_duration_ms: int((end_time - start_time).total_seconds() * 1000),  # Duration in milliseconds
                event_overflow: False,  # This needs to be set dynamically
                Body: message,
                InstrumentationScope: "CyberSecurity"
            }

            if enrich_http_context:
                http_data = extract_http_context()
                log_data.update(http_data)

            log_data.update(additional_context)
            logger.info(message, extra=log_data)
            # Placeholder for logging the data, replace with actual logging logic
            print(log_data)

            return result
        return wrapper
    return decorator_cyberlog
