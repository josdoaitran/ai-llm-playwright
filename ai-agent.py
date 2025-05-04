from browser_use import Agent
from langchain_openai import ChatOpenAI
import asyncio

agent = Agent(
    task="Find the latest news about generative AI and summarize it in 3 sentences.",
    llm=ChatOpenAI(model="gpt-4o")
)
async def main():
    result = await agent.run()
    print(result)
asyncio.run(main())