# ATM Management System

A console-based ATM and banking management system built with Python and MySQL. Supports account creation, secure PIN-based login, deposits, withdrawals, fund transfers between accounts, transaction history, and account management — all backed by a relational database with proper foreign-key constraints.

## Features

- **Account Creation** — Create accounts with 8-digit account number, 4-digit PIN, phone number, and initial balance validation
- **Authentication** — PIN-based login system before accessing any banking operation
- **Balance Inquiry** — Check current account balance
- **Deposit & Withdrawal** — With balance validation to prevent overdrafts
- **Money Transfer** — Transfer funds between accounts with automatic balance updates on both ends
- **Mini Statement** — View the last 5 transactions (type, amount, date)
- **Change PIN** — Update account PIN after verifying the existing one
- **Update Phone Number** — Update registered contact number
- **Delete Account** — Remove account and associated transaction history (with confirmation prompt)
- **Transaction Logging** — Every deposit, withdrawal, and transfer is recorded with a timestamp

## Tech Stack

- **Language:** Python 3
- **Database:** MySQL
- **Library:** `mysql-connector-python`

## Database Schema

**`accounts` table**
| Column | Type | Description |
|---|---|---|
| acc_num | BIGINT (PK) | 8-digit account number |
| holder_name | VARCHAR(50) | Account holder's name |
| phone | BIGINT | 10-digit phone number |
| pin | INT | 4-digit PIN |
| balance | DECIMAL(10,2) | Current balance |

**`transactions` table**
| Column | Type | Description |
|---|---|---|
| transaction_id | INT (PK, auto-increment) | Unique transaction ID |
| acc_num | BIGINT (FK → accounts) | Associated account |
| transaction_type | VARCHAR(20) | Deposit / Withdraw / Transfer Sent / Transfer Received |
| amount | DECIMAL(10,2) | Transaction amount |
| transaction_date | DATETIME | Auto-generated timestamp |

## Setup

1. Install the required package:
```bash
   pip install mysql-connector-python
```

2. Make sure MySQL Server is installed and running locally.

3. Update the database credentials in the `Database` class before running:
```python
   self.conn = mysql.connector.connect(
       host="localhost",
       user="your_mysql_username",
       password="your_mysql_password",
       database="your_database_name"
   )
```
   > **Note:** For a public repo, avoid hardcoding real credentials — consider using environment variables (e.g. `os.environ.get("DB_PASSWORD")`) instead.

4. The script automatically creates the required tables (`accounts`, `transactions`) on first run if they don't already exist.

## Run

```bash
python atm_management_system.py
```

You'll see a menu-driven interface:
========== ATM SERVICES ==========

1. Create Account
2. Login
3. Check Balance
4. Deposit
5. Withdraw
6. Transfer Money
7. Mini Statement
8. Change PIN
9. Update Phone
10. Delete Account
11. Exit

## Sample Flow

1. Choose `1` to create a new account (8-digit account number, 4-digit PIN)
2. Choose `2` to log in with your account number and PIN
3. Access banking operations (deposit, withdraw, transfer, statement, etc.)
4. Choose `11` to exit

## Notes

- Account numbers must be exactly 8 digits, PINs exactly 4 digits, and phone numbers exactly 10 digits — enforced during account creation.
- Transfers and deletions use rollback on database errors to keep data consistent.
