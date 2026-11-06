# Python Logging

## 1. What is Logging?

Logging records information about an application's execution.

It helps developers understand:
- What the application is doing.
- Whether operations succeeded or failed.
- What errors occurred.
- Where an error happened.

Logging is useful for debugging, monitoring, and investigating application failures.

Python provides the built-in `logging` module.

```python
import logging
```

---

## 2. Logging Levels

Logging levels indicate the severity or importance of a message.

| Level | Purpose | Example |
|---|---|---|
| DEBUG | Detailed information useful for debugging | Variable values, detailed execution information |
| INFO | Normal application events | Application started, request completed |
| WARNING | Something unexpected happened, but the application can continue | Retry initiated, unexpected condition |
| ERROR | An operation failed | API request failed |
| CRITICAL | A serious failure that may prevent the application from continuing | Application cannot continue operating |

### Example

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Application started")
logging.warning("Unexpected condition")
logging.error("Operation failed")
logging.critical("Critical failure")
```

### Important

The configured logging level determines which messages are accepted.

For example:

```python
logging.basicConfig(level=logging.INFO)
```

INFO, WARNING, ERROR, and CRITICAL messages are accepted.

DEBUG messages are filtered out.

---

## 3. Basic Logging Configuration

`logging.basicConfig()` configures the default logging system.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

### Common configuration options

| Option | Purpose |
|---|---|
| `level` | Minimum logging level |
| `format` | Defines the log message format |
| `filename` | Writes logs to a file |
| `datefmt` | Controls timestamp formatting |

### Example

```python
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log"
)
```

This configuration writes logs to `app.log`.

---

## 4. Logging Format

The format determines what information appears in each log record.

```python
format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

### Common format attributes

| Attribute | Meaning |
|---|---|
| `%(asctime)s` | Timestamp |
| `%(name)s` | Logger name |
| `%(levelname)s` | Logging level |
| `%(message)s` | Log message |
| `%(filename)s` | Source filename |
| `%(funcName)s` | Function name |
| `%(lineno)d` | Source line number |

### Example

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s"
)

logging.info("Application started")
```

---

## 5. Logging to a File

The `filename` argument writes logs to a file instead of using the default console output.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")
logging.error("Operation failed")
```

### Purpose

File logging is useful when:
- Application output needs to be retained.
- Errors need to be investigated later.
- The application runs without an interactive terminal.

---

## 6. Named Loggers

Named loggers allow different modules to identify their own log messages.

```python
import logging

logger = logging.getLogger(__name__)
```

### Why use named loggers?

In applications containing multiple modules, named loggers help identify where a message originated.

Example project:

```text
application/
├── main.py
└── ticket.py
```

In `main.py`:

```python
import logging

logger = logging.getLogger(__name__)

logger.info("Application started")
```

In `ticket.py`:

```python
import logging

logger = logging.getLogger(__name__)

logger.info("Ticket module loaded")
```

When the modules are imported and executed, their logger names identify their respective modules.

### Understanding `__name__`

`__name__` is a Python variable that identifies the current module.

When a Python file runs directly:

```python
__name__ == "__main__"
```

When imported:

```python
__name__ == "module_name"
```

This makes `logging.getLogger(__name__)` useful for module-level logging.

---

## 7. Logging Exceptions

Logging exceptions helps identify failures and provides traceback information.

### Example

```python
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

def divide(a: int, b: int) -> float:
    return a / b

try:
    result = divide(1, 0)
except Exception:
    logger.exception("An exception occurred")
```

### `logger.exception()`

`logger.exception()`:
- Logs an ERROR-level message.
- Includes exception information.
- Includes the traceback when called inside an exception handler.

Use it when an exception has been caught and its details need to be recorded.

### Difference

```python
logger.error("Operation failed")
```

Records an error message.

```python
logger.exception("Operation failed")
```

Records an error message with exception information and traceback.

---

## 8. Logging Handlers

A handler determines where log records are sent.

Common handlers:

| Handler | Destination |
|---|---|
| `StreamHandler` | Terminal or console |
| `FileHandler` | File |
| `RotatingFileHandler` | File with size-based rotation |
| `TimedRotatingFileHandler` | File with time-based rotation |

### FileHandler

```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)
```

This handler writes INFO and higher-level messages to `app.log`.

### StreamHandler

```python
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

logger.addHandler(console_handler)
```

This handler sends accepted log messages to the console.

### Important

Handlers are independent destinations.

A logger can have multiple handlers:

```python
logger.addHandler(file_handler)
logger.addHandler(console_handler)
```

The same log record can be sent to both destinations.

---

## 9. Handler Levels

Logger levels and handler levels serve different purposes.

### Logger level

Determines which records the logger allows through.

### Handler level

Determines which records a particular handler accepts.

Example:

