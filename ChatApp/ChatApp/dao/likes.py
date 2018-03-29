class LikesDAO:
    def __init__(self):
        P1 = [0, 1, 7, 0]
        P2 = [1, 0, 4, 3]
        P3 = [2, 1, 3, 2]
        P4 = [3, 1, 2, 1]
        P5 = [4, 1, 4, 1]
        P6 = [5, 0, 7, 1]
        P7 = [6, 0, 2, 2]
        P8 = [7, 0, 1, 2]

        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)
        self.data.append(P5)
        self.data.append(P6)
        self.data.append(P7)
        self.data.append(P8)

    def getAllLikes(self):
        return self.data

    def getLikesById(self, id):
        likesByUser = []
        for r in self.data:
            if int(id) == r[3]:
                likesByUser.append(r)
        return likesByUser

    def getLikesByMessageId(self, id):
        likesByMessage = []
        for r in self.data:
            if int(id) == r[2]:
                likesByMessage.append(r)
        return likesByMessage
