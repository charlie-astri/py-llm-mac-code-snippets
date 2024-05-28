
# code snippet of retrieve key from local environment variables
import os
# import dotenv
# dotenv.load_dotenv()
#key = os.environ["DEEPSEEK_API_KEY"]
key = os.getenv("DEEPSEEK_API_KEY")
print(key)