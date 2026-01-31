class ExpenseService:
    def __init__(self, account_repository):
        self._account_repository = account_repository
        
    def apply_expense(self, account_id, expense):
        account = self._account_repository.get_by_id(account_id)
        expense.apply_to(account)
        