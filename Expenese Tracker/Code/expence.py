#Expense Tracker :- 

expenses = []   
budget = 0     


def set_budget():
    global budget
    budget = float(input("Enter your budget amount: "))
    print(f"Budget set to {budget}")


def add_to_budget():
    global budget
    extra_money = float(input("Enter amount to add to your budget: "))
    budget = budget + extra_money
    print(f"Added : {extra_money}, to your budget. Your New budget : {budget}")




def view_budget():
    print(f"your Total Budget:- {budget}")

def add_expense():
    category = input("Enter category (Food, Travel, etc.): ")
    amount = float(input("Enter amount: "))
    expenses.append({"category": category, "amount": amount})
    print("Expense added In Your Tracker")

    total = get_total()
    if budget > 0:
        if total > budget:
            print("WARNING: You have gone OVER your budget!")
            print(f"Budget : {budget}, Spent : {total}")
        else:
            remaining = budget - total
            print(f"You have{remaining} remaining, left in your budget.")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    for expense in expenses:
        print(expense["category"], "-", expense["amount"])
    print()


def get_total():
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    return total


def show_summary():
    total = get_total()
    print("Budget:", budget)
    print("Total spent:", total)
    if budget > 0:
        print("Remaining:", budget - total)
    print()


while True:
    print("1. Set budget")
    print("2. View budget")
    print("3. Add More Budget")
    print("4. Add expense")
    print("5. View expenses")
    print("6. Show summary")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        set_budget()
    elif choice == "2":
        view_budget()
    elif choice == "3":
        add_to_budget()
    elif choice == "4":
        add_expense()
    elif choice == "5":
        view_expenses()
    elif choice == "6":
        show_summary()
    elif choice == "7":
        print("Bye!")
        print("Thank You")
        break
    else:
        print("Invalid choice, try 1 to 7")