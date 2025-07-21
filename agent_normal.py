import os
import json
import logging
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import asyncio
from browser_use.llm import ChatOpenAI
from browser_use import Agent

from browser_use.llm import ChatOllama,ChatGroq
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()
# Azure setup
llm = ChatGroq(model="meta-llama/llama-4-maverick-17b-128e-instruct")

async def main():
    agent = Agent(
        task="go to google and Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())