"""A simple example of using LangChain with Ollama LLMs."""

# pip install langchain
# pip install langchain-ollama

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

template = """You are a helpful AI assistant. Provide a concise answer to the following question.
Question: {question}"""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="gemma3:4b")

chain = prompt | model

# result = chain.invoke({"question": "What is LangChain?"})
result = chain.invoke({"question": "what is the weather in sf?"})

print(result)