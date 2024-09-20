"""Main project file"""

import asyncio
import random

from fastapi import FastAPI

from sse_starlette.sse import EventSourceResponse

# see llm.py to better understand the interaction with OpenAI's Chat Completion service.
from llm.llm import prompt_llm_async

from handlers.chatsHandler import ChatsHandler
from handlers.conversationHandler import ConversationHandler
from dataModels.bodies import ConversationMessage, ConversationHistory
from utilities.streamer import stream_response

app = FastAPI()

chats = ChatsHandler()

@app.get("/stream-example")
async def stream_example():
    """
    Example route for streaming text to the client, one word/token at a time.
    """
    async def stream_tokens():
        """
        Placeholder implementation for token streaming. Try running this route as-is to better understand how to
        stream data using Server-Sent Events (SSEs) in FastAPI.
        See this tutorial for more information: https://devdojo.com/bobbyiliev/how-to-use-server-sent-events-sse-with-fastapi
        """
        for token in ['hello', ', ', 'this ', 'is ', 'a ', 'streamed ', 'response.']:
            # fake delay:
            await asyncio.sleep(random.randint(0, 3))

            print(f"Yielding token: {token}")
            yield token

    return EventSourceResponse(stream_tokens())

@app.post("/start-chat")
async def start_chat():
    chatID = chats.newChat()
    print(chatID)
    return {"Session":chatID}

@app.post("/send-message")
async def send_message(conversation: ConversationMessage):
    handler = ConversationHandler()
    #response = prompt_llm_async(conversation.message)
    #answer = response.choices[0].message.content
    #role = response.choices[0].message.role
    answer = "This is, a test response"
    role = "Assistant"
    user_message = {"role": "user", "content": conversation.message}
    response_message = {"role": role, "content": answer}
    handler.addMessage(id= conversation.id, message= user_message)
    handler.addMessage(id= conversation.id, message= response_message)
    return EventSourceResponse(stream_response(answer))

@app.get("/get-full-conversation")
async def get_full_conversation(history: ConversationHistory):
    handler = ConversationHandler()
    conversation = handler.getChat(history.id)
    return {"Conversation": conversation}