# MCP-Server-Employee-Performance-Tracking

A Model Context Protocol (MCP) server for tracking employee feature assignments and completion status.

## Quick Start

### 1. Project Setup
Create project and install dependencies:
- `uv init project-name`
- `cd project-name`
- `uv add "mcp[cli]"`
- `pip install "mcp[cli]"`

### 2. Implementation
- Server logic is implemented in `server.py`
- Entry point is `main.py`

### 3. Installation
Install the MCP server:
- `uv run mcp install server.py`

This command registers the MCP server, allowing MCP clients like Claude Desktop (used for this project) to consume the defined tools.

## Tools (functionalities)

The server provides three tools:

- **Get Current Feature** - Fetch the current feature being worked on by an employee
- **Get Completed Features** - Get the count of completed features for an employee  
- **Update Current Feature** - Reassign employee's current assignment and mark previous as complete
