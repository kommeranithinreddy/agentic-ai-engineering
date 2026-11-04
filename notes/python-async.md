# Asynchronous Programming in Python

## 1. What is Asynchronous Programming?

Asynchronous programming is a programming approach that allows an application to perform other tasks while waiting for an operation to complete.

Applications frequently need to wait for external operations, such as:

* API responses.
* Database queries.
* File operations.
* Network communication.
* External AI model responses.

Instead of blocking execution while waiting, asynchronous programming allows other tasks to run.

### Example

Imagine an application performing two operations:

1. Fetching an AI response (3 seconds).
2. Fetching database information (2 seconds).

In synchronous execution, the operations run one after another.

Total time = 3 + 2 = 5 seconds.

In asynchronous execution, both operations can run concurrently.

Total time ≈ 3 seconds.

**Important:** Asynchronous programming does not necessarily make individual operations faster. It improves how efficiently an application handles waiting time.

---

## 2. Synchronous Programming

Synchronous programming executes operations sequentially.

The next operation starts after the previous operation finishes.

### Example

```python
import time

start = time.perf_counter()

def fetch_ai_response():
    print("Fetching AI response")
    time.sleep(3)
    print("AI response received")

def fetch_database_data():
    print("Fetching database data")
    time.sleep(2)
    print("Database data fetched")

fetch_ai_response()
fetch_database_data()

end = time.perf_counter()

print(f"Total time: {end - start:.2f} seconds")
```

### Execution Flow

```text
Start
  |
  v
AI request (3 seconds)
  |
  v
Database request (2 seconds)
  |
  v
Finish
```

Expected execution time: approximately 5 seconds.

### Important Concepts

**`time.sleep(seconds)`**

Pauses execution for the specified duration.

It blocks the current thread while sleeping.

**`time.perf_counter()`**

Provides a high-resolution performance counter.

It is useful for measuring how long an operation takes.

---

## 3. Asynchronous Programming

Asynchronous programming allows a program to suspend one task while waiting and execute other available tasks.

Python provides the `asyncio` library for asynchronous programming.

### Example

```python
import asyncio
import time

start = time.perf_counter()

async def fetch_ai_response():
    print("Fetching AI response")
    await asyncio.sleep(3)
    print("AI response received")

async def fetch_database_data():
    print("Fetching database data")
    await asyncio.sleep(2)
    print("Database data fetched")

async def main():
    await asyncio.gather(
        fetch_ai_response(),
        fetch_database_data()
    )

asyncio.run(main())

end = time.perf_counter()

print(f"Total time: {end - start:.2f} seconds")
```

### Execution Flow

```text
             Start
               |
        ┌──────┴──────┐
        |             |
        v             v
     Task A         Task B
        |             |
   Wait 3 sec     Wait 2 sec
        |             |
        |          Complete
        |
     Complete
        |
        v
       Finish
```

Expected execution time: approximately 3 seconds.

---

## 4. Important Asynchronous Programming Concepts

### 4.1 `async def`

The `async def` keyword defines an asynchronous function.

Example:

```python
async def fetch_data():
    print("Fetching data")
```

Calling an asynchronous function creates a coroutine object. It does not execute the function body immediately.

The coroutine must be awaited or scheduled to run.

### 4.2 Coroutine

A coroutine is an object representing an asynchronous operation.

Example:

```python
async def fetch_data():
    print("Fetching data")

result = fetch_data()
```

Here, `result` is a coroutine object.

The function body has not executed yet.

### 4.3 `await`

The `await` keyword is used inside an asynchronous function to wait for an awaitable operation.

Example:

```python
async def fetch_data():
    await asyncio.sleep(3)
    print("Data fetched")
```

When the coroutine reaches `await`, it suspends until the awaited operation completes.

During that time, the event loop can execute other available coroutines.

Important: `await` alone does not guarantee concurrency. The awaited operation must support asynchronous execution, and other tasks must be scheduled.

### 4.4 `asyncio.run()`

Starts an event loop, executes the supplied coroutine and manages the event loop's shutdown.

Example:

```python
async def main():
    print("Application started")

asyncio.run(main())
```

It is commonly used as the entry point for an asynchronous Python application.

### 4.5 `asyncio.sleep()`

Provides a non-blocking way to suspend an asynchronous coroutine.

Example:

```python
await asyncio.sleep(3)
```

Unlike `time.sleep()`, it does not block the event loop.

### 4.6 `asyncio.gather()`

Runs multiple awaitable operations concurrently and waits for their results.

Example:

