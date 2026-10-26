# weather_server.py
# This server is used to get the weather for a given location
from typing import List     # To define the type of the location
from mcp.server.fastmcp import FastMCP      # To create the MCP server


# Create the MCP server
mcp = FastMCP("Weather")


# Define the tools
@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    return "Hot as hell"


if __name__ == "__main__":
    mcp.run(transport="sse")
            # SSE is a server-sent events stream that allows the MCP server to be run in a browser
            # This is for cases that we want to run the MCP server over the internet (via a web browser)