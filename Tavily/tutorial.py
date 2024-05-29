import os
import dotenv
import pprint
dotenv.load_dotenv()
#key = os.environ["DEEPSEEK_API_KEY"]
key = os.getenv("TAVILY_API_KEY")
print(key)

from tavily import TavilyClient
tavily = TavilyClient(api_key=key)
# For basic search:
response = tavily.search(query="Should I invest in Apple in 2024?")
# For advanced search:
# response = tavily.search(query="Should I invest in Apple in 2024?", search_depth="advanced")
# Get the search results as context to pass an LLM:
pprint.pprint(response)
context = [{"url": obj["url"], "content": obj["content"]} for obj in response["results"]]