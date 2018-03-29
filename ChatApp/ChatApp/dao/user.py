class UserDAO:
    def __init__(self):
        P1 = [0, 'Daniel', 'daniel.rodriguez22@upr.edu', 'daniel22', '7875292359']
        P2 = [1, 'Gustavo', 'gustavo.marrero1@upr.edu', 'gustavo1', '7874085888']
        P3 = [2, 'Jaime', 'jaime.cortes@upr.edu', 'jaime', '7877036404']
        P4 = [3, 'Luis', 'luis.perez67@upr.edu', 'luis67', '7871347633']

        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)

    def getAllUsers(self):
        return self.data

    def getUserById(self, id):
        for r in self.data:
            if id == r[0]:
                return r

    def searchByUsername(self, args):
        dao = UserDAO()
        allUsers = self.getAllUsers()
        for r in allUsers:
            if r[3] == args:
                return r
