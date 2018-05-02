from flask import jsonify, request
from dao.user import UserDAO


class UserHandler:
    def getAllUsersDB(self):
        data = UserDAO().getAllUsersDB()
        result = []
        for i in data:
            result.append(self.mapToDictionary(i))

        return jsonify(Messages=result)

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
            print(result)
            mapped = self.mapToDictionary(result)
            return jsonify(User=mapped)

    def searchUsers(self, args):
        dao = UserDAO()
        result = dao.searchByUsername(str(args))
        if not result:
            return jsonify(Error="USER NOT FOUND"), 404
        else:
            return jsonify(User=result)

    def registerUser(self, name, username, email, password, phone):
        return jsonify(Register="User with name: '" + name + "',username: '"+username+"', email: '"+email+"', password: '"+password+"' and phone: '"+phone+"' has been registered")

    def login(self,username, password):
        return jsonify(Login="User with username: '" + username + "' has succesfully logged in")

    def activeUsers(self):
        return jsonify(Login="Number of active users is: "+str(UserDAO().activeUsers()[0]))

