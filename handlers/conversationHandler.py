import pickle
import os
from .chat import Chat

"""
This class works as an ORM, handling and managing the calls and CRUD operations of the main table: Chats.
This class is responsible of managing the files and the conversations order.
"""

class ConversationHandler:
    def __init__(self):
        self.__saving_path = str(os.getcwd())+"/chats"
    
    """
    Reads the chat session and if it esists, adds a new message to it, and saves the file for persistance.
    """
    def addMessage(self, message: str, id: str) -> bool:
        chat = self.readChat(id)
        if chat:
            chat.addMessage(message)
            self.saveChat(chat)
            return True
        return False

    """
    Reads the chat file from the specified id, if it exists returns the chat history.
    """
    def getChat(self, id: str) -> list[dict[str,str]] | None:
        chat = self.readChat(id)
        if chat:
            return chat.getConversation()
        return None
    
    """
    Receuves a chat object and then saves it in a file using Piclke for persisntence.
    The file name is the Chat ID.
    """
    def saveChat(self, chat: Chat) -> bool:
        file = self.__saving_path+"/"+ chat.getID() +".pkl"
        with open(file, 'wb') as f:
            pickle.dump(chat, f, pickle.HIGHEST_PROTOCOL)
            return True

    """
    Reads the chat file from the specified id with Pickle, if it exists returns the chat object.
    """
    def readChat(self, id: str) -> Chat | None:
        file = self.__saving_path+"/"+ id +".pkl"
        if os.path.exists(file):
            with open(file, "rb") as f:
                chat = pickle.load(f)
                return chat
        return None