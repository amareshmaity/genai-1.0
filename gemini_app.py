from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

responses = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is genai?"
)

print(responses.output_text)