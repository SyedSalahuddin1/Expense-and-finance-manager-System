class FakeAccount:
    def __init__(self):
        self.withdraw_called = False

    def withdraw(self, money):
        self.withdraw_called = True


class FakeRepository:
    def __init__(self, account):
        self._account = account

    def get_by_id(self, _):
        return self._account


def test_expense_service_applies_expense():
    from services.expense_service import ExpenseService
    from domain.expense import Expense
    from domain.money import Money
    from strategies.expense_strategy import NormalExpense

    fake_account = FakeAccount()
    fake_repo = FakeRepository(fake_account)

    service = ExpenseService(fake_repo)
    expense = Expense(Money(100, "USD"), NormalExpense())

    service.apply_expense(1, expense)

    assert fake_account.withdraw_called is True
