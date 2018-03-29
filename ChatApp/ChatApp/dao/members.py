class MemberDAO:
    def __init__(self):
        P1 = [0, 1, 1]
        P2 = [1, 1, 2]
        P3 = [2, 1, 3]
        P4 = [3, 0, 2]
        P5 = [4, 0, 3]
        P6 = [5, 2, 3]

        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)
        self.data.append(P5)
        self.data.append(P6)

    def getAllMembers(self):
        return self.data

    def getMembersById(self, id):
        result = []
        allMembers = self.getAllMembers()
        for r in allMembers:
            if r[1] == int(id):
                result.append(r)
        return result
