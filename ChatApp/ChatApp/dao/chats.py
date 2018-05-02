import psycopg2
class ChatDAO:
    def __init__(self):
        conn_string = "host='localhost' dbname='chatapp' user='postgres' password='postgres'"
        self.conn = psycopg2.connect(conn_string)

    def getAllChats(self):
        cursor = self.conn.cursor()
        cursor.execute("select * from chats;")
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getAdminByChatId(self, id):
        cursor = self.conn.cursor()
        cursor.execute("select chatid, username, email from chats inner join users on chats.admin=users.userid where chatid = %s;", id)
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getChatById(self, id):
        cursor = self.conn.cursor()
        cursor.execute("select * from chats where chatid=%s;", id)
        return cursor.fetchone()