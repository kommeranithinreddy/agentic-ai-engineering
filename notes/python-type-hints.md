# Python Type Hints

## 1. What Are Type Hints?

Type hints tell us what kind of value a variable, function parameter, or function return is expected to have.

They make code easier to understand and help tools detect possible mistakes.

Python does not enforce type hints automatically at runtime.

```python
name: str = "Agent"
age: int = 25
is_active: bool = True
```

Here:
- `str` means string.
- `int` means integer.
- `bool` means Boolean.

The values should match their declared types.

---

## 2. Type Hints for Variables

Type hints can describe the expected type of a variable.

```python
name: str = "Agentic AI"
retry_count: int = 3
temperature: float = 0.7
is_enabled: bool = True
```

They help communicate what the variable represents.

---

## 3. Type Hints for Function Parameters

Type hints can specify the expected types of function arguments.

```python
def greet(name: str):
    print(f"Hello, {name}")
```

Here, `name: str` means the function expects `name` to be a string.

Example:

```python
greet("Agent")
```

Expected output:

```text
Hello, Agent
```

---

## 4. Return Type Hints

A return type hint describes the type of value a function is expected to return.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Here:

- `a: int` means the first parameter is expected to be an integer.
- `b: int` means the second parameter is expected to be an integer.
- `-> int` means the function is expected to return an integer.

Example:

```python
result = add(10, 20)
print(result)
```

Expected output:

```text
30
```

A function that does not return a value can use `None` as its return type.

```python
def log_message(message: str) -> None:
    print(message)
```

---

## 5. Common Python Types

| Type | Description | Example |
|---|---|---|
| `str` | Text | `"Hello"` |
| `int` | Integer | `10` |
| `float` | Decimal number | `3.14` |
| `bool` | Boolean value | `True` |
| `None` | No value | `None` |
| `list` | Collection of items | `[1, 2, 3]` |
| `dict` | Key-value collection | `{"name": "Agent"}` |
| `tuple` | Ordered collection | `(1, 2, 3)` |
| `set` | Unique items | `{1, 2, 3}` |

---

## 6. Type Hints for Lists

Use `list` to describe a list.

To specify the type of items inside the list, use:

```python
list[int]
```

Example:

```python
def calculate_total(numbers: list[int]) -> int:
    return sum(numbers)
```

This indicates:

- `numbers` is expected to be a list of integers.
- The function is expected to return an integer.

Example:

```python
total = calculate_total([10, 20, 30])
print(total)
```

Expected output:

```text
60
```

A list of strings:

```python
names: list[str] = ["Agent", "Assistant"]
```

---

## 7. Type Hints for Dictionaries

Use `dict` to describe a dictionary.

Example:

```python
user: dict[str, str] = {
    "name": "Agent",
    "role": "assistant",
}
```

This indicates:

- Dictionary keys are expected to be strings.
- Dictionary values are expected to be strings.

A dictionary with integer values:

```python
scores: dict[str, int] = {
    "Python": 90,
    "API": 85,
}
```

---

## 8. Optional Values

Sometimes a variable may contain a value or `None`.

Use `str | None` to indicate that a value can be either a string or `None`.

```python
def get_username() -> str | None:
    return None
```

This means the function may return:

- A string.
- `None`.

Example:

```python
username: str | None = "Agent"
```

Or:

```python
username: str | None = None
```

This is useful when a value is not always available.

---

## 9. Union Types

A union type allows a value to have more than one possible type.

Example:

```python
def process_value(value: int | str) -> str:
    return str(value)
```

The parameter `value` can be:

- An integer.
- A string.

Example:

```python
print(process_value(100))
print(process_value("Agent"))
```

Expected output:

```text
100
Agent
```

The `|` operator is used to combine types.

---

## 10. Type Hints with Literal

`Literal` restricts a value to a specific set of allowed values.

```python
from typing import Literal

Priority = Literal["low", "medium", "high"]
```

Example:

```python
def create_ticket(priority: Priority) -> None:
    print(priority)
```

Allowed:

```python
create_ticket("low")
create_ticket("medium")
create_ticket("high")
```

Not allowed according to the type hint:

```python
create_ticket("urgent")
```

