from domain.money import Money


class Account:
    """
    Domain Entity representing a financial account.
    Owns balance state and balance transition rules.
    """

    def __init__(self, account_id: int, owner_name: str, opening_balance: Money):
        if not isinstance(opening_balance, Money):
            raise TypeError("opening_balance must be a Money instance")

        self._id = account_id
        self._owner_name = owner_name
        self._balance = opening_balance
        self._observers = []

    # ---------- Identity & State (Read-only) ----------

    @property
    def id(self) -> int:
        return self._id

    @property
    def owner_name(self) -> str:
        return self._owner_name

    @property
    def balance(self) -> Money:
        return self._balance

    # ---------- Observer Management ----------

    def add_observer(self, observer) -> None:
        self._observers.append(observer)

    def _notify(self, message: str) -> None:
        for observer in self._observers:
            observer.notify(self, message)

    # ---------- Internal Balance Transition ----------

    def _change_balance(self, new_balance: Money, reason: str) -> None:
        """
        Single internal authority for changing balance.
        """
        if not isinstance(new_balance, Money):
            raise TypeError("new_balance must be Money")

        self._balance = new_balance
        self._notify(reason)

    # ---------- Public Domain Behaviors ----------

    def deposit(self, money: Money) -> None:
        if not isinstance(money, Money):
            raise TypeError("deposit requires Money")

        new_balance = self._balance.add(money)
        self._change_balance(new_balance, f"Deposited {money}")

    def withdraw(self, money: Money) -> None:
        if not isinstance(money, Money):
            raise TypeError("withdraw requires Money")

        new_balance = self._balance.subtract(money)
        self._change_balance(new_balance, f"Withdrew {money}")

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} "
            f"id={self.id}, owner='{self.owner_name}', "
            f"balance={self.balance}>"
        )
