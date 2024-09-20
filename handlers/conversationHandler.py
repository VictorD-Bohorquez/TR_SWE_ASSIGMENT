import pickle
import os
from chat import Chat

class ConversationHandler:
    def __init__(self):
        self.__saving_path = os.getcwd()+"/chats"
    
    def addMessage(self, message, id):
        chat = self.readChat(id)
        if chat:
            chat.addMessage(message)
            self.saveChat(chat)
            return True
        return False

    def getChat(self, id):
        chat = self.readChat(id)
        if chat:
            return chat.getConversation()
        return None
    
    def saveChat(self, chat):
        file = self.__saving_path+"/"+ id +".pkl"
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