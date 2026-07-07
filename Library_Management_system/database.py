import sqlite3

class Database:
    def __init__(self, dbname='library.db'):
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()

        self.cursor.execute("PRAGMA foreign_keys = ON")

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()