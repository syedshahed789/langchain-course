import os
from dotenv import load_dotenv
from tavily import TavilyClient
load_dotenv("/Users/macbookairm3/Documents/Udemy Course/langchain-course-searchtext/.venv/.env")


 
# Load .env

 
# Verify the API key is loaded
print("Tavily API Key exists:", os.getenv("TAVILY_API_KEY") is not None)
 
# Create Tavily client
client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
 
# Perform a search
response = client.search(
    query="rahul gandhi?",
    search_depth="advanced"
)
 
print(response)

