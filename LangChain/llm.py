# ref: https://python.langchain.com/v0.2/docs/tutorials/llm_chain/

import os
import pprint
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from dotenv import (load_dotenv, find_dotenv) 
load_dotenv(find_dotenv())

# no need of getpass
# os.environ["OPENAI_API_KEY"] = getpass.getpass()


model = ChatOpenAI(
    model='deepseek-chat', 
    openai_api_key=os.getenv("DEEPSEEK_API_KEY"), 
    openai_api_base='https://api.deepseek.com',
    max_tokens=1024,
)
messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

parser = StrOutputParser()

# result = model.invoke(messages)

# pprint.pprint(parser.invoke(result))

# use | to build a chain
chain = model | parser

print(chain.invoke(messages))

# try template
system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

result = prompt_template.invoke({"language": "italian", "text": "hi"})

print(result.to_messages())

chain = prompt_template | model | parser

print(chain.invoke({"language": "italian", "text": "hi"}))