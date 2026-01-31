from domain.money import Money
from domain.expense import Expense
from strategies.expense_strategy import NormalExpenseStrategy
from repositories.account_repository import AccountRepository
from services.expense_service import ExpenseService
from observer.account_observer import ConsoleAccountObserver
from factories.account_factory import AccountFactory


def main():
    # ----- Infrastructure -----
    account_repository = AccountRepository()
    account_factory = AccountFactory()
    observer = ConsoleAccountObserver()

    # ----- Accounts -----
    savings_account = account_factory.create(
        kind="savings",
        account_id=1,
        owner_name="Salahuddin",
        opening_balance=Money(1000, "USD"),
        interest_rate=0.05,
    )

    credit_account = account_factory.create(
        kind="credit",
        account_id=2,
        owner_name="Ahmed",
        opening_balance=Money(0, "USD"),
        credit_limit=500,
    )

    savings_account.add_observer(observer)
    credit_account.add_observer(observer)

    account_repository.add(savings_account)
    account_repository.add(credit_account)

    # ----- Application Services -----
    expense_service = ExpenseService(account_repository)

    # ----- Use Case Execution -----
    expense = Expense(
        money=Money(200, "USD"),
        strategy=NormalExpenseStrategy(),
    )

    expense_service.apply_expense(1, expense)
    expense_service.apply_expense(2, expense)

    # ----- CLI Output -----
    for account in account_repository.list_all():
        print(account)


if __name__ == "__main__":
    main()
