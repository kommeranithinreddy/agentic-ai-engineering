# API Fundamentals

## 1. What Is an API?

API stands for **Application Programming Interface**.

An API allows one software application to communicate with another application.

For example, an Agentic AI application might need to:
- Retrieve information from an external service.
- Send data to another application.
- Create or update records.
- Call an LLM provider.
- Access tools through an API.

Instead of directly accessing another application's internal code or database, the application communicates through an API.

### Example

An AI application wants to retrieve weather information.

The application sends a request to a weather API.

The API processes the request and returns weather data.

The application can then use that data.

**Basic flow:**

```text
Application
    |
    | API Request
    v
External Service
    |
    | API Response
    v
Application
```

---

## 2. How an API Works

An API communication usually involves two sides:

### Client

The client sends a request.

Examples:
- Python application
- Web browser
- Agent
- Mobile application

### Server

The server receives the request, processes it, and sends a response.

The server may:
- Retrieve data.
- Validate input.
- Perform an operation.
- Communicate with a database.
- Return an error.

### Communication flow

```text
Client
  |
  | 1. Sends request
  v
API Server
  |
  | 2. Processes request
  |
  | 3. Returns response
  v
Client
```

The client and server communicate using an agreed interface.

---

## 3. What Is an API Endpoint?

An endpoint is a specific address where an API operation can be accessed.

Example:

```text
https://api.example.com/users
```

This endpoint represents a resource related to users.

Another endpoint:

```text
https://api.example.com/users/101
```

This represents a specific user.

An endpoint usually consists of:

- Base URL
- Resource path

Example:

```text
Base URL:
https://api.example.com

Resource path:
/users/101

Endpoint:
https://api.example.com/users/101
```

The endpoint identifies where the client sends its request.

---

## 4. API Request

An API request is a message sent by a client to an API server.

A request commonly contains:

1. HTTP method
2. URL
3. Headers
4. Optional request body

Example:

```http
GET /users/101 HTTP/1.1
Host: api.example.com
Accept: application/json
```

This request asks the server to retrieve user information.

### Request components

| Component | Purpose |
|---|---|
| Method | Specifies the requested operation |
| URL | Identifies the endpoint |
| Headers | Provide additional request information |
| Body | Contains data sent to the server, when required |

Not every request contains a body.

For example, a GET request commonly retrieves information without sending a request body.

---

## 5. HTTP Methods Used in APIs

HTTP methods indicate what operation the client wants to perform.

### GET

Retrieves information.

Example:

```http
GET /users/101
```

Meaning:

Retrieve the user with ID 101.

### POST

Submits data to create a resource or perform an operation.

Example:

```http
POST /users
```

A request body might contain:

```json
{
  "name": "Agent",
  "role": "assistant"
}
```

Meaning:

Submit data to create a user.

The exact behavior depends on the API.

### PUT

Usually replaces the representation of an existing resource.

Example:

```http
PUT /users/101
```

The request may contain the complete updated user representation.

### PATCH

Updates part of an existing resource.

Example:

```http
PATCH /users/101
```

A request body might contain:

```json
{
  "role": "admin"
}
```

Meaning:

Update the user's role.

### DELETE

Requests deletion of a resource.

Example:

```http
DELETE /users/101
```

Meaning:

Delete the user with ID 101.

### Method summary

| Method | Common purpose |
|---|---|
| GET | Retrieve information |
| POST | Create a resource or perform an operation |
| PUT | Replace a resource |
| PATCH | Partially update a resource |
| DELETE | Delete a resource |

The API documentation defines the exact behavior of each endpoint.

---

## 6. API Request Headers

Headers provide additional information about a request.

Example:

```http
Accept: application/json
```

This tells the server that the client expects JSON response data.

### Common headers

| Header | Purpose |
|---|---|
| Accept | Indicates response formats the client can accept |
| Content-Type | Indicates the format of the request body |
| Authorization | Provides authentication credentials |
| User-Agent | Identifies the client software |

### Content-Type

Example:

```http
Content-Type: application/json
```

This indicates that the request body contains JSON data.

Example request:

```http
POST /users HTTP/1.1
Host: api.example.com
Content-Type: application/json
```

Request body:

```json
{
  "name": "Agent"
}
```

### Accept

Example:

```http
Accept: application/json
```

