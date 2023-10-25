import functools
from datetime import datetime
import logging


# Importing the semantic conventions for common
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


def applog(message="", additional_context=None):
    """
    A decorator to automate application logging.
    
    :param message: A default message to be logged.
    :param additional_context: Additional context to be logged in the form of a dictionary.
    """
    if additional_context is None:
        additional_context = {}

    def decorator_applog(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            
            result = func(*args, **kwargs)

            end_time = datetime.now()

            # Generating the log
            log_data = {
               
            }

            log_data.update(additional_context)
            logging.info( message, extra=log_data)

            # Here you'd typically send the `log_data` to your logging system. 
            # As a placeholder, we're just printing it.
            
            return result
        return wrapper
    return decorator_applog
