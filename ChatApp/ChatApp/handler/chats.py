from flask import jsonify, request
from dao.chats import ChatDAO
from dao.messages import MessagesDAO


class ChatHandler:

    def mapMessagesToDictionary(self, row):
        result = {}
        result['messageId'] = row[0]
        result['poster'] = row[1]
        result['chat'] = row[2]
        result['message'] = row[3]
        result['timeStamp'] = row[4]
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
        result['email'] = row[2]
        return result

    def getAllChats(self):
        dao = ChatDAO()
        result = dao.getAllChats()
        mapped_result = []
        return self.mapToDictionary(r)

    def getChatById(self, id):
        dao = ChatDAO()
        result = dao.getChatById(id)
        if result == None:
            return jsonify(Error="CHAT NOT FOUND"), 404
        else:
            return self.mapToDictionary(result)

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

    def createChat(self, admin, name):
        dao = ChatDAO()
        dao.createChat(admin, name)
        return jsonify(Created="Chat with name " + name + " has been created")

    def addContactToChat(self, chatId, contact):
        return jsonify(ContactAddedToChat="User with id "+contact + " has been added to chat " + chatId)

    def removeContactFromChat(self, chatId, contact):
        dao = ChatDAO()
        dao.removeUser(chatId, contact)
        return jsonify(ContactAddedToChat="User " + contact + " has been removed from chat " + chatId)

    def removeChat(self, name):
        dao = ChatDAO()
        dao.removeChat(name)
        return jsonify(Removed="Chat with id '" + name + "' has been removed")

    def postMessage(self, chat, user, message):
        dao = ChatDAO()
        dao.postMessage(chat, user, message)
        return jsonify(Posted="Message: '" + message + "' has been posted to chat: " + chat)

    def getMessages(self, chatId):
        dao = MessagesDAO()
        messages = dao.getMessagesByChatId(chatId)
        if messages:
            mappedResult = []
            for m in messages:
                mappedResult.append(self.mapMessagesToDictionary(m))
            return jsonify(Messages=mappedResult)
        return jsonify(Empty="No messages in this chat yet")

    def likeMessage(self, chatId, user, messageId, like):
        dao = ChatDAO()
        dao.likeMessage(messageId, like, user)
        if int(like):
            return jsonify(Like="Message with id: " + messageId + " in chat: " + chatId + " has been liked")
        return jsonify(Like="Message with id: " + messageId + " in chat: " + chatId + " has been disliked")

    def replyToMessage(self, message, replying):
        dao = ChatDAO()
        dao.reply(message, replying)
        return jsonify(
            Reply="Message '" + message + " has posted a reply to message: " + replying)
    #REPLY QUERY FOR WHEN ITS READY: WITH result AS ( insert into messages values(DEFAULT, 2, 1, 'This is test for reply', '2018-12-18') returning messageid )
    # insert into replies values(DEFAULT, (select * from result), 4); select * from replies;