# This file contains semantic conventions for the cyber log.

# Event Name - This would usually be a string, e.g., "UserLogin"
event_name = "event.name"

# Event Action - Possible values might include "CREATE", "DELETE", "UPDATE", etc.
event_action = "event.action"

# Event Outcome - E.g., "SUCCESS", "FAILURE"
event_outcome = "event.outcome"

# Event Severity - E.g., "LOW", "MEDIUM", "HIGH"
event_severity = "event.severity"

# Descriptive reason for outcome, e.g., "Invalid Password"
event_reason = "event.reason"

# Any other specific details, possibly JSON or string
event_details = "event.details"

# Duration of the event in milliseconds
event_duration_ms = "event.duration.ms"

# Indicates if some logged data was truncated or overflowed
event_overflow = "event.overflow"