```python
async def task_a():
    await asyncio.sleep(3)
    return "Task A completed"

async def task_b():
    await asyncio.sleep(2)
    return "Task B completed"

async def main():
    results = await asyncio.gather(
        task_a(),
        task_b()
    )

    print(results)

asyncio.run(main())
```

Output:

```text
['Task A completed', 'Task B completed']
```

The results are returned in the same order as the awaitables were supplied, not necessarily the order in which they finish.

---

## 5. Synchronous vs Asynchronous Programming

| Feature                | Synchronous                  | Asynchronous                      |
| ---------------------- | ---------------------------- | --------------------------------- |
| Execution              | Sequential                   | Can handle concurrent tasks       |
| Waiting                | Blocks the current thread    | Suspends the current coroutine    |
| Sleep                  | `time.sleep()`               | `asyncio.sleep()`                 |
| Function definition    | `def`                        | `async def`                       |
| Waiting for operations | Normal function calls        | `await`                           |
| Concurrency            | Not automatic                | Supported through task scheduling |
| Best suited for        | Simple sequential operations | I/O-bound operations              |

---

## 6. Blocking vs Non-Blocking Operations

### Blocking operation

A blocking operation prevents the current thread from doing other work until the operation finishes.

Example:

```python
import time

time.sleep(5)
```

If this runs inside an event loop's thread, it blocks that event loop.

### Non-blocking asynchronous operation

An asynchronous operation allows the event loop to execute other tasks while the current coroutine waits.

Example:

```python
import asyncio

await asyncio.sleep(5)
```

The current coroutine is suspended, but the event loop remains available.

---

## 7. What is the Event Loop?

The event loop is responsible for managing and scheduling asynchronous tasks.

It decides which ready coroutine should execute next.

For example:

```text
             Event Loop
                  |
          ┌───────┴───────┐
          |               |
          v               v
        Task A          Task B
          |               |
      Waiting          Executing
          |               |
          v               |
     Task Suspended       |
          |               |
          └───────┬───────┘
                  |
          Task A becomes ready
                  |
                  v
          Event Loop resumes
             Task A
```

The event loop allows multiple asynchronous operations to make progress without requiring a separate thread for every operation.

---

## 8. Why Asynchronous Programming Matters for Agentic AI

Agentic AI applications frequently communicate with multiple external services.

For example, an AI assistant might:

1. Search for information using a search API.
2. Retrieve user information from a database.
3. Send a request to an LLM API.
4. Call an external tool.
5. Send an email.

These operations often involve waiting for network responses.

Asynchronous programming helps an application handle multiple independent I/O operations efficiently.

### Example Architecture

```text
             AI Application
                   |
          ┌────────┼────────┐
          |        |        |
          v        v        v
       Search   Database   LLM
        API       Query    API
          |        |        |
          └────────┼────────┘
                   |
                   v
             Process Results
                   |
                   v
                Response
```

The application can execute independent operations concurrently instead of waiting for each one sequentially.

---

## 9. Important Limitations

Asynchronous programming is not always the best solution.

### I/O-bound operations

Examples:

* HTTP requests.
* Database communication.
* Network operations.

Asynchronous programming is particularly useful for these operations.

### CPU-bound operations

Examples:

* Large mathematical calculations.
* Image processing.
* Computationally intensive machine learning tasks.

Asyncio does not automatically make CPU-intensive work faster.

Such work may require multiprocessing, worker processes or other approaches.

---

## 10. Current Practical Understanding

The following concepts have been introduced and practised:

* Synchronous execution.
* Asynchronous execution.
* `async def`.
* Coroutines.
* `await`.
* `asyncio.run()`.
* `asyncio.sleep()`.
* `asyncio.gather()`.
* `time.sleep()`.
* `time.perf_counter()`.
* Blocking vs non-blocking execution.
* Basic event loop behaviour.
* I/O-bound operations.

# Additional Async Programming Topics

## 11. Async HTTP Requests with HTTPX

Asynchronous HTTP requests allow an application to communicate with external APIs without blocking the event loop while waiting for network responses.

Python's HTTPX library supports both synchronous and asynchronous HTTP requests.

### Synchronous HTTP Request

```python
import httpx

response = httpx.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

print(response.json())
```

This performs a synchronous HTTP request.

The current thread waits until the request completes.

### Asynchronous HTTP Request

```python
import asyncio
import httpx


async def fetch_user():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://jsonplaceholder.typicode.com/users/1"
        )

        response.raise_for_status()

        return response.json()


async def main():
    user = await fetch_user()
    print(user)


asyncio.run(main())
```

### Important Concepts

**`httpx.AsyncClient`**

Provides an asynchronous HTTP client.

**`await client.get()`**

Waits for the HTTP request to complete without blocking the event loop.

**`async with`**

