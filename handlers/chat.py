
"""
This class simulates a Table from a Database, it has id and convesation columns.
This Chat object is handled by the ConversationHandler which acts as an ORM for this DB.
"""

class Chat:
    def __init__(self, id:str):
        self.__id = id
        self.__conversation = []

    def getConversation(self) -> list[dict[str,str]]:
        return self.__conversation
    
    def addMessage(self, message: str):
        self.__conversation.append(message)
    
    def getID(self) -> str:
        return self.__id