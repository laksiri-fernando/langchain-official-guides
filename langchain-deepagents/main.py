# pip install -qU deepagents langchain-google-genai langchain-openrouter tavily-python
# pip install -qU python-dotenv

from deepagents import create_deep_agent
from dotenv import load_dotenv

load_dotenv()

def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    # In a real implementation, this function would call a weather API.
    # For this example, we'll return a dummy weather report.
    return f"The current weather in {city} is sunny with a temperature of 25°C."

agent = create_deep_agent(
    # model="google_genai:gemini-3.5-flash",
    model="openrouter:google/gemma-4-31b-it:free",
    tools=[get_weather],
    system_prompt="You are a helpful assistant that provides weather information based on the get_weather function."
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

# print(result)
print(result["messages"][-1].content_blocks)