Creates and manages the asynchronous client's lifecycle.

**`response.raise_for_status()`**

Raises an exception when the response contains an HTTP error status.

---

## 12. Reusing an Async HTTP Client

When an application makes multiple HTTP requests, creating a new client for every request is usually unnecessary.

A shared `AsyncClient` can reuse connections and manage resources more efficiently.

### Example

```python
import asyncio
import httpx


async def fetch_user(client, user_id):
    response = await client.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )

    response.raise_for_status()

    return response.json()


async def main():
    async with httpx.AsyncClient() as client:
        user = await fetch_user(client, 1)

        print(user)


asyncio.run(main())
```

### Important

The client is created once inside the asynchronous context manager.

The same client is passed to the function.

This avoids creating a separate HTTP client for every request.

---

## 13. Concurrent API Requests

An application may need to retrieve information from multiple API endpoints.

If the requests are independent, they can run concurrently.

### Sequential Requests

```python
import asyncio
import httpx


async def main():
    async with httpx.AsyncClient() as client:
        response1 = await client.get(
            "https://jsonplaceholder.typicode.com/users/1"
        )

        response2 = await client.get(
            "https://jsonplaceholder.typicode.com/users/2"
        )

        print(response1.json())
        print(response2.json())


asyncio.run(main())
```

The second request starts after the first request completes.

### Concurrent Requests

```python
import asyncio
import httpx


async def fetch_user(client, user_id):
    response = await client.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )

    response.raise_for_status()

    return response.json()


async def main():
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            fetch_user(client, 1),
            fetch_user(client, 2),
        )

        print(results)


asyncio.run(main())
```

### Important Concepts

- `asyncio.gather()` schedules multiple awaitable operations.
- Independent requests can make progress concurrently.
- Results are returned in the order of the supplied awaitables.
- Concurrent execution can reduce total waiting time.

**Important:** Concurrent requests do not guarantee that every request succeeds.

Each request still needs appropriate error handling.

---

## 14. Retry Handling

A request may fail because of temporary problems.

Examples:

- Network connection problems.
- Temporary server errors.
- Service unavailability.
- Request timeouts.

Retry handling allows an application to attempt a request again.

### Basic Retry Flow

```text
Request
   |
   v
Success?
   |
   +---- Yes ----> Return Result
   |
   +---- No -----> Retry
                    |
                    v
                Attempt Limit?
                    |
                    +---- No ----> Request Again
                    |
                    +---- Yes ---> Return Failure
```

### Important Concepts

**Retry**

Attempting an operation again after a failure.

**Retry attempt**

One execution of the operation.

**Maximum attempts**

The maximum number of times the application will execute the operation, including the initial attempt.

**Retry exhaustion**

The situation where all allowed attempts fail.

---

## 15. Retry Attempts

Retry attempts should be limited.

Without a limit, an application may continue retrying indefinitely.

### Example

```python
import asyncio
import httpx


async def fetch_data():
    max_attempts = 3

    async with httpx.AsyncClient() as client:
        for attempt in range(1, max_attempts + 1):
            try:
                response = await client.get(
                    "https://jsonplaceholder.typicode.com/users/1"
                )

                response.raise_for_status()

                return response.json()

            except httpx.HTTPError:
                if attempt == max_attempts:
                    raise

                await asyncio.sleep(1)


async def main():
    data = await fetch_data()

    print(data)


asyncio.run(main())
```

### How It Works

1. The application sends the request.
2. If the request succeeds, the result is returned.
3. If an HTTPX-related error occurs, the application checks the attempt count.
4. If attempts remain, the application waits.
5. The request is attempted again.
6. If all attempts fail, the exception is raised.

### Important

This example retries HTTPX-related errors broadly.

In production applications, retry policies should distinguish between retryable and non-retryable errors.

For example:

- A temporary network failure may be retryable.
- A `401 Unauthorized` response generally requires fixing authentication.
- A `404 Not Found` response generally does not become successful by retrying.

---

## 16. Retry Exhaustion

Retry exhaustion occurs when the request has failed on every allowed attempt.

The application should stop retrying and handle the failure.

### Example

```python
import asyncio
import httpx


async def fetch_data():
    max_attempts = 3

    async with httpx.AsyncClient() as client:
        for attempt in range(1, max_attempts + 1):
            try:
                response = await client.get(
                    "https://jsonplaceholder.typicode.com/users/1"
                )

                response.raise_for_status()

                return response.json()

            except httpx.HTTPError:
                if attempt == max_attempts:
                    raise

                await asyncio.sleep(1)

    raise RuntimeError("Request failed")


async def main():
    try:
        data = await fetch_data()

        print(data)

    except httpx.HTTPError as error:
        print(f"Request failed after retries: {error}")


asyncio.run(main())
```