```python
logger.setLevel(logging.DEBUG)

file_handler.setLevel(logging.INFO)
console_handler.setLevel(logging.DEBUG)
```

The logger allows DEBUG and higher.

The file handler accepts INFO and higher.

The console handler accepts DEBUG and higher.

### Reference

| Logger Level | Handler Level | Result |
|---|---|---|
| DEBUG | DEBUG | DEBUG and higher |
| DEBUG | INFO | INFO and higher |
| INFO | DEBUG | INFO and higher |
| WARNING | DEBUG | WARNING and higher |

The effective result depends on both the logger and handler configuration.

---

## 10. Logging Filters

Filters provide additional control over which records a handler accepts.

A filter can check:
- Logging level.
- Logger name.
- Message content.
- Other attributes of a log record.

### Example: DEBUG-only filter

```python
import logging

class DebugOnlyFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.DEBUG
```

Attach the filter:

```python
debug_handler.addFilter(DebugOnlyFilter())
```

### Purpose

A handler level of DEBUG accepts DEBUG and higher.

A DEBUG-only filter accepts only DEBUG.

### Important

Filters are attached to specific handlers.

A filter attached to one handler does not automatically apply to other handlers.

---

## 11. Multiple Logging Destinations

An application can send different logging levels to different files.

Example configuration:

```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

debug_handler = logging.FileHandler("debug.log")
debug_handler.setLevel(logging.DEBUG)

app_handler = logging.FileHandler("app.log")
app_handler.setLevel(logging.INFO)

logger.addHandler(debug_handler)
logger.addHandler(app_handler)
```

### Result

Without an additional filter:

| File | Messages |
|---|---|
| `debug.log` | DEBUG and higher |
| `app.log` | INFO and higher |

To make `debug.log` contain DEBUG messages only, attach the DEBUG-only filter.

```python
debug_handler.addFilter(DebugOnlyFilter())
```

### Practical application

Separate destinations can be useful when:
- Debugging requires detailed logs.
- Application logs should contain operational events.
- Error logs need to be separated from normal application activity.

---

## 12. File and Terminal Logging Together

A logger can send messages to both a file and the terminal.

```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
```

### Result

- INFO and higher are written to `app.log`.
- DEBUG and higher are sent to the terminal.

The terminal handler is optional.

Use it when terminal output is useful during development or when running an application interactively.

---

## 13. Logging Retry Attempts

Logging retry attempts helps track operations that fail temporarily.

Useful information includes:
- Attempt number.
- Failure reason.
- Whether another attempt will be made.
- Whether all attempts have failed.

### Example

```python
logger.info("Attempt number: %s", attempt)
logger.warning("Request failed. Retrying.")
logger.error("All attempts exhausted")
```

### Logging level reference

| Event | Suitable level |
|---|---|
| Attempt started | INFO |
| Temporary failure | WARNING |
| Retry initiated | WARNING |
| All attempts exhausted | ERROR |

The exact level depends on the application's behavior and whether the failure is expected or requires attention.

---

## 14. Logging Best Practices

### Use named loggers

```python
logger = logging.getLogger(__name__)
```

This identifies the module that generated the message.

### Use appropriate logging levels

Choose the level based on the event's importance.

### Avoid unnecessary repetition

Log useful information rather than repeatedly recording the same message.

### Use exception logging

```python
logger.exception("Request failed")
```

Use this inside an exception handler when traceback information is needed.

### Avoid sensitive information

Do not log:
- Passwords.
- API keys.
- Access tokens.
- Sensitive personal information.

### Use parameterized logging

Prefer:

```python
logger.info("Request completed with status %s", status_code)
```

Instead of:

```python
logger.info(f"Request completed with status {status_code}")
```

Parameterized logging allows the logging system to format the message when needed.

---

## 15. Quick Reference

| Requirement | Logging feature |
|---|---|
| Record application events | `logger.info()` |
| Record unexpected conditions | `logger.warning()` |
| Record operation failures | `logger.error()` |
| Record exception traceback | `logger.exception()` |
| Identify the current module | `logging.getLogger(__name__)` |
| Write logs to a file | `logging.FileHandler()` |
| Write logs to terminal | `logging.StreamHandler()` |
| Configure minimum log level | `setLevel()` |
| Apply additional record conditions | `logging.Filter` |
| Send logs to multiple destinations | Multiple handlers |

---

## 16. Application Logging Reference

Logging should be applied where application behavior requires visibility.

Examples:

### Application startup

```python
logger.info("Application started")
```

### Operation completed

```python
logger.info("Request completed")
```

### Unexpected condition

```python
logger.warning("Unexpected response received")
```

### Operation failed

```python
logger.error("Request failed")
```

### Exception with traceback

```python
try:
    operation()
except Exception:
    logger.exception("Operation failed")
```

The purpose of logging is to make application behavior understandable when running, debugging, or investigating failures.