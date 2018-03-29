from flask import jsonify, request
from dao.messages import MessagesDAO


class MessagesHandler:

    def mapToDictionary(self, row):
        result = {}
        result['messageId'] = row[0]
        result['poster'] = row[1]
        result['chat'] = row[2]
        result['message'] = row[3]
        result['timeStamp'] = row[4]
        result['replyId'] = row[5]
        return result

    def getAllMessages(self):
        dao = MessagesDAO()
        result = dao.getAllMessages()
        mappedResult = []
        for r in result:
            mappedResult.append(self.mapToDictionary(r))
        return jsonify(Messages=mappedResult)

    def getMessagesByChatId(self, id):
        dao = MessagesDAO()
        result = dao.getMessagesByChatId(id)
        mappedResult = []
        if not result:
            return jsonify(Error="THIS CHAT HAS NO MESSAGES"), 404
        else:
            for r in result:
                mappedResult.append(self.mapToDictionary(r))
            return jsonify(Messages=mappedResult)
