import uuid
import pickle
import os
from .chat import Chat
from .conversationHandler import ConversationHandler

"""
Class that simulates a Cache memory for the API, once the system is running.
Once the API is up, this class works as cache, saving all the available chat IDs.
"""

class ChatsHandler:
    def __init__(self):
        self.__saving_path = str(os.getcwd())+"/chats"
        self.__chats = []
        if not os.path.exists(self.__saving_path):
            os.makedirs(self.__saving_path)

    """
    Method that creates a new Chat session using the conversation Handler.
    The chat ID is saved on the chat's array simulating the System's Cache.
    """
    def newChat(self) -> str: 
        id = str(uuid.uuid4())
        self.__chats.append(id)
        chat = Chat(id=id)
        handler = ConversationHandler()
        handler.saveChat(chat)
        return id
    
    def availableChat(self, id: str) -> bool:
        if id in self.__chats:
            return True
        return False