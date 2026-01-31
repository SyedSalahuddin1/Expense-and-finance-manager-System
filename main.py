from domain import account
from domain.money import Money 
from domain.expense import Expense
from strategies.expense_strategy import ExpenseStrategy
from repositories.account_repository import AccountRepository
from services.expense_service import ExpenseService
from observer.account_observer import ConsoleLogger
from factories.account_factory import AccountFactory
from tests.test_money import NormalExpense

repo = AccountRepository()
factory = AccountFactory()

savings = factory.create(
    kind= "savings",
    account_id = 1,
    owner_name = "Salahuddin",
    opening_balance = Money(1000, "INR"),
    interest_rate = 0.05
    )

logger = ConsoleLogger()
savings.add_observer(logger)

repo.add(savings)

service = ExpenseService(repo)
expense = Expense(Money(200, "INR"), NormalExpense())

print(savings)
