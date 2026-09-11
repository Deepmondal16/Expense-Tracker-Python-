# Expense Tracker (Python)

A simple command-line expense tracker built in Python. It lets users set a budget, log expenses by category, and get real-time feedback on their spending versus their budget.

## Features

- **Set Budget** – Define an initial budget amount.
- **Add to Budget** – Top up your existing budget at any time.
- **View Budget** – Check your current total budget.
- **Add Expense** – Log an expense with a category (e.g., Food, Travel) and amount.
- **View Expenses** – List all recorded expenses.
- **Show Summary** – See total budget, total spent, and remaining balance.
- **Overspend Alerts** – Automatic warning when total expenses exceed the set budget.

## How It Works

The app runs in a loop, presenting a simple text menu:

```
1. Set budget
2. View budget
3. Add More Budget
4. Add expense
5. View expenses
6. Show summary
7. Exit
```

Users select an option by entering its number, and the program calls the corresponding function to handle that action.

## Tech Stack

- **Language:** Python 3
- **Concepts used:** Functions, global variables, lists of dictionaries, loops, conditionals, user input handling


## Example Usage

```
Enter your budget amount: 5000
Budget set to 5000.0

Enter category (Food, Travel, etc.): Food
Enter amount: 500
Expense added In Your Tracker
You have 4500.0 remaining, left in your budget.
```

## Author

**Deep Mondal**
.
