import psycopg2
class MemberDAO:
    def __init__(self):
        conn_string = "host='localhost' dbname='chatapp' user='postgres' password='postgres'"
        self.conn = psycopg2.connect(conn_string)

    def getAllMembers(self):
        return self.data

    def getMembersById(self, id):
        cursor = self.conn.cursor()
        cursor.execute("select username, email from users natural inner join members where chat = %s;", id)
        result = []
        for row in cursor:
            result.append(row)
        return result
