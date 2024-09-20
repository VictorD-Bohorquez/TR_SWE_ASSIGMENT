
class Chat:
    def __init__(self, id):
        self.__id = id
        self.__conversation = []

    def getConversation(self):
        return self.__conversation
    
    def addMessage(self, message):
        self.__conversation.append(message)
    
    def getID(self):
        return self.__id