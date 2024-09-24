import csv
from datetime import datetime

class Expenses:
    all_expenses = []
    monthly_budgets = {}

    def __init__(self, description, amount, date=None, category="General"):
        """
        Initializes an instance of the class with a description, amount, date, and category.

        :param description: A brief description of the expense.
        :type description: str
        :param amount: The amount of the expense.
        :type amount: float
        :param date: The date of the expense (optional). Defaults to the current date.
        :type date: str or datetime
        :param category: Category of the expense (e.g., 'Food', 'Rent', 'Entertainment').
        :type category: str
        :raises ValueError: If `amount` is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("the amount should be greater than 0")

        self.description = description
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now()  # If no date is provided, set to the current date
        if isinstance(self.date, str):
            self.date = datetime.strptime(self.date, '%Y-%m-%d')

        Expenses.all_expenses.append(self)

    def __str__(self):
        """
        Returns a string that describes the expense, amount, date, and category.

        :return: Description, amount, date, and category of the expense.
        :rtype: str
        """
        return (f'Expense: {self.description}, Amount: R${self.amount:.2f}, '
                f'Date: {self.date.strftime("%Y-%m-%d")}, Category: {self.category}')

    @property
    def expenses(self):
        """
        Returns a tuple of the description, amount, date, and category of the expense.

        :return: A tuple with the description, amount, date, and category.
        :rtype: tuple
        """
        return (self.description, self.amount, self.date, self.category)

    @expenses.setter
    def expenses(self, values):
        """
        Updates the description, amount, date, and category of the expense.

        :param values: A tuple containing the new description, amount, date, and category.
        :type values: tuple
        :raises ValueError: If `amount` is less than or equal to zero.
        """
        new_description, new_amount, new_date, new_category = values
        if new_amount <= 0:
            raise ValueError("the amount should be greater than 0")
        self.description = new_description
        self.amount = new_amount
        self.date = datetime.strptime(new_date, '%Y-%m-%d')
        self.category = new_category

    @expenses.deleter
    def expenses(self):
        """
        Deletes the expense by resetting description, amount, date, and removing it from the list.

        :raises AttributeError: If trying to delete an already deleted expense.
        """
        if self.description == "" and self.amount == 0:
            raise AttributeError("Expense has already been deleted")

        if self in Expenses.all_expenses:
            Expenses.all_expenses.remove(self)

        self.description = ""
        self.amount = 0
        self.category = ""
        print("Expense deleted successfully.")

    @classmethod
    def list_all_expenses(cls):
        """
        Lists all created expense instances.
        """
        for exp in cls.all_expenses:
            print(exp)

    @classmethod
    def sum_all_expenses(cls):
        """
        Sums the amount of all created expenses.
        """
        total = sum(exp.amount for exp in cls.all_expenses)
        print(f"Total expenses: R${total:.2f}")
        return total

    @classmethod
    def sum_expenses_by_month(cls, month, year):
        """
        Sums and lists expenses for a specific month and year.

        :param month: The month to filter expenses by (1-12).
        :type month: int
        :param year: The year to filter expenses by.
        :type year: int
        :return: Total sum of expenses for the specified month and year.
        :rtype: float
        """
        monthly_expenses = [exp for exp in cls.all_expenses if exp.date.month == month and exp.date.year == year]
        total = sum(exp.amount for exp in monthly_expenses)

        print(f"Expenses for {year}-{month:02d}:")
        for exp in monthly_expenses:
            print(exp)

        print(f"Total: R${total:.2f}")
        return total

    @classmethod
    def filter_by_category(cls, category):
        """
        Filters and lists expenses by category.

        :param category: The category to filter expenses by.
        :type category: str
        """
        filtered_expenses = [exp for exp in cls.all_expenses if exp.category == category]
        total = sum(exp.amount for exp in filtered_expenses)

        print(f"Expenses in category '{category}':")
        for exp in filtered_expenses:
            print(exp)

        print(f"Total: R${total:.2f}")
        return total

    @classmethod
    def set_monthly_budget(cls, month, year, budget_amount):
        """
        Sets a budget for a specific month and year.

        :param month: The month to set the budget for.
        :type month: int
        :param year: The year to set the budget for.
        :type year: int
        :param budget_amount: The budget amount for that month and year.
        :type budget_amount: float
        """
        cls.monthly_budgets[(year, month)] = budget_amount
        print(f"Budget set for {year}-{month:02d}: R${budget_amount:.2f}")

    @classmethod
    def check_budget(cls, month, year):
        """
        Checks if the total expenses for a specific month exceed the set budget.

        :param month: The month to check the budget for.
        :type month: int
        :param year: The year to check the budget for.
        :type year: int
        :return: Whether the expenses exceeded the budget or not.
        :rtype: bool
        """
        total_expenses = cls.sum_expenses_by_month(month, year)
        budget = cls.monthly_budgets.get((year, month), None)

        if budget is not None:
            if total_expenses > budget:
                print(f"Warning: You have exceeded your budget of R${budget:.2f} by R${total_expenses - budget:.2f}!")
                return True
            else:
                print(f"You are within your budget of R${budget:.2f}.")
                return False
        else:
            print(f"No budget set for {year}-{month:02d}.")
            return False

    @classmethod
    def export_to_csv(cls, filename="expenses.csv"):
        """
        Exports all expenses to a CSV file.

        :param filename: The name of the CSV file to save expenses to.
        :type filename: str
        """
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Amount", "Date", "Category"])

            for exp in cls.all_expenses:
                writer.writerow([exp.description, f"R${exp.amount:.2f}", exp.date.strftime("%Y-%m-%d"), exp.category])

        print(f"Expenses exported to {filename}")
