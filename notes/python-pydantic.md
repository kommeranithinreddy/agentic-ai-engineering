# Pydantic in Python

## 1. What is Pydantic?

Pydantic is a Python library used for data validation and data parsing.

It ensures that the data received by an application follows the expected structure and data types.

For example, imagine building an AI support-ticket application.

A ticket might contain:

* Ticket ID
* Title
* Description
* Priority
* Status

We want to ensure that the priority is valid and that required fields are provided.

Pydantic helps enforce these rules.

### Why is Pydantic useful?

Pydantic is commonly used for:

* Validating API requests.
* Validating API responses.
* Defining structured data.
* Validating LLM outputs.
* Managing application configurations.
* Enforcing data types and constraints.

It is particularly useful in Agentic AI applications because LLMs can produce unpredictable outputs. Pydantic helps validate those outputs before the application processes them.

---

## 2. Installing Pydantic

Install Pydantic inside the Python virtual environment.

```powershell
pip install pydantic
```

Verify the installation:

```powershell
pip show pydantic
```

---

## 3. BaseModel

`BaseModel` is the foundation of Pydantic.

We create a model by inheriting from `BaseModel`.

Example:

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(
    name="John",
    age=25
)

print(user)
```

Output:

```text
name='John' age=25
```

### Understanding the code

* `BaseModel`: Provides Pydantic's validation functionality.
* `name: str`: Defines a string field.
* `age: int`: Defines an integer field.
* `User(...)`: Creates an instance and validates the supplied data.

If an incompatible value is supplied, Pydantic attempts to validate or convert it according to its type rules.

---

## 4. Required Fields and Default Values

Pydantic supports required fields and fields with default values.

### Required fields

A required field must be supplied when creating the model.

Example:

```python
from pydantic import BaseModel

class Ticket(BaseModel):
    title: str
    description: str
    priority: str

ticket = Ticket(
    title="Login issue",
    description="Unable to access account",
    priority="High"
)
```

All three fields are required.

If a required field is missing, Pydantic raises a `ValidationError`.

### Default values

A default value is used when a field is not supplied.

Example:

```python
from pydantic import BaseModel

class Ticket(BaseModel):
    title: str
    priority: str = "Medium"
    status: str = "Open"

ticket = Ticket(
    title="Login issue"
)

print(ticket)
```

Output:

```text
title='Login issue' priority='Medium' status='Open'
```

Here:

* `title` is required.
* `priority` defaults to `"Medium"`.
* `status` defaults to `"Open"`.

---

## 5. Literal Types

`Literal` restricts a field to a predefined set of values.

For example, a ticket priority should only accept:

* Low
* Medium
* High
* Critical

We don't want arbitrary values such as `"Urgent123"`.

Example:

```python
from typing import Literal
from pydantic import BaseModel

class Ticket(BaseModel):
    title: str
    priority: Literal["Low", "Medium", "High", "Critical"]

ticket = Ticket(
    title="Login issue",
    priority="High"
)

print(ticket)
```

Valid value:

```python
priority="High"
```

Invalid value:

```python
priority="Urgent123"
```

The invalid value raises a `ValidationError`.

### Why is Literal useful?

It prevents fields from accepting values outside the predefined options.

In Agentic AI applications, this is useful when an LLM must return structured values such as:

* Task priority.
* Ticket status.
* Action type.
* Execution mode.
* User role.

---

## 6. Field()

Pydantic provides `Field()` to configure individual model fields.

It can be used to define:

* Default values.
* Minimum and maximum lengths.
* Numeric constraints.
* Descriptions.
* Examples.
* Additional field metadata.

Example:

```python
from pydantic import BaseModel, Field

class Ticket(BaseModel):
    title: str = Field(
        min_length=5,
        max_length=100,
        description="Short title describing the issue"
    )

    priority: int = Field(
        ge=1,
        le=5
    )
```

### Understanding the constraints

For the title:

* `min_length=5`: At least five characters.
* `max_length=100`: Maximum 100 characters.

For priority:

* `ge=1`: Greater than or equal to 1.
* `le=5`: Less than or equal to 5.

If the supplied values violate these constraints, validation fails.

---

## 7. Field Validation

Sometimes basic type validation is not enough.

We may need custom validation rules.

For example:

* A username must not contain spaces.
* An email must follow a particular rule.
* A ticket title must not contain only whitespace.

Pydantic provides `@field_validator` for custom field validation.

Example:

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str

    @field_validator("username")
    @classmethod
    def validate_username(cls, value):
        if " " in value:
            raise ValueError("Username cannot contain spaces")

        return value
```

Valid input:

```python
user = User(username="john123")
```

Invalid input:

```python
user = User(username="john smith")
```

The invalid input raises a `ValidationError`.

### Understanding the decorator

`@field_validator("username")` tells Pydantic that the method validates the `username` field.

`@classmethod` makes the validator a class method.

