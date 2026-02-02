from domain.account import Account
from domain.money import Money


class CreditAccount(Account):
    """
    Specialized Account that allows negative balance up to a credit limit.
    """

    def __init__(
        self,
        account_id: int,
        owner_name: str,
        opening_balance: Money,
        credit_limit: float,
    ):
        if credit_limit < 0:
            raise ValueError("credit limit must be non-negative")

        super().__init__(account_id, owner_name, opening_balance)
        self._credit_limit = credit_limit

    def withdraw(self, money: Money) -> None:
        if not isinstance(money, Money):
            raise TypeError("withdraw requires Money")

        new_amount = self.balance.amount - money.amount

        if new_amount < self._credit_limit:
            raise ValueError("Credit limit exceeded")

        new_balance = Money(new_amount, self.balance.currency)
        self._change_balance(new_balance, f"Withdrew {money} (credit)")
