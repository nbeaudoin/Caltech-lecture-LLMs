import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
import streamlit as st

# Load credentuals
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OpenAI.api_key = OPENAI_API_KEY

st.title('LLM Model')
prompt = st.text_input('Enter a prompt here')

llm = OpenAI(temperature=2,
             max_tokens=100,
             )

if prompt:
    response = llm(prompt)
    st.write(response)

