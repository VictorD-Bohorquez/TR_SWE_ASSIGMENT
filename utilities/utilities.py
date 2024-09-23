import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 
from dotenv import load_dotenv
import os
import asyncio
import re

load_dotenv()
nltk.download('punkt_tab')

delay = int(os.environ.get("DELAY"))

"""
Utility Method to simulate the response of a GPT conversation, sending the response in parts.
The DELAY environment variable sets the amount of time that every part of the response will take to be sent.
The response tokenization is handled by NLTK labrary, which provides a more complex and refined tokenization that the normal split method.
"""
async def stream_response(message: str) -> str:
    tokens = word_tokenize(message)
    for token in tokens:
        await asyncio.sleep(delay)
        yield token

"""
Utility Method to delete scritp tags in the inputs to avoid injection attacks and also prevent the API from being blocked from OpenAI API.
"""
def sanitize_str(message: str) -> str:
    sanitized_str = re.sub(r'<script\b[^>]*>(.*?)</script>', '', message, flags=re.IGNORECASE)
    return sanitized_str