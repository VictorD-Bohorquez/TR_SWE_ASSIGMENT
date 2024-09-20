import pickle
import os
from chat import Chat

class ConversationHandler:
    def __init__(self, id):
        self.__saving_path = os.getcwd()+"/chats"
        self.__id = id
    
    def addMessage(self, message):
        file = self.__saving_path+"/"+ id +".pkl"
        if not os.path.exists(file):
            return False
        else: 
            with open(file, "rb") as f:
                chat = pickle.load(f)
                chat.addMessage(message)
            with open(file, 'wb') as f:
                pickle.dump(chat, f, pickle.HIGHEST_PROTOCOL)
            return True

    def getChat(self, id):
        file = self.__saving_path+"/"+ id +".pkl"
        if not os.path.exists(file):
            return None
        else:
            with open(file, 'rb') as f:
                chat = pickle.load(f)
                return chat.getConversation()
    