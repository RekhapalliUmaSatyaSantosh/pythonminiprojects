class BankAccount:
    def __init__(self,account_number,holder_name,balance=0.0):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance
        self.transaction=[]
        if self.balance>0:
            self.transaction.append(f"Initial Amount: ₹{self.balance}")
    def deposit(self,amount):
        if amount>0:
            print('Money deposited=',amount)
            self.balance+=amount
            print('New Balance=',self.balance)
            self.transaction.append(f"Deposited: ₹{amount}")
        else:
            print('The amount should be positive')
    def withdrawl(self,amount):
        if amount >0 and amount<self.balance:
            print('Withdraw=',amount)
            self.balance-=amount
            print('New balance=',self.balance)
            self.transaction.append(f"Withdrew: ₹{amount}")
        else:
            print('Insufficient funds')
    def getbalance(self):
        return self.balance
    def showtransactions(self): 
        if not self.transaction:
            print("No transactions yet!")
        else:
            print("\n--- Transaction History ---")
            for i in self.transaction:
                print(i)
            print(f"Current Balance: ₹{self.balance}")
c=BankAccount('a1234','john',1000)
c.deposit(1200)
c.withdrawl(500)
c.getbalance()
c.showtransactions()
