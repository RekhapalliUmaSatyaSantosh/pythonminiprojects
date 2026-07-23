import mysql.connector
from datetime import datetime

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Santosh@1503",
            database="expense_tracker"
        )
        self.cursor=self.conn.cursor()
        
    def close(self):
        self.cursor.close()
        self.conn.close()

class Transaction:
    def __init__(self, db):
        self.conn = db.conn
        self.cursor = db.cursor

    def add_transaction(self):
        try:
            date = input("Enter date (YYYY-MM-DD): ")
            transaction_type = input("Enter type (Income/Expense): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")

            query = """
            insert into transactions
            (transaction_date, transaction_type, category, amount, description)
            values (%s, %s, %s, %s, %s)
            """

            values = (
                date,
                transaction_type,
                category,
                amount,
                description
            )

            self.cursor.execute(query, values)
            self.conn.commit()

            print("Transaction added successfully.")
        except ValueError:
            print('Amount must be a number')
            
    def view_transactions(self):
        self.cursor.execute('select * from transactions')
        print("\n" + "=" * 80)
        print("ALL TRANSACTIONS")
        print("=" * 80)
        print(
            f"{'ID':<5} "
            f"{'Date':<12} "
            f"{'Type':<10} "
            f"{'Category':<15} "
            f"{'Amount':<10} "
            f"Description"
        )
        print("-" * 80)
        result=self.cursor.fetchall()
        if not result:
            print('Not tranasctions found')
            return
        for transaction in result:
            print(
                f"{transaction[0]:<5} "
                f"{str(transaction[1]):<12} "
                f"{transaction[2]:<10} "
                f"{transaction[3]:<15} "
                f"₹{transaction[4]:<10.2f} "
                f"{transaction[5]}"
            )
        
    def search_transaction(self):
        print("\n" + "=" * 50)
        print("SEARCH TRANSACTION")
        print("=" * 50)
        try:
            
            transaction_id = input("Enter Transaction ID: ")
            query='select * from transactions where transaction_id=%s'
            self.cursor.execute(query,(transaction_id,))
            result=self.cursor.fetchone()
            if not result:
                print('No transaction found')
                return
            print("\n" + "-" * 80)

            print(
                f"{'ID':<5} "
                f"{'Date':<12} "
                f"{'Type':<10} "
                f"{'Category':<15} "
                f"{'Amount':<10} "
                f"Description"
            )

            print("-" * 80)

            print(
                f"{result[0]:<5} "
                f"{str(result[1]):<12} "
                f"{result[2]:<10} "
                f"{result[3]:<15} "
                f"₹{result[4]:<10.2f} "
                f"{result[5]}"
            )
        except ValueError:
            print('Enter a number')    
        
    def update_transaction(self):

        print("\n" + "=" * 50)
        print("UPDATE TRANSACTION")
        print("=" * 50)
        try:
            
            transaction_id = int(input("Enter Transaction ID: "))
            
            check_query = """
            SELECT *
            FROM transactions
            WHERE transaction_id = %s
            """

            self.cursor.execute(check_query, (transaction_id,))
            result = self.cursor.fetchone()

            if not result:
                print("No transaction found.")
                return

            print("\nCurrent Transaction:")
            print(result)

            print("\nEnter New Details")

            date = input("Enter date (YYYY-MM-DD): ")
            transaction_type = input("Enter type (Income/Expense): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")

            update_query = """
            UPDATE transactions
            SET transaction_date = %s,
                transaction_type = %s,
                category = %s,
                amount = %s,
                description = %s
            WHERE transaction_id = %s
            """

            values = (
                date,
                transaction_type,
                category,
                amount,
                description,
                transaction_id
            )

            self.cursor.execute(update_query, values)

            self.conn.commit()

            print("Transaction updated successfully.")
        except ValueError:
            print('Transaction ID and amount must be valid numbers')
            
    def delete_transaction(self):
        print("\n" + "=" * 50)
        print("DELETE TRANSACTION")
        print("=" * 50)
        try:
            transaction_id=int(input('Enter id= '))
            query1='select * from transactions where transaction_id=%s'
            self.cursor.execute(query1,(transaction_id,))
            res=self.cursor.fetchone()
            if not res:
                print('No transaction found')
                return
            print('\n Transaction to be deleted= ')
            print(res)
            confirmation = input( "\nAre you sure you want to delete this transaction? (y/n): " ).lower() 
            if confirmation != "y": 
                print("Deletion cancelled.") 
                return
            query='delete from transactions where transaction_id=%s'
            self.cursor.execute(query,(transaction_id,))
            self.conn.commit()
            print('Transaction deleted successfully')
        except ValueError:
            print('Transaction ID must be valid number')
