from pydantic import BaseModel

"""
Bodies for the available request to the API, both of them are sent through the request body as ID's are sent.
This prevents security leaks.
"""

class ConversationMessage(BaseModel):
    id: str
    message: str 

class ConversationHistory(BaseModel):
    id: str