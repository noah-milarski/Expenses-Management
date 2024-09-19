class Expenses:
    
    def __init__(self, description, amount):
        #TODO Thomas, tenta adicionar um verificador se 'self.amount' é maior que zero, faz um: raise ValueError
        """
        Initializes an instance of the class with a description and an amount.

        Args:
            description (str): A brief description of the expense.
            amount (float): The amount of the expense.

        Raises:
            ValueError: If `amount` is less than zero.
        """
        if amount <= 0:
            raise ValueError("the amount should be greater than 0")
        

        self.description = description #str: Description of the expense
        self.amount = amount # float: Amount of the expense
        

    def __str__(self):
        #TODO Thomas veja como você quer que seja printado quando instanciamos uma despesa
        """
        Return a what was the expense and it's amount
        """
        return f'Expense: {self.description}, Amount: R${self.amount:.2f}'
    
    def update_expense(self, newdescription, newamount):
        #TODO Thomas faça a lógica para substituir por um novo valor de quantidade e a descrição
        """
        Updates the amount of the expense
        """
        if newamount <= 0:
            raise ValueError("the amount should be greater than 0")
        self.amount = newamount
        self.description = newdescription