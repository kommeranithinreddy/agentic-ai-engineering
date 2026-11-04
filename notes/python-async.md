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

### Topics Still To Be Covered

* Creating and managing tasks using `asyncio.create_task()`.
* Understanding task lifecycle.
* Exception handling in asynchronous tasks.
* Timeouts and cancellation.
* Async context managers.
* Async HTTP clients.
* Concurrent API requests.
* Practical asynchronous database operations.

**Status: Asynchronous programming is IN PROGRESS.**

These notes document the concepts covered so far, not a completed asynchronous programming curriculum.
