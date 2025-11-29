# Shell Tools MCP Server

An MCP server for shell tools, allowing you to run shell commands and edit files via the Model Context Protocol.

## Installation

### Using `uv` (Recommended)

You can run the server directly using `uv`:

```bash
uv run shell-tools-mcp-server
```

### Using `pip`

```bash
pip install .
shell-tools-mcp-server
```

## Usage

### Stdio (Default)

By default, the server runs over stdio, which is suitable for integration with MCP clients like Claude Desktop or other agents.

```bash
uv run shell-tools-mcp-server
```

### HTTP (SSE)

You can also run the server over HTTP using Server-Sent Events (SSE).

```bash
uv run shell-tools-mcp-server --http --port 8000
```

## Available Tools

### `run_shell_command`
Run a shell command and return its output.

- **command** (`str`): The shell command to run.
- **cwd** (`str`, optional): The working directory to run the command in. Defaults to current directory.
- **timeout** (`int`, optional): Timeout for the command in seconds. Defaults to 60 seconds.
- **run_in_bg** (`bool`, optional): If `True`, runs the command in the background. Defaults to `False`.

### `file_edit`
Edit a file by replacing occurrences of a string.

- **file_path** (`str`): The absolute path to the file to modify.
- **old_string** (`str`): The text to replace.
- **new_string** (`str`): The text to replace it with.
- **replace_all** (`bool`, optional): Replace all occurrences if `True`, else only the first occurrence. Defaults to `False`.

### `file_multi_edit`
Edit a file by applying multiple edit operations in sequence.

- **file_path** (`str`): The absolute path to the file to modify.
- **edits** (`List[dict]`): List of edit operations. Each dict should have:
    - `old_string`: The text to replace.
    - `new_string`: The text to replace it with.
    - `replace_all` (optional): Boolean to replace all occurrences.

### `file_read`
Read a file with optional offset and limit.

- **file_path** (`str`): The absolute path to the file to read.
- **offset** (`int`, optional): The line number to start reading from (0-indexed).
- **limit** (`int`, optional): The number of lines to read.

### `file_replace`
Replace occurrences of a string in a file. This is functionally identical to `file_edit`.

- **file_path** (`str`): The absolute path to the file to modify.
- **old_string** (`str`): The text to replace.
- **new_string** (`str`): The text to replace it with.
- **replace_all** (`bool`, optional): Replace all occurrences if `True`, else only the first occurrence. Defaults to `False`.

## Development

### Prerequisites

- Python 3.10+
- `uv` package manager

### Setup

1. Clone the repository.
2. Install dependencies:

```bash
uv sync
```

### Running Locally

You can run the server locally for testing:

```bash
uv run shell-tools-mcp-server --help
```

### Testing

You can test the server by running it and interacting with it via an MCP inspector or by invoking the tools directly if you add a test script.
