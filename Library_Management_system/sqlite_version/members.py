import sqlite3

class Members:
    def __init__(self, db):
        self.conn = db.conn
        self.cursor = db.cursor
        
    def add_member(self):
        try:
            memberid=int(input('Enter Member id= '))
            mname=input('Enter Member name= ')
            phone=input('Enter phone= ')
            email=input('Enter email= ')
            self.cursor.execute('insert into Members values(?,?,?,?)',(memberid,mname,phone,email))
            self.conn.commit()
            print('Member added successfully!')
        except ValueError:
            print("Member ID must be a number.")
        except sqlite3.IntegrityError as e:
            print(e)
    
    def view_member(self):
        self.cursor.execute('select * from Members')
        rows=self.cursor.fetchall()
        if not rows:
            print('No Member found.')
        else:
            for row in rows:
                print(f'''
-----------------------------------  
Member ID   = {row[0]}
Member Name = {row[1]}
Phone       = {row[2]}
Email       = {row[3]}
-----------------------------------
    ''')
                
    def search_member(self):
        try:
            choose=int(input('1.Search by Member ID \n2.Search by Member Name \nEnter your choice= '))
            if choose==1:
                try:
                    memberid=int(input('Enter Member id= '))
                    self.cursor.execute('select * from Members where memberid=?',(memberid,))
                    row=self.cursor.fetchone()
                    if row:
                        print(f"""
-----------------------------------
Member ID   = {row[0]}
Member Name = {row[1]}
Phone       = {row[2]}
Email       = {row[3]}
-----------------------------------
    """)
                    else:
                        print('Member not found')
                except Exception as e:
                    print(e)
            elif choose==2:
                mname=input('Enter Member Name= ')
                self.cursor.execute('select * from Members where membername like ?',('%'+mname+'%',))
                rows=self.cursor.fetchall()
                if rows:
                    for row in rows:
                        print(f"""
-----------------------------------
Member ID   = {row[0]}
Member Name = {row[1]}
Phone       = {row[2]}
Email       = {row[3]}
-----------------------------------
    """)
                else:
                    print('Member not found')
        except Exception as f:
            print(f)
    
    def update_member(self):
        memberid=int(input('Enter Member id= '))
        self.cursor.execute('select * from Members where memberid=?',(memberid,))
        row=self.cursor.fetchone()
        if not row:
            print('Member id not found')
            return
        
        print('''
1. Update Name
2. Update phone
3. Update Email''')
        choice=int(input('Enter your choice= '))
        if choice==1:
            new_value=input('Enter new name= ')
            self.cursor.execute('update Members set membername=? where memberid=?',(new_value,memberid))
        elif choice==2:
            new_value=input('Enter new phone number= ')
            self.cursor.execute('update Members set phone=? where memberid=?',(new_value,memberid))
        elif choice==3:
            new_value=input('Enter new Email= ')
            self.cursor.execute('update Members set email=? where memberid=?',(new_value,memberid))
        else:
            print('Invalid choice')
            return
        
        self.conn.commit()
        print('Member updated successfully!')

    def delete_member(self):
        memid=int(input('Enter Member id= '))
        self.cursor.execute('select * from Members where memberid=?',(memid,))
        row=self.cursor.fetchone()
        if not row:
            print('Member not found')
            return
        self.cursor.execute(
                '''
                select *
                from IssueBooks
                where memberid=?
                and returndate is null
                ''',
                (memid,))

        if self.cursor.fetchone():
            print('Member has borrowed books')
            return
        
        confirm=input('Do you want delete this record? (y/n)= ').lower()
        if confirm=='y':
            self.cursor.execute('delete from Members where memberid=?',(memid,))
            self.conn.commit()
            print('Member deleted successfully')
        else:
            print('Delete cancelled')