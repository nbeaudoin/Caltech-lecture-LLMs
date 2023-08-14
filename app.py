import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

# Load credentuals
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Build template
template = """Question: {question}
Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])

# Create LLM
llm = OpenAI()
llm = OpenAI(openai_api_key=OPENAI_API_KEY)

# Chain things together
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Ask a question
question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

# Run the result
print(llm_chain.run(question))




