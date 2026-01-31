class ExpenseService:
    """
    Application service representing the 'Apply Expense' use case.
    Coordinates domain objects without containing domain logic.
    """

    def __init__(self, account_repository):
        self._account_repository = account_repository

    def apply_expense(self, account_id: int, expense) -> None:
        account = self._account_repository.get_by_id(account_id)
        expense.apply_to(account)
