# Python Mocking

## 1. What is mocking?

Mocking is a testing technique that replaces a dependency with a
controlled substitute.

A dependency is something a function relies on, such as: - an API
client - a database function - another service

Mocking lets us test our own code without calling the real dependency.

## 2. Dependency injection

Dependency injection means passing a dependency into a function instead
of hardcoding it inside the function.

``` python
def get_ticket_priority(ticket_id):
    return "High"


def process_ticket(ticket_id, priority_function):
    priority = priority_function(ticket_id)
    return priority


result = process_ticket(101, get_ticket_priority)
print(result)
```

`process_ticket()` receives the function it should use. This makes it
possible to pass either the real function or a substitute during a test.

Pass the function name without parentheses:

``` python
process_ticket(101, get_ticket_priority)
```

Using `get_ticket_priority()` would call the function immediately and
pass its result instead.

## 3. Using `Mock`

Python provides `Mock` in the standard library:

``` python
from unittest.mock import Mock

mock_function = Mock()
```

No separate package installation is required.

### Set a return value

``` python
mock_function.return_value = "Low"
```

When the mock is called, it returns `"Low"`.

``` python
def process_ticket(ticket_id, priority_function):
    priority = priority_function(ticket_id)
    return priority


result = process_ticket(101, mock_function)
assert result == "Low"
```

This lets us control the dependency's response.

## 4. Verify how a mock was called

Mocks can record calls. For example:

``` python
mock_function.assert_called_once_with(101)
```

This checks that: - the mock was called - it was called exactly once -
it was called with argument `101`

A call assertion verifies the interaction with the dependency. It does
not prove that the real API or database works.

## 5. Simulate an exception with `side_effect`

Use `side_effect` to make a mock raise an exception:

``` python
from unittest.mock import Mock

mock_function = Mock()
mock_function.side_effect = RuntimeError("API unavailable")
```

Calling the mock raises the configured exception.

Example:

``` python
def process_ticket(ticket_id, priority_function):
    priority = priority_function(ticket_id)
    return priority


try:
    process_ticket(101, mock_function)
except RuntimeError as error:
    print(error)

mock_function.assert_called_once_with(101)
```

Output:

``` text
API unavailable
```

The exception propagates unless the calling code catches it. The mock
call assertion can still verify that the dependency was called.

## 6. `return_value` vs `side_effect`

  Setting          Purpose
  ---------------- ------------------------------------------------------
  `return_value`   Controls the value returned by the mock
  `side_effect`    Can raise an exception or provide behavior for calls

When `side_effect` is configured to raise an exception, that exception
is raised when the mock is called.

## 7. When mocking is useful

Mock a dependency when: - it calls an external API - it accesses a
database - it is slow, unreliable, or costly - you need to test error
handling - you need a predictable response for a test

Avoid mocking simple deterministic code when the real function is easy
and safe to call.

## 8. Important limitation

Mocking tests how your code behaves with a controlled dependency.

It does **not** verify that the real API, database, or external service
is working. That requires an integration test.

## Summary

-   Mocking replaces a dependency with controlled behavior.
-   Dependency injection makes a dependency replaceable.
-   `Mock()` creates a mock object.
-   `return_value` controls the returned result.
-   `side_effect` can make a mock raise an exception.
-   `assert_called_once_with()` checks that the mock was called exactly
    once with expected arguments.
-   Mocking helps test application behavior, but does not replace
    integration testing.
