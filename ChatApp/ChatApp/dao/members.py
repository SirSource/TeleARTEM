import psycopg2
class MemberDAO:
    def __init__(self):
        conn_string = "host='chatapp.crxgakfnkwhg.us-east-1.rds.amazonaws.com' dbname='chatapp' user='masterUsername' password='ICOM5026'"
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
