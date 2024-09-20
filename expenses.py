class Expenses:
    all_expenses = []

    def __init__(self, description, amount):
        """
        Initializes an instance of the class with a description and an amount.

        :param description: A brief description of the expense.
        :type description: str
        :param amount: The amount of the expense.
        :type amount: float
        :raises ValueError: If `amount` is less than or equal to zero.
        """
        
        if amount <= 0:
            raise ValueError("the amount should be greater than 0")

        self.description = description
        self.amount = amount
        Expenses.all_expenses.append(self)

    def __str__(self):
        """
        Returns a string that describes the expense and its amount.

        :return: Description and amount of the expense.
        :rtype: str
        """

        return f'Expense: {self.description}, Amount: R${self.amount:.2f}'

    @property
    def expenses(self):
        """
        Returns a tuple of the description and amount of the expense.

        :return: A tuple with the description and amount.
        :rtype: tuple
        """
        return (self.description, self.amount)

    @expenses.setter
    def expenses(self, values):
        """
        Updates the description and amount of the expense.

        :param values: A tuple containing the new description and new amount.
        :type values: tuple
        :raises ValueError: If `amount` is less than or equal to zero.
        """
        new_description, new_amount = values
        if new_amount <= 0:
            raise ValueError("the amount should be greater than 0")
        self.description = new_description
        self.amount = new_amount

    @expenses.deleter
    def expenses(self):
        """
        Deletes the expense by resetting description and amount and removing from the list.

        :raises AttributeError: If trying to delete an already deleted expense.
        """
        if self.description == "" and self.amount == 0:
            raise AttributeError("Expense has already been deleted")

        if self in Expenses.all_expenses:
            Expenses.all_expenses.remove(self)

        self.description = ""
        self.amount = 0
        print("Expense deleted successfully.")

    @classmethod
    def list_all_expenses(cls):
        """
        Lists all created expense instances.
        """
        for exp in cls.all_expenses:
            print(exp)