from langchain.agents import create_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="ollama:gpt-oss:20b-cloud",
    tools=[get_weather],
    system_prompt="You are a helpful assistant. Provide concise answers to user questions. Start with a greetings.",
)

# Run the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

# print(response)
print(response["messages"][2])