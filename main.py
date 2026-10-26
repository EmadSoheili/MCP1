from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    print("Hello, MCP!")


if __name__ == "__main__":
    asyncio.run(main())