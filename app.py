import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

# Load credentuals
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OpenAI.api_key = OPENAI_API_KEY

st.title('Caltech Story Bot🐛')
prompt = st.text_input('Enter a theme here')

# Prompt templates
title_template = PromptTemplate(
    input_variables=['topic'],
    template='Write me a children\'s story about {topic} that takes place at Caltech'
)

llm = OpenAI(temperature=2,
             max_tokens=100,
             )

title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

if prompt:
    response = title_chain.run(topic=prompt)
    st.write(response)

