from domain.money import Money
from domain.expense import Expense
from domain.account import Account
from strategies.expense_strategy import NormalExpenseStrategy
from services.expense_service import ExpenseService
from repositories.account_repository import AccountRepository

class FakeRepository:
    def __init__(self, account):
        self._account = account

    def get_by_id(self, _):
        return self._account

def test_expense_service_applies_expense():
    repo = AccountRepository()
    account = Account(
        account_id=1,
        owner_name="Test User",
        opening_balance=Money(1000, "USD"),
    )
    repo.add(account)

    service = ExpenseService(repo)

    expense = Expense(
        money=Money(200, "USD"),
        strategy=NormalExpenseStrategy(),
    )

    updated_account = service.apply_expense(1, expense)

    assert updated_account.balance.amount == 800
