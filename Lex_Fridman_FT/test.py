import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


## Example of using OpenRouter API for DeepSeek Chat (free)
# response_chat = requests.post(
#   url="https://openrouter.ai/api/v1/chat/completions",
#   headers={
#     "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
#   },
#   data=json.dumps({
#     "model": "deepseek/deepseek-chat:free", # Optional
#     "messages": [
#       {"role": "user", "content": "What is the meaning of life?"}
#     ],
#     "top_p": 1,
#     "temperature": 1,
#     "frequency_penalty": 0,
#     "presence_penalty": 0,
#     "repetition_penalty": 1,
#     "top_k": 0,
#   })
# )


## Example of using OpenRouter API for DeepSeek R1 (free)
response_r1 = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
  },
  data=json.dumps({
    "model": "deepseek/deepseek-r1-distill-llama-70b:free", # Optional
    "messages": [
      {"role": "user", "content": "What is the meaning of life?"}
    ]
  })
)


# print(response_chat.json())
print(response_r1.json())