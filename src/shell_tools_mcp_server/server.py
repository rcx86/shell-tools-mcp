import os
import subprocess
import argparse
from typing import List, Optional
from fastmcp import FastMCP
from rich import print as rprint

# Initialize FastMCP server
mcp = FastMCP("Shell Tools")

@mcp.tool()
def run_shell_command(command: str, cwd: Optional[str] = None, timeout: int = 60, run_in_bg: bool = False) -> str:
    """
    Run a shell command and return its output.

    Args:
        command (str): The shell command to run.
        cwd (Optional[str]): The working directory to run the command in.
        timeout (int): Timeout for the command in seconds. Defaults to 60 seconds.
        run_in_bg (bool): If True, runs the command in the background.
    """
    rprint(f"[bold blue]Running shell command:[/bold blue] [green]{command}[/green] in [yellow]{cwd or os.getcwd()}[/yellow] with timeout = [cyan]{timeout}[/cyan] run_in_bg = [cyan]{run_in_bg}[/cyan]")
    try:
        if run_in_bg:
            process = subprocess.Popen(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, preexec_fn=os.setsid)
            return f"Process started in background with PID {process.pid}"
        else:
            result = subprocess.run(
                command,
                cwd=cwd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=timeout,
                shell=True,
                check=True
            )
            return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return (f"Command failed: {e.stderr.strip()}")
    except subprocess.TimeoutExpired as e:
        return f"Command {command} timed out"

@mcp.tool()
def file_edit(
        file_path: str,
        old_string: str,
        new_string: str,
        replace_all: bool = False
) -> str:
    """
    Edit a file by replacing occurrences of old_string with new_string.

    Args:
        file_path (str): The absolute path to the file to modify.
        old_string (str): The text to replace.
        new_string (str): The text to replace it with.
        replace_all (bool): Replace all occurrences if True, else only the first occurrence.

    Returns:
        str: Success message or error.
    """
    rprint(f"[bold blue]Running edit[/bold blue] on file: [yellow]{file_path}[/yellow] replacing [red]{old_string}[/red] with [green]{new_string}[/green] replace_all = [cyan]{replace_all}[/cyan]")
    if not os.path.isfile(file_path):
        return (f"File not found: {file_path}. Recheck the path.")

    try:
        with open(file_path, 'r') as file:
            content = file.read()

        if replace_all:
            new_content = content.replace(old_string, new_string)
        else:
            new_content = content.replace(old_string, new_string, 1)

        with open(file_path, 'w') as file:
            file.write(new_content)

        return f"Successfully edited {file_path}"
    except Exception as e:
        return (f"Failed to edit file: {str(e)}")

@mcp.tool()
def file_multi_edit(
        file_path: str,
        edits: List[dict]
) -> str:
    """
    Edit a file by applying multiple edit operations.

    Args:
        file_path (str): The absolute path to the file to modify.
        edits (List[dict]): List of edit operations. Each dict should have 'old_string', 'new_string', and optionally 'replace_all'.

    Returns:
        str: Success message or error.
    """
    rprint(f"[bold blue]Running multi_edit[/bold blue] on file: [yellow]{file_path}[/yellow] with edits: [cyan]{edits}[/cyan]")
    if not os.path.isfile(file_path):
        return (f"File not found: {file_path}. Recheck the path.")

    try:
        with open(file_path, 'r') as file:
            content = file.read()

        for edit in edits:
            old_string = edit.get("old_string")
            new_string = edit.get("new_string")
            replace_all = edit.get("replace_all", False)

            if old_string is None or new_string is None:
                continue

            if replace_all:
                content = content.replace(old_string, new_string)
            else:
                content = content.replace(old_string, new_string, 1)

        with open(file_path, 'w') as file:
            file.write(content)

        return f"Successfully applied multiple edits to {file_path}"
    except Exception as e:
        return (f"Failed to edit file: {str(e)}")

@mcp.tool()
def file_read(
        file_path: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None
) -> str:
    """
    Read a file with optional offset and limit.

    Args:
        file_path (str): The absolute path to the file to read.
        offset (Optional[int]): The line number to start reading from (0-indexed).
        limit (Optional[int]): The number of lines to read.

    Returns:
        str: The content read from the file.

    Note:
        For file formats which are usually large, like logs, consider using offset and limit to avoid reading the entire file.
    """
    rprint(f"[bold blue]Running read_file[/bold blue] on: [yellow]{file_path}[/yellow] with offset = [cyan]{offset}[/cyan] and limit = [cyan]{limit}[/cyan]")
    if not os.path.isfile(file_path):
        return (f"File not found: {file_path}. Recheck the path.")

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        if offset is not None:
            lines = lines[offset:]
        if limit is not None:
            lines = lines[:limit]

        return ''.join(lines)
    except Exception as e:
        return (f"Failed to read file: {str(e)}")

@mcp.tool()
def file_replace(
        file_path: str,
        old_string: str,
        new_string: str,
        replace_all: bool = False
) -> str:
    """
    Replace occurrences of old_string with new_string in a file.

    Args:
        file_path (str): The absolute path to the file to modify.
        old_string (str): The text to replace.
        new_string (str): The text to replace it with.
        replace_all (bool): Replace all occurrences if True, else only the first occurrence.

    Returns:
        str: Success message or error.
    """
    rprint(f"[bold blue]Running replace[/bold blue] on file: [yellow]{file_path}[/yellow] replacing [red]{old_string}[/red] with [green]{new_string}[/green] replace_all = [cyan]{replace_all}[/cyan]")
    # Reuse file_edit logic or just call it? I'll just reimplement to keep it standalone as requested.
    if not os.path.isfile(file_path):
        return (f"File not found: {file_path}. Recheck the path.")

    try:
        with open(file_path, 'r') as file:
            content = file.read()

        if replace_all:
            new_content = content.replace(old_string, new_string)
        else:
            new_content = content.replace(old_string, new_string, 1)

        with open(file_path, 'w') as file:
            file.write(new_content)

        return f"Successfully replaced text in {file_path}"
    except Exception as e:
        return (f"Failed to replace text in file: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Shell Tools MCP Server")
    parser.add_argument("--http", action="store_true", help="Run over HTTP (SSE)")
    parser.add_argument("--port", type=int, default=8000, help="Port for HTTP server")
    args = parser.parse_args()

    if args.http:
        mcp.settings.port = args.port
        mcp.run(transport="http")
    else:
        mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
