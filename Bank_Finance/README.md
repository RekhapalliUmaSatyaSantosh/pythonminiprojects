# 💰 Banking & Finance

Projects that simulate banking, ATM, and personal finance operations — useful for practicing OOP, database connectivity (MySQL), and file handling (CSV).

## Projects

| File | Description |
|---|---|
| `ATM.py` | An ATM system class connected to a MySQL database (deposits, withdrawals, balance checks, etc.). |
| `ATM_card.py` | A simplified ATM/card simulation using an in-memory dictionary of user accounts (card number, name, PIN, balance). |
| `BankAccount.py` | A `BankAccount` class demonstrating core OOP concepts — account number, holder name, and balance management. |
| `BusTicketBokking.py` | A bus ticket booking system backed by a MySQL database. |
| `Monthly_expnses.py` | Tracks monthly expenses/transactions using a CSV file for storage. |

## Requirements
- `ATM.py` and `BusTicketBokking.py` require a running **MySQL server** and the `mysql-connector-python` package:
```bash
  pip install mysql-connector-python
```
  Update the `host`, `user`, and `password` fields to match your local MySQL setup before running.
- `Monthly_expnses.py` uses only the standard library (`csv`, `os`) — no extra setup needed.
- `ATM_card.py` and `BankAccount.py` run with plain Python, no external dependencies.

## Notes
Since some scripts store real credentials in code (e.g. MySQL password), avoid committing real passwords — use environment variables or a config file for anything beyond local testing.
