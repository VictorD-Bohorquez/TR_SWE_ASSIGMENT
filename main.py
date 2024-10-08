"""Main project file"""

import asyncio
import random

from fastapi import FastAPI,Response, status


from sse_starlette.sse import EventSourceResponse

# see llm.py to better understand the interaction with OpenAI's Chat Completion service.
from llm.llm import prompt_llm_async

from handlers.chatsHandler import ChatsHandler
from handlers.conversationHandler import ConversationHandler
from dataModels.bodies import ConversationMessage, ConversationHistory
from utilities.utilities import stream_response, sanitize_str

app = FastAPI()

chats = ChatsHandler()

"""
Endpoint to start a new conversartion from scratch.
"""
@app.post("/start-chat", status_code=201)
async def start_chat(response: Response):
    """
    Create a new chat object and responds to the calle the session ID of that chat, for future references and conversation tracking and managing.
    """
    chatID = chats.newChat()
    return {"Session":chatID}

"""
Endpoint to send messages to a created chat session.
"""
@app.post("/send-message", status_code=200)
async def send_message(conversation: ConversationMessage, response: Response):
    """
    The conversation is read from the save files (Simulatuing a DB) then the user new message is sent with all the previous messages.
    Once the LLM replies it saves the original question and it's response in the chat file.
    The replies are sent with the  SSE mechanism.
    """
    if chats.availableChat(conversation.id):
        user_message = sanitize_str(conversation.message)
        handler = ConversationHandler()
        previous_conversation = handler.readChat(conversation.id)
        response = prompt_llm_async(user_message_content=user_message, existing_messages=previous_conversation.getConversation())
        answer = response.choices[0].message.content
        role = response.choices[0].message.role
        user_message = {"role": "user", "content": conversation.message}
        response_message = {"role": role, "content": answer}
        handler.addMessage(id= conversation.id, message= user_message)
        handler.addMessage(id= conversation.id, message= response_message)
        return EventSourceResponse(stream_response(answer))
    else:
        response.status_code= status.HTTP_404_NOT_FOUND
        return {"Error": "The required session is not available."}

"""
Endpoint to get the full conversation.
"""
@app.get("/get-full-conversation", status_code=200)
async def get_full_conversation(history: ConversationHistory, response: Response):
    """
    The conversation is read from the save files (Simulatuing a DB) and all previous message are retrieved.
    """
    if chats.availableChat(history.id):
        handler = ConversationHandler()
        conversation = handler.getChat(history.id)
        return {"Conversation": conversation}
    else:
        response.status_code= status.HTTP_404_NOT_FOUND
        return {"Error": "The required session is not available."}