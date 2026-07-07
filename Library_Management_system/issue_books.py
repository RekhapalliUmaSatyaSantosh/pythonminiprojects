import sqlite3

class IssueBook:
    def __init__(self,db):
        self.conn = db.conn
        self.cursor = db.cursor
    
    def issue_book(self):
        try:
            issueid=int(input('Enter issue id= '))
            memberid=int(input('Enter member id= '))
            self.cursor.execute('select * from Members where memberid=?',(memberid,))
            member=self.cursor.fetchone()
            if not member:
                print('Member not found')
                return
            bookid=int(input('Enter book id= '))
            self.cursor.execute('select * from Books where bookid=?',(bookid,))
            book=self.cursor.fetchone()
            if not book:
                print('Book not found')
                return
            self.cursor.execute(
                        '''
                        select *
                        from IssueBooks
                        where memberid=?
                        and bookid=?
                        and returndate is null
                        ''',
                        (memberid, bookid)
                    )

            if self.cursor.fetchone():
                print('Member already borrowed this book')
                return
            if book[4]<=0:
                print('Book not available')
                return
            print(f'''
Book Name : {book[1]}
Author    : {book[2]}
Available : {book[4]}
''')
            issuedate=input('Enter the issue date (DD-MM-YYYY/YY)= ')
            self.cursor.execute('insert into IssueBooks values(?,?,?,?,?)',(issueid,memberid,bookid,issuedate,None))
            self.cursor.execute('update Books set quantity = quantity - 1 where bookid=?',(bookid,))
            self.conn.commit()
            print('Book issued successfully!')
        except sqlite3.IntegrityError:
            print('Issue ID already exists')
        except ValueError:
            print('Enter a integer')
    
    def return_book(self):
        issueid = int(input('Enter issue id= '))
        self.cursor.execute('select * from IssueBooks where issueid=?',(issueid,))
        record = self.cursor.fetchone()
        if not record:
            print('Issue not found')
            return
        if record[4] is not None:
            print('Book already returned')
            return
        rdate = input('Enter return date (DD-MM-YYYY)= ')
        self.cursor.execute('update IssueBooks set returndate=? where issueid=?',(rdate, issueid))
        bookid = record[2]
        self.cursor.execute('update Books set quantity = quantity + 1 where bookid=?',(bookid,))

        self.conn.commit()
        print('Book returned successfully!')
    
    def view_issued_books(self):
        self.cursor.execute(
            '''select i.issueid, m.membername, b.title,
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
            print(
                f'''
------------------------------------------------
Issue ID    = {row[0]}
Member      = {row[1]}
Book        = {row[2]}
Issue Date  = {row[3]}
Return Date = {returndate}
------------------------------------------------
                '''
            )
    def search_issued_book(self):
        issueid = int(input('Enter issue id= '))

        self.cursor.execute(
            '''
            select i.issueid,
                m.membername,
                b.title,
                i.issuedate,
                i.returndate
            from IssueBooks i
            join Members m
            on i.memberid=m.memberid
            join Books b
            on i.bookid=b.bookid
            where i.issueid=?
            ''',
            (issueid,)
        )

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
----------------------------------
    ''')
    
    def pending_returns(self):
        self.cursor.execute(
            '''
            select i.issueid,
                m.membername,
                b.title,
                i.issuedate
            from IssueBooks i
            join Members m
            on i.memberid=m.memberid
            join Books b
            on i.bookid=b.bookid
            where i.returndate is null
            '''
        )

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
--------------------------------
    ''')
        
    def dashboard(self):
        self.cursor.execute('select sum(quantity) from Books')
        total_books = self.cursor.fetchone()[0]

        self.cursor.execute('select count(*) from Members')
        total_members = self.cursor.fetchone()[0]

        self.cursor.execute('select count(*) from IssueBooks')
        total_issued = self.cursor.fetchone()[0]

        self.cursor.execute(
            '''
            select count(*)
            from IssueBooks
            where returndate is null
            '''
        )
        pending = self.cursor.fetchone()[0]

        self.cursor.execute(
            '''
            select count(*)
            from IssueBooks
            where returndate is not null
            '''
        )
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

====================================
    ''')
