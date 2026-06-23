import csv
import os

if not os.path.exists('transactions.csv'):
    with open('transactions.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "ID",
            "Date",
            "Type",
            "Category",
            "Amount",
            "Description"
        ])

class Expenses:
    """Expense Tracker Class for managing financial transactions"""
    
    def add_transaction(self):
        """Add a new transaction to the CSV file"""
        print("\n" + "=" * 50)
        print("ADD NEW TRANSACTION")
        print("=" * 50)
        
        transaction_id = input("Enter ID           : ")
        date = input("Enter Date (DD-MM-YYYY): ")
        transaction_type = input("Enter Type (Income/Expense): ")
        category = input("Enter Category      : ")
        amount = input("Enter Amount        : ")
        description = input("Enter Description   : ")

        with open('transactions.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                transaction_id,
                date,
                transaction_type,
                category,
                amount,
                description
            ])

        print("\n✅ Transaction Added Successfully")
        print("=" * 50)
    
    def view_transactions(self):
        """View all transactions in a formatted table"""
        print("\n" + "=" * 80)
        print("ALL TRANSACTIONS")
        print("=" * 80)
        
        with open('transactions.csv', 'r') as f:
            reader = csv.reader(f)
            
            print(f"{'ID':<5} {'Date':<12} {'Type':<8} {'Category':<15} {'Amount':<10} Description")
            print("-" * 80)
            
            for row in reader:
                if row[0].lower() == 'id': 
                    continue
                print(f"{row[0]:<5} {row[1]:<12} {row[2]:<8} {row[3]:<15} ₹{float(row[4]):<9.2f} {row[5]}")
            
            print("=" * 80)

    def search_transaction(self):
        """Search for a transaction by ID"""
        print("\n" + "=" * 50)
        print("SEARCH TRANSACTION")
        print("=" * 50)
        
        transaction_id = input("Enter Transaction ID: ")

        with open('transactions.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  
            found = False

            for row in reader:
                if row[0] == transaction_id:
                    print("\n✅ Transaction Found:")
                    print("-" * 40)
                    print(f"ID          : {row[0]}")
                    print(f"Date        : {row[1]}")
                    print(f"Type        : {row[2]}")
                    print(f"Category    : {row[3]}")
                    print(f"Amount      : ₹{float(row[4]):.2f}")
                    print(f"Description : {row[5]}")
                    print("-" * 40)
                    found = True
                    break
            
            if not found:
                print("\n❌ Transaction Not Found")
            print("=" * 50)
    
    def filter_category(self):
        """Filter and display transactions by category"""
        print("\n" + "=" * 50)
        print("FILTER BY CATEGORY")
        print("=" * 50)
        
        category = input("Enter Category: ")
        found = False

        with open('transactions.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  
            
            print(f"\n📊 Transactions in '{category}':")
            print("-" * 60)
            print(f"{'ID':<5} {'Date':<12} {'Type':<8} {'Amount':<10} Description")
            print("-" * 60)

            for row in reader:
                if row[3].lower() == category.lower():
                    print(f"{row[0]:<5} {row[1]:<12} {row[2]:<8} ₹{float(row[4]):<9.2f} {row[5]}")
                    found = True

            if not found:
                print("❌ No transactions found in this category")
            print("-" * 60)
            print("=" * 50)
    
    def monthly_report(self):
        """Generate and display monthly financial report"""
        print("\n" + "=" * 50)
        print("MONTHLY REPORT")
        print("=" * 50)
        
        month = input("Enter Month (e.g., January, Jan, or 1-12): ").lower()

        months = {
            "january": "1", "jan": "1",
            "february": "2", "feb": "2",
            "march": "3", "mar": "3",
            "april": "4", "apr": "4",
            "may": "5",
            "june": "6", "jun": "6",
            "july": "7", "jul": "7",
            "august": "8", "aug": "8",
            "september": "9", "sep": "9",
            "october": "10", "oct": "10",
            "november": "11", "nov": "11",
            "december": "12", "dec": "12"
        }

        if month.isdigit():
            month_num = str(int(month))
            if not (1 <= int(month_num) <= 12):
                print("❌ Invalid Month! Please enter 1-12")
                return
        else:
            month_num = months.get(month)
            if month_num is None:
                print("❌ Invalid Month")
                return

        month_names = {
            "1": "January", "2": "February", "3": "March", "4": "April",
            "5": "May", "6": "June", "7": "July", "8": "August",
            "9": "September", "10": "October", "11": "November", "12": "December"
        }
        month_name = month_names.get(month_num, month_num)

        total_income = 0
        total_expenses = 0
        transaction_count = 0

        with open('transactions.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  

            for row in reader:
                date = row[1]
                trans_type = row[2]
                amount = float(row[4])

                if date.split('-')[1] == month_num:
                    transaction_count += 1
                    if trans_type.lower() == 'income':
                        total_income += amount
                    elif trans_type.lower() == 'expense':
                        total_expenses += amount

        balance = total_income - total_expenses

        print("\n" + "=" * 50)
        print(f"📊 MONTHLY REPORT - {month_name}")
        print("=" * 50)
        print(f"📌 Total Transactions : {transaction_count}")
        print(f"💰 Total Income       : ₹{total_income:,.2f}")
        print(f"💸 Total Expenses     : ₹{total_expenses:,.2f}")
        print(f"📈 Balance            : ₹{balance:,.2f}")
        
        if transaction_count == 0:
            print("\n📭 No transactions found for this month!")
        elif balance > 0:
            print("\n✅ You have a surplus this month!")
        elif balance < 0:
            print("\n⚠️  You have a deficit this month!")
        else:
            print("\n⚖️  You've broken even this month!")
        print("=" * 50)
    
    def edit_transaction(self):
        """Edit an existing transaction"""
        print("\n" + "=" * 50)
        print("EDIT TRANSACTION")
        print("=" * 50)
        
        transaction_id = input("Enter Transaction ID to Edit: ")
        found = False
        updated_rows = []

        if transaction_id.lower() == 'id':
            print("❌ Cannot edit the header row!")
            return

        with open('transactions.csv', 'r') as f:
            reader = csv.reader(f)
            
            for row in reader:
                if row[0] == transaction_id:
                    found = True
                    print("\n📝 Current Record:")
                    print("-" * 40)
                    print(f"Date        : {row[1]}")
                    print(f"Type        : {row[2]}")
                    print(f"Category    : {row[3]}")
                    print(f"Amount      : ₹{float(row[4]):.2f}")
                    print(f"Description : {row[5]}")
                    print("-" * 40)
                    
                    print("\nEnter new values (press Enter to keep current):")
                    new_date = input(f"New Date [{row[1]}]: ")
                    if not new_date:
                        new_date = row[1]
                    
                    new_type = input(f"New Type [{row[2]}]: ")
                    if not new_type:
                        new_type = row[2]
                    
                    new_category = input(f"New Category [{row[3]}]: ")
                    if not new_category:
                        new_category = row[3]
                    
                    new_amount = input(f"New Amount [{row[4]}]: ")
                    if not new_amount:
                        new_amount = row[4]
                    
                    new_description = input(f"New Description [{row[5]}]: ")
                    if not new_description:
                        new_description = row[5]

                    updated_rows.append([
                        transaction_id,
                        new_date,
                        new_type,
                        new_category,
                        new_amount,
                        new_description
                    ])
                else:
                    updated_rows.append(row)

        with open('transactions.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(updated_rows)

        if found:
            print("\n✅ Transaction Updated Successfully")
        else:
            print("\n❌ Transaction Not Found")
        print("=" * 50)
    
    def delete_transaction(self):
        """Delete a transaction from the file"""
        print("\n" + "=" * 50)
        print("DELETE TRANSACTION")
        print("=" * 50)
        
        transaction_id = input("Enter Transaction ID to Delete: ")
        
        if transaction_id.lower() == 'id':
            print("❌ Cannot delete the header row!")
            return
        
        confirm = input(f"Are you sure you want to delete transaction {transaction_id}? (y/n): ")
        if confirm.lower() != 'y':
            print("❌ Deletion cancelled!")
            return
        
        found = False
        updated_rows = []

        with open('transactions.csv', 'r') as f:
            reader = csv.reader(f)

            for row in reader:
                if row[0] == transaction_id:
                    found = True
                else:
                    updated_rows.append(row)

        with open('transactions.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(updated_rows)

        if found:
            print("✅ Transaction Deleted Successfully")
        else:
            print("❌ Transaction Not Found")
        print("=" * 50)


exp = Expenses()

while True:
    print('''
╔════════════════════════════════════════╗
║       EXPENSE TRACKER MENU             ║
╠════════════════════════════════════════╣
║  1. Add Transaction                    ║
║  2. View All Transactions              ║
║  3. Search Transaction                 ║
║  4. Filter by Category                 ║
║  5. Monthly Report                     ║
║  6. Edit Transaction                   ║
║  7. Delete Transaction                 ║
║  8. Exit                               ║
╚════════════════════════════════════════╝
''')

    try:
        choice = int(input('Enter Your Choice (1-8) = '))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        input("Click Enter to continue...")
        continue

    if choice == 1:
        exp.add_transaction()
    elif choice == 2:
        exp.view_transactions()
    elif choice == 3:
        exp.search_transaction()
    elif choice == 4:
        exp.filter_category()
    elif choice == 5:
        exp.monthly_report()
    elif choice == 6:
        exp.edit_transaction()
    elif choice == 7:
        exp.delete_transaction()
    elif choice == 8:
        print('''
╔════════════════════════════════════════╗
║  Thanks for using Expense Tracker!     ║
║   Stay financially healthy!💰         ║
╚════════════════════════════════════════╝
''')
        break
    else:
        print("❌ Invalid Choice! Please select 1-8")

    input("\nClick Enter to continue...")
