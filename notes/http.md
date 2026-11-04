# HTTP Fundamentals

## 1. What is HTTP?

HTTP stands for **Hypertext Transfer Protocol**.

It is a communication protocol that defines how applications exchange information over a network.

HTTP establishes rules for:
- Sending requests.
- Receiving responses.
- Identifying resources.
- Communicating data.
- Handling different request methods.
- Returning status codes.

HTTP is commonly used when a Python application communicates with an external service.

### Example

A Python application needs information from an external API.

```text
Python Application
       |
       | HTTP Request
       v
External Server
       |
       | HTTP Response
       v
Python Application
```

The application sends a request, and the server returns a response.

---

## 2. Client and Server

HTTP communication commonly involves two roles.

### Client

The client initiates a request.

Examples:
- Python application.
- Web browser.
- Mobile application.
- AI application.

### Server

The server receives the request, processes it, and returns a response.

Examples:
- AI provider server.
- Google Calendar server.
- Application backend.
- Database API server.

### Communication Flow

```text
Client
  |
  | Request
  v
Server
  |
  | Process request
  |
  | Response
  v
Client
```

The client and server communicate using the rules defined by HTTP.

---

## 3. HTTP Request

An HTTP request is a message sent by a client to a server.

A request commonly contains:

- HTTP method.
- URL.
- Headers.
- Optional query parameters.
- Optional request body.

### Example

```http
GET /users/25 HTTP/1.1
Host: api.example.com
Accept: application/json
```

This request asks the server to retrieve information about user 25.

### Request Components

| Component | Purpose |
|---|---|
| Method | Defines the operation being requested. |
| URL | Identifies the server and resource. |
| Headers | Provide additional information about the request. |
| Query parameters | Pass additional information through the URL. |
| Body | Contains data sent to the server when required. |

Not every request contains a body.

For example, a GET request commonly retrieves information without sending a request body.

---

## 4. HTTP Methods

HTTP methods describe the operation the client wants to perform.

| Method | Purpose | Example |
|---|---|---|
| GET | Retrieve information | Get user details |
| POST | Submit information or create a resource | Create a ticket |
| PUT | Replace a resource | Replace user details |
| PATCH | Partially update a resource | Update user email |
| DELETE | Delete a resource | Delete a ticket |

### GET

Used to retrieve information.

Example:

```http
GET /users/25
```

Meaning:

Retrieve information about user 25.

### POST

Used to submit information or create a resource.

Example:

```http
POST /tickets
```

The request body might contain:

```json
{
  "title": "Login issue",
  "priority": "high"
}
```

The server processes the submitted information.

### PUT

Used to replace a resource.

Example:

```http
PUT /users/25
```

The client sends the replacement representation of the resource.

### PATCH

Used to partially update a resource.

Example:

```http
PATCH /users/25
```

The request body might contain:

```json
{
  "email": "new@example.com"
}
```

The intention is to update only the email field.

### DELETE

Used to request deletion of a resource.

Example:

```http
DELETE /tickets/10
```

The server processes the deletion according to its implementation and permissions.

---

## 5. HTTP Headers

HTTP headers provide additional information about a request or response.

Headers contain metadata.

They do not normally contain the main resource data.

### Content-Type

`Content-Type` describes the media type of the message body.

Example:

```http
Content-Type: application/json
```

Meaning:

The message body contains JSON data.

It can appear in a request or response.

### Accept

`Accept` indicates which response media types the client can accept.

Example:

```http
Accept: application/json
```

Meaning:

The client indicates that it can accept a JSON response.

### Authorization

`Authorization` provides credentials used to authenticate a request.

Example:

```http
Authorization: Bearer <access_token>
```

The server can use the supplied credential to identify the caller and determine whether the requested operation is permitted.

### Important Difference

| Header | Purpose |
|---|---|
| Content-Type | Describes the message body format. |
| Accept | Indicates the response formats the client accepts. |
| Authorization | Provides authentication credentials. |

---

## 6. JSON

JSON stands for **JavaScript Object Notation**.

It is a data format commonly used to exchange information between applications.

JSON supports:

- Strings.
- Numbers.
- Booleans.
- Arrays.
- Objects.
- Null values.

### Example

```json
{
  "id": 25,
  "name": "John",
  "active": true
}
```

This represents an object containing three fields.

### JSON and Python

JSON objects resemble Python dictionaries.

JSON:

```json
{
  "name": "John",
  "active": true
}
```

Python:

