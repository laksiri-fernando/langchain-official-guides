
""" 
Quickstart example for using LangChain Agents with Anthropic Claude Sonnet model.
"""

# pip install -U langchain
# pip install -U langchain-anthropic
# pip install -U python-dotenv
# pip install -U langchain-openai
# pip install -U langchain-ollama
# pip install -U langchain-google-genai

from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    # model="anthropic:claude-sonnet-4-5",
    # model="openai:gpt-5.5",
    model="google_genai:gemini-2.5-flash-lite",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in San Francisco?"}]}
)

print(result["messages"][-1].content_blocks)