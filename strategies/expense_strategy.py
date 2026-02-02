from abc import ABC, abstractmethod
from domain.money import Money


class ExpenseStrategy(ABC):
    """
    Strategy interface defining how an expense is applied to an account.
    """

    @abstractmethod
    def apply(self, account, money: Money) -> None:
        """
        Applies the given money to the account.
        """
        raise NotImplementedError


class NormalExpenseStrategy(ExpenseStrategy):
    """
    Applies an expense without modification.
    """

    def apply(self, account, money: Money) -> None:
        account.withdraw(money)


class TaxedExpenseStrategy(ExpenseStrategy):
    """
    Applies an expense with an additional tax.
    """

    def __init__(self, tax_rate: float):
        if tax_rate < 0:
            raise ValueError("tax rate must be non-negative")

        self._tax_rate = tax_rate

    def apply(self, account, money: Money) -> None:
        tax_amount = money.amount * self._tax_rate
        total = Money(money.amount + tax_amount, money.currency)
        account.withdraw(total)
