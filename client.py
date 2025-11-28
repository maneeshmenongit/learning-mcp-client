import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env

class MCPClient:
    def __init__(self):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.anthropic = Anthropic()

    async def connect_to_server(self, server_script_path: str):
        """Connect to an MCP server

        Args:
            server_script_path: Path to the server script (e.g., "path/to/server.py")
        """
        server_params = StdioServerParameters(
            command="python",
            args=[server_script_path],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(
            stdio_client(server_params)
        )
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(
            ClientSession(self.stdio, self.write)
        )

        await self.session.initialize()

        # List available tools
        response = await self.session.list_tools()
        tools = response.tools
        print(f"\nConnected to server with {len(tools)} tools:")
        for tool in tools:
            print(f"  - {tool.name}: {tool.description}")

        return tools

    async def process_query(self, query: str):
        """Process a query using Claude and available MCP tools

        Args:
            query: The user's question or request
        """
        messages = [{"role": "user", "content": query}]

        # Get available tools from the MCP server
        response = await self.session.list_tools()
        available_tools = [
            {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.inputSchema
            }
            for tool in response.tools
        ]

        print(f"\n{'='*60}")
        print(f"User Query: {query}")
        print(f"{'='*60}\n")

        # Agentic loop - let Claude use tools as needed
        while True:
            # Call Claude with the current messages and available tools
            # Use alias for latest version (or use "claude-sonnet-4-5-20250929" to pin a specific version)
            claude_response = self.anthropic.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=4096,
                messages=messages,
                tools=available_tools
            )

            # Add Claude's response to messages
            messages.append({
                "role": "assistant",
                "content": claude_response.content
            })

            # Check if Claude wants to use any tools
            if claude_response.stop_reason == "tool_use":
                # Process all tool calls
                tool_results = []

                for content_block in claude_response.content:
                    if content_block.type == "tool_use":
                        tool_name = content_block.name
                        tool_args = content_block.input

                        print(f"🔧 Claude is using tool: {tool_name}")
                        print(f"   Arguments: {tool_args}\n")

                        # Execute the tool via MCP
                        result = await self.session.call_tool(tool_name, tool_args)

                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": content_block.id,
                            "content": result.content
                        })

                # Add tool results to messages
                messages.append({
                    "role": "user",
                    "content": tool_results
                })

            elif claude_response.stop_reason == "end_turn":
                # Claude is done, extract the final response
                final_response = ""
                for content_block in claude_response.content:
                    if hasattr(content_block, "text"):
                        final_response += content_block.text

                print(f"\n{'='*60}")
                print(f"Claude's Response:")
                print(f"{'='*60}")
                print(final_response)
                print(f"{'='*60}\n")

                return final_response

    async def chat_loop(self):
        """Interactive chat loop"""
        print("\n" + "="*60)
        print("MCP Client Started - Type your queries (or 'quit' to exit)")
        print("="*60 + "\n")

        while True:
            try:
                query = input("You: ").strip()

                if query.lower() in ['quit', 'exit', 'q']:
                    print("\nGoodbye!")
                    break

                if not query:
                    continue

                await self.process_query(query)

            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break

    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()