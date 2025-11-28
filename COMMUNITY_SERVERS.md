# Community MCP Servers Guide

This guide shows how to connect to popular community MCP servers for your projects.

## Quick Start

1. **Install Node.js** (if not already installed):
   ```bash
   brew install node
   ```

2. **Install an MCP server**:
   ```bash
   npm install -g @modelcontextprotocol/server-filesystem
   ```

3. **Run the demo**:
   ```bash
   python demo_filesystem.py
   ```

## Popular MCP Servers

### 1. Filesystem Server (Most Useful!)

**What it does**: Read, write, search files in a directory

**Install**:
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Use cases**:
- Code reviews: "Review all Python files"
- Documentation: "Summarize all markdown files"
- Search: "Find all TODOs in the code"
- Analysis: "Show files that use asyncio"

**Run**:
```bash
python demo_filesystem.py
```

**Example queries**:
- "What files are in this directory?"
- "Read client.py and suggest improvements"
- "Find all files containing 'MCP'"

---

### 2. GitHub Server

**What it does**: Interact with GitHub repositories

**Install**:
```bash
npm install -g @modelcontextprotocol/server-github
```

**Setup**: Add `GITHUB_TOKEN` to `.env` (get from https://github.com/settings/tokens/new)

**Use cases**:
- Issue management
- Pull request reviews
- Repository analysis
- Commit history

**Run**:
```bash
python demo_github.py
```

**Example queries**:
- "List all open issues"
- "Create an issue about improving docs"
- "Show me recent commits"

---

### 3. PostgreSQL Server

**What it does**: Query and analyze PostgreSQL databases

**Install**:
```bash
npm install -g @modelcontextprotocol/server-postgres
```

**Use cases**:
- Database queries: "How many users signed up today?"
- Schema exploration: "Show me the users table structure"
- Data analysis: "What's the average order value?"

**Example**:
```python
from enhanced_client import EnhancedMCPClient

client = EnhancedMCPClient()
await client.connect_to_node_server(
    "@modelcontextprotocol/server-postgres",
    "postgresql://user:pass@localhost/dbname"
)
```

---

### 4. Brave Search Server

**What it does**: Web search using Brave Search API

**Install**:
```bash
npm install -g @modelcontextprotocol/server-brave-search
```

**Setup**: Get API key from https://brave.com/search/api/

**Use cases**:
- Research: "Search for latest MCP tutorials"
- Documentation: "Find Python async best practices"
- Current events: "What's new in AI this week?"

---

### 5. Memory Server

**What it does**: Persistent memory across conversations

**Install**:
```bash
npm install -g @modelcontextprotocol/server-memory
```

**Use cases**:
- Remember user preferences
- Track conversation context
- Store project-specific information

---

### 6. Puppeteer Server

**What it does**: Browser automation and web scraping

**Install**:
```bash
npm install -g @modelcontextprotocol/server-puppeteer
```

**Use cases**:
- Web scraping
- Screenshot generation
- Form automation
- Testing

---

## Creating Custom Connections

### Connect to Any Node.js Server

```python
from enhanced_client import EnhancedMCPClient

client = EnhancedMCPClient()

# Connect using npx
await client.connect_to_node_server(
    "@modelcontextprotocol/server-name",
    "arg1",
    "arg2"
)
```

### Connect to Python Server

```python
from enhanced_client import EnhancedMCPClient

client = EnhancedMCPClient()

# Connect to Python server
await client.connect_to_python_server("path/to/server.py")
```

### Connect with Custom Command

```python
from enhanced_client import EnhancedMCPClient

client = EnhancedMCPClient()

# Connect with any command
await client.connect_to_server(
    command="node",
    args=["server.js", "--port", "3000"],
    env={"API_KEY": "your-key"}
)
```

---

## Real Project Examples

### Example 1: Code Review Tool

```python
# review_code.py
import asyncio
from enhanced_client import EnhancedMCPClient

async def main():
    client = EnhancedMCPClient()

    # Connect to filesystem
    await client.connect_to_node_server(
        "@modelcontextprotocol/server-filesystem",
        "/path/to/project"
    )

    # Ask Claude to review
    await client.process_query(
        "Review all Python files for: "
        "1. Code quality issues "
        "2. Security vulnerabilities "
        "3. Performance problems"
    )

    await client.cleanup()

asyncio.run(main())
```

### Example 2: Database Analysis

```python
# analyze_db.py
import asyncio
from enhanced_client import EnhancedMCPClient

async def main():
    client = EnhancedMCPClient()

    await client.connect_to_node_server(
        "@modelcontextprotocol/server-postgres",
        "postgresql://localhost/mydb"
    )

    await client.process_query(
        "Analyze the users table and tell me: "
        "1. Total user count "
        "2. Users created in the last week "
        "3. Most common registration sources"
    )

    await client.cleanup()

asyncio.run(main())
```

### Example 3: GitHub Issue Manager

```python
# manage_issues.py
import asyncio
from enhanced_client import EnhancedMCPClient

async def main():
    client = EnhancedMCPClient()

    await client.connect_to_node_server(
        "@modelcontextprotocol/server-github"
    )

    await client.process_query(
        "Review all open issues and: "
        "1. Group them by category "
        "2. Identify duplicates "
        "3. Suggest priorities"
    )

    await client.cleanup()

asyncio.run(main())
```

---

## Finding More Servers

- **Official servers**: https://github.com/modelcontextprotocol/servers
- **Community servers**: Search GitHub for "mcp-server"
- **MCP Registry**: https://mcp-get.com (community registry)

---

## Troubleshooting

### Server Won't Connect

1. Check Node.js is installed: `node --version`
2. Check server is installed: `npm list -g @modelcontextprotocol/server-NAME`
3. Check environment variables in `.env`

### Permission Errors

- Filesystem: Make sure the path exists and is readable
- GitHub: Check token has correct scopes
- Database: Verify connection string

### Tools Not Showing Up

- Check server logs for errors
- Verify server initialization completed
- Try running server manually: `npx @modelcontextprotocol/server-NAME`

---

## Next Steps

1. **Try the filesystem demo**: `python demo_filesystem.py`
2. **Set up GitHub integration**: Add GITHUB_TOKEN and run `demo_github.py`
3. **Create a custom server** for your specific needs
4. **Combine multiple servers** for complex workflows

Happy building! 🚀
