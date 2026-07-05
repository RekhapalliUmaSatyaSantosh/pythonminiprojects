# 🗄️ Database Management

Projects that demonstrate CRUD operations and relational data modeling using `sqlite3`.

## Projects

| File | Description |
|---|---|
| `Students_Management.py` | A menu-driven Student Management System backed by SQLite (`students.db`). Manages two related tables — `Departments` and `Students` — with a foreign key relationship. |

### Features
- Create departments and students
- View all departments/students (with department joined in via `INNER JOIN`)
- Search a student by ID
- Update student details (name, phone, email, or department)
- Delete a student (with confirmation prompt)
- Input validation and error handling for duplicate IDs, invalid foreign keys, etc.

## How to Run
```bash
python Student_Management_System.py
```
This will automatically create `students.db` in the same folder on first run (via `create_tables()`), so no manual database setup is required.

## Requirements
Uses only the Python standard library (`sqlite3`) — no installation needed.

## Notes
- `students.db` is generated at runtime. Avoid committing a database file containing real personal data — consider adding `*.db` to `.gitignore`.
- This folder is a good place for any future scripts that read/write `students.db` (e.g. CSV export, backups, migrations, reporting tools).
