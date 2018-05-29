import psycopg2
class ContactDAO:
    def __init__(self):
        conn_string = "host='chatapp.crxgakfnkwhg.us-east-1.rds.amazonaws.com' dbname='chatapp' user='masterUsername' password='ICOM5026'"
        self.conn = psycopg2.connect(conn_string)

    def getAllContacts(self, id):
        return self.data

    def getContactsById(self, id):
        cursor = self.conn.cursor()
        cursor.execute("select name, email, username from contacts inner join users on contacts.friend = users.userid where holder = %s",
                       (id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getContact(self, id):
        cursor = self.conn.cursor()
        cursor.execute("select username from users  where userid = %s",
                       (id))
        return cursor.fetchone()
