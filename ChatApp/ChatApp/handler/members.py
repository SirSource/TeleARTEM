from flask import jsonify, request
from dao.members import MemberDAO


class MemberHandler:

    def mapToDictionary(self, row):
        result = {}
        result['memberId'] = row[0]
        result['chat'] = row[1]
        result['userID'] = row[2]
        return result

    def getAllMembers(self):
        dao = MemberDAO()
        result = dao.getAllMembers()
        mappedResult = []
        for r in result:
            mappedResult.append(self.mapToDictionary(r))
        return jsonify(Members=mappedResult)

    def getMembersByChatId(self, id):
        dao = MemberDAO()
        result = dao.getMembersById(id)
        mappedResult = []
        if not result:
            return jsonify(Error="THIS CHAT HAS NO MEMBERS"), 404
        else:
            for r in result:
                mappedResult.append(self.mapToDictionary(r))
            return jsonify(Members=mappedResult)
