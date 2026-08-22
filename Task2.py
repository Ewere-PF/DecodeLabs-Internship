print("Welcome to the Expense Tracker!")

total = 0

while True:
    expense = input("Enter an expense amount (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    expense = float(expense)
    total = total + expense

    print(f"Expense added: ₦{expense:.2f}")
    print(f"Total spent: ₦{total:.2f}")
    print()

print(f"\nYour total spending is: ₦{total:.2f}")
print("Thank you for using the Expense Tracker!")
