# code snippet of retrieve key from local environment variables
import os
from dotenv import (load_dotenv, find_dotenv) 
load_dotenv(find_dotenv())

#key = os.environ["DEEPSEEK_API_KEY"]
key = os.getenv("DEEPSEEK_API_KEY")
print(key)