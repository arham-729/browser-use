import asyncio
from browser_use import BrowserSession, Agent
from browser_use.llm import ChatGroq
from dotenv import load_dotenv
load_dotenv()

# ✅ Step 1: Define the LLM (Groq + LLaMA 4 Maverick)
llm = ChatGroq(model="meta-llama/llama-4-maverick-17b-128e-instruct")

# ✅ Step 2: Define the browser profile path (for session persistence)
PROFILE_DIR = "./browser_profiles/github_login_session"

# ✅ Step 3: Main async function
async def main():
    # Step 3.1: Create a browser session (non-headless, custom size, persistent profile)
    browser_session = BrowserSession(
        headless=False,  # So you can see browser window
        viewport={'width': 1200, 'height': 800},  # Desktop-like dimensions
        user_data_dir=PROFILE_DIR,  # Save cookies/session here
    )

    # Step 3.2: Define a clear natural language task
    task = (
        "Go to https://github.com/login. "
        "If not logged in, prompt the user to log in manually. "
        "Once logged in, go to https://github.com and check if the profile icon is visible to confirm login success."
    )

    # Step 3.3: Initialize the Agent with LLM + browser session
    agent = Agent(
        task=task,
        llm=llm,
        browser_session=browser_session,
    )

    # Step 3.4: Run the agent and print results
    result = await agent.run()
    print("\n✅ AGENT RESULT:\n", result)

# ✅ Step 4: Launch everything
asyncio.run(main())
