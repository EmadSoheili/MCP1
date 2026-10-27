# langchain_client.py
# This is to ...


from dotenv import load_dotenv  
load_dotenv()

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
import asyncio


MODEL="gemini-3.5-flash"
llm = ChatGoogleGenerativeAI(model=MODEL)


async def main():
    print("Hello Langchian MCP!")


if __name__ == "__main__":
    asyncio.run(main())