import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="*******",
            database="santosh"
        )
        self.cursor=self.conn.cursor()
    def close(self):
        self.cursor.close()
        self.conn.close()
    
class Create_Table:
    def __init__(self,db):
        self.conn=db.conn
        self.cursor=db.cursor
        
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts(
            acc_num BIGINT PRIMARY KEY,
            holder_name VARCHAR(50),
            phone BIGINT,
            pin INT,
            balance DECIMAL(10,2))""")
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INT AUTO_INCREMENT PRIMARY KEY,
        acc_num BIGINT,
        transaction_type VARCHAR(20),
        amount DECIMAL(10,2),
        transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (acc_num)REFERENCES accounts(acc_num))''')
        
        self.conn.commit()
        
class Account:
    def __init__(self,db):
        self.conn=db.conn
        self.cursor=db.cursor
    def create_account(self):
        try:
            acc_num = int(input("Enter Account Number: "))
            name = input("Enter Holder Name: ")
            phone = int(input("Enter Phone Number: "))
            pin = int(input("Enter 4-digit PIN: "))
            balance = float(input("Enter Initial Balance: "))
            
            if len(str(pin))!=4:
                print('The password should be 4-digit')
                return
            elif len(str(acc_num))!=8:
                print('The account number should be 8-digit')
                return
            elif len(str(phone))!=10:
                print('The phone number is not valid')
                return
            elif balance<=0:
                print('The Balance should be grater than zero')
                return
            
        except ValueError as e:
            print('Error:',e)
            return
        
        query=('''
            insert into accounts (acc_num,holder_name,phone,pin,balance)
            values(%s,%s,%s,%s,%s)''')
        values=(acc_num,name,phone,pin,balance)
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            print("Account created successfully.")
        except mysql.connector.Error as e:
            print("Error:", e)

class Authentication:
    def __init__(self, db):
        self.conn = db.conn
        self.cursor = db.cursor
        self.is_authenticated = False
        self.userid = None

    def login(self):
        acc_num = int(input("Enter Account Number: "))
        pin = int(input("Enter PIN: "))

        query = """
        SELECT acc_num, holder_name
        FROM accounts
        WHERE acc_num=%s AND pin=%s
        """

        self.cursor.execute(query, (acc_num, pin))
        result = self.cursor.fetchone()

        if result:
            self.userid = result[0]
            self.is_authenticated = True
            print(f"\nWelcome {result[1]}!")
            return True
        else:
            print("\nInvalid Account Number or PIN.")
            return False
        
class ATM:
    def __init__(self,db,auth):
        self.conn=db.conn
        self.cursor=db.cursor
        self.auth=auth
    
    def check_balance(self):
        query='select balance from accounts where acc_num=%s'
        self.cursor.execute(query,(self.auth.userid,))
        result=self.cursor.fetchone()
        if result:
            print(f"Available Balance: ₹{result[0]}")
        else:
            print('Account not found')
    
    def deposit(self):
        try:
            amount=float(input('Enter amount to be deposit= '))
            
            if amount<=0:
                print("Invalid Amount.")
                return
            else:
                query='update accounts set balance=balance+%s where acc_num=%s'
                self.cursor.execute(query,(amount,self.auth.userid))
            print('Deposited successfully!')
            
            query = """
            INSERT INTO transactions (acc_num, transaction_type, amount)
            VALUES (%s, %s, %s)
            """

            self.cursor.execute(query, (self.auth.userid, "Deposit", amount))
            self.conn.commit()
        except ValueError:
            print('Enter a number')
        
    def withdrawal(self):
        try:
            amount=float(input('Enter amount to Withdrawn= '))
            
            query = "SELECT balance FROM accounts WHERE acc_num=%s"
            self.cursor.execute(query, (self.auth.userid,))
            balance = self.cursor.fetchone()[0]
            
            if amount>balance:
                print("Insufficient funds.")
                return
            
            query='update accounts set balance=balance-%s where acc_num=%s'
            self.cursor.execute(query, (amount, self.auth.userid))

            print("Amount withdraw successfully.")
            
            query = """
            INSERT INTO transactions (acc_num, transaction_type, amount)
            VALUES (%s, %s, %s)
            """

            self.cursor.execute(query, (self.auth.userid, "Withdraw", amount))
            self.conn.commit()
        except ValueError:
            print('Enter a number')
    
    def mini_statement(self):
        query = """
        SELECT transaction_type, amount, transaction_date
        FROM transactions
        WHERE acc_num=%s
        ORDER BY transaction_date DESC
        LIMIT 5
        """

        self.cursor.execute(query, (self.auth.userid,))
        result = self.cursor.fetchall()

        if not result:
            print("No transactions found.")
            return

        print("\n------------ Mini Statement ------------------")
        print(f"{'Type':<25}{'Amount':<15}{'Date'}")

        for row in result:
            print(f"{row[0]:<25}{row[1]:<15}{row[2]}")

        print("------------------------------------------------")
    
    def money_transfer(self):
        try:
            accnum=int(input('Enter Reciever account number= '))
            
            if accnum == self.auth.userid:
                print("You cannot transfer money to your own account.")
                return
            
            query='select * from accounts where acc_num=%s'
            self.cursor.execute(query,(accnum,))
            row = self.cursor.fetchone()
            if not row:
                print('Account not found')
                return
            else:
                print(f'Name={row[1]}')
            amount=float(input('Enter amount to transfer= '))
            if amount <= 0:
                print("Amount should be greater than zero.")
                return
            
            query = "SELECT balance FROM accounts WHERE acc_num=%s"
            self.cursor.execute(query, (self.auth.userid,))
            balance = self.cursor.fetchone()[0]
            
            if balance<amount:
                print('Insufficient Funds.')
                return
            query='update accounts set balance=balance-%s where acc_num=%s'
            self.cursor.execute(query,(amount,self.auth.userid))
            
            query1='update accounts set balance=balance+%s where acc_num=%s'
            self.cursor.execute(query1,(amount,accnum))
            
            query = """
            INSERT INTO transactions(acc_num, transaction_type, amount)
            VALUES(%s, %s, %s)
            """
            self.cursor.execute(query, (self.auth.userid, "Transfer Sent", amount))
            
            self.cursor.execute(query, (accnum, "Transfer Received", amount))
            
            self.conn.commit()
            print('Transaction completed.')
        except ValueError:
            print("Invalid input.")

        except mysql.connector.Error as e:
            self.conn.rollback()
            print("Database Error:", e)
    
    def change_pin(self):
        try:
            pin=int(input('Enter existing pin= '))
            query='select pin from accounts where acc_num=%s'
            self.cursor.execute(query,(self.auth.userid,))
            row=self.cursor.fetchone()
            if pin!=row[0]:
                print('Invalid pin.')
                return
            new_pin=int(input('Enter new pin= '))
            if not isinstance(new_pin,int):
                print('Enter a number')
                return
            if pin==new_pin:
                print('New pin is not the Old pin')
                return
            if len(str(new_pin))!=4:
                print('Please enter 4-digit pin.')
                return
            query1='update accounts set pin=%s where acc_num=%s'
            self.cursor.execute(query1,(new_pin,self.auth.userid))
            self.conn.commit()
            print('Changed pin successfully.')
        except ValueError:
            print('Invalid input')
        except mysql.connector.Error as e:
            print('Error:',e)
    
    def change_phone(self):
        try:
            new_phone=int(input('Enter new phone number= '))
            if len(str(new_phone))!=10:
                print('Invalid number.')
                return
            query='update accounts set phone=%s where acc_num=%s'
            self.cursor.execute(query,(new_phone,self.auth.userid))
            self.conn.commit()
            print('Phone number updated.')
        except ValueError:
            print('Invalid input')
        except mysql.connector.Error as e:
            print('Error:',e)
    
    def delete_account(self):
        try:
            choice = input("Are you sure you want to delete your account? (Y/N): ").upper()

            if choice != "Y":
                print("Account deletion cancelled.")
                return

            query = "DELETE FROM transactions WHERE acc_num=%s"
            self.cursor.execute(query, (self.auth.userid,))

            query = "DELETE FROM accounts WHERE acc_num=%s"
            self.cursor.execute(query, (self.auth.userid,))

            self.conn.commit()

            self.auth.is_authenticated = False
            self.auth.userid = None

            print("Account deleted successfully.")

        except mysql.connector.Error as e:
            self.conn.rollback()
            print("Error:", e)
        

def menu():
    db=Database()
    tables=Create_Table(db)
    acc=Account(db)
    auth=Authentication(db)
    atm=ATM(db,auth)
    tables.create_table()
    while True:
        print("""