```python
{
    "name": "John",
    "active": True
}
```

Important differences:

- JSON uses `true`; Python uses `True`.
- JSON uses `false`; Python uses `False`.
- JSON uses `null`; Python uses `None`.

Python applications commonly convert JSON responses into Python data structures before processing them.

---

## 7. HTTP Response

An HTTP response is a message returned by the server after receiving a request.

A response commonly contains:

- Status code.
- Response headers.
- Optional response body.

### Example

```http
HTTP/1.1 200 OK
Content-Type: application/json
```

Response body:

```json
{
  "id": 25,
  "name": "John"
}
```

The server has returned information about the requested resource.

### Response Components

| Component | Purpose |
|---|---|
| Status code | Indicates the result of the request. |
| Headers | Provide additional response information. |
| Body | Contains the returned data, when present. |

---

## 8. HTTP Status Codes

Status codes indicate the result of an HTTP request.

### Successful Responses

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content |

### Client Errors

| Code | Meaning |
|---|---|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 405 | Method Not Allowed |
| 429 | Too Many Requests |

### Server Errors

| Code | Meaning |
|---|---|
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |

### Important Differences

**401 Unauthorized**

The request lacks valid authentication credentials or the supplied credentials are invalid.

**403 Forbidden**

The server refuses the requested operation because the caller does not have sufficient permission.

**404 Not Found**

The requested resource was not found, or the server does not expose it.

**429 Too Many Requests**

The client has exceeded a request limit.

**503 Service Unavailable**

The server is temporarily unable to handle the request.

---

## 9. HTTP and HTTPS

### HTTP

HTTP defines the communication protocol.

Traditional HTTP communication does not itself provide encryption.

### HTTPS

HTTPS is HTTP communication protected by TLS.

TLS provides:
- Encryption.
- Server authentication.
- Protection against unauthorized modification of data in transit.

HTTPS is important when applications exchange:
- API keys.
- Access tokens.
- Personal information.
- Sensitive application data.

For external APIs, HTTPS should be used whenever supported.

---

## 10. Stateless Communication

HTTP is stateless by default.

This means the protocol does not automatically remember the previous request when processing a new request.

### Example

A client sends:

```http
GET /users/25
```

Later, it sends:

```http
GET /users/25/orders
```

The second request does not automatically inherit the first request's authentication or application state.

Applications can maintain state using mechanisms such as:

- Cookies.
- Sessions.
- Access tokens.
- Application databases.

Stateless HTTP does not mean applications cannot maintain user sessions.

It means that HTTP itself does not automatically remember previous requests.

---

## 11. HTTP in Agentic AI Applications

HTTP is important because AI applications frequently communicate with external services.

Examples include:

- LLM providers.
- Search services.
- Calendar APIs.
- Email APIs.
- Internal application APIs.
- External tools.

### Example: AI Assistant

```text
User
 |
 | Request
 v
Python AI Application
 |
 | HTTP Request
 v
LLM Provider
 |
 | HTTP Response
 v
Python AI Application
 |
 | Process Model Response
 v
User
```

The Python application sends information to the AI provider.

The provider processes the request and returns a response.

The application then processes that response.

### Example: Agent Tool

An agent may need to retrieve information from an external service.

```text
User Request
     |
     v
AI Agent
     |
     v
Python Tool
     |
     v
HTTP Request
     |
     v
External API
     |
     v
HTTP Response
     |
     v
Python Tool
     |
     v
AI Agent
```

The HTTP request allows the application to communicate with the external service.

The agent can then use the returned information to continue processing the user's request.

---

## 12. Key Points

- HTTP defines communication rules between applications.
- A client sends a request.
- A server processes the request and returns a response.
- HTTP methods describe the requested operation.
- Headers provide additional information.
- JSON is a common data format.
- Status codes indicate the result of a request.
- HTTPS protects HTTP communication using TLS.
- HTTP is stateless by default.
- AI applications commonly use HTTP APIs to communicate with external services.

---

## 13. Completion Criteria

HTTP fundamentals are sufficiently covered when I can:

- Explain the client-server communication flow.
- Identify the components of an HTTP request.
- Explain the difference between GET, POST, PUT, PATCH, and DELETE.
- Explain Content-Type, Accept, and Authorization.
- Understand JSON request and response bodies.
- Interpret common HTTP status codes.
- Explain HTTP versus HTTPS.
- Explain why HTTP is stateless.
- Describe how an AI application uses HTTP to communicate with an external API.