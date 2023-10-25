# This file contains semantic conventions that are common across different types of logs.

# Timestamp when the event was created
Timestamp = "timestamp"

# Timestamp when the event was observed (can be different from when it was created)
ObservedTimestamp = "observed_timestamp"

# Request Trace ID
TraceId = "trace_id"

# Request Span ID
SpanId = "span_id"

# Trace flags to provide additional details about the trace
TraceFlags = "trace_flags"

# Text description of severity
SeverityText = "severity_text"

# Numeric representation of severity
SeverityNumber = "severity_number"

# Actual message or body of the log
Body = "body"

# Scope or source of instrumentation (e.g., "HTTPServer", "DBQuery")
InstrumentationScope = "instrumentation_scope"
