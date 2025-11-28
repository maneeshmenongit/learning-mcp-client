import asyncio
from client import MCPClient


async def main():
    """Main entry point for the MCP client"""
    client = MCPClient()

    try:
        # Connect to the simple calculator server
        print("Connecting to MCP server...")
        await client.connect_to_server("simple_server.py")

        # Start the interactive chat loop
        await client.chat_loop()

    finally:
        # Clean up resources
        await client.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