This indicates that the client accepts JSON as a response format.

**Remember:**

- `Content-Type` describes the body being sent.
- `Accept` describes the response format the client can accept.

---

## 7. JSON in APIs

JSON stands for **JavaScript Object Notation**.

It is a common format for exchanging structured data between applications.

Example:

```json
{
  "name": "Agent",
  "active": true,
  "priority": 2
}
```

JSON supports:

- Strings
- Numbers
- Booleans
- Arrays
- Objects
- `null`

### JSON object

```json
{
  "name": "Agent",
  "role": "assistant"
}
```

### JSON array

```json
[
  "Python",
  "API",
  "FastAPI"
]
```

### Nested JSON

```json
{
  "user": {
    "id": 101,
    "name": "Agent"
  }
}
```

APIs commonly use JSON because it provides a structured format that applications can exchange and process.

---

## 8. API Response

An API response is the message returned by the server after processing a request.

A response commonly contains:

1. Status code
2. Headers
3. Response body

Example:

```http
HTTP/1.1 200 OK
Content-Type: application/json
```

Response body:

```json
{
  "id": 101,
  "name": "Agent"
}
```

The response tells the client whether the request succeeded and may contain the requested information.

---

## 9. HTTP Status Codes

Status codes indicate the result of an HTTP request.

### 2xx — Success

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 202 | Accepted |
| 204 | No Content |

Examples:

- `200 OK`: Request succeeded.
- `201 Created`: A resource was created.
- `204 No Content`: Request succeeded, but there is no response body.

### 4xx — Client Error

| Code | Meaning |
|---|---|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 422 | Unprocessable Content |
| 429 | Too Many Requests |

Examples:

- `400`: Request contains invalid information.
- `401`: Authentication is missing or invalid.
- `403`: The client does not have permission.
- `404`: The requested resource was not found.
- `429`: The client exceeded a rate limit.

### 5xx — Server Error

| Code | Meaning |
|---|---|
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |
| 504 | Gateway Timeout |

These indicate that the server or an upstream service could not successfully complete the request.

### Important distinction

**401 Unauthorized**

The client has not successfully authenticated.

**403 Forbidden**

The client is authenticated or otherwise identified, but does not have permission to perform the operation.

---

## 10. API Authentication

Authentication allows an API to identify the client making a request.

Some APIs require credentials before allowing access.

Common authentication approaches include:

- API keys
- Bearer tokens
- OAuth 2.0
- Session-based authentication

The API documentation specifies which method is required.

### API Key

An API key is a credential used to identify or authorize an application.

Example:

```http
X-API-Key: YOUR_API_KEY
```

The actual header name depends on the API.

API keys should be kept private.

### Bearer Token

A bearer token is a credential sent with a request.

Example:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

The server validates the token before allowing access.

Do not expose real access tokens in:
- GitHub repositories
- Public logs
- Screenshots
- Shared code

### OAuth 2.0

OAuth 2.0 is an authorization framework that allows applications to obtain limited access to another service.

For example, an application might request permission to read a user's calendar.

The user grants the required permission through the service's authorization flow.

The application receives an access token and uses it to make permitted API requests.

The available permissions depend on the authorization granted.

---

## 11. API Errors

API requests can fail for different reasons.

Common causes include:

- Incorrect endpoint
- Invalid request data
- Missing authentication
- Insufficient permissions
- Rate limits
- Network problems
- Server errors

Example:

```http
GET /users/999999
```

The server might return:

```http
HTTP/1.1 404 Not Found
```

This indicates that the requested resource was not found.

Another example:

```http
HTTP/1.1 429 Too Many Requests
```

This indicates that the client has exceeded a request limit.

The application should inspect the response and handle the error appropriately.

---

## 12. API Documentation

API documentation explains how to use an API.

It commonly provides:

- Base URL
- Endpoints
- HTTP methods
- Required parameters
- Request headers
- Request body schema
- Authentication requirements
- Response formats
- Status codes
- Rate limits

Before integrating an API, identify:

1. What endpoint is required?
2. Which HTTP method should be used?
3. What parameters are required?
4. Does authentication need to be configured?
5. What response format is returned?
6. What errors can occur?

The documentation is the source of truth for the API's behavior.

---

## 13. Calling an API from Python

