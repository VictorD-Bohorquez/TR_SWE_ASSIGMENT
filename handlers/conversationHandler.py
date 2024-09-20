import pickle
import os
from .chat import Chat

class ConversationHandler:
    def __init__(self):
        self.__saving_path = str(os.getcwd())+"/chats"
    
    def addMessage(self, message: str, id: str):
        chat = self.readChat(id)
        if chat:
            chat.addMessage(message)
            self.saveChat(chat)
            return True
        return False

    def getChat(self, id: str):
        chat = self.readChat(id)
        if chat:
            return chat.getConversation()
        return None
    
    def saveChat(self, chat: Chat):
        file = self.__saving_path+"/"+ chat.getID() +".pkl"
        with open(file, 'wb') as f:
            pickle.dump(chat, f, pickle.HIGHEST_PROTOCOL)
            return True
    
    def readChat(self, id):
        file = self.__saving_path+"/"+ id +".pkl"
        if os.path.exists(file):
            with open(file, "rb") as f:
                chat = pickle.load(f)
                return chat
        return None