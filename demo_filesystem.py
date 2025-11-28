#!/usr/bin/env python3
"""
Filesystem MCP Server Demo

This connects to the official filesystem MCP server and lets you
interact with files using natural language.

Setup:
1. Install Node.js (if not installed): brew install node
2. Install the server: npm install -g @modelcontextprotocol/server-filesystem
3. Run: python demo_filesystem.py

Example queries:
- "What files are in this directory?"
- "Read the README.md file"
- "Find all Python files"
- "Show me the content of client.py"
- "List all files that contain 'MCP' in their name"
"""

import asyncio
import os
from enhanced_client import EnhancedMCPClient


async def main():
    client = EnhancedMCPClient()

    try:
        current_dir = os.getcwd()

        print(f"\n{'='*60}")
        print(f"Filesystem MCP Server Demo")
        print(f"{'='*60}")
        print(f"\nAllowed directory: {current_dir}")
        print(f"\nInstalling the server if needed...")
        print(f"Run: npm install -g @modelcontextprotocol/server-filesystem")
        print(f"{'='*60}\n")

        # Connect to filesystem server
        # The server will only have access to the current directory
        await client.connect_to_node_server(
            "@modelcontextprotocol/server-filesystem", current_dir
        )

        # Start interactive chat
        await client.chat_loop()

    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure you have:")
        print("1. Node.js installed: brew install node")
        print(
            "2. Filesystem server installed: npm install -g @modelcontextprotocol/server-filesystem"
        )
    finally:
        await client.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
