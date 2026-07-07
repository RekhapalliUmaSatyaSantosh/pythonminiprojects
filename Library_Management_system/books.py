import sqlite3
    
class Books:
    def __init__(self, db):
        self.conn = db.conn
        self.cursor = db.cursor
    
    def add_book(self):
        try:
            bookid=int(input('Enter book id= '))
            title=input('Enter book title= ')
            author=input('Enter author name= ')
            publisher=input('Enter Publisher name= ')
            quantity=int(input('Enter no.of books= '))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return
            self.cursor.execute('insert into Books values(?,?,?,?,?)',(bookid,title,author,publisher,quantity))
            self.conn.commit()
            print('Book added successfully!')
        except ValueError:
            print("Book ID and quantity must be a number.")
        except sqlite3.IntegrityError:
            print("Book ID already exists.")
            
    def view_books(self):
        self.cursor.execute('select * from Books')
        rows=self.cursor.fetchall()
        if not rows:
            print('No Books found.')
        else:
            for row in rows:
                print(f'''
-----------------------------------  
Book ID         = {row[0]}
Book Name       = {row[1]}
Book Author     = {row[2]}
Book Publisher  = {row[3]}
Available Books = {row[4]}
-----------------------------------
    ''')
    def search_book(self):
        try:
            choose=int(input('1.Search by Book ID \n2.Search by Book Name \nEnter your choice= '))
            if choose==1:
                try:
                    bookid=int(input('Enter Book id= '))
                    self.cursor.execute('select * from Books where bookid=?',(bookid,))
                    row=self.cursor.fetchone()
                    if row:
                        print(f"""
-----------------------------------
Book ID         = {row[0]}
Book Name       = {row[1]}
Book Author     = {row[2]}
Book Publisher  = {row[3]}
Available Books = {row[4]}
-----------------------------------
    """)
                    else:
                        print('Book not found')
                except Exception as e:
                    print(e)
            elif choose==2:
                bookname=input('Enter Book Name= ')
                self.cursor.execute('select * from Books where title like ?',('%'+bookname+'%',))
                rows=self.cursor.fetchall()
                if not rows:
                    print('Book not found')
                    return
                for row in rows:
                    print(f"""
-----------------------------------
Book ID         = {row[0]}
Book Name       = {row[1]}
Book Author     = {row[2]}
Book Publisher  = {row[3]}
Available Books = {row[4]}
-----------------------------------
    """)
        except Exception as f:
            print(f)
            
    def update_book(self):
        bookid=int(input('Enter Book id= '))
        self.cursor.execute('select * from Books where bookid=?',(bookid,))
        row=self.cursor.fetchone()
        if not row:
            print('Book Id not found')
            return
        
        print('''
1. Update Title
2. Update Author
3. Update Publisher
4. Update Quantity''')
        choice=int(input('Enter your choice= '))
        if choice==1:
            new_value=input('Enter new title= ')
            self.cursor.execute('update Books set title=? where bookid=?',(new_value,bookid))
        elif choice==2:
            new_value=input('Enter new Author= ')
            self.cursor.execute('update Books set author=? where bookid=?',(new_value,bookid))
        elif choice==3:
            new_value=input('Enter new Publisher= ')
            self.cursor.execute('update Books set publisher=? where bookid=?',(new_value,bookid))
        elif choice==4:
            new_value=int(input('Enter new no.of books= '))
            if new_value < 0:
                print('Quantity cannot be negative')
                return
            self.cursor.execute('update Books set quantity=? where bookid=?',(new_value,bookid))
        else:
            print('Invalid choice')
            return
        
        self.conn.commit()
        print('Book updated successfully!')

    def delete_book(self):
        bookid=int(input('Enter Book id= '))
        self.cursor.execute('select * from Books where bookid=?',(bookid,))
        row=self.cursor.fetchone()
        if not row:
            print('Book not found')
            return
        self.cursor.execute(
            '''
            select *
            from IssueBooks
            where bookid=?
            and returndate is null
            ''',
            (bookid,))
        if self.cursor.fetchone():
            print('Book is currently issued')
            return
        
        confirm=input('Do you want delete this record? (y/n)= ').lower()
        if confirm=='y':
            self.cursor.execute('delete from Books where bookid=?',(bookid,))
            self.conn.commit()
            print('Book deleted successfully')
        else:
            print('Delete cancelled')
