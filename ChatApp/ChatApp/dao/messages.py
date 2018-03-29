class MessagesDAO:
    def __init__(self):
        P1 = [0, 3, 0, 'Message Data Structures 0', '010118 0900', None]
        P2 = [1, 0, 1, 'Message Databases 0', '010118 0901', None]
        P3 = [2, 3, 1, 'Message Databases 1', '010118 0911', None]
        P4 = [3, 1, 1, 'Message Databases 2', '010118 0923', None]
        P5 = [4, 2, 2, 'Message OS 0', '010118 0908', None]
        P6 = [5, 2, 2, 'Message OS 1', '010118 09019', None]
        P7 = [6, 2, 0, 'Message Data Structures 1', '010118 0905', None]
        P8 = [7, 1, 1, 'Message Databases 3', '010118 0947', 1]

        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)
        self.data.append(P5)
        self.data.append(P6)
        self.data.append(P7)
        self.data.append(P8)

    def getAllMessages(self):
        return self.data

    def getMessagesByChatId(self, id):
        messages = []
        for r in self.data:
            if int(id) == r[2]:
                messages.append(r)
        return messages

    def getMessagesByUserId(self, id):
        messages = []
        for r in self.data:
            if int(id) == r[1]:
                messages.append(r)
        return messages
