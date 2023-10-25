import functools
from datetime import datetime
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
# Importing the semantic conventions
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


def auditlog(message="", additional_context=None):
    """
    A decorator to automate logging for audit purposes.
    
    :param message: A default message to be logged.
    :param additional_context: Additional context to be logged in the form of a dictionary.
    """
    if additional_context is None:
        additional_context = {}

    def decorator_auditlog(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            
            result = func(*args, **kwargs)

            end_time = datetime.now()

            # Generating the log
            log_data = {
                Timestamp: start_time.strftime('%Y-%m-%d %H:%M:%S'),
                ObservedTimestamp: end_time.strftime('%Y-%m-%d %H:%M:%S'),
                TraceId: "trace_id_placeholder",
                SpanId: "span_id_placeholder",
                TraceFlags: "trace_flags_placeholder",
                SeverityText: "INFO",
                SeverityNumber: 20,
                Body: message,
                InstrumentationScope: "Audit"
            }

            log_data.update(additional_context)

            # Here you'd typically send the `log_data` to your logging system. 
            # As a placeholder, we're just printing it.
            print(log_data)
            logger.info(message, extra=log_data)
            return result
        return wrapper
    return decorator_auditlog