Python applications can send HTTP requests using an HTTP client library.

One commonly used library is `httpx`.

Install it:

```bash
pip install httpx
```

### Example: GET request

```python
import httpx

response = httpx.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

print(response.status_code)
print(response.json())
```

This example:

1. Sends a GET request.
2. Receives an HTTP response.
3. Prints the status code.
4. Converts the JSON response into Python data.

The returned JSON object can be accessed using normal Python operations.

Example:

```python
user = response.json()

print(user["name"])
```

### Example: POST request

```python
import httpx

response = httpx.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={
        "title": "Agent API",
        "body": "API request example",
        "userId": 1,
    },
)

print(response.status_code)
print(response.json())
```

The `json` parameter sends the provided Python data as JSON.

**Note:** JSONPlaceholder is a testing service. Its POST endpoint simulates resource creation and does not permanently save the submitted post.

---

## 14. Handling API Errors in Python

A successful HTTP request does not always mean the application received the expected result.

The application should check for HTTP errors.

Example:

```python
import httpx

response = httpx.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

response.raise_for_status()

user = response.json()
```

`raise_for_status()` raises an exception when the response contains an HTTP error status.

This helps prevent the application from treating an unsuccessful response as successful data.

### Basic error handling

```python
import httpx

try:
    response = httpx.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=10,
    )

    response.raise_for_status()

    user = response.json()

except httpx.HTTPError as error:
    print(f"API request failed: {error}")
```

This catches HTTPX-related request and response errors.

In production applications, errors should be handled according to their type and the application's requirements.

---

## 15. API Integration in Agentic AI Engineering

Agentic AI applications often communicate with external services through APIs.

Examples include:

- LLM providers
- Search services
- Databases
- Calendar applications
- File storage
- Internal business systems

An agent may use a tool that calls an API.

### Example flow

```text
User
 |
 | Request
 v
AI Agent
 |
 | Selects a tool
 v
Tool Function
 |
 | API Request
 v
External API
 |
 | API Response
 v
Tool Function
 |
 | Returns result
 v
AI Agent
 |
 | Generates response
 v
User
```

### Example

A user asks:

```text
Find information about a document.
```

The agent may:

1. Understand the request.
2. Select a search tool.
3. Call the tool.
4. The tool sends an API request.
5. The API returns results.
6. The tool provides the results to the agent.
7. The agent uses the results to answer.

The API performs the external communication.

The agent decides when and how to use the tool, based on its instructions and available capabilities.

---

## 16. Important API Concepts

| Concept | Meaning |
|---|---|
| API | Interface that allows software systems to communicate |
| Endpoint | Address where an API operation is available |
| Request | Message sent by the client |
| Response | Message returned by the server |
| HTTP method | Operation requested by the client |
| Header | Additional information about a request or response |
| JSON | Structured data format |
| Status code | Indicates the result of an HTTP request |
| Authentication | Identifies or verifies the client |
| Authorization | Determines what the client is allowed to access |
| Access token | Credential used to access protected resources |
| Rate limit | Restriction on how frequently requests can be made |

---

## 17. Summary

An API allows applications to communicate through a defined interface.

Important concepts:

- APIs connect clients and servers.
- Endpoints identify API operations.
- HTTP methods describe the requested operation.
- Headers provide additional request information.
- JSON is commonly used to exchange structured data.
- Responses contain status codes and may contain data.
- Authentication identifies the client.
- Authorization controls access.
- API documentation explains how to use an API.
- Python HTTP clients can send requests and process responses.
- Agentic AI tools can use APIs to interact with external services.

**Remember:** An API is the interface. HTTP is a communication protocol commonly used by web APIs. JSON is a data format often exchanged through those APIs.

---

## Completion Criteria

- [ ] Explain what an API is.
- [ ] Identify client and server.
- [ ] Understand endpoints.
- [ ] Understand GET, POST, PUT, PATCH, and DELETE.
- [ ] Identify request components.
- [ ] Understand headers and JSON.
- [ ] Read an API response.
- [ ] Recognize common HTTP status codes.
- [ ] Understand API authentication.
- [ ] Read API documentation.
- [ ] Send a GET request using Python.
- [ ] Send a POST request using Python.
- [ ] Handle HTTP errors.
- [ ] Explain how an Agentic AI tool can call an API.