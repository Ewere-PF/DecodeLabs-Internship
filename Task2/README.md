# Expense Tracker

A simple Python-based Expense Tracker that allows users to enter multiple expenses, calculates the total amount spent, and displays the result. This project was created as part of a Python programming learning project to practice basic programming concepts.

## Features

* Allows users to enter multiple expense amounts.
* Automatically calculates the total expenses.
* Displays the running total after each expense.
* Allows the user to type `done` to stop entering expenses.
* Uses Nigerian Naira (₦) for displaying amounts.

## Technologies Used

* **Python 3**
* `input()` for collecting user data
* Variables and arithmetic operations
* `while` loops
* Conditional statements
* Type conversion using `float()`

## How It Works

The program starts with a total of zero:

```python
total = 0
```

Each time the user enters an expense, the amount is added to the total:

```python
total = total + expense
```

The program continues accepting expenses until the user enters `done`.

### Example

```text
Welcome to the Expense Tracker!

Enter an expense amount (or type 'done' to finish): 100
Expense added: ₦100.00
Total spent: ₦100.00

Enter an expense amount (or type 'done' to finish): 50
Expense added: ₦50.00
Total spent: ₦150.00

Enter an expense amount (or type 'done' to finish): 20
Expense added: ₦20.00
Total spent: ₦170.00

Enter an expense amount (or type 'done' to finish): done

Your total spending is: ₦170.00
Thank you for using the Expense Tracker!
```
This project helped me practice:

* Variables
* User input
* Data types
* Type conversion
* Arithmetic operations
* `while` loops
* `if` statements
* Accumulators
* Basic program flow and logic

# Future Improvements

Some features that could be added in future versions include:

* Categorizing expenses such as food, transportation, and bills.
* Saving expenses to a file or database.
* Displaying a detailed list of all expenses.
* Adding dates to each expense.
* Creating a graphical user interface.
* Generating spending summaries and reports.