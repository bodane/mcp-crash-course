import asyncio
import os

from dotenv import load_dotenv
from langchain_ollama import ChatOllama
#from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatOllama(model="hf.co/lthn/lemma:Q4_K_M") 
#llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command="python",
    args={r"E:\Training\MCP Crash Course - Complete Model Context Protocol in a Day\Section_6\39\mcp-crash-course\servers\math_server.py"},
)

async def main():
    async with stdio_client(stdio_server_params) as (read,write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("session initialized")
            tools = await load_mcp_tools(session)

            
            agent = create_agent(llm,tools)

            result = await agent.ainvoke({"messages": [HumanMessage(content="Using the math tool, what is 54 + 2 * 3?")]})
            print(result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
