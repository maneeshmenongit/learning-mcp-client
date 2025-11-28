# MCP Client Tutorial

A beginner-friendly introduction to building MCP (Model Context Protocol) clients.

## What is MCP?

MCP (Model Context Protocol) allows AI models like Claude to connect to external tools and data sources. This project demonstrates:
- How to build an MCP client in Python
- How to connect to MCP servers
- How to let Claude use tools through MCP

## Project Structure

- `client.py` - The MCP client implementation
- `simple_server.py` - A sample MCP server with calculator tools
- `main.py` - Entry point to run the client

## Setup

1. Install dependencies:
```bash
uv pip install mcp anthropic python-dotenv
```

2. Make sure you have a `.env` file with your Anthropic API key:
```bash
ANTHROPIC_API_KEY=your_actual_key_here
```

## Running the Client

```bash
python main.py
```

This will:
1. Connect to the simple calculator MCP server
2. Start an interactive chat loop
3. Let you ask Claude questions that require using the calculator tools

## Example Queries

Try asking:
- "What is 42 plus 58?"
- "Multiply 7 by 8"
- "Please greet Alice"
- "Add 15 and 20, then multiply the result by 3"

## How It Works

1. **Client connects** to the MCP server (`simple_server.py`)
2. **Server advertises** its available tools (add, multiply, greet)
3. **You ask a question** through the client
4. **Claude decides** if it needs to use any tools
5. **Client executes** the tool on the server
6. **Claude formulates** a final answer using the tool results

## Key Components

### MCPClient (client.py)

- `connect_to_server()` - Establishes connection to an MCP server
- `process_query()` - The "agentic loop" that handles Claude's tool usage
- `chat_loop()` - Interactive interface for asking questions

### Simple Server (simple_server.py)

- Implements basic tools: add, multiply, greet
- Shows the server-side structure of MCP

## Next Steps

- Try creating your own MCP server with different tools
- Connect to existing MCP servers (file system, databases, APIs)
- Extend the client to handle multiple servers simultaneously

## Authentication Setup

This project is configured with SSH authentication for GitHub.
