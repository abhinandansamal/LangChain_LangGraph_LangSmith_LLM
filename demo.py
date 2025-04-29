import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAI

_ = load_dotenv(find_dotenv())
openai_api_key = os.getenv("OPENAI_API_KEY")

llm_model = OpenAI()

for chunk in llm_model.stream(
    "Provide me tips to learn Generative AI."
):
    print(chunk, end="", flush=True)