from domain.account import Account
from domain.money import Money

def test_account_deposit():
    acc = Account(1, "User", Money(100, "USD"))

    acc.deposit(Money(50, "USD"))

    assert acc.balance.amount == 150


def test_account_withdraw():
    acc = Account(1, "User", Money(100, "USD"))

    acc.withdraw(Money(30, "USD"))

    assert acc.balance.amount == 70
