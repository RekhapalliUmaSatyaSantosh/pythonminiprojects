# 💰 Expense Tracker

A **console-based Expense Tracker application** built using **Python and MySQL** to help users manage income and expenses efficiently. The application provides complete transaction management along with useful financial reports and summaries.

---

## 🚀 Features

### 📌 Transaction Management

* ➕ Add new income or expense transactions
* 📋 View all transactions
* 🔍 Search transactions by Transaction ID
* ✏️ Update transaction details
* 🗑️ Delete transactions with confirmation

### 📊 Financial Reports

* 💵 Calculate total income
* 💸 Calculate total expenses
* 🏦 View current balance
* 📂 View category-wise expenses
* 📅 Generate monthly income and expense summaries
* 🔥 Find the highest expense
* 🗓️ Filter transactions by date range
* 📈 View complete financial summary

---

## 🛠️ Technologies Used

* **Python**
* **MySQL**
* **mysql-connector-python**
* **Object-Oriented Programming (OOP)**
* **SQL Queries**
* **CRUD Operations**

---

## 🏗️ Project Structure

```text
Expense-Tracker/
│
├── expense_tracker.py
└── README.md
```

---

## 🗄️ Database Structure

The application uses a MySQL database named:

```text
expense_tracker
```

### Transactions Table

| Column           | Description           |
| ---------------- | --------------------- |
| transaction_id   | Unique transaction ID |
| transaction_date | Date of transaction   |
| transaction_type | Income or Expense     |
| category         | Transaction category  |
| amount           | Transaction amount    |
| description      | Additional details    |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/expense-tracker.git
```

### 2. Navigate to the Project Directory

```bash
cd expense-tracker
```

### 3. Install Required Package

```bash
pip install mysql-connector-python
```

### 4. Create the MySQL Database

```sql
CREATE DATABASE expense_tracker;
```

Create the required `transactions` table according to your project database schema.

### 5. Configure Database Connection

Update the database connection details in the Python file:

```python
mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="expense_tracker"
)
```

> ⚠️ Never upload your real database password to GitHub. Use environment variables for better security.

---

## ▶️ How to Run

Run the following command:

```bash
python expense_tracker.py
```

You will see a menu similar to:

```text
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
```

---

## 📊 Sample Reports

The application can generate reports such as:

```text
Total Income       : ₹50,000.00
Total Expenses     : ₹18,500.00
Current Balance    : ₹31,500.00

Highest Expense    : ₹8,000.00
Category           : Education
Description        : Course Fee
```

---

## 🎯 What I Learned

Through this project, I practiced:

* Python Object-Oriented Programming
* Connecting Python with MySQL
* CRUD operations
* SQL aggregate functions such as `SUM()`
* `GROUP BY` and `ORDER BY`
* Date-based filtering
* Exception handling
* Database transactions using `commit()`
* Building a menu-driven application
* Structuring a real-world Python project

---

## 🔮 Future Enhancements

* 🔐 User login and authentication
* 📊 Graphical charts and visual reports
* 🌐 Convert the application into a Django web application
* 📱 Add a responsive frontend
* 📤 Export reports to CSV or Excel
* 🔔 Budget limit notifications
* 📈 Expense trend analysis
* 🔒 Store database credentials securely using environment variables

---

## 👨‍💻 Author

**Santosh Rekhapalli**

Python Full Stack Developer | Python | Django | SQL | HTML | CSS | JavaScript

---

⭐ If you found this project useful, consider giving the repository a star!