`value` contains the field value being validated.

`raise ValueError()` indicates that the supplied value is invalid.

`return value` returns the validated value.

**Important:** Always return the value from a field validator when validation succeeds.

---

## 8. ValidationError

Pydantic raises `ValidationError` when the supplied data does not satisfy the model's validation requirements.

Example:

```python
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int

try:
    user = User(
        name="John",
        age="invalid"
    )

except ValidationError as error:
    print(error)
```

Pydantic identifies the field that failed validation and provides information about the error.

### Why is this important?

Applications frequently receive external data.

That data might be:

* Incorrect.
* Incomplete.
* In an unexpected format.
* Generated by an LLM.

ValidationError allows applications to identify invalid data instead of blindly processing it.

---

## 9. Strict Mode

By default, Pydantic may convert certain compatible values into the expected types.

For example, a string containing a number may be converted into an integer.

Strict mode reduces this automatic conversion.

Example:

```python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(strict=True)

    name: str
    age: int
```

Valid input:

```python
user = User(
    name="John",
    age=25
)
```

Invalid input:

```python
user = User(
    name="John",
    age="25"
)
```

The second example raises a `ValidationError` because the age is supplied as a string instead of an integer.

### Why use strict mode?

Strict validation is useful when an application must enforce predictable data types.

However, strict mode should be used according to the requirements of the application.

---

## 10. Putting the Concepts Together

Let's combine the concepts into a practical support-ticket model.

```python
from typing import Literal

from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
    field_validator
)

class SupportTicket(BaseModel):

    model_config = ConfigDict(strict=True)

    title: str = Field(
        min_length=5,
        max_length=100
    )

    description: str = Field(
        min_length=10
    )

    priority: Literal[
        "Low",
        "Medium",
        "High",
        "Critical"
    ] = "Medium"

    status: Literal[
        "Open",
        "In Progress",
        "On Hold",
        "Resolved",
        "Closed"
    ] = "Open"

    @field_validator("title", "description")
    @classmethod
    def validate_text(cls, value):
        if not value.strip():
            raise ValueError("Field cannot contain only whitespace")

        return value
```

Create a ticket:

```python
ticket = SupportTicket(
    title="Unable to login",
    description="The user cannot access the application.",
    priority="High"
)

print(ticket)
```

This model combines:

1. `BaseModel`
2. Required fields.
3. Default values.
4. `Literal`.
5. `Field()`.
6. `@field_validator`.
7. `ValidationError`.
8. Strict mode.

This is an example of how Pydantic can enforce structured data in an application.

---

## 11. Why Pydantic Matters for Agentic AI Engineering

Agentic AI applications frequently receive and generate structured data.

Consider an AI support-ticket agent.

A user says:

"I cannot log in. Please create a high-priority support ticket."

The LLM might generate:

```json
{
    "title": "Login issue",
    "description": "Unable to access the application",
    "priority": "High",
    "status": "Open"
}
```

Before processing this information, the application can validate it using Pydantic.

The process looks like this:

```text
User Input
    |
    v
LLM Processing
    |
    v
Structured Output
    |
    v
Pydantic Validation
    |
    ├── Valid
    |     |
    |     v
    |  Application Processing
    |
    └── Invalid
          |
          v
      Validation Error
```

This helps prevent invalid or unexpected data from entering application workflows.

**Important:** Pydantic validates the data structure and rules you define. It does not guarantee that an LLM-generated response is factually correct or that an intended action is safe.

---

## 12. Important Pydantic Concepts Covered

| Concept                   | Purpose                           | Status            |
| ------------------------- | --------------------------------- | ----------------- |
| `BaseModel`               | Defines structured data models    | Covered           |
| Required fields           | Enforces mandatory fields         | Covered           |
| Default values            | Provides fallback values          | Covered           |
| `Literal`                 | Restricts accepted values         | Covered           |
| `Field()`                 | Defines field constraints         | Covered           |
| `@field_validator`        | Implements custom validation      | Covered           |
| `ValidationError`         | Handles invalid data              | Covered           |
| `ConfigDict(strict=True)` | Enforces stricter type validation | Introduced        |
| Type hints                | Defines expected data types       | Basic familiarity |

---

## 13. Topics to Explore Later

These concepts are useful but are not part of the initial coverage:

* `model_validator`
* Nested Pydantic models.
* Lists and dictionaries in models.
* Optional fields and nullable values.
* `model_dump()`
* `model_dump_json()`
* `model_validate()`
* `model_validate_json()`
* JSON Schema generation.
* Pydantic integration with FastAPI.
* Validating structured LLM outputs.

We will introduce them when they become necessary in actual applications.

---

## 14. Current Progress

**Pydantic status: Basic coverage completed.**

The fundamental concepts have been introduced and practised.

This does not mean Pydantic is fully mastered.

Further concepts will be introduced when we start building applications involving APIs, structured LLM responses and agent tools.
