import mysql.connector
class atm:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='santosh@1503',
            database='santosh'
            )
        self.cursor=self.conn.cursor()
        self.userid=None
        self.is_authenticated=False
    def authenticate(self,enterpin):
        query="select acc from atm where pin=%s"
        self.cursor.execute(query,(enterpin,))
        result=self.cursor.fetchone()
        if result:
            self.userid=result[0]
            self.is_authenticated=True
            print("Authentication successful!")
        else:
            print('Authentication failed. Please try again.')

    def check_balance(self):
        if not self.is_authenticated:
            print('Authenticate first')
            return
        query="select bal from atm where acc=%s"
        self.cursor.execute(query,(self.userid,))
        balance=self.cursor.fetchone()[0]
        print(f'Your Current Balance=₹{balance:.2f}')
    def withdraw(self,amount):
        if not self.is_authenticated:
            print('Authenticate first')
            return
        query="select bal from atm where acc=%s"
        self.cursor.execute(query,(self.userid,))
        balance=self.cursor.fetchone()[0]
        if amount > balance:
            print('Insufficient funds')
        elif amount <= 0:
            print('Withdrawal amount must be positive')
        else:
            newbalance=balance - amount
            updatequery="update atm set bal=%s where acc=%s"
            self.cursor.execute(updatequery,(newbalance,self.userid))
            self.conn.commit()
            print(f'Successfully withdrew: ₹{amount:.2f}')

    def deposite(self,amount):
        if not self.is_authenticated:
            print('Authenticate first')
            return
        if amount<=0:
            print('Deposit amount must be positive')
        else:
            query="select bal from atm where acc=%s"
            self.cursor.execute(query,(self.userid,))
            balance=self.cursor.fetchone()[0]
            newbalance=balance + amount
            updatequery="update atm set bal=%s where acc=%s"
            self.cursor.execute(updatequery,(newbalance,self.userid))
            self.conn.commit()
            print(f'Successfully deposited: ₹{amount:.2f}')
    def close(self):
        self.cursor.close()
        self.conn.close()
a=atm()
authenticated = False
while not authenticated:
    print("\nPlease authenticate to proceed.")
    pin_input = input("Enter your PIN: ")
    a.authenticate(pin_input)
    authenticated = a.is_authenticated 

while True:
    print("\n--- Menu ---")
    print("c - Check Balance")
    print("d - Deposit")
    print("w - Withdraw")
    print("e - Exit")
    choice=input("Enter your Choice: ")

    if choice.lower()=='c':
        a.check_balance()
    elif choice.lower()=='d':
        try:
            amount=float(input('Enter amount to deposit: '))
            a.deposite(amount)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice.lower()=='w':
        try:
            amount=float(input('Enter amount to withdraw: '))
            a.withdraw(amount)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice.lower()=='e':
        print('Thanks for using ATM! Visit Again......')
        break
    else:
        print('Please choose a valid option.')
