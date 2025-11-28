import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


class EnhancedMCPClient:
    """Enhanced MCP Client that supports both Python and Node.js servers"""

    def __init__(self):
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.anthropic = Anthropic()

    async def connect_to_server(
        self, command: str, args: list[str] = None, env: dict = None
    ):
        """Connect to an MCP server (Python or Node.js)

        Args:
            command: The command to run (e.g., "python", "node", "npx")
            args: List of arguments (e.g., ["server.py"] or ["@modelcontextprotocol/server-filesystem", "/path"])
            env: Optional environment variables
        """
        if args is None:
            args = []

        server_params = StdioServerParameters(command=command, args=args, env=env)

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

    async def connect_to_python_server(self, script_path: str):
        """Helper: Connect to a Python MCP server"""
        return await self.connect_to_server("python", [script_path])

    async def connect_to_node_server(self, package: str, *args):
        """Helper: Connect to a Node.js MCP server via npx

        Args:
            package: NPM package name (e.g., "@modelcontextprotocol/server-filesystem")
            *args: Additional arguments (e.g., directory paths, config)
        """
        return await self.connect_to_server("npx", [package, *args])

    async def process_query(self, query: str):
        """Process a query using Claude and available MCP tools"""
        messages = [{"role": "user", "content": query}]

        response = await self.session.list_tools()
        available_tools = [
            {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.inputSchema,
            }
            for tool in response.tools
        ]

        print(f"\n{'='*60}")
        print(f"User Query: {query}")
        print(f"{'='*60}\n")

        while True:
            claude_response = self.anthropic.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=4096,
                messages=messages,
                tools=available_tools,
            )

            messages.append({"role": "assistant", "content": claude_response.content})

            if claude_response.stop_reason == "tool_use":
                tool_results = []

                for content_block in claude_response.content:
                    if content_block.type == "tool_use":
                        tool_name = content_block.name
                        tool_args = content_block.input

                        print(f"🔧 Claude is using tool: {tool_name}")
                        print(f"   Arguments: {tool_args}\n")

                        result = await self.session.call_tool(tool_name, tool_args)

                        tool_results.append(
                            {
                                "type": "tool_result",
                                "tool_use_id": content_block.id,
                                "content": result.content,
                            }
                        )

                messages.append({"role": "user", "content": tool_results})

            elif claude_response.stop_reason == "end_turn":
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
        print("\n" + "=" * 60)
        print("MCP Client Started - Type your queries (or 'quit' to exit)")
        print("=" * 60 + "\n")

        while True:
            try:
                query = input("You: ").strip()

                if query.lower() in ["quit", "exit", "q"]:
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
