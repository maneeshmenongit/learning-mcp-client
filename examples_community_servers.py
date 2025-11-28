"""
Examples of connecting to community MCP servers

This file shows how to connect to various community-built MCP servers
that provide useful tools for different tasks.
"""

import asyncio
from client import MCPClient


async def example_filesystem_server():
    """
    Filesystem MCP Server

    Provides tools for:
    - Reading files
    - Writing files
    - Listing directories
    - Searching files

    Installation:
    npm install -g @modelcontextprotocol/server-filesystem
    """
    client = MCPClient()

    try:
        # Connect to filesystem server (allows access to a specific directory)
        await client.connect_to_server(
            "npx @modelcontextprotocol/server-filesystem /path/to/allowed/directory"
        )

        # Example query: "What files are in this directory?"
        # Example query: "Read the README.md file"
        # Example query: "Search for all Python files containing 'async'"

        await client.chat_loop()

    finally:
        await client.cleanup()


async def example_github_server():
    """
    GitHub MCP Server

    Provides tools for:
    - Creating/updating issues
    - Managing pull requests
    - Searching repositories
    - Reading file contents from repos

    Installation:
    npm install -g @modelcontextprotocol/server-github

    Requires: GITHUB_TOKEN environment variable
    """
    client = MCPClient()

    try:
        await client.connect_to_server(
            "npx @modelcontextprotocol/server-github"
        )

        # Example query: "List all open issues in my repository"
        # Example query: "Create a new issue about improving documentation"
        # Example query: "Show me the content of README.md from the main branch"

        await client.chat_loop()

    finally:
        await client.cleanup()


async def example_postgres_server():
    """
    PostgreSQL MCP Server

    Provides tools for:
    - Executing SQL queries
    - Reading database schemas
    - Managing database connections

    Installation:
    npm install -g @modelcontextprotocol/server-postgres

    Requires: Database connection string
    """
    client = MCPClient()

    try:
        await client.connect_to_server(
            "npx @modelcontextprotocol/server-postgres postgresql://user:pass@localhost/dbname"
        )

        # Example query: "Show me the schema for the users table"
        # Example query: "How many users are in the database?"
        # Example query: "Find all orders from the last 7 days"

        await client.chat_loop()

    finally:
        await client.cleanup()


async def example_slack_server():
    """
    Slack MCP Server (Community)

    Provides tools for:
    - Sending messages to channels
    - Reading channel history
    - Managing conversations

    Note: This is a community server, check GitHub for installation
    """
    client = MCPClient()

    try:
        # Example - actual command depends on the server implementation
        await client.connect_to_server(
            "npx @modelcontextprotocol/server-slack"
        )

        # Example query: "Send a message to #general channel"
        # Example query: "What were the latest messages in #dev-team?"

        await client.chat_loop()

    finally:
        await client.cleanup()


async def example_google_drive_server():
    """
    Google Drive MCP Server (Community)

    Provides tools for:
    - Reading documents
    - Searching files
    - Managing folders

    Note: Check community servers for installation
    """
    client = MCPClient()

    try:
        await client.connect_to_server(
            "path/to/gdrive-server"
        )

        # Example query: "List all documents in my Drive"
        # Example query: "Read the content of 'Project Plan.docx'"

        await client.chat_loop()

    finally:
        await client.cleanup()


async def example_multiple_servers():
    """
    Connect to multiple MCP servers simultaneously

    This requires extending the MCPClient class to handle multiple sessions.
    See the documentation for implementing multi-server support.
    """
    # TODO: Implement multi-server client
    pass


# Example usage
if __name__ == "__main__":
    print("Community MCP Server Examples")
    print("=" * 60)
    print("\n1. Filesystem Server - File operations")
    print("2. GitHub Server - GitHub API integration")
    print("3. PostgreSQL Server - Database queries")
    print("4. Slack Server - Slack messaging")
    print("5. Google Drive Server - Document access")
    print("\nEdit this file and uncomment the example you want to try!")
    print("\nNote: Make sure to install the required servers first:")
    print("  npm install -g @modelcontextprotocol/server-<name>")

    # Uncomment the example you want to run:
    # asyncio.run(example_filesystem_server())
    # asyncio.run(example_github_server())
    # asyncio.run(example_postgres_server())
