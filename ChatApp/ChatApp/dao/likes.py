import psycopg2
class LikesDAO:
    def __init__(self):
        conn_string = "host='localhost' dbname='chatapp' user='postgres' password='postgres'"
        self.conn = psycopg2.connect(conn_string)

    def getUserReactionsByMessageId(self, id):
        cursor = self.conn.cursor()
        cursor.execute("select username from likes natural inner join users where message = %s AND likevalue = 0", (id,))
        result = [[], []]
        for row in cursor:
            result[0].append(row)
        cursor.execute("select username from likes natural inner join users where message = %s AND likevalue = 1", (id,))
        for row in cursor:
            result[1].append(row)
        return result

    def getAllLikes(self, like):
        cursor = self.conn.cursor()
        cursor.execute("select * from likes where likevalue=%s;", like)
        result = []
        for row in cursor:
            result.append(row)
        return result
