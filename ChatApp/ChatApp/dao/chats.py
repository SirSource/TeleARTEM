class ChatDAO:
    def __init__(self):
        P1 = [0, 67, 'ICOM4035 Chat']
        P2 = [1, 53, 'ICOM5016 Chat']
        P3 = [2, 97, 'ICOM5009 Chat']
        P4 = [3, 97, 'ICOM4036 Chat']

        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)

    def getAllChats(self):
        return self.data

    def getChatById(self, id):
        for r in self.data:
            if int(id) == r[0]:
                return r

    def getAdminByChatId(self, id):
        adminInChats = []
        for i in self.data:
            if i[0] == int(id):
                adminInChats.append(i)
        return adminInChats
