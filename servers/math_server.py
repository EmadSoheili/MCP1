# math_server.py
# This server is used to perform mathematical operations
from mcp.server.fastmcp import FastMCP      # To create the MCP server


# Create the MCP server
mcp = FastMCP("Math")


# Define the tools
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


if __name__ == "__main__":
    mcp.run(transport="stdio")      # Run the MCP server using stdio
            # STDIO is a standard input/output stream that allows the MCP server to be run in a terminal
            # This is for the cases that we create our own tools or for testing purposes