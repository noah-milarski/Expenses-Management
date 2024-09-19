# Expenses Tracker

## Overview

The `Expenses` class provides a straightforward way to manage and track personal expenses. It supports creating, updating, and deleting expenses, as well as listing all recorded expenses. Each expense entry includes a description and an amount, with built-in validation to ensure amounts are positive.

## Features

- **Create an Expense**: Instantiate a new expense with a description and amount.
- **Update an Expense**: Change the description or amount of an existing expense.
- **Delete an Expense**: Remove an expense from the list and reset its attributes.
- **List All Expenses**: Display all expenses currently tracked.

## Installation

To use the `Expenses` class, simply include the class definition in your Python project. No additional libraries or packages are required.

## Usage

Here’s how you can use the `Expenses` class:

```python
from expenses import Expenses

def main():
    # Create some expense records
    expense1 = Expenses('Groceries', 45.6)
    expense2 = Expenses('Gym', 20)
    expense3 = Expenses('College', 12000)

    # Display all expenses
    Expenses.list_all_expenses()

    # Update an expense
    expense1.expenses = ('Golf Club', 550.25)
    print("\nUpdated expense:")
    print(expense1)

    # Delete an expense
    del expense2
    print("\nAfter deletion:")
    Expenses.list_all_expenses()

if __name__ == '__main__':
    main()
```
# Class Reference

## Expenses

### Attributes
- **description** (str): Description of the expense.
- **amount** (float): Amount of the expense.

### Methods
- **`__init__(description, amount)`**: Initializes a new expense with a description and amount.
- **`__str__()`**: Returns a string representation of the expense.
- **`expenses`**: A property to get and set the description and amount of the expense.
- **`list_all_expenses()`**: Class method to display all created expense instances.

### Authors
- **Pedro Noah**
- **Thomas Pickler**
