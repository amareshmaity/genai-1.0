from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini-2025-04-14",
    input="what is the use of ai"
)

print(response.output_text)