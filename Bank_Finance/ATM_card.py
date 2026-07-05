d = {
    'user1': [48062392934, 'Kishore', 1503, 1300.00],
    'user2': [23927055023, 'Ramesh', 3426, 2300.45],
    'user3': [37952608907, 'Uday', 7832, 123.45],
    'user4': [19152991766, 'Arjun', 6654, 257.98],
    'user5': [92391634683, 'Satya', 8723, 899.90]
}

class ATM:
    '''🏦 Welcome to RBI Bank - Your Trusted Banking Partner 🏦'''
    
    # MIN_PIN_LENGTH = 4
    # MAX_PIN_LENGTH = 4
    DECORATION = '═' * 50
    
    def __init__(self, user):
        self.user = user
        self.current_user = None
        self.transaction_count = 0  
    
    def _print_header(self, title):
        """Helper method for consistent header printing"""
        print('\n' + '─' * 50)
        print(f'  {title}')
        print('─' * 50)
    
    def _print_success(self, message):
        """Helper method for success messages"""
        print(f'✅ {message}')
    
    def _print_error(self, message):
        """Helper method for error messages"""
        print(f'❌ {message}')
    
    def _print_info(self, message):
        """Helper method for info messages"""
        print(f'ℹ️  {message}')
    
    def login(self):
        """User login authentication"""
        self._print_header('🔐 USER LOGIN')
        try:
            self.acc_no = int(input("  Enter Your Account Number: "))
            self.pin = int(input("  Enter Your Account PIN: "))
            
            for user, details in self.user.items():
                if details[0] == self.acc_no and details[2] == self.pin:
                    self.current_user = user
                    print('\n' + '═' * 50)
                    print(f'  🌟 Welcome {details[1]}! 🌟')
                    print(f'  Login Successful!')
                    print('═' * 50 + '\n')
                    return
            self._print_error('Invalid Account Number or PIN! Please try again.')
        except:
            self._print_error('Invalid input! Please enter numeric values.')
    
    def check_balance(self):
        """Check current account balance"""
        balance = self.user[self.current_user][3]
        self._print_header('💰 CHECK BALANCE')
        print(f'  Account Holder: {self.user[self.current_user][1]}')
        print(f'  Current Balance: ₹{balance:,.2f}')
        print('─' * 50)
        self.transaction_count += 1
    
    def deposit(self):
        """Deposit money into account"""
        self._print_header('💰 DEPOSIT MONEY')
        try:
            amount = int(input('  Enter amount to deposit: ₹'))
            
            if amount <= 0:
                self._print_error('Cannot deposit amount less than or equal to zero!')
                return
            
            balance = self.user[self.current_user][3]
            balance += amount
            self.user[self.current_user][3] = balance
            self._print_success(f'Amount ₹{amount:,.2f} deposited successfully!')
            print(f'  Current Balance: ₹{balance:,.2f}')
            print('─' * 50)
            self.transaction_count += 1
        except:
            self._print_error('Invalid input! Please enter a valid number.')
    
    def withdraw(self):
        """Withdraw money from account"""
        self._print_header('💳 WITHDRAW MONEY')
        try:
            amount = int(input('  Enter amount to Withdraw: ₹'))
            balance = self.user[self.current_user][3]
            
            if amount <= 0:
                self._print_error('Cannot withdraw amount less than or equal to zero!')
                return
            elif amount > balance:
                self._print_error(f'Insufficient Funds! Available balance: ₹{balance:,.2f}')
                return
            else:
                balance -= amount
                self.user[self.current_user][3] = balance
                self._print_success(f'Amount ₹{amount:,.2f} withdrawn successfully!')
                print(f'  Current Balance: ₹{balance:,.2f}')
                print('─' * 50)
                self.transaction_count += 1
        except:
            self._print_error('Invalid input! Please enter a valid number.')
    
    def change_pin(self):
        """Change account PIN with validation"""
        self._print_header('🔑 CHANGE PIN')
        try:
            old_pin = int(input('  Enter old PIN: '))
            
            if old_pin != self.user[self.current_user][2]:
                self._print_error('Invalid PIN! Please try again.')
                return
            
            new_pin = int(input('  Enter your new PIN: '))
            
            if len(str(new_pin)) != self.MIN_PIN_LENGTH:
                self._print_error(f'PIN must be exactly {self.MIN_PIN_LENGTH} digits!')
                return
            
            for user, details in self.user.items():
                if user != self.current_user and details[2] == new_pin:
                    self._print_error('This PIN is already taken! Please choose another.')
                    return
            
            self.user[self.current_user][2] = new_pin
            self._print_success('PIN updated successfully!')
            print('─' * 50)
            self.transaction_count += 1
        except:
            self._print_error('Invalid input! Please enter numeric values.')
    
    def transfer_money(self):
        """Transfer money to another user"""
        self._print_header('💸 TRANSFER MONEY')
        try:
            receiver_acc = int(input('  Enter Account number to send: '))
            
            receiver_user = None
            for users, details in self.user.items():
                if details[0] == receiver_acc:
                    receiver_user = users
                    break
            
            if receiver_user is None:
                self._print_error('User not Found! Please check the account number.')
                return
            
            if receiver_user == self.current_user:
                self._print_error('Cannot transfer money to your own account!')
                return
            
            amount = int(input('  Enter amount to transfer: ₹'))
            sender_balance = self.user[self.current_user][3]
            
            if amount <= 0:
                self._print_error('Cannot transfer amount less than or equal to zero!')
                return
            elif amount > sender_balance:
                self._print_error(f'Insufficient Funds! Available: ₹{sender_balance:,.2f}')
                return
            
            self.user[self.current_user][3] -= amount
            self.user[receiver_user][3] += amount
            
            print('\n' + '═' * 50)
            self._print_success(f'₹{amount:,.2f} transferred successfully to {self.user[receiver_user][1]}!')
            print(f'  Your Current Balance: ₹{self.user[self.current_user][3]:,.2f}')
            print('═' * 50)
            self.transaction_count += 1
        except:
            self._print_error('Invalid input! Please enter numeric values.')
    
    def account_details(self):
        """Display account details"""
        self._print_header('👤 ACCOUNT DETAILS')
        try:
            pin = int(input('  Enter your PIN for verification: '))
            
            if pin != self.user[self.current_user][2]:
                self._print_error('Incorrect PIN!')
                return
            
            print('\n  ┌─' + '─' * 40 + '─┐')
            print(f'  │  📋 ACCOUNT INFORMATION{' ' * 18}│')
            print('  ├─' + '─' * 40 + '─┤')
            print(f'  │  Account Number: {self.user[self.current_user][0]}')
            print(f'  │  Account Holder: {self.user[self.current_user][1]}')
            print(f'  │  Current Balance: ₹{self.user[self.current_user][3]:,.2f}')
            print(f'  │  Transactions: {self.transaction_count}')
            print('  └─' + '─' * 40 + '─┘')
            self.transaction_count += 1
        except:
            self._print_error('Invalid input! Please enter numeric values.')

