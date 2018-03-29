from flask import jsonify, request
from dao.user import UserDAO


class UserHandler:

    def mapToDictionary(self, row):
        result = {}
        result['userId'] = row[0]
        result['name'] = row[1]
        result['email'] = row[2]
        result['username'] = row[3]
        result['phone'] = row[4]
        return result

    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        mappedResult = []
        for r in result:
            mappedResult.append(self.mapToDictionary(r))
        return jsonify(Users=mappedResult)

    def getUserById(self, id):
        dao = UserDAO()
        result = dao.getUserById(id)
        if not result:
            return jsonify(Error="USER NOT FOUND"), 404
        else:
            mapped = self.mapToDictionary(result)
            return jsonify(User=mapped)

    def searchUsers(self, args):
        dao = UserDAO()
        result = dao.searchByUsername(str(args))
        if not result:
            return jsonify(Error="USER NOT FOUND"), 404
        else:
            return jsonify(User=result)

    def registerUser(self):
        return jsonify(Success="USER HAS BEEN REGISTERED")
