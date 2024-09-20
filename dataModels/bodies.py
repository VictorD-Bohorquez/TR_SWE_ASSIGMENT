from pydantic import BaseModel

class ConversationMessage(BaseModel):
    id: str
    message: str 

class ConversationHistory(BaseModel):
    id: str