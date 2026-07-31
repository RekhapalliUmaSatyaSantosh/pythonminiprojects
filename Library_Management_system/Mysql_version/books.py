import mysql.connector

class Books:
    
    def __init__(self,db):
          self.conn=db.conn
          self.cursor=db.cursor
    
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
            query='insert into books (bookid,title,author,publisher,quantity) values(%s,%s,%s,%s,%s)'
            values=(bookid,title,author,publisher,quantity)
            self.cursor.execute(query,values)
            self.conn.commit()
            print('Book added successfully!')
        except ValueError:
            print('Bookid must be a number.')
        except Exception as e:
            print('Error: ',e)
    
    def view_books(self):
        self.cursor.execute('select * from books')
        rows=self.cursor.fetchall()
        if not rows:
            print('No books found')
            return
        for row in rows:
            status = "Available" if row[4] > 0 else "Out of Stock"
            print(f"""
-----------------------------------
Book ID         : {row[0]}
Book Name       : {row[1]}
Author          : {row[2]}
Publisher       : {row[3]}
Quantity        : {row[4]}
Status          : {status}
-----------------------------------""")
            
    def search_book(self):
        try:
            choose=int(input('1.Search by Book ID \n2.Search by Book Name \n#.Search by Author \n 4.Search by Publihser \nEnter your choice= '))
            if choose==1:
                try:
                    bookid=int(input('Enter book id= '))
                    self.cursor.execute('select * from Books where bookid=%s',(bookid,))
                    row=self.cursor.fetchone()
                    if row:
                        print(f"""
-----------------------------------
Book ID         = {row[0]}
Book Name       = {row[1]}
Book Author     = {row[2]}
Book Publisher  = {row[3]}
Available Books = {row[4]}
-----------------------------------""")
                    else:
                        print('No book found.')
                except ValueError:
                    print('Bookid must be number.')
            elif choose==2:
                bookname=input('Enter Bookname= ')
                self.cursor.execute('select * from books where title like %s',('%'+bookname+'%'))
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
-----------------------------------""")
            elif choose==3:
                self.search_by_author()
            elif choose==4:
                self.search_by_publisher()
                
        except Exception as e:
            print('Error: ',e)
    
    def search_by_author(self):
        author = input("Enter author name: ")
        self.cursor.execute(
            "SELECT * FROM Books WHERE author LIKE %s",
            ('%' + author + '%',)
        )
        rows = self.cursor.fetchall()

        if not rows:
            print("No books found.")
            return

        for row in rows:
            print(f"""
Book ID   : {row[0]}
Title     : {row[1]}
Author    : {row[2]}
Publisher : {row[3]}
Quantity  : {row[4]}
""")
            
    def search_by_publisher(self):
        publisher = input("Enter publisher name: ")
        self.cursor.execute(
            "SELECT * FROM Books WHERE publisher LIKE %s",
            ('%' + publisher + '%',)
        )
        rows = self.cursor.fetchall()

        if not rows:
            print("No books found.")
            return

        for row in rows:
            print(f"""
Book ID   : {row[0]}
Title     : {row[1]}
Author    : {row[2]}
Publisher : {row[3]}
Quantity  : {row[4]}
""")
    
    def available_books(self):
        self.cursor.execute(
            "SELECT * FROM Books WHERE quantity > 0"
        )
        rows = self.cursor.fetchall()

        if not rows:
            print("No books available.")
            return

        for row in rows:
            print(f"""
Book ID   : {row[0]}
Title     : {row[1]}
Author    : {row[2]}
Publisher : {row[3]}
Quantity  : {row[4]}
""")
            
    def out_of_stock_books(self):
        self.cursor.execute(
            "SELECT * FROM Books WHERE quantity = 0"
        )
        rows = self.cursor.fetchall()

        if not rows:
            print("No out-of-stock books.")
            return

        for row in rows:
            print(f"""
Book ID   : {row[0]}
Title     : {row[1]}
Author    : {row[2]}
Publisher : {row[3]}
Quantity  : {row[4]}
""")
        
    def update_book(self):
        try:
            bookid=int(input('Enter Book id= '))
            self.cursor.execute('select * from Books where bookid=%s',(bookid,))
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
                self.cursor.execute('update Books set title=%s where bookid=%s',(new_value,bookid))
            elif choice==2:
                new_value=input('Enter new Author= ')
                self.cursor.execute('update Books set author=%s where bookid=%s',(new_value,bookid))
            elif choice==3:
                new_value=input('Enter new Publisher= ')
                self.cursor.execute('update Books set publisher=%s where bookid=%s',(new_value,bookid))
            elif choice==4:
                new_value=int(input('Enter new no.of books= '))
                if new_value < 0:
                    print('Quantity cannot be negative')
                    return
                self.cursor.execute('update Books set quantity=%s where bookid=%s',(new_value,bookid))
            else:
                print('Invalid choice')
                return
            
            self.conn.commit()
            print('Book updated successfully!')
        except ValueError:
            print('Bookid must be number.')
        except mysql.connector.Error as e:
            print(e)
  
    def delete_book(self):
        
        bookid=int(input('Enter Book id= '))
        self.cursor.execute('select * from Books where bookid=%s',(bookid,))
        row=self.cursor.fetchone()
        if not row:
            print('Book not found')
            return
        self.cursor.execute(
            '''
            select *
            from IssueBooks
            where bookid=%s
            and returndate is null
            ''',
            (bookid,))
        if self.cursor.fetchone():
            print('Book is currently issued')
            return
        
        confirm=input('Do you want delete this record? (y/n)= ').lower()
        if confirm=='y':
            self.cursor.execute('delete from Books where bookid=%s',(bookid,))
            self.conn.commit()
            print('Book deleted successfully')
        else:
            print('Delete cancelled')