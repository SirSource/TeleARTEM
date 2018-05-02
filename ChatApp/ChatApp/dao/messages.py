import psycopg2
class MessagesDAO:
    def __init__(self):

        #conn_string = "host='teleartem.crxgakfnkwhg.us-east-1.rds.amazonaws.com' dbname='chatapp' user='masterUsername' password='ARTEMiusCorp'"
        conn_string = "host='localhost' dbname='chatapp' user='postgres' password='postgres'"
        self.conn = psycopg2.connect(conn_string)

    def messagesChatReady(self):
        cursor = self.conn.cursor()
        cursor.execute("select messageID, M.message, Users.username, M.timeStamp, (select count(likeValue) from Likes where likeValue = 1 AND message=M.messageID) as like, "
                       "(select count(likeValue) from Likes where likeValue = 0 AND message=M.messageID) as dislike "
                       "from Users inner join Messages as M on Users.userID=M.poster inner join Likes on M.poster=Likes.userID "
                       "group by messageID, Users.username order by timeStamp;")

        result = []
        for row in cursor:
            result.append(row)
        return result
    def getHashtagAggregates(self, date):
        cursor = self.conn.cursor()
        key = '%#%'
        cursor.execute("SELECT word, count(*) AS ct FROM   messages, unnest(string_to_array(message, ' ')) word WHERE word LIKE %s AND timestamp>%s GROUP  BY word ORDER BY ct DESC LIMIT 3;", (key, date))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessages(self):
        cursor = self.conn.cursor()
        cursor.execute("select * from messages;")
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getLikesOfMessage(self, id, like):
        cursor = self.conn.cursor()
        cursor.execute("select messages.messageid, messages.message, count(*) from messages inner join likes on messages.messageid=likes.message AND likes.message = %s AND likevalue = %s group by messages.messageid, messages.message;", (id, like))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesByChatId(self, id):
        cursor = self.conn.cursor()
        cursor.execute("select messageid, poster, chat, message, timestamp from messages where chat = %s;",id)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesByUserId(self, id):
        messages = []
        for r in self.data:
            if int(id) == r[1]:
                messages.append(r)
        return messages

    def getUsersByMessageReactions(self, id, like):
        cursor = self.conn.cursor()
        cursor.execute("select username from likes natural inner join users where message = %s AND likevalue = %s", (id, like))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRepliesPerDate(self, date):
        cursor = self.conn.cursor()
        cursor.execute("SELECT messageid, replyid, replyingto, timestamp, message from messages natural inner join replies where timestamp = %s;", (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesPerDate(self, date):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * from messages where timestamp = %s;", (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result
