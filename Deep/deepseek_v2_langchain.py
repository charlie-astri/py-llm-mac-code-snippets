# pip3 install langchain_openai
# python3 deepseek_v2_langchain.py
import os
from dotenv import (load_dotenv, find_dotenv) 
load_dotenv(find_dotenv())

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model='deepseek-chat', 
    openai_api_key=os.getenv("DEEPSEEK_API_KEY"), 
    openai_api_base='https://api.deepseek.com',
    max_tokens=1024
)

response = llm.invoke("Hi!")
print(response.content)