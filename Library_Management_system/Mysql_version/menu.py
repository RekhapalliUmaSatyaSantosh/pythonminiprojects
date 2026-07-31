from books import Books
from issuedbooks import IssueBook
from members import Members

def menu(db):
    books=Books(db)
    members=Members(db)
    issuebook=IssueBook(db)
    while True:
        print('''
╔════════════════════════════════════════╗
║      LIBRARY MANAGEMENT SYSTEM         ║
╠════════════════════════════════════════╣
║  1.  Add Book                          ║
║  2.  View Books                        ║
║  3.  Search Book                       ║
║  4.  Update Book                       ║
║  5.  Delete Book                       ║
║  6.  Add Member                        ║
║  7.  View Members                      ║
║  8.  Search Member                     ║
║  9.  Update Member                     ║
║  10. Delete Member                     ║
║  11. Issue Book                        ║
║  12. Return Book                       ║
║  13. View Issued Books                 ║
║  14. Search Issued Book                ║
║  15. Pending Return Books              ║
║  16. Dashboard                         ║
║  17. Search by Author                  ║
║  18. Search by Publisher               ║
║  19. Available Books                   ║
║  20. Out of Stock Books                ║
║  21. Member Borrow History             ║
║  22. Most Issued Books                 ║
║  23. Calculate Fine                    ║
║  24. Exit                              ║
╚════════════════════════════════════════╝''')
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
                books.search_by_author()
            elif choice==18:
                books.search_by_publisher()
            elif choice==19:
                books.available_books()
            elif choice==20:
                books.out_of_stock_books()
            elif choice==21:
                issuebook.member_history()
            elif choice==22:
                issuebook.most_issued_books()
            elif choice==23:
                issuebook.calculate_fine()
            elif choice==24:
                print('Thank you. Goodbye!')
                break
            else:
                print('Invalid option')
        except ValueError:
            print('Enter a number')
        input('\n Press Enter to continue.....')