========== ATM SERVICES ==========

1.  Create Account
2.  Login
3.  Check Balance
4.  Deposit
5.  Withdraw
6.  Transfer Money
7.  Mini Statement
8.  Change PIN
9.  Update Phone
10. Delete Account
11. Exit

===================================
""")        
        try:
            
            choice=int(input('Enter your choice= '))
            if choice==1:
                acc.create_account()
            elif choice==2:
                auth.login()
            elif choice==3:
                if not auth.is_authenticated:
                    print("Please login first.")
                    continue
                atm.check_balance()
            elif choice==4:
                if not auth.is_authenticated:
                    print("Please login first.")
                    continue
                atm.deposit()
            elif choice==5:
                if not auth.is_authenticated:
                    print("Please login first.")
                    continue
                atm.withdrawal()
            elif choice==6:
                if not auth.is_authenticated:
                    print("Please login first.")
                atm.money_transfer()
            elif choice==7:
                if not auth.is_authenticated:
                    print("Please login first.")
                    continue
                atm.mini_statement()
            elif choice==8:
                if not auth.is_authenticated:
                    print("Please login first.")
                    continue
                atm.change_pin()
            elif choice==9:
                if not auth.is_authenticated:
                    print("Please login first.")
                    continue
                atm.change_phone()
            elif choice==10:
                if not auth.is_authenticated:
                    print("Please login first.")
                    continue
                atm.delete_account()
            elif choice==11:
                print('Thank for using ATM! Visit Again......')
                break
            else:
                print('Invalid choice. Please choose between 1-11')
                
        except ValueError:
            print('Enter a digit')
        input('\n Press Enter to continue.....')
if __name__=='__main__':
    db=Database()
    try:
        menu()
    except KeyboardInterrupt:
        print('\nProgram terminated')
    finally:
        db.close()