class Report:
    def __init__(self,db):
        self.conn=db.conn
        self.cursor=db.cursor
    
    def total_income(self):
        print("\n" + "=" * 50)
        print("TOTAL INCOME")
        print("=" * 50)
        query='select sum(amount) from transactions where transaction_type = %s'
        self.cursor.execute(query,('Income',))
        result=self.cursor.fetchone()
        if result[0] is None:
            print('No income')
            return
        print(f'Total income= ₹{result[0]:.2f}')
    
    def total_expense(self):
        print("\n" + "=" * 50)
        print("TOTAL EXPENSES")
        print("=" * 50)
        query='select sum(amount) from transactions where transaction_type=%s'
        self.cursor.execute(query,('Expense',))
        result=self.cursor.fetchone()
        if result[0] is None:
            print('No expense')
            return
        print(f'Total Expenses= ₹{result[0]:.2f}')
    def current_balance(self):
        print("\n" + "=" * 50)
        print("CURRENT BALANCE")
        print("=" * 50)
        query1='select sum(amount) from transactions where transaction_type = %s'
        self.cursor.execute(query1,('Income',))
        income=self.cursor.fetchone()[0]
        if income is None:
            income=0
        query2='select sum(amount) from transactions where transaction_type=%s'
        self.cursor.execute(query2,('Expense',))
        expense=self.cursor.fetchone()[0]
        if expense is None:
            expense=0
        result=income-expense
        print(f"Total Income = ₹{income:.2f}") 
        print(f"Total Expenses = ₹{expense:.2f}")
        print("-" * 30)
        print(f'Current Balance= ₹{result:.2f}')
    
    def category_wise_expenses(self):
        print("\n" + "=" * 50)
        print("CATEGORY-WISE EXPENSES")
        print("=" * 50)
        query='''select category,sum(amount)
        from transactions 
        where transaction_type=%s 
        group by category 
        order by sum(amount) desc'''
        self.cursor.execute(query,('Expense',))
        result=self.cursor.fetchall()
        if not result:
            print('No expenses found')
            return
        print(f"{'Category':<20} {'Total Amount':>15}")
        print('-'*40)
        for category, total_amount in result: 
            amount = f"₹{total_amount:.2f}"
            print(f"{category:<20}{amount:>15}")    
    def monthly_summary(self):
        print("\n" + "=" * 50)
        print("MONTHLY SUMMARY")
        print("=" * 50)
        query='''
        SELECT YEAR(transaction_date),MONTH(transaction_date),
        SUM(CASE WHEN transaction_type = 'Income' THEN amount ELSE 0 END) AS total_income,
        SUM(CASE WHEN transaction_type = 'Expense' THEN amount ELSE 0 END) AS total_expenses
        FROM transactions
        GROUP BY YEAR(transaction_date),MONTH(transaction_date)
        ORDER BY YEAR(transaction_date),MONTH(transaction_date)'''
        self.cursor.execute(query,)
        result=self.cursor.fetchall()
        if not result:
            print('No monthly summary found.')
            return
        print( f"{'Month':<15}" f"{'Income':>15}" f"{'Expenses':>15}" f"{'Balance':>15}" )
        print("-" * 60)
        for year, month, income, expenses in result:
            balance = income - expenses
            month_name = datetime(year, month, 1).strftime("%B") 
            print(
    f"{month_name + ' ' + str(year):<15}"
    f"{f'₹{income:.2f}':>15}"
    f"{f'₹{expenses:.2f}':>15}"
    f"{f'₹{balance:.2f}':>15}"
)
        
    def highest_expense(self):
        print("\n" + "=" * 50)
        print("HIGHEST EXPENSE")
        print("=" * 50)
        query = """SELECT * 
        FROM transactions 
        WHERE transaction_type = %s
        ORDER BY amount DESC
        LIMIT 1"""
        self.cursor.execute(query, ("Expense",))
        result = self.cursor.fetchone()
        if not result:
            print("No expenses found.")
            return
        print("\nHighest Expense:")
        print(
        f"{'ID':<5} "
        f"{'Date':<12} "
        f"{'Type':<10} "
        f"{'Category':<15} "
        f"{'Amount':<10} "
        f"Description")
        print("-" * 80)
        print(
            f"{result[0]:<5} "
            f"{str(result[1]):<12} "
            f"{result[2]:<10} "
            f"{result[3]:<15} "
            f"₹{result[4]:<10.2f} "
            f"{result[5]}")
        
    def filter_by_date(self):
        print("\n" + "=" * 80)
        print("FILTER TRANSACTIONS BY DATE")
        print("=" * 80)
        try:
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            query = """
            SELECT *
            FROM transactions
            WHERE transaction_date BETWEEN %s AND %s
            ORDER BY transaction_date
            """
            self.cursor.execute(query, (start_date, end_date))
            result = self.cursor.fetchall()
            if not result:
                print("No transactions found for the selected date range.")
                return
            print("\n" + "-" * 80)
            print(
                f"{'ID':<5} "
                f"{'Date':<12} "
                f"{'Type':<10} "
                f"{'Category':<15} "
                f"{'Amount':<10} "
                f"Description"
            )
            print("-" * 80)
            for transaction in result:
                print(
                    f"{transaction[0]:<5} "
                    f"{str(transaction[1]):<12} "
                    f"{transaction[2]:<10} "
                    f"{transaction[3]:<15} "
                    f"₹{transaction[4]:<10.2f} "
                    f"{transaction[5]}"
                )
        except ValueError:
            print("Invalid date format.")
    
    def financial_summary(self):
        print("\n" + "=" * 60)
        print("FINANCIAL SUMMARY")
        print("=" * 60)
        income_query = """
        SELECT COALESCE(SUM(amount), 0)
        FROM transactions
        WHERE transaction_type = %s
        """
        self.cursor.execute(income_query, ("Income",))
        total_income = self.cursor.fetchone()[0]
        expense_query = """
        SELECT COALESCE(SUM(amount), 0)
        FROM transactions
        WHERE transaction_type = %s
        """
        self.cursor.execute(expense_query, ("Expense",))
        total_expenses = self.cursor.fetchone()[0]
        balance = total_income - total_expenses
        highest_query = """
        SELECT category, amount, description
        FROM transactions
        WHERE transaction_type = %s
        ORDER BY amount DESC
        LIMIT 1
        """
        self.cursor.execute(highest_query, ("Expense",))
        highest_expense = self.cursor.fetchone()
        print(f"Total Income       : ₹{total_income:.2f}")
        print(f"Total Expenses     : ₹{total_expenses:.2f}")
        print(f"Current Balance    : ₹{balance:.2f}")
        print("-" * 60)
        if highest_expense:
            print(f"Highest Expense    : ₹{highest_expense[1]:.2f}")
            print(f"Category           : {highest_expense[0]}")
            print(f"Description        : {highest_expense[2]}")
        else:
            print("No expenses found.")
            
