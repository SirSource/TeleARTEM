import psycopg2
class ChatDAO:
    def __init__(self):
        conn_string = "host='chatapp.crxgakfnkwhg.us-east-1.rds.amazonaws.com' dbname='chatapp' user='masterUsername' password='ICOM5026'"
        self.conn = psycopg2.connect(conn_string)

    def getAllChats(self):
        cursor = self.conn.cursor()
        cursor.execute("select * from chats;")
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getAllChatsNames(self, id):
        cursor = self.conn.cursor()
        cursor.execute("select * from chats where chatId not in (select chat as chatId from members where userid="+id+")")
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllChatsMember(self, id):
        cursor = self.conn.cursor()
        print(id)
        cursor.execute("select * from chats where chatId in (select chat as chatId from members where userid="+id+");")
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminByChatId(self, id):
        cursor = self.conn.cursor()
        cursor.execute("select chatid, username, email from chats inner join users on chats.admin=users.userid where chatid = "+id+";")
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getChatById(self, id):
        cursor = self.conn.cursor()
        cursor.execute("select * from chats where chatid=%s;", str(id))
        return cursor.fetchone()

    def addContactToChat(self, chat, user):
        cursor = self.conn.cursor()
        cursor.execute("insert into members values(DEFAULT, %s, %s);", (chat, user))
        self.conn.commit()

    def likeMessage(self, userId, messageId, like):
        cursor = self.conn.cursor()
        cursor.execute("insert into likes values(DEFAULT, %s, %s, %s, current_timestamp);", (like, messageId, userId))
        self.conn.commit()

    def postMessage(self, chat, user, message):
        cursor = self.conn.cursor()
        print(message)
        cursor.execute("insert into messages values(DEFAULT, %s, %s, %s, current_timestamp) returning messageid;",
                       (user, chat, message,))
        self.conn.commit()
        return cursor.fetchone()[0]

    def reply(self, message, replying):
        cursor = self.conn.cursor()
        cursor.execute("insert into replies values(DEFAULT, %s, %s);", (message, replying,))
        self.conn.commit()