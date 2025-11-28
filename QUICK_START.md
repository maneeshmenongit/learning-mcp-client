# Quick Start Guide

## Run the Basic Example (5 minutes)

```bash
# 1. Make sure you're in the project directory
cd /Users/maneeshmenon/PycharmProjects/mcp-client

# 2. Run the simple calculator demo
python main.py
```

Try asking:
- "What is 42 plus 58?"
- "Multiply 7 by 8, then add 10"

Type `quit` to exit.

---

## Try Community Servers (10 minutes)

### Option 1: Filesystem Server (Recommended First)

**Install**:
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Run**:
```bash
python demo_filesystem.py
```

**Try**:
- "What files are in this directory?"
- "Read the README.md file"
- "Find all Python files"

### Option 2: GitHub Server

**Setup**:
1. Get token: https://github.com/settings/tokens/new (needs 'repo' scope)
2. Add to `.env`: `GITHUB_TOKEN=your_token`
3. Install: `npm install -g @modelcontextprotocol/server-github`

**Run**:
```bash
python demo_github.py
```

**Try**:
- "List my repositories"
- "Show open issues in learning-mcp-client"

---

## For Your Other Projects

### Use Case: Code Review

```python
from enhanced_client import EnhancedMCPClient
import asyncio

async def review_project():
    client = EnhancedMCPClient()

    # Point to your project directory
    await client.connect_to_node_server(
        "@modelcontextprotocol/server-filesystem",
        "/path/to/your/project"
    )

    await client.process_query(
        "Review all Python files and suggest improvements"
    )

    await client.cleanup()

asyncio.run(review_project())
```

### Use Case: Database Analysis

```python
from enhanced_client import EnhancedMCPClient
import asyncio

async def analyze_db():
    client = EnhancedMCPClient()

    await client.connect_to_node_server(
        "@modelcontextprotocol/server-postgres",
        "postgresql://user:pass@localhost/dbname"
    )

    await client.process_query(
        "Show me statistics about user signups this month"
    )

    await client.cleanup()

asyncio.run(analyze_db())
```

### Use Case: GitHub Automation

```python
from enhanced_client import EnhancedMCPClient
import asyncio

async def manage_issues():
    client = EnhancedMCPClient()

    await client.connect_to_node_server(
        "@modelcontextprotocol/server-github"
    )

    await client.process_query(
        "Create an issue titled 'Add unit tests' with a detailed description"
    )

    await client.cleanup()

asyncio.run(manage_issues())
```

---

## Available Servers

| Server | Install Command | Use For |
|--------|----------------|---------|
| Filesystem | `npm install -g @modelcontextprotocol/server-filesystem` | File operations |
| GitHub | `npm install -g @modelcontextprotocol/server-github` | GitHub management |
| PostgreSQL | `npm install -g @modelcontextprotocol/server-postgres` | Database queries |
| Brave Search | `npm install -g @modelcontextprotocol/server-brave-search` | Web search |
| Puppeteer | `npm install -g @modelcontextprotocol/server-puppeteer` | Browser automation |

See [COMMUNITY_SERVERS.md](COMMUNITY_SERVERS.md) for full list and details.

---

## Troubleshooting

**"npm: command not found"**
```bash
brew install node
```

**"Server won't connect"**
```bash
# Check if server is installed
npm list -g @modelcontextprotocol/server-filesystem

# Reinstall if needed
npm install -g @modelcontextprotocol/server-filesystem
```

**"GITHUB_TOKEN not found"**
1. Create token: https://github.com/settings/tokens/new
2. Add to `.env` file:
   ```
   GITHUB_TOKEN=your_token_here
   ```

---

## Next Steps

1. ✅ Try the basic calculator demo
2. ✅ Install and try filesystem server
3. ✅ Read [COMMUNITY_SERVERS.md](COMMUNITY_SERVERS.md)
4. 🎯 Build your own MCP server
5. 🎯 Combine multiple servers for complex workflows

Happy coding! 🚀
