from flask import jsonify, request
from dao.likes import LikesDAO


class LikesHandler:

    def mapToDictionary(self, row):
        result = {}
        result['likeId'] = row[0]
        result['likeValue'] = row[1]
        result['message'] = row[2]
        result['userID'] = row[3]
        return result

    def getAllLikes(self):
        dao = LikesDAO()
        result = dao.getAllLikes()
        mappedResult = []
        for r in result:
            mappedResult.append(self.mapToDictionary(r))
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
