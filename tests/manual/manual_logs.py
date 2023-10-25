import logging
import pytest
from unittest.mock import patch
from logging_wrapper.decorators import applog, cyberlog
from datetime import datetime
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
provider = TracerProvider()
processor = SimpleSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)

tracer = trace.get_tracer("logging-example")

#logging.basicConfig(level=logging.INFO)
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry._logs import get_logger_provider, set_logger_provider
from opentelemetry.sdk._logs.export import ConsoleLogExporter, BatchLogRecordProcessor
log_provider = LoggerProvider(resource=Resource({"service.name": "test"})) 
exporter = ConsoleLogExporter()
log_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
set_logger_provider(log_provider)
handler = LoggingHandler(level=logging.INFO, logger_provider=log_provider)
from opentelemetry.instrumentation.logging import LoggingInstrumentor
LoggingInstrumentor().uninstrument()
LoggingInstrumentor().instrument(set_logging_format=True, set_logging_context=True, log_level=logging.INFO)
logging.getLogger().addHandler(handler)


@applog(message="Test Message", additional_context={"applogsKey": "applogsValue"})
#@cyberlog(message="Test Message", additional_context={"applogsKey": "applogsValue"})
def example_function(): 
    with tracer.start_as_current_span("span-name") as span:   
        logging.getLogger().info("Testing logs using opentelemetry", extra={"key": "value", "span": "tester"})
        pass

example_function()
log_provider.force_flush()
log_provider.shutdown()
