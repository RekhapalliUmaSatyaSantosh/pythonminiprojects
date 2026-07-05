import sqlite3

DB_NAME = "students.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")


def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Departments(
        deptid INTEGER PRIMARY KEY,
        deptname TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students(
        stdid INTEGER PRIMARY KEY,
        stdname TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        deptid INTEGER NOT NULL,
        FOREIGN KEY(deptid) REFERENCES Departments(deptid)
    )
    """)

    conn.commit()


def add_department():
    try:
        deptid = int(input("Enter Department ID: "))
        deptname = input("Enter Department Name: ")

        cursor.execute(
            "INSERT INTO Departments VALUES(?, ?)",
            (deptid, deptname)
        )
        conn.commit()
        print("Department added successfully.")

    except ValueError:
        print("Department ID must be a number.")
    except sqlite3.IntegrityError:
        print("Department ID or name already exists.")


def view_departments():
    cursor.execute("SELECT * FROM Departments")
    rows = cursor.fetchall()

    if not rows:
        print("No departments found.")
        return

    print("\n--- Departments ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]}")


def add_student():
    try:
        stdid = int(input("Enter Student ID: "))
        stdname = input("Enter Student Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        print("\nAvailable Departments:")
        view_departments()

        deptid = int(input("Enter Department ID: "))

        cursor.execute(
            "INSERT INTO Students VALUES(?, ?, ?, ?, ?)",
            (stdid, stdname, phone, email, deptid)
        )
        conn.commit()
        print("Student added successfully.")

    except ValueError:
        print("Student ID and Department ID must be numbers.")
    except sqlite3.IntegrityError as e:
        if "FOREIGN KEY" in str(e):
            print("Invalid Department ID.")
        else:
            print("Student ID or email already exists.")


def view_students():
    cursor.execute("""
    SELECT Students.stdid, Students.stdname, Students.phone,
           Students.email, Departments.deptname
    FROM Students
    INNER JOIN Departments
    ON Students.deptid = Departments.deptid
    """)

    rows = cursor.fetchall()

    if not rows:
        print("No students found.")
        return

    print("\n--- Students ---")
    for row in rows:
        print(f"""
ID         : {row[0]}
Name       : {row[1]}
Phone      : {row[2]}
Email      : {row[3]}
Department : {row[4]}
----------------------------
""")


def search_student():
    try:
        stdid = int(input("Enter Student ID: "))

        cursor.execute("""
        SELECT Students.stdid, Students.stdname, Students.phone,
               Students.email, Departments.deptname
        FROM Students
        INNER JOIN Departments
        ON Students.deptid = Departments.deptid
        WHERE Students.stdid = ?
        """, (stdid,))

        row = cursor.fetchone()

        if row:
            print(f"""
--- Student Found ---
ID         : {row[0]}
Name       : {row[1]}
Phone      : {row[2]}
Email      : {row[3]}
Department : {row[4]}
""")
        else:
            print("Student not found.")

    except ValueError:
        print("Student ID must be a number.")


def update_student():
    try:
        stdid = int(input("Enter Student ID: "))

        cursor.execute("SELECT * FROM Students WHERE stdid=?", (stdid,))
        row = cursor.fetchone()

        if not row:
            print("Student not found.")
            return

        print("""
1. Update Name
2. Update Phone
3. Update Email
4. Update Department
""")

        choice = int(input("Enter option: "))

        if choice == 1:
            new_value = input("Enter new name: ")
            cursor.execute(
                "UPDATE Students SET stdname=? WHERE stdid=?",
                (new_value, stdid)
            )

        elif choice == 2:
            new_value = input("Enter new phone: ")
            cursor.execute(
                "UPDATE Students SET phone=? WHERE stdid=?",
                (new_value, stdid)
            )

        elif choice == 3:
            new_value = input("Enter new email: ")
            cursor.execute(
                "UPDATE Students SET email=? WHERE stdid=?",
                (new_value, stdid)
            )

        elif choice == 4:
            view_departments()
            new_value = int(input("Enter new department ID: "))
            cursor.execute(
                "UPDATE Students SET deptid=? WHERE stdid=?",
                (new_value, stdid)
            )

        else:
            print("Invalid option.")
            return

        conn.commit()
        print("Student updated successfully.")

    except ValueError:
        print("Please enter valid numbers.")
    except sqlite3.IntegrityError:
        print("Invalid update. Email may already exist or department does not exist.")


def delete_student():
    try:
        stdid = int(input("Enter Student ID: "))

        cursor.execute("SELECT * FROM Students WHERE stdid=?", (stdid,))
        row = cursor.fetchone()

        if not row:
            print("Student not found.")
            return

        confirm = input("Are you sure you want to delete this student? (y/n): ")

        if confirm.lower() == "y":
            cursor.execute("DELETE FROM Students WHERE stdid=?", (stdid,))
            conn.commit()
            print("Student deleted successfully.")
        else:
            print("Delete cancelled.")

    except ValueError:
        print("Student ID must be a number.")


def display_menu():
    print("""
========== STUDENT MANAGEMENT SYSTEM ==========

1. Add Department
2. View Departments
3. Add Student
4. View Students
5. Search Student
6. Update Student
7. Delete Student
8. Exit

===============================================
""")


def main():
    create_tables()

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_department()
            elif choice == 2:
                view_departments()
            elif choice == 3:
                add_student()
            elif choice == 4:
                view_students()
            elif choice == 5:
                search_student()
            elif choice == 6:
                update_student()
            elif choice == 7:
                delete_student()
            elif choice == 8:
                print("Thank you. Goodbye!")
                break
            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a number only.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    finally:
        conn.close()
