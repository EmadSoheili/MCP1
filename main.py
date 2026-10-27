from dotenv import load_dotenv
load_dotenv()

import asyncio
from mcp import ClientSession, StdioServerParameters
        # ClientSession provides framework for Python application to act as an MCP client. 
                # It is responsible for connecting to the MCP server and sending/receiving messages.
        # StdioServerParameters provides a way to connect to the MCP server via stdin/stdout. (How to run the MCP server).
from mcp.client.stdio import stdio_client       # To communicate with MCP servers through transporting input and output (read and write)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.tools import load_mcp_tools       # Take tools exposed through MCP servers and transform it to LangChain tools.
from langchain.agents import create_agent
from pathlib import Path        # To add the relative path instead of the absolute path.


MODEL="gemini-3.5-flash"
llm = ChatGoogleGenerativeAI(model=MODEL)


BASE_DIR = Path(__file__).resolve().parent      # Point to the directory where the file lives


stdio_server_params = StdioServerParameters(    # It will hold information on how to run the MCP server
        command = "python",
        args = [str(BASE_DIR / "servers" / "math_server.py")]
)


async def main():
    print("Hello, MCP!")


if __name__ == "__main__":
    asyncio.run(main())