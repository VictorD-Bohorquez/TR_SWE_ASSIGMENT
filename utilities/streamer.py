import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
nltk.download('punkt_tab')

delay = int(os.environ.get("DELAY"))

async def stream_response(message: str):
    tokens = word_tokenize(message)
    for token in tokens:
        await asyncio.sleep(delay)
        yield token