# LangServe helps developers deploy LangChain runnables and chains as a REST API.
# This library is integrated with FastAPI and uses pydantic for data validation.
# In addition, it provides a client that can be used to call into runnables deployed on a server.
# https://python.langchain.com/docs/langserve/

import os
from dotenv import find_dotenv, load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from fastapi import FastAPI
from langserve import add_routes
import uvicorn


_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

parser = StrOutputParser()

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", "{text}")
    ]
)

chain = prompt_template | llm | parser

app = FastAPI(
    title="simpleTranslator",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces"
)

add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

# run the file using command : python 10_langserve_demo.py
# then you will find http://localhost:8000 in the log. Copy it & open it in browser.
# You will see the following message: {"detail":"Not Found"}
# You have to use the following URL to test the API: http://localhost:8000/chain/playground/