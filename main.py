from expenses import Expenses

def main():
    expense1 = Expenses('Groceries', 45.6)
    expense2 = Expenses('Gym', 20)
    expense3 = Expenses('College', 12000)

    Expenses.list_all_expenses()

    expense1.expenses = ('Golf Club', 550.25)
    print("\nUpdated expense:")
    print(expense1)

    del expense2  # Remove from list and resets attributes
    print("\nAfter deletion:")
    Expenses.list_all_expenses()

if __name__ == '__main__':
    main()