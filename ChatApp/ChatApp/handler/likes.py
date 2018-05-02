from flask import jsonify, request
from dao.likes import LikesDAO


class LikesHandler:
    def mapToDictionaryAll(self, row):
        result = {}
        result['likeId'] = row[0]
        result['likeValue'] = row[1]
        result['message'] = row[2]
        result['userID'] = row[3]
        result['timestamp'] = row[4]
        return result

    def mapToDictionary(self, row):
        result = {}
        result['username'] = row[0]
        return result

    def getUserReactionsByMessageId(self, messageId):
        dao = LikesDAO()
        result = dao.getUserReactionsByMessageId(messageId)
        mappedResult = [[],[]]
        for r in result[0]:
            mappedResult[0].append(self.mapToDictionary(r))
        for r in result[1]:
            mappedResult[1].append(self.mapToDictionary(r))
        return jsonify(Likes=mappedResult)

    def getAllLikes(self, like):
        dao = LikesDAO()
        result = dao.getAllLikes(like)
        mappedResult = []
        for r in result:
            mappedResult.append(self.mapToDictionaryAll(r))
        return jsonify(Likes=mappedResult)

    def getLikesByMessageId(self, id):
        dao = LikesDAO()
        result = dao.getLikesByMessageId(id)
        mappedResult = []
        if not result:
            return jsonify(Error="THIS MESSAGE HAS NO LIKES"), 404
        else:
            for r in result:
                mappedResult.append(self.mapToDictionary(r))
            return jsonify(Likes=mappedResult)