A type checker can flag `"urgent"` because it is not one of the declared values.

Type hints do not automatically prevent invalid values at runtime.

---

## 11. Type Hints with Any

`Any` allows a value to have any type.

```python
from typing import Any

def process_data(data: Any) -> Any:
    return data
```

This provides flexibility, but it also reduces the benefits of type checking.

Use `Any` when the type genuinely cannot be determined.

Avoid using it everywhere.

---

## 12. Type Hints with Callable

`Callable` describes a value that can be called like a function.

```python
from collections.abc import Callable

def execute_task(task: Callable[[], str]) -> str:
    return task()
```

Here:

```python
Callable[[], str]
```

means:

- The callable takes no arguments.
- It is expected to return a string.

Example:

```python
def get_message() -> str:
    return "Task completed"

result = execute_task(get_message)
print(result)
```

Expected output:

```text
Task completed
```

---

## 13. Type Hints with Async Functions

Async functions can also use type hints.

```python
async def fetch_data() -> str:
    return "Data received"
```

The return type is `str`.

The function itself returns a coroutine when called. The type hint describes the value produced when that coroutine is awaited.

Example:

```python
import asyncio

async def fetch_data() -> str:
    return "Data received"

async def main() -> None:
    result = await fetch_data()
    print(result)

asyncio.run(main())
```

Expected output:

```text
Data received
```

---

## 14. Type Hints and Pydantic

Type hints describe the expected types in Python code.

Pydantic uses type annotations to validate data at runtime.

Example:

```python
from pydantic import BaseModel

class Ticket(BaseModel):
    title: str
    priority: int
```

Here:

- `title` is expected to be a string.
- `priority` is expected to be an integer.

Creating a model:

```python
ticket = Ticket(
    title="API request failed",
    priority=2,
)
```

Pydantic checks the provided data when the model is created.

**Important distinction:**

- Type hints alone do not perform runtime validation.
- Pydantic uses type annotations to perform runtime validation.

---

## 15. Type Hints in Agentic AI Engineering

Type hints help make application code easier to understand and maintain.

They are useful when building:

- API clients.
- Tool functions.
- Agent inputs and outputs.
- Configuration objects.
- Data processing functions.
- Async operations.

Example:

```python
def search_documents(query: str, limit: int) -> list[str]:
    ...
```

This communicates that:

- `query` is expected to be a string.
- `limit` is expected to be an integer.
- The function is expected to return a list of strings.

This makes function contracts easier to understand.

---

## 16. Common Mistakes

### Mistake 1: Assuming type hints validate data

```python
def process_age(age: int) -> int:
    return age
```

Python does not automatically reject a string passed to this function.

Type hints are not runtime validation.

### Mistake 2: Using the wrong return type

```python
def get_name() -> int:
    return "Agent"
```

The declared return type is `int`, but the function returns a string.

A type checker can identify this mismatch.

### Mistake 3: Using `Any` unnecessarily

```python
from typing import Any

def process(data: Any) -> Any:
    ...
```

This gives up useful type information.

Use a specific type whenever possible.

### Mistake 4: Confusing `None` with no return annotation

```python
def log_message(message: str) -> None:
    print(message)
```

`None` indicates that the function is not expected to return a meaningful value.

---

## 17. Summary

Type hints describe the expected types of variables, parameters, and return values.

Important concepts:

- `str`, `int`, `float`, and `bool` describe basic types.
- `list[int]` describes a list of integers.
- `dict[str, int]` describes a dictionary with string keys and integer values.
- `str | None` describes a string or `None`.
- `Literal` restricts values to a specific set.
- `Any` allows any type.
- `Callable` describes callable objects.
- Async functions can use return type hints.
- Pydantic uses type annotations for runtime validation.

**Remember:** Type hints improve clarity and support static checking. They do not automatically enforce types at runtime.

---

## Completion Criteria

The note is complete when the following concepts are understood:

- [ ] Variable type hints
- [ ] Function parameter hints
- [ ] Return type hints
- [ ] Lists and dictionaries
- [ ] Optional values
- [ ] Union types
- [ ] Literal types
- [ ] Any
- [ ] Callable
- [ ] Async function return types
- [ ] Difference between type hints and Pydantic validation