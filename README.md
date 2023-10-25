# Logging Wrapper

Logging Wrapper is a Python package that provides automation for logging with a focus on performance and maintainable code. It offers decorators for application logs, cyber logs, and audit logs with enhanced semantic conventions.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
   - [AppLog](#applog)
   - [CyberLog](#cyberlog)
   - [AuditLog](#auditlog)
4. [Semantic Conventions](#semantic-conventions)
5. [Testing](#testing)
6. [Contributing](#contributing)
7. [License](#license)

## Features

- **Decorators for Different Log Types:** Simplified logging for applications, cybersecurity, and audits.
- **Automated HTTP Context Enrichment:** Enhance your logs with details from HTTP requests.
- **Semantic Conventions:** Use string constants for consistent and understandable logs.
- **Support for Popular Web Frameworks:** Compatible with FastAPI, Flask, and Django.

## Installation

```bash
pip install logging-wrapper
```

## Usage

### AppLog

Use the `@applog` decorator to automatically log details related to general application actions.

```python
from logging_wrapper.decorators import applog

@applog("App started")
def start_app():
    # your app logic here
    pass
```


### Cyberlog

The `@cyberlog` decorator is perfect for logging cybersecurity-specific events. Optionally enrich the logs with HTTP request details.

from logging_wrapper.decorators import cyberlog

@cyberlog("User login attempt", enrich_http_context=True)
def user_login(username, password):
    # login logic here
    pass


```
from logging_wrapper.decorators import cyberlog

@cyberlog("User login attempt", enrich_http_context=True)
def user_login(username, password):
    # login logic here
    pass

```

### Auditlog
Ensure regulatory compliance with detailed audit logs using the `@auditlog` decorator.

```
from logging_wrapper.decorators import auditlog

@auditlog("User data retrieval")
def get_user_data(user_id):
    # retrieve user data logic here
    pass

```

