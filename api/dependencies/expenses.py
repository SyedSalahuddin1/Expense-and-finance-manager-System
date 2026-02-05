from services.expense_service import ExpenseService
from api.dependencies.accounts import get_account_repository


def get_expense_service():
    return ExpenseService(get_account_repository())