def menu(db):
    t=Transaction(db)
    r=Report(db)
    while True:
        print('''
╔════════════════════════════════════════╗
║       EXPENSE TRACKER MENU             ║
╠════════════════════════════════════════╣
║  1. Add Transaction                    ║
║  2. View All Transactions              ║
║  3. Search Transaction                 ║
║  4. Update Transaction                 ║
║  5. Delete Transaction                 ║
║  6. Total Income                       ║
║  7. Total Expenses                     ║
║  8. Current Balance                    ║
║  9. Category-wise Report               ║
║  10. Monthly Summary                   ║
║  11. Highest Expense                   ║
║  12. Filter By Date                    ║
║  13. Financial Summary                 ║
║  14. Exit                              ║
╚════════════════════════════════════════╝
''')
        try:
            choice = int(input('Enter Your Choice (1-14) = '))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            input("Click Enter to continue...")
            continue
        if choice==1:
            t.add_transaction()
        elif choice==2:
            t.view_transactions()
        elif choice==3:
            t.search_transaction()
        elif choice==4:
            t.update_transaction()
        elif choice==5:
            t.delete_transaction()
        elif choice==6:
            r.total_income()
        elif choice==7:
            r.total_expense()
        elif choice==8:
            r.current_balance()
        elif choice==9:
            r.category_wise_expenses()
        elif choice==10:
            r.monthly_summary()
        elif choice==11:
            r.highest_expense()
        elif choice==12:
            r.filter_by_date()
        elif choice==13:
            r.financial_summary()
        elif choice==14:
            print('''
╔════════════════════════════════════════╗
║  Thanks for using Expense Tracker!     ║
║    Stay financially healthy!💰         ║        
╚════════════════════════════════════════╝''')
            break
        else:
            print("❌ Invalid Choice! Please select 1-14")
        
        input("\nClick Enter to continue...")
if __name__=='__main__':
    db=Database()
    try:
        menu(db)
    except KeyboardInterrupt:
        print('\nProgram terminated')
    finally:
        db.close()
