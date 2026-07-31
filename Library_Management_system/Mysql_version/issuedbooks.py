import mysql.connector
from datetime import date,timedelta

class IssueBook:
    def __init__(self,db):
        self.conn=db.conn
        self.cursor=db.cursor
    
    def issue_book(self):
        try:
            issueid=int(input('Enter issue id= '))
            memberid=int(input('Enter member id= '))
            self.cursor.execute('select * from Members where memberid=%s',(memberid,))
            member=self.cursor.fetchone()
            
            if not member:
                print('Member not found')
                return
            bookid=int(input('Enter book id= '))
            self.cursor.execute('select * from Books where bookid=%s',(bookid,))
            book=self.cursor.fetchone()
            
            if not book:
                print('Book not found')
                return
            self.cursor.execute('''
            select *
            from IssueBooks
            where memberid=%s
            and bookid=%s
            and returndate is null''',(memberid, bookid))

            if self.cursor.fetchone():
                print('Member already borrowed this book')
                return
            
            if book[4]<=0:
                print('Book not available')
                return
            print(f'''
================================
Book Name : {book[1]}
Author    : {book[2]}
Available : {book[4]}
================================''')

            issuedate = date.today()
            duedate = issuedate + timedelta(days=14)
            
            self.cursor.execute("""
INSERT INTO IssueBooks
(issueid, memberid, bookid, issuedate, duedate, returndate, fine)
VALUES (%s, %s, %s, %s, %s, %s, %s)
""",(issueid, memberid, bookid, issuedate, duedate, None, 0))
            self.cursor.execute('update Books set quantity = quantity - 1 where bookid=%s',(bookid,))
            self.conn.commit()
            
            print('Book issued successfully!')
            
        except mysql.connector.IntegrityError:
            print("Issue ID already exists.")
        except mysql.connector.Error as e:
            print(e)
        except ValueError:
            print('Enter a integer')
    def return_book(self):
        try:
            issueid = int(input("Enter issue id = "))

            self.cursor.execute(
                "SELECT * FROM IssueBooks WHERE issueid=%s",
                (issueid,)
            )
            record = self.cursor.fetchone()

            if not record:
                print("Issue not found")
                return

            if record[5] is not None:
                print("Book already returned")
                return

            rdate = date.today()
            due_date = record[4]

            fine = 0
            if rdate > due_date:
                fine = (rdate - due_date).days * 5

            self.cursor.execute("""
                UPDATE IssueBooks
                SET returndate=%s,
                    fine=%s
                WHERE issueid=%s
            """, (rdate, fine, issueid))

            bookid = record[2]

            self.cursor.execute(
                "UPDATE Books SET quantity = quantity + 1 WHERE bookid=%s",
                (bookid,)
            )

            self.conn.commit()

            print(f"Book returned successfully! Fine = ₹{fine}")

        except ValueError:
            print("Issue ID must be a number.")
        except mysql.connector.Error as e:
            print("Database Error:", e)
            
    def member_history(self):
        memberid = int(input("Enter member id: "))

        self.cursor.execute("""
            SELECT b.title, i.issuedate, i.returndate
            FROM IssueBooks i
            JOIN Books b ON i.bookid = b.bookid
            WHERE i.memberid = %s
        """, (memberid,))

        rows = self.cursor.fetchall()

        if not rows:
            print("No borrowing history.")
            return

        for row in rows:
            print(f"""
Book        : {row[0]}
Issue Date  : {row[1]}
Return Date : {row[2] if row[2] else "Not Returned"}
    """)
            
    def most_issued_books(self):
        self.cursor.execute("""
            SELECT b.title, COUNT(*) AS issued
            FROM IssueBooks i
            JOIN Books b ON i.bookid = b.bookid
            GROUP BY b.bookid
            ORDER BY issued DESC
            LIMIT 5
        """)

        rows = self.cursor.fetchall()

        if not rows:
            print("No issued books.")
            return

        for row in rows:
            print(f"{row[0]} - Issued {row[1]} times")
            
    def view_issued_books(self):
        self.cursor.execute('''
        select i.issueid, m.membername, b.title,
        i.issuedate, i.returndate
        from Books b
        inner join IssueBooks i
        on b.bookid=i.bookid
        inner join Members m
        on m.memberid=i.memberid
        where i.returndate is null''')
        
        rows=self.cursor.fetchall()
        if not rows:
            print('No issued books found')
            return
        
        for row in rows:
            returndate = row[4] if row[4] else 'Not Returned'
            print(f'''
------------------------------------------------
Issue ID    = {row[0]}
Member      = {row[1]}
Book        = {row[2]}
Issue Date  = {row[3]}
Return Date = {returndate}
------------------------------------------------''')

    def calculate_fine(self):
        issueid = int(input("Enter issue id: "))

        self.cursor.execute("SELECT duedate FROM IssueBooks WHERE issueid=%s",(issueid,))
        row = self.cursor.fetchone()

        if not row:
            print("Issue not found.")
            return
        due = row[0]
        if date.today() <= due:
            print("No fine.")
        else:
            fine = (date.today() - due).days * 5
            print(f"Fine Amount = ₹{fine}")   
 
    def search_issued_book(self):
        try:
            issueid = int(input('Enter issue id= '))
    
            self.cursor.execute('''
                select i.issueid,m.membername,b.title,i.issuedate,i.returndate
                from IssueBooks i
                join Members m
                on i.memberid=m.memberid
                join Books b
                on i.bookid=b.bookid
                where i.issueid=%s''',(issueid,))
            row = self.cursor.fetchone()
            if not row:
                print('Issue not found')
                return
            returndate = row[4] if row[4] else 'Not Returned'
    
            print(f'''
----------------------------------
Issue ID    = {row[0]}
Member      = {row[1]}
Book        = {row[2]}
Issue Date  = {row[3]}
Return Date = {returndate}
----------------------------------''')
        except ValueError:
            print('Issue id must be a number.')

    def pending_returns(self):
        self.cursor.execute('''select i.issueid,m.membername,b.title,i.issuedate
        from IssueBooks i
        join Members m
        on i.memberid=m.memberid
        join Books b
        on i.bookid=b.bookid
        where i.returndate is null''')

        rows=self.cursor.fetchall()

        if not rows:
            print('No pending returns')
            return

        for row in rows:
            print(f'''
--------------------------------
Issue ID   : {row[0]}
Member     : {row[1]}
Book       : {row[2]}
Issue Date : {row[3]}
--------------------------------''')
    
    def dashboard(self):
        self.cursor.execute('select sum(quantity) from Books')
        total_books = self.cursor.fetchone()[0] or 0

        self.cursor.execute('select count(*) from Members')
        total_members = self.cursor.fetchone()[0]

        self.cursor.execute('select count(*) from IssueBooks')
        total_issued = self.cursor.fetchone()[0]

        self.cursor.execute('select count(*) from IssueBooks where returndate is null ')
        pending = self.cursor.fetchone()[0]

        self.cursor.execute('select count(*) from IssueBooks where returndate is not null')
        returned = self.cursor.fetchone()[0]

        print(f'''
====================================
            DASHBOARD
====================================
Total Books      : {total_books}
Total Members    : {total_members}
Books Issued     : {total_issued}
Books Returned   : {returned}
Pending Returns  : {pending}
====================================''')