def main():
    user = ATM(d)
    
    print('\n' + '═' * 80)
    print('  ' + '═' * 60)
    print(f'  {ATM.__doc__}')
    print('  ' + '═' * 60)
    print('═' * 80)
    
    user.login()
    
    if user.current_user is None:
        print('\n' + '⚠️  Too many failed attempts or invalid credentials.')
        print('   Please restart the application.\n')
        return
    
    print('  🏧 Welcome to ATM Services')
    print('═' * 50 + '\n')
    
    while True:
        print('\n' + '┌─' + '─' * 40 + '─┐')
        print('│  📌 ATM SERVICES MENU            │')
        print('├─' + '─' * 40 + '─┤')
        print('│  1. 💰 Check Balance             │')
        print('│  2. 💵 Deposit Money             │')
        print('│  3. 💳 Withdraw Money            │')
        print('│  4. 🔑 Change PIN                │')
        print('│  5. 💸 Transfer Money            │')
        print('│  6. 👤 Account Details           │')
        print('│  7. 🚪 Logout                    │')
        print('└─' + '─' * 40 + '─┘')
        
        try:
            choose = int(input('  Enter your choice (1-7): '))
            print()
            
            if choose == 1:
                user.check_balance()
            elif choose == 2:
                user.deposit()
            elif choose == 3:
                user.withdraw()
            elif choose == 4:
                user.change_pin()
            elif choose == 5:
                user.transfer_money()
            elif choose == 6:
                user.account_details()
            elif choose == 7:
                print('\n' + '═' * 50)
                print('  🌟 Thank you for choosing RBI Bank! 🌟')
                print('  Have a great day! 👋')
                print('═' * 50 + '\n')
                break
            else:
                user._print_error('Invalid Option! Please choose between 1-7.')
        
        except:
            user._print_error('Please enter a valid number (1-7)!')

        if choose != 7:
            input('\n  Press Enter to continue...')

if __name__ == "__main__":
    main()
