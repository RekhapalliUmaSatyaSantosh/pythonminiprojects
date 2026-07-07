import sqlite3

class Tables:
    def __init__(self, db):
        self.conn = db.conn
        self.cursor = db.cursor

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Books(
            bookid INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publisher TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Members(
            memberid INTEGER PRIMARY KEY,
            membername TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT UNIQUE
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS IssueBooks(
            issueid INTEGER PRIMARY KEY,
            memberid INTEGER NOT NULL,
            bookid INTEGER NOT NULL,
            issuedate TEXT NOT NULL,
            returndate TEXT,
            FOREIGN KEY (memberid)
                REFERENCES Members(memberid),
            FOREIGN KEY (bookid)
                REFERENCES Books(bookid)
        )
        """)

        self.conn.commit()
        print('Database initialized successfully!')