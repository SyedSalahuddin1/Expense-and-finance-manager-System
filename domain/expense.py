from domain.money import Money


class Expense:
    """
    Domain action representing an expense applied to an account
    using a specific strategy.
    """

    def __init__(self, money: Money, strategy):
        if not isinstance(money, Money):
            raise TypeError("Expense requires Money")

        if not hasattr(strategy, "apply"):
            raise TypeError("strategy must implement apply(account, money)")

        self._money = money
        self._strategy = strategy

    @property
    def money(self) -> Money:
        return self._money

    def apply_to(self, account) -> None:
        """
        Delegates expense application to its strategy.
        """
        self._strategy.apply(account, self._money)

    def __repr__(self) -> str:
        return f"<Expense {self._money}>"