### Important

The retry loop should have a clear stopping condition.

The application should not silently return invalid data when all attempts fail.

---

## 17. Logging in Python

Logging records events that occur while an application runs.

It helps developers understand:

- What the application is doing.
- Whether operations succeeded.
- Whether requests failed.
- Whether retries occurred.
- Why an operation failed.

Python provides the built-in `logging` module.

### Example

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Application started")
logging.warning("Request failed")
logging.error("API operation failed")
```

### Common Logging Levels

| Level | Purpose |
|---|---|
| DEBUG | Detailed information for debugging |
| INFO | Normal application events |
| WARNING | Something unexpected happened |
| ERROR | An operation failed |
| CRITICAL | A serious application failure |

### Important

Logging levels help control which messages are recorded.

For example:

```python
logging.basicConfig(level=logging.INFO)
```

This records INFO messages and more severe messages.

DEBUG messages are not displayed at this level.

---

## 18. Logging in Async Applications

Logging can be used inside asynchronous functions.

### Example

```python
import asyncio
import logging

logging.basicConfig(level=logging.INFO)


async def fetch_data():
    logging.info("Starting request")

    await asyncio.sleep(2)

    logging.info("Request completed")


async def main():
    await fetch_data()


asyncio.run(main())
```

### Important

Logging does not automatically make an operation asynchronous.

It records application events.

The asynchronous behavior comes from the coroutine and its awaited operations.

---

## 19. Logging API Requests and Retries

Logging helps track the behavior of API requests.

Useful events include:

- Request started.
- Request succeeded.
- Request failed.
- Retry started.
- Retry limit reached.

### Example

```python
import asyncio
import logging
import httpx

logging.basicConfig(level=logging.INFO)


async def fetch_data():
    max_attempts = 3

    async with httpx.AsyncClient() as client:
        for attempt in range(1, max_attempts + 1):
            try:
                logging.info(
                    "Request started. Attempt %s",
                    attempt,
                )

                response = await client.get(
                    "https://jsonplaceholder.typicode.com/users/1"
                )

                response.raise_for_status()

                logging.info("Request succeeded")

                return response.json()

            except httpx.HTTPError as error:
                if attempt == max_attempts:
                    logging.error(
                        "Request failed after %s attempts: %s",
                        max_attempts,
                        error,
                    )

                    raise

                logging.warning(
                    "Request failed. Retrying: %s",
                    error,
                )

                await asyncio.sleep(1)


async def main():
    try:
        data = await fetch_data()

        print(data)

    except httpx.HTTPError:
        logging.error("Unable to retrieve data")


asyncio.run(main())
```

### Important Concepts

**INFO**

Records normal application events.

**WARNING**

Records a failure that the application intends to retry.

**ERROR**

Records a final failure when the operation cannot complete.

**Exception handling**

Allows the application to handle errors instead of terminating unexpectedly.

---

## 20. Retry and Logging Best Practices

### Retry

- Set a maximum number of attempts.
- Retry only appropriate failures.
- Avoid retrying permanent errors unnecessarily.
- Use delays between attempts.
- Respect API rate limits.
- Avoid retrying operations that may cause duplicate side effects unless the API supports safe retries.

### Logging

- Record important application events.
- Use appropriate logging levels.
- Include useful error information.
- Avoid logging passwords, API keys, access tokens, or sensitive data.
- Avoid logging excessive information for every request.

### Important

Retry handling and logging serve different purposes.

Retry handling attempts to recover from failures.

Logging records what happened.

---

## 21. Current Async Coverage

### Covered

- Synchronous execution.
- Asynchronous execution.
- `async def`.
- Coroutines.
- `await`.
- `asyncio.run()`.
- `asyncio.sleep()`.
- `asyncio.gather()`.
- Blocking vs non-blocking operations.
- Event loop basics.
- I/O-bound operations.
- Async HTTPX requests.
- Shared async HTTP clients.
- Concurrent API requests.
- Basic retry handling.
- Maximum retry attempts.
- Retry exhaustion.

### Still To Be Covered

- Python logging.
- Logging levels.
- Logging request failures and retries.
- Creating and managing tasks using `asyncio.create_task()`.
- Task lifecycle.
- Exception handling across concurrent tasks.
- Timeouts and cancellation.
- Async context managers in more detail.
- Async database operations.
- Production retry policies.
- Backoff strategies.
- Request concurrency limits.

**Status: Asynchronous programming is IN PROGRESS.**

These notes document the topics covered so far. They do not represent completion of the full asynchronous programming curriculum.
