#!/usr/bin/env python3
"""
Filesystem MCP Server Example

This demonstrates connecting to the official MCP filesystem server,
which gives Claude the ability to read/write files in a specified directory.

Installation:
1. Install the server: npm install -g @modelcontextprotocol/server-filesystem
2. Run this script: python filesystem_example.py

Use cases:
- Code reviews: "Review all Python files in this directory"
- Documentation: "Read all markdown files and summarize the project"
- Refactoring: "Find all TODO comments in the codebase"
- Analysis: "Show me all files that import pandas"
"""

import asyncio
import os
from client import MCPClient


async def main():
    """Connect to filesystem server and start interactive session"""
    client = MCPClient()

    try:
        # Get the current directory as the allowed path
        current_dir = os.getcwd()

        print(f"\n{'='*60}")
        print(f"Filesystem MCP Server Example")
        print(f"{'='*60}")
        print(f"\nAllowed directory: {current_dir}")
        print(f"\nClaude will be able to:")
        print(f"  - Read files in this directory")
        print(f"  - List directory contents")
        print(f"  - Search for files")
        print(f"  - Get file information")
        print(f"\nNote: The server restricts access to only this directory for security.")
        print(f"{'='*60}\n")

        # Connect to the filesystem server
        # The server is installed via npm and runs as a subprocess
        print("Connecting to filesystem MCP server...")

        # Note: Modify connect_to_server to accept command + args
        # For now, this shows the concept
        server_command = f"npx @modelcontextprotocol/server-filesystem {current_dir}"

        print(f"Server command: {server_command}")
        print("\nTry asking:")
        print('  - "What files are in this directory?"')
        print('  - "Read the README.md file"')
        print('  - "Show me all Python files"')
        print('  - "Search for files containing \'async\'"')
        print()

        # This would need the client to support non-Python servers
        # await client.connect_to_server(server_command)
        # await client.chat_loop()

        print("NOTE: To use Node.js MCP servers, you need to modify the client")
        print("to support different command types (not just Python scripts).")
        print("\nSee the enhanced_client.py example for a working implementation.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        await client.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
