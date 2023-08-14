import os
from dotenv import load_dotenv
import openai

# Load credentuals
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

prompt = "Tell me a joke"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", 
     "content": "You are a helpfu assistant"},
    {"role": "user", 
     "content": prompt}
  ],
  temperature=0,
  top_p=.1
)

print(completion.choices[0].message.content)


