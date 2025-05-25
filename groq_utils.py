import os
from typing import List
from groq import Groq

from dotenv import load_dotenv
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def init_groq_client():
    """Initialize and return a Groq client using the API key from environment variables."""
    return client

def get_natural_language_response(prompt: str, model: str = "llama3-8b-8192") -> str:
    """Query the Groq model and return the response in natural language."""
    client = init_groq_client()
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
        stream=False,
    )
    return chat_completion.choices[0].message.content
