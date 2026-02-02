from domain.account import Account
from domain.money import Money


class SavingsAccount(Account):
    """
    Specialized Account that supports interest application.
    """

    def __init__(
        self,
        account_id: int,
        owner_name: str,
        opening_balance: Money,
        interest_rate: float,
    ):
        if interest_rate < 0:
            raise ValueError("interest rate must be non-negative")

        super().__init__(account_id, owner_name, opening_balance)
        self._interest_rate = interest_rate

    def apply_interest(self) -> None:
        """
        Applies interest to the account balance.
        Delegates balance mutation to base Account.
        """
        interest_amount = Money(
            self.balance.amount * self._interest_rate,
            self.balance.currency,
        )
        self.deposit(interest_amount)
