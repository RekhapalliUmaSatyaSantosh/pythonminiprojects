from menu import menu
from database import Database

if __name__=='__main__':
    db=Database()
    try:
        menu(db)
    except KeyboardInterrupt:
        print('\nProgram terminated')
    finally:
        db.close()