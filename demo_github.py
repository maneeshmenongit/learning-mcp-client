#!/usr/bin/env python3
"""
GitHub MCP Server Demo

Connect to the official GitHub MCP server to interact with GitHub using natural language.

Setup:
1. Install: npm install -g @modelcontextprotocol/server-github
2. Get GitHub token: https://github.com/settings/tokens/new
   - Scopes needed: repo, read:org, read:user
3. Add to .env: GITHUB_TOKEN=your_token_here
4. Run: python demo_github.py

Example queries:
- "List my repositories"
- "Show me open issues in learning-mcp-client"
- "Create an issue: Add error handling to client.py"
- "What are the latest commits in this repo?"
- "Show me pull requests that need review"
"""

import asyncio
import os
from enhanced_client import EnhancedMCPClient


async def main():
    client = EnhancedMCPClient()

    try:
        print(f"\n{'='*60}")
        print(f"GitHub MCP Server Demo")
        print(f"{'='*60}")

        # Check for GitHub token
        github_token = os.getenv("GITHUB_TOKEN")
        if not github_token:
            print("\n⚠️  GITHUB_TOKEN not found in environment!")
            print("\nSetup instructions:")
            print("1. Go to: https://github.com/settings/tokens/new")
            print("2. Create a token with 'repo' scope")
            print("3. Add to .env file: GITHUB_TOKEN=your_token_here")
            print(
                "4. Install server: npm install -g @modelcontextprotocol/server-github"
            )
            return

        print(f"\n✓ GitHub token found")
        print(
            f"\nInstall the server if needed: npm install -g @modelcontextprotocol/server-github"
        )
        print(f"{'='*60}\n")

        # Connect to GitHub server
        await client.connect_to_node_server("@modelcontextprotocol/server-github")

        # Start interactive chat
        await client.chat_loop()

    except Exception as e:
        print(f"\nError: {e}")
        print("\nTroubleshooting:")
        print("1. Check GITHUB_TOKEN is in .env")
        print("2. Install: npm install -g @modelcontextprotocol/server-github")
        print("3. Verify Node.js is installed: node --version")
    finally:
        await client.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
