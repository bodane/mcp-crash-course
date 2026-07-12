import asyncio
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command="python",
    args={r"E:\Training\MCP Crash Course - Complete Model Context Protocol in a Day\Section_6\39\mcp-crash-course\servers\math_server.py"},
)

async def main():
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
    asyncio.run(main())
