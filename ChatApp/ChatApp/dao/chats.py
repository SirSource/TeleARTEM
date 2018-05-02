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
    def createChat(self, admin, name):
        cursor = self.conn.cursor()
        cursor.execute("insert into chats values(DEFAULT, %s, %s);",(admin, name,))
        self.conn.commit()
    def removeUser(self, chatId, contact):
        cursor = self.conn.cursor()
        cursor.execute("delete from members where chat =%s and userid=%s;",(chatId, contact,))
        self.conn.commit()

    def removeChat(self, name):
        cursor = self.conn.cursor()
        cursor.execute("delete from chats where name =%s;",(name,))
        self.conn.commit()

    def postMessage(self, chat, user, message):
        cursor = self.conn.cursor()
        cursor.execute("insert into messages values(DEFAULT, %s, %s, %s, current_timestamp);",(user, chat, message,))
        self.conn.commit()

    def likeMessage(self, id, like, user):
        cursor = self.conn.cursor()
        cursor.execute("insert into likes values(DEFAULT, %s, %s, %s, current_timestamp);",(like, id, user,))
        self.conn.commit()

    def reply(self, message, replying):
        cursor = self.conn.cursor()
        cursor.execute("insert into replies values(DEFAULT, %s, %s);",(message, replying,))
        self.conn.commit()

