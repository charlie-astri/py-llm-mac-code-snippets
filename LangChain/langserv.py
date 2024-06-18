# ref: https://python.langchain.com/v0.2/docs/tutorials/llm_chain/

import os
import pprint
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from typing import List
from fastapi import FastAPI
from langserve import add_routes

from dotenv import (load_dotenv, find_dotenv) 
load_dotenv(find_dotenv())


model = ChatOpenAI(
    model='deepseek-chat', 
    openai_api_key=os.getenv("DEEPSEEK_API_KEY"), 
    openai_api_base='https://api.deepseek.com',
    max_tokens=1024,
)

parser = StrOutputParser()


# try template
system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)


chain = prompt_template | model | parser
# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route

add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)

    