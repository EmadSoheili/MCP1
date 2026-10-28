from dotenv import load_dotenv
load_dotenv()

import asyncio
from mcp import ClientSession, StdioServerParameters
        # ClientSession provides framework for Python application to act as an MCP client. 
                # It is responsible for connecting to the MCP server and sending/receiving messages.
        # StdioServerParameters provides a way to connect to the MCP server via stdin/stdout. (How to run the MCP server).
from mcp.client.stdio import stdio_client       # To communicate with MCP servers through transporting input and output (read and write)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools       # Take tools exposed through MCP servers and transform it to LangChain tools.
from langchain.agents import create_agent
from pathlib import Path        # To add the relative path instead of the absolute path.


MODEL="gemini-3.5-flash"
llm = ChatGoogleGenerativeAI(model=MODEL)


BASE_DIR = Path(__file__).resolve().parent      # Point to the directory where the file lives


# Define the stdio server parameters. It will hold information on how to run the MCP server.
# Object itself (stdio) defines the way of communication, and the parameters are what is needed to run the MCP server.
stdio_server_params = StdioServerParameters(
        command = "python",
        args = [str(BASE_DIR / "servers" / "math_server.py")]
)


async def main():

        # stdio context manager. Pass the stdio server params to the client and get back the read and write.
        # This is for telling the client how to connect to server to communicate.
        async with stdio_client(stdio_server_params) as (read, write):

                # Create the client session and feed the read and write to it. Then get the session from it.
                # Session is handling all the communication.
                async with ClientSession(read_stream=read, write_stream=write) as session:

                        # Initialize the session
                        await session.initialize()
                        print("---Session Initialized---")

                        # Get the list of available tools
                        tools = await load_mcp_tools(session)
                        print("---Getting Available Tools---")
                        #print(tools)

                        # Create Langchain ReAct agent to use this tool and decide what to do with it.
                        agent = create_agent(llm, tools)

                        # Invoke the LLM
                        result = await agent.ainvoke({"messages": [HumanMessage(content = "What is 54 + 2 * 3?")]})
                        print("---Answer---")
                        print(result["messages"][-1].text)


if __name__ == "__main__":
    asyncio.run(main())