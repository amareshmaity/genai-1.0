## https://github.com/ollama/ollama-python
from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(
  model='llama3.1:8b',
  messages=[
    {
      'role': 'user',
      'content': 'Why is the sky blue?',
    },
  ],
)
print(response)
print("\n\n")

print(response['message'])
# or access fields directly from the response object
print("\n\n")
print(response.message.content)