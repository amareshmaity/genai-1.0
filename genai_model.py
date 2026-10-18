from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)

# Input and prompt
prompt = """
Explain Generative AI to a beginner in three bullet points.
"""

responses = client.responses.create(
    model="gpt-4.1-nano",
    input = prompt
)

print(responses.output_text)