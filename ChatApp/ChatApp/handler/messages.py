from flask import jsonify, request
from dao.messages import MessagesDAO


class MessagesHandler:
    def messagesChatReady(self, chat):
        data = MessagesDAO().messagesChatReady(chat)
        result = []
        print(data)
        for i in data:
            result.append(self.messagesChatReadyToDictionary(i))

        return jsonify(Messages=result)

    def messagesChatReadyToDictionary(self, row):
        result = {}
        result['messageId'] = row[0]
        result['message'] = row[1]
        result['poster'] = row[2]
        result['timeStamp'] = row[3]
        result['like'] = row[4]
        result['dislike'] = row[5]
        return result

    def mapHashtagsToDictionary(self, row):
        result = {}
        result['id'] = row[0]
        result['count'] = row[1]
        return result

    def mapLikesOfMessage(self, row):
        result = {}
        result['messageId'] = row[0]
        result['message'] = row[1]
        result['count'] = row[2]
        return result

    def mapRepliesToDictionary(self, row):
        result = {}
        print(row)
        result['messageid'] = row[0]
        result['replyid'] = row[1]
        result['replyingto'] = row[2]
        result['timestamp'] = row[3]
        result['message'] = row[4]
        return result

    def mapToDictionary(self, row):
        result = {}
        result['messageId'] = row[0]
        result['poster'] = row[1]
        result['chat'] = row[2]
        result['message'] = row[3]
        result['timestamp'] = row[4]
        return result
    def mapToDictionaryMessagesDate(self, row):
        result = {}
        result['date'] = row[0]
        result['count'] = row[1]
        return result

    def getAllMessages(self):
        dao = MessagesDAO()
        result = dao.getAllMessages()
        mappedResult = []
        for r in result:
            mappedResult.append(self.mapToDictionary(r))
        return jsonify(Messages=mappedResult)

    def getLikesOfMessage(self, id, like):
        dao = MessagesDAO()
        result = dao.getLikesOfMessage(id, like)
        mappedResult = []
        for r in result:
            mappedResult.append(self.mapLikesOfMessage(r))
        return jsonify(Messages=mappedResult)

    def getUsersLikesOfMessage(self, id, like):
        dao = MessagesDAO()
        result = dao.getLikesOfMessage(id, like)
        mappedResult = []
        for r in result:
            mappedResult.append(self.mapLikesOfMessage(r))
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

    def mapUsersToDictionary(self, row):
        result = {}
        result['username'] = row[0]
        return result

    def getUserReactionsByMessage(self, id, like):
        dao = MessagesDAO()
        result = dao.getUsersByMessageReactions(id, like)
        mappedResult = []
        for r in result:
            mappedResult.append(self.mapUsersToDictionary(r))
        return jsonify(Users=mappedResult)

    def getHashtagAggregates(self):
        dao = MessagesDAO()
        result = dao.getHashtagAggregates()
        mappedResult = []
        for r in result:
            mappedResult.append(self.mapHashtagsToDictionary(r))
        return jsonify(Hashtags=mappedResult)

    def getTopUsers(self):
        dao = MessagesDAO()
        result = dao.getTopUsers()
        mappedResult = []
        for r in result:
            mappedResult.append(self.mapHashtagsToDictionary(r))
        return jsonify(TopUsers=mappedResult)

    def getHashtagAggregatesWord(self, chat, word):
        dao = MessagesDAO()
        result = dao.getHashtagAggregatesSearch(chat, word)
        mappedResult = []
        for r in result:
            mappedResult.append(self.messagesChatReadyToDictionary(r))
        return jsonify(Messages=mappedResult)

    def getRepliesPerDate(self, date):
        dao = MessagesDAO()
        result = dao.getRepliesPerDate(date)
        mappedResult = []
        for r in result:
            mappedResult.append(self.mapRepliesToDictionary(r))
        return jsonify(Users=mappedResult)

    def getMessagesPerDate(self):
        dao = MessagesDAO()
        result = dao.getMessagesPerDate()
        mappedResult = []
        if not result:
            return jsonify(Error="THIS DAY NO MESSAGE WAS POSTED"), 404
        else:
            for r in result:
                mappedResult.append(self.mapToDictionaryMessagesDate(r))
            return jsonify(MsgDate=mappedResult)

    def getRepliesPerDate(self):
        dao = MessagesDAO()
        result = dao.getRepliesPerDate()
        mappedResult = []
        if not result:
            return jsonify(Error="THIS DAY NO MESSAGE WAS POSTED"), 404
        else:
            for r in result:
                mappedResult.append(self.mapToDictionaryMessagesDate(r))
            return jsonify(RepliesDate=mappedResult)
    def getLikesPerDate(self):
        dao = MessagesDAO()
        result = dao.getLikesPerDate()
        mappedResult = []
        if not result:
            return jsonify(Error="THIS DAY NO MESSAGE WAS POSTED"), 404
        else:
            for r in result:
                mappedResult.append(self.mapToDictionaryMessagesDate(r))
            return jsonify(LikesDate=mappedResult)

    def getDislikesPerDate(self):
        dao = MessagesDAO()
        result = dao.getDislikesPerDate()
        mappedResult = []
        if not result:
            return jsonify(Error="THIS DAY NO MESSAGE WAS POSTED"), 404
        else:
            for r in result:
                mappedResult.append(self.mapToDictionaryMessagesDate(r))
            return jsonify(DislikesDate=mappedResult)