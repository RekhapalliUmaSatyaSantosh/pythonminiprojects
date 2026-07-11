from database import Database
from tables import Tables
from books import Books
from members import Members
from issue_books import IssueBook

def menu():
    db=Database()
    tables=Tables(db)
    books=Books(db)
    members=Members(db)
    issuebook=IssueBook(db)
    
    tables.create_tables()
    while True:
        print("""
========== LIBRARY MANAGEMENT SYSTEM ==========
1.  Add Book
2.  View Books
3.  Search Book
4.  Update Book
5.  Delete Book
6.  Add Member
7.  View Members
8.  Search Member
9.  Update Member
10. Delete Member
11. Issue Book
12. Return Book
13. View Issued Books
14. Search Issued Book
15. Pending Return Books
16. Dashboard
17. Exit

===============================================
""")
        try:
            choice=int(input('Enter your choice= '))
            if choice==1:
                books.add_book()
            elif choice==2:
                books.view_books()
            elif choice==3:
                books.search_book()
            elif choice==5:
                books.delete_book()
            elif choice==4:
                books.update_book()
            elif choice==6:
                members.add_member()
            elif choice==7:
                members.view_member()
            elif choice==8:
                members.search_member()
            elif choice==9:
                members.update_member()
            elif choice==10:
                members.delete_member()
            elif choice==11:
                issuebook.issue_book()
            elif choice==12:
                issuebook.return_book()
            elif choice==13:
                issuebook.view_issued_books()
            elif choice==14:
                issuebook.search_issued_book()
            elif choice==15:
                issuebook.pending_returns()
            elif choice==16:
                issuebook.dashboard()
            elif choice==17:
                print('Thank you. Goodbye!')
                break
            else:
                print('Invalid option')
        except ValueError:
            print('Enter a number')
        input('\n Press Enter to continue.....')
    db.close()
