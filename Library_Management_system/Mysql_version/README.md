# 📚 Library Management System (MySQL Version)

A console-based **Library Management System** built with **Python** and **MySQL**. This project demonstrates database-driven application development using Object-Oriented Programming (OOP), MySQL Connector, and SQL CRUD operations.

## 🚀 Features

- 📖 Book Management
  - Add Books
  - View Books
  - Update Book Details
  - Delete Books

- 👤 Member Management
  - Add Members
  - View Members
  - Update Member Details
  - Delete Members

- 📚 Book Transactions
  - Issue Books
  - Return Books
  - Track Issue Date and Return Date

- 💾 Persistent data storage using MySQL

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Database:** MySQL
- **Database Connector:** mysql-connector-python
- **Concepts Used**
  - Object-Oriented Programming (OOP)
  - CRUD Operations
  - SQL Queries
  - Transactions
  - Modular Programming

---

## 📂 Project Structure

```
Mysql_version/
│
├── main.py
├── database.py
├── books.py
├── members.py
├── issue_books.py
├── authentication.py
├── create_tables.py
└── README.md
```

> *The file names may differ slightly depending on your implementation.*

---

## ⚙️ Prerequisites

- Python 3.x
- MySQL Server
- MySQL Workbench (Optional)
- mysql-connector-python

Install the required package:

```bash
pip install mysql-connector-python
```

---

## ⚙️ Database Configuration

Update the database credentials in `database.py`.

```python
host = "localhost"
user = "root"
password = "your_password"
database = "library"
```

Create the database before running the project.

```sql
CREATE DATABASE library;
```

The required tables will be created automatically (or run the table creation script if provided).

---

## ▶️ Run the Project

Run the application:

```bash
python main.py
```

---

## 📋 Functionalities

### 📚 Book Management

- Add Book
- Update Book
- Delete Book
- Search Book
- Display All Books

### 👤 Member Management

- Add Member
- Update Member
- Delete Member
- View Members

### 📖 Issue & Return

- Issue Book
- Return Book
- View Issued Books
- Maintain Transaction History

---

## 🗄️ Database Tables

Typical tables used in this project include:

- Books
- Members
- IssueBooks

---

## 🎯 Learning Outcomes

This project helped me gain practical experience in:

- Python with MySQL Integration
- SQL CRUD Operations
- Database Design
- Relational Database Management
- Object-Oriented Programming
- Authentication System
- Exception Handling
- Modular Code Organization

---

## 🔮 Future Enhancements

- Fine Calculation
- Book Reservation
- Admin Dashboard
- Search by Category/Author
- Report Generation

---

## 👨‍💻 Author

**Rekhapalli Uma Satya Santosh**

- GitHub: https://github.com/RekhapalliUmaSatyaSantosh
- LinkedIn: https://www.linkedin.com/in/rekhapalli-uma-satya-santosh/

---

## ⭐ Show Your Support

If you found this project useful, please consider giving this repository a **⭐ Star**.
