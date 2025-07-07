import os
from dotenv import load_dotenv

load_dotenv()

APILAYER_API_KEY = os.getenv("APILAYER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PROXY_URL = os.getenv("PROXY_URL")
