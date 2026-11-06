# Environment Variables

## 1. What Are Environment Variables?

Environment variables are named configuration values available to an
application at runtime. They let an application use different settings
without changing its source code.

Examples: - `APP_NAME` --- application name - `APP_ENV` --- environment
such as development or production - `PORT` --- server port -
`DATABASE_URL` --- database connection string - `API_KEY` --- secret
credential

Environment variables are not limited to secrets. They are also used for
ordinary application configuration.

## 2. Reading Environment Variables in Python

Python provides `os.environ` and `os.getenv()`.

``` python
import os

app_name = os.getenv("APP_NAME")
app_env = os.getenv("APP_ENV")
```

### `os.environ["KEY"]`

``` python
app_name = os.environ["APP_NAME"]
```

-   Reads the variable.
-   Raises `KeyError` if the variable does not exist.

### `os.getenv("KEY")`

``` python
app_name = os.getenv("APP_NAME")
```

-   Reads the variable.
-   Returns `None` if it does not exist.

A default value can also be provided:

``` python
app_env = os.getenv("APP_ENV", "development")
```

## 3. Environment Variable Scope

In PowerShell, an environment variable can be set for the current
process:

``` powershell
$env:APP_NAME = "TicketProcessor"
```

Read it:

``` powershell
echo $env:APP_NAME
```

This value is available in the current PowerShell session and processes
launched from it. It does not automatically persist into a separate new
terminal session.

## 4. What Is a `.env` File?

A `.env` file stores configuration as `KEY=value` lines.

Example:

``` env
APP_NAME=TicketProcessor
APP_ENV=development
```

A `.env` file is a convenient way to keep local configuration outside
Python source code.

Python does not automatically read `.env` files. A package such as
`python-dotenv` can load them.

## 5. Loading `.env` with `python-dotenv`

Install the package:

``` powershell
python -m pip install python-dotenv
```

Use it in Python:

``` python
from dotenv import load_dotenv
import os

load_dotenv()

app_name = os.getenv("APP_NAME")
app_env = os.getenv("APP_ENV")

print(app_name)
print(app_env)
```

### How it works

1.  `load_dotenv()` searches for and reads a `.env` file.
2.  Its values are loaded into the process environment.
3.  Python reads the values using `os.getenv()` or `os.environ`.

The import name is `dotenv`, even though the package is installed as
`python-dotenv`.

## 6. `.env` Location

A `.env` file can be placed in the repository root or a project
subfolder.

Example:

``` text
agentic-ai-engineering/
├── .env
├── practice/
│   └── python-environment/
│       └── 02_dotenv.py
└── .venv/
```

When using `load_dotenv()` without an explicit path, it searches for a
`.env` file from its search location and parent directories. The current
working directory and how the script is launched can affect which file
is found.

For a specific file location, pass its path to `load_dotenv()`.

## 7. Protecting `.env` with `.gitignore`

Actual local configuration should generally not be committed when it may
contain secrets.

Example `.gitignore` rules:

``` gitignore
# Environment variables and secrets
.env
.env.*

# Keep example configuration files
!.env.example
```

Meaning: - `.env` --- ignore the local environment file. - `.env.*` ---
ignore files such as `.env.local` and `.env.production`. -
`!.env.example` --- exception: allow the example file to be tracked.

**Important:** `.gitignore` prevents untracked matching files from being
added. It does not automatically untrack a file that Git already tracks.

## 8. Purpose of `.env.example`

`.env.example` documents the configuration variables an application
needs without sharing actual credentials.

Example:

``` env
APP_NAME=your_app_name
APP_ENV=your_app_env
```

A typical workflow:

1.  The project maintainer commits `.env.example`.
2.  The maintainer keeps their actual `.env` local and ignored.
3.  A user clones the repository.
4.  The user copies `.env.example` to `.env`.
5.  The user fills in their own configuration.
6.  The application loads `.env` using `python-dotenv`.

## 9. Key Points

-   Environment variables separate configuration from application code.
-   They can contain ordinary settings or secrets.
-   `os.environ["KEY"]` raises `KeyError` when the key is missing.
-   `os.getenv("KEY")` returns `None` when the key is missing unless a
    default is supplied.
-   Python does not automatically load `.env` files.
-   `python-dotenv` provides `load_dotenv()`.
-   `.env` should be excluded from Git when it contains local
    configuration or secrets.
-   `.env.example` can be committed to document required variables.
-   `.gitignore` does not remove files that are already tracked.

## 10. Practice Files

Environment variable practice was performed in:

``` text
practice/python-environment/
├── 01_environment_variables.py
├── 02_dotenv.py
└── .env
```

The repository's `.gitignore` already includes rules for `.env` and
`.env.*`, while allowing `.env.example`.
