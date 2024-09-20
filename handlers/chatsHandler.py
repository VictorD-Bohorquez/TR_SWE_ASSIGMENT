import uuid
import pickle
import os
from .chat import Chat
from .conversationHandler import ConversationHandler

class ChatsHandler:
    def __init__(self):
        self.__saving_path = str(os.getcwd())+"/chats"
        self.__chats = []
        if not os.path.exists(self.__saving_path):
            os.makedirs(self.__saving_path)

    def newChat(self):
        id = str(uuid.uuid4())
        self.__chats.append(id)
        chat = Chat(id=id)
        handler = ConversationHandler()
        handler.saveChat(chat)
        return id