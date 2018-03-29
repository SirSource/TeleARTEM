from flask import jsonify, request
from dao.chats import ChatDAO
from dao.messages import MessagesDAO


class ChatHandler:

    def mapMessagesToDictionary(self, row):
        print(row)
        result = {}
        result['messageId'] = row[0]
        result['poster'] = row[1]
        result['chat'] = row[2]
        result['message'] = row[3]
        result['timeStamp'] = row[4]
        result['replyId'] = row[5]
        return result

    def mapToDictionary(self, row):
        result = {}
        result['chatId'] = row[0]
        result['admin'] = row[1]
        result['name'] = row[2]
        return result

    def mapToAdminDictionary(self, row):
        result = {}
        result['chatId'] = row[0]
        result['admin'] = row[1]
        result['name'] = row[2]
        return result

    def getAllChats(self):
        dao = ChatDAO()
        result = dao.getAllChats()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDictionary(r))
        return jsonify(Chats=mapped_result)

    def getChatById(self, id):
        dao = ChatDAO()
        result = dao.getChatById(id)
        print(result)
        if result == None:
            return jsonify(Error="CHAT NOT FOUND"), 404
        else:
            mapped = self.mapToDictionary(result)
            return jsonify(Chat=mapped)

    def getAdminByChatId(self, id):
        dao = ChatDAO()
        result = dao.getAdminByChatId(id)
        mappedResult = []
        for r in result:
            mappedResult.append(self.mapToDictionary(r))
        return jsonify(Admin=mappedResult)

    def getNameByChatId(self, id):
        dao = ChatDAO()
        result = dao.getNameByChatId(id)
        mappedResult = []
        for r in result:
            mappedResult.append(self.mapToAdminDictionary(r))
        return jsonify(Admin=mappedResult)

    def createChat(self, name):
        return jsonify(Created="Chat with name " + name + " has been created")

    def addContactToChat(self, chatId, contact):
        return jsonify(ContactAddedToChat=contact + " has been added to chat " + chatId)

    def removeContactFromChat(self, chatId, contact):
        return jsonify(ContactAddedToChat="User " + contact + " has been removed from chat " + chatId)

    def removeChat(self, name):
        return jsonify(Removed="Chat with name " + name + " has been removed")

    def postMessage(self, name, message):
        return jsonify(Posted="Message: '" + message + "' has been posted to chat: " + name)

    def getMessages(self, chatId):
        dao = MessagesDAO()
        messages = dao.getMessagesByChatId(chatId)
        if messages:
            mappedResult = []
            for m in messages:
                mappedResult.append(self.mapMessagesToDictionary(m))
            return jsonify(Messages=mappedResult)
        return jsonify(Empty="No messages in this chat yet")

    def likeMessage(self, chatId, messageId, like):
        if int(like):
            return jsonify(Like="Message with id: " + messageId + " in chat: " + chatId + " has been liked")
        return jsonify(Like="Message with id: " + messageId + " in chat: " + chatId + " has been disliked")

    def replyToMessage(self, chatId, messageId, message):
        return jsonify(
            Reply="Message '" + message + "' in chat: " + chatId + " has been posted as a reply to message: " + messageId)
