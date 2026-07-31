import mysql.connector

class Database:
    def __init__(self,):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Santosh@1503',
            database='library'
        )
        self.cursor=self.conn.cursor()
    def close(self):
                self.cursor.close()
                self.conn.close()