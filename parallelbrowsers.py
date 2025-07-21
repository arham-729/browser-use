import asyncio
from browser_use import BrowserSession, BrowserProfile, Agent
from browser_use.llm import ChatGroq
from playwright.async_api import async_playwright
from dotenv import load_dotenv
load_dotenv()


import asyncio
from browser_use.llm import ChatGroq  # ✅ Your LLaMA-4 Maverick LLM
from browser_use import Agent, BrowserProfile, BrowserSession
from playwright.sync_api import sync_playwright  # For device descriptor access

# 🤖 LLM using Groq LLaMA-4 Maverick
llm = ChatGroq(model="meta-llama/llama-4-maverick-17b-128e-instruct")

# ✅ Shared mobile browser profile: iPhone 13
device_descriptor = sync_playwright().start().devices["iPhone 13"]
base_iphone13 = BrowserProfile(
    storage_state='/tmp/auth.json',  # Shared cookies
    **device_descriptor,
    timezone_id='UTC',              # Base timezone
)

# ✅ Browser sessions with different timezones
usa_browser = BrowserSession(
    browser_profile=base_iphone13,
    timezone_id='America/New_York',  # 🇺🇸 Eastern Time
)

eu_browser = BrowserSession(
    browser_profile=base_iphone13,
    timezone_id='Europe/Paris',      # 🇫🇷 Central European Time
)

# ✅ Two agents in different regions
usa_agent = Agent(
    task="What time is it currently according to your browser?",
    llm=llm,
    browser_session=usa_browser,
)

eu_agent = Agent(
    task="What time is it currently according to your browser?",
    llm=llm,
    browser_session=eu_browser,
)

# ✅ Run both agents in parallel and display output
async def main():
    await asyncio.gather(
        usa_agent.run(),
        eu_agent.run()
    )

# Run async code (Jupyter: use `await main()` instead)
asyncio.run(main())
