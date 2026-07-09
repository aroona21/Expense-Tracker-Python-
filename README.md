# Expense Tracker
### Python | Console Application

A beginner-friendly console-based expense tracker written in **Python**. The program lets you log multiple expenses in a session, validates all input, maintains a running total, and prints a final summary with the total spent, number of expenses, and average expense amount.


## 📌 Features

| Feature | Description |
|---|---|
| ➕ Add Expenses | Enter any positive dollar amount to log it |
| 🔄 Running Total | Displays updated total after every entry |
| ✅ Input Validation | Rejects non-numeric input and zero/negative values |
| 📊 Session Summary | Shows total spent, expense count, and average on exit |
| 🚪 Quit Anytime | Type `quit` to stop and view the final report |


## 🛠️ Concepts Demonstrated

- `while True` loop with `break` for session control
- `try/except ValueError` for robust input validation
- `float()` type conversion and formatted output with f-strings (`:.2f`)
- Conditional logic (`if/continue`) to filter invalid inputs
- Accumulator pattern (`total += expense`, `expense_count += 1`)


## 📁 Project Structure

```
├── Project 2.py    # Full Python source code
```


## ⚙️ How to Run

### Prerequisites
- Python 3.x installed ([download here](https://www.python.org/downloads/))

### Steps

1. Clone this repository
2. Run:
   ```bash
   python Project 2.py
   ```


## 🖥️ Sample Output

```
Welcome to the Expense Tracker!
Type 'quit' to stop and see your total.
------------------------------------------
 Enter expense amount: 500
Added! Running total: $500.00
 Enter expense amount: 1200
Added! Running total: $1700.00
 Enter expense amount: -50
 Please enter a positive amount!
 Enter expense amount: abc
Invalid input! Please enter a number.
 Enter expense amount: quit
------------------------------------------
Total Spent: $1700.00
Number of expenses: 2
Average expense: $850.00
```

## 👩‍💻 Author

**Aroona Noor